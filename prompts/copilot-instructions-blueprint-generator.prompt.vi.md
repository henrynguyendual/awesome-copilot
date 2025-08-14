---
description: "Trình tạo bản thiết kế độc lập công nghệ để tạo các tệp copilot-instructions.md toàn diện, hướng dẫn GitHub Copilot tạo ra mã nhất quán với các tiêu chuẩn dự án, mẫu kiến trúc và phiên bản công nghệ chính xác bằng cách phân tích các mẫu mã nguồn hiện có và tránh các giả định."
---

# Trình tạo Bản thiết kế Hướng dẫn cho Copilot

## Các biến cấu hình

${PROJECT_TYPE="Tự động phát hiện|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Nhiều|Khác"} <!-- Công nghệ chính -->
${ARCHITECTURE_STYLE="Phân lớp|Vi dịch vụ|Nguyên khối|Hướng miền|Hướng sự kiện|Phi máy chủ|Hỗn hợp"} <!-- Phương pháp tiếp cận kiến trúc -->
${CODE_QUALITY_FOCUS="Khả năng bảo trì|Hiệu suất|Bảo mật|Khả năng truy cập|Khả năng kiểm thử|Tất cả"} <!-- Các ưu tiên về chất lượng -->
${DOCUMENTATION_LEVEL="Tối thiểu|Tiêu chuẩn|Toàn diện"} <!-- Yêu cầu về tài liệu -->
${TESTING_REQUIREMENTS="Đơn vị|Tích hợp|Đầu cuối|TDD|BDD|Tất cả"} <!-- Phương pháp tiếp cận kiểm thử -->
${VERSIONING="Semantic|CalVer|Tùy chỉnh"} <!-- Phương pháp tiếp cận phiên bản -->

## Lời nhắc được tạo ra

"Tạo một tệp copilot-instructions.md toàn diện sẽ hướng dẫn GitHub Copilot tạo ra mã nhất quán với các tiêu chuẩn, kiến trúc và phiên bản công nghệ của dự án chúng tôi. Các hướng dẫn phải dựa trên các mẫu mã thực tế trong mã nguồn của chúng tôi và tránh đưa ra bất kỳ giả định nào. Hãy làm theo phương pháp sau:

### 1. Cấu trúc Hướng dẫn Cốt lõi

```markdown
# Hướng dẫn GitHub Copilot

## Nguyên tắc Ưu tiên

Khi tạo mã cho kho lưu trữ này:

1.  **Tương thích phiên bản**: Luôn phát hiện và tôn trọng các phiên bản chính xác của ngôn ngữ, framework và thư viện được sử dụng trong dự án này.
2.  **Tệp ngữ cảnh**: Ưu tiên các mẫu và tiêu chuẩn được định nghĩa trong thư mục .github/copilot.
3.  **Mẫu mã nguồn**: Khi các tệp ngữ cảnh không cung cấp hướng dẫn cụ thể, hãy quét mã nguồn để tìm các mẫu đã được thiết lập.
4.  **Nhất quán kiến trúc**: Duy trì phong cách kiến trúc ${ARCHITECTURE_STYLE} và các ranh giới đã được thiết lập của chúng tôi.
5.  **Chất lượng mã**: Ưu tiên ${CODE_QUALITY_FOCUS == "All" ? "khả năng bảo trì, hiệu suất, bảo mật, khả năng truy cập và khả năng kiểm thử" : CODE_QUALITY_FOCUS} trong tất cả mã được tạo ra.

## Phát hiện Phiên bản Công nghệ

Trước khi tạo mã, hãy quét mã nguồn để xác định:

1.  **Phiên bản ngôn ngữ**: Phát hiện các phiên bản chính xác của các ngôn ngữ lập trình đang được sử dụng.

    - Kiểm tra các tệp dự án, tệp cấu hình và trình quản lý gói.
    - Tìm kiếm các chỉ báo phiên bản dành riêng cho ngôn ngữ (ví dụ: <LangVersion> trong các dự án .NET).
    - Không bao giờ sử dụng các tính năng ngôn ngữ vượt quá phiên bản đã phát hiện.

2.  **Phiên bản Framework**: Xác định các phiên bản chính xác của tất cả các framework.

    - Kiểm tra package.json, .csproj, pom.xml, requirements.txt, v.v.
    - Tôn trọng các ràng buộc phiên bản khi tạo mã.
    - Không bao giờ đề xuất các tính năng không có sẵn trong các phiên bản framework đã phát hiện.

3.  **Phiên bản thư viện**: Ghi lại các phiên bản chính xác của các thư viện và phần phụ thuộc chính.
    - Tạo mã tương thích với các phiên bản cụ thể này.
    - Không bao giờ sử dụng các API hoặc tính năng không có sẵn trong các phiên bản đã phát hiện.

## Tệp Ngữ cảnh

Ưu tiên các tệp sau trong thư mục .github/copilot (nếu chúng tồn tại):

- **architecture.md**: Nguyên tắc kiến trúc hệ thống.
- **tech-stack.md**: Phiên bản công nghệ và chi tiết framework.
- **coding-standards.md**: Tiêu chuẩn về phong cách và định dạng mã.
- **folder-structure.md**: Nguyên tắc tổ chức dự án.
- **exemplars.md**: Các mẫu mã tiêu biểu để làm theo.

## Hướng dẫn Quét Mã nguồn

Khi các tệp ngữ cảnh không cung cấp hướng dẫn cụ thể:

1.  Xác định các tệp tương tự với tệp đang được sửa đổi hoặc tạo mới.
2.  Phân tích các mẫu về:
    - Quy ước đặt tên.
    - Tổ chức mã.
    - Cách xử lý lỗi.
    - Phương pháp ghi log.
    - Phong cách tài liệu.
    - Mẫu kiểm thử.
3.  Tuân theo các mẫu nhất quán nhất được tìm thấy trong mã nguồn.
4.  Khi có các mẫu xung đột, ưu tiên các mẫu trong các tệp mới hơn hoặc các tệp có độ bao phủ kiểm thử cao hơn.
5.  Không bao giờ giới thiệu các mẫu không có trong mã nguồn hiện có.

## Tiêu chuẩn Chất lượng Mã

${CODE_QUALITY_FOCUS.includes("Maintainability") || CODE_QUALITY_FOCUS == "All" ? `### Khả năng bảo trì

