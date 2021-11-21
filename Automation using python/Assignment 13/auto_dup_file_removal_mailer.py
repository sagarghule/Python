
import sys;
from auto_dup_file_removal import*;
import schedule;


def run():

	try:

		time1 = time.ctime();

		starttime = time.time();

		dict, scfile = finddupfile(sys.argv[1]);

		fname, dupfile = deletedupfile(dict);

		if is_connected():

			mailsender(fname, time1, scfile, dupfile, sys.argv[3]);


		endtime = time.time();

	except:
	
		pass;


def main():

	print("---"*26);

	print("Script Name:",sys.argv[0]);

	print("---"*26);

	print("Script by 'SB' \n All copyrights are reserve by SB ");

	print("---"*26);
	
	if len(sys.argv) == 2:

		if sys.argv[1].lower == "-help":

			print("This script is use for auto duplicate file removal");

			print("When this file run on with right commands it remove all duplicate files from specified directory");

			print("Please check usage to know how to use this script");

		if sys.argv[1].lower() == "-usage":
	
			print("Enter a command as given below");

			print("Script_name Directory_path Time_in_minute Mail_id");

			print("Script_name : Name of the script with .py extension");

			print("Directory_path : provide absulte path of directory from you want to delete duplicate file");

			print("Time_in_minute : Time interval to run the script in loop");

			print("Mail_id : Mail id to send a log file of deleted file");

	elif len(sys.argv) == 4:

		try:

			schedule.every(int(sys.argv[2])).minutes.do(run);

		
			while True:

				schedule.run_pending();
			
				time.sleep(1);

		except Exception:

			pass;
			

	else:

		print("Invaild input or use of script");

		print("please use command '%s -help' or '%s -usage' to use this script"%(sys.argv[0]));


	
		
if __name__=="__main__":

	main();
