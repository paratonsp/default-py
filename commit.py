from git import Repo
from datetime import datetime
import time

print("Push?")
cp =  input()
PATH_OF_GIT_REPO = r'../default-py'

def git_push():
    try:
        now = datetime.now()
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit("Update: " + str(now))
        origin = repo.remote(name='origin')
        origin.push()
        print("Commit: " + str(now))
    except:
        print('Error')    


for x in range (1,int(cp)):
    time.sleep(1)
    git_push()
