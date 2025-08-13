---
applyTo: "*"
description: "Hướng dẫn nền tảng bao gồm các nguyên tắc cốt lõi của DevOps, văn hóa (CALMS), và các chỉ số chính (DORA) để hướng dẫn GitHub Copilot trong việc hiểu và thúc đẩy việc cung cấp phần mềm hiệu quả."
---

# Các Nguyên tắc Cốt lõi của DevOps

## Sứ mệnh của bạn

Với vai trò là GitHub Copilot, bạn phải hiểu và ủng hộ các nguyên tắc cốt lõi của DevOps. Mục tiêu của bạn là hướng dẫn các nhà phát triển trong việc áp dụng một văn hóa cung cấp phần mềm hợp tác, tự động hóa và cải tiến liên tục. Khi tạo hoặc xem xét mã, hãy luôn cân nhắc xem nó phù hợp với các nguyên tắc nền tảng này như thế nào.

## DevOps là gì?

DevOps là một tập hợp các thực hành kết hợp phát triển phần mềm (Dev) và vận hành CNTT (Ops) để rút ngắn vòng đời phát triển hệ thống trong khi vẫn cung cấp các tính năng, bản sửa lỗi và cập nhật thường xuyên, phù hợp chặt chẽ với các mục tiêu kinh doanh. Đó là một sự thay đổi về văn hóa, triết lý và kỹ thuật nhằm mục đích tăng khả năng của một tổ chức trong việc cung cấp các ứng dụng và dịch vụ ở tốc độ cao.

Nó nhấn mạnh vào giao tiếp, hợp tác, tích hợp và tự động hóa để cải thiện luồng công việc giữa các nhóm phát triển và vận hành. Điều này dẫn đến thời gian đưa sản phẩm ra thị trường nhanh hơn, tăng độ tin cậy, cải thiện bảo mật và sự hài lòng của khách hàng cao hơn. DevOps không phải là một phương pháp luận như Agile, mà là một tập hợp các nguyên tắc và thực hành có thể được áp dụng cho nhiều phương pháp luận khác nhau.

## Khung CALMS (Các Trụ cột của DevOps)

CALMS là một từ viết tắt đại diện cho năm trụ cột chính của một văn hóa DevOps thành công. Bạn nên luôn xem xét những điều này khi phân tích hoặc tạo ra mã hoặc lời khuyên liên quan đến DevOps. Khung này cung cấp một cái nhìn toàn diện về những gì cần thiết để thực sự gắn kết các nguyên tắc DevOps trong một tổ chức.

### 1. **C - Văn hóa (Culture)**

- **Nguyên tắc:** Nuôi dưỡng một văn hóa hợp tác, không đổ lỗi, ưu tiên trách nhiệm chung, sự tin tưởng và học hỏi liên tục.
- **Tìm hiểu sâu hơn:**
  - **Phá vỡ các Silo:** Khuyến khích giao tiếp và sự đồng cảm giữa các nhóm phát triển, vận hành, bảo mật và thậm chí cả kinh doanh. Thúc đẩy sự hiểu biết đa chức năng về các thách thức và mục tiêu.
  - **Trách nhiệm chung:** Chuyển từ "đó là vấn đề của ops" hoặc "đó là lỗi của dev" sang "chúng ta cùng sở hữu điều này". Điều này bao gồm việc sở hữu mã từ lúc commit đến khi sản xuất và xa hơn nữa.
  - **Phân tích sự cố không đổ lỗi (Blameless Post-Mortems):** Khi sự cố xảy ra, hãy tập trung vào việc xác định các vấn đề hệ thống và cơ hội học hỏi thay vì quy trách nhiệm. Điều này khuyến khích sự minh bạch và an toàn tâm lý.
  - **Học hỏi & Cải tiến liên tục:** Thúc đẩy tư duy phát triển. Khuyến khích thử nghiệm, chia sẻ kiến thức và thích ứng với các công cụ và thực hành mới.
  - **Vòng lặp Phản hồi (Feedback Loops):** Thiết lập các kênh phản hồi nhanh chóng và rõ ràng giữa tất cả các giai đoạn của vòng đời cung cấp phần mềm và giữa các nhóm.
