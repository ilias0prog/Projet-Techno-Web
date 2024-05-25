#from uuid import uuid4
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from uuid import uuid4
from datetime import datetime, date
import random

engine = create_engine(
    #"sqlite:///data/database.sqlite",
    "sqlite:///Librairie\data\database.sqlite", 
    echo=False
)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

from app.models.usersandarticles import  User
from app.models.usersandarticles import  Article
from app.models.usersandarticles import  Comment




def create_database():
    Base.metadata.create_all(engine)


def clear_database():
    Base.metadata.clear()
    
def delete_database():
    Base.metadata.drop_all(engine)

def fill_users_db():    
    users_data = [
    {
        "id": str(uuid4()),
        "username": "john_doe",
        "firstname": "John",
        "name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "admin": True,
        "interests" : "sport technology health cinema music politics environment international economics",
    },
    {
        "id": str(uuid4()),
        "username": "jane_smith",
        "firstname": "Jane",
        "name": "Smith",
        "email": "jane.smith@example.com",
        "password": "password456",
        "admin": False,
        "interests" : "health cinema music",
    },
    {
        "id": str(uuid4()),
        "username": "bob_johnson",
        "firstname": "Bob",
        "name": "Johnson",
        "email": "bob.johnson@example.com",
        "password": "password789",
        "admin": False,
        "interests" : "politics technology",
    },
    {
        "id": str(uuid4()),
        "username": "emily_clark",
        "firstname": "Emily",
        "name": "Clark",
        "email": "emily.clark@example.com",
        "password": "passwordabc",
        "admin": True,
       "interests" : "sport environment international",
    },
    {
        "id": str(uuid4()),
        "username": "michael_taylor",
        "firstname": "Michael",
        "name": "Taylor",
        "email": "michael.taylor@example.com",
        "password": "passworddef",
        "admin": False,
        "interests" : "sport social",
    },
    {
        "id": str(uuid4()),
        "username": "susan_miller",
        "firstname": "Susan",
        "name": "Miller",
        "email": "susan.miller@example.com",
        "password": "passwordghi",
        "admin": False,
        "interests" : "cinema politics economics",
    },
    {
        "id": str(uuid4()),
        "username": "david_anderson",
        "firstname": "David",
        "name": "Anderson",
        "email": "david.anderson@example.com",
        "password": "passwordjkl",
        "admin": True,
       "interests" : "economics cinema",
    },
    {
        "id": str(uuid4()),
        "username": "amy_wilson",
        "firstname": "Amy",
        "name": "Wilson",
        "email": "amy.wilson@example.com",
        "password": "passwordmno",
        "admin": False,
        "interests" : "environment international health",
    },
    {
        "id": str(uuid4()),
        "username": "peter_brown",
        "firstname": "Peter",
        "name": "Brown",
        "email": "peter.brown@example.com",
        "password": "passwordpqr",
        "admin": False,
        "interests" : "social music politics",
    },
    {
        "id": str(uuid4()),
        "username": "laura_evans",
        "firstname": "Laura",
        "name": "Evans",
        "email": "laura.evans@example.com",
        "password": "passwordstu",
        "admin": True,
        "interests" : "sport technology",
    }
]
    
    with Session() as session:
        for user_data in users_data:
            user = User(
                id=user_data["id"],
                username=user_data["username"],
                firstname=user_data["firstname"],
                name=user_data["name"],
                email=user_data["email"],
                password=user_data["password"],
                interests  = user_data["interests"],
                admin=user_data["admin"],
                )
            session.add(user)
            session.commit()

