
#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class listen:
    #Callback function to print the subscribed data on the terminal
   def __init__(self):
        self.data1 = ""
        self.data2 = ""
   def callback0(self,data):
        self.data1= data
   def callback1(self,data):
        self.data2= data
   

    
if __name__ == '__main__':
    #initialize the subscriber node called 'listener'
    rospy.init_node('listener', anonymous=True)
    l = listen() 
    #This is to subscribe to the messages from the topic named 'chatter'
    rospy.Subscriber("listen1", String, l.callback0)
    rospy.Subscriber("listen2", String, l.callback1)
    rospy.loginfo(l.data1 + " "  + l.data2)  
    
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()