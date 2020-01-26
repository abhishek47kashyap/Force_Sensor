/* 
 * rosserial ADC Example
 * 
 * This is a poor man's Oscilloscope.  It does not have the sampling 
 * rate or accuracy of a commerical scope, but it is great to get
 * an analog value into ROS in a pinch.
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif
#include <ros.h>
#include <rosserial_arduino/Adc.h>

ros::NodeHandle nh;

rosserial_arduino::Adc adc_msg;
ros::Publisher p("adc", &adc_msg);

void setup()
{ 
  nh.initNode();

  nh.advertise(p);
}


long adc_timer;

void loop()
{

  adc_msg.adc0 = analogRead(0);  
  p.publish(&adc_msg);

  nh.spinOnce();
}

