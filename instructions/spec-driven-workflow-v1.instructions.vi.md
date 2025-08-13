---
description: "Quy trình làm việc dựa trên Đặc tả v1 cung cấp một phương pháp tiếp cận có cấu trúc để phát triển phần mềm, đảm bảo rằng các yêu cầu được định nghĩa rõ ràng, các thiết kế được lên kế hoạch tỉ mỉ, và việc triển khai được ghi lại và xác thực một cách kỹ lưỡng."
applyTo: "**"
---

# Quy trình làm việc dựa trên Đặc tả v1

**Quy trình làm việc dựa trên Đặc tả:**
Thu hẹp khoảng cách giữa yêu cầu và triển khai.

**Luôn duy trì các tạo tác (artifacts) sau:**

- **`requirements.md`**: Câu chuyện người dùng (user stories) và tiêu chí chấp nhận (acceptance criteria) theo ký pháp EARS có cấu trúc.
- **`design.md`**: Kiến trúc kỹ thuật, biểu đồ tuần tự, các cân nhắc khi triển khai.
- **`tasks.md`**: Kế hoạch triển khai chi tiết, có thể theo dõi.

## Khung tài liệu chung

**Quy tắc tài liệu:**
Sử dụng các mẫu chi tiết làm **nguồn sự thật duy nhất** cho tất cả tài liệu.

**Các định dạng tóm tắt:**
Chỉ sử dụng cho các tạo tác ngắn gọn như nhật ký thay đổi (changelogs) và mô tả pull request.

### Các mẫu tài liệu chi tiết

#### Mẫu tài liệu hành động (Tất cả các bước/Thực thi/Kiểm thử)

```bash
### [LOẠI] - [HÀNH ĐỘNG] - [DẤU THỜI GIAN]
**Mục tiêu**: [Mục tiêu đang được thực hiện]
**Bối cảnh**: [Trạng thái hiện tại, yêu cầu, và tham chiếu đến các bước trước đó]
**Quyết định**: [Phương pháp được chọn và lý do, tham chiếu đến Biên bản Quyết định nếu có]
**Thực thi**: [Các bước đã thực hiện với tham số và lệnh đã sử dụng. Đối với mã nguồn, bao gồm đường dẫn tệp.]
**Đầu ra**: [Kết quả, nhật ký, đầu ra lệnh và các chỉ số đầy đủ và không cắt xén]
**Xác thực**: [Phương pháp xác minh thành công và kết quả. Nếu thất bại, bao gồm kế hoạch khắc phục.]
**Tiếp theo**: [Kế hoạch tiếp tục tự động đến hành động cụ thể tiếp theo]
```

#### Mẫu Biên bản Quyết định (Tất cả các quyết định)

```bash
### Quyết định - [DẤU THỜI GIAN]
**Quyết định**: [Điều đã được quyết định]
**Bối cảnh**: [Tình huống yêu cầu quyết định và dữ liệu thúc đẩy nó]
**Các lựa chọn**: [Các phương án thay thế đã được đánh giá với ưu và nhược điểm ngắn gọn]
**Lý do**: [Tại sao lựa chọn được chọn là vượt trội, với các đánh đổi được nêu rõ ràng]
**Tác động**: [Hậu quả dự kiến đối với việc triển khai, khả năng bảo trì và hiệu suất]
**Xem xét lại**: [Điều kiện hoặc lịch trình để đánh giá lại quyết định này]
```

### Các định dạng tóm tắt (dành cho báo cáo)

#### Nhật ký hành động tinh gọn

Để tạo ra các nhật ký thay đổi ngắn gọn. Mỗi mục nhật ký được lấy từ một Tài liệu Hành động đầy đủ.

`[LOẠI][DẤU THỜI GIAN] Mục tiêu: [X] → Hành động: [Y] → Kết quả: [Z] → Tiếp theo: [W]`

#### Biên bản Quyết định rút gọn

Để sử dụng trong các bản tóm tắt pull request hoặc tóm tắt cho quản lý.

