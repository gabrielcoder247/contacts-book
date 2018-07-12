import unittest 
from contact import Contact

class TestContact(unittest.TestCase):
    '''
    Test class that define test case for the contact class behaviours.
    
    Args:
    unittest.TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_contact = Contact("james","Muriuki","07030538879","gabrielcoder247@gmail.com")
    def test_init(self):

        self.assertEqual(self.new_contact.first_name,"james")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"07030538879")
        self.assertEqual(self.new_contact.email,"gabrielcoder247@gmail.com")

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test has run.
        '''
        Contact.contact_list = []
    # other test cases here

    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)


    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@gmail.com")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@gmail.com")
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0712345678")
        self.assertEqual(found_contact.email,test_contact.email)



        

    
if __name__ == '__main__':
    unittest.main()
