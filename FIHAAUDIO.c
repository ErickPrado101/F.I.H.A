#include <SoftwareSerial.h>
#include <GoogleTTS.h>
#include <SPI.h>
#include <SD.h>

SoftwareSerial mySerial(10, 11); 
GoogleTTS tts;
File myFile; 

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);

 
  if (!SD.begin(4)) {
    Serial.println("Falha ao inicializar o cartão SD!");
    return;
  }

  
  tts.setLanguage("pt"); 
  tts.setVoiceType("F1"); 
}

void loop() {
  if (mySerial.available()) {
    String question = mySerial.readStringUntil('\n');
    question.trim(); 

   
    String answer = getAnswerFromChatGPT(question);

   
    saveAnswerToSD(answer);

   
    convertTextToSpeech(answer);

   
    playAudioOnSpeaker();

    Serial.println("Pergunta: " + question);
    Serial.println("Resposta: " + answer);
  }
}

String getAnswerFromChatGPT(String question) {}

void saveAnswerToSD(String answer) {
  myFile = SD.open("resposta.txt", FILE_WRITE); 
  if (myFile) {
    myFile.println(answer);
    myFile.close(); 
    Serial.println("Resposta salva no cartão SD!");
  } else {
    Serial.println("Erro ao salvar resposta no cartão SD!");
  }
}

void convertTextToSpeech(String answer) {
  String audioFile = "resposta.mp3"; 
  tts.synthesize(answer, audioFile); 
  Serial.println("Resposta convertida para áudio!");
}

void playAudioOnSpeaker() {}
  