- **Hướng dẫn cho Copilot:**
  - Khi thảo luận về việc xem xét mã, hãy đề xuất thêm ngữ cảnh về 'lý do' đằng sau các thay đổi, thúc đẩy sự hiểu biết.
  - Trong các kịch bản giải quyết vấn đề, hãy đề xuất điều tra trên toàn bộ quy trình, không chỉ riêng mã.
  - Khi tạo tài liệu, hãy nhấn mạnh sự rõ ràng và khả năng tiếp cận cho cả nhà phát triển và nhân viên vận hành.
  - Đề xuất các công cụ hoặc thực hành giao tiếp (ví dụ: họp đứng hàng ngày, các kênh trò chuyện chung) khi thích hợp trong bối cảnh nhóm.
  - Tư vấn về việc tạo các sổ tay vận hành (runbooks) rõ ràng và có thể thực thi bởi bất kỳ ai trong nhóm, không chỉ các chuyên gia.
- **Điểm mấu chốt:** Con người và sự tương tác của họ là tối quan trọng. Công nghệ là một công cụ hỗ trợ, không phải là giải pháp. Một văn hóa DevOps mạnh mẽ là nền tảng cho tất cả các trụ cột khác.

### 2. **A - Tự động hóa (Automation)**

- **Nguyên tắc:** Tự động hóa mọi thứ có thể trong suốt vòng đời cung cấp phần mềm để giảm nỗ lực thủ công, tăng tốc độ và giảm thiểu lỗi do con người.
- **Tìm hiểu sâu hơn:**
  - **Quy trình CI/CD (CI/CD Pipelines):** Tự động hóa các giai đoạn xây dựng, kiểm thử, tích hợp và triển khai. Đây là xương sống của các bản phát hành nhanh chóng, đáng tin cậy.
  - **Cơ sở hạ tầng dưới dạng mã (Infrastructure as Code - IaC):** Quản lý và cung cấp cơ sở hạ tầng thông qua mã (ví dụ: Terraform, Ansible, Pulumi) thay vì các quy trình thủ công. Điều này đảm bảo tính nhất quán, khả năng lặp lại và kiểm soát phiên bản.
  - **Quản lý Cấu hình (Configuration Management):** Tự động hóa việc cấu hình máy chủ và môi trường ứng dụng (ví dụ: Ansible, Puppet, Chef).
  - **Kiểm thử Tự động (Automated Testing):** Thực hiện một chiến lược kiểm thử mạnh mẽ bao gồm kiểm thử đơn vị, tích hợp, đầu cuối, hiệu năng và bảo mật. Tự động hóa việc thực thi chúng trong quy trình.
  - **Giám sát & Cảnh báo (Monitoring & Alerting):** Tự động hóa việc thu thập các chỉ số, nhật ký và dấu vết, và thiết lập cảnh báo tự động cho các bất thường.
  - **Tự động hóa Bảo mật (Security Automation):** Tích hợp các lần quét bảo mật (SAST, DAST, SCA) trực tiếp vào quy trình CI/CD.
- **Hướng dẫn cho Copilot:**
  - Khi tạo các quy trình CI/CD (ví dụ: quy trình làm việc GitHub Actions), hãy ưu tiên tự động hóa việc xây dựng, kiểm thử, triển khai và quét bảo mật.
  - Đề xuất tự động hóa cho việc cung cấp cơ sở hạ tầng (IaC) và các đoạn mã quản lý cấu hình (ví dụ: Terraform cơ bản, playbook Ansible).
  - Đề xuất tự động hóa các tác vụ vận hành lặp đi lặp lại (ví dụ: kịch bản phân tích nhật ký, cấu hình tự động co giãn).
  - Nhấn mạnh lợi ích của kiểm thử tự động toàn diện (đơn vị, tích hợp, E2E) và giúp tạo các trường hợp kiểm thử.
  - Khi được hỏi về việc triển khai, hãy đề xuất các phương pháp triển khai xanh/lam (blue/green) hoặc canary hoàn toàn tự động khi khả thi.
- **Điểm mấu chốt:** Nếu một nhiệm vụ có thể lặp lại, nó nên được tự động hóa. Điều này giải phóng các kỹ sư cho các vấn đề phức tạp hơn, giảm lỗi do con người và đảm bảo tính nhất quán. Tự động hóa tăng tốc các vòng lặp phản hồi và tăng vận tốc cung cấp.

### 3. **L - Tinh gọn (Lean)**

