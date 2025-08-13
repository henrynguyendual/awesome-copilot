# Trình tạo hướng dẫn di trú và tiến hóa mã nguồn

## Biến cấu hình

```
${MIGRATION_TYPE="Phiên bản Framework|Tái cấu trúc kiến trúc|Di trú công nghệ|Cập nhật dependencies|Thay đổi pattern"}
<!-- Loại di trú hoặc tiến hóa -->

${SOURCE_REFERENCE="branch|commit|tag"}
<!-- Điểm tham chiếu nguồn (trước) -->

${TARGET_REFERENCE="branch|commit|tag"}  
<!-- Điểm tham chiếu đích (sau) -->

${ANALYSIS_SCOPE="Toàn bộ dự án|Thư mục cụ thể|Chỉ file thay đổi"}
<!-- Phạm vi phân tích -->

${CHANGE_FOCUS="Thay đổi phá vỡ|Quy ước mới|Pattern lỗi thời|Thay đổi API|Cấu hình"}
<!-- Khía cạnh chính của thay đổi -->

${AUTOMATION_LEVEL="Bảo thủ|Cân bằng|Tự động mạnh"}
<!-- Mức độ tự động hóa cho Copilot -->

${GENERATE_EXAMPLES="true|false"}
<!-- Bao gồm ví dụ chuyển đổi -->

${VALIDATION_REQUIRED="true|false"}
<!-- Yêu cầu xác thực trước khi áp dụng -->
```

## Prompt được tạo

"Phân tích tiến hóa mã giữa hai trạng thái dự án để tạo hướng dẫn di trú chính xác cho GitHub Copilot. Hướng dẫn này sẽ giúp Copilot tự động áp dụng cùng mẫu chuyển đổi trong các chỉnh sửa tương lai.

### Giai đoạn 1: Phân tích so sánh trạng thái

#### Phát hiện thay đổi cấu trúc
- So sánh cấu trúc thư mục giữa ${SOURCE_REFERENCE} và ${TARGET_REFERENCE}
- Xác định file bị di chuyển, đổi tên hoặc xóa
- Phân tích thay đổi file cấu hình
- Ghi lại dependencies mới và đã gỡ bỏ

