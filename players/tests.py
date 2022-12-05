import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from players.models import Player


class PlayerTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Player.objects.create(name="Python", code=123, owner=self.test_user)
        Player.objects.create(name="Docker", code=789, owner=self.test_user)

        player_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(player_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(player_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Player.objects.create(name=mock_name, code=mock_code, owner=self.test_user)

    def test_player_model(self):
        """Players creation are correctly identified"""
        python_player = Player.objects.get(name="Python")
        docker_player = Player.objects.get(name="Docker")
        self.assertEqual(python_player.owner.username, "testuser")
        self.assertEqual(docker_player.owner.username, "testuser")
        self.assertEqual(python_player.code, 123)
        self.assertEqual(docker_player.code, 789)

    def test_player_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            player_test = Player.objects.get(name=mock_name)
            self.assertEqual(player_test.owner.username, "testuser")
            self.assertEqual(player_test.code, mock_code)