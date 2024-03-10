from app.models import db, User, environment, SCHEMA
from sqlalchemy import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1216252913798877254/profile_image-1.jpeg?ex=65ffb6cb&is=65ed41cb&hm=bf8805106f1010c50f2a13931af3965be4895b0280b54d60b31ea6bc0f0a1e6a&')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1216252963706896535/profile_image-2.png?ex=65ffb6d7&is=65ed41d7&hm=48cdda0173641a57a1a20ba155d3d3a144767a1a1370df3ff3ed2bbf3dc94027&')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1216252991859064933/profile_image-3.jpeg?ex=65ffb6de&is=65ed41de&hm=a7472a7a7eab04000d3b3bb503cba093cfd9251fe3f0ae4ffc099228a2ace6fd&')
    dave = User(
        username='dave', email='dave@aa.io', password='password', profile_url='https://cdn.discordapp.com/attachments/885032629299212308/1216253022393466880/profile_image-4.png?ex=65ffb6e5&is=65ed41e5&hm=1c4ee54cc1704b48804f2b7c06daf98091c6afa8575056f09d52b02113bbca97&')

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
