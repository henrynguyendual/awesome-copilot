---
applyTo: "**/.copilot-tracking/changes/*.md"
description: "Hướng dẫn triển khai kế hoạch tác vụ với theo dõi tiến độ và ghi lại thay đổi - Mang đến cho bạn bởi microsoft/edge-ai"
---

# Hướng dẫn Triển khai Kế hoạch Tác vụ

Bạn sẽ triển khai kế hoạch tác vụ cụ thể của mình nằm trong `.copilot-tracking/plans/**` và `.copilot-tracking/details/**`. Mục tiêu của bạn là triển khai từng bước trong các tệp kế hoạch một cách tuần tự và hoàn chỉnh để tạo ra phần mềm chất lượng cao, hoạt động tốt và đáp ứng tất cả các yêu cầu đã chỉ định.

Tiến độ triển khai PHẢI được theo dõi trong một tệp thay đổi tương ứng nằm trong `.copilot-tracking/changes/**`.

## Quy trình Triển khai Cốt lõi

### 1. Phân tích và Chuẩn bị Kế hoạch

**PHẢI hoàn thành trước khi bắt đầu triển khai:**

- **BẮT BUỘC**: Đọc và hiểu đầy đủ tệp kế hoạch bao gồm phạm vi, mục tiêu, tất cả các giai đoạn và mọi mục trong danh sách kiểm tra.
- **BẮT BUỘC**: Đọc và hiểu đầy đủ tệp thay đổi tương ứng - nếu bất kỳ phần nào bị thiếu trong ngữ cảnh, hãy đọc lại toàn bộ tệp bằng `read_file`.
- **BẮT BUỘC**: Xác định tất cả các tệp được tham chiếu trong kế hoạch và kiểm tra chúng để lấy ngữ cảnh.
- **BẮT BUỘC**: Hiểu cấu trúc và quy ước hiện tại của dự án.

### 2. Quy trình Triển khai Hệ thống

**Triển khai từng tác vụ trong kế hoạch một cách có hệ thống:**

1.  **Xử lý các tác vụ theo thứ tự** - Tuân thủ chính xác trình tự kế hoạch, mỗi lần một tác vụ.
2.  **BẮT BUỘC trước khi triển khai bất kỳ tác vụ nào:**

    - **LUÔN LUÔN đảm bảo việc triển khai được liên kết với một tác vụ cụ thể từ kế hoạch.**
    - **LUÔN LUÔN đọc toàn bộ phần chi tiết cho tác vụ đó từ tệp markdown chi tiết liên quan trong `.copilot-tracking/details/**`\*\*
    - **HIỂU ĐẦY ĐỦ tất cả các chi tiết triển khai trước khi tiếp tục.**
    - Thu thập bất kỳ ngữ cảnh bổ sung cần thiết nào.

3.  **Triển khai tác vụ một cách hoàn chỉnh với mã nguồn hoạt động:**

    - Tuân theo các mẫu và quy ước mã nguồn hiện có từ không gian làm việc.
    - Tạo chức năng hoạt động đáp ứng tất cả các yêu cầu của tác vụ được chỉ định trong phần chi tiết.
    - Bao gồm xử lý lỗi phù hợp, tài liệu hóa và tuân thủ các phương pháp hay nhất.

4.  **Đánh dấu tác vụ hoàn thành và cập nhật theo dõi thay đổi:**
    - Cập nhật tệp kế hoạch: thay đổi `[ ]` thành `[x]` cho tác vụ đã hoàn thành.
    - **BẮT BUỘC sau khi hoàn thành MỌI tác vụ**: Cập nhật tệp thay đổi bằng cách thêm vào các mục Đã thêm, Đã sửa đổi hoặc Đã xóa với đường dẫn tệp tương đối và tóm tắt một câu về những gì đã được triển khai.
    - **BẮT BUỘC**: Nếu có bất kỳ thay đổi nào khác với kế hoạch và chi tiết tác vụ, hãy nêu rõ trong phần liên quan rằng thay đổi đó được thực hiện ngoài kế hoạch và bao gồm lý do cụ thể.
    - Nếu TẤT CẢ các tác vụ trong một giai đoạn đều hoàn thành `[x]`, hãy đánh dấu tiêu đề giai đoạn là hoàn thành `[x]`.

### 3. Tiêu chuẩn Chất lượng Triển khai

**Mọi hoạt động triển khai PHẢI:**

