#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <curl/curl.h>

// Генерация случайного символа
char getRandomChar() {
    const char charset[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const int charsetSize = sizeof(charset) - 1;
    return charset[rand() % charsetSize];
}

// Генерация случайной строки из 16 символов
std::string generateRandomString() {
    std::string result;
    for (int i = 0; i < 16; ++i) {
        result += getRandomChar();
    }
    return result;
}

// Генерация случайного имени файла
std::string generateRandomFileName() {
    return "output.txt";
}

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(0));

    // Генерация случайного имени файла
    std::string fileName = generateRandomFileName();

    // Открытие файла для записи
    std::ofstream outputFile(fileName);

    if (!outputFile.is_open()) {
        std::cerr << "Не удалось открыть файл для записи." << std::endl;
        return 1;
    }

    // Генерация и вывод строк в файл и в консоль
    const int numberOfStrings = 10000; // Вы можете изменить количество строк по вашему желанию
    for (int i = 0; i < numberOfStrings; ++i) {
        std::string randomString = generateRandomString();
        std::string fullString = "https://discord.gift/" + randomString;

        // Вывод в файл
        outputFile << fullString << std::endl;

        // Вывод в консоль
        std::cout << fullString << std::endl;
    }

    // Закрытие файла
    outputFile.close();

    std::cout << "Файл успешно создан: " << fileName << std::endl;

    // Копирование вывода в буфер обмена
    std::system(("cat " + fileName + " | xclip -selection clipboard").c_str()); // Для Linux
    // Или std::system(("type " + fileName + " | clip").c_str()); // Для Windows

    return 0;
}
