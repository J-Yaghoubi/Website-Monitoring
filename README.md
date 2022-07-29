# Website Monitoring
A handy and easy-to-use python script for monitoring the functionality of the website by checking its status.          
If the website does not returns 200 as the status code, the script will send an email to the defined destination and tell the user about problem.     

All you should do is customizing this section of code depending on your information, and be sure the dependencies are installed on your machine. That's it! 


<div>

```python
    config = {
        
        # check time in second 
        # the website that we want to monitor it 
        # your email address
        # your email password  
        # receiver email 
        'interval'      : 5,                                  
        'target'        : 'http://google.com',       
        'sender_email'  : 'Email_Address',       
        'sender_pass'   : 'Email_Password',         
        'receiver_email': 'Destination Email',   

        # email service host and port
        'host' : 'smtp.gmail.com',                      
        'port' : 578,                          

        # sended email subject and massage
        'email_subject' : 'Target is out of range!',      
        'email_massage' : 'Please check the functionality of your site', 

        # stop when find a problem or do looping(repeatedly checking and emailing)  
        'looping' : False,    
    }
```

</div>



### Dependencies
[Requests](https://pypi.org/project/requests)