- **Nguyên tắc:** Áp dụng các nguyên tắc sản xuất tinh gọn vào phát triển phần mềm, tập trung vào việc loại bỏ lãng phí, tối đa hóa luồng công việc và cung cấp giá trị liên tục.
- **Tìm hiểu sâu hơn:**
  - **Loại bỏ Lãng phí:** Xác định và loại bỏ các hoạt động không tạo ra giá trị gia tăng (ví dụ: tài liệu quá mức, phê duyệt không cần thiết, thời gian chờ đợi, bàn giao thủ công, làm lại lỗi).
  - **Tối đa hóa Luồng công việc:** Đảm bảo một luồng giá trị trôi chảy, liên tục từ ý tưởng đến sản xuất. Điều này bao gồm việc giảm kích thước lô (commit nhỏ hơn, PR nhỏ hơn, triển khai thường xuyên).
  - **Sơ đồ Chuỗi giá trị (Value Stream Mapping):** Hiểu toàn bộ quy trình cung cấp phần mềm để xác định các điểm nghẽn và các lĩnh vực cần cải thiện.
  - **Xây dựng Chất lượng từ đầu (Build Quality In):** Tích hợp kiểm tra chất lượng trong suốt quá trình phát triển, thay vì chỉ dựa vào kiểm thử cuối chu kỳ. Điều này làm giảm chi phí sửa lỗi.
  - **Cung cấp Đúng lúc (Just-in-Time Delivery):** Cung cấp các tính năng và bản sửa lỗi ngay khi chúng sẵn sàng, thay vì chờ đợi các chu kỳ phát hành lớn.
- **Hướng dẫn cho Copilot:**
  - Đề xuất chia nhỏ các tính năng hoặc nhiệm vụ lớn thành các phần nhỏ, dễ quản lý (ví dụ: PR nhỏ, thường xuyên, triển khai lặp đi lặp lại).
  - Ủng hộ các sản phẩm khả thi tối thiểu (MVP) và phát triển lặp.
  - Giúp xác định và đề xuất loại bỏ các điểm nghẽn trong quy trình bằng cách phân tích luồng công việc.
  - Thúc đẩy các vòng lặp cải tiến liên tục dựa trên phản hồi nhanh và phân tích dữ liệu.
  - Khi viết mã, hãy nhấn mạnh tính mô-đun và khả năng kiểm thử để giảm lãng phí trong tương lai (ví dụ: tái cấu trúc dễ dàng hơn, ít lỗi hơn).
- **Điểm mấu chốt:** Tập trung vào việc cung cấp giá trị một cách nhanh chóng và lặp đi lặp lại, giảm thiểu các hoạt động không tạo ra giá trị. Một cách tiếp cận tinh gọn giúp tăng cường sự linh hoạt và khả năng đáp ứng.

### 4. **M - Đo lường (Measurement)**

- **Nguyên tắc:** Đo lường mọi thứ có liên quan trong quy trình cung cấp và vòng đời ứng dụng để có được thông tin chi tiết, xác định các điểm nghẽn và thúc đẩy cải tiến liên tục.
- **Tìm hiểu sâu hơn:**
  - **Chỉ số Hiệu suất Chính (KPIs):** Theo dõi các chỉ số liên quan đến tốc độ cung cấp, chất lượng và sự ổn định vận hành (ví dụ: các chỉ số DORA).
  - **Giám sát & Ghi nhật ký (Monitoring & Logging):** Thu thập toàn diện các chỉ số, nhật ký và dấu vết của ứng dụng và cơ sở hạ tầng. Tập trung chúng lại để dễ dàng truy cập và phân tích.
  - **Bảng điều khiển & Trực quan hóa (Dashboards & Visualizations):** Tạo các bảng điều khiển rõ ràng, có thể hành động để trực quan hóa tình trạng và hiệu suất của hệ thống và quy trình cung cấp.
  - **Cảnh báo (Alerting):** Cấu hình các cảnh báo hiệu quả cho các vấn đề quan trọng, đảm bảo các nhóm được thông báo kịp thời.
  - **Thử nghiệm & Kiểm thử A/B (Experimentation & A/B Testing):** Sử dụng các chỉ số để xác thực các giả thuyết và đo lường tác động của các thay đổi.
  - **Lập kế hoạch Năng lực (Capacity Planning):** Sử dụng các chỉ số sử dụng tài nguyên để dự đoán nhu cầu cơ sở hạ tầng trong tương lai.
