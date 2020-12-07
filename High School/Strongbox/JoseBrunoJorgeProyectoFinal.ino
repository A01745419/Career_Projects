//Proyecto Final
//José Luis Madrigal, Bruno Leonardo Larios y Jorge Isidro Blanco
//Caja fuerte
#include <Arduino.h>
#include <TM1637Display.h>
int CLK = A4; // el pin CLK está conectado al pin análogo 1
int DIO = A5; // el pin DIO está conectado al pin análogo 2
#include <Servo.h> 
Servo jbj_servo;
TM1637Display display(DIO,CLK);
int jbj_cont1 = 0;
int jbj_cont2 = 0;
int jbj_cont3 = 0;
int jbj_pausa=100;
int jbj_6 = 6;     // led 1
int jbj_7 = 7;    // led 2
int jbj_8 = 8;   // led 3
int jbj_rojo=11;
int jbj_verde = 9;
int jbj_azul = 10;
int jbj_boton1=2;      // boton1 en el pin 2
int jbj_boton2=3;     // boton2 en el pin 3
int jbj_boton3=4;    // boton3 en el pin 4
int jbj_boton4=5;   // boton 4 en el pin 5
int jbj_buzzer= 0; // pin buzzer

void ledjbj_verde () {
  digitalWrite(jbj_verde,HIGH);  // enciendo led verde
  delay (500);                  // pausa de .5 segundos
  digitalWrite(jbj_verde,LOW); // se apaga el led verde
}

void ledjbj_azul () {
  digitalWrite(jbj_azul,HIGH);   // enciendo led azul 
  digitalWrite(jbj_verde,LOW);  // apago led verde
  delay (500);                 // pausa de .5 segundos
  digitalWrite(jbj_azul,LOW); // apago led azul
}

void prendejbj_buzer_servo () {
  tone(jbj_buzzer,10);         // sonido tipo grillito
  jbj_servo.write(100);       // poner servo a la mitad
}

void apagajbj_buzer_servo () {
  noTone(jbj_buzzer);         // silencia el buzzer
  jbj_servo.write(0);        // poner servo en posición inicial
}

void setup() {
// leds normales
pinMode(jbj_6,OUTPUT); 
pinMode(jbj_7,OUTPUT); 
pinMode(jbj_8,OUTPUT); 
// RGB
pinMode(jbj_rojo,OUTPUT); 
pinMode(jbj_verde,OUTPUT); 
pinMode(jbj_azul,OUTPUT); 
// botones
pinMode(jbj_boton1,INPUT_PULLUP); 
pinMode(jbj_boton2,INPUT_PULLUP);
pinMode(jbj_boton3,INPUT_PULLUP);
pinMode(jbj_boton4,INPUT_PULLUP);
// buzzer
pinMode(jbj_buzzer,OUTPUT); 
// pantalla serial
Serial.begin(9600); // se abre pantalla serial
//Servo
jbj_servo.attach(A0); // pin analógio 0 donde está conectado el servo 
jbj_servo.write(0); // poner servo en posición inicial

display.clear();
//display.setBrightness(0x0a); //brillo del display no tan intenso
display.setBrightness(0xF); //brillo del display muy intenso
Serial.begin(9600); //Inicio el puerto serie
}


void loop()
{
//display.showNumberDec(con,false,2,2);//columna posición
delay(300); // pausa de .3 segundos

if (digitalRead(jbj_boton1)==LOW){               //si se oprime el botón 3
jbj_cont1 = jbj_cont1 + 1;                      //se aumenta una unidad en el contador 1
display.showNumberDec(jbj_cont1,true,2,2);     //columna posición
}

if (digitalRead(jbj_boton2)==LOW) {              //si se oprime el botón 2
jbj_cont2 = jbj_cont2 + 1;                      //se aumenta una unidad en el contador 2
display.showNumberDec(jbj_cont2,true,2,2);     //columna posición
}

if (digitalRead(jbj_boton3)==LOW){              //se se oprime el botón 3
jbj_cont3 = jbj_cont3 + 1;                     //se aumenta una unidad en el contador 3
display.showNumberDec(jbj_cont3,true,2,2);    //columna posición
}

if (digitalRead(jbj_boton4)==LOW){               //si se oprime el botón 4
jbj_cont1 = 0;
jbj_cont2 = 0;       //contadores se reinician
jbj_cont3 = 0;
display.showNumberDec(jbj_cont1,true,2,2);     //columna posición
digitalWrite(jbj_rojo,HIGH);                  // enciendo led rojo
tone(jbj_buzzer,100);                        // sonido tipo alarma
digitalWrite(jbj_verde,LOW);                //enciendo led verde
delay (3000);                              // pausa de 3 segundos
digitalWrite(jbj_rojo,LOW);               // apago led rojo
noTone(jbj_buzzer);                      // silencia el buzzer
}



if ((jbj_cont1 == 2) and (jbj_cont2 == 5) and (jbj_cont3 == 3)) // contraseña = 2,5,3 - si cada contador tiene su número correspondiente
{
prendejbj_buzer_servo ();
}
else
{
apagajbj_buzer_servo ();
}

if ((jbj_cont1 == 2) and (jbj_cont2 == 5) and (jbj_cont3 == 3))  // contraseña = 2,5,3 - si cada contador tiene su número correspondiente
{
ledjbj_verde ();
}
else
{
ledjbj_azul ();
}

}
