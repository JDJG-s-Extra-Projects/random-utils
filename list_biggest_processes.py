import os

import psutil

processes = psutil.process_iter()

current_process = psutil.Process(os.getpid())
username = current_process.username()

filtered_processes = list(filter(lambda process: process.username() == username, processes))

sorted_processes = sorted(filtered_processes, key=lambda process: process.memory_percent(), reverse=True)

for process in sorted_processes[:10]:
        if process.pid != current_process.pid and process.name():
                try:
                        print(process.name(), process.cmdline(), process.cwd(), process.username(), f"Memory Percent: {process.memory_percent()}%")

                except:
                        pass
                        # nothing here
                        # add something soon.
