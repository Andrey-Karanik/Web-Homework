from django.db import models

class User(models.Model):
    login = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id} {self.login} {self.email} {self.nickname} {self.password}"

class Question(models.Model):
    title = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(User, related_name="questions")
    text = models.CharField(max_length=256)
    like_users = models.ManyToManyField(User, related_name="likes", blank=True)
    dislike_users = models.ManyToManyField(User, related_name="dislikes", blank=True)


BEST_MEMBERS = [
    'Mr. Freeman',
    'Dr. House',
    'Bender',
    'Queen Victoria',
    'V. Pupkin'
]

POPULAR_TAGS = [
    'perl',
    'python',
    'TechnoPark',
    'MySQL',
    'django',
    'Mail.Ru',
    'Voloshin',
    'Firefox'
]

QUESTIONS = []
for id in range(80):
    ANSWERS = []
    for i in range(id * id):
        ANSWERS.append({
            'id': i,
            'text': f'Text of Answer {i}'
        })
    QUESTIONS.append({
        'id': id,
        'title': f'Question {id}',
        'text': f'Text of Question {id}',
        'answers_number': id * id,
        'answers': ANSWERS,
        'tags': [f'tag{i}' for i in range(id)]
    })

HOT_QUESTION_IDS = [0, 5, 12]

IS_AUTH = False

