
import unittest
from models import QuestionsModel
from sqlalchemy.sql import select

class TestGetQuestionsWithId(unittest.TestCase):

    def setUp(self):
        self.question_id = 1
        self.session = Session()

    def test_get_questions_with_id(self):
        # Execute the code snippet or function
        query = select(QuestionsModel)
        query = query.filter(QuestionsModel.id == self.question_id)
        with self.session as session:
            result = session.execute(query).scalars().unique().first()
        response_json = {
            "id": result.id,
            "question": result.question,
            "title": result.question,
            "description": result.description,
            "likes": result.likes,
            "bookmarks": result.bookmark,
            "verified": result.verified,
        }

        # Assert the expected results
        self.assertEqual(response_json['id'], self.question_id)
        self.assertEqual(response_json['question'], result.question)
        self.assertEqual(response_json['title'], result.question)
        self.assertEqual(response_json['description'], result.description)
        self.assertEqual(response_json['likes'], result.likes)
        self.assertEqual(response_json['bookmarks'], result.bookmark)
        self.assertEqual(response_json['verified'], result.verified)

if __name__ == '__main__':
    unittest.main()