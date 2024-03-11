import unittest
from testCases.Registration import TestRegistration
from testCases.Login_test import Login_test
from testCases.changing_the_status import changing_the_status
from testCases.prospects_To_leads import prospects_To_leads
from testCases.job_2 import Job
from testCases.Route_List import Route_List
from testCases.Leads import Leads

tc1 = unittest.TestLoader().loadTestsFromTestCase(Login_test)

tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRegistration)

tc3 = unittest.TestLoader().loadTestsFromTestCase(changing_the_status)

tc4 = unittest.TestLoader().loadTestsFromTestCase(prospects_To_leads)

tc5 = unittest.TestLoader().loadTestsFromTestCase(Job)

tc6 = unittest.TestLoader().loadTestsFromTestCase(Route_List)

tc7 = unittest.TestLoader().loadTestsFromTestCase(Leads)

functionality = unittest.TestSuite([tc7])

unittest.TextTestRunner().run(functionality)
