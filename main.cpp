#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <string>
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
    return "output/" + generateRandomString() + ".txt";
}

// Callback-функция для libcurl
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* output) {
    size_t total_size = size * nmemb;
    output->append((char*)contents, total_size);
    return total_size;
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

    // Генерация и вывод строк в файл
    const int numberOfStrings = 10;
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

    // Отправка файла на GitHub
    CURL* curl;
    CURLcode res;

    // Инициализация библиотеки libcurl
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl) {
        // Формирование URL GitHub API
        std::string githubApiUrl = "https://api.github.com/repos/kvilial/kvilafl/contents/output/" + fileName;

        // Открытие файла для чтения
        std::ifstream fileToSend(fileName, std::ios::binary);
        std::string fileContents((std::istreambuf_iterator<char>(fileToSend)), std::istreambuf_iterator<char>());

        // Формирование заголовков HTTP-запроса
        struct curl_slist* headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        headers = curl_slist_append(headers, "User-Agent: curl/7.78.0");
        headers = curl_slist_append(headers, "Authorization: Bearer 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"); // Замените YOUR_GITHUB_TOKEN на ваш токен

        // Установка параметров HTTP-запроса
        curl_easy_setopt(curl, CURLOPT_URL, githubApiUrl.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, fileContents.c_str());

        // Выполнение HTTP-запроса
        res = curl_easy_perform(curl);

        // Проверка результата выполнения запроса
        if (res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

        // Очистка ресурсов libcurl
        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }

    // Очистка ресурсов libcurl
    curl_global_cleanup();

    return 0;
}
