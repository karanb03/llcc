#include <iostream>
#include <vector>
#include <sstream>

std::vector<std::string> generate_three_address_code(std::string expression) {
    std::vector<std::string> tokens;
    std::istringstream iss(expression);
    for(std::string s; iss >> s; )
        tokens.push_back(s);

    int temp_var_counter = 1;
    std::vector<std::string> three_address_code;

    for(int i = 2; i < tokens.size(); i += 2) {
        if(i == 2)
            three_address_code.push_back("t" + std::to_string(temp_var_counter) + " = " + tokens[i-1] + " " + tokens[i] + " " + tokens[i+1]);
        else
            three_address_code.push_back("t" + std::to_string(temp_var_counter) + " = t" + std::to_string(temp_var_counter-1) + " " + tokens[i] + " " + tokens[i+1]);

        temp_var_counter++;
    }

    three_address_code.push_back(tokens[0] + " = t" + std::to_string(temp_var_counter-1));

    return three_address_code;
}

int main() {
    std::string expression = "w = u * u - u * v + v * v";
    std::vector<std::string> three_address_code = generate_three_address_code(expression);

    for(const auto &code : three_address_code)
        std::cout << code << std::endl;

    return 0;
}
