#pragma once
#include <cstdint>
#include <sstream>
#include <string>
namespace retrocontrol {
struct Frame {
    std::uint32_t sequence;
    std::uint64_t timestamp_ms;
    unsigned channel;
    unsigned value;
    std::string csv() const {
        std::ostringstream s;
        s << "1," << sequence << ',' << timestamp_ms << ",synthetic,"
          << channel << ',' << value << ",mV,demo,DEMO";
        return s.str();
    }
    std::string json() const {
        std::ostringstream s;
        s << "{\"schema_version\":1,\"sequence\":" << sequence
          << ",\"timestamp_ms\":" << timestamp_ms
          << ",\"source\":\"synthetic\",\"channel\":" << channel
          << ",\"value\":" << value
          << ",\"unit\":\"mV\",\"quality\":\"demo\",\"state\":\"DEMO\"}";
        return s.str();
    }
};
inline Frame synthetic(std::uint32_t sequence) {
    return {sequence, static_cast<std::uint64_t>(sequence) * 100,
            sequence % 8, 1000 + (sequence % 10) * 25};
}
} // namespace retrocontrol
