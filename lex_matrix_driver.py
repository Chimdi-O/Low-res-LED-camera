

int index = 0;
int rowPins[3] = {11,10,9}; 
int columnPins[4] = {6,5,4,3}; 

const int dataLength = 12;
char incomingData[dataLength*3 +1]; 
int pixelData[dataLength];

void writeColumn(int data[],int columnNum){
  digitalWrite(columnPins[columnNum],LOW);
  analogWrite(rowPins[0],data[0]);
  analogWrite(rowPins[1],data[1]);
  analogWrite(rowPins[2],data[2]);

  delay(2);
  digitalWrite(columnPins[columnNum],HIGH);
  digitalWrite(rowPins[0],LOW);
  digitalWrite(rowPins[1],LOW); 
  digitalWrite(rowPins[2],LOW); 


}

void processing(char* data){ 
  int valueIndex = 0; 
  for(int i = 0; i < dataLength * 3; i += 3){ 
    char temp[4]; 
    temp[0] = data[i];
    temp[1] = data[i+1];
    temp[2] = data[i+2]; 
    temp[3] = '\0';

    pixelData[valueIndex] = atoi(temp);
    valueIndex++;  
  }
}


void setup() {
  // put your setup code here, to run once:

  // row initialization
  pinMode(rowPins[0],OUTPUT);
  pinMode(rowPins[1],OUTPUT);
  pinMode(rowPins[2],OUTPUT);
  digitalWrite(rowPins[0],LOW);
  digitalWrite(rowPins[1],LOW);
  digitalWrite(rowPins[2],LOW);

  //column initialization
  pinMode(columnPins[0],OUTPUT); 
  pinMode(columnPins[1],OUTPUT);
  pinMode(columnPins[2],OUTPUT);
  pinMode(columnPins[3],OUTPUT);
  digitalWrite(columnPins[0],HIGH);
  digitalWrite(columnPins[1],HIGH);
  digitalWrite(columnPins[2],HIGH);
  digitalWrite(columnPins[3],HIGH);


}

void loop() {
 
    if (Serial.read() == '/'){
  
    index = 0; 
    while(index <= dataLength  * 3){ 
       if (Serial.available()){ 
      incomingData[index] = Serial.read(); 
      index++; 
      delay(2); 
          }
    }
      incomingData[index] = '\0';

      
      processing(incomingData); 
  

  for(int i = 0; i < dataLength-2;i+3){
    int data[] = {pixelData[i],pixelData[i+1],pixelData[i+2]};
    writeColumn(data,i);
    delay(2);}}

    
  }
