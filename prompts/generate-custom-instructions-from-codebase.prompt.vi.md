---
description: "Trình tạo hướng dẫn di chuyển và tiến hóa mã nguồn cho GitHub Copilot. Phân tích sự khác biệt giữa hai phiên bản dự án (nhánh, commit, hoặc bản phát hành) để tạo ra các hướng dẫn chính xác cho phép Copilot duy trì tính nhất quán trong quá trình di chuyển công nghệ, tái cấu trúc lớn, hoặc nâng cấp phiên bản framework."
---

# Trình tạo Hướng dẫn Di chuyển và Tiến hóa Mã nguồn

## Biến Cấu hình

```
${MIGRATION_TYPE="Phiên bản Framework|Tái cấu trúc Kiến trúc|Di chuyển Công nghệ|Cập nhật Phụ thuộc|Thay đổi Mẫu"}
<!-- Loại di chuyển hoặc tiến hóa -->

${SOURCE_REFERENCE="nhánh|commit|tag"}
<!-- Điểm tham chiếu nguồn (trạng thái trước) -->

${TARGET_REFERENCE="nhánh|commit|tag"}
<!-- Điểm tham chiếu đích (trạng thái sau) -->

${ANALYSIS_SCOPE="Toàn bộ dự án|Thư mục cụ thể|Chỉ các tệp đã sửa đổi"}
<!-- Phạm vi phân tích -->

${CHANGE_FOCUS="Thay đổi Gây lỗi (Breaking Changes)|Quy ước Mới|Mẫu Lỗi thời|Thay đổi API|Cấu hình"}
<!-- Khía cạnh chính của các thay đổi -->

${AUTOMATION_LEVEL="Thận trọng|Cân bằng|Tích cực"}
<!-- Mức độ tự động hóa cho các đề xuất của Copilot -->

${GENERATE_EXAMPLES="true|false"}
<!-- Bao gồm các ví dụ chuyển đổi -->

${VALIDATION_REQUIRED="true|false"}
<!-- Yêu cầu xác thực trước khi áp dụng -->
```

## Prompt được Tạo ra