`Quyết định: [X] | Lý do: [Y] | Tác động: [Z] | Xem xét lại: [Ngày]`

## Quy trình thực thi (Vòng lặp 6 giai đoạn)

**Không bao giờ bỏ qua bất kỳ bước nào. Sử dụng thuật ngữ nhất quán. Giảm sự mơ hồ.**

### **Giai đoạn 1: PHÂN TÍCH (ANALYZE)**

**Mục tiêu:**

- Hiểu rõ vấn đề.
- Phân tích hệ thống hiện có.
- Tạo ra một bộ yêu cầu rõ ràng, có thể kiểm thử được.
- Suy nghĩ về các giải pháp khả thi và tác động của chúng.

**Danh sách kiểm tra:**

- [ ] Đọc tất cả mã nguồn, tài liệu, kiểm thử và nhật ký được cung cấp. - Ghi lại danh sách tệp, tóm tắt và kết quả phân tích ban đầu.
- [ ] Định nghĩa yêu cầu theo **Ký pháp EARS**: - Chuyển đổi các yêu cầu tính năng thành các yêu cầu có cấu trúc, có thể kiểm thử. - Định dạng: `KHI [một điều kiện hoặc sự kiện], HỆ THỐNG SẼ [hành vi mong đợi]`
- [ ] Xác định các phụ thuộc và ràng buộc. - Ghi lại biểu đồ phụ thuộc với các rủi ro và chiến lược giảm thiểu.
- [ ] Sơ đồ hóa luồng dữ liệu và tương tác. - Ghi lại các biểu đồ tương tác hệ thống và mô hình dữ liệu.
- [ ] Liệt kê các trường hợp biên và lỗi. - Ghi lại một ma trận trường hợp biên toàn diện và các điểm có thể xảy ra lỗi.
- [ ] Đánh giá mức độ tự tin. - Tạo ra một **Điểm Tự tin (0-100%)** dựa trên sự rõ ràng của yêu cầu, độ phức tạp và phạm vi vấn đề. - Ghi lại điểm số và lý do của nó.

**Ràng buộc quan trọng:**

- **Không tiếp tục cho đến khi tất cả các yêu cầu đều rõ ràng và được ghi lại.**

### **Giai đoạn 2: THIẾT KẾ (DESIGN)**

**Mục tiêu:**

- Tạo ra một thiết kế kỹ thuật toàn diện và một kế hoạch triển khai chi tiết.

**Danh sách kiểm tra:**

- [ ] **Xác định chiến lược thực thi thích ứng dựa trên Điểm Tự tin:**

  - **Tự tin cao (>85%)**
    - Soạn thảo một kế hoạch triển khai toàn diện, từng bước.
    - Bỏ qua các bước chứng minh khái niệm (proof-of-concept).
    - Tiến hành triển khai đầy đủ, tự động.
    - Duy trì tài liệu toàn diện tiêu chuẩn.
  - **Tự tin trung bình (66–85%)**
    - Ưu tiên một **Chứng minh Khái niệm (PoC)** hoặc **Sản phẩm Khả thi Tối thiểu (MVP)**.
    - Xác định tiêu chí thành công rõ ràng cho PoC/MVP.
    - Xây dựng và xác thực PoC/MVP trước, sau đó mở rộng kế hoạch theo từng bước.
    - Ghi lại mục tiêu, thực thi và kết quả xác thực của PoC/MVP.
  - **Tự tin thấp (<66%)**
    - Dành giai đoạn đầu tiên để nghiên cứu và xây dựng kiến thức.
    - Sử dụng tìm kiếm ngữ nghĩa và phân tích các triển khai tương tự.
    - Tổng hợp các phát hiện vào một tài liệu nghiên cứu.
    - Chạy lại giai đoạn PHÂN TÍCH sau khi nghiên cứu.
    - Báo cáo cấp trên chỉ khi mức độ tự tin vẫn thấp.