- Viết mã tự giải thích với cách đặt tên rõ ràng.
- Tuân theo các quy ước đặt tên và tổ chức rõ ràng trong mã nguồn.
- Tuân theo các mẫu đã được thiết lập để đảm bảo tính nhất quán.
- Giữ cho các hàm tập trung vào một trách nhiệm duy nhất.
- Hạn chế độ phức tạp và độ dài của hàm để phù hợp với các mẫu hiện có.` : ""}

${CODE_QUALITY_FOCUS.includes("Performance") || CODE_QUALITY_FOCUS == "All" ? `### Hiệu suất

- Tuân theo các mẫu hiện có để quản lý bộ nhớ và tài nguyên.
- Phù hợp với các mẫu hiện có để xử lý các hoạt động tốn kém về mặt tính toán.
- Tuân theo các mẫu đã được thiết lập cho các hoạt động bất đồng bộ.
- Áp dụng bộ nhớ đệm một cách nhất quán với các mẫu hiện có.
- Tối ưu hóa theo các mẫu rõ ràng trong mã nguồn.` : ""}

${CODE_QUALITY_FOCUS.includes("Security") || CODE_QUALITY_FOCUS == "All" ? `### Bảo mật

- Tuân theo các mẫu hiện có để xác thực đầu vào.
- Áp dụng các kỹ thuật làm sạch dữ liệu tương tự được sử dụng trong mã nguồn.
- Sử dụng các truy vấn tham số hóa phù hợp với các mẫu hiện có.
- Tuân theo các mẫu xác thực và ủy quyền đã được thiết lập.
- Xử lý dữ liệu nhạy cảm theo các mẫu hiện có.` : ""}

${CODE_QUALITY_FOCUS.includes("Accessibility") || CODE_QUALITY_FOCUS == "All" ? `### Khả năng truy cập

- Tuân theo các mẫu khả năng truy cập hiện có trong mã nguồn.
- Phù hợp với việc sử dụng thuộc tính ARIA với các thành phần hiện có.
- Duy trì hỗ trợ điều hướng bằng bàn phím nhất quán với mã hiện có.
- Tuân theo các mẫu đã được thiết lập về màu sắc và độ tương phản.
- Áp dụng các mẫu văn bản thay thế nhất quán với mã nguồn.` : ""}

${CODE_QUALITY_FOCUS.includes("Testability") || CODE_QUALITY_FOCUS == "All" ? `### Khả năng kiểm thử

