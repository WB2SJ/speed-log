import datetime
import os
import speedtest


def main():
    timestamp = datetime.datetime.now()

    # init the speedtest class
    speed = speedtest.Speedtest()

    # open log file
    f = open(os.path.expanduser('~') + '/speed_log.txt', "a")

    # run speed tests
    download_megabits = speed.download()/1024/1024
    upload_megabits = speed.upload()/1024/1024

    # output and save results
    output = f"{timestamp.isoformat()} - Download: {download_megabits}, Upload: {upload_megabits}\n"
    # print(output)
    f.write(output)
    f.close()
    return 0

if __name__ == '__main__':
    main()