- [ ] **Ghi lại thiết kế kỹ thuật trong `design.md`:**

  - **Kiến trúc:** Tổng quan cấp cao về các thành phần và tương tác.
  - **Luồng dữ liệu:** Biểu đồ và mô tả.
  - **Giao diện:** Hợp đồng API, lược đồ, chữ ký hàm công khai.
  - **Mô hình dữ liệu:** Cấu trúc dữ liệu và lược đồ cơ sở dữ liệu.

- [ ] **Ghi lại việc xử lý lỗi:**

  - Tạo một ma trận lỗi với các quy trình và phản hồi mong đợi.

- [ ] **Xác định chiến lược kiểm thử đơn vị.**

- [ ] **Tạo kế hoạch triển khai trong `tasks.md`:**
  - Đối với mỗi nhiệm vụ, bao gồm mô tả, kết quả mong đợi và các phụ thuộc.

**Ràng buộc quan trọng:**

- **Không chuyển sang triển khai cho đến khi thiết kế và kế hoạch được hoàn thành và xác thực.**

### **Giai đoạn 3: TRIỂN KHAI (IMPLEMENT)**

**Mục tiêu:**

- Viết mã nguồn chất lượng sản phẩm theo thiết kế và kế hoạch.

**Danh sách kiểm tra:**

- [ ] Viết mã theo từng phần nhỏ, có thể kiểm thử. - Ghi lại mỗi phần với các thay đổi mã nguồn, kết quả và liên kết đến kiểm thử.
- [ ] Triển khai từ các phụ thuộc trở lên. - Ghi lại thứ tự giải quyết, lý do và xác minh.
- [ ] Tuân thủ các quy ước. - Ghi lại sự tuân thủ và bất kỳ sai lệch nào bằng một Biên bản Quyết định.
- [ ] Thêm các bình luận có ý nghĩa. - Tập trung vào mục đích ("tại sao"), không phải cơ chế ("cái gì").
- [ ] Tạo các tệp như đã lên kế hoạch. - Ghi lại nhật ký tạo tệp.
- [ ] Cập nhật trạng thái nhiệm vụ theo thời gian thực.

**Ràng buộc quan trọng:**

- **Không hợp nhất (merge) hoặc triển khai (deploy) mã nguồn cho đến khi tất cả các bước triển khai được ghi lại và kiểm thử.**

### **Giai đoạn 4: XÁC THỰC (VALIDATE)**

**Mục tiêu:**

- Xác minh rằng việc triển khai đáp ứng tất cả các yêu cầu và tiêu chuẩn chất lượng.

**Danh sách kiểm tra:**

- [ ] Thực thi các kiểm thử tự động. - Ghi lại đầu ra, nhật ký và báo cáo độ bao phủ. - Đối với các lỗi, ghi lại phân tích nguyên nhân gốc rễ và cách khắc phục.
- [ ] Thực hiện xác minh thủ công nếu cần. - Ghi lại các quy trình, danh sách kiểm tra và kết quả.
- [ ] Kiểm thử các trường hợp biên và lỗi. - Ghi lại kết quả và bằng chứng về việc xử lý lỗi chính xác.
- [ ] Xác minh hiệu suất. - Ghi lại các chỉ số và phân tích các phần quan trọng.
- [ ] Ghi lại dấu vết thực thi. - Ghi lại phân tích đường dẫn và hành vi thời gian chạy.

**Ràng buộc quan trọng:**

- **Không tiếp tục cho đến khi tất cả các bước xác thực được hoàn thành và tất cả các vấn đề được giải quyết.**

### **Giai đoạn 5: NHÌN LẠI (REFLECT)**

**Mục tiêu:**

- Cải thiện cơ sở mã nguồn, cập nhật tài liệu và phân tích hiệu suất.

**Danh sách kiểm tra:**

