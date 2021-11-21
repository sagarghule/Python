This script is designed for creating log of all 
running processes on machine in specified directory
and send that file by mail to specified mail id. 
This code contain four function as processlog, logprocess
is_connected and mail_sender. 
processlog give us list of all running processes on machine 
with their Pid,name and username.
logprocess write all process information into the log file 
this log file is created at run time in specified directory. 
The directory path is taken from user.
is_connected checks internet connection is available or
not and return true or false.
mail_sender is to send mail to given mail id with
that log file.
This functions are called from main function the directory name 
to create log file is taken as command line argument.
Also show the execution time on console.