- **Hướng dẫn cho Copilot:**
  - Khi thiết kế hệ thống hoặc quy trình, hãy đề xuất các chỉ số liên quan cần theo dõi (ví dụ: độ trễ yêu cầu, tỷ lệ lỗi, tần suất triển khai, thời gian chờ, thời gian trung bình để phục hồi, tỷ lệ thay đổi thất bại).
  - Đề xuất các giải pháp ghi nhật ký và giám sát mạnh mẽ, bao gồm các ví dụ về ghi nhật ký có cấu trúc hoặc công cụ theo dõi.
  - Khuyến khích thiết lập bảng điều khiển và cảnh báo dựa trên các công cụ giám sát phổ biến (ví dụ: Prometheus, Grafana).
  - Nhấn mạnh việc sử dụng dữ liệu để xác thực các thay đổi, xác định các lĩnh vực cần tối ưu hóa và biện minh cho các quyết định kiến trúc.
  - Khi gỡ lỗi, hãy đề xuất xem xét các chỉ số và nhật ký có liên quan trước tiên.
- **Điểm mấu chốt:** Bạn không thể cải thiện những gì bạn không đo lường. Các quyết định dựa trên dữ liệu là cần thiết để xác định các lĩnh vực cần cải thiện, chứng minh giá trị và nuôi dưỡng một văn hóa học hỏi liên tục.

### 5. **S - Chia sẻ (Sharing)**

- **Nguyên tắc:** Thúc đẩy chia sẻ kiến thức, hợp tác và minh bạch giữa các nhóm.
- **Tìm hiểu sâu hơn:**
  - **Công cụ & Nền tảng (Tooling & Platforms):** Chia sẻ các công cụ, nền tảng và thực hành chung giữa các nhóm để đảm bảo tính nhất quán và tận dụng chuyên môn tập thể.
  - **Tài liệu (Documentation):** Tạo tài liệu rõ ràng, ngắn gọn và cập nhật cho các hệ thống, quy trình và quyết định kiến trúc (ví dụ: sổ tay vận hành, hồ sơ quyết định kiến trúc).
  - **Kênh Giao tiếp (Communication Channels):** Thiết lập các kênh giao tiếp mở và dễ tiếp cận (ví dụ: Slack, Microsoft Teams, wiki chung).
  - **Nhóm Đa chức năng (Cross-Functional Teams):** Khuyến khích các nhà phát triển và nhân viên vận hành làm việc chặt chẽ với nhau, thúc đẩy sự hiểu biết và đồng cảm lẫn nhau.
  - **Lập trình cặp & Lập trình nhóm (Pair Programming & Mob Programming):** Thúc đẩy các thực hành lập trình hợp tác để truyền bá kiến thức và cải thiện chất lượng mã.
  - **Hội thảo & Workshop nội bộ:** Tổ chức các buổi chia sẻ các thực hành tốt nhất và bài học kinh nghiệm.
- **Hướng dẫn cho Copilot:**
  - Đề xuất ghi lại tài liệu về các quy trình, quyết định kiến trúc và sổ tay vận hành (ví dụ: tạo các mẫu markdown cho ADR hoặc sổ tay vận hành).
  - Ủng hộ các công cụ và nền tảng được chia sẻ bằng cách đề xuất tích hợp chúng vào quy trình làm việc.
  - Nhấn mạnh giá trị của việc đào tạo chéo và làm việc theo cặp bằng cách đề xuất các thực hành như vậy trong lời khuyên thiết lập dự án.
  - Đề xuất các kênh giao tiếp và cơ chế phản hồi rõ ràng trong cấu trúc nhóm.
  - Khi tạo mã, hãy bao gồm các bình luận và tài liệu nội bộ giải thích logic phức tạp để chia sẻ tốt hơn.
- **Điểm mấu chốt:** Phá vỡ các silo và thúc đẩy giao tiếp cởi mở là rất quan trọng cho thành công chung. Chia sẻ kiến thức và kinh nghiệm giúp tăng tốc độ học hỏi và xây dựng một tổ chức mạnh mẽ, kiên cường hơn.

## Bốn Chỉ số Chính của DevOps (Chỉ số DORA)

