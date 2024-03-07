import psutil 
import time

def main():
    print("Press CTRL C to stop bandwidth monitor.")
    #Get initial network stats
    prev_stats = psutil.net_io_counters()
    prev_received = prev_stats.bytes_recv
    prev_sent = prev_stats.bytes_sent

    try:
        while True:
            #Delay loop by:
            time.sleep(1)
            #Get network stats 
            new_stats = psutil.net_io_counters()
            new_received = new_stats.bytes_recv
            new_sent = new_stats.bytes_sent

            #Calculate difference between prev_stats and new_stats and convert to KB from bytes
            received_rate = (new_received - prev_received) / 1024
            sent_rate = (new_sent - prev_sent) / 1024
          
            #Set new variables to previous variables for next loop
            prev_received, prev_sent = new_received, new_sent
            print(f"Download rate: {received_rate: .2f} KB/s,  Upload rate: {sent_rate: .2f} KB/s")

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

if __name__ == "__main__":
    main()
