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
}
void loop() {
  if(Serial.available()>0){
    serialData =Serial.read();
    Serial.println(serialData);

    if(serialData=='A'){
      digitalWrite(uni,HIGH);
    }
    else if(serialData =='a'){
      digitalWrite(uni,LOW);
    }
    else if(serialData =='b'){
      digitalWrite(blake,LOW);
    }
    else if(serialData =='B'){
      digitalWrite(blake,HIGH);
    }
    else if(serialData =='c'){
      digitalWrite(odin,LOW);
    }
    else if(serialData =='C'){
      digitalWrite(odin,HIGH);
    }
    else if(serialData =='d'){
      digitalWrite(relay1,LOW);
    }
    else if(serialData =='D'){
      digitalWrite(relay1,HIGH);
    } 
    else if(serialData =='e'){
      digitalWrite(relay2,LOW);
    }
    else if(serialData =='E'){
      digitalWrite(relay2,HIGH);
    }
    else if(serialData =='f'){
      digitalWrite(relay3,LOW);
    }
    else if(serialData =='F'){
      digitalWrite(relay3,HIGH);
    }
    
    else if(serialData =='g'){
      digitalWrite(relay4,LOW);
    }
    else if(serialData =='G'){
      digitalWrite(relay4,HIGH);
    }
    
    else if(serialData =='h'){
      digitalWrite(relay5,LOW);
    }
    else if(serialData =='H'){
      digitalWrite(relay5,HIGH);
    }
    else if(serialData =='i'){
      digitalWrite(relay6,LOW);
    }
    else if(serialData =='I'){
      digitalWrite(relay6,HIGH);
    }
        else if(serialData =='j'){
      digitalWrite(relay7,LOW);
    }
    else if(serialData =='J'){
      digitalWrite(relay7,HIGH);
    }
        else if(serialData =='k'){
      digitalWrite(relay8,LOW);
    }
    else if(serialData =='K'){
      digitalWrite(relay8,HIGH);
    }
        else if(serialData =='l'){
      digitalWrite(relay9,LOW);
    }
    else if(serialData =='L'){
      digitalWrite(relay9,HIGH);
    }
        else if(serialData =='m'){
      digitalWrite(relay10,LOW);
    }
    else if(serialData =='M'){
      digitalWrite(relay10,HIGH);
    }
        else if(serialData =='n'){
      digitalWrite(relay11,LOW);
    }
    else if(serialData =='N'){
      digitalWrite(relay11,HIGH);
    }
        else if(serialData =='o'){
      digitalWrite(relay12,LOW);
    }
    else if(serialData =='O'){
      digitalWrite(relay12,HIGH);
    }
  }

}
