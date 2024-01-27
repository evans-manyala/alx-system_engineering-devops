# 0x05. Processes and signals
    Welcome to this REPO, here we continue to run several bash scripts that perform various tasks when executed

    => TASK 0 - What is my PID:
        Bash script that displays its own PID.
    => TASK 1 - List your processes:
        Bash script that displays a list of currently running processes.
            Requirements:
            * Must show all processes, for all users, including those which might not have a TTY.
            * Display in a user-oriented format
            * Show process hierarchy
    => TASK 2 - Show your Bash PID
        Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
            Requirements:
            * You cannot use pgrep
            * The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
    => TASK 3 - Show your Bash PID made easy
        Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
            Requirements:
            * You cannot use ps
    => TASK 4 - To infinity and beyond
        Bash script that displays To infinity and beyond indefinitely.
            Requirements:
                In between each iteration of the loop, add a sleep 2
    => TASK 5 - Don't stop me now!
        Write a Bash script that stops 4-to_infinity_and_beyond process.
            Requirements:
            *  You must use kill
            * Terminal #0