class Contact:
 '''
 Class that generates new instances of contacts
 '''
 pass

def __init__(self,first_name,last_name,phone_number,email):
    '''
    __init__ method that helps us define properties for our objects.
  
    Args:
        first_name:New contact first first_name
        last_name:New contact last first_name
        number:New contact phone number
        email:New contact email address.
    '''
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email

    contact_list = [] # Empty contact list