- [ ] Tái cấu trúc (refactor) để dễ bảo trì. - Ghi lại các quyết định, so sánh trước/sau và tác động.
- [ ] Cập nhật tất cả tài liệu dự án. - Đảm bảo tất cả các tệp README, biểu đồ và bình luận đều được cập nhật.
- [ ] Xác định các cải tiến tiềm năng. - Ghi lại danh sách công việc tồn đọng (backlog) với mức độ ưu tiên.
- [ ] Xác thực các tiêu chí thành công. - Ghi lại ma trận xác minh cuối cùng.
- [ ] Thực hiện phân tích tổng hợp (meta-analysis). - Nhìn lại hiệu quả, việc sử dụng công cụ và sự tuân thủ quy trình.
- [ ] Tự động tạo các vấn đề về nợ kỹ thuật. - Ghi lại danh sách và kế hoạch khắc phục.

**Ràng buộc quan trọng:**

- **Không đóng giai đoạn cho đến khi tất cả tài liệu và các hành động cải tiến được ghi lại.**

### **Giai đoạn 6: BÀN GIAO (HANDOFF)**

**Mục tiêu:**

- Đóng gói công việc để xem xét và triển khai, và chuyển sang nhiệm vụ tiếp theo.

**Danh sách kiểm tra:**

- [ ] Tạo tóm tắt cho quản lý. - Sử dụng định dạng **Biên bản Quyết định rút gọn**.
- [ ] Chuẩn bị pull request (nếu có):
  1. Tóm tắt cho quản lý.
  2. Nhật ký thay đổi từ **Nhật ký hành động tinh gọn**.
  3. Liên kết đến các tạo tác xác thực và Biên bản Quyết định.
  4. Liên kết đến các tệp `requirements.md`, `design.md`, và `tasks.md` cuối cùng.
- [ ] Hoàn tất không gian làm việc. - Lưu trữ các tệp trung gian, nhật ký và tạo tác tạm thời vào `.agent_work/`.
- [ ] Tiếp tục nhiệm vụ tiếp theo. - Ghi lại việc chuyển giao hoặc hoàn thành.

**Ràng buộc quan trọng:**

- **Không coi nhiệm vụ là hoàn thành cho đến khi tất cả các bước bàn giao được kết thúc và ghi lại.**

## Quy trình khắc phục sự cố & Thử lại

**Nếu bạn gặp lỗi, sự mơ hồ hoặc trở ngại:**

**Danh sách kiểm tra:**

1. **Phân tích lại**:
   - Quay lại giai đoạn PHÂN TÍCH.
   - Xác nhận tất cả các yêu cầu và ràng buộc đều rõ ràng và đầy đủ.
2. **Thiết kế lại**:
   - Quay lại giai đoạn THIẾT KẾ.
   - Cập nhật thiết kế kỹ thuật, kế hoạch hoặc các phụ thuộc khi cần thiết.
3. **Lập kế hoạch lại**:
   - Điều chỉnh kế hoạch triển khai trong `tasks.md` để giải quyết các phát hiện mới.
4. **Thử lại thực thi**:
   - Thực thi lại các bước thất bại với các tham số hoặc logic đã được sửa chữa.
5. **Báo cáo cấp trên (Escalate)**:
   - Nếu vấn đề vẫn tồn tại sau khi thử lại, hãy tuân theo quy trình báo cáo cấp trên.

**Ràng buộc quan trọng:**

- **Không bao giờ tiếp tục với các lỗi hoặc sự mơ hồ chưa được giải quyết. Luôn ghi lại các bước khắc phục sự cố và kết quả.**

## Quản lý Nợ kỹ thuật (Tự động)

### Nhận dạng & Ghi lại

- **Chất lượng mã nguồn**: Liên tục đánh giá chất lượng mã nguồn trong quá trình triển khai bằng cách sử dụng phân tích tĩnh.
- **Đường tắt**: Ghi lại rõ ràng tất cả các quyết định ưu tiên tốc độ hơn chất lượng cùng với hậu quả của chúng trong một Biên bản Quyết định.
- **Không gian làm việc**: Theo dõi sự thiếu tổ chức và sự không nhất quán trong cách đặt tên.
- **Tài liệu**: Theo dõi tài liệu không đầy đủ, lỗi thời hoặc bị thiếu.

