Logback Rolling File Test
=========================

Test the behaviour of logback when rolling files with the RollingFileAppender.

Running uk.co.arunhorne.Main will cause log messages to be written to a file every second.
The configuration in resources/logback.xml rolls files every minute.

Using the following commands we can determine that when rolled, a log file retains its inode
value.

    ahorne@lorelei:logback-rolling$ ls -il logFile*
    12812187 -rw-r--r--  1 ahorne  wheel  184 21 Jun 17:30 logFile.log

    ahorne@lorelei:logback-rolling$ ls -il logFile*
    12812187 -rw-r--r--  1 ahorne  wheel  4082 21 Jun 17:31 logFile.2012-06-21-17-30.log
    12812198 -rw-r--r--  1 ahorne  wheel   186 21 Jun 17:31 logFile.log    

This is useful information as it allows us to write a process that consumes logFile.log as it
is written to, but also behave correctly when the logFile is rolled.

Code to demonstrate this approach is included in this package. Run Main.java to produce a logfile
via logback - a new entry will be added to this log every second and the file will be rolled every
minute.

By running the enclosed Python script you will see it tail the logFile and detect the rolled file
correctly.