- Tuân theo các mẫu và quy ước hiện có của không gian làm việc (kiểm tra thư mục `copilot/` để biết các tiêu chuẩn).
- Triển khai chức năng hoàn chỉnh, hoạt động và đáp ứng tất cả các yêu cầu của tác vụ.
- Bao gồm xử lý lỗi và xác thực phù hợp.
- Sử dụng quy ước đặt tên và cấu trúc mã nhất quán từ không gian làm việc.
- Thêm tài liệu và nhận xét cần thiết cho logic phức tạp.
- Đảm bảo khả năng tương thích với các hệ thống và phụ thuộc hiện có.

### 4. Tiến độ và Xác thực Liên tục

**Sau khi triển khai mỗi tác vụ:**

1.  Xác thực các thay đổi đã thực hiện so với các yêu cầu của tác vụ từ tệp chi tiết.
2.  Sửa bất kỳ vấn đề nào trước khi chuyển sang tác vụ tiếp theo.
3.  **BẮT BUỘC**: Cập nhật tệp kế hoạch để đánh dấu các tác vụ đã hoàn thành `[x]`.
4.  **BẮT BUỘC sau MỖI lần hoàn thành tác vụ**: Cập nhật tệp thay đổi bằng cách thêm vào các mục Đã thêm, Đã sửa đổi hoặc Đã xóa với đường dẫn tệp tương đối và tóm tắt một câu về những gì đã được triển khai.
5.  Tiếp tục với tác vụ chưa được đánh dấu tiếp theo.

**Tiếp tục cho đến khi:**

- Tất cả các tác vụ trong kế hoạch được đánh dấu hoàn thành `[x]`.
- Tất cả các tệp được chỉ định đã được tạo hoặc cập nhật với mã nguồn hoạt động.
- Tất cả các tiêu chí thành công từ kế hoạch đã được xác minh.

### 5. Hướng dẫn Thu thập Tài liệu Tham khảo

**Khi thu thập tài liệu tham khảo bên ngoài:**

- Tập trung vào các ví dụ triển khai thực tế hơn là tài liệu lý thuyết.
- Xác thực rằng các nguồn bên ngoài chứa các mẫu thực sự có thể sử dụng được.
- Điều chỉnh các mẫu bên ngoài để phù hợp với quy ước và tiêu chuẩn của không gian làm việc.

**Khi triển khai từ tài liệu tham khảo:**

- Ưu tiên tuân theo các mẫu và quy ước của không gian làm việc trước, sau đó mới đến các mẫu bên ngoài.
- Triển khai chức năng hoàn chỉnh, hoạt động thay vì chỉ là các ví dụ.
- Đảm bảo tất cả các phụ thuộc và cấu hình được tích hợp đúng cách.
- Đảm bảo việc triển khai hoạt động trong cấu trúc dự án hiện có.

### 6. Hoàn thành và Tài liệu hóa

**Việc triển khai được coi là hoàn thành khi:**

- Tất cả các tác vụ trong kế hoạch được đánh dấu hoàn thành `[x]`.
- Tất cả các tệp được chỉ định đều tồn tại với mã nguồn hoạt động.
- Tất cả các tiêu chí thành công từ kế hoạch được xác minh.
- Không còn lỗi triển khai nào.

**Bước cuối cùng - cập nhật tệp thay đổi với tóm tắt bản phát hành:**

- Chỉ thêm phần Tóm tắt Bản phát hành sau khi TẤT CẢ các giai đoạn được đánh dấu hoàn thành `[x]`.
- Ghi lại danh sách tệp hoàn chỉnh và tóm tắt triển khai tổng thể cho tài liệu phát hành.

### 7. Giải quyết Vấn đề

**Khi gặp sự cố triển khai:**

- Ghi lại vấn đề cụ thể một cách rõ ràng.
- Thử các phương pháp tiếp cận thay thế hoặc các thuật ngữ tìm kiếm khác.
- Sử dụng các mẫu của không gian làm việc làm phương án dự phòng khi tài liệu tham khảo bên ngoài không hiệu quả.
- Tiếp tục với thông tin có sẵn thay vì dừng lại hoàn toàn.
- Ghi chú lại bất kỳ vấn đề nào chưa được giải quyết trong tệp kế hoạch để tham khảo trong tương lai.

## Luồng công việc Triển khai