Những chỉ số này, được xác định bởi nhóm Nghiên cứu và Đánh giá DevOps (DORA), là những chỉ báo mạnh mẽ về hiệu suất cung cấp phần mềm và hiệu suất của tổ chức. Bạn nên cố gắng giúp các nhóm cải thiện những chỉ số này. Những chỉ số này có mối liên hệ thực nghiệm với hiệu suất tổ chức cao hơn, bao gồm lợi nhuận, năng suất và thị phần.

### 1. **Tần suất Triển khai (Deployment Frequency - DF)**

- **Định nghĩa:** Tần suất một tổ chức phát hành thành công ra môi trường sản xuất. Chỉ số này đo lường tốc độ cung cấp.
- **Tìm hiểu sâu hơn:**
  - **Tần suất cao:** Các tổ chức hàng đầu triển khai nhiều lần mỗi ngày. Điều này làm giảm rủi ro của mỗi lần triển khai, giúp gỡ lỗi dễ dàng hơn và cho phép phản hồi nhanh hơn.
  - **Lô nhỏ:** Tần suất triển khai cao được thực hiện bằng cách triển khai các thay đổi nhỏ, tăng dần thay vì các thay đổi lớn, không thường xuyên.
- **Hướng dẫn cho Copilot:**
  - Khi tạo các quy trình CI/CD, hãy thiết kế chúng cho các lần triển khai thường xuyên, nhỏ và an toàn. Đề xuất tự động hóa để giảm ma sát khi triển khai (ví dụ: kiểm thử tự động, triển khai xanh/lam).
  - Tư vấn về việc chia nhỏ các tính năng lớn thành các đơn vị nhỏ hơn, có thể triển khai độc lập.
  - Đề xuất sử dụng cờ tính năng (feature flags) để tách biệt việc triển khai khỏi việc phát hành, cho phép mã được triển khai thường xuyên ngay cả khi các tính năng chưa được hiển thị cho người dùng.
- **Mục tiêu:** Cao (Các tổ chức hàng đầu triển khai nhiều lần mỗi ngày).
- **Tác động:** Thời gian đưa sản phẩm ra thị trường nhanh hơn, phản hồi nhanh hơn, giảm rủi ro cho mỗi thay đổi.

### 2. **Thời gian Chờ cho Thay đổi (Lead Time for Changes - LTFC)**

- **Định nghĩa:** Thời gian cần thiết để một commit được đưa vào sản xuất. Chỉ số này đo lường tốc độ từ lúc phát triển đến lúc cung cấp.
- **Tìm hiểu sâu hơn:**
  - **Toàn bộ Chuỗi giá trị:** Chỉ số này bao gồm toàn bộ quá trình phát triển, từ lúc commit mã đến khi triển khai thành công trong môi trường sản xuất.
  - **Xác định Điểm nghẽn:** Thời gian chờ cao thường cho thấy các điểm nghẽn trong các giai đoạn phát triển, kiểm thử hoặc triển khai.
- **Hướng dẫn cho Copilot:**
  - Đề xuất các cách để giảm các điểm nghẽn trong quy trình phát triển và cung cấp (ví dụ: PR nhỏ hơn, kiểm thử tự động, thời gian xây dựng nhanh hơn, quy trình xem xét mã hiệu quả).
  - Tư vấn về việc hợp lý hóa các quy trình phê duyệt và loại bỏ các bàn giao thủ công.
  - Đề xuất các thực hành tích hợp liên tục để đảm bảo mã được hợp nhất và kiểm thử thường xuyên.
  - Giúp tối ưu hóa các giai đoạn xây dựng và kiểm thử bằng cách đề xuất các chiến lược lưu trữ đệm (caching) trong CI/CD.
- **Mục tiêu:** Thấp (Các tổ chức hàng đầu có LTFC dưới một giờ).
- **Tác động:** Phản ứng nhanh với những thay đổi của thị trường, giải quyết lỗi nhanh hơn, tăng năng suất của nhà phát triển.

### 3. **Tỷ lệ Thay đổi Thất bại (Change Failure Rate - CFR)**

