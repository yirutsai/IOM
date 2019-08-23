char serialData=' ';
int uni =13;
int blake =12;
int odin =11;
int com3 =3;
int com4 =4;
int com5 =5;
int com6 =6;
int com7 =7;
int com8=8;


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
      digitalWrite(com3,LOW);
    }
    else if(serialData =='D'){
      digitalWrite(com3,HIGH);
    } 
    else if(serialData =='e'){
      digitalWrite(com4,LOW);
    }
    else if(serialData =='E'){
      digitalWrite(com4,HIGH);
    }
    else if(serialData =='f'){
      digitalWrite(com5,LOW);
    }
    else if(serialData =='F'){
      digitalWrite(com5,HIGH);
    }
    
    else if(serialData =='g'){
      digitalWrite(com6,LOW);
    }
    else if(serialData =='G'){
      digitalWrite(com6,HIGH);
    }
    
    else if(serialData =='h'){
      digitalWrite(com7,LOW);
    }
    else if(serialData =='H'){
      digitalWrite(com7,HIGH);
    }
    else if(serialData =='i'){
      digitalWrite(com8,LOW);
    }
    else if(serialData =='I'){
      digitalWrite(com8,HIGH);
    }
  }

}
