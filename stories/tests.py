from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Story

# Create your tests here.
class StoryTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='Hamza', password='123456')
        test_user.save()

        test_post = Story.objects.create(
            author = test_user,
            title = "Moira's Day Off",
            body = '''
            I can imagine Moira’s reply: You’re not on track with your calcium and folic acid targets today. Spinach is advised. Maybe a green curry?

But today there’s no level, pleasant voice in my ear. Moira is, as they used to say, “in the shop” today for her annual updates and maintenance. I don’t know why they can’t just upload the stuff into them, but these maintenance days are a fact of life we all deal with. I guess even artificial intelligence is entitled to one vacation day a year.

Most people just sleep through it. Sometimes I do, too, but this year I was curious.

“I’ll be fine,” I told Moira before she went dark. “You’ve taught me well. I’ve probably absorbed you into my own interior monologue. I won’t ruin what we’ve worked for,” I promised her.
            '''
        )
        test_post.save()

    def test_story_content(self):
        story = Story.objects.get(id=1)
        actual_author = str(story.author)
        actual_title = str(story.title)
        actual_body = str(story.body)
        self.assertEqual(actual_author, 'Hamza')
        self.assertEqual(actual_title, "Moira's Day Off")
        self.assertEqual(actual_body, '''
            I can imagine Moira’s reply: You’re not on track with your calcium and folic acid targets today. Spinach is advised. Maybe a green curry?

But today there’s no level, pleasant voice in my ear. Moira is, as they used to say, “in the shop” today for her annual updates and maintenance. I don’t know why they can’t just upload the stuff into them, but these maintenance days are a fact of life we all deal with. I guess even artificial intelligence is entitled to one vacation day a year.

Most people just sleep through it. Sometimes I do, too, but this year I was curious.

“I’ll be fine,” I told Moira before she went dark. “You’ve taught me well. I’ve probably absorbed you into my own interior monologue. I won’t ruin what we’ve worked for,” I promised her.
            ''')