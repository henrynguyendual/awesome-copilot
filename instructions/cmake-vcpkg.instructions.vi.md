---
description: "Cấu hình dự án C++ và quản lý gói"
applyTo: "**/*.cmake, **/CMakeLists.txt, **/*.cpp, **/*.h, **/*.hpp"
---

Dự án này sử dụng vcpkg ở chế độ manifest. Vui lòng ghi nhớ điều này khi đưa ra các đề xuất về vcpkg. Không đưa ra các đề xuất như `vcpkg install library`, vì chúng sẽ không hoạt động như mong đợi.
Ưu tiên đặt các biến cache và các loại khác thông qua `CMakePresets.json` nếu có thể.
Cung cấp thông tin về bất kỳ Chính sách CMake nào có thể ảnh hưởng đến các biến CMake được đề xuất hoặc đề cập.
Dự án này cần phải đa nền tảng và đa trình biên dịch cho MSVC, Clang và GCC.
Khi cung cấp các mẫu OpenCV sử dụng hệ thống tệp để đọc tệp, vui lòng luôn sử dụng đường dẫn tệp tuyệt đối thay vì tên tệp hoặc đường dẫn tệp tương đối. Ví dụ: sử dụng `video.open("C:/project/file.mp4")`, không
