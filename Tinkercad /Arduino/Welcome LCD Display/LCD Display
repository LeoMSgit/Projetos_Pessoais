#include <LiquidCrystal_I2C.h>

// Inicializa o LCD com endereço I2C 0x20, 16 colunas e 2 linhas
LiquidCrystal_I2C lcd_1(0x20, 16, 2);

void setup()
{
  lcd_1.init();
  lcd_1.backlight();
  lcd_1.display();
}

void loop()
{
  // Primeira mensagem
  lcd_1.clear();
  lcd_1.setCursor(0, 0);
  lcd_1.print("WELCOME TO MY");
  lcd_1.setCursor(0, 1);
  lcd_1.print("TINKERCAD PAGE!");
  delay(2000); // Espera por 2000 milissegundos

  // Segunda mensagem
  lcd_1.clear();
  lcd_1.setCursor(0, 0);
  lcd_1.print("BE SURE TO CHECK");
  lcd_1.setCursor(0, 1);
  lcd_1.print("MY OTHER PROJECTS");
  delay(2000); // Espera por 2000 milissegundos

  // Terceira mensagem
  lcd_1.clear();
  lcd_1.setCursor(0, 0);
  lcd_1.print("And my github");
  lcd_1.setCursor(0, 1);
  lcd_1.print("git/LeoMSgit");
  delay(2000); // Espera por 2000 milissegundos
}
