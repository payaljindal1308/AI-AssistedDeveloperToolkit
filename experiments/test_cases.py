
import unittest
from unittest.mock import MagicMock, patch
from src.my_module import get_all_questions_with_liked


class TestGetAllQuestionsWithLiked(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock()

    @patch('src.my_module.session', new_callable=MagicMock)
    def test_get_all_questions_with_liked_success(self, patched_session):
        # Setup
        session, data = MagicMock(), {'questionsLikes': [1, 2]}

        mock_questions = [
            MagicMock(id=1, liked=False),
            MagicMock(id=2, liked=False)
        ]

        patched_session.execute.return_value.scalars.unique.return_value.all.return_value = mock_questions
        # Execute
        results = get_all_questions_with_liked(session, data)
        # Assert
        self.assertE