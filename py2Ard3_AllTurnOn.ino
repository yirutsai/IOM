char serialData=' ';
int uni =30;
int blake =31;
int odin =32;
int relay1 =2;
int relay2 =3;
int relay3 =4;
int relay4=5;
int relay5 =6;
int relay6 =7;
int relay7 =8;
int relay8 =9;
int relay9=10;
int relay10=11;
int relay11=12;
int relay12=13;


void setup() {

  Serial.begin(9600);
  Serial.println("Ready");
  for(int i=2;i<=13;i++){
    pinMode(i,OUTPUT);
  }
  for(int i=30;i<=32;i++){
    pinMode(i,OUTPUT);
  }
}
void loop() {
  if(Serial.available()>0){
    serialData =Serial.read();
    Serial.println(serialData);

    if(serialData=='A'){
      for(int i=2;i<=13;i++){
        digitalWrite(i,HIGH);
      }
      for(int i=30;i<=32;i++){
        digitalWrite(i,HIGH);
      }
    }
    else if(serialData =='a'){
      for(int i=2;i<=13;i++){
        digitalWrite(i,LOW);
      }
      for(int i=30;i<=32;i++){
        digitalWrite(i,LOW);
      }
    }
  }

}
