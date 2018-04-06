#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif
#include <ros.h>
#include <rosserial_arduino/Adc.h>

int num = 30;  // no. of samples over which to average

ros::NodeHandle nh;

rosserial_arduino::Adc adc_msg;
ros::Publisher p("adc", &adc_msg);

// average
int averageAnalog(int pin){
  int v=0;
  for(int i=0; i<num; i++) v+= analogRead(pin);
  return v/num;
}

void setup() {
  nh.getHardware()->setBaud(115200); // 115200
  nh.initNode();

  nh.advertise(p);

}


void loop() {
//  adc_msg.adc0 = averageAnalog(0);  
  adc_msg.adc1 = averageAnalog(1);
//  adc_msg.adc2 = averageAnalog(2);
  adc_msg.adc3 = averageAnalog(3);
  
  
  p.publish(&adc_msg);

  nh.spinOnce();

}
