import json

class Employee():
    def __init__(self, name = None, emp_id = None, json_string = None):
        if name is not None and emp_id is not None:
            self.name = name
            self.emp_id = emp_id
        elif json_string is not None:
            self.load_json(json_string)

    def load_json(self, json_string):
        my_dict = json.loads(json_string)
        self.name = my_dict['name']
        self.emp_id = my_dict['emp_id']
    
    def write_json(self, file_name):
        my_dict =  {
            'name' : self.name,
            'emp_id' : self.emp_id
        }

        file = open(file_name, 'a+')
        file.write(json.dumps(my_dict) + '\n')
        file.close()
    
class Event():
    def __init__(self, title = None, description = None, start_time = None, user_id = None, end_time = None, json_string = None):
        if title is not None and description is not None and start_time is not None and user_id is not None:
            self.title = title
            self.description = description
            self.start_time = start_time
            self.user_id = user_id
            if end_time is not None:
                self.end_time = end_time
        elif json_string is not None:
            self.load_json(json_string)
    
    def load_json(self, json_string):
        my_dict = json.loads(json_string)

        self.title = my_dict['title']
        self.description = my_dict['description']
        self.start_time = my_dict['start_time']
        self.user_id = Employee(json_string= my_dict['user_id'])
        self.end_time = my_dict['end_time']

    def write_json(self, file_name):
        my_dict = {
            'title' : self.title,
            'description' : self.description,
            'start_time' : self.start_time,
            'user_id' : self.user_id,
            'end_time' : self.end_time
        }

        file = open(file_name, 'a+')
        file.write(json.dumps(my_dict))
        file.close()

if __name__ == "__main__":
    test_emp = Employee(name = 'Jake', emp_id = 1234)
    test_emp.write_json('test.json')
    del test_emp
    
    test_emp = Employee(json_string=open('test.json', 'r').readline())
    print(test_emp.name)




    import os
    input('Hit <Enter> and it will remove the test.json file')
    os.remove('test.json')