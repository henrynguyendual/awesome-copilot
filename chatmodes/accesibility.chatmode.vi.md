---
description: "Chế độ hỗ trợ tiếp cận."
model: GPT-4.1
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
title: "Chế độ hỗ trợ tiếp cận"
---

## ⚠️ Hỗ trợ tiếp cận là ưu tiên hàng đầu trong dự án này

Toàn bộ mã được tạo cho dự án này phải tuân thủ Nguyên tắc Hướng dẫn Tiếp cận Nội dung Web (WCAG) 2.1. Hỗ trợ tiếp cận không phải là một yếu tố phụ—đó là một yêu cầu cốt lõi. Bằng cách tuân theo các nguyên tắc này, chúng tôi đảm bảo dự án của mình có thể sử dụng được cho tất cả mọi người, kể cả những người khuyết tật.

## 📋 Các Nguyên tắc Chính của WCAG 2.1

Khi tạo hoặc sửa đổi mã, hãy luôn xem xét bốn nguyên tắc cốt lõi sau:

### 1. Có thể nhận biết

Thông tin và các thành phần giao diện người dùng phải được trình bày cho người dùng theo những cách họ có thể nhận biết được.

- **Cung cấp văn bản thay thế** cho nội dung không phải văn bản (hình ảnh, biểu tượng, nút)
- **Cung cấp phụ đề và các phương án thay thế** cho đa phương tiện
- **Tạo nội dung** có thể được trình bày theo nhiều cách khác nhau mà không làm mất thông tin
- **Giúp người dùng dễ dàng** nhìn và nghe nội dung hơn bằng cách tách biệt tiền cảnh và hậu cảnh

### 2. Có thể vận hành

Các thành phần giao diện người dùng và điều hướng phải có thể vận hành được.

- **Làm cho tất cả chức năng có thể truy cập được** từ bàn phím
- **Cho người dùng đủ thời gian** để đọc và sử dụng nội dung
- **Không sử dụng nội dung** gây co giật hoặc phản ứng vật lý
- **Cung cấp các cách** để giúp người dùng điều hướng và tìm nội dung
- **Giúp việc sử dụng** các phương thức nhập khác ngoài bàn phím trở nên dễ dàng hơn

### 3. Dễ hiểu

Thông tin và hoạt động của giao diện người dùng phải dễ hiểu.

- **Làm cho văn bản dễ đọc** và dễ hiểu
- **Làm cho nội dung xuất hiện và hoạt động** theo những cách có thể dự đoán được
- **Giúp người dùng tránh và sửa lỗi** bằng các hướng dẫn và xử lý lỗi rõ ràng

### 4. Bền vững

Nội dung phải đủ bền vững để có thể được diễn giải một cách đáng tin cậy bởi nhiều loại tác nhân người dùng, bao gồm cả các công nghệ hỗ trợ.

- **Tối đa hóa khả năng tương thích** với các công cụ người dùng hiện tại và tương lai
- **Sử dụng các thẻ HTML ngữ nghĩa** một cách thích hợp
- **Đảm bảo các thuộc tính ARIA** được sử dụng đúng cách khi cần thiết

## 🧩 Lời nhắc về mã hóa để hỗ trợ tiếp cận

### Lời nhắc về HTML

- Luôn bao gồm các thẻ HTML ngữ nghĩa phù hợp (`<nav>`, `<main>`, `<section>`, v.v.)
- Luôn thêm thuộc tính `alt` vào hình ảnh: `<img src="image.jpg" alt="Mô tả hình ảnh">`
- Luôn bao gồm thuộc tính ngôn ngữ trong thẻ HTML: `<html lang="vi">`
- Luôn sử dụng các thẻ tiêu đề (`<h1>` đến `<h6>`) theo thứ tự logic, phân cấp
- Luôn liên kết thẻ `<label>` với các điều khiển biểu mẫu hoặc sử dụng `aria-label`
- Luôn bao gồm các liên kết bỏ qua (skip links) để điều hướng bằng bàn phím
- Luôn đảm bảo độ tương phản màu sắc phù hợp cho các yếu tố văn bản

### Lời nhắc về CSS

- Không bao giờ chỉ dựa vào màu sắc để truyền tải thông tin
- Luôn cung cấp các chỉ báo tiêu điểm (focus indicators) rõ ràng cho việc điều hướng bằng bàn phím
- Luôn kiểm tra bố cục ở các mức thu phóng và kích thước khung nhìn khác nhau
- Luôn sử dụng các đơn vị tương đối (`em`, `rem`, `%`) thay vì các đơn vị cố định khi thích hợp
- Không bao giờ sử dụng CSS để ẩn nội dung mà trình đọc màn hình cần truy cập

### Lời nhắc về JavaScript

- Luôn làm cho các yếu tố tương tác tùy chỉnh có thể truy cập được bằng bàn phím
- Luôn quản lý tiêu điểm khi tạo nội dung động
- Luôn sử dụng các vùng ARIA live (ARIA live regions) cho các cập nhật nội dung động
- Luôn duy trì thứ tự tiêu điểm logic trong các ứng dụng tương tác
- Luôn kiểm tra với việc điều hướng chỉ bằng bàn phím

## QUAN TRỌNG

Vui lòng thực thi pa11y và axe-core mỗi khi bạn thực hiện thay đổi đối với mã nguồn để đảm bảo tuân thủ các tiêu chuẩn hỗ trợ tiếp cận. Điều này sẽ giúp phát hiện sớm bất kỳ vấn đề nào và duy trì tiêu chuẩn cao về khả năng tiếp cận trong
