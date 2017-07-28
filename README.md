# IoT-SPIT
## Project 1 : A GUI to broadcast a message String to more than 1000 users using them GSM modem in Phones  
### Day 1 26/07/17
    -Broke the project into 3 parts designing the GUI, extracting the attached file given by the user and passing it,
     using Minicom to send a message using its CLI to another number and then creating our own code to do the same. 
    -Researched on the topics of how to design a GUI in python, File handling in python, Minicom, GSM modems and 
     AT-commands.
    -Run multiple tests to connect the device (Smartphone) as a modem and establish a running network.
        --Problem Faced: abstraction layer problem.
    -Successfully designed the GUI and were able to extract numbers from different file types like .txt, .xlxs, .csv .  

### Day 2 27/07/17
    -Successfully combined the GUI with the extraction code and were able to obtain the output on the terminal
    -The extracted output has been stored in a dictionary in python for using it in the search algorithm which is
     to be created.
    -Wrote Python code for sending a text message using AT commands with the help of PySerial package
    -Messages are successfully being sent to other devices by using a Wismo GSM modem.
    -A successful call was placed from a single Samsung Smartphone. 
        --Problem Faced: the abstraction layer problem still persists due to which messages from other
          device cannot be sent.
    
### Day 3 28/07/17
    -Merged all the three code files together and successfully sent a message to multiple devices using the 
     code and the Wismo GSM modem.
        --Problem : Still could not achieve a serial connection with the Smartphone (+CMS ERROR: 302).
    -Creating an algorithm which helps in searching and selecting only those to whom the message must be sent, 
     in the GUI.
    -Started creating an executable file
