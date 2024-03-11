#include <MD5.h>

void setup()
{
  //initialize serial
  Serial.begin(9600);
  while (!Serial);
  //give it a second
  delay(1000);

  //MD5 hash
  Serial.print("The quick brown fox jumps over the lazy dog hash: ");
  unsigned char* hash=MD5::make_hash("The quick brown fox jumps over the lazy dog");
  //generate the digest (hex encoding) of our hash
  char *md5str = MD5::make_digest(hash, 16);
  free(hash);
  //print it on our serial monitor
  Serial.println(md5str);
  //Give the Memory back to the System if you run the md5 Hash generation in a loop
  //free(md5str);
}

void loop()
{
}