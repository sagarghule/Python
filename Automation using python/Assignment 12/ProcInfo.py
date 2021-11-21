
import psutil;

import sys;



def processlog():

	list = [];

	for process in psutil.process_iter():

		try:

			pinfo = process.as_dict(attrs = ['pid','name','username']);

			pinfo['vms'] = process.memory_info.vms/(1024*1024),'MB';

			list.append(pinfo);

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):

			pass;


	return list;




def main():

	print("Application name is",sys.argv[0]);

	print(processlog());





if __name__=="__main__":


	main();