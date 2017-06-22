Hey Cathodians

This is the readme file for useful information about our project.

Please add more info as you see necessary.

I am writing this python program in python3 so make sure you have that downloaded into your OS.

Our raspberrys will have the correct version so it should be good.

The idea of this repository is so we can add the different files to our project and have a log of the different changes that we have done as well as the documentation.

The initial python program that I have uploaded is just a simple program that starts udp cast, I will continue to work on it this week but if you guys can also contribute to the program it would be great. I know that this program might not run on windows or mac but they will run on our raspberrys.

--Progress so Far.--

Managed to keep udp-sender looping to initiate transfer as long as user keeps entering number 1.

After transfer completes User will be asked if another transfer is required. If user enters 1 it restarts udp-sender

If user presses any other key it will exit and display "Thanks for using data diode"


--Need work--
Program for udp-sender

The idea is to keep the program lopping and waiting for file to receive. 
We have to write a script for a filename and how its going to increment each time to have all different file names.
Also a function that searches for file that was just received to confirm that file exists in the current directory.
If file does not exists then that file while be transferred again until it finds it.
Implement led light confirmation in program.

