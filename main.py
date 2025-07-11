import air
import yaml
import collections, functools, pathlib, json, csv
from datetime import datetime
from fastapi.staticfiles import StaticFiles

app  = air.Air()

# Mount static files for CSS
app.mount("/public", StaticFiles(directory='public'), name="public")


class ContentNotFound(Exception): pass


# The following functions are three content loading. They are cached in
# memory to boost the speed of the site. In production at a minumum the
# app is restarted every time the project is deployed.
@functools.cache
def list_posts(published: bool = True, posts_dirname="posts", content=False) -> list[dict]:
    """
    Loads all the posts and their frontmatter.
    Note: Could use pathlib better
    """
    posts: list[dict] = []
    for post in pathlib.Path('.').glob(f"{posts_dirname}/**/*.md"):
        raw: str = post.read_text().split("---")[1]
        data: dict = yaml.safe_load(raw)
        data["slug"] = post.stem
        data['class_'] = 'marked'
        if content:
            data["content"] = '\n'.join(post.read_text().split("---")[2:])
        posts.append(data)

    posts.sort(key=lambda x: x["date"], reverse=True)
    return [x for x in filter(lambda x: x["published"] is published, posts)]

@functools.lru_cache
def get_post(slug: str) -> tuple|None:
    posts = list_posts(content=True)
    post = next((x for x in posts if x["slug"] == slug), None)
    if post is None: raise ContentNotFound
    return (post['content'], post)


def BlogPostPreview(title: str, slug: str, timestamp: str, description: str):
    """
    This renders a blog posts short display used for the index, article list, and tags.
    """
    return air.Span(
                air.H2(air.A(title, href=f"/posts/{slug}")),
                air.P(description, air.Br(), air.Small(air.Time(timestamp))))

def TILPreview(title: str, slug: str, timestamp: str, description: str):
    return air.Span(
                air.H3(air.A(title[4:], href=f"/posts/{slug}")),
                air.P(air.Small(air.Time(timestamp)))
        )   

def Socials(
        title,
        description,
        image,
        twitter_image):
    return [
        air.Meta(property='og:image', content=image),
        air.Meta(property='og:site_name', content='https://daniel.feldroy.com'),
        air.Meta(property='og:image:type', content='image/png'),
        air.Meta(property='og:type', content='website'),
        air.Meta(property='og:url', content='https://daniel.feldroy.com'),
        air.Meta(property='og:title', content=title),
        air.Meta(property='og:description', content=description),
        air.Meta(name='twitter:image', content=twitter_image),
        air.Meta(name='twitter:card', content='summary'),
        air.Meta(name='twitter:title', content=title),
        air.Meta(name='twitter:description', content=description),
        air.Link(rel='canonical', href='http://daniel.feldroy.com/'),  
    ]
    return

def Layout(
        *children,
        title='Daniel Roy Greenfeld',
        description="Daniel Roy Greenfeld's personal blog",
        image='https://daniel.feldroy.com/public/images/profile.jpg',
        twitter_image='https://daniel.feldroy.com/public/images/profile.jpg',
           ):
    "Generic layout for pages"
    head_children = air.layouts.filter_head_tags(children)
    body_children = air.layouts.filter_body_tags(children)
    return air.Html(
        air.Head(
            *Socials(title,description,image,twitter_image),

            air.Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
            ),     
            air.Script(
                src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js",
                integrity="sha384-Akqfrbj/HpNVo8k11SXBb6TlBWmXXlYQrCSqEWmyKJe+hDm3Z/B2WVG4smwBkRVm",
                crossorigin="anonymous",
            ),
            air.Link(rel='stylesheet', href='/public/style.css', type='text/css'),
            *head_children,
        ),
        air.Body(
            air.Header(
                    air.A(air.Img(
                        class_='borderCircle', alt='Daniel Roy Greenfeld', src='/public/images/profile.jpg', width='108', height='108')
                        , href='/'),
                    air.A(air.H2('Daniel Roy Greenfeld'), href="/"),
                    air.P(
                        air.A('About', href='/about'),' | ', 
                        air.A('Articles', href='/posts'), ' | ',
                        air.A('Books', href='/books'), ' | ',
                        air.A('Jobs', href='/jobs'), ' | ',
                        air.A('Tags', href='/tags'), ' | ',
                        air.A('Search', href='/search')
                    ), style="text-align: center;"
                ),            
            air.Main(
                *body_children,
                class_="container"  
            ),
            air.Footer(air.Hr(), air.P(
                        air.A('LinkedIn', href='https://www.linkedin.com/in/danielfeldroy/'), ' | ',    
                        air.A('Bluesky', href='https://bsky.app/profile/daniel.feldroy.com'), ' | ',
                        air.A('Twitter', href='https://twitter.com/pydanny'), ' | ',             
                        'Feeds: ',
                        air.A('All', href='/feeds/atom.xml'), ', ' , 
                        air.A('Python', href='/feeds/python.atom.xml'), ', ' ,
                        air.A('TIL', href='/feeds/til.atom.xml')
                    ),
                    air.P(f'All rights reserved {datetime.now().year}, Daniel Roy Greenfeld'),
                    class_='container'
                ),
            air.Dialog(
                air.Header(
                    air.H2('Search'),            
                    air.Input(name='q', type='text', id='search-input', hx_trigger="keyup", placeholder='Enter your search query...', hx_get='/search-results', hx_target='.search-results-modal'),
                    air.Div(class_='search-results-modal'),
                    class_='modal-content'
                ),
                id='search-modal',
                style='display:none;',
                class_='modal overflow-auto'
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
            """)                      
        )
    ).render()





@app.page
def index():
    all_posts = list_posts()
    most_posts = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in all_posts if 'TIL' not in x.get('tags')]
    popular = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in all_posts if x.get("popular", False)]    
    tils = [TILPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description='') for x in all_posts if 'TIL' in x.get('tags')]        
    return Layout(
        air.Title('Daniel Roy Greenfeld'),
        air.Div(
            air.Section(
                    air.H1('Recent Writings'),
                    *most_posts[:4],
                    air.P(air.A('Read all articles', href=posts))
                ),          
            air.Section(
                    air.H1('TIL', air.Small(' (Today I learned)')),
                    *tils[:7],
                    air.P(air.A('Read more TIL articles', href='/tags/TIL'))
                ),
            air.Section(
                    air.H1('Popular Writings'),
                    *popular
            ),     
            class_="grid"            
        )
    )

@app.page
def posts():
    posts = list_posts()
    duration = round((datetime.now() - datetime(2005, 9, 3)).days / 365.25, 2)
    description = f'Everything written by Daniel Roy Greenfeld for the past {duration} years.'
    posts = [BlogPostPreview(title=x["title"],slug=x["slug"],timestamp=x["date"],description=x.get("description", "")) for x in list_posts()]
    return Layout(
        air.Title('All blog posts'),
        air.Section(
                air.H1(f'All Articles ({len(posts)})'),
                air.P(description),
                *posts,
                air.A("← Back to home", href="/"),
        ),
        title='All blog posts by Daniel Roy Greenfeld'
    )