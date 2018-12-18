#include<Servo.h>
Servo servoright;
Servo servoleft;
int time = 1000;
int pingPin1 = 10;
int pingPin2 = 11;
long durationR,durationL,R,L;
bool cgo = false;
String state = "sstop";
void setup(){
  servoright.attach(12);
  servoleft.attach(13);
  Serial.begin(9600);
}
void loop(){

  //計算左右超音波的距離
  //disR();
  //disL();
  pinMode(pingPin1,OUTPUT);
  digitalWrite(pingPin1,LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin1,HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin1,LOW);
  pinMode(pingPin1,INPUT);
  durationR = pulseIn(pingPin1,HIGH);
  R = durationR/58;
  
  pinMode(pingPin2,OUTPUT);
  digitalWrite(pingPin2,LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin2,HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin2,LOW);
  pinMode(pingPin2,INPUT);
  durationL = pulseIn(pingPin2,HIGH);
  L = durationL/58;
  
  Serial.print(R);
  Serial.print(",");
  Serial.print(L);
  Serial.println(",");

  //自動模式
  if(cgo == true){
    if(R<30&& L<30){
      CR();
    }
    else if(R<30 && L>30){
      CL();
    }
    else if(R>30&& L<30){
      CR();
    }
    else{
      CF();
    }
  }
  else if(state=="sstop"){
    CS();
  }
  else if(state=="sfoword"){
    CF();
  }
  else if(state=="sback"){
    CB();
  }
  else if(state=="sleft"){
    CL();
  }
  else if(state=="sright"){
    CR();
  }
  else if(state=="sfl"){
    CFL();
  }
  else if(state=="sfll"){
    CFLL();
  }
  else if(state=="sfr"){
    CFR();
  }
  else if(state=="sfrr"){
    CFRR();
  }


  
  char c;

  
  if(Serial.available()>0)
  {
    c=Serial.read();
    if(c == 'T'){
      cgo = true;
      state = "sfoword";
    }
    else if(c == 'Q'){
      cgo = false;
      state = "sstop";
    }
    else if(c == 'F'){
      CF();
      state = "sfoword";
    }
    else if(c == 'S'){
      CS();
      state = "sstop";
    }
    else if(c == 'L'){
      CL();
      state = "sleft";
    }
    else if(c == 'R'){
      CR();
      state = "sright";
    }
    else if(c == 'B'){
      CB();
      state = "sback";
    }
    else if(c == '1'){
      CFL();
      state = "sfl";
    }
    else if(c == '2'){
      CFLL();
      state = "sfll";
    }
    else if(c == '3'){
      CFR();
      state = "sfr";
    }
    else if(c == '4'){
      CFRR();
      state = "sfrr";
    }
  }


  delay(time);
}

long disR(){
  pinMode(pingPin1,OUTPUT);
  digitalWrite(pingPin1,LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin1,HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin1,LOW);
  pinMode(pingPin1,INPUT);
  durationR = pulseIn(pingPin1,HIGH);
  R = durationR/58;
  return (pulseIn(pingPin1,HIGH)/58);
}

long disL(){
  pinMode(pingPin2,OUTPUT);
  digitalWrite(pingPin2,LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin2,HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin2,LOW);
  pinMode(pingPin2,INPUT);
  durationL = pulseIn(pingPin2,HIGH);
  L = durationL/58;
  return (pulseIn(pingPin2,HIGH)/58);
}

void CF(){
  servoleft.writeMicroseconds(1560);
  servoright.writeMicroseconds(1440);
}

void CS(){
  servoleft.writeMicroseconds(1500);
  servoright.writeMicroseconds(1500);
}

void CB(){
  servoleft.writeMicroseconds(1400);
  servoright.writeMicroseconds(1600);
}

void CL(){
  servoleft.writeMicroseconds(1400);
  servoright.writeMicroseconds(1400);
}

void CR(){
  servoleft.writeMicroseconds(1600);
  servoright.writeMicroseconds(1600);
}

void CFL(){
  servoright.writeMicroseconds(1440);
  servoleft.writeMicroseconds(1560);
}
void CFLL(){
  servoright.writeMicroseconds(1350);
  servoleft.writeMicroseconds(1550);
}
void CFR(){
  servoright.writeMicroseconds(1450);
  servoleft.writeMicroseconds(1570);
}
void CFRR(){
  servoright.writeMicroseconds(1450);
  servoleft.writeMicroseconds(1650);
}
void CBL(){
  servoleft.writeMicroseconds(1450);
  servoright.writeMicroseconds(1700);
}

void CBF(){
  servoleft.writeMicroseconds(1300);
  servoright.writeMicroseconds(1550);
}

void CSF(){
  servoright.writeMicroseconds(1480);
  servoleft.writeMicroseconds(1520);
}

void CSB(){
  servoleft.writeMicroseconds(1480);
  servoright.writeMicroseconds(1520);
}



