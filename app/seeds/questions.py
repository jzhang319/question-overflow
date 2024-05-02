from app.models import db, Question, environment, SCHEMA
from sqlalchemy import text

def seed_questions():
    demo = Question(
        user_id=1, question="how do i bathe", detail="people say i stink and say that i should bathe", url="https://cdn.discordapp.com/attachments/885032629299212308/1235680291654336594/9k.png?ex=66354073&is=6633eef3&hm=22e848a96df713e0bb26cb135771f74b890cdec02ed03a450a3ebc6a63ed46fc&"
    )
    demo1 = Question(
        user_id=2, question="how to what", detail="dont know what to do most of the time", url="https://cdn.discordapp.com/attachments/885032629299212308/1235680508810235956/eFfVvaN7YcU7MoewP4Po745U2Jrn24AAAAASUVORK5CYII.png?ex=663540a7&is=6633ef27&hm=722532008f3196691207c84e9799f6499eaa14ab16a6e3e7c9e22418b119802e&"
    )
    demo2 = Question(
        user_id=3, question="how to when", detail="people say i have no concept of time, it's true", url="https://cdn.discordapp.com/attachments/885032629299212308/1235680632550588426/9k.png?ex=663540c4&is=6633ef44&hm=2ada9fc9ba1636b9907dd1a799cfc5345de1e981feaf057c4879e9b87203f29c&"
    )
    demo3 = Question(
        user_id=1, question="What is a Stack Overflow?", detail="just wondering", url="https://cdn.discordapp.com/attachments/885032629299212308/1235680807105073233/2Q.png?ex=663540ee&is=6633ef6e&hm=a03549b6f24ba9f391640d2f3b77a81ebcf2e2abcae8204b0be2f1ec050df1cb&"
    )
    demo4 = Question(
        user_id=1, question="How do I search for a specific question on Stack Overflow?", detail="beginner question", url="https://cdn.discordapp.com/attachments/885032629299212308/1235680971102224454/9k.png?ex=66354115&is=6633ef95&hm=90afa1d96afbc4e513d9904b1581b214655f2560ccc142230969e6466f05b2d9&"
    )
    demo5 = Question(
        user_id=1, question="Is Stack Overflow free to use?", detail="more beginner question1", url="https://cdn.discordapp.com/attachments/885032629299212308/1235681086529474641/EAAAAASUVORK5CYII.png?ex=66354130&is=6633efb0&hm=77cd3a5ae6a909491511ef8a1d08ed2a82c46766adcaf14d3a20ce971b5c48bd&"
    )
    demo6 = Question(
        user_id=1, question="How do I ask a question on Stack Overflow?", detail="more beginner question1", url="https://cdn.discordapp.com/attachments/885032629299212308/1235681238367600722/Z.png?ex=66354155&is=6633efd5&hm=83dd11c4e364f66d058e009eb798ab344327cc1874e7aded57c4662e695759e9&"
    )
    demo7 = Question(
        user_id=1, question="What are tags on Stack Overflow?", detail="more beginner question1", url="https://cdn.discordapp.com/attachments/885032629299212308/1235681346714730587/Z.png?ex=6635416e&is=6633efee&hm=7b79e4f1d6efdbaba8ef86266b84e72b395821f606eceb0697d83330756b2f39&"
    )
    demo8 = Question(
        user_id=1, question="How do I post an answer to a question on Stack Overflow?", detail="more beginner question1", url="https://cdn.discordapp.com/attachments/885032629299212308/1235681506077315112/Z.png?ex=66354194&is=6633f014&hm=b7ff87775b6dcb158bdbf63898f645497f04423ff886c73a5afed16df0b36024&"
    )
    demo9 = Question(
        user_id=1, question="What is the difference between a cell phone and a smartphone?", detail="more beginner question1", url="https://cdn.discordapp.com/attachments/885032629299212308/1235681686923116676/Z.png?ex=663541c0&is=6633f040&hm=c0ba95861aa59f0467d4093a713e7ef44411a5c23a8d60d63fe8fe4813507d90&"
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
