# Exercise 1: Call History

class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call_phone(self, other_phone):
        '''Print a message saying who called who, and add it to the internal  
        call history of the phone'''
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        self.call_history.append(call_record)
        print(f"{self.phone_number} is calling {other_phone.phone_number}")
        return self
    
    def send_message(self,other_phone,content=''):
        '''Send a text message to another phone'''
        text = {}
        text.update({'To' : other_phone.phone_number})
        text.update({'From' : self.phone_number})
        text.update({'content' : content})
        self.messages.append(text)
        other_phone.messages.append(text)

        return self

    def show_outgoing_messages(self):
        '''Show all messages you sent to other phones.'''
        print("Outgoing Messages: ")
        for text in self.messages:
            if text['From'] == self.phone_number:
                print(text)

    
    def show_incoming_messages(self):
        '''Show all the messages you have received'''
        print("Received Messages: ")
        for text in self.messages:
            if text['To'] == self.phone_number:
                print(text)

    def show_call_history(self):
        '''Print the calls that have been sent/received'''
        print("Call History:")
        for call in self.call_history:
            print(call)

    def show_messages_from(self,other_phone):
        '''Prints the messages received from a specified phone'''
        print(f"Messages from {other_phone.phone_number}: ")
        for text in self.messages:
            if text['From'] == other_phone.phone_number:
                print(text)
    



my_phone = Phone('052-555-1234')
gf_phone = Phone('123-555-5555')
friends_phone = Phone('052-555-2222')
moms_phone = Phone('052-555-1111')

print(my_phone.__dict__)

my_phone.send_message(gf_phone,'I love you')
gf_phone.send_message(my_phone,"Awh you're so sweet")
gf_phone.send_message(my_phone,'lets grab dinner later')
gf_phone.send_message(my_phone,'wanna go to the mall?')
moms_phone.send_message(my_phone,"Where are you?")
my_phone.send_message(friends_phone,'lets hang out')
friends_phone.send_message(my_phone,'Sounds good. After dinner.')

my_phone.show_incoming_messages()
my_phone.show_outgoing_messages()
my_phone.show_messages_from(gf_phone)
my_phone.show_messages_from(friends_phone)