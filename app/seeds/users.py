from app.models import db, User, environment, SCHEMA
from sqlalchemy import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1235671323729203321/Z.png?ex=66353819&is=6633e699&hm=64c4cf8b36be9366cb178bad0ee30b7f39148c80711cc6d735eb8f8ecaa83ada&')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1235671445661814844/E3iyNtMQ1ksOp1N7mEBY0USRiJW2kvuv3eajzY7sIIgSLHdjBe9frdRbuSckhkIf8Hv1E2luXy6qsAAAAASUVORK5CYII.png?ex=66353836&is=6633e6b6&hm=b4d86434cb61effd49f58afc201be373d38d9966264bb425df65d580308c03ea&')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1235671582681075823/images.png?ex=66353856&is=6633e6d6&hm=345584951bd6b9353f6e1f8289cfeeeb1a62569ff7ff315560e79aa56763171b&')
    dave = User(
        username='dave', email='dave@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1235671483582382191/images.png?ex=6635383f&is=6633e6bf&hm=30c10b8a208db5e165566dab835e13ad1410dc082313e5cae1892cdfeb31e007&')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(dave)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
