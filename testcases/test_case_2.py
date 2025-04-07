import pytest
import softest
from pages.home_page import HomePage
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("setup")
@ddt
class Test_Case2(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.ut = Utils(self.driver)

    @file_data("../testdata/testdata.json")
    def test_case_2(self, name, email, msg):
        #Step 1: From the home page go to contact page
        cp = self.hp.go_to_contact_page()

        #Step 2 & 3: Populate mandatory fields and click submit
        #cp.submit_message(forename="John", email="John@example.com", message="This is a test", submit=True)
        cp.submit_message(name, email, msg, True)

        #Step 4:Validate successful submission message
        self.ut.validate_success()

