import psutil;
import platform;
from os import *;
from datetime import datetime;
 
def cpu_Info_os():
	print("----Marvellous Infosystem CPU Info OS----");
	if platform.system() == "Windows":
		return platform.processor();
	elif platform.system() == "Darwin":
		command = '/usr/sbin/syscti -n manchdep.cpu.brand_string';
		return popen(command).read().strip();
	elif platform.system() == "Linux":
		command = '/proc/cpuinfo';
		return popen(command).read().strip()
	return 'platform not identified';

def get_size(bytes, sufix ="B"):
	factor =1024;
	for unit in ["","K","M","G","T","P"]:
		if bytes < factor:
			return f"{bytes:.2f}{unit}{sufix}";
		bytes /= factor;


def platform_info():
	print("----System Information----");
	uname = platform.uname();
	print(f"System:{uname.system}");
	print(f"Node Name:{uname.node}");
	print(f"Release:{uname.release}");
	print(f"Version:{uname.version}");
	print(f"Machine:{uname.machine}");
	print(f"Processor:{uname.processor}");


def boot_info():
	print("----Boot Time----");
	boot_time_timestamp = psutil.boot_time();
	bt = datetime.fromtimestamp(boot_time_timestamp)
	print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}") ;

def cpu_info():
	print("----CPU Info----");
	print("Physical cores:", psutil.cpu_count(logical=False));
	print("Total cores:", psutil.cpu_count(logical=True));

	cpufreq = psutil.cpu_freq()
	print(f"Max Frequency: {cpufreq.max:.2f}Mhz");
	print(f"Min Frequency: {cpufreq.min:.2f}Mhz");
	print(f"Current Frequecy:{cpufreq.current:.2f}Mhz");

	print("CPU Usage Per Core");
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
		print(f"Core{i} : {percentage}%");
	print(f"Total CPU Usage: {psutil.cpu_percent()}%");

def ram_usage():
	print("----Memory Information----");
	
	svmem = psutil.virtual_memory();
	print(f"Total: {get_size(svmem.total)}");
	print(f"Available: {get_size(svmem.available)}");
	print(f"Used: {get_size(svmem.used)}");
	print(f"Percentage: {svmem.percent}%");
	print(f"----SWAP----");

	swap = psutil.swap_memory();
	print(f"Total: {get_size(swap.total)}");
	print(f"Free: {get_size(swap.free)}");
	print(f"Used: {get_size(swap.used)}");
	print(f"Percentage: {swap.percent}%");


def disk_info():
	print("----Disk Information----");
	print("Partition and Usage:");
	
	partitions = psutil.disk_partitions();
	for partition in partitions:
		print(f"=== Device: {partition.device}===");
		print(f"  Mountpoint: {partition.mountpoint}");
		print(f" FIle system type: {partition.fstype}");
		try: 
			partition_usage = psutil.disk_usage(partition.mountpoint);
		except PermissionError:
			continue;
		print(f" Total Size: {get_size(partition_usage.total)}");
		print(f" Used: {get_size(partition_usage.used)}");
		print(f" Free: {get_size(partition_usage.free)}");
		print(f" Percentage: {partition_usage.percent}%");
		disk_io = psutil.disk_io_counters();
		print(f"Total read: {get_size(disk_io.read_bytes)}");
		print(f"Total write: {get_size(disk_io.write_bytes)}");



def main():
	txt = '''
1 . Operating system information.
2 . Machine information.
3 . CPU information.
4 . Boot Time.
5 . Ram Usage.
6 . Hard Drive Information.
7 . Exit
'''
	ch = 0;
	while(ch != 7):
		
		print(txt);

		ch = int(input("Enter choice : "));
		
		if ch == 1:
			cpu_Info_os();
		elif ch == 2:
			platform_info();
		elif ch == 3:
			cpu_info();
		elif ch == 4:
			boot_info();
		elif ch == 5:
			ram_usage();
		elif ch == 6:
			disk_info();
		
	print("Thanks For Using Our Application");

if __name__=='__main__':
	main();















