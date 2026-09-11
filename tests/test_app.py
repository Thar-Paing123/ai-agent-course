import unittest

import app


class AppTests(unittest.TestCase):
    def test_fetch_joke_returns_expected_fields(self):
        joke = app.fetch_joke()
        self.assertIn("setup", joke)
        self.assertIn("punchline", joke)


if __name__ == "__main__":
    unittest.main()