### Mẫu tạo vấn đề tự động

```text
**Tiêu đề**: [Nợ kỹ thuật] - [Mô tả ngắn gọn]
**Ưu tiên**: [Cao/Trung bình/Thấp dựa trên tác động kinh doanh và chi phí khắc phục]
**Vị trí**: [Đường dẫn tệp và số dòng]
**Lý do**: [Tại sao nợ phát sinh, liên kết đến một Biên bản Quyết định nếu có]
**Tác động**: [Hậu quả hiện tại và tương lai (ví dụ: làm chậm quá trình phát triển, tăng nguy cơ lỗi)]
**Khắc phục**: [Các bước giải quyết cụ thể, có thể hành động]
**Nỗ lực**: [Ước tính để giải quyết (ví dụ: kích thước áo phông: S, M, L)]
```

### Khắc phục (Ưu tiên tự động)

- Ưu tiên dựa trên rủi ro với phân tích phụ thuộc.
- Ước tính nỗ lực để hỗ trợ lập kế hoạch trong tương lai.
- Đề xuất các chiến lược di chuyển cho các nỗ lực tái cấu trúc lớn.

## Đảm bảo chất lượng (Tự động)

### Giám sát liên tục

- **Phân tích tĩnh**: Linting cho phong cách mã nguồn, chất lượng, lỗ hổng bảo mật và tuân thủ quy tắc kiến trúc.
- **Phân tích động**: Theo dõi hành vi thời gian chạy và hiệu suất trong môi trường thử nghiệm (staging).
- **Tài liệu**: Kiểm tra tự động về tính đầy đủ và chính xác của tài liệu (ví dụ: liên kết, định dạng).

### Các chỉ số chất lượng (Theo dõi tự động)

- Tỷ lệ phần trăm độ bao phủ mã nguồn và phân tích khoảng trống.
- Điểm độ phức tạp Cyclomatic cho mỗi hàm/phương thức.
- Đánh giá chỉ số khả năng bảo trì.
- Tỷ lệ nợ kỹ thuật (ví dụ: thời gian khắc phục ước tính so với thời gian phát triển).
- Tỷ lệ phần trăm độ bao phủ tài liệu (ví dụ: các phương thức công khai có bình luận).

## Tham khảo Ký pháp EARS

**EARS (Easy Approach to Requirements Syntax)** - Định dạng tiêu chuẩn cho các yêu cầu:

- **Phổ biến (Ubiquitous)**: `HỆ THỐNG SẼ [hành vi mong đợi]`
- **Hướng sự kiện (Event-driven)**: `KHI [sự kiện kích hoạt] HỆ THỐNG SẼ [hành vi mong đợi]`
- **Hướng trạng thái (State-driven)**: `TRONG KHI [ở trạng thái cụ thể] HỆ THỐNG SẼ [hành vi mong đợi]`
- **Hành vi không mong muốn (Unwanted behavior)**: `NẾU [điều kiện không mong muốn] THÌ HỆ THỐNG SẼ [phản hồi bắt buộc]`
- **Tùy chọn (Optional)**: `NƠI [tính năng được bao gồm] HỆ THỐNG SẼ [hành vi mong đợi]`
- **Phức tạp (Complex)**: Kết hợp các mẫu trên cho các yêu cầu phức tạp

Mỗi yêu cầu phải:

- **Có thể kiểm thử (Testable)**: Có thể được xác minh thông qua kiểm thử tự động hoặc thủ công
- **Không mơ hồ (Unambiguous)**: Chỉ có một cách diễn giải duy nhất
- **Cần thiết (Necessary)**: Đóng góp vào mục đích của hệ thống
- **Khả thi (Feasible)**: Có thể được triển khai trong các ràng buộc
- **Có thể truy vết (Traceable)**: Được liên kết với nhu cầu của người dùng và các yếu tố thiết
