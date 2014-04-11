__author__ = 'ganesh'
import sys,os
import subprocess


def display_info():
    # test_stream = subprocess.check_output("uname -a",shell=False)
    kernel_info = subprocess.check_output("uname -a",shell=True)
    distro_info = subprocess.check_output("head -n1 /etc/issue",shell=True)
    sys_info = subprocess.check_output("lsb_release -a",shell=True)
    print kernel_info
    print distro_info
    print sys_info

display_info()