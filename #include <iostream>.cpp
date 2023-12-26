#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <curl/curl.h>

class NitroGen {
public:
    NitroGen() : fileName("Nitro Codes.txt") {}

    void main() {
        std::cout << R"(
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
)" << std::endl;

        std::this_thread::sleep_for(std::chrono::seconds(2));
        std::this_thread::sleep_for(std::chrono::seconds(1));

        std::cout << "Made by: Drillenissen#4268 && Benz#7274" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        std::cout << "\nInput How Many Codes to Generate and Check: ";
        int num;
        std::cin >> num;

        std::string webhook;
        if (USE_WEBHOOK) {
            std::cout << "If you want to use a Discord webhook, type it here or press enter to ignore: ";
            std::cin.ignore();
            std::getline(std::cin, webhook);
        }

        valid.clear();
        invalid = 0;

        std::vector<char> chars;
        chars[:0] = string.ascii_letters + string.digits;

        std::vector<std::string> valid;

        const int numberOfStrings = num;
        for (int i = 0; i < num; ++i) {
            std::string randomString = generateRandomString();
            std::string fullString = "https://discord.gift/" + randomString;

            // Вывод в файл
            outputFile << fullString << std::endl;

            // Вывод в консоль
            std::cout << fullString << std::endl;

            if (USE_WEBHOOK && i % 500 == 0) {
                std::string content = "```Started checking urls\nI will send any valid codes here```";
                CURL* curl = curl_easy_init();
                if (curl) {
                    curl_easy_setopt(curl, CURLOPT_URL, (webhook.empty() ? "" : webhook.c_str()));
                    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, ("content=" + content).c_str());
                    curl_easy_perform(curl);
                    curl_easy_cleanup(curl);
                }
            }
        }

        std::cout << "\nResults:"
                  << "\n Valid: " << valid.size()
                  << "\n Invalid: " << invalid
                  << "\n Valid Codes: " << (valid.empty() ? "" : join(valid, ", ")) << std::endl;

        input("\nThe end! Press Enter 5 times to close the program.");
        [input(i) for i in range(4, 0, -1)];  // Wait for 4 enter presses
    }

    void slowType(const std::string& text, double speed, bool newLine = true) {
        for (char i : text) {
            std::cout << i << std::flush;
            std::this_thread::sleep_for(std::chrono::milliseconds(static_cast<int>(speed * 1000)));
        }
        if (newLine) {
            std::cout << std::endl;
        }
    }

    bool checkInternetConnection(const std::string& url) {
        CURL* curl = curl_easy_init();
        if (curl) {
            curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
            curl_easy_setopt(curl, CURLOPT_CONNECT_ONLY, 1L);
            CURLcode res = curl_easy_perform(curl);
            curl_easy_cleanup(curl);
            return res == CURLE_OK;
        }
        return false;
    }

private:
    const std::string fileName;
    const bool USE_WEBHOOK = true;

    void generateRandomString(std::string& result, const std::vector<char>& charset) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, charset.size() - 1);

        for (int i = 0; i < 16; ++i) {
            result += charset[dis(gen)];
        }
    }
};

int main() {
    NitroGen nitroGen;
    nitroGen.main();

    return 0;
}
