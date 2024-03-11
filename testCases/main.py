import unittest
import HtmlTestRunner

from testCases.Login_test import Login_test
from testCases.Registration import TestRegistration
from testCases.changing_the_status import changing_the_status
from testCases.job_2 import Job
from testCases.addingClients import adding_Client
from testCases.prospects_To_leads import prospects_To_leads
from testCases.Route_List import Route_List
from testCases.Leads import Leads
from testCases.addingLocation import adding_Location
from testCases.Settings import Adding_team_member
from testCases.Add_appointment import Adding_appointment

if __name__ == '__main__':
    suite = unittest.TestSuite()

    unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report_directory'))
