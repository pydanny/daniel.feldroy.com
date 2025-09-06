import air
from os import getenv
from layouts import Layout
from models import Subscription, async_session
from rich import print
from datetime import datetime
from sqlmodel import select
from mailgun.client import Client as MailgunClient

router = air.AirRouter()

if getenv("RAILWAY_PUBLIC_DOMAIN"):
    # Production setting
    def print(x):
        pass

    DOMAIN = "https://feldroy.com"
else:
    # local dev
    from rich import print

    DOMAIN = "localhost:8000"

# mailgun config
mg_key: str = getenv('MAILGUN_API_KEY', '')
mg_client: MailgunClient = MailgunClient(auth=("api", mg_key))    

MAILSERVER = getenv('MAILSERVER', 'mailhog')


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



def post_email(to: str, subject: str, text: str, html: str, mailserver: str='mailhog') -> None:

    data = {
        "from": 'hi@feldroy.com',
        "to": to,
        "subject": subject,
        "text": text,
        "html": html,
        "o:tag": "Python test",
    }    
    # Messages
    # POST /<domain>/messages
    if mailserver == 'mailgun':
        # do mailgun
        req = mg_client.messages.create(data=data, domain='mg.feldroy.com')
        return req
    else:
        # do mailhog
        pass


def send_subscription_email(email, initial=True):
    if initial:
        post_email(email, subject="A confirmation email", text='', html=air.Tag(air.H1('Another email confirmation')).render(), mailserver='mailgun')
    else:
        post_email(email, subject="We're sending another confirmation email ", text='', html=air.Tag(air.H1('Another email confirmation')).render(), mailserver='mailgun')



async def save_subscription(email):

    session = async_session()
    statement = select(Subscription).where(Subscription.email==email)
    obj = await session.exec(statement)
    subscription = obj.first()
    if subscription is None:
        subscription = Subscription(email=email)    
        session.add(subscription)
        await session.commit()
        send_subscription_email(email)
        print('[green bold]subscription saved![/green bold]')
    else:
        # Already in the system, email again, and increment the subscribe attempts by 1
        # let the user know
        subscription.attempts_to_subscribe += 1
        subscription.updated_at = datetime.now()
        session.add(subscription)
        await session.commit()
        send_subscription_email(email)
        print("[red bold]In the system already, let's send them the email again[/red bold]") 
    

@router.post('/subscribe')
async def subscribe(request: air.Request, background_tasks: air.BackgroundTasks):
    form = await request.form()
    email = form.get('email')
    if email.strip():
        background_tasks.add_task(save_subscription, email)
    return air.Article(air.P('Check your email (and your spam folder) for a confirmation email which should arrive in the next few minutes.'), id='form', hx_swap_oob='true')
