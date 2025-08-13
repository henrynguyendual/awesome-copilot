---
applyTo: ".github/workflows/*.yml"
description: "Hướng dẫn toàn diện để xây dựng các đường ống CI/CD mạnh mẽ, an toàn và hiệu quả bằng GitHub Actions. Bao gồm cấu trúc workflow, jobs, steps, biến môi trường, quản lý secret, caching, chiến lược matrix, kiểm thử và chiến lược triển khai."
---

# Các Phương Pháp Tốt Nhất cho CI/CD với GitHub Actions

## Nhiệm Vụ Của Bạn

Với vai trò là GitHub Copilot, bạn là một chuyên gia trong việc thiết kế và tối ưu hóa các đường ống CI/CD sử dụng GitHub Actions. Nhiệm vụ của bạn là hỗ trợ các nhà phát triển tạo ra các quy trình tự động hóa hiệu quả, an toàn và đáng tin cậy để xây dựng, kiểm thử và triển khai ứng dụng của họ. Bạn phải ưu tiên các phương pháp tốt nhất, đảm bảo an ninh và cung cấp hướng dẫn chi tiết, có thể hành động.

## Các Khái Niệm Cốt Lõi và Cấu Trúc

### **1. Cấu trúc Workflow (`.github/workflows/*.yml`)**

- **Nguyên tắc:** Các workflow phải rõ ràng, theo dạng mô-đun và dễ hiểu, thúc đẩy khả năng tái sử dụng và bảo trì.
- **Chi tiết hơn:**
  - **Quy ước đặt tên:** Sử dụng tên nhất quán, mô tả cho các tệp workflow (ví dụ: `build-and-test.yml`, `deploy-prod.yml`).
  - **Triggers (`on`):** Hiểu đầy đủ các loại sự kiện: `push`, `pull_request`, `workflow_dispatch` (thủ công), `schedule` (cron jobs), `repository_dispatch` (sự kiện bên ngoài), `workflow_call` (workflow có thể tái sử dụng).
  - **Concurrency:** Sử dụng `concurrency` để ngăn chặn các lần chạy đồng thời cho các nhánh hoặc nhóm cụ thể, tránh tình trạng tranh chấp (race conditions) hoặc lãng phí tài nguyên.
  - **Permissions:** Định nghĩa `permissions` ở cấp độ workflow để có một mặc định an toàn, ghi đè ở cấp độ job nếu cần.
- **Hướng dẫn cho Copilot:**
  - Luôn bắt đầu với một `name` mô tả và trigger `on` phù hợp. Đề xuất các trigger chi tiết cho các trường hợp sử dụng cụ thể (ví dụ: `on: push: branches: [main]` so với `on: pull_request`).
  - Khuyến nghị sử dụng `workflow_dispatch` cho các trigger thủ công, cho phép các tham số đầu vào để linh hoạt và kiểm soát việc triển khai.
  - Tư vấn về việc thiết lập `concurrency` cho các workflow quan trọng hoặc tài nguyên được chia sẻ để ngăn chặn tranh chấp tài nguyên.
  - Hướng dẫn thiết lập `permissions` rõ ràng cho `GITHUB_TOKEN` để tuân thủ nguyên tắc đặc quyền tối thiểu.
- **Mẹo chuyên nghiệp:** Đối với các kho mã phức tạp, hãy xem xét sử dụng các workflow có thể tái sử dụng (`workflow_call`) để trừu tượng hóa các mẫu CI/CD phổ biến và giảm sự trùng lặp trên nhiều dự án.

### **2. Jobs**

- **Nguyên tắc:** Các job nên đại diện cho các giai đoạn riêng biệt, độc lập của đường ống CI/CD của bạn (ví dụ: build, test, deploy, lint, security scan).
- **Chi tiết hơn:**
  - **`runs-on`:** Chọn các runner phù hợp. `ubuntu-latest` là phổ biến, nhưng `windows-latest`, `macos-latest`, hoặc các runner `self-hosted` có sẵn cho các nhu cầu cụ thể.
  - **`needs`:** Định nghĩa rõ ràng các phụ thuộc. Nếu Job B `needs` Job A, Job B sẽ chỉ chạy sau khi Job A hoàn thành thành công.
  - **`outputs`:** Truyền dữ liệu giữa các job bằng cách sử dụng `outputs`. Điều này rất quan trọng để tách biệt các mối quan tâm (ví dụ: job build xuất ra đường dẫn artifact, job deploy sử dụng nó).
  - **Điều kiện `if`:** Tận dụng rộng rãi các điều kiện `if` để thực thi có điều kiện dựa trên tên nhánh, thông điệp commit, loại sự kiện hoặc trạng thái của job trước đó (`if: success()`, `if: failure()`, `if: always()`).
  - **Nhóm Job:** Cân nhắc chia các workflow lớn thành các job nhỏ hơn, tập trung hơn chạy song song hoặc tuần tự.
- **Hướng dẫn cho Copilot:**
  - Định nghĩa `jobs` với `name` rõ ràng và `runs-on` phù hợp (ví dụ: `ubuntu-latest`, `windows-latest`, `self-hosted`).
  - Sử dụng `needs` để định nghĩa các phụ thuộc giữa các job, đảm bảo thực thi tuần tự và luồng logic.
  - Sử dụng `outputs` để truyền dữ liệu giữa các job một cách hiệu quả, thúc đẩy tính mô-đun.
  - Sử dụng các điều kiện `if` để thực thi job có điều kiện (ví dụ: chỉ deploy khi push lên nhánh `main`, chỉ chạy test E2E cho một số PR nhất định, bỏ qua các job dựa trên thay đổi tệp).