- Tuân theo các mẫu đã được thiết lập cho mã có thể kiểm thử.
- Phù hợp với các phương pháp tiêm phụ thuộc được sử dụng trong mã nguồn.
- Áp dụng các mẫu tương tự để quản lý các phần phụ thuộc.
- Tuân theo các mẫu mocking và test double đã được thiết lập.
- Phù hợp với phong cách kiểm thử được sử dụng trong các bài kiểm thử hiện có.` : ""}

## Yêu cầu về Tài liệu

${DOCUMENTATION_LEVEL == "Minimal" ?
`- Phù hợp với mức độ và phong cách của các bình luận được tìm thấy trong mã hiện có.

- Ghi tài liệu theo các mẫu được quan sát trong mã nguồn.
- Tuân theo các mẫu hiện có để ghi lại hành vi không rõ ràng.
- Sử dụng cùng một định dạng cho mô tả tham số như mã hiện có.` : ""}

${DOCUMENTATION_LEVEL == "Standard" ?
`- Tuân theo định dạng tài liệu chính xác được tìm thấy trong mã nguồn.

- Phù hợp với phong cách và sự đầy đủ của các bình luận XML/JSDoc hiện có.
- Ghi tài liệu về tham số, giá trị trả về và ngoại lệ theo cùng một phong cách.
- Tuân theo các mẫu hiện có cho các ví dụ sử dụng.
- Phù hợp với phong cách và nội dung tài liệu ở cấp độ lớp.` : ""}

${DOCUMENTATION_LEVEL == "Comprehensive" ?
`- Tuân theo các mẫu tài liệu chi tiết nhất được tìm thấy trong mã nguồn.

- Phù hợp với phong cách và sự đầy đủ của mã được ghi tài liệu tốt nhất.
- Ghi tài liệu chính xác như các tệp được ghi tài liệu kỹ lưỡng nhất.
- Tuân theo các mẫu hiện có để liên kết tài liệu.
- Phù hợp với mức độ chi tiết trong các giải thích về quyết định thiết kế.` : ""}

## Phương pháp Tiếp cận Kiểm thử

${TESTING_REQUIREMENTS.includes("Unit") || TESTING_REQUIREMENTS == "All" ?
`### Kiểm thử Đơn vị

- Phù hợp với cấu trúc và phong cách chính xác của các bài kiểm thử đơn vị hiện có.
- Tuân theo các quy ước đặt tên tương tự cho các lớp và phương thức kiểm thử.
- Sử dụng các mẫu khẳng định tương tự được tìm thấy trong các bài kiểm thử hiện có.
- Áp dụng phương pháp mocking tương tự được sử dụng trong mã nguồn.
- Tuân theo các mẫu hiện có để cách ly kiểm thử.` : ""}

${TESTING_REQUIREMENTS.includes("Integration") || TESTING_REQUIREMENTS == "All" ?
`### Kiểm thử Tích hợp

- Tuân theo các mẫu kiểm thử tích hợp tương tự được tìm thấy trong mã nguồn.
- Phù hợp với các mẫu hiện có để thiết lập và dọn dẹp dữ liệu kiểm thử.
- Sử dụng phương pháp tương tự để kiểm thử sự tương tác của các thành phần.
- Tuân theo các mẫu hiện có để xác minh hành vi của hệ thống.` : ""}

${TESTING_REQUIREMENTS.includes("E2E") || TESTING_REQUIREMENTS == "All" ?
`### Kiểm thử Đầu cuối

- Phù hợp với cấu trúc và các mẫu kiểm thử E2E hiện có.
- Tuân theo các mẫu đã được thiết lập để kiểm thử giao diện người dùng.
- Áp dụng phương pháp tương tự để xác minh các hành trình của người dùng.` : ""}

${TESTING_REQUIREMENTS.includes("TDD") || TESTING_REQUIREMENTS == "All" ?
`### Phát triển Hướng Kiểm thử (TDD)

- Tuân theo các mẫu TDD rõ ràng trong mã nguồn.
- Phù hợp với sự tiến triển của các trường hợp kiểm thử được thấy trong mã hiện có.
- Áp dụng các mẫu tái cấu trúc tương tự sau khi các bài kiểm thử vượt qua.` : ""}

${TESTING_REQUIREMENTS.includes("BDD") || TESTING_REQUIREMENTS == "All" ?
`### Phát triển Hướng Hành vi (BDD)

