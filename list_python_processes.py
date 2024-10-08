import os
import psutil

processes = psutil.process_iter()

current_process = psutil.Process(os.getpid())


for process in processes:
	if process.pid != current_process.pid and process.name().lower().startswith("python"):
		print(process.name(), process.cmdline(), process.cwd(), process.username())