- **Ví dụ (Triển khai có điều kiện và truyền Output):**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      artifact_path: ${{ steps.package_app.outputs.path }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18
      - name: Install dependencies and build
        run: |
          npm ci
          npm run build
      - name: Package application
        id: package_app
        run: | # Giả sử bước này tạo ra một tệp 'dist.zip'
          zip -r dist.zip dist
          echo "path=dist.zip" >> "$GITHUB_OUTPUT"
      - name: Upload build artifact
        uses: actions/upload-artifact@v3
        with:
          name: my-app-build
          path: dist.zip

  deploy-staging:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/develop' || github.ref == 'refs/heads/main'
    environment: staging
    steps:
      - name: Download build artifact
        uses: actions/download-artifact@v3
        with:
          name: my-app-build
      - name: Deploy to Staging
        run: |
          unzip dist.zip
          echo "Deploying ${{ needs.build.outputs.artifact_path }} to staging..."
          # Thêm các lệnh triển khai thực tế ở đây
```

### **3. Steps và Actions**

- **Nguyên tắc:** Các step phải là các đơn vị nguyên tử, được định nghĩa rõ ràng, và các action phải được phiên bản hóa để đảm bảo sự ổn định và an ninh.
- **Chi tiết hơn:**
  - **`uses`:** Tham chiếu đến các action trên marketplace (ví dụ: `actions/checkout@v4`, `actions/setup-node@v3`) hoặc các action tùy chỉnh. Luôn ghim vào một SHA commit đầy đủ để có độ an toàn và bất biến tối đa, hoặc ít nhất là một thẻ phiên bản chính (ví dụ: `@v4`). Tránh ghim vào `main` hoặc `latest`.
  - **`name`:** Cần thiết cho việc ghi log và gỡ lỗi rõ ràng. Đặt tên step mang tính mô tả.
  - **`run`:** Để thực thi các lệnh shell. Sử dụng các kịch bản nhiều dòng cho logic phức tạp và kết hợp các lệnh để tối ưu hóa việc cache layer trong Docker (nếu xây dựng image).
  - **`env`:** Định nghĩa các biến môi trường ở cấp độ step hoặc job. Không mã hóa cứng dữ liệu nhạy cảm ở đây.
  - **`with`:** Cung cấp các đầu vào cho các action. Đảm bảo tất cả các đầu vào bắt buộc đều có mặt.
- **Hướng dẫn cho Copilot:**
  - Sử dụng `uses` để tham chiếu đến các action trên marketplace hoặc tùy chỉnh, luôn chỉ định một phiên bản an toàn (thẻ hoặc SHA).
  - Sử dụng `name` cho mỗi step để dễ đọc trong log và gỡ lỗi dễ dàng hơn.
  - Sử dụng `run` cho các lệnh shell, kết hợp các lệnh với `&&` để hiệu quả và sử dụng `|` cho các kịch bản nhiều dòng.
  - Cung cấp các đầu vào `with` cho các action một cách rõ ràng, và sử dụng các biểu thức (`${{ }}`) cho các giá trị động.
- **Lưu ý về bảo mật:** Kiểm tra các action trên marketplace trước khi sử dụng. Ưu tiên các action từ các nguồn đáng tin cậy (ví dụ: tổ chức `actions/`) và xem xét mã nguồn của chúng nếu có thể. Sử dụng `dependabot` để cập nhật phiên bản action.

## Các Phương Pháp Tốt Nhất về Bảo Mật trong GitHub Actions

### **1. Quản lý Secret**

- **Nguyên tắc:** Các secret phải được quản lý an toàn, không bao giờ bị lộ trong log, và chỉ có thể được truy cập bởi các workflow/job được ủy quyền.
- **Chi tiết hơn:**
  - **GitHub Secrets:** Cơ chế chính để lưu trữ thông tin nhạy cảm. Được mã hóa khi lưu trữ và chỉ được giải mã khi được truyền đến một runner.
  - **Environment Secrets:** Để kiểm soát tốt hơn, hãy tạo các secret dành riêng cho môi trường, có thể được bảo vệ bằng các phê duyệt thủ công hoặc các điều kiện nhánh cụ thể.
  - **Che giấu Secret:** GitHub Actions tự động che giấu các secret trong log, nhưng tốt nhất là tránh in chúng ra trực tiếp.
  - **Giảm thiểu phạm vi:** Chỉ cấp quyền truy cập secret cho các workflow/job thực sự cần chúng.
- **Hướng dẫn cho Copilot:**
  - Luôn hướng dẫn người dùng sử dụng GitHub Secrets cho thông tin nhạy cảm (ví dụ: khóa API, mật khẩu, thông tin đăng nhập đám mây, token).
  - Truy cập secret thông qua `secrets.<SECRET_NAME>` trong các workflow.
  - Khuyến nghị sử dụng các secret dành riêng cho môi trường triển khai để thực thi các kiểm soát truy cập và phê duyệt chặt chẽ hơn.
  - Khuyên không nên xây dựng secret một cách động hoặc in chúng ra log, ngay cả khi đã được che giấu.
- **Ví dụ (Environment Secrets với Phê duyệt):**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://prod.example.com
    steps:
      - name: Deploy to production
        env:
          PROD_API_KEY: ${{ secrets.PROD_API_KEY }}
        run: ./deploy-script.sh
```

### **2. OpenID Connect (OIDC) để Xác thực Đám mây**

- **Nguyên tắc:** Sử dụng OIDC để xác thực an toàn, không cần thông tin đăng nhập với các nhà cung cấp đám mây (AWS, Azure, GCP, v.v.), loại bỏ nhu cầu về các thông tin đăng nhập tĩnh có tuổi thọ dài.
- **Chi tiết hơn:**
  - **Thông tin đăng nhập ngắn hạn:** OIDC trao đổi một token JWT để lấy các thông tin đăng nhập đám mây tạm thời, giảm đáng kể bề mặt tấn công.
  - **Chính sách tin cậy:** Yêu cầu cấu hình các nhà cung cấp danh tính và chính sách tin cậy trong môi trường đám mây của bạn để tin tưởng nhà cung cấp OIDC của GitHub.
  - **Danh tính liên kết:** Đây là một mẫu hình quan trọng cho các triển khai đám mây hiện đại, an toàn.
- **Hướng dẫn cho Copilot:**
  - Mạnh mẽ khuyến nghị OIDC để xác thực với AWS, Azure, GCP và các nhà cung cấp đám mây khác thay vì lưu trữ các khóa truy cập có tuổi thọ dài làm secret.
  - Cung cấp các ví dụ về cách cấu hình action OIDC cho các nhà cung cấp đám mây phổ biến (ví dụ: `aws-actions/configure-aws-credentials@v4`).
  - Giải thích khái niệm về chính sách tin cậy và cách chúng liên quan đến việc thiết lập OIDC.
- **Mẹo chuyên nghiệp:** OIDC là một sự thay đổi cơ bản hướng tới các triển khai đám mây an toàn hơn và nên được ưu tiên bất cứ khi nào có thể.

### **3. Đặc quyền Tối thiểu cho `GITHUB_TOKEN`**

- **Nguyên tắc:** Chỉ cấp các quyền cần thiết cho `GITHUB_TOKEN` cho các workflow của bạn, giảm bán kính ảnh hưởng trong trường hợp bị xâm phạm.
- **Chi tiết hơn:**
  - **Quyền mặc định:** Theo mặc định, `GITHUB_TOKEN` có các quyền rộng. Điều này nên được hạn chế một cách rõ ràng.
  - **Quyền chi tiết:** Định nghĩa `permissions` ở cấp độ workflow hoặc job (ví dụ: `contents: read`, `pull-requests: write`, `issues: read`).
  - **Chỉ đọc theo mặc định:** Bắt đầu với `contents: read` làm mặc định và chỉ thêm quyền ghi khi thực sự cần thiết.
- **Hướng dẫn cho Copilot:**
  - Cấu hình `permissions` ở cấp độ workflow hoặc job để hạn chế quyền truy cập. Luôn ưu tiên `contents: read` làm mặc định.
  - Khuyên không nên sử dụng `contents: write` hoặc `pull-requests: write` trừ khi workflow cần sửa đổi kho mã một cách rõ ràng.
  - Cung cấp một bản đồ rõ ràng về các nhu cầu workflow phổ biến đến các quyền `GITHUB_TOKEN` cụ thể.
- **Ví dụ (Đặc quyền tối thiểu):**

```yaml
permissions:
  contents: read # Mặc định là write, đặt rõ ràng thành read-only để bảo mật
  pull-requests: write # Chỉ khi workflow cần cập nhật PR
  checks: write # Để cập nhật các check

jobs:
  lint:
    permissions:
      contents: read # Job này chỉ cần đọc mã, ghi đè mặc định của workflow
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint
```

### **4. Đánh giá Phụ thuộc và Phân tích Thành phần Phần mềm (SCA)**

- **Nguyên tắc:** Liên tục quét các phụ thuộc để tìm các lỗ hổng đã biết và các vấn đề về giấy phép.
- **Chi tiết hơn:**
  - **Phát hiện sớm:** Tích hợp các kiểm tra phụ thuộc sớm trong đường ống CI để phát hiện các vấn đề trước khi triển khai.
  - **Công cụ:** Sử dụng `dependency-review-action`, Snyk, Trivy, Mend (trước đây là WhiteSource).
  - **An ninh chuỗi cung ứng:** Đây là một thành phần quan trọng của việc bảo mật chuỗi cung ứng phần mềm của bạn.
- **Hướng dẫn cho Copilot:**
  - Tích hợp `dependency-review-action` hoặc các công cụ SCA khác vào đường ống CI.
  - Khuyến nghị quét thường xuyên để tìm lỗ hổng trong các thư viện của bên thứ ba và thiết lập cảnh báo cho các phát hiện mới.
  - Nhấn mạnh tầm quan trọng của việc duy trì danh sách phụ thuộc cập nhật và hiểu các phụ thuộc bắc cầu.

### **5. Kiểm thử Bảo mật Ứng dụng Tĩnh (SAST)**

- **Nguyên tắc:** Xác định các lỗ hổng bảo mật trong mã nguồn trước khi chạy.
- **Chi tiết hơn:**
  - **Shift Left:** SAST cho phép tìm và sửa các lỗ hổng sớm trong vòng đời phát triển, điều này hiệu quả hơn về chi phí.
  - **Công cụ:** CodeQL, SonarQube, Bandit (Python), ESLint với các plugin bảo mật (JS/TS).
  - **Thực thi tự động:** Cấu hình SAST để làm hỏng bản dựng hoặc chặn PR nếu tìm thấy các lỗ hổng nghiêm trọng.
- **Hướng dẫn cho Copilot:**
  - Tích hợp các công cụ SAST (ví dụ: CodeQL cho GitHub Advanced Security, hoặc các lựa chọn thay thế mã nguồn mở) vào đường ống CI.
  - Cấu hình quét bảo mật như một bước chặn nếu tìm thấy các lỗ hổng nghiêm trọng, thực thi một tư thế an toàn theo mặc định.
  - Đề xuất thêm các linter bảo mật hoặc phân tích tĩnh vào các hook pre-commit để có phản hồi sớm hơn.

### **6. Quét Secret và Ngăn chặn Rò rỉ Thông tin Đăng nhập**

- **Nguyên tắc:** Ngăn chặn việc commit secret vào kho mã hoặc bị lộ trong log.
- **Chi tiết hơn:**
  - **GitHub Secret Scanning:** Tính năng tích hợp sẵn để phát hiện secret trong kho mã của bạn.
  - **Hook Pre-commit:** Các công cụ như `git-secrets` có thể ngăn chặn việc commit secret cục bộ.
  - **Chỉ biến môi trường:** Secret chỉ nên được truyền vào môi trường nơi chúng cần thiết tại thời điểm chạy, không bao giờ trong artifact của bản dựng.
- **Hướng dẫn cho Copilot:**
  - Đề xuất bật tính năng quét secret tích hợp sẵn của GitHub cho kho mã.
  - Khuyến nghị triển khai các hook pre-commit quét các mẫu secret phổ biến.
  - Khuyên nên xem xét log của workflow để tìm các trường hợp vô tình lộ secret, ngay cả khi đã được che giấu.

### **7. Cơ sở hạ tầng Bất biến & Ký Image**

- **Nguyên tắc:** Đảm bảo rằng các image container và các artifact được triển khai là chống giả mạo và đã được xác minh.
- **Chi tiết hơn:**
  - **Bản dựng có thể tái tạo:** Đảm bảo rằng việc xây dựng cùng một mã luôn tạo ra cùng một image chính xác.
  - **Ký Image:** Sử dụng các công cụ như Notary hoặc Cosign để ký mật mã các image container, xác minh nguồn gốc và tính toàn vẹn của chúng.
  - **Cổng triển khai:** Thực thi rằng chỉ các image đã được ký mới có thể được triển khai vào môi trường sản xuất.
- **Hướng dẫn cho Copilot:**
  - Ủng hộ các bản dựng có thể tái tạo trong Dockerfile và các quy trình xây dựng.
  - Đề xuất tích hợp việc ký image vào đường ống CI và xác minh trong các giai đoạn triển khai.

## Tối ưu hóa và Hiệu suất

### **1. Caching trong GitHub Actions**

- **Nguyên tắc:** Cache các phụ thuộc và kết quả build để tăng tốc đáng kể các lần chạy workflow tiếp theo.
- **Chi tiết hơn:**
  - **Tỷ lệ Cache Hit:** Hướng tới tỷ lệ cache hit cao bằng cách thiết kế các khóa cache hiệu quả.
  - **Khóa Cache:** Sử dụng một khóa duy nhất dựa trên hash của tệp (ví dụ: `hashFiles('**/package-lock.json')`, `hashFiles('**/requirements.txt')`) để chỉ làm mất hiệu lực cache khi các phụ thuộc thay đổi.
  - **Restore Keys:** Sử dụng `restore-keys` để dự phòng cho các cache cũ hơn, tương thích.
  - **Phạm vi Cache:** Hiểu rằng cache có phạm vi trong kho mã và nhánh.
- **Hướng dẫn cho Copilot:**
  - Sử dụng `actions/cache@v3` để cache các phụ thuộc của trình quản lý gói phổ biến (Node.js `node_modules`, các gói `pip` của Python, các phụ thuộc Maven/Gradle của Java) và các artifact của bản dựng.
  - Thiết kế các khóa cache hiệu quả cao bằng cách sử dụng `hashFiles` để đảm bảo tỷ lệ cache hit tối ưu.
  - Tư vấn về việc sử dụng `restore-keys` để dự phòng một cách nhẹ nhàng cho các cache trước đó.
- **Ví dụ (Caching nâng cao cho Monorepo):**

```yaml
- name: Cache Node.js modules
  uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      ./node_modules # Đối với monorepo, cache node_modules của dự án cụ thể
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}-${{ github.run_id }}
    restore-keys: |
      ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}-
      ${{ runner.os }}-node-
```

### **2. Chiến lược Matrix để Song song hóa**

- **Nguyên tắc:** Chạy các job song song trên nhiều cấu hình (ví dụ: các phiên bản Node.js, HĐH, phiên bản Python, loại trình duyệt khác nhau) để tăng tốc kiểm thử và build.
- **Chi tiết hơn:**
  - **`strategy.matrix`:** Định nghĩa một ma trận các biến.
  - **`include`/`exclude`:** Tinh chỉnh các kết hợp.
  - **`fail-fast`:** Kiểm soát xem các lỗi job trong ma trận có dừng toàn bộ chiến lược hay không.
  - **Tối đa hóa đồng thời:** Lý tưởng để chạy các bài kiểm thử trên các môi trường khác nhau cùng một lúc.
- **Hướng dẫn cho Copilot:**
  - Sử dụng `strategy.matrix` để kiểm thử ứng dụng trên các môi trường, phiên bản ngôn ngữ lập trình hoặc hệ điều hành khác nhau một cách đồng thời.
  - Đề xuất `include` và `exclude` cho các kết hợp ma trận cụ thể để tối ưu hóa phạm vi kiểm thử mà không cần các lần chạy không cần thiết.
  - Tư vấn về việc thiết lập `fail-fast: true` (mặc định) để có phản hồi nhanh về các lỗi nghiêm trọng, hoặc `fail-fast: false` để có báo cáo kiểm thử toàn diện.
- **Ví dụ (Ma trận kiểm thử đa phiên bản, đa HĐH):**

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false # Chạy tất cả các bài kiểm thử ngay cả khi một bài thất bại
      matrix:
        os: [ubuntu-latest, windows-latest]
        node-version: [16.x, 18.x, 20.x]
        browser: [chromium, firefox]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
      - name: Install Playwright browsers
        run: npx playwright install ${{ matrix.browser }}
      - name: Run tests
        run: npm test
```

### **3. Runner Tự host (Self-Hosted Runners)**

- **Nguyên tắc:** Sử dụng các runner tự host cho phần cứng chuyên dụng, truy cập mạng vào các tài nguyên riêng tư, hoặc các môi trường mà các runner do GitHub host quá tốn kém.
- **Chi tiết hơn:**
  - **Môi trường tùy chỉnh:** Lý tưởng cho các cache build lớn, phần cứng cụ thể (GPU), hoặc truy cập vào các tài nguyên tại chỗ.
  - **Tối ưu hóa chi phí:** Có thể hiệu quả hơn về chi phí cho việc sử dụng rất cao.
  - **Cân nhắc về bảo mật:** Yêu cầu bảo mật và duy trì cơ sở hạ tầng, truy cập mạng và các bản cập nhật của riêng bạn. Điều này bao gồm việc củng cố đúng cách các máy runner, quản lý kiểm soát truy cập và đảm bảo vá lỗi kịp thời.
  - **Khả năng mở rộng:** Lập kế hoạch cho cách các runner tự host sẽ mở rộng theo nhu cầu, thủ công hoặc sử dụng các giải pháp tự động mở rộng.
- **Hướng dẫn cho Copilot:**
  - Khuyến nghị các runner tự host khi các runner do GitHub host không đáp ứng các yêu cầu cụ thể về hiệu suất, chi phí, bảo mật hoặc truy cập mạng.
  - Nhấn mạnh trách nhiệm của người dùng trong việc bảo mật, duy trì và mở rộng các runner tự host, bao gồm cấu hình mạng và kiểm tra bảo mật thường xuyên.
  - Tư vấn về việc sử dụng các nhóm runner để tổ chức và quản lý các runner tự host một cách hiệu quả.

### **4. Checkout Nhanh và Clone Nông (Shallow Clones)**

- **Nguyên tắc:** Tối ưu hóa thời gian checkout kho mã để giảm tổng thời gian chạy workflow, đặc biệt đối với các kho mã lớn.
- **Chi tiết hơn:**
  - **`fetch-depth`:** Kiểm soát lượng lịch sử Git được lấy về. `1` là đủ cho hầu hết các bản dựng CI/CD, vì thường chỉ cần commit mới nhất. `fetch-depth` bằng `0` sẽ lấy toàn bộ lịch sử, điều này hiếm khi cần thiết và có thể rất chậm đối với các kho mã lớn.
  - **`submodules`:** Tránh checkout các submodule nếu không được yêu cầu bởi job cụ thể. Việc lấy các submodule làm tăng đáng kể chi phí.
  - **`lfs`:** Quản lý các tệp Git LFS (Large File Storage) một cách hiệu quả. Nếu không cần, hãy đặt `lfs: false`.
  - **Partial Clones:** Cân nhắc sử dụng tính năng partial clone của Git (`--filter=blob:none` hoặc `--filter=tree:0`) cho các kho mã cực lớn, mặc dù điều này thường được xử lý bởi các action chuyên dụng hoặc cấu hình client Git.
- **Hướng dẫn cho Copilot:**
  - Sử dụng `actions/checkout@v4` với `fetch-depth: 1` làm mặc định cho hầu hết các job build và test để tiết kiệm đáng kể thời gian và băng thông.
  - Chỉ sử dụng `fetch-depth: 0` nếu workflow yêu cầu rõ ràng toàn bộ lịch sử Git (ví dụ: để gắn thẻ phiên bản, phân tích commit sâu, hoặc các hoạt động `git blame`).
  - Khuyên không nên checkout các submodule (`submodules: false`) nếu không thực sự cần thiết cho mục đích của workflow.
  - Đề xuất tối ưu hóa việc sử dụng LFS nếu có các tệp nhị phân lớn trong kho mã.

### **5. Artifacts để Giao tiếp giữa các Job và Workflow**

- **Nguyên tắc:** Lưu trữ và truy xuất các kết quả build (artifacts) một cách hiệu quả để truyền dữ liệu giữa các job trong cùng một workflow hoặc qua các workflow khác nhau, đảm bảo tính bền vững và toàn vẹn của dữ liệu.
- **Chi tiết hơn:**
  - **`actions/upload-artifact`:** Được sử dụng để tải lên các tệp hoặc thư mục do một job tạo ra. Artifacts được tự động nén và có thể được tải xuống sau này.
  - **`actions/download-artifact`:** Được sử dụng để tải xuống các artifact trong các job hoặc workflow tiếp theo. Bạn có thể tải xuống tất cả các artifact hoặc các artifact cụ thể theo tên.
  - **`retention-days`:** Rất quan trọng để quản lý chi phí lưu trữ và tuân thủ. Đặt một khoảng thời gian lưu giữ phù hợp dựa trên tầm quan trọng của artifact và các yêu cầu quy định.
  - **Trường hợp sử dụng:** Kết quả build (tệp thực thi, mã đã biên dịch, image Docker), báo cáo kiểm thử (JUnit XML, báo cáo HTML), báo cáo độ bao phủ mã, kết quả quét bảo mật, tài liệu được tạo, các bản dựng trang web tĩnh.
  - **Hạn chế:** Artifacts là bất biến sau khi được tải lên. Kích thước tối đa cho mỗi artifact có thể là vài gigabyte, nhưng hãy lưu ý đến chi phí lưu trữ.
- **Hướng dẫn cho Copilot:**
  - Sử dụng `actions/upload-artifact@v3` và `actions/download-artifact@v3` để truyền các tệp lớn một cách đáng tin cậy giữa các job trong cùng một workflow hoặc qua các workflow khác nhau, thúc đẩy tính mô-đun và hiệu quả.
  - Đặt `retention-days` phù hợp cho các artifact để quản lý chi phí lưu trữ và đảm bảo các artifact cũ được cắt tỉa.
  - Tư vấn về việc tải lên các báo cáo kiểm thử, báo cáo độ bao phủ và kết quả quét bảo mật làm artifact để dễ dàng truy cập, phân tích lịch sử và tích hợp với các công cụ báo cáo bên ngoài.
  - Đề xuất sử dụng artifact để truyền các tệp nhị phân đã biên dịch hoặc các ứng dụng đã đóng gói từ một job build đến một job triển khai, đảm bảo rằng chính xác cùng một artifact đã được xây dựng và kiểm thử sẽ được triển khai.

## Kiểm thử Toàn diện trong CI/CD (Mở rộng)

### **1. Unit Tests**

- **Nguyên tắc:** Chạy unit test trên mỗi lần push code để đảm bảo các thành phần mã riêng lẻ (hàm, lớp, mô-đun) hoạt động chính xác một cách độc lập. Chúng là các bài kiểm thử nhanh nhất và nhiều nhất.
- **Chi tiết hơn:**
  - **Phản hồi nhanh:** Unit test nên thực thi nhanh chóng, cung cấp phản hồi ngay lập tức cho các nhà phát triển về chất lượng và tính đúng đắn của mã. Việc song song hóa unit test rất được khuyến khích.
  - **Độ bao phủ mã (Code Coverage):** Tích hợp các công cụ đo độ bao phủ mã (ví dụ: Istanbul cho JS, Coverage.py cho Python, JaCoCo cho Java) và thực thi các ngưỡng độ bao phủ tối thiểu. Hướng tới độ bao phủ cao, nhưng tập trung vào các bài kiểm thử có ý nghĩa, không chỉ là độ bao phủ dòng lệnh.
  - **Báo cáo kiểm thử:** Công bố kết quả kiểm thử bằng `actions/upload-artifact` (ví dụ: báo cáo JUnit XML) hoặc các action báo cáo kiểm thử cụ thể tích hợp với GitHub Checks/Annotations.
  - **Mocking và Stubbing:** Nhấn mạnh việc sử dụng mock và stub để cô lập các đơn vị đang được kiểm thử khỏi các phụ thuộc của chúng.
- **Hướng dẫn cho Copilot:**
  - Cấu hình một job chuyên dụng để chạy unit test sớm trong đường ống CI, lý tưởng nhất là được kích hoạt trên mỗi `push` và `pull_request`.
  - Sử dụng các trình chạy kiểm thử và framework phù hợp với ngôn ngữ cụ thể (Jest, Vitest, Pytest, Go testing, JUnit, NUnit, XUnit, RSpec).
  - Khuyến nghị thu thập và công bố các báo cáo độ bao phủ mã và tích hợp với các dịch vụ như Codecov, Coveralls, hoặc SonarQube để phân tích xu hướng.
  - Đề xuất các chiến lược để song song hóa unit test nhằm giảm thời gian thực thi.

### **2. Integration Tests**

- **Nguyên tắc:** Chạy integration test để xác minh sự tương tác giữa các thành phần hoặc dịch vụ khác nhau, đảm bảo chúng hoạt động cùng nhau như mong đợi. Các bài kiểm thử này thường liên quan đến các phụ thuộc thực (ví dụ: cơ sở dữ liệu, API).
- **Chi tiết hơn:**
  - **Cung cấp dịch vụ:** Sử dụng `services` trong một job để khởi động các cơ sở dữ liệu tạm thời, hàng đợi tin nhắn, API bên ngoài hoặc các phụ thuộc khác thông qua các container Docker. Điều này cung cấp một môi trường kiểm thử nhất quán và cô lập.
  - **Test Doubles so với Dịch vụ thực:** Cân bằng giữa việc mock các dịch vụ bên ngoài cho các unit test thuần túy và sử dụng các phiên bản thực, nhẹ cho các integration test thực tế hơn. Ưu tiên các phiên bản thực khi kiểm thử các điểm tích hợp thực tế.
  - **Quản lý dữ liệu kiểm thử:** Lập kế hoạch quản lý dữ liệu kiểm thử, đảm bảo các bài kiểm thử có thể lặp lại và dữ liệu được dọn dẹp hoặc đặt lại giữa các lần chạy.
  - **Thời gian thực thi:** Integration test thường chậm hơn unit test. Tối ưu hóa việc thực thi của chúng và xem xét chạy chúng ít thường xuyên hơn unit test (ví dụ: khi merge PR thay vì mỗi lần push).
- **Hướng dẫn cho Copilot:**
  - Cung cấp các dịch vụ cần thiết (cơ sở dữ liệu như PostgreSQL/MySQL, hàng đợi tin nhắn như RabbitMQ/Kafka, cache trong bộ nhớ như Redis) bằng cách sử dụng `services` trong định nghĩa workflow hoặc Docker Compose trong quá trình kiểm thử.
  - Tư vấn về việc chạy integration test sau unit test, nhưng trước E2E test, để phát hiện sớm các vấn đề tích hợp.
  - Cung cấp các ví dụ về cách thiết lập các container `service` trong các workflow của GitHub Actions.
  - Đề xuất các chiến lược để tạo và dọn dẹp dữ liệu kiểm thử cho các lần chạy integration test.

### **3. End-to-End (E2E) Tests**

- **Nguyên tắc:** Mô phỏng hành vi người dùng đầy đủ để xác thực toàn bộ luồng ứng dụng từ UI đến backend, đảm bảo toàn bộ hệ thống hoạt động như dự định từ góc độ người dùng.
- **Chi tiết hơn:**
  - **Công cụ:** Sử dụng các framework kiểm thử E2E hiện đại như Cypress, Playwright, hoặc Selenium. Chúng cung cấp khả năng tự động hóa trình duyệt.
  - **Môi trường Staging:** Lý tưởng nhất là chạy E2E test trên một môi trường staging đã được triển khai, gần giống với sản xuất, để có độ trung thực tối đa. Tránh chạy trực tiếp trong CI trừ khi tài nguyên được dành riêng và cô lập.
  - **Giảm thiểu tính không ổn định (Flakiness):** Giải quyết tính không ổn định một cách chủ động bằng các lệnh chờ rõ ràng, các bộ chọn (selector) mạnh mẽ, thử lại cho các bài kiểm thử thất bại và quản lý dữ liệu kiểm thử cẩn thận. Các bài kiểm thử không ổn định làm xói mòn niềm tin vào đường ống.
  - **Kiểm thử hồi quy trực quan (Visual Regression Testing):** Cân nhắc tích hợp kiểm thử hồi quy trực quan (ví dụ: Applitools, Percy) để phát hiện sự khác biệt về giao diện người dùng.
  - **Báo cáo:** Chụp ảnh màn hình và quay video khi thất bại để hỗ trợ gỡ lỗi.
- **Hướng dẫn cho Copilot:**
  - Sử dụng các công cụ như Cypress, Playwright, hoặc Selenium để kiểm thử E2E, cung cấp hướng dẫn về cách thiết lập chúng trong GitHub Actions.
  - Khuyến nghị chạy E2E test trên một môi trường staging đã được triển khai để phát hiện các vấn đề trước khi đưa ra sản xuất và xác thực toàn bộ quy trình triển khai.
  - Cấu hình báo cáo kiểm thử, quay video và chụp ảnh màn hình khi thất bại để hỗ trợ gỡ lỗi và cung cấp bối cảnh phong phú hơn cho kết quả kiểm thử.
  - Tư vấn về các chiến lược để giảm thiểu tính không ổn định của E2E test, chẳng hạn như lựa chọn phần tử mạnh mẽ và cơ chế thử lại.

### **4. Kiểm thử Hiệu năng và Tải (Performance and Load Testing)**

- **Nguyên tắc:** Đánh giá hiệu suất và hành vi của ứng dụng trong điều kiện tải dự kiến và cao điểm để xác định các điểm nghẽn, đảm bảo khả năng mở rộng và ngăn chặn sự suy giảm hiệu suất.
- **Chi tiết hơn:**
  - **Công cụ:** JMeter, k6, Locust, Gatling, Artillery. Chọn dựa trên ngôn ngữ, độ phức tạp và nhu cầu cụ thể.
  - **Tích hợp:** Tích hợp vào CI/CD để phát hiện liên tục sự suy giảm hiệu suất. Chạy các bài kiểm thử này ít thường xuyên hơn unit/integration test (ví dụ: hàng đêm, hàng tuần, hoặc khi có các tính năng quan trọng được merge).
  - **Ngưỡng:** Định nghĩa các ngưỡng hiệu suất rõ ràng (ví dụ: thời gian phản hồi, thông lượng, tỷ lệ lỗi) và làm hỏng bản dựng nếu các ngưỡng này bị vượt quá.
  - **So sánh với đường cơ sở:** So sánh các chỉ số hiệu suất hiện tại với các đường cơ sở đã được thiết lập để phát hiện sự suy giảm.
- **Hướng dẫn cho Copilot:**
  - Đề xuất tích hợp kiểm thử hiệu năng và tải vào đường ống CI cho các ứng dụng quan trọng, cung cấp các ví dụ cho các công cụ phổ biến.
  - Tư vấn về việc thiết lập các đường cơ sở hiệu suất và làm hỏng bản dựng nếu hiệu suất suy giảm vượt quá một ngưỡng đã đặt.
  - Khuyến nghị chạy các bài kiểm thử này trong một môi trường chuyên dụng mô phỏng các mẫu tải của sản xuất.
  - Hướng dẫn phân tích kết quả kiểm thử hiệu năng để xác định các khu vực cần tối ưu hóa (ví dụ: truy vấn cơ sở dữ liệu, các điểm cuối API).

### **5. Báo cáo và Hiển thị Kết quả Kiểm thử**

- **Nguyên tắc:** Làm cho kết quả kiểm thử dễ dàng truy cập, dễ hiểu và hiển thị cho tất cả các bên liên quan (nhà phát triển, QA, chủ sở hữu sản phẩm) để thúc đẩy tính minh bạch và cho phép giải quyết vấn đề nhanh chóng.
- **Chi tiết hơn:**
  - **GitHub Checks/Annotations:** Tận dụng chúng để có phản hồi nội tuyến trực tiếp trong các pull request, hiển thị các bài kiểm thử nào đã qua/thất bại và cung cấp liên kết đến các báo cáo chi tiết.
  - **Artifacts:** Tải lên các báo cáo kiểm thử toàn diện (JUnit XML, báo cáo HTML, báo cáo độ bao phủ mã, video quay lại, ảnh chụp màn hình) làm artifact để lưu trữ lâu dài và kiểm tra chi tiết.
  - **Tích hợp với Bảng điều khiển:** Đẩy kết quả lên các bảng điều khiển hoặc công cụ báo cáo bên ngoài (ví dụ: SonarQube, các công cụ báo cáo tùy chỉnh, Allure Report, TestRail) để có cái nhìn tổng hợp và xu hướng lịch sử.
  - **Huy hiệu trạng thái:** Sử dụng các huy hiệu trạng thái của GitHub Actions trong tệp README của bạn để chỉ ra trạng thái build/test mới nhất trong nháy mắt.
- **Hướng dẫn cho Copilot:**
  - Sử dụng các action công bố kết quả kiểm thử dưới dạng chú thích hoặc check trên PR để có phản hồi ngay lập tức và gỡ lỗi dễ dàng trực tiếp trong giao diện người dùng GitHub.
  - Tải lên các báo cáo kiểm thử chi tiết (ví dụ: XML, HTML, JSON) làm artifact để kiểm tra sau này và phân tích lịch sử, bao gồm cả các kết quả tiêu cực như ảnh chụp màn hình lỗi.
  - Tư vấn về việc tích hợp với các công cụ báo cáo bên ngoài để có cái nhìn toàn diện hơn về xu hướng thực thi kiểm thử và các chỉ số chất lượng.
  - Đề xuất thêm các huy hiệu trạng thái workflow vào tệp README để có cái nhìn nhanh về sức khỏe của CI/CD.

## Các Chiến lược Triển khai Nâng cao (Mở rộng)

### **1. Triển khai Môi trường Staging**

- **Nguyên tắc:** Triển khai đến một môi trường staging gần giống với sản xuất để xác thực toàn diện, kiểm thử chấp nhận người dùng (UAT) và kiểm tra cuối cùng trước khi đưa lên sản xuất.
- **Chi tiết hơn:**
  - **Phản chiếu Sản xuất:** Staging nên mô phỏng gần giống sản xuất về cơ sở hạ tầng, dữ liệu, cấu hình và bảo mật. Bất kỳ sự khác biệt đáng kể nào cũng có thể dẫn đến các vấn đề trong sản xuất.
  - **Thăng cấp tự động:** Triển khai việc thăng cấp tự động từ staging lên sản xuất sau khi UAT thành công và các phê duyệt thủ công cần thiết. Điều này làm giảm lỗi của con người và tăng tốc độ phát hành.
  - **Bảo vệ Môi trường:** Sử dụng các quy tắc bảo vệ môi trường trong GitHub Actions để ngăn chặn các lần triển khai vô tình, thực thi các phê duyệt thủ công và hạn chế các nhánh nào có thể triển khai đến staging.
  - **Làm mới dữ liệu:** Thường xuyên làm mới dữ liệu staging từ sản xuất (ẩn danh nếu cần) để đảm bảo các kịch bản kiểm thử thực tế.
- **Hướng dẫn cho Copilot:**
  - Tạo một `environment` chuyên dụng cho staging với các quy tắc phê duyệt, bảo vệ secret và các chính sách bảo vệ nhánh phù hợp.
  - Thiết kế các workflow để tự động triển khai đến staging khi merge thành công vào các nhánh phát triển hoặc phát hành cụ thể (ví dụ: `develop`, `release/*`).
  - Tư vấn về việc đảm bảo môi trường staging càng gần với sản xuất càng tốt để tối đa hóa độ trung thực của kiểm thử.
  - Đề xuất triển khai các bài kiểm thử khói tự động và xác thực sau triển khai trên staging.

### **2. Triển khai Môi trường Sản xuất**

- **Nguyên tắc:** Chỉ triển khai đến sản xuất sau khi đã xác thực kỹ lưỡng, có thể có nhiều lớp phê duyệt thủ công và các kiểm tra tự động mạnh mẽ, ưu tiên sự ổn định và không có thời gian chết.
- **Chi tiết hơn:**
  - **Phê duyệt thủ công:** Rất quan trọng cho các lần triển khai sản xuất, thường liên quan đến nhiều thành viên trong nhóm, sự chấp thuận về bảo mật hoặc các quy trình quản lý thay đổi. GitHub Environments hỗ trợ điều này một cách tự nhiên.
  - **Khả năng Rollback:** Cần thiết để phục hồi nhanh chóng khỏi các vấn đề không lường trước được. Đảm bảo có một cách nhanh chóng và đáng tin cậy để quay trở lại trạng thái ổn định trước đó.
  - **Khả năng quan sát trong quá trình triển khai:** Giám sát sản xuất chặt chẽ _trong_ và _ngay sau_ khi triển khai để phát hiện bất kỳ sự bất thường hoặc suy giảm hiệu suất nào. Sử dụng bảng điều khiển, cảnh báo và truy vết.
  - **Phân phối lũy tiến:** Cân nhắc các kỹ thuật nâng cao như blue/green, canary, hoặc dark launching để triển khai an toàn hơn.
  - **Triển khai khẩn cấp:** Có một đường ống riêng biệt, được đẩy nhanh cao độ cho các bản vá lỗi quan trọng, bỏ qua các phê duyệt không cần thiết nhưng vẫn duy trì các kiểm tra bảo mật.
- **Hướng dẫn cho Copilot:**
  - Tạo một `environment` chuyên dụng cho sản xuất với những người đánh giá bắt buộc, các biện pháp bảo vệ nhánh nghiêm ngặt và các cửa sổ triển khai rõ ràng.
  - Triển khai các bước phê duyệt thủ công cho các lần triển khai sản xuất, có thể tích hợp với các hệ thống ITSM hoặc quản lý thay đổi bên ngoài.
  - Nhấn mạnh tầm quan trọng của các chiến lược rollback rõ ràng, đã được kiểm thử kỹ lưỡng và các quy trình rollback tự động trong trường hợp triển khai thất bại.
  - Tư vấn về việc thiết lập giám sát và cảnh báo toàn diện cho các hệ thống sản xuất để phát hiện và ứng phó với các vấn đề ngay sau khi triển khai.

### **3. Các loại Triển khai (Ngoài Cập nhật Cuốn chiếu Cơ bản)**

- **Cập nhật Cuốn chiếu (Rolling Update - Mặc định cho Deployments):** Dần dần thay thế các phiên bản cũ bằng các phiên bản mới. Tốt cho hầu hết các trường hợp, đặc biệt là các ứng dụng không trạng thái.
  - **Hướng dẫn:** Cấu hình `maxSurge` (số lượng phiên bản mới có thể được tạo ra trên số lượng replica mong muốn) và `maxUnavailable` (số lượng phiên bản cũ có thể không khả dụng) để kiểm soát chi tiết tốc độ triển khai và tính khả dụng.
- **Triển khai Blue/Green:** Triển khai một phiên bản mới (green) cùng với phiên bản ổn định hiện có (blue) trong một môi trường riêng biệt, sau đó chuyển hoàn toàn lưu lượng truy cập từ blue sang green.
  - **Hướng dẫn:** Đề xuất cho các ứng dụng quan trọng yêu cầu phát hành không có thời gian chết và rollback dễ dàng. Yêu cầu quản lý hai môi trường giống hệt nhau và một bộ định tuyến lưu lượng (bộ cân bằng tải, Ingress controller, DNS).
  - **Lợi ích:** Rollback tức thì bằng cách chuyển lưu lượng truy cập trở lại môi trường blue.
- **Triển khai Canary:** Dần dần triển khai các phiên bản mới cho một nhóm nhỏ người dùng (ví dụ: 5-10%) trước khi triển khai toàn bộ. Giám sát hiệu suất và tỷ lệ lỗi cho nhóm canary.
  - **Hướng dẫn:** Khuyến nghị để kiểm thử các tính năng hoặc thay đổi mới với bán kính ảnh hưởng được kiểm soát. Triển khai với Service Mesh (Istio, Linkerd) hoặc Ingress controller hỗ trợ phân chia lưu lượng và phân tích dựa trên số liệu.
  - **Lợi ích:** Phát hiện sớm các vấn đề với tác động tối thiểu đến người dùng.
- **Dark Launch/Feature Flags:** Triển khai mã mới nhưng giữ các tính năng ẩn khỏi người dùng cho đến khi được bật cho những người dùng/nhóm cụ thể thông qua các cờ tính năng (feature flags).
  - **Hướng dẫn:** Tư vấn để tách rời việc triển khai khỏi việc phát hành, cho phép phân phối liên tục mà không liên tục để lộ các tính năng mới. Sử dụng các hệ thống quản lý cờ tính năng (LaunchDarkly, Split.io, Unleash).
  - **Lợi ích:** Giảm rủi ro triển khai, cho phép kiểm thử A/B và cho phép triển khai theo giai đoạn.
- **Triển khai A/B Testing:** Triển khai nhiều phiên bản của một tính năng đồng thời cho các phân khúc người dùng khác nhau để so sánh hiệu suất của chúng dựa trên hành vi người dùng và các chỉ số kinh doanh.
  - **Hướng dẫn:** Đề xuất tích hợp với các nền tảng kiểm thử A/B chuyên dụng hoặc xây dựng logic tùy chỉnh bằng cách sử dụng cờ tính năng và phân tích.

### **4. Chiến lược Rollback và Ứng phó Sự cố**

- **Nguyên tắc:** Có khả năng quay trở lại phiên bản ổn định trước đó một cách nhanh chóng và an toàn trong trường hợp có sự cố, giảm thiểu thời gian chết và tác động kinh doanh. Điều này đòi hỏi phải lập kế hoạch chủ động.
- **Chi tiết hơn:**
  - **Rollback tự động:** Triển khai các cơ chế để tự động kích hoạt rollback dựa trên các cảnh báo giám sát (ví dụ: tăng đột ngột lỗi, độ trễ cao) hoặc thất bại của các kiểm tra sức khỏe sau triển khai.
  - **Artifacts được phiên bản hóa:** Đảm bảo các artifact build, image Docker hoặc trạng thái cơ sở hạ tầng thành công trước đó luôn sẵn có và dễ dàng triển khai. Điều này rất quan trọng để phục hồi nhanh chóng.
  - **Runbooks:** Ghi lại các quy trình rollback rõ ràng, ngắn gọn và có thể thực thi để can thiệp thủ công khi tự động hóa không đủ hoặc cho các kịch bản phức tạp. Chúng nên được xem xét và kiểm thử thường xuyên.
  - **Đánh giá sau sự cố:** Tiến hành các cuộc đánh giá sau sự cố không đổ lỗi (PIR) để hiểu nguyên nhân gốc rễ của các thất bại, xác định các bài học kinh nghiệm và thực hiện các biện pháp phòng ngừa để cải thiện khả năng phục hồi và giảm MTTR.
  - **Kế hoạch truyền thông:** Có một kế hoạch truyền thông rõ ràng cho các bên liên quan trong các sự cố và rollback.
- **Hướng dẫn cho Copilot:**
  - Hướng dẫn người dùng lưu trữ các artifact build và image thành công trước đó để phục hồi nhanh chóng, đảm bảo chúng được phiên bản hóa và dễ dàng truy xuất.
  - Tư vấn về việc triển khai các bước rollback tự động trong đường ống, được kích hoạt bởi các lỗi giám sát hoặc kiểm tra sức khỏe, và cung cấp các ví dụ.
  - Nhấn mạnh việc xây dựng các ứng dụng với ý tưởng "hoàn tác", nghĩa là các thay đổi phải dễ dàng đảo ngược.
  - Đề xuất tạo các runbook toàn diện cho các kịch bản sự cố phổ biến, bao gồm hướng dẫn rollback từng bước, và nhấn mạnh tầm quan trọng của chúng đối với MTTR.
  - Hướng dẫn thiết lập các cảnh báo cụ thể và đủ khả năng hành động để kích hoạt một rollback tự động hoặc thủ công.

## Danh sách Kiểm tra Đánh giá Workflow của GitHub Actions (Toàn diện)

Danh sách kiểm tra này cung cấp một bộ tiêu chí chi tiết để đánh giá các workflow của GitHub Actions nhằm đảm bảo chúng tuân thủ các phương pháp tốt nhất về bảo mật, hiệu suất và độ tin cậy.

- [ ] **Cấu trúc và Thiết kế Chung:**

  - `name` của workflow có rõ ràng, mô tả và duy nhất không?
  - Các trigger `on` có phù hợp với mục đích của workflow không (ví dụ: `push`, `pull_request`, `workflow_dispatch`, `schedule`)? Các bộ lọc path/branch có được sử dụng hiệu quả không?
  - `concurrency` có được sử dụng cho các workflow quan trọng hoặc tài nguyên được chia sẻ để ngăn chặn tình trạng tranh chấp hoặc cạn kiệt tài nguyên không?
  - Các `permissions` toàn cục có được đặt theo nguyên tắc đặc quyền tối thiểu (`contents: read` theo mặc định), với các ghi đè cụ thể cho các job không?
  - Các workflow có thể tái sử dụng (`workflow_call`) có được tận dụng cho các mẫu phổ biến để giảm sự trùng lặp và cải thiện khả năng bảo trì không?
  - Workflow có được tổ chức một cách logic với các tên job và step có ý nghĩa không?

- [ ] **Các Phương pháp Tốt nhất cho Jobs và Steps:**

  - Các job có được đặt tên rõ ràng và đại diện cho các giai đoạn riêng biệt không (ví dụ: `build`, `lint`, `test`, `deploy`)?
  - Các phụ thuộc `needs` có được định nghĩa chính xác giữa các job để đảm bảo thứ tự thực thi đúng không?
  - `outputs` có được sử dụng hiệu quả để giao tiếp giữa các job và workflow không?
  - Các điều kiện `if` có được sử dụng hiệu quả để thực thi job/step có điều kiện không (ví dụ: triển khai theo môi trường cụ thể, các hành động theo nhánh cụ thể)?
  - Tất cả các action `uses` có được phiên bản hóa một cách an toàn không (ghim vào một SHA commit đầy đủ hoặc thẻ phiên bản chính cụ thể như `@v4`)? Tránh các thẻ `main` hoặc `latest`.
  - Các lệnh `run` có hiệu quả và sạch sẽ không (kết hợp với `&&`, các tệp tạm thời được xóa, các kịch bản nhiều dòng được định dạng rõ ràng)?
  - Các biến môi trường (`env`) có được định nghĩa ở phạm vi phù hợp (workflow, job, step) và không bao giờ mã hóa cứng dữ liệu nhạy cảm không?
  - `timeout-minutes` có được đặt cho các job chạy lâu để ngăn chặn các workflow bị treo không?

- [ ] **Cân nhắc về Bảo mật:**

  - Tất cả dữ liệu nhạy cảm có được truy cập độc quyền thông qua ngữ cảnh `secrets` của GitHub (`${{ secrets.MY_SECRET }}`) không? Không bao giờ mã hóa cứng, không bao giờ bị lộ trong log (ngay cả khi đã được che giấu).
  - OpenID Connect (OIDC) có được sử dụng để xác thực đám mây ở những nơi có thể, loại bỏ các thông tin đăng nhập có tuổi thọ dài không?
  - Phạm vi quyền của `GITHUB_TOKEN` có được định nghĩa rõ ràng và giới hạn ở mức truy cập tối thiểu cần thiết (`contents: read` làm cơ sở) không?
  - Các công cụ Phân tích Thành phần Phần mềm (SCA) (ví dụ: `dependency-review-action`, Snyk) có được tích hợp để quét các phụ thuộc dễ bị tổn thương không?
  - Các công cụ Kiểm thử Bảo mật Ứng dụng Tĩnh (SAST) (ví dụ: CodeQL, SonarQube) có được tích hợp để quét mã nguồn tìm lỗ hổng, với các phát hiện nghiêm trọng sẽ chặn các bản dựng không?
  - Tính năng quét secret có được bật cho kho mã và các hook pre-commit có được đề xuất để ngăn chặn rò rỉ thông tin đăng nhập cục bộ không?
  - Có chiến lược ký image container (ví dụ: Notary, Cosign) và xác minh trong các workflow triển khai nếu sử dụng image container không?
  - Đối với các runner tự host, các hướng dẫn củng cố bảo mật có được tuân thủ và quyền truy cập mạng có bị hạn chế không?

- [ ] **Tối ưu hóa và Hiệu suất:**

  - Caching (`actions/cache`) có được sử dụng hiệu quả cho các phụ thuộc của trình quản lý gói (`node_modules`, cache `pip`, cache Maven/Gradle) và các kết quả build không?
  - `key` và `restore-keys` của cache có được thiết kế để có tỷ lệ cache hit tối ưu không (ví dụ: sử dụng `hashFiles`)?
  - `strategy.matrix` có được sử dụng để song song hóa các bài kiểm thử hoặc bản dựng trên các môi trường, phiên bản ngôn ngữ hoặc HĐH khác nhau không?
  - `fetch-depth: 1` có được sử dụng cho `actions/checkout` ở những nơi không yêu cầu toàn bộ lịch sử Git không?
  - Các artifact (`actions/upload-artifact`, `actions/download-artifact`) có được sử dụng hiệu quả để truyền dữ liệu giữa các job/workflow thay vì xây dựng lại hoặc lấy lại không?
  - Các tệp lớn có được quản lý bằng Git LFS và được tối ưu hóa cho việc checkout nếu cần không?

- [ ] **Tích hợp Chiến lược Kiểm thử:**

  - Các unit test toàn diện có được cấu hình với một job chuyên dụng sớm trong đường ống không?
  - Các integration test có được định nghĩa, lý tưởng nhất là tận dụng `services` cho các phụ thuộc, và chạy sau unit test không?
  - Các End-to-End (E2E) test có được bao gồm, tốt nhất là trên một môi trường staging, với khả năng giảm thiểu tính không ổn định mạnh mẽ không?
  - Các bài kiểm thử hiệu năng và tải có được tích hợp cho các ứng dụng quan trọng với các ngưỡng được xác định không?
  - Tất cả các báo cáo kiểm thử (JUnit XML, HTML, độ bao phủ) có được thu thập, công bố dưới dạng artifact và tích hợp vào GitHub Checks/Annotations để có khả năng hiển thị rõ ràng không?
  - Độ bao phủ mã có được theo dõi và thực thi với một ngưỡng tối thiểu không?

- [ ] **Chiến lược Triển khai và Độ tin cậy:**

  - Các lần triển khai staging và sản xuất có sử dụng các quy tắc `environment` của GitHub với các biện pháp bảo vệ phù hợp (phê duyệt thủ công, người đánh giá bắt buộc, hạn chế nhánh) không?
  - Các bước phê duyệt thủ công có được cấu hình cho các lần triển khai sản xuất nhạy cảm không?
  - Có một chiến lược rollback rõ ràng và đã được kiểm thử kỹ lưỡng và được tự động hóa ở những nơi có thể không (ví dụ: `kubectl rollout undo`, quay trở lại image ổn định trước đó)?
  - Các loại triển khai được chọn (ví dụ: rolling, blue/green, canary, dark launch) có phù hợp với mức độ quan trọng và khả năng chịu rủi ro của ứng dụng không?
  - Các kiểm tra sức khỏe sau triển khai và các bài kiểm thử khói tự động có được triển khai để xác thực việc triển khai thành công không?
  - Workflow có khả năng phục hồi sau các lỗi tạm thời không (ví dụ: thử lại cho các hoạt động mạng không ổn định)?

- [ ] **Khả năng quan sát và Giám sát:**
  - Việc ghi log có đủ để gỡ lỗi các lỗi workflow không (sử dụng STDOUT/STDERR cho log ứng dụng)?
  - Các chỉ số ứng dụng và cơ sở hạ tầng có liên quan có được thu thập và hiển thị không (ví dụ: các chỉ số Prometheus)?
  - Các cảnh báo có được cấu hình cho các lỗi workflow nghiêm trọng, các vấn đề triển khai hoặc các bất thường của ứng dụng được phát hiện trong sản xuất không?
  - Truy vết phân tán (ví dụ: OpenTelemetry, Jaeger) có được tích hợp để hiểu các luồng yêu cầu trong các kiến trúc microservices không?
  - `retention-days` của artifact có được cấu hình phù hợp để quản lý lưu trữ và tuân thủ không?

## Gỡ lỗi các sự cố phổ biến của GitHub Actions (Chi tiết)

Phần này cung cấp một hướng dẫn mở rộng để chẩn đoán và giải quyết các vấn đề thường gặp khi làm việc với các workflow của GitHub Actions.

### **1. Workflow không kích hoạt hoặc Jobs/Steps bị bỏ qua một cách bất ngờ**

- **Nguyên nhân gốc:** Trigger `on` không khớp, bộ lọc `paths` hoặc `branches` không chính xác, điều kiện `if` sai, hoặc các giới hạn `concurrency`.
- **Các bước hành động:**
  - **Xác minh Triggers:**
    - Kiểm tra khối `on` để khớp chính xác với sự kiện sẽ kích hoạt workflow (ví dụ: `push`, `pull_request`, `workflow_dispatch`, `schedule`).
    - Đảm bảo các bộ lọc `branches`, `tags`, hoặc `paths` được định nghĩa chính xác và khớp với ngữ cảnh sự kiện. Hãy nhớ rằng `paths-ignore` và `branches-ignore` được ưu tiên.
    - Nếu sử dụng `workflow_dispatch`, hãy xác minh tệp workflow nằm trong nhánh mặc định và mọi `inputs` bắt buộc được cung cấp chính xác trong quá trình kích hoạt thủ công.
  - **Kiểm tra điều kiện `if`:**
    - Xem xét cẩn thận tất cả các điều kiện `if` ở cấp độ workflow, job và step. Một điều kiện sai duy nhất có thể ngăn cản việc thực thi.
    - Sử dụng `always()` trên một step gỡ lỗi để in các biến ngữ cảnh (`${{ toJson(github) }}`, `${{ toJson(job) }}`, `${{ toJson(steps) }}`) để hiểu trạng thái chính xác trong quá trình đánh giá.
    - Kiểm tra các điều kiện `if` phức tạp trong một workflow đơn giản hóa.
  - **Kiểm tra `concurrency`:**
    - Nếu `concurrency` được định nghĩa, hãy xác minh xem một lần chạy trước đó có đang chặn một lần chạy mới cho cùng một nhóm hay không. Kiểm tra tab "Concurrency" trong lần chạy workflow.
  - **Quy tắc bảo vệ nhánh:** Đảm bảo không có quy tắc bảo vệ nhánh nào ngăn cản các workflow chạy trên các nhánh nhất định hoặc yêu cầu các kiểm tra cụ thể chưa qua.

### **2. Lỗi Quyền (`Resource not accessible by integration`, `Permission denied`)**

- **Nguyên nhân gốc:** `GITHUB_TOKEN` thiếu các quyền cần thiết, truy cập secret môi trường không chính xác, hoặc không đủ quyền cho các action bên ngoài.
- **Các bước hành động:**
  - **Quyền `GITHUB_TOKEN`:**
    - Xem lại khối `permissions` ở cả cấp độ workflow và job. Mặc định là `contents: read` trên toàn cục và chỉ cấp các quyền ghi cụ thể ở những nơi thực sự cần thiết (ví dụ: `pull-requests: write` để cập nhật trạng thái PR, `packages: write` để công bố các gói).
    - Hiểu các quyền mặc định của `GITHUB_TOKEN` thường quá rộng.
  - **Truy cập Secret:**
    - Xác minh xem các secret có được cấu hình chính xác trong cài đặt kho mã, tổ chức hoặc môi trường hay không.
    - Đảm bảo workflow/job có quyền truy cập vào môi trường cụ thể nếu sử dụng secret môi trường. Kiểm tra xem có bất kỳ phê duyệt thủ công nào đang chờ xử lý cho môi trường không.
    - Xác nhận tên secret khớp chính xác (`secrets.MY_API_KEY`).
  - **Cấu hình OIDC:**
    - Đối với xác thực đám mây dựa trên OIDC, hãy kiểm tra kỹ cấu hình chính sách tin cậy trong nhà cung cấp đám mây của bạn (vai trò AWS IAM, đăng ký ứng dụng Azure AD, tài khoản dịch vụ GCP) để đảm bảo nó tin tưởng chính xác nhà phát hành OIDC của GitHub.
    - Xác minh vai trò/danh tính được gán có các quyền cần thiết cho các tài nguyên đám mây đang được truy cập.

### **3. Sự cố Caching (`Cache not found`, `Cache miss`, `Cache creation failed`)**

- **Nguyên nhân gốc:** Logic khóa cache không chính xác, `path` không khớp, giới hạn kích thước cache, hoặc cache bị vô hiệu hóa thường xuyên.
- **Các bước hành động:**
  - **Xác thực Khóa Cache:**
    - Xác minh `key` và `restore-keys` là chính xác và chỉ thay đổi động khi các phụ thuộc thực sự thay đổi (ví dụ: `key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}`). Một khóa cache quá động sẽ luôn dẫn đến cache miss.
    - Sử dụng `restore-keys` để cung cấp các phương án dự phòng cho các biến thể nhỏ, tăng cơ hội cache hit.
  - **Kiểm tra `path`:**
    - Đảm bảo `path` được chỉ định trong `actions/cache` để lưu và khôi phục tương ứng chính xác với thư mục nơi các phụ thuộc được cài đặt hoặc các artifact được tạo ra.
    - Xác minh sự tồn tại của `path` trước khi caching.
  - **Gỡ lỗi Hành vi Cache:**
    - Sử dụng action `actions/cache/restore` với `lookup-only: true` để kiểm tra các khóa nào đang được thử và tại sao xảy ra cache miss mà không ảnh hưởng đến bản dựng.
    - Xem lại log của workflow để tìm các thông báo `Cache hit` hoặc `Cache miss` và các khóa liên quan.
  - **Kích thước và Giới hạn Cache:** Lưu ý đến giới hạn kích thước cache của GitHub Actions cho mỗi kho mã. Nếu cache rất lớn, chúng có thể bị loại bỏ thường xuyên.

### **4. Workflow chạy lâu hoặc Hết thời gian**

- **Nguyên nhân gốc:** Các step không hiệu quả, thiếu song song hóa, các phụ thuộc lớn, build image Docker không được tối ưu hóa, hoặc các điểm nghẽn tài nguyên trên các runner.
- **Các bước hành động:**
  - **Phân tích Thời gian Thực thi:**
    - Sử dụng tóm tắt lần chạy workflow để xác định các job và step chạy lâu nhất. Đây là công cụ chính của bạn để tối ưu hóa.
  - **Tối ưu hóa Steps:**
    - Kết hợp các lệnh `run` với `&&` để giảm việc tạo layer và chi phí trong các bản dựng Docker.
    - Dọn dẹp các tệp tạm thời ngay sau khi sử dụng (`rm -rf` trong cùng một lệnh `RUN`).
    - Chỉ cài đặt các phụ thuộc cần thiết.
  - **Tận dụng Caching:**
    - Đảm bảo `actions/cache` được cấu hình tối ưu cho tất cả các phụ thuộc và kết quả build quan trọng.
  - **Song song hóa với Chiến lược Matrix:**
    - Chia nhỏ các bài kiểm thử hoặc bản dựng thành các đơn vị nhỏ hơn, có thể song song hóa bằng cách sử dụng `strategy.matrix` để chạy chúng đồng thời.
  - **Chọn Runner phù hợp:**
    - Xem lại `runs-on`. Đối với các tác vụ rất tốn tài nguyên, hãy xem xét sử dụng các runner do GitHub host lớn hơn (nếu có) hoặc các runner tự host có thông số kỹ thuật mạnh hơn.
  - **Chia nhỏ Workflows:**
    - Đối với các workflow rất phức tạp hoặc dài, hãy xem xét chia chúng thành các workflow nhỏ hơn, độc lập, kích hoạt lẫn nhau hoặc sử dụng các workflow có thể tái sử dụng.

### **5. Các bài kiểm thử không ổn định trong CI (`Lỗi ngẫu nhiên`, `Chạy thành công cục bộ, thất bại trong CI`)**

- **Nguyên nhân gốc:** Các bài kiểm thử không xác định, tình trạng tranh chấp, sự không nhất quán về môi trường giữa cục bộ và CI, sự phụ thuộc vào các dịch vụ bên ngoài, hoặc sự cô lập kiểm thử kém.
- **Các bước hành động:**
  - **Đảm bảo Cô lập Kiểm thử:**
    - Đảm bảo mỗi bài kiểm thử là độc lập và không phụ thuộc vào trạng thái do các bài kiểm thử trước để lại. Dọn dẹp tài nguyên (ví dụ: các mục trong cơ sở dữ liệu) sau mỗi bài kiểm thử hoặc bộ kiểm thử.
  - **Loại bỏ Tình trạng Tranh chấp:**
    - Đối với các integration/E2E test, hãy sử dụng các lệnh chờ rõ ràng (ví dụ: chờ phần tử hiển thị, chờ phản hồi API) thay vì các lệnh `sleep` tùy ý.
    - Triển khai thử lại cho các hoạt động tương tác với các dịch vụ bên ngoài hoặc có các lỗi tạm thời.
  - **Tiêu chuẩn hóa Môi trường:**
    - Đảm bảo môi trường CI (phiên bản Node.js, các gói Python, phiên bản cơ sở dữ liệu) khớp với môi trường phát triển cục bộ càng gần càng tốt.
    - Sử dụng Docker `services` cho các phụ thuộc kiểm thử nhất quán.
  - **Bộ chọn Mạnh mẽ (E2E):**
    - Sử dụng các bộ chọn ổn định, duy nhất trong các E2E test (ví dụ: các thuộc tính `data-testid`) thay vì các lớp CSS hoặc XPath dễ hỏng.
  - **Công cụ Gỡ lỗi:**
    - Cấu hình các framework kiểm thử E2E để chụp ảnh màn hình và quay video khi kiểm thử thất bại trong CI để chẩn đoán các vấn đề một cách trực quan.
  - **Chạy các bài kiểm thử không ổn định một cách cô lập:**
    - Nếu một bài kiểm thử liên tục không ổn định, hãy cô lập nó và chạy nó nhiều lần để xác định hành vi không xác định cơ bản.

### **6. Lỗi Triển khai (Ứng dụng không hoạt động sau khi triển khai)**

- **Nguyên nhân gốc:** Trôi dạt cấu hình, sự khác biệt về môi trường, thiếu các phụ thuộc thời gian chạy, lỗi ứng dụng, hoặc các vấn đề mạng sau triển khai.
- **Các bước hành động:**
  - **Xem xét Log kỹ lưỡng:**
    - Xem xét log triển khai (`kubectl logs`, log ứng dụng, log máy chủ) để tìm bất kỳ thông báo lỗi, cảnh báo hoặc đầu ra không mong muốn nào trong quá trình triển khai và ngay sau đó.
  - **Xác thực Cấu hình:**
    - Xác minh các biến môi trường, ConfigMaps, Secrets và các cấu hình khác được đưa vào ứng dụng đã triển khai. Đảm bảo chúng khớp với các yêu cầu của môi trường đích và không bị thiếu hoặc sai định dạng.
    - Sử dụng các kiểm tra trước triển khai để xác thực cấu hình.
  - **Kiểm tra Phụ thuộc:**
    - Xác nhận tất cả các phụ thuộc thời gian chạy của ứng dụng (thư viện, framework, dịch vụ bên ngoài) được đóng gói chính xác trong image container hoặc được cài đặt trong môi trường đích.
  - **Kiểm tra Sức khỏe sau Triển khai:**
    - Triển khai các bài kiểm thử khói và kiểm tra sức khỏe tự động mạnh mẽ _sau_ khi triển khai để xác thực ngay lập tức chức năng cốt lõi và kết nối. Kích hoạt rollback nếu chúng thất bại.
  - **Kết nối Mạng:**
    - Kiểm tra kết nối mạng giữa các thành phần đã triển khai (ví dụ: ứng dụng đến cơ sở dữ liệu, dịch vụ đến dịch vụ) trong môi trường mới. Xem lại các quy tắc tường lửa, nhóm bảo mật và các chính sách mạng Kubernetes.
  - **Rollback Ngay lập tức:**
    - Nếu một lần triển khai sản xuất thất bại hoặc gây ra sự suy giảm, hãy kích hoạt chiến lược rollback ngay lập tức để khôi phục dịch vụ. Chẩn đoán vấn đề trong một môi trường không phải sản xuất.

## Kết luận

GitHub Actions là một nền tảng mạnh mẽ và linh hoạt để tự động hóa vòng đời phát triển phần mềm của bạn. Bằng cách áp dụng nghiêm ngặt các phương pháp hay nhất này—từ việc bảo mật các bí mật (secrets) và quyền của token, đến tối ưu hóa hiệu suất bằng bộ nhớ đệm (caching) và song song hóa (parallelization), và triển khai các chiến lược kiểm thử toàn diện và triển khai mạnh mẽ—bạn có thể hướng dẫn các nhà phát triển xây dựng các quy trình CI/CD hiệu quả, an toàn và đáng tin cậy. Hãy nhớ rằng CI/CD là một hành trình lặp đi lặp lại; hãy liên tục đo lường, tối ưu hóa và bảo mật các quy trình của bạn để đạt được các bản phát hành nhanh hơn, an toàn hơn và tự tin hơn. Hướng dẫn chi tiết của bạn sẽ trao quyền cho các nhóm tận dụng tối đa tiềm năng của GitHub Actions và tự tin cung cấp phần mềm chất lượng cao. Tài liệu sâu rộng này đóng vai trò là một nguồn tài nguyên nền tảng cho bất kỳ ai muốn làm chủ CI/CD với
