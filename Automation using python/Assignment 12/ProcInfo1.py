
import psutil;

import sys;



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



def findprocess(pname):


	list1 = processlog();


	for items in list1:

		if pname.lower() in items['name']:

			print(items);


def main():

	print("Application name is",sys.argv[0]);

	print(findprocess(sys.argv[1]));





if __name__=="__main__":


	main();