from subprocess import Popen, PIPE
import time;
import os;

def execute(cmd):
    popen = Popen(cmd, stdout=PIPE, universal_newlines=True);
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line ;
    popen.stdout.close();

lastDayCompleted = 24;

totalTime = 0;
for n in range(1, lastDayCompleted + 1):
    folder = "{:02d}".format(n);
    os.chdir("./" + folder);
    start = time.time();
    for statement in execute(['python', '-u', 'solution.py']):
        print("\t"+statement, end="");
    end = time.time();
    os.chdir("../");
    print("\tSolved in {:06.3f} seconds".format(end-start));
    print();
    totalTime += (end - start);

print("\tAll Days Solved in {:06.3f} seconds".format(totalTime));