```
"Phân tích sự tiến hóa của mã nguồn giữa hai trạng thái dự án để tạo ra các hướng dẫn di chuyển chính xác cho GitHub Copilot. Những hướng dẫn này sẽ chỉ dẫn Copilot tự động áp dụng các mẫu chuyển đổi tương tự trong các lần sửa đổi trong tương lai. Hãy tuân theo phương pháp này:

### Giai đoạn 1: Phân tích So sánh Trạng thái

#### Phát hiện Thay đổi Cấu trúc
- So sánh cấu trúc thư mục giữa ${SOURCE_REFERENCE} và ${TARGET_REFERENCE}
- Xác định các tệp đã di chuyển, đổi tên hoặc xóa
- Phân tích các thay đổi trong tệp cấu hình
- Ghi lại các phụ thuộc mới và các phụ thuộc đã bị loại bỏ

#### Phân tích Chuyển đổi Mã nguồn
${MIGRATION_TYPE == "Phiên bản Framework" ?
  "- Xác định các thay đổi API giữa các phiên bản framework
   - Phân tích các tính năng mới đang được sử dụng
   - Ghi lại các phương thức/thuộc tính lỗi thời
   - Ghi chú các thay đổi về cú pháp hoặc quy ước" : ""}

${MIGRATION_TYPE == "Tái cấu trúc Kiến trúc" ?
  "- Phân tích các thay đổi về mẫu kiến trúc
   - Xác định các lớp trừu tượng mới được giới thiệu
   - Ghi lại việc tổ chức lại trách nhiệm
   - Ghi chú các thay đổi trong luồng dữ liệu" : ""}

${MIGRATION_TYPE == "Di chuyển Công nghệ" ?
  "- Phân tích việc thay thế một công nghệ bằng một công nghệ khác
   - Xác định các chức năng tương đương
   - Ghi lại các thay đổi về API và cú pháp
   - Ghi chú các phụ thuộc và cấu hình mới" : ""}

#### Trích xuất Mẫu Chuyển đổi
- Xác định các phép chuyển đổi lặp đi lặp lại đã được áp dụng
- Phân tích các quy tắc chuyển đổi từ định dạng cũ sang định dạng mới
- Ghi lại các trường hợp ngoại lệ và đặc biệt
- Tạo ma trận tương ứng trước/sau

### Giai đoạn 2: Tạo Hướng dẫn Di chuyển

Tạo một tệp `.github/copilot-migration-instructions.md` với cấu trúc này:

\`\`\`markdown
# Hướng dẫn Di chuyển cho GitHub Copilot

## Bối cảnh Di chuyển
- **Loại**: ${MIGRATION_TYPE}
- **Từ**: ${SOURCE_REFERENCE}
- **Đến**: ${TARGET_REFERENCE}
- **Ngày**: [NGÀY_TẠO]
- **Phạm vi**: ${ANALYSIS_SCOPE}

## Quy tắc Chuyển đổi Tự động

### 1. Các Chuyển đổi Bắt buộc
${AUTOMATION_LEVEL != "Thận trọng" ?
  "[QUY_TẮC_CHUYỂN_ĐỔI_TỰ_ĐỘNG]
   - **Mẫu cũ**: [MÃ_NGUỒN_CŨ]
   - **Mẫu mới**: [MÃ_NGUỒN_MỚI]
   - **Điều kiện kích hoạt**: Khi nào phát hiện mẫu này
   - **Hành động**: Phép chuyển đổi sẽ được áp dụng tự động" : ""}

### 2. Các Chuyển đổi cần Xác thực
${VALIDATION_REQUIRED == "true" ?
  "[CÁC_CHUYỂN_ĐỔI_CẦN_XÁC_THỰC]
   - **Mẫu được phát hiện**: [MÔ_TẢ]
   - **Chuyển đổi được đề xuất**: [PHƯƠNG_PHÁP_MỚI]
   - **Yêu cầu Xác thực**: [TIÊU_CHÍ_XÁC_THỰC]
   - **Các lựa chọn thay thế**: [CÁC_LỰA_CHỌN_KHÁC]" : ""}

### 3. Bảng tương ứng API
${CHANGE_FOCUS == "Thay đổi API" || MIGRATION_TYPE == "Phiên bản Framework" ?
  "[BẢNG_TƯƠNG_ỨNG_API]
   | API cũ    | API mới   | Ghi chú   | Ví dụ          |
   | --------- | --------- | --------- | -------------- |
   | [API_CŨ]  | [API_MỚI] | [THAY_ĐỔI]| [VÍ_DỤ_MÃ]     | " : ""} |

### 4. Các Mẫu mới cần Áp dụng
[CÁC_MẪU_MỚI_NỔI_BẬT_ĐƯỢC_PHÁT_HIỆN]
- **Mẫu**: [TÊN_MẪU]
- **Sử dụng**: [KHI_NÀO_SỬ_DỤNG]
- **Triển khai**: [CÁCH_TRIỂN_KHAI]
- **Lợi ích**: [ƯU_ĐIỂM]

### 5. Các Mẫu lỗi thời cần Tránh
[CÁC_MẪU_LỖI_THỜI_ĐƯỢC_PHÁT_HIỆN]
- **Mẫu lỗi thời**: [MẪU_CŨ]
- **Tại sao cần tránh**: [LÝ_DO]
- **Giải pháp thay thế**: [MẪU_MỚI]
- **Di chuyển**: [CÁC_BƯỚC_CHUYỂN_ĐỔI]

## Hướng dẫn Cụ thể theo Loại Tệp

${GENERATE_EXAMPLES == "true" ?
  "### Tệp Cấu hình
   [VÍ_DỤ_CHUYỂN_ĐỔI_CẤU_HÌNH]

   ### Tệp Nguồn Chính
   [VÍ_DỤ_CHUYỂN_ĐỔI_NGUỒN]

   ### Tệp Kiểm thử
   [VÍ_DỤ_CHUYỂN_ĐỔI_KIỂM_THỬ]" : ""}

## Xác thực và Bảo mật

### Các Điểm Kiểm soát Tự động
- Các kiểm tra cần thực hiện sau mỗi lần chuyển đổi
- Các bài kiểm thử cần chạy để xác thực thay đổi
- Các chỉ số hiệu suất cần theo dõi
- Các kiểm tra tương thích cần thực hiện

### Báo cáo lên Cấp trên (Manual Escalation)
Các tình huống yêu cầu sự can thiệp của con người:
- [DANH_SÁCH_CÁC_TRƯỜNG_HỢP_PHỨC_TẠP]
- [CÁC_QUYẾT_ĐỊNH_VỀ_KIẾN_TRÚC]
- [CÁC_TÁC_ĐỘNG_KINH_DOANH]

## Giám sát Di chuyển

### Các Chỉ số Theo dõi
- Tỷ lệ phần trăm mã được di chuyển tự động
- Số lượng xác thực thủ công được yêu cầu
- Tỷ lệ lỗi của các phép chuyển đổi tự động
- Thời gian di chuyển trung bình cho mỗi tệp

### Báo cáo Lỗi
Cách báo cáo các phép chuyển đổi không chính xác cho Copilot:
- Các mẫu phản hồi để cải thiện quy tắc
- Các trường hợp ngoại lệ cần ghi lại
- Các điều chỉnh cần thực hiện đối với hướng dẫn

\`\`\`

### Giai đoạn 3: Tạo Ví dụ theo Ngữ cảnh

${GENERATE_EXAMPLES == "true" ?
  "#### Ví dụ Chuyển đổi
   Đối với mỗi mẫu được xác định, hãy tạo:

   \`\`\`
   // TRƯỚC (${SOURCE_REFERENCE})
   [VÍ_DỤ_MÃ_CŨ]

   // SAU (${TARGET_REFERENCE})
   [VÍ_DỤ_MÃ_MỚI]

   // HƯỚNG DẪN CHO COPILOT
   Khi bạn thấy mẫu này [ĐIỀU_KIỆN_KÍCH_HOẠT], hãy chuyển đổi nó thành [MẪU_MỚI] theo các bước sau: [CÁC_BƯỚC]
   \`\`\`" : ""}

### Giai đoạn 4: Xác thực và Tối ưu hóa

#### Kiểm thử Hướng dẫn
- Áp dụng hướng dẫn trên mã kiểm thử
- Xác minh tính nhất quán của phép chuyển đổi
- Điều chỉnh quy tắc dựa trên kết quả
- Ghi lại các trường hợp ngoại lệ và các trường hợp biên

#### Tối ưu hóa Lặp lại
${AUTOMATION_LEVEL == "Tích cực" ?
  "- Tinh chỉnh các quy tắc để tối đa hóa tự động hóa
   - Giảm các trường hợp dương tính giả trong phát hiện
   - Cải thiện độ chính xác của phép chuyển đổi
   - Ghi lại các bài học kinh nghiệm" : ""}

### Kết quả Cuối cùng

Các hướng dẫn di chuyển cho phép GitHub Copilot:
1. **Tự động áp dụng** các phép chuyển đổi tương tự trong các lần sửa đổi trong tương lai
2. **Duy trì tính nhất quán** với các quy ước mới được áp dụng
3. **Tránh các mẫu lỗi thời** bằng cách tự động đề xuất các giải pháp thay thế
4. **Tăng tốc các lần di chuyển trong tương lai** bằng cách tận dụng kinh nghiệm đã có
5. **Giảm thiểu lỗi** bằng cách tự động hóa các phép chuyển đổi lặp đi lặp lại

Những hướng dẫn này biến Copilot thành một trợ lý di chuyển thông minh, có khả năng tái tạo các quyết định tiến hóa công nghệ của bạn một cách nhất quán và đáng tin cậy.
"
```

