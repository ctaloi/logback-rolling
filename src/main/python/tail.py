import stat
import time, os

def follow(filename):

    file_obj = open(filename)
    st_file_obj_inode = fstat_inode(file_obj)

    while True:

        line = file_obj.readline()

        if not line:

            #Detect if the file has been moved or deleted
            st_filename_inode = stat_inode(filename)
            if st_filename_inode != st_file_obj_inode:
                print "Log roll detected - no data read and file inode has changed"
                file_obj.close()
                file_obj = open(filename)
                st_file_obj_inode = fstat_inode(file_obj)

            #Wait a bit for more data
            time.sleep(1)
            continue
        yield line

def stat_inode(filename):
    return os.stat(filename)[stat.ST_INO]

def fstat_inode(file_obj):
    return os.fstat(file_obj.fileno())[stat.ST_INO]


loglines = follow("../../../logFile.log")
for line in loglines:
    print line,
