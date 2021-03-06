import unittest

from credentialData import CredentialData


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = CredentialData("Gmail", "cliff", "lolololo") 

    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_credential.platform, "Gmail")
        self.assertEqual(self.new_credential.username, "cliff")
        self.assertEqual(self.new_credential.password, "lolololo")

    def tearDown(self):
    
        CredentialData.credentials = []

    def test_save_credential(self):
        """
        test if credential is saved in the credentials list
        """
        self.new_credential.save_credential()  
        self.assertEqual(len(CredentialData.credentials), 1)

    def test_display_credentials(self):
        """
        test display credentials method
        """
        self.assertEqual(CredentialData.display_credentials(),CredentialData.credentials)

if __name__ == '__main__':
    unittest.main()
