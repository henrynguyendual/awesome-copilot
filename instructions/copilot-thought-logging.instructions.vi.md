---
applyTo: "**"
description: "Xem quy trình Copilot đang theo dõi, nơi bạn có thể chỉnh sửa để định hình lại tương tác hoặc lưu lại khi cần theo dõi thêm"
---

# Hướng dẫn theo dõi Quy trình Copilot

**QUY TẮC BẮT BUỘC TUYỆT ĐỐI:**

- Bạn phải xem xét toàn bộ các hướng dẫn này trước khi thực hiện bất kỳ bước nào để hiểu đầy đủ các nguyên tắc hướng dẫn.
- Bạn phải tuân thủ chính xác các hướng dẫn này mà không có bất kỳ sai lệch nào.
- Không lặp đi lặp lại các cập nhật trạng thái trong quá trình xử lý hoặc giải thích trừ khi được yêu cầu rõ ràng. Điều này là không tốt và sẽ làm tràn ngữ cảnh phiên làm việc của Copilot.
- KHÔNG thông báo giai đoạn (không có tiêu đề "# Giai đoạn X" trong đầu ra)
- Các giai đoạn phải được thực hiện từng cái một và theo đúng thứ tự đã chỉ định.
- KHÔNG kết hợp các giai đoạn trong một phản hồi
- KHÔNG bỏ qua các giai đoạn
- KHÔNG giải thích hoặc bình luận dài dòng
- Chỉ xuất ra văn bản chính xác được chỉ định trong hướng dẫn của từng giai đoạn

# Giai đoạn 1: Khởi tạo

- Tạo tệp `\Copilot-Processing.md` trong thư mục gốc của không gian làm việc
- Điền chi tiết yêu cầu của người dùng vào tệp `\Copilot-Processing.md`
- Làm việc âm thầm không thông báo cho đến khi hoàn thành.
- Khi giai đoạn này hoàn tất, hãy ghi nhớ rằng <Giai đoạn 1> đã xong và không cần lặp lại.

# Giai đoạn 2: Lập kế hoạch

- Tạo một kế hoạch hành động vào tệp `\Copilot-Processing.md`.
- Tạo các mục hành động cụ thể, chi tiết và đủ nhỏ để theo dõi từng mục trong kế hoạch hành động với trạng thái cần làm/hoàn thành trong tệp `\Copilot-Processing.md`.
- Điều này nên bao gồm:
  - Các nhiệm vụ cụ thể cho từng mục hành động trong kế hoạch hành động như một giai đoạn.
  - Mô tả rõ ràng về những gì cần phải làm
  - Bất kỳ sự phụ thuộc hoặc điều kiện tiên quyết nào cho mỗi nhiệm vụ
  - Đảm bảo các nhiệm vụ đủ nhỏ để có thể thực hiện từng cái một
- Làm việc âm thầm không thông báo cho đến khi hoàn thành.
- Khi giai đoạn này hoàn tất, hãy ghi nhớ rằng <Giai đoạn 2> đã xong và không cần lặp lại.

# Giai đoạn 3: Thực thi

- Thực hiện các mục hành động từ kế hoạch hành động theo các nhóm/giai đoạn hợp lý
- Làm việc âm thầm không thông báo cho đến khi hoàn thành.
- Cập nhật tệp `\Copilot-Processing.md` và đánh dấu (các) mục hành động là đã hoàn thành trong phần theo dõi.
- Khi một giai đoạn hoàn tất, hãy ghi nhớ rằng giai đoạn cụ thể từ `\Copilot-Processing.md` đã xong và không cần lặp lại.
- Lặp lại mô hình này cho đến khi tất cả các mục hành động được hoàn thành

# Giai đoạn 4: Tóm tắt

- Thêm tóm tắt vào `\Copilot-Processing.md`
- Làm việc âm thầm không thông báo cho đến khi hoàn thành.
- Chỉ thực hiện khi TẤT CẢ các hành động đã hoàn thành
- Thông báo cho người dùng: "Đã thêm tóm tắt cuối cùng vào `\Copilot-Processing.md`."
- Nhắc người dùng xem lại bản tóm tắt và xác nhận hoàn thành quy trình, sau đó xóa tệp khi xong để nó không được thêm vào kho lưu trữ.

**QUY TẮC THỰC THI:**

- KHÔNG BAO GIỜ viết tiêu đề "# Giai đoạn X" trong các phản hồi
- KHÔNG BAO GIỜ lặp lại từ "Giai đoạn" trong đầu ra trừ khi được yêu cầu rõ ràng
- KHÔNG BAO GIỜ cung cấp giải thích ngoài văn bản chính xác đã chỉ định
- KHÔNG BAO GIỜ kết hợp nhiều giai đoạn trong một phản hồi
- KHÔNG BAO GIỜ tiếp tục qua giai đoạn hiện tại mà không có sự đồng ý của người dùng
- Nếu bạn thấy mình đang nói dài dòng, DỪNG LẠI và chỉ cung cấp đầu ra được yêu cầu
- Nếu bạn thấy mình sắp bỏ qua một giai đoạn, DỪNG LẠI và quay lại giai đoạn chính xác
- Nếu bạn thấy mình đang kết hợp các giai đoạn, DỪNG LẠI và chỉ thực hiện giai đoạn hiện tại
