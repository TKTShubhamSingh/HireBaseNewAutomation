import logging
import unittest

from oauth2client.service_account import ServiceAccountCredentials


class Skill (unittest.TestCase):
    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s: %(levelname)s: %(message)s',
            handlers=[
                logging.FileHandler("Test.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("setting up the environment")

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name()