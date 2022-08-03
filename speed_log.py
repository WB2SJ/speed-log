import datetime
import speedtest
speed = speedtest.Speedtest()


def main():
    # open log file
    f = open("speed_log.txt", "a")

    timestamp = datetime.datetime.now()

    # run speed tests
    download_megabits = speed.download()/1024/1024
    upload_megabits = speed.download()/1024/1024

    # output and save results
    print(download_megabits, upload_megabits)
    output = f"{timestamp.isoformat()} - Download: {download_megabits}, Upload: {upload_megabits}\n"
    print(output)
    f.write(output)
    f.close()


if __name__ == '__main__':
    main()