- Phù hợp với cấu trúc Given-When-Then hiện có trong các bài kiểm thử.
- Tuân theo các mẫu tương tự để mô tả hành vi.
- Áp dụng cùng một mức độ tập trung vào nghiệp vụ trong các trường hợp kiểm thử.` : ""}

## Hướng dẫn theo Công nghệ Cụ thể

${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Hướng dẫn .NET

- Phát hiện và tuân thủ nghiêm ngặt phiên bản .NET cụ thể đang được sử dụng.
- Chỉ sử dụng các tính năng ngôn ngữ C# tương thích với phiên bản đã phát hiện.
- Tuân theo các mẫu sử dụng LINQ chính xác như chúng xuất hiện trong mã nguồn.
- Phù hợp với các mẫu sử dụng async/await từ mã hiện có.
- Áp dụng phương pháp tiêm phụ thuộc tương tự được sử dụng trong mã nguồn.
- Sử dụng các loại collection và mẫu tương tự được tìm thấy trong mã hiện có.` : ""}

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Hướng dẫn Java

- Phát hiện và tuân thủ phiên bản Java cụ thể đang được sử dụng.
- Tuân theo các mẫu thiết kế chính xác tương tự được tìm thấy trong mã nguồn.
- Phù hợp với các mẫu xử lý ngoại lệ từ mã hiện có.
- Sử dụng các loại collection và phương pháp tương tự được tìm thấy trong mã nguồn.
- Áp dụng các mẫu tiêm phụ thuộc rõ ràng trong mã hiện có.` : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "TypeScript" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Hướng dẫn JavaScript/TypeScript

- Phát hiện và tuân thủ phiên bản ECMAScript/TypeScript cụ thể đang được sử dụng.
- Tuân theo các mẫu import/export module tương tự được tìm thấy trong mã nguồn.
- Phù hợp với các định nghĩa kiểu TypeScript với các mẫu hiện có.
- Sử dụng các mẫu bất đồng bộ (promises, async/await) tương tự như mã hiện có.
- Tuân theo các mẫu xử lý lỗi từ các tệp tương tự.` : ""}

