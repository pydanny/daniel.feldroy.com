import air
from layouts import Layout
from models import Subscription, async_session
from rich import print

router = air.AirRouter()


@router.page
def mailing_list():
    title = 'Sign up for the feldroy.com mailing list'
    return Layout(
        air.Title(title),
        air.Section(air.H1(title)),
        air.Article(
            air.P('Software projects, books I write or work on, open source, and more.'),
            air.Form(
                air.Fieldset(
                    air.Input(
                        name="email",
                        type="email",
                        placeholder="Enter your email",
                        autocomplete="email",
                        required=True,
                        autofocus=True
                    ),
                    air.Input(type="submit", value="Subscribe"),
                    role="group",
                ),
                hx_post='/subscribe',                                    
            ),
            air.P(air.Small('By subscribing you agree to receive periodic emails from feldroy.com, which is just me and my wife/partner Audrey.')),                     
            id='form' 
        ),
        title=title,
        description=''
    )

async def save_subscription(email):
    session = async_session()
    subscription = Subscription(email=email)    
    session.add(subscription)
    await session.commit()
    print('[green bold]subscription saved![/green bold]')



@router.post('/subscribe')
async def subscribe(request: air.Request, background_tasks: air.BackgroundTasks):
    form = await request.form()
    email = form.get('email')
    if email.strip():
        background_tasks.add_task(save_subscription, email)
    return air.Article(air.P('Check your email (and your spam folder) for a confirmation email which should arrive in the next few minutes.'), id='form', hx_swap_oob='true')
