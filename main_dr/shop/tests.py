import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, figures, handle_help, handle_add_figure, echo_all


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 534895748
        start(message)

    def test_help(self):
        message = MagicMock()
        message.chat.id = 534895748
        handle_help(message)

    def test_figures(self):
        message = MagicMock()
        message.chat.id = 534895748
        figures(message)

    def test_add_figure(self):
        message = MagicMock()
        message.chat.id = 534895748
        handle_add_figure(message)


if __name__ == '__main__':
    unittest.main()