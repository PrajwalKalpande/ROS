#!/usr/bin/env python
# license removed for brevity

#import the rospy package and the String message type 
import rospy
from std_msgs.msg import String

#function to publish messages at the rate of 10 per second
def talker():
    #define a topic to which the messages will be published
    pub = rospy.Publisher('listen1', String, queue_size=10)
    
    #initialize the Publisher node
    #Setting anonymous=True will append random integers at the end of the publisher node
    rospy.init_node('talker1', anonymous=True)
    
    #publishes at a rate of 2 messages per second
    rate = rospy.Rate(10) # 10hz
    
    #Keep publishing the messages until the user interrupts
    while not rospy.is_shutdown():
        hello_str = "I am not a psychopath, Anderson."
	
	#display the message on the terminal
        rospy.loginfo(hello_str)
	
	#publish the message to the topic
        pub.publish(hello_str)
	
	#rate.sleep() will help wait long enough to maintain the desired rate through the loop
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    #to capture the Interrupt signals that could be thrown by rate.sleep()
    except rospy.ROSInterruptException:
        pass