def fill_articles_db():
    # Assurez-vous que les utilisateurs existent dans la base de donnees
    with Session() as session:
        users = session.query(User).all()
        if not users:
            print("No users found in the database. Please add users before adding articles.")
            return
        articles_data = [
                {
                    "id": str(uuid4()),
                    "author_username": users[0].username,
                    "title": "The Impact of Technology on Sportsmanship",
                    "date": date(2024,5,18),
                    "content": "In the realm of sports, the ongoing debate about the role of technology continues to evolve. From controversial referee decisions to athlete performance enhancements, technology has become deeply intertwined with the fabric of sportsmanship. As advancements in data analytics and wearable technology push the boundaries of athletic performance, questions arise about fairness, ethics, and the essence of true competition. This article explores the intricate relationship between sports and technology, examining both its benefits and drawbacks."
                    +"The rise of technology in sports has brought about a myriad of changes, some hailed as revolutionary advancements and others criticized as detrimental interferences in the game. The use of video technology to review contentious decisions on the field has significantly improved the accuracy and transparency of competitions, thereby reducing human errors and controversies. Similarly, advances in tracking devices and biometric sensors allow coaches and athletes to gather valuable data on individual performances, thereby facilitating training optimization and injury prevention."
                    +"However, with these benefits also come challenges and ethical dilemmas. The introduction of technology into sports raises questions about fairness and equal opportunities. Teams and athletes with greater financial resources may invest more in cutting-edge technologies, thereby creating a competitive imbalance. Furthermore, the use of advanced technologies such as genetic modification and robotic prosthetics raises fundamental questions about what is considered fair in sports competition."
                    +"Ultimately, the relationship between sports and technology is a complex issue that requires thoughtful consideration and open dialogue. As technology continues to progress by leaps and bounds, it is imperative that stakeholders in the world of sports engage in meaningful discussions about how it can be used responsibly to enhance the sporting experience while preserving the integrity and ethics of competition.",
                    "theme": "sport",
                    "likes": 4,
                    "dislikes": 1
                },
                {
                    "id" : str(uuid4),
                    "author_username": users[1].username,
                    "title": "The Critical Role of Mental Health in Overall Well-being",
                    "date": date(2024,4,29),
                    "content": "In recent years, the focus on mental health has increased significantly, shedding light on its essential role in overall well-being. Mental health, often misunderstood and stigmatized, is now recognized as crucial to our physical health, social interactions, and productivity. As society becomes more aware of the importance of mental health, it's essential to understand its impact and the measures we can take to nurture it."
                    + " At its core, mental health encompasses our emotional, psychological, and social well-being. It influences how we think, feel, and behave in various situations, as well as how we navigate relationships, cope with stress, and make decisions. A positive state of mental health is characterized by resilience, self-awareness, and the ability to maintain a sense of balance and perspective amidst life's challenges."
                    + " Furthermore, the stigma surrounding mental illness often exacerbates the challenges faced by individuals seeking help and support. Misconceptions, discrimination, and societal attitudes towards mental health can deter individuals from seeking timely interventions and accessing appropriate treatment and care. As a result, many individuals suffer in silence, grappling with their mental health issues without the necessary support systems in place."
                    + " Social interactions and relationships are deeply affected by mental health. Poor mental health can lead to isolation, strained relationships, and difficulty in maintaining social connections. Healthy relationships, in turn, are essential for mental well-being, providing support, companionship, and a sense of belonging. Encouraging open conversations about mental health can help reduce stigma, making it easier for individuals to seek help and support from friends and family."
                    + " In conclusion, mental health is integral to overall well-being and must be prioritized in our efforts to promote health and wellness for all. By fostering awareness, reducing stigma, and investing in mental health services and support systems, we can create a more compassionate and supportive society where individuals can thrive mentally, emotionally, and socially. Let us recognize the critical role of mental health in shaping our collective well-being and commit to building a healthier, more resilient future for generations to come.",
                    "theme": "health",
                    "likes": 5,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[2].username,
                    "title": "The Path to Holistic Wellness: A Journey of Self-Care",
                    "date": date(2024,5,15),
                    "content": "The pursuit of optimal health and well-being is a universal endeavor that transcends geographical boundaries and cultural differences. In today's fast-paced world, the importance of holistic health practices is increasingly recognized as essential for longevity and vitality. From mindful meditation to nutritional therapy, this article navigates the intricate landscape of holistic health, offering insights into alternative healing modalities and lifestyle choices. Join us on a journey toward holistic wellness and discover the transformative power of self-care.",
                    "theme": "health",
                    "likes": 3,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[3].username,
                    "title": "Navigating the Complexities of Political Theory",
                    "date": date(2024,5,12),
                    "content": "Politics, the art and science of governance, shapes the course of nations and the destiny of societies. As geopolitical landscapes shift and power dynamics evolve, the study of politics becomes ever more critical in understanding global affairs. This article delves into the nuances of political theory, examining ideologies, institutions, and international relations. From democracy to authoritarianism, we explore the diverse spectrum of political systems and their impact on policy, diplomacy, and human rights.",
                    "theme": "politics",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[4].username,
                    "title": "Unraveling the Digital Revolution: Exploring Emerging Technologies",
                    "date": date(2024,3,5),
                    "content": "The rapid advancement of technology has revolutionized virtually every aspect of modern life, from communication and commerce to healthcare and education. As we navigate the complexities of the digital age, questions about privacy, security, and ethics loom large. This article delves into the frontiers of technological innovation, exploring emerging trends such as artificial intelligence, blockchain, and virtual reality. Join us as we unravel the possibilities and pitfalls of the digital revolution, and contemplate the future of humanity in an increasingly interconnected world.",
                    "theme": "technology",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[5].username,
                    "title": "The Rhythm of Life: Exploring the Evolution of Music",
                    "date": date(2024,5,18),
                    "content": "Music, the universal language of emotions, has captivated human hearts and minds for millennia. From ancient chants to modern symphonies, the evolution of music reflects the cultural, social, and technological changes of each era. This article embarks on a journey through musical history, tracing the origins of different genres, instruments, and musical traditions. Join us as we explore the transformative power of music and its profound impact on our lives and societies.",
                    "theme": "music",
                    "likes": 3,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[6].username,
                    "title": "Lights, Camera, Action! The Art of Cinematic Storytelling",
                    "date": date(2024,3,30),
                    "content": "Cinema, the magical world of storytelling through moving images, has enchanted audiences around the globe for over a century. From silent films to blockbuster franchises, the evolution of cinema mirrors the evolution of human imagination and technology. This article delves into the art and craft of cinematic storytelling, examining the techniques, themes, and cultural significance of iconic films. Join us as we embark on a cinematic journey through time and space, exploring the boundless creativity of filmmakers and the enduring impact of their stories.",
                    "theme": "cinema",
                    "likes": 5,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[7].username,
                    "title": "The Green Revolution: Navigating Environmental Sustainability",
                    "date": date(2024,5,5),
                    "content": "The global environmental crisis has reached a critical juncture, necessitating urgent action to mitigate climate change and preserve our planet's biodiversity. From renewable energy to conservation efforts, the green revolution is paving the way toward a sustainable future. This article explores the challenges and opportunities of environmental sustainability, highlighting innovative solutions and grassroots initiatives that aim to protect and restore our natural ecosystems. Join us as we delve into the frontline of environmental activism and envision a world where humanity lives in harmony with nature.",
                    "theme": "environment",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[8].username,
                    "title": "The Socioeconomic Impact of Globalization",
                    "date": date(2024,5,5),
                    "content": "Globalization, the interconnectedness of economies and cultures on a global scale, has reshaped the geopolitical landscape and transformed the way we live and work. From multinational corporations to cross-border trade agreements, the socioeconomic impact of globalization is profound and far-reaching. This article examines the opportunities and challenges of economic globalization, discussing its effects on income inequality, labor markets, and social welfare. Join us as we navigate the complexities of globalization and explore its implications for the future of humanity.",
                    "theme": "economics",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[0].username,
                    "title": "The Power of Connectivity: Social Media in the Digital Age",
                    "date": date(2024,4,28),
                    "content": "Social media, the digital agora of the 21st century, has revolutionized the way we connect, communicate, and collaborate with one another. From viral memes to online activism, social media platforms have become integral to modern society, shaping public discourse and influencing cultural trends. This article delves into the dynamics of social media in the digital age, exploring its impact on identity formation, community building, and political engagement. Join us as we navigate the virtual landscapes of Facebook, Twitter, and Instagram, and examine the evolving role of social media in our lives.",
                    "theme": "social",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "id": str(uuid4()),
                    "author_username": users[1].username,
                    "title": "The Evolving Dynamics of Modern Politics",
                    "date": date(2024,4,16),
                    "content": "In the fast-paced landscape of modern politics, dynamics are constantly evolving, shaped by shifting ideologies, socio-economic factors, and technological advancements. This article delves into the multifaceted realm of political discourse, exploring key trends, challenges, and opportunities that define contemporary governance."
                    + " At the heart of political evolution lies the interplay between traditional and emerging ideologies. From conservatism to liberalism, socialism to populism, political movements reflect society's diverse values and aspirations. Today, we witness a resurgence of nationalism and populism, fueled by economic uncertainties, cultural anxieties, and disillusionment with establishment politics. These movements challenge the status quo and amplify voices traditionally marginalized in mainstream discourse."
                    + " Moreover, technology has revolutionized political engagement, democratizing access to information and enabling grassroots mobilization. Social media platforms serve as battlegrounds for political debate and activism, amplifying echo chambers while also fostering connections across diverse communities. However, the proliferation of misinformation and echo chambers poses challenges to informed decision-making and consensus-building, undermining the integrity of democratic processes."
                    + " In parallel, globalization has reshaped the geopolitical landscape, blurring traditional boundaries and reshaping power dynamics. Economic interdependence, transnational threats, and global governance mechanisms highlight the interconnectedness of nations and the need for collaborative solutions to shared challenges. However, globalization also fuels tensions over trade, immigration, and cultural identity, leading to polarization and nationalist sentiments."
                    + " Furthermore, the quest for environmental sustainability and social justice has emerged as central themes in contemporary politics. Climate change, income inequality, and racial injustice galvanize movements for systemic change, demanding policy responses that prioritize the well-being of people and the planet. Grassroots activism, civil disobedience, and political mobilization drive momentum for transformative action, challenging entrenched power structures and fostering a more inclusive political discourse."
                    + " As we navigate the complexities of modern politics, it is crucial to uphold democratic principles, respect diverse perspectives, and engage in constructive dialogue. By fostering civic participation, promoting transparency, and holding leaders accountable, we can safeguard democratic institutions and ensure responsive governance. Ultimately, the future of politics lies in our collective ability to adapt, innovate, and collaborate in pursuit of a more just, equitable, and sustainable world.",
                    "theme": "politics",
                    "likes": 4,
                    "dislikes": 0
                },
            ]
        with Session() as session:
            for article_data in articles_data:
                article = Article(
                    id=article_data["id"],
                    author_username=article_data["author_username"],
                    title=article_data["title"],
                    date=article_data["date"],
                    content=article_data["content"],
                    theme=article_data["theme"],
                    likes=article_data["likes"],
                    dislikes=article_data["dislikes"],)
                session.add(article)
                session.commit()

def fill_comments_db():
    with Session() as session:
        # Récupérer les utilisateurs et les articles existants
        users = session.query(User).all()
        articles = session.query(Article).all()
        
        if not users:
            print("No users found in the database. Please add users before adding comments.")
            return
        
        if not articles:
            print("No articles found in the database. Please add articles before adding comments.")
            return
        
        comments_data = [
            {
                "author_id": (users)[0].id,
                "article_id": random.choice(articles).id,
                "content": "Great article! Very informative."
            },
            {
                "author_id": (users)[1].id,
                "article_id": random.choice(articles).id,
                "content": "I completely disagree with the points made in this article."
            },
            {
                "author_id": (users)[2].id,
                "article_id": random.choice(articles).id,
                "content": "Well written and very insightful."
            },
            {
                "author_id": (users)[3].id,
                "article_id": random.choice(articles).id,
                "content": "This article needs more references."
            },
            {
                "author_id": (users)[4].id,
                "article_id": random.choice(articles).id,
                "content": "Interesting perspective, I learned something new."
            },
            {
                "author_id": (users)[5].id,
                "article_id": random.choice(articles).id,
                "content": "The article was too long, it could have been shorter."
            },
            {
                "author_id": (users)[6].id,
                "article_id": random.choice(articles).id,
                "content": "I enjoyed reading this, keep up the good work."
            },
            {
                "author_id": (users)[7].id,
                "article_id": random.choice(articles).id,
                "content": "This article is biased, please provide balanced views."
            },
            {
                "author_id": (users)[8].id,
                "article_id": random.choice(articles).id,
                "content": "Excellent writing, I look forward to more articles like this."
            },
            {
                "author_id": (users)[9].id,
                "article_id": random.choice(articles).id,
                "content": "Not enough evidence to support the claims made in this article."
            }
        ]

        for comment_data in comments_data:
            comment = Comment(
                author_id=comment_data["author_id"],
                article_id=comment_data["article_id"],
                content=comment_data["content"]
            )
            session.add(comment)
            session.commit()