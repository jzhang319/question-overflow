from app.models import db, Question, environment, SCHEMA
from sqlalchemy import text

def seed_questions():
    static_url_prefix = '/images/'

    demo = Question(
        user_id=1, question="how do i bathe", detail="people say i stink and say that i should bathe", url=f'{static_url_prefix}image1.png'
    )
    demo1 = Question(
        user_id=2, question="how to what", detail="dont know what to do most of the time", url=f'{static_url_prefix}image2.png'
    )
    demo2 = Question(
        user_id=3, question="how to when", detail="people say i have no concept of time, it's true", url=f'{static_url_prefix}image3.png'
    )
    demo3 = Question(
        user_id=1, question="What is a Stack Overflow?", detail="just wondering", url=f'{static_url_prefix}image4.png'
    )
    demo4 = Question(
        user_id=1, question="How do I search for a specific question on Stack Overflow?", detail="beginner question", url=f'{static_url_prefix}image5.png'
    )
    demo5 = Question(
        user_id=1, question="Is Stack Overflow free to use?", detail="more beginner question1", url=f'{static_url_prefix}image6.png'
    )
    demo6 = Question(
        user_id=1, question="How do I ask a question on Stack Overflow?", detail="more beginner question1", url=f'{static_url_prefix}image7.png'
    )
    demo7 = Question(
        user_id=1, question="What are tags on Stack Overflow?", detail="more beginner question1", url=f'{static_url_prefix}image8.png'
    )
    demo8 = Question(
        user_id=1, question="How do I post an answer to a question on Stack Overflow?", detail="more beginner question1", url=f'{static_url_prefix}image9.png'
    )
    demo9 = Question(
        user_id=1, question="What is the difference between a cell phone and a smartphone?", detail="more beginner question1", url=f'{static_url_prefix}image10.png'
    )

    db.session.add(demo)
    db.session.add(demo1)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.add(demo4)
    db.session.add(demo5)
    db.session.add(demo6)
    db.session.add(demo7)
    db.session.add(demo8)

    db.session.commit()


def undo_questions():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM questions"))

    db.session.commit()
