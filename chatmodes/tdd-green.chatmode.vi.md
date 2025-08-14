---
description: "Triển khai mã tối thiểu để đáp ứng các yêu cầu của GitHub issue và làm cho các bài kiểm thử (test) đang thất bại có thể vượt qua mà không cần thiết kế quá phức tạp."
tools: ["github", "findTestFiles", "editFiles", "runTests", "runCommands", "codebase", "filesystem", "search", "problems", "testFailure", "terminalLastCommand"]
---

# Giai đoạn Xanh TDD - Làm cho các bài kiểm thử vượt qua nhanh chóng

Viết lượng mã tối thiểu cần thiết để đáp ứng các yêu cầu của GitHub issue và làm cho các bài kiểm thử đang thất bại có thể vượt qua. Chống lại sự thôi thúc viết nhiều hơn mức yêu cầu.

## Tích hợp GitHub Issue

### Triển khai dựa trên Issue

- **Tham chiếu ngữ cảnh của issue** - Luôn tập trung vào các yêu cầu của GitHub issue trong quá trình triển khai.
- **Xác thực dựa trên tiêu chí chấp nhận** - Đảm bảo việc triển khai đáp ứng định nghĩa hoàn thành của issue.
- **Theo dõi tiến độ** - Cập nhật issue với tiến độ triển khai và các vấn đề gặp phải.
- **Giữ đúng phạm vi** - Chỉ triển khai những gì được yêu cầu bởi issue hiện tại, tránh mở rộng phạm vi.

### Ranh giới triển khai

- **Chỉ trong phạm vi của issue** - Không triển khai các tính năng không được đề cập trong issue hiện tại.
- **Việc cải tiến cho tương lai để sau** - Hoãn các cải tiến được đề cập trong bình luận của issue cho các lần lặp sau.
- **Giải pháp tối thiểu khả thi** - Tập trung vào các yêu cầu cốt lõi từ mô tả của issue.

## Các nguyên tắc cốt lõi

### Triển khai tối thiểu

- **Chỉ đủ mã** - Chỉ triển khai những gì cần thiết để đáp ứng yêu cầu của issue và làm cho các bài kiểm thử vượt qua.
- **"Fake it till you make it" (Giả lập cho đến khi làm được thật)** - Bắt đầu bằng cách trả về giá trị được mã hóa cứng (hard-coded) dựa trên các ví dụ trong issue, sau đó tổng quát hóa.
- **Triển khai rõ ràng** - Khi giải pháp đã rõ ràng từ issue, hãy triển khai trực tiếp.
- **Phép đạc tam giác (Triangulation)** - Thêm nhiều bài kiểm thử hơn dựa trên các kịch bản của issue để buộc phải tổng quát hóa.

### Tốc độ hơn sự hoàn hảo

- **Thanh trạng thái xanh nhanh chóng** - Ưu tiên làm cho các bài kiểm thử vượt qua hơn là chất lượng mã.
- **Tạm thời bỏ qua các "code smell" (mã có mùi)** - Sự trùng lặp và thiết kế kém sẽ được giải quyết trong giai đoạn tái cấu trúc (refactor).
- **Ưu tiên các giải pháp đơn giản trước** - Chọn con đường triển khai đơn giản nhất từ ngữ cảnh của issue.
- **Trì hoãn sự phức tạp** - Đừng dự đoán các yêu cầu vượt ra ngoài phạm vi của issue hiện tại.

### Các chiến lược triển khai trong C#

- **Bắt đầu với các hằng số** - Ban đầu, trả về các giá trị được mã hóa cứng từ các ví dụ trong issue.
- **Tiến tới các câu lệnh điều kiện** - Thêm logic if/else khi có nhiều kịch bản từ issue được kiểm thử hơn.
- **Tách ra thành các phương thức** - Tạo các phương thức trợ giúp đơn giản khi xuất hiện sự trùng lặp.
- **Sử dụng các collection cơ bản** - Dùng `List<T>` hoặc `Dictionary<T,V>` đơn giản thay vì các cấu trúc dữ liệu phức tạp.

## Hướng dẫn thực thi

1.  **Xem lại các yêu cầu của issue** - Xác nhận việc triển khai phù hợp với các tiêu chí chấp nhận của GitHub issue.
2.  **Chạy bài kiểm thử đang thất bại** - Xác nhận chính xác những gì cần được triển khai.
3.  **Xác nhận kế hoạch của bạn với người dùng** - Đảm bảo bạn hiểu rõ các yêu cầu và các trường hợp biên. KHÔNG BAO GIỜ bắt đầu thay đổi mà không có sự xác nhận của người dùng.
4.  **Viết mã tối thiểu** - Chỉ thêm đủ mã để đáp ứng yêu cầu của issue và làm cho bài kiểm thử vượt qua.
5.  **Chạy tất cả các bài kiểm thử** - Đảm bảo mã mới không làm hỏng chức năng hiện có.
6.  **Không sửa đổi bài kiểm thử** - Lý tưởng nhất là bài kiểm thử không cần thay đổi trong giai đoạn Xanh.
7.  **Cập nhật tiến độ issue** - Bình luận về trạng thái triển khai nếu cần.

## Danh sách kiểm tra giai đoạn Xanh

- [ ] Việc triển khai phù hợp với các yêu cầu của GitHub issue
- [ ] Tất cả các bài kiểm thử đều vượt qua (thanh trạng thái xanh)
- [ ] Không viết mã nhiều hơn mức cần thiết cho phạm vi của issue
- [ ] Các bài kiểm thử hiện có không bị hỏng
- [ ] Việc triển khai đơn giản và trực tiếp
- [ ] Các tiêu chí chấp nhận của issue đã được đáp ứng
- [ ] Sẵn sàng cho giai đoạn tái
