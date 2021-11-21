import psutil;
import sys;
import os;
import time;


def processlog():

	list = [];

	for process in psutil.process_iter():

		try:

			pinfo = process.as_dict(attrs = ['pid','name','username']);

			pinfo['vms'] = process.memory_info().vms/(1024*1024), 'MB';

			list.append(pinfo);

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):

			pass;


	return list;



def logprocess(path):

	flag = os.path.isabs(path);

	if not flag:

		path = os.path.abspath(path);

	if os.path.isdir(path):

		t = time.time();

		fd = open(path+'/log+%s.txt'%t,'w');

		fd.write("Current running processes are \n\n");

		for items in processlog():

			items = str(items);

			fd.write("%s\n"%items);
	
		fd.close();

		

def main():

	print("Application name is",sys.argv[0]);

	print(logprocess(sys.argv[1]));





if __name__=="__main__":

	main();