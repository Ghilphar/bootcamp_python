import sys
import time

def ft_progress(lst):
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        elapsed_time = time.time() - start_time
        # estimated time of arrival
        eta = (elapsed_time / (i + 1)) * total - elapsed_time if i != 0 else 0

        percent_complete = (i + 1) / total * 100
        bar_length = 50
        fileld_chars = int(bar_length * (i + 1) // total)        
        bar = '=' * fileld_chars + '>' + ' ' * (bar_length - fileld_chars - 1)
        
        sys.stdout.write(f"\rETA: {eta:.2f}s [{percent_complete:.0f}%][{bar}] {i+1}/{total} | elapsed time {elapsed_time:.2f}s")
        sys.stdout.flush()

        yield item
        
    sys.stdout.write("\n")
    sys.stdout.flush()
