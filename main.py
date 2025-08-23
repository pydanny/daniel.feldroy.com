import air
import yaml
import collections, functools, pathlib, json, csv
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from air.responses import RedirectResponse
from fastapi.responses import Response
from fastapi import HTTPException
from dateutil import parser
import pytz
from os import getenv
from fastapi.responses import HTMLResponse
from pyinstrument import Profiler

PROFILING = True  # Set this from a settings model


if getenv('RAILWAY_PUBLIC_DOMAIN'):
    app = air.Air()

    @app.get('/')
    def everything():
        return RedirectResponse('https://daniel.fastapicloud.dev')

    @app.get('/{path:path}')
    def everything(path: pathlib.Path):
        return RedirectResponse(f'https://daniel.fastapicloud.dev/{path}')

else:


    def Page404(request: air.Request, exc: Exception) -> air.AirResponse:
        return Layout(
            air.Title("404 Not Found"),
            air.H1("404 Not Found"),
            air.P("The page you are looking for does not exist."),
            title="404 not found",
            description="404 not found",
            status_code=404,
        )

    # import sentry_sdk

    # sentry_sdk.init(
    #     dsn=getenv('SENTRY_DSN'),
    #     # Add data like request headers and IP for users,
    #     # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    #     send_default_pii=True,
    # )


    app = air.Air(exception_handlers={404: Page404})

    # Mount static files for CSS
    app.mount("/public", StaticFiles(directory="public"), name="public")    

    if PROFILING:
        @app.middleware("http")
        async def profile_request(request: air.Request, call_next):
            profiling = request.query_params.get("blarg", False)
            if profiling:
                profiler = Profiler()
                profiler.start()
                await call_next(request)
                profiler.stop()
                return HTMLResponse(profiler.output_html())
            else:
                return await call_next(request)    

    default_social_image = "https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg"

    redirects = json.loads(pathlib.Path(f"redirects.json").read_text())


    # The next block of code is several date utilities
    # We need these because I've been sloppy about defining dates
    # TODO: Fix datetimes in all markdown files so this wouldn't be necessary
    def convert_dtstr_to_dt(date_str: str) -> datetime:
        """
        Convert a naive or non-naive date/datetime string to a datetime object.
        Naive datetime strings are assumed to be in GMT (UTC) timezone.
        """
        try:
            dt = parser.parse(date_str)
            if dt.tzinfo is None:
                # If the datetime object is naive, set it to GMT (UTC)
                dt = dt.replace(tzinfo=pytz.UTC)
            return format_datetime(dt)
        except (ValueError, TypeError) as e:
            return ""


    def format_datetime(dt: datetime) -> str:
        """Format the datetime object"""
        if dt is None:
            return ""
        formatted_date = dt.strftime("%B %d, %Y")
        formatted_time = dt.strftime("%I:%M%p").lstrip("0").lower()
        return f"{formatted_date} at {formatted_time}"


    class ContentNotFound(Exception):
        pass


    # The following functions are three content loading. They are cached in
    # memory to boost the speed of the site. In production at a minumum the
    # app is restarted every time the project is deployed.
    @functools.cache
    def list_posts(
        published: bool = True, posts_dirname="posts", content=False
    ) -> list[dict]:
        """
        Loads all the posts and their frontmatter.
        Note: Could use pathlib better
        """
        posts: list[dict] = []
        for post in pathlib.Path(".").glob(f"{posts_dirname}/**/*.md"):
            raw: str = post.read_text().split("---")[1]
            data: dict = yaml.safe_load(raw)
            data["slug"] = post.stem
            data["class_"] = "marked"
            if content:
                data["content"] = "\n".join(post.read_text().split("---")[2:])
            posts.append(data)

        posts.sort(key=lambda x: x["date"], reverse=True)
        return [x for x in filter(lambda x: x["published"] is published, posts)]


    @functools.lru_cache
    async def get_post(slug: str) -> tuple | None:
        posts = list_posts(content=True)
        post = next((x for x in posts if x["slug"] == slug), None)
        if post is None:
            raise ContentNotFound
        return (post["content"], post)


    @functools.cache
    async def list_tags() -> dict[str, int]:
        unsorted_tags = {}
        for post in list_posts():
            page_tags = post.get("tags", [])
            for tag in page_tags:
                if tag in unsorted_tags:
                    unsorted_tags[tag] += 1
                else:
                    unsorted_tags[tag] = 1

        tags: dict = collections.OrderedDict(
            sorted(unsorted_tags.items(), key=lambda x: x[1], reverse=True)
        )
        return tags


    def TagLink(slug: str):
        return air.Span(air.A(slug, href=f"/tags/{slug}"), " ")


    def TagLinkWithCount(slug: str, count: int):
        return air.Span(
            air.A(air.Span(slug), air.Small(f" ({count})"), href=f"/tags/{slug}"), " "
        )


    def BlogPostPreview(title: str, slug: str, timestamp: str, description: str):
        """
        This renders a blog posts short display used for the index, article list, and tags.
        """
        return air.Span(
            air.H2(air.A(title, href=f"/posts/{slug}")),
            air.P(
                description, air.Br(), air.Small(air.Time(convert_dtstr_to_dt(timestamp)))
            ),
        )


    def TILPreview(title: str, slug: str, timestamp: str, description: str):
        return air.Span(
            air.H3(air.A(title[4:], href=f"/posts/{slug}")),
            air.P(air.Small(air.Time(convert_dtstr_to_dt(timestamp)))),
        )


    def MarkdownPage(slug: str):
        """Renders a non-sequential markdown file"""
        try:
            text = pathlib.Path(f"pages/{slug}.md").read_text()
        except FileNotFoundError:
            raise HTTPException(status_code=404)
        content = "".join(text.split("---")[2:])
        metadata = yaml.safe_load(text.split("---")[1])
        date = metadata.get("date", "")
        return Layout(
            air.Title(metadata.get("title", slug)),
            air.Section(
                air.H1(metadata.get("title", "")),
                air.P(
                    metadata.get("author", ""),
                    air.Br(),
                    air.Small(air.Time(date)),
                ),
                air.Div(content, class_="marked"),
            ),
            title=metadata.get("title", slug),
            description=metadata.get("description", "slug"),
            url=f"https://daniel.feldroy.com/{slug}",
            image=metadata.get("image", default_social_image),
        )


    def Socials(title, description, image, twitter_image, url):
        return [
            air.Meta(property="og:image", content=image),
            air.Meta(property="og:site_name", content="https://daniel.feldroy.com"),
            air.Meta(property="og:image:type", content="image/png"),
            air.Meta(property="og:type", content="website"),
            air.Meta(property="og:url", content=url),
            air.Meta(property="og:title", content=title),
            air.Meta(property="og:description", content=description),
            air.Meta(name="twitter:image", content=twitter_image),
            air.Meta(name="twitter:card", content="summary"),
            air.Meta(name="twitter:title", content=title),
            air.Meta(name="twitter:description", content=description),
            air.Link(rel="canonical", href=url),
        ]
        return


    def Layout(
        *children,
        title="Daniel Roy Greenfeld",
        description="Daniel Roy Greenfeld's personal blog",
        image="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg",
        twitter_image="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg",
        url="http://daniel.feldroy.com/",
        status_code=200,
    ) -> air.AirResponse:
        "Generic layout for pages"
        body_children = air.layouts.filter_body_tags(children)
        return air.AirResponse(
            air.Html(
                air.Head(
                    *Socials(title, description, image, twitter_image, url),
                    air.Link(
                        rel="stylesheet",
                        href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
                    ),
                    air.Script(
                        src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js",
                        integrity="sha384-Akqfrbj/HpNVo8k11SXBb6TlBWmXXlYQrCSqEWmyKJe+hDm3Z/B2WVG4smwBkRVm",
                        crossorigin="anonymous",
                    ),
                    air.Style(":root { --pico-font-size: 100%; }"),
                    air.Link(
                        rel="stylesheet",
                        href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/atom-one-dark.css",
                        media="(prefers-color-scheme: dark)",
                    ),
                    air.Link(
                        rel="stylesheet",
                        href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/atom-one-light.css",
                        media="(prefers-color-scheme: light)",
                    ),
                    air.Script(src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"),
                    air.Script(
                        src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
                    ),
                    air.Script(
                        src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/python.min.js"
                    ),
                    air.Script(
                        src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/javascript.min.js"
                    ),
                    air.Script(
                        src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/html.min.js"
                    ),
                    air.Script(
                        src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/css.min.js"
                    ),
                    air.Script(src="/public/render.js"),
                    air.Link(rel="stylesheet", href="/public/style.css", type="text/css"),
                    *air.layouts.filter_head_tags(children),
                ),
                air.Body(
                    air.Header(
                        air.A(
                            air.Img(
                                class_="borderCircle",
                                alt="Daniel Roy Greenfeld",
                                src="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg",
                                width="108",
                                height="108",
                            ),
                            href="/",
                        ),
                        air.A(air.H2("Daniel Roy Greenfeld"), href="/"),
                        air.P(
                            air.A("About", href="/about"),
                            " | ",
                            air.A("Articles", href="/posts"),
                            " | ",
                            air.A("Books", href="/books"),
                            " | ",
                            air.A("Jobs", href="/jobs"),
                            " | ",
                            air.A("Tags", href="/tags"),
                            " | ",
                            air.A("Search", href="/search"),
                        ),
                        style="text-align: center;",
                    ),
                    air.Main(*air.layouts.filter_body_tags(children), class_="container"),
                    air.Footer(
                        air.Hr(),
                        air.P(
                            air.A(
                                "LinkedIn",
                                href="https://www.linkedin.com/in/danielfeldroy/",
                            ),
                            " | ",
                            air.A(
                                "Bluesky",
                                href="https://bsky.app/profile/daniel.feldroy.com",
                            ),
                            " | ",
                            air.A("Twitter", href="https://twitter.com/pydanny"),
                            " | ",
                            air.A("Github", href="https://github.com/pydanny"),
                            " | ",                        
                            "Feeds: ",
                            air.A("All", href="/feeds/atom.xml"),
                            ", ",
                            air.A("Python", href="/feeds/python.atom.xml"),
                            ", ",
                            air.A("TIL", href="/feeds/til.atom.xml"),
                        ),
                        air.P(
                            f"All rights reserved {datetime.now().year}, Daniel Roy Greenfeld"
                        ),
                        class_="container",
                    ),
                    air.Dialog(
                        air.Header(
                            air.H2("Search"),
                            air.Input(
                                name="q",
                                type="text",
                                id="search-input",
                                hx_trigger="keyup",
                                placeholder="Enter your search query...",
                                hx_get="/search-results",
                                hx_target=".search-results-modal",
                            ),
                            air.Div(class_="search-results-modal"),
                            class_="modal-content",
                        ),
                        id="search-modal",
                        style="display:none;",
                        class_="modal overflow-auto",
                    ),
                    air.Div(hx_trigger="keyup[key=='/'] from:body"),
                    air.Script("""
                document.body.addEventListener('keydown', e => {
                if (e.key === '/') {
                    e.preventDefault();
                    document.getElementById('search-modal').style.display = 'block';
                    document.getElementById('search-input').focus();
                }
                if (e.key === 'Escape') {
                    document.getElementById('search-modal').style.display = 'none';
                }
                });

                document.getElementById('search-input').addEventListener('input', e => {
                htmx.trigger('.search-results', 'htmx:trigger', {value: e.target.value});
                });
                """),
                ),
            ).render(),
            status_code=status_code,
        )


    @app.page
    async def index():
        all_posts = list_posts()
        most_posts = [
            BlogPostPreview(
                title=x["title"],
                slug=x["slug"],
                timestamp=x["date"],
                description=x.get("description", ""),
            )
            for x in all_posts
            if "TIL" not in x.get("tags")
        ]
        popular = [
            BlogPostPreview(
                title=x["title"],
                slug=x["slug"],
                timestamp=x["date"],
                description=x.get("description", ""),
            )
            for x in all_posts
            if x.get("popular", False)
        ]
        tils = [
            TILPreview(
                title=x["title"], slug=x["slug"], timestamp=x["date"], description=""
            )
            for x in all_posts
            if "TIL" in x.get("tags")
        ]
        return Layout(
            air.Title("Daniel Roy Greenfeld"),
            air.Div(
                air.Section(
                    air.H1("Recent Writings"),
                    *most_posts[:4],
                    air.P(air.A("Read all articles", href=posts)),
                ),
                air.Section(
                    air.H1("TIL", air.Small(" (Today I learned)")),
                    *tils[:7],
                    air.P(air.A("Read more TIL articles", href="/tags/TIL")),
                ),
                air.Section(air.H1("Popular Writings"), *popular),
                class_="grid",
            ),
        )


    @app.page
    async def posts():
        duration = round((datetime.now() - datetime(2005, 9, 3)).days / 365.25, 2)
        description = (
            f"Everything written by Daniel Roy Greenfeld for the past {duration} years."
        )
        posts = [
            BlogPostPreview(
                title=x["title"],
                slug=x["slug"],
                timestamp=x["date"],
                description=x.get("description", ""),
            )
            for x in list_posts()
        ]
        return Layout(
            air.Title("All blog posts"),
            air.Section(
                air.H1(f"All Articles ({len(posts)})"),
                air.P(description),
                *posts,
                air.A("← Back to home", href="/"),
            ),
            title="All blog posts by Daniel Roy Greenfeld",
        )


    @app.get("/posts/{slug}")
    async def article(slug: str):
        try:
            content, metadata = get_post(slug)
        except ContentNotFound:
            redirects_url = redirects.get("posts/" + slug, None)
            if redirects_url is not None:
                return RedirectResponse(redirects_url)
            raise HTTPException(status_code=404)
        tags = [TagLink(slug=x) for x in metadata.get("tags", [])]
        specials = ()
        if "TIL" in metadata["tags"]:
            specials = air.A(
                air.Img(
                    src="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png",
                    alt="Today I Learned",
                    width="200",
                    height="200",
                    class_="center",
                ),
                href="/tags/TIL",
            )
        return Layout(
            air.Title(metadata["title"]),
            air.Section(
                air.H1(metadata["title"]),
                air.P(air.I(metadata.get("description", ""))),
                air.P(air.Small(air.Time(metadata["date"]))),
                air.Div(content, class_=metadata["class_"]),
                # air.Div(*specials, style="width: 200px; margin: auto; display: block;"),
                air.P(air.Span("Tags: "), *tags),
                air.A("← Back to all articles", href="/"),
            ),
            title=metadata["title"],
            description=metadata.get("description", ""),
            image=f"https://daniel.feldroy.com{metadata.get('image', default_social_image)}",
            url=f"https://daniel.feldroy.com/posts/{slug}",
        )


    @app.page
    async def tags():
        tags = [TagLinkWithCount(slug=x[0], count=x[1]) for x in list_tags().items()]
        return Layout(
            air.Title("Tags"),
            air.Section(
                air.H1("Tags"),
                air.P("All tags used in the blog"),
                *tags,
                air.Br(),
                air.Br(),
                air.A("← Back home", href="/"),
            ),
            title="Tags",
            description="All tags used in the site.",
        )


    @app.get("/tags/{slug}")
    async def tag(slug: str):
        posts = [
            BlogPostPreview(
                title=x["title"],
                slug=x["slug"],
                timestamp=x["date"],
                description=x.get("description", ""),
            )
            for x in list_posts()
            if slug in x.get("tags", [])
        ]
        return Layout(
            air.Title(f"Tag: {slug}"),
            air.Section(
                air.H1(f'Posts tagged with "{slug}" ({len(posts)})'),
                *posts,
                air.A("← Back home", href="/"),
            ),
            title=f"Tag: {slug}",
            description=f'Posts tagged with "{slug}" ({len(posts)})',
        )


    @functools.cache
    def _search(q: str = ""):
        def _s(obj: dict, name: str, q: str):
            content = obj.get(name, "")
            if isinstance(content, list):
                content = " ".join(content)
            return q.lower().strip() in str(content).lower().strip()

        messages = []
        articles = []
        posts = []
        description = f"No results found for '{q}'"
        if q.strip():
            posts = list_posts()
            # Search engine is list comprehension of a list of dicts
            # ranks = search_model.rank(q, L(posts).map(json.dumps), return_documents=True)
            # ranks = ranks[:10]
            # articles = L(ranks).attrgot('text').map(json.loads)
            # old engine
            articles = [
                x
                for x in posts
                if any(
                    _s(x, name, q) for name in ["title", "description", "content", "tags"]
                )
            ]
        if articles:
            # Build the posts for display
            posts = [
                BlogPostPreview(
                    title=x["title"],
                    slug=x["slug"],
                    timestamp=x["date"],
                    description=x.get("description", ""),
                )
                for x in articles
            ]
        if posts:
            messages = [
                air.H2(f"Search results on '{q}'"),
                air.P(f"Found {len(posts)} entries"),
            ]
            description = f"Search results on '{q}'"
        elif q.strip():
            messages = [air.P(f"No results found for '{q}'")]
        return air.Div(
            air.Meta(property="description", content=description),
            air.Meta(property="og:description", content=description),
            air.Meta(name="twitter:description", content=description),
            *messages,
            *posts,
        )


    @app.get("/search-results")
    async def search_results(q: str):
        return _search(q)


    @app.page
    async def search(q: str | None = None):
        result = []
        if q is not None:
            result.append(_search(q))
        return Layout(
            air.Title("Search"),
            air.Form(
                air.Fieldset(
                    air.Input(name="q", id="q", value=q, type="search", autofocus=True),
                    air.Button(
                        "Search",
                        hx_get="/search-results",
                        hx_target=".search-results",
                        hx_include="#q",
                        onclick="updateQinURL()",
                    ),
                    class_="center",
                    role="group",
                )
            ),
            air.Section(
                air.Div(*result, class_="search-results"),
                air.P(air.Small('Hint: Use the "/" shortcut to search from any page.')),
                air.A("← Back home", href="/"),
            ),
            air.Script("""function updateQinURL() {
                let url = new URL(window.location);
                const value = document.getElementById('q').value
                url.searchParams.set('q', value);
                window.history.pushState({}, '', url);            
            };
            """),
            title="Search the site",
            description="",
        )


    @app.get("/feeds/{slug}.xml")
    async def atom_feed(slug: str):
        path = pathlib.Path(f"public/feeds/{slug}.xml")
        if path.exists():
            return Response(path.read_text(), media_type="application/xml")
        raise HTTPException(status_code=404)


    def convert_minutes(total_minutes):
        hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        return hours, remaining_minutes


    @app.page
    async def fitness():
        with open("fitness.csv") as f:
            rows = [o for o in csv.DictReader(f)]

        dates = collections.defaultdict(list)
        for row in rows:
            dates[row["Date"][:7]].append(row)

        current_weight = rows[0]["Weight"]        


        config = {"responsive": True}
        config = json.dumps(config)

        charts = []
        for month, rows in dates.items():
            month_str = datetime.strptime(month, "%Y-%m").strftime("%B %Y")
            fitness = [
                {
                    "type": "bar",
                    "x": [o["Date"] for o in rows],
                    "y": [o["Weight"] for o in rows],
                    "text": [o["Weight"] for o in rows],
                    "textposition": "auto",
                    "hoverinfo": "none",
                    "marker": {
                        "color": "blue",
                    },
                    "name": "Weight kg",
                },
                {
                    "type": "bar",
                    "x": [o["Date"] for o in rows],
                    "y": [o["BJJ"] for o in rows],
                    "text": [o["BJJ"] for o in rows],
                    "textposition": "auto",
                    "hoverinfo": "none",
                    "marker": {
                        "color": "green",
                    },
                    "name": "BJJ",
                },
                {
                    "type": "bar",
                    "x": [o["Date"] for o in rows],
                    "y": [o["Other"] for o in rows],
                    "text": [o["Other"] for o in rows],
                    "textposition": "auto",
                    "hoverinfo": "none",
                    "marker": {
                        "color": "red",
                    },
                    "name": "Other",
                },
            ]
            layout = {
                "title": {"text": month_str},
                "font": {"size": 18},
                "barcornerradius": 15,
            }

            layout = json.dumps(layout)
            chart_name = f"weightChart-{month}"
            charts.append(air.Div(id=chart_name))
            bjj_hours, bjj_minutes = convert_minutes(sum([int(o["BJJ"]) for o in rows]))
            other_hours, other_minutes = convert_minutes(
                sum([int(o["Other"]) for o in rows])
            )
            charts.append(
                air.Div(
                    air.H3(f"{month_str} Summary"),
                    air.P(
                        air.Strong("Weight: "),
                        f"{rows[-1]['Weight']} kg",
                        air.Br(),
                        air.Strong("Total BJJ:"),
                        f" {bjj_hours} hours, {bjj_minutes} minutes",
                        air.Br(),
                        air.Strong("Total Other:"),
                        f" {other_hours} hours, {other_minutes} minutes",
                    ),
                ),
            )
            charts.append(
                air.Script(f"Plotly.newPlot('{chart_name}', {fitness}, {layout}, {config});")
            )

        return Layout(
            air.Title("Fitness Tracking"),
            air.Script(src="https://cdn.plot.ly/plotly-2.32.0.min.js"),
            air.Section(
                air.P(
                    "Wt Goal: ",
                    air.Strong("77 kg / 169 lbs"),
                    air.Br(),
                    f"Current: {current_weight} kg / {round(float(current_weight) * 2.2, 2)} lb",
                ),
                air.H2(f"Fitness Tracking"),
                air.Ol(
                    air.Li("Weight kg is how much I weigh in kilograms."),
                    air.Li("BJJ is how many minutes of Brazilian Jiu-Jitsu in a day."),
                    air.Li(
                        "Other is how many minutes of other training done in a day, most often weights, ATG, walking at speed, sometimes alternative exercise like Yoga or Pilates."
                    ),
                ),
                *charts,
                air.A("← Back home", href="/"),
            ),        
            
        )


    @app.get("/writing-stats")
    async def writing_stats():
        years = collections.defaultdict(int)
        for post in list_posts():
            years[post["date"][:4]] += 1
        data = [
            {
                "x": list(map(int, years.keys())),
                "y": list(map(int, years.values())),
                "type": "scatter",
            }
        ]
        # data = json.dumps(data)

        config = {"responsive": True}
        config = json.dumps(config)
        layout = {
            "title": {"text": "Writing stats"},
            "font": {"size": 18},
            "barcornerradius": 15,
        }
        layout = json.dumps(layout)

        return Layout(
            air.Title("Writing Stats"),
            air.Script(src="https://cdn.plot.ly/plotly-2.32.0.min.js"),
            air.Div(id="post-counts"),
            air.Children(
            air.Script(f"Plotly.newPlot('post-counts', {data}, {layout}, {config});"),
            ),
            description="Numbers about my writing patterns",
        )

    @app.get('/.well-known/atproto-did')
    async def wellknown_atproto_did():
        # for bluesky!
        return air.responses.PlainTextResponse('did:plc:qmkhbnaaxxr7pcdkgdpis6pi')


    @app.get('/robots.txt')
    async def robots():
        return air.responses.PlainTextResponse(pathlib.Path('robots.txt').read_text())

    @app.page
    async def blarg():
        return 1/0


    @app.get("/{slug}")
    async def page_or_redirect1(slug: str):
        redirects_url = redirects.get(slug, None)
        if redirects_url is not None:
            return RedirectResponse(redirects_url)    
        try:
            return MarkdownPage(slug)    
        except TypeError:
            raise HTTPException(status_code=404)


    @app.get("/{slug_1}/{slug_2}")
    async def page_or_redirect2(slug_1: str, slug_2: str):
        redirects_url = redirects.get(slug_1 + "/" + slug_2, None)
        if redirects_url is not None:
            return RedirectResponse(redirects_url)
        try:
            return MarkdownPage(slug_1 + "/" + slug_2)
        except TypeError:
            raise HTTPException(status_code=404)