${PROJECT_TYPE == "React" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Hướng dẫn React

- Phát hiện và tuân thủ phiên bản React cụ thể đang được sử dụng.
- Phù hợp với các mẫu cấu trúc thành phần từ các thành phần hiện có.
- Tuân theo các mẫu hooks và vòng đời tương tự được tìm thấy trong mã nguồn.
- Áp dụng phương pháp quản lý trạng thái tương tự được sử dụng trong các thành phần hiện có.
- Phù hợp với các mẫu định kiểu và xác thực prop từ mã hiện có.` : ""}

${PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Hướng dẫn Angular

- Phát hiện và tuân thủ phiên bản Angular cụ thể đang được sử dụng.
- Tuân theo các mẫu thành phần và module tương tự được tìm thấy trong mã nguồn.
- Phù hợp với việc sử dụng decorator chính xác như đã thấy trong mã hiện có.
- Áp dụng các mẫu RxJS tương tự được tìm thấy trong mã nguồn.
- Tuân theo các mẫu hiện có để giao tiếp giữa các thành phần.` : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Multiple" ? `### Hướng dẫn Python

- Phát hiện và tuân thủ phiên bản Python cụ thể đang được sử dụng.
- Tuân theo cách tổ chức import tương tự được tìm thấy trong các module hiện có.
- Phù hợp với các phương pháp gợi ý kiểu nếu được sử dụng trong mã nguồn.
- Áp dụng các mẫu xử lý lỗi tương tự được tìm thấy trong mã hiện có.
- Tuân theo các mẫu tổ chức module tương tự.` : ""}

## Hướng dẫn Quản lý Phiên bản

${VERSIONING == "Semantic" ?
`- Tuân theo các mẫu Đánh số phiên bản ngữ nghĩa (Semantic Versioning) như được áp dụng trong mã nguồn.

- Phù hợp với các mẫu hiện có để ghi lại các thay đổi đột phá.
- Tuân theo phương pháp tương tự cho các thông báo về việc ngừng hỗ trợ.` : ""}

${VERSIONING == "CalVer" ?
`- Tuân theo các mẫu Đánh số phiên bản theo lịch (Calendar Versioning) như được áp dụng trong mã nguồn.

- Phù hợp với các mẫu hiện có để ghi lại các thay đổi.
- Tuân theo phương pháp tương tự để làm nổi bật các thay đổi quan trọng.` : ""}

${VERSIONING == "Custom" ?
`- Phù hợp với mẫu đánh số phiên bản chính xác được quan sát trong mã nguồn.

- Tuân theo định dạng nhật ký thay đổi tương tự được sử dụng trong tài liệu hiện có.
- Áp dụng các quy ước gắn thẻ tương tự được sử dụng trong dự án.` : ""}

## Các Thực hành Tốt Nhất Chung

- Tuân theo các quy ước đặt tên chính xác như chúng xuất hiện trong mã hiện có.
- Phù hợp với các mẫu tổ chức mã từ các tệp tương tự.
- Áp dụng xử lý lỗi nhất quán với các mẫu hiện có.
- Tuân theo phương pháp kiểm thử tương tự như đã thấy trong mã nguồn.
- Phù hợp với các mẫu ghi log từ mã hiện có.
- Sử dụng phương pháp cấu hình tương tự như đã thấy trong mã nguồn.

## Hướng dẫn Cụ thể cho Dự án

- Quét kỹ mã nguồn trước khi tạo bất kỳ mã nào.
- Tôn trọng các ranh giới kiến trúc hiện có mà không có ngoại lệ.
- Phù hợp với phong cách và các mẫu của mã xung quanh.
- Khi không chắc chắn, hãy ưu tiên tính nhất quán với mã hiện có hơn là các thực hành tốt nhất bên ngoài.
```

### 2. Hướng dẫn Phân tích Mã nguồn

Để tạo tệp copilot-instructions.md, trước tiên hãy phân tích mã nguồn để:

1.  **Xác định Phiên bản Công nghệ Chính xác**:

    - ${PROJECT_TYPE == "Auto-detect" ? "Phát hiện tất cả các ngôn ngữ lập trình, framework và thư viện bằng cách quét phần mở rộng tệp và tệp cấu hình" : `Tập trung vào các công nghệ ${PROJECT_TYPE}`}
    - Trích xuất thông tin phiên bản chính xác từ các tệp dự án, package.json, .csproj, v.v.
    - Ghi lại các ràng buộc phiên bản và yêu cầu tương thích.

2.  **Hiểu Kiến trúc**:

    - Phân tích cấu trúc thư mục và tổ chức module.
    - Xác định các ranh giới lớp rõ ràng và mối quan hệ giữa các thành phần.
    - Ghi lại các mẫu giao tiếp giữa các thành phần.

3.  **Ghi lại các Mẫu Mã**:

    - Liệt kê các quy ước đặt tên cho các yếu tố mã khác nhau.
    - Ghi lại phong cách và sự đầy đủ của tài liệu.
    - Ghi lại các mẫu xử lý lỗi.
    - Sơ đồ hóa các phương pháp kiểm thử và độ bao phủ.

4.  **Ghi lại các Tiêu chuẩn Chất lượng**:
    - Xác định các kỹ thuật tối ưu hóa hiệu suất thực sự được sử dụng.
    - Ghi lại các thực hành bảo mật được triển khai trong mã.
    - Ghi lại các tính năng khả năng truy cập hiện có (nếu có).
    - Ghi lại các mẫu chất lượng mã rõ ràng trong mã nguồn.

### 3. Ghi chú Triển khai

Tệp copilot-instructions.md cuối cùng nên:

- Được đặt trong thư mục .github/copilot.
- Chỉ tham chiếu đến các mẫu và tiêu chuẩn tồn tại trong mã nguồn.
- Bao gồm các yêu cầu tương thích phiên bản rõ ràng.
- Tránh quy định bất kỳ thực hành nào không rõ ràng trong mã.
- Cung cấp các ví dụ cụ thể từ mã nguồn.
- Toàn diện nhưng đủ ngắn gọn để Copilot sử dụng hiệu quả.

Quan trọng: Chỉ bao gồm hướng dẫn dựa trên các mẫu thực sự được quan sát trong mã nguồn. Hướng dẫn Copilot một cách rõ ràng để ưu tiên tính nhất quán với mã hiện có hơn là các thực hành tốt nhất bên ngoài hoặc các tính năng ngôn ngữ mới hơn.
"

## Đầu ra Dự kiến

Một tệp copilot-instructions.md toàn diện sẽ hướng dẫn GitHub Copilot tạo ra mã hoàn toàn tương thích với các phiên bản công nghệ hiện có của bạn và tuân theo các mẫu và kiến trúc đã được thiết lập của