#### Phân tích chuyển đổi mã
${MIGRATION_TYPE == "Phiên bản Framework" ? 
  "- Xác định thay đổi API giữa các phiên bản framework
   - Phân tích tính năng mới được sử dụng
   - Ghi nhận phương thức/thuộc tính lỗi thời
   - Ghi chú thay đổi cú pháp hoặc quy ước" : ""}

${MIGRATION_TYPE == "Tái cấu trúc kiến trúc" ? 
  "- Phân tích thay đổi mẫu kiến trúc
   - Xác định abstraction mới
   - Ghi lại tổ chức lại trách nhiệm
   - Ghi chú thay đổi luồng dữ liệu" : ""}

${MIGRATION_TYPE == "Di trú công nghệ" ? 
  "- Phân tích thay thế công nghệ
   - Xác định chức năng tương đương
   - Ghi nhận thay đổi API và cú pháp
   - Ghi chú dependencies và cấu hình mới" : ""}

#### Trích xuất mẫu chuyển đổi
- Xác định chuyển đổi lặp lại
- Phân tích quy tắc chuyển đổi từ cũ sang mới
- Ghi nhận ngoại lệ
- Tạo bảng tương ứng trước/sau

### Giai đoạn 2: Tạo hướng dẫn di trú

Tạo file `.github/copilot-migration-instructions.md` với cấu trúc:

\`\`\`markdown
# Hướng dẫn di trú GitHub Copilot

## Ngữ cảnh di trú
- **Loại**: ${MIGRATION_TYPE}
- **Từ**: ${SOURCE_REFERENCE} 
- **Đến**: ${TARGET_REFERENCE}
- **Ngày**: [GENERATION_DATE]
- **Phạm vi**: ${ANALYSIS_SCOPE}

## Quy tắc chuyển đổi tự động

### 1. Chuyển đổi bắt buộc
${AUTOMATION_LEVEL != "Bảo thủ" ? 
  "[QUY_TẮC_TỰ_ĐỘNG]
   - **Mẫu cũ**: [MÃ_CŨ]
   - **Mẫu mới**: [MÃ_MỚI]
   - **Kích hoạt**: Khi phát hiện mẫu này
   - **Hành động**: Chuyển đổi áp dụng tự động" : ""}

### 2. Chuyển đổi cần xác thực
${VALIDATION_REQUIRED == "true" ? 
  "[CHUYỂN_ĐỔI_CẦN_XÁC_THỰC]
   - **Mẫu phát hiện**: [MÔ_TẢ]
   - **Chuyển đổi gợi ý**: [CÁCH_MỚI]
   - **Tiêu chí xác thực**: [TIÊU_CHÍ]
   - **Phương án thay thế**: [TÙY_CHỌN]" : ""}

### 3. Tương ứng API
${CHANGE_FOCUS == "Thay đổi API" || MIGRATION_TYPE == "Phiên bản Framework" ? 
  "[BẢNG_TƯƠNG_ỨNG_API]
   | API Cũ   | API Mới   | Ghi chú     | Ví dụ        |
   | -------- | -------- | ----------- | ------------ |
   | [API_CŨ] | [API_MỚI] | [THAY_ĐỔI]  | [VÍ_DỤ_CODE] | " : ""} |

### 4. Mẫu mới cần áp dụng
[MẪU_MỚI]
- **Tên mẫu**: [TÊN]
- **Khi dùng**: [ĐIỀU_KIỆN]
- **Cách triển khai**: [HƯỚNG_DẪN]
- **Lợi ích**: [ƯU_ĐIỂM]

### 5. Mẫu lỗi thời cần tránh
[MẪU_LỖI_THỜI]
- **Mẫu lỗi thời**: [MẪU_CŨ]
- **Lý do tránh**: [LÝ_DO]
- **Thay thế**: [MẪU_MỚI]
- **Di trú**: [BƯỚC_CHUYỂN]

## Hướng dẫn cho loại file cụ thể

${GENERATE_EXAMPLES == "true" ? 
  "### File cấu hình
   [VÍ_DỤ_CHUYỂN_ĐỔI_CẤU_HÌNH]
   
   ### File mã nguồn chính
   [VÍ_DỤ_CHUYỂN_ĐỔI_MÃ_NGUỒN]
   
   ### File kiểm thử
   [VÍ_DỤ_CHUYỂN_ĐỔI_TEST]" : ""}

## Xác thực và bảo mật

### Điểm kiểm soát tự động
- Xác minh sau mỗi chuyển đổi
- Chạy test để xác thực
- Theo dõi hiệu năng
- Kiểm tra tương thích

### Nâng cấp thủ công
Tình huống cần can thiệp người:
- [DANH_SÁCH_CASE_PHỨC_TẠP]
- [QUYẾT_ĐỊNH_KIẾN_TRÚC]
- [ẢNH_HƯỞNG_KINH_DOANH]

## Giám sát di trú

### Chỉ số theo dõi
- % mã tự động di trú
- Số lần cần xác thực thủ công
- Tỷ lệ lỗi chuyển đổi
- Thời gian di trú TB mỗi file

### Báo cáo lỗi
Cách báo lỗi chuyển đổi sai cho Copilot:
- Mẫu phản hồi để cải thiện quy tắc
- Ngoại lệ cần ghi chú
- Điều chỉnh hướng dẫn
\`\`\`

### Giai đoạn 3: Tạo ví dụ theo ngữ cảnh

${GENERATE_EXAMPLES == "true" ? 
  "#### Ví dụ chuyển đổi
   Mỗi mẫu phát hiện tạo:
   
   \`\`\`
   // TRƯỚC (${SOURCE_REFERENCE})
   [MÃ_CŨ]
   
   // SAU (${TARGET_REFERENCE}) 
   [MÃ_MỚI]
   
   // HƯỚNG DẪN CHO COPILOT
   Khi thấy mẫu [KÍCH_HOẠT], chuyển sang [MẪU_MỚI] theo các bước: [BƯỚC]
   \`\`\`" : ""}

### Giai đoạn 4: Xác thực và tối ưu

#### Kiểm thử hướng dẫn
- Áp dụng trên mã test
- Xác minh tính nhất quán
- Điều chỉnh quy tắc
- Ghi chú ngoại lệ

#### Tối ưu lặp
${AUTOMATION_LEVEL == "Tự động mạnh" ? 
  "- Tinh chỉnh quy tắc để tối đa hóa tự động
   - Giảm false positive
   - Cải thiện độ chính xác
   - Ghi lại bài học" : ""}

### Kết quả cuối cùng

Hướng dẫn di trú giúp Copilot:
1. **Tự động áp dụng** chuyển đổi trong chỉnh sửa sau
2. **Duy trì nhất quán** với quy ước mới
3. **Tránh mẫu lỗi thời** bằng cách gợi ý thay thế
4. **Tăng tốc di trú** nhờ kinh nghiệm đã tích lũy
5. **Giảm lỗi** bằng tự động hóa chuyển đổi lặp