```
1. Đọc và hiểu đầy đủ tệp kế hoạch và tất cả các danh sách kiểm tra.
2. Đọc và hiểu đầy đủ tệp thay đổi (đọc lại toàn bộ tệp nếu thiếu ngữ cảnh).
3. Đối với mỗi tác vụ chưa được đánh dấu:
   a. Đọc toàn bộ phần chi tiết cho tác vụ đó từ tệp markdown chi tiết.
   b. Hiểu đầy đủ tất cả các yêu cầu triển khai.
   c. Triển khai tác vụ với mã nguồn hoạt động theo các mẫu của không gian làm việc.
   d. Xác thực việc triển khai đáp ứng các yêu cầu của tác vụ.
   e. Đánh dấu tác vụ hoàn thành [x] trong tệp kế hoạch.
   f. Cập nhật tệp thay đổi với các mục Đã thêm, Đã sửa đổi hoặc Đã xóa.
   g. Nêu rõ bất kỳ sự khác biệt nào so với kế hoạch/chi tiết trong các phần liên quan kèm theo lý do cụ thể.
4. Lặp lại cho đến khi tất cả các tác vụ hoàn thành.
5. Chỉ sau khi TẤT CẢ các giai đoạn hoàn thành [x]: Thêm Tóm tắt Bản phát hành cuối cùng vào tệp thay đổi.
```

## Tiêu chí Thành công

Việc triển khai được coi là hoàn thành khi:

- ✅ Tất cả các tác vụ trong kế hoạch được đánh dấu hoàn thành `[x]`
- ✅ Tất cả các tệp được chỉ định chứa mã nguồn hoạt động
- ✅ Mã nguồn tuân theo các mẫu và quy ước của không gian làm việc
- ✅ Tất cả chức năng hoạt động như mong đợi trong dự án
- ✅ Tệp thay đổi được cập nhật sau mỗi lần hoàn thành tác vụ với các mục Đã thêm, Đã sửa đổi hoặc Đã xóa
- ✅ Tệp thay đổi ghi lại tất cả các giai đoạn với tài liệu chi tiết sẵn sàng cho việc phát hành và tóm tắt bản phát hành cuối cùng

## Tệp Mẫu Ghi lại Thay đổi

Sử dụng mẫu sau cho tệp thay đổi để theo dõi tiến độ triển khai cho các bản phát hành.
Thay thế `{{ }}` bằng các giá trị thích hợp. Tạo tệp này trong `./.copilot-tracking/changes/` với tên tệp: `YYYYMMDD-task-description-changes.md`

**QUAN TRỌNG**: Cập nhật tệp này sau MỖI lần hoàn thành tác vụ bằng cách thêm vào các mục Đã thêm, Đã sửa đổi hoặc Đã xóa.
**BẮT BUỘC**: Luôn bao gồm dòng sau ở đầu tệp thay đổi: `<!-- markdownlint-disable-file -->`

<!-- <changes-template> -->

```markdown
<!-- markdownlint-disable-file -->

# Thay đổi của Bản phát hành: {{task name}}

**Kế hoạch Liên quan**: {{plan-file-name}}
**Ngày Triển khai**: {{YYYY-MM-DD}}

## Tóm tắt

{{Mô tả ngắn gọn về những thay đổi tổng thể được thực hiện cho bản phát hành này}}

## Các thay đổi

### Đã thêm

- {{relative-file-path}} - {{tóm tắt một câu về những gì đã được triển khai}}

### Đã sửa đổi

- {{relative-file-path}} - {{tóm tắt một câu về những gì đã được thay đổi}}

### Đã xóa

- {{relative-file-path}} - {{tóm tắt một câu về những gì đã được xóa}}

## Tóm tắt Bản phát hành

**Tổng số Tệp bị ảnh hưởng**: {{number}}

### Các Tệp đã tạo ({{count}})

- {{file-path}} - {{mục đích}}

### Các Tệp đã sửa đổi ({{count}})

- {{file-path}} - {{những-thay-đổi-đã-thực-hiện}}

### Các Tệp đã xóa ({{count}})

- {{file-path}} - {{lý do}}

### Phụ thuộc & Cơ sở hạ tầng

- **Phụ thuộc Mới**: {{danh-sách-các-phụ-thuộc-mới}}
- **Phụ thuộc được Cập nhật**: {{danh-sách-các-phụ-thuộc-được-cập-nhật}}
- **Thay đổi Cơ sở hạ tầng**: {{cập-nhật-cơ-sở-hạ-tầng}}
- **Cập nhật Cấu hình**: {{thay-đổi-cấu-hình}}

### Ghi chú Triển khai

{{Bất kỳ cân nhắc hoặc các bước triển khai cụ thể nào}}
```
