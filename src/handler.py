from main import *
from datetime import datetime
import string
import random


def handler(event, context):
    print("Log start date: ", datetime.today())
    
    health_check = random.randint (0, 2)

    if health_check == 0:
        print("I'm a lazy fuck")
    elif health_check == 1:
        print("Working today")
        work()
    elif health_check == 2:
        print("Hardworking AF")
        for i in range(0, health_check):
            work()
    
    print("Finished")

def work():
    branch_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
    file_path = f"dump/{branch_name}.txt"
    commit_message = "Add new file"
    file_content = "This is the content of the new file."

    print("Branch name: ", branch_name)
    github_profile_maker(branch_name, file_path, commit_message, file_content)

handler(None, None)