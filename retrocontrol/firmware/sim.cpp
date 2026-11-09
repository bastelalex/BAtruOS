#include "diagnostics.hpp"
#include <iostream>
int main() {
    std::cout << "schema_version,sequence,timestamp_ms,source,channel,value,unit,quality,state\n";
    for (unsigned i = 0; i < 16; ++i) {
        const auto frame = retrocontrol::synthetic(i);
        std::cout << frame.csv() << '\n' << frame.json() << '\n';
    }
}
