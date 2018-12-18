int pingPin1 = 10;
int pingPin2 = 11;
int durationR,durationL,R,L;
void setup(){
Serial.begin(9600);
}
void loop(){
pinMode(pingPin1,OUTPUT);
digitalWrite(pingPin1,LOW);
delayMicroseconds(2);
digitalWrite(pingPin1,HIGH);
delayMicroseconds(5);
digitalWrite(pingPin1,LOW);
pinMode(pingPin1,INPUT);
durationR = pulseIn(pingPin1,HIGH);
R = durationR/2/29;

pinMode(pingPin2,OUTPUT);
digitalWrite(pingPin2,LOW);
delayMicroseconds(2);
digitalWrite(pingPin2,HIGH);
delayMicroseconds(5);
digitalWrite(pingPin2,LOW);
pinMode(pingPin2,INPUT);
durationL = pulseIn(pingPin2,HIGH);
L = durationL/2/29;

Serial.print(R);
Serial.print(",");
Serial.print(L);
Serial.println(",");
delay(500);
}