## Các Trường hợp Sử dụng Tiêu biểu

### Di chuyển Phiên bản Framework

Hoàn hảo để ghi lại quá trình chuyển đổi từ Angular 14 sang Angular 17, React Class Components sang Hooks, hoặc .NET Framework sang .NET Core. Tự động xác định các thay đổi gây lỗi và tạo ra các quy tắc chuyển đổi tương ứng.

### Tiến hóa Ngăn xếp Công nghệ

Cần thiết khi thay thế hoàn toàn một công nghệ: jQuery sang React, REST sang GraphQL, SQL sang NoSQL. Tạo ra một hướng dẫn di chuyển toàn diện với các ánh xạ mẫu.

### Tái cấu trúc Kiến trúc

Lý tưởng cho các lần tái cấu trúc lớn như Monolith sang Microservices, MVC sang Clean Architecture, hoặc kiến trúc dựa trên Component sang Composable. Lưu giữ kiến thức kiến trúc cho các lần chuyển đổi tương tự trong tương lai.

### Hiện đại hóa Mẫu Thiết kế

Hữu ích cho việc áp dụng các mẫu mới: Repository Pattern, Dependency Injection, Observer sang Reactive Programming. Ghi lại lý do và sự khác biệt trong cách triển khai.

## Các Lợi ích Độc đáo

### 🧠 **Tăng cường Trí tuệ Nhân tạo**

Không giống như các tài liệu di chuyển truyền thống, những hướng dẫn này "huấn luyện" GitHub Copilot để tự động tái tạo các quyết định tiến hóa công nghệ của bạn trong các lần sửa đổi mã trong tương lai.

### 🔄 **Vốn hóa Tri thức**

Biến kinh nghiệm dự án cụ thể thành các quy tắc có thể tái sử dụng, tránh mất mát chuyên môn về di chuyển và tăng tốc các lần chuyển đổi tương tự trong tương lai.

### 🎯 **Độ chính xác Nhận biết Ngữ cảnh**

Thay vì đưa ra lời khuyên chung chung, nó tạo ra các hướng dẫn phù hợp với cơ sở mã cụ thể của bạn, với các ví dụ thực tế trước/sau từ quá trình tiến hóa dự án của bạn.

### ⚡ **Tính nhất quán Tự động**

Đảm bảo rằng các đoạn mã mới được thêm vào sẽ tự động tuân theo các quy ước mới, ngăn chặn sự thụt lùi về kiến trúc và duy trì sự mạch lạc trong quá trình tiến hóa mã nguồn.
