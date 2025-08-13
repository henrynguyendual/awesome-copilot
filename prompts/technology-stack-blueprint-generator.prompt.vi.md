---
description: 'Trình tạo bản thiết kế ngăn xếp công nghệ toàn diện, phân tích mã nguồn để tạo tài liệu kiến trúc chi tiết. Tự động phát hiện các ngăn xếp công nghệ, ngôn ngữ lập trình và mẫu triển khai trên nhiều nền tảng (.NET, Java, JavaScript, React, Python). Sinh bản thiết kế có thể cấu hình với thông tin phiên bản, chi tiết giấy phép, mẫu sử dụng, quy ước viết mã và sơ đồ trực quan. Cung cấp các mẫu sẵn sàng triển khai và duy trì tính nhất quán kiến trúc cho phát triển có định hướng.'
---

# Trình Tạo Bản Thiết Kế Ngăn Xếp Công Nghệ Toàn Diện

## Biến Cấu Hình
${PROJECT_TYPE="Tự động phát hiện|.NET|Java|JavaScript|React.js|React Native|Angular|Python|Khác"} <!-- Công nghệ chính -->
${DEPTH_LEVEL="Cơ bản|Tiêu chuẩn|Toàn diện|Sẵn sàng triển khai"} <!-- Mức độ phân tích -->
${INCLUDE_VERSIONS=true|false} <!-- Bao gồm thông tin phiên bản -->
${INCLUDE_LICENSES=true|false} <!-- Bao gồm thông tin giấy phép -->
${INCLUDE_DIAGRAMS=true|false} <!-- Tạo sơ đồ kiến trúc -->
${INCLUDE_USAGE_PATTERNS=true|false} <!-- Bao gồm mẫu sử dụng mã -->
${INCLUDE_CONVENTIONS=true|false} <!-- Tài liệu quy ước mã -->
${OUTPUT_FORMAT="Markdown|JSON|YAML|HTML"} <!-- Chọn định dạng đầu ra -->
${CATEGORIZATION="Loại công nghệ|Tầng|Mục đích"} <!-- Phương pháp phân loại -->

## Prompt Sinh Ra

"Phân tích mã nguồn và tạo bản thiết kế ngăn xếp công nghệ mức ${DEPTH_LEVEL} để tài liệu hóa chi tiết công nghệ và mẫu triển khai, hỗ trợ tạo mã nhất quán. Thực hiện như sau:

### 1. Giai đoạn Xác Định Công Nghệ
- ${PROJECT_TYPE == "Tự động phát hiện" ? "Quét mã nguồn, tệp cấu hình và phụ thuộc để xác định các ngăn xếp công nghệ đang sử dụng" : "Tập trung vào công nghệ ${PROJECT_TYPE}"}
- Xác định tất cả ngôn ngữ lập trình qua phần mở rộng và nội dung tệp
- Phân tích tệp cấu hình (package.json, .csproj, pom.xml, v.v.) để lấy danh sách phụ thuộc
- Xem xét script build và pipeline để lấy thông tin công cụ
- ${INCLUDE_VERSIONS ? "Trích xuất thông tin phiên bản từ tệp package và cấu hình" : "Bỏ qua chi tiết phiên bản"}
- ${INCLUDE_LICENSES ? "Ghi lại thông tin giấy phép của các phụ thuộc" : ""}

### 2. Phân Tích Công Nghệ Cốt Lõi
... (dịch tương tự phần phân tích .NET, Java, JavaScript, React, Python như bản gốc)