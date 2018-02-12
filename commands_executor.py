import subprocess


def ge_last_rows(path):
    task = subprocess.Popen("tail -n 20 {}".format(path), shell=True, stdout=subprocess.PIPE)
    data = task.stdout.read()
    task.kill()
    return data


def memory_stat():
    task = subprocess.Popen("free -h", shell=True, stdout=subprocess.PIPE)
    data = task.stdout.read()
    task.kill()
    return data


def cpu_application():
    task = subprocess.Popen("mpstat -P ALL | cut -d ' ' -f7-10 |tr -d \" \" ", shell=True, stdout=subprocess.PIPE)
    data = task.stdout.read()
    task.kill()
    return data


def system_info():
    task = subprocess.Popen("uname; uname -n;uname -v;uname -m;curl ipinfo.io/ip", shell=True, stdout=subprocess.PIPE)
    data = task.stdout.read()
    task.kill()
    return data