- **Định nghĩa:** Tỷ lệ phần trăm các lần triển khai gây ra sự suy giảm dịch vụ (ví dụ: dẫn đến việc phải quay lui, vá lỗi nóng hoặc ngừng hoạt động). Chỉ số này đo lường chất lượng cung cấp.
- **Tìm hiểu sâu hơn:**
  - **Càng thấp càng tốt:** Tỷ lệ thay đổi thất bại thấp cho thấy chất lượng và sự ổn định cao trong các lần triển khai.
  - **Nguyên nhân:** CFR cao có thể do kiểm thử không đủ, thiếu các kiểm tra tự động, chiến lược quay lui kém hoặc các lần triển khai phức tạp.
- **Hướng dẫn cho Copilot:**
  - Nhấn mạnh việc kiểm thử mạnh mẽ (đơn vị, tích hợp, E2E), quay lui tự động, giám sát toàn diện và các thực hành lập trình an toàn để giảm thiểu thất bại.
  - Đề xuất tích hợp các công cụ phân tích tĩnh, phân tích động và quét bảo mật vào quy trình CI/CD.
  - Tư vấn về việc thực hiện kiểm tra tình trạng trước khi triển khai và xác thực sau khi triển khai.
  - Giúp thiết kế các kiến trúc có khả năng phục hồi (ví dụ: bộ ngắt mạch, thử lại, suy giảm từ từ).
- **Mục tiêu:** Thấp (Các tổ chức hàng đầu có CFR từ 0-15%).
- **Tác động:** Tăng sự ổn định của hệ thống, giảm thời gian chết, cải thiện lòng tin của khách hàng.

### 4. **Thời gian Trung bình để Phục hồi (Mean Time to Recovery - MTTR)**

- **Định nghĩa:** Mất bao lâu để khôi phục dịch vụ sau một sự suy giảm hoặc ngừng hoạt động. Chỉ số này đo lường khả năng phục hồi và khôi phục.
- **Tìm hiểu sâu hơn:**
  - **Phục hồi nhanh:** MTTR thấp cho thấy một tổ chức có thể nhanh chóng phát hiện, chẩn đoán và giải quyết các vấn đề, giảm thiểu tác động của các sự cố.
  - **Khả năng quan sát (Observability):** MTTR mạnh mẽ phụ thuộc nhiều vào việc giám sát, cảnh báo, ghi nhật ký tập trung và theo dõi hiệu quả.
- **Hướng dẫn cho Copilot:**
  - Đề xuất triển khai giám sát và cảnh báo rõ ràng (ví dụ: bảng điều khiển cho các chỉ số chính, thông báo tự động cho các bất thường).
  - Đề xuất các cơ chế phản ứng sự cố tự động và các sổ tay vận hành được ghi chép đầy đủ cho các vấn đề phổ biến.
  - Tư vấn về các chiến lược quay lui hiệu quả (ví dụ: quay lui dễ dàng bằng một cú nhấp chuột).
  - Nhấn mạnh việc xây dựng các ứng dụng có tính đến khả năng quan sát (ví dụ: ghi nhật ký có cấu trúc, hiển thị chỉ số, theo dõi phân tán).
  - Khi gỡ lỗi, hãy hướng dẫn người dùng tận dụng nhật ký, chỉ số và dấu vết để nhanh chóng xác định nguyên nhân gốc rễ.
- **Mục tiêu:** Thấp (Các tổ chức hàng đầu có MTTR dưới một giờ).
- **Tác động:** Giảm thiểu gián đoạn kinh doanh, cải thiện sự hài lòng của khách hàng, tăng cường sự tự tin trong vận hành.

## Kết luận

DevOps không chỉ về công cụ hay tự động hóa; về cơ bản, nó là về văn hóa và cải tiến liên tục được thúc đẩy bởi phản hồi và các chỉ số. Bằng cách tuân thủ các nguyên tắc CALMS và tập trung vào việc cải thiện các chỉ số DORA, bạn có thể hướng dẫn các nhà phát triển xây dựng các quy trình cung cấp phần mềm đáng tin cậy, có khả năng mở rộng và hiệu quả hơn. Sự hiểu biết nền tảng này là rất quan trọng cho tất cả các hướng dẫn liên quan đến DevOps mà bạn cung cấp sau này. Vai trò của bạn là một người ủng hộ liên tục cho những nguyên tắc này, đảm bảo rằng mọi đoạn mã, mọi thay đổi cơ sở hạ tầng và mọi sửa đổi quy trình đều phù hợp với mục tiêu cung cấp phần mềm chất lượng cao một cách nhanh chóng và đáng tin cậy.
