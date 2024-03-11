import unittest
import HtmlTestRunner
from testCases.addingClients import adding_Client
from testCases.Registration import TestRegistration
from testCases.Login_test import Login_test
from testCases.changing_the_status import changing_the_status
from testCases.prospects_To_leads import prospects_To_leads
from testCases.job_2 import Job
from testCases.Route_List import Route_List
from testCases.Leads import Leads
from testCases.addingLocation import adding_Location
from testCases.Settings import Adding_team_member

tc1 = unittest.TestLoader().loadTestsFromTestCase(Login_test)

tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRegistration)

tc3 = unittest.TestLoader().loadTestsFromTestCase(changing_the_status)

tc4 = unittest.TestLoader().loadTestsFromTestCase(prospects_To_leads)

tc5 = unittest.TestLoader().loadTestsFromTestCase(Job)

tc6 = unittest.TestLoader().loadTestsFromTestCase(Route_List)

tc7 = unittest.TestLoader().loadTestsFromTestCase(Leads)

tc8 = unittest.TestLoader().loadTestsFromTestCase(adding_Client)

tc9 = unittest.TestLoader().loadTestsFromTestCase(adding_Location)

tc10 = unittest.TestLoader.loadTestsFromTestCase(Adding_team_member)


functionality = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10])

unittest.TextTestRunner().run(functionality)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report_dir'))
