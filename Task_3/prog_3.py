import time
from pathlib import Path
import os
class Test1:
    tc_id=1
    name='List of files'

    def prep(self):
        if int(time.time()) % 2 != 0:
            raise ValueError        

    def run(self):
        home = Path.home()
        print(os.listdir(home))

    def clean_up(self):
        pass

    def execute(self):
        logout=f"Test number {self.tc_id}  with name \"{self.name}\" started\n"
        print("Execute started")
        try:
            self.prep()
        except ValueError:
            logout+=f"Test number {self.tc_id}  with name \"{self.name}\" was interrupted\n"
            print("test interrupted")
            with open('logT1.txt', 'w') as f:
                f.write(logout)
            return
        logout+="Prep was executed\n"
        print("prep executed")
        self.run()
        logout+="Run was executed\n"
        print("run executed")
        self.clean_up()
        logout+="Clean up was executed\n"
        print("clean_up executed")
        print("test finished")
        logout+=f"Test number {self.tc_id}  with name \"{self.name}\" was finished\n"
        with open('logT1.txt', 'w') as f:
            f.write(logout)

class Test2:
    tc_id=2

    name='Random file'

    def prep(self):
        process = os.popen('wmic memorychip get capacity')
        result = process.read()
        process.close()
        totalMem = 0
        for m in result.split("  \n\n")[1:-1]:
            totalMem += int(m)
        totalMem=totalMem / (1024**3)
        if totalMem < 1:
            raise MemoryError

    def run(self):
        my_file = open("new_file.txt", "wb")
        info=os.urandom(1048576)
        my_file.write(info)

    def clean_up(self):
        os.remove("new_file.txt")

    def execute(self):
        logout=f"Test number {self.tc_id}  with name \"{self.name}\" started\n"
        print("execute started")
        try:
            self.prep()
        except MemoryError:
            print("test interrupted")
            logout+=f"Test number {self.tc_id}  with name \"{self.name}\" was interrupted\n"
            with open('logT2.txt', 'w') as f:
                f.write(logout)
            return
        logout+="Prep was executed\n"
        print("prep executed")
        self.run()
        logout+="Run was executed\n"
        print("run executed")
        self.clean_up()
        logout+="Clean up was executed\n"
        print("clean_up executed")
        logout+=f"Test number {self.tc_id}  with name \"{self.name}\" was finished\n"
        print("test finished")
        with open('logT2.txt', 'w') as f:
            f.write(logout)

test=Test2()
test.execute()
