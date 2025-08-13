---
description: "Mô-đun Azure đã xác minh (AVM) và Terraform"
applyTo: "**/*.terraform, **/*.tf, **/*.tfvars, **/*.tfstate, **/*.tflint.hcl, **/*.tf.json, **/*.tfvars.json"
---

# Mô-đun Azure đã xác minh (AVM) Terraform

## Tổng quan

Mô-đun Azure đã xác minh (AVM) là các mô-đun Terraform và Bicep được xây dựng sẵn, đã được kiểm thử và xác thực theo các phương pháp hay nhất của Azure. Sử dụng các mô-đun này để tạo, cập nhật hoặc xem xét Cơ sở hạ tầng dưới dạng Mã (IaC) của Azure một cách tự tin.

## Hướng dẫn tùy chỉnh cho GitHub Copilot Agents

**QUAN TRỌNG**: Khi GitHub Copilot Agent hoặc GitHub Copilot Coding Agent làm việc trên kho lưu trữ này, các bài kiểm tra đơn vị cục bộ sau đây PHẢI được thực thi để tuân thủ các kiểm tra PR. Việc không chạy các bài kiểm tra này sẽ gây ra lỗi xác thực PR:

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

Các lệnh này phải được chạy trước khi bất kỳ pull request nào được tạo hoặc cập nhật để đảm bảo tuân thủ các tiêu chuẩn của Mô-đun Azure đã xác minh và ngăn ngừa lỗi trong quy trình CI/CD.
Thông tin chi tiết hơn về quy trình AVM có thể được tìm thấy trong [Tài liệu đóng góp cho Mô-đun Azure đã xác minh](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/).

**Việc không chạy các bài kiểm tra này sẽ gây ra lỗi xác thực PR và ngăn chặn việc hợp nhất thành công.**

## Khám phá Mô-đun

### Terraform Registry

- Tìm kiếm "avm" + tên tài nguyên
- Lọc theo thẻ "Partner" để tìm các mô-đun AVM chính thức
- Ví dụ: Tìm kiếm "avm storage account" → lọc theo Partner

### Chỉ mục AVM chính thức

- **Tài nguyên Terraform**: `https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`
- **Mẫu Terraform**: `https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-pattern-modules/`
- **Tài nguyên Bicep**: `https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- **Mẫu Bicep**: `https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-pattern-modules/`

## Cách sử dụng Mô-đun Terraform

### Từ các ví dụ

1.  Sao chép mã ví dụ từ tài liệu của mô-đun
2.  Thay thế `source = "../../"` bằng `source = "Azure/avm-res-{service}-{resource}/azurerm"`
3.  Thêm `version = "~> 1.0"` (sử dụng phiên bản mới nhất có sẵn)
4.  Đặt `enable_telemetry = true`

### Từ đầu

1.  Sao chép Hướng dẫn cung cấp từ tài liệu của mô-đun
2.  Cấu hình các đầu vào bắt buộc và tùy chọn
3.  Ghim phiên bản mô-đun
4.  Bật đo từ xa (telemetry)

### Ví dụ sử dụng

```hcl
module "storage_account" {
  source  = "Azure/avm-res-storage-storageaccount/azurerm"
  version = "~> 0.1"

  enable_telemetry    = true
  location            = "East US"
  name                = "mystorageaccount"
  resource_group_name = "my-rg"

  # Cấu hình bổ sung...
}
```

## Quy ước đặt tên

### Các loại mô-đun

- **Mô-đun tài nguyên**: `Azure/avm-res-{service}-{resource}/azurerm`
  - Ví dụ: `Azure/avm-res-storage-storageaccount/azurerm`
- **Mô-đun mẫu**: `Azure/avm-ptn-{pattern}/azurerm`
  - Ví dụ: `Azure/avm-ptn-aks-enterprise/azurerm`
- **Mô-đun tiện ích**: `Azure/avm-utl-{utility}/azurerm`
  - Ví dụ: `Azure/avm-utl-regions/azurerm`

### Đặt tên dịch vụ

- Sử dụng kiểu kebab-case cho các dịch vụ và tài nguyên
- Tuân theo tên dịch vụ của Azure (ví dụ: `storage-storageaccount`, `network-virtualnetwork`)

## Quản lý phiên bản

### Kiểm tra các phiên bản có sẵn

- Endpoint: `https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`
- Ví dụ: `https://registry.terraform.io/v1/modules/Azure/avm-res-storage-storageaccount/azurerm/versions`

### Các phương pháp hay nhất về ghim phiên bản

- Sử dụng ràng buộc phiên bản bi quan: `version = "~> 1.0"`
- Ghim vào các phiên bản cụ thể cho môi trường sản xuất: `version = "1.2.3"`
- Luôn xem lại nhật ký thay đổi (changelog) trước khi nâng cấp

## Nguồn Mô-đun

### Terraform Registry

- **Mẫu URL**: `https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- **Ví dụ**: `https://registry.terraform.io/modules/Azure/avm-res-storage-storageaccount/azurerm/latest`

### Kho lưu trữ GitHub

- **Mẫu URL**: `https://github.com/Azure/terraform-azurerm-avm-{type}-{service}-{resource}`
- **Ví dụ**:
  - Tài nguyên: `https://github.com/Azure/terraform-azurerm-avm-res-storage-storageaccount`
  - Mẫu: `https://github.com/Azure/terraform-azurerm-avm-ptn-aks-enterprise`

## Các phương pháp phát triển hay nhất

### Sử dụng mô-đun

- ✅ **Luôn luôn** ghim phiên bản mô-đun và nhà cung cấp (provider)
- ✅ **Bắt đầu** với các ví dụ chính thức từ tài liệu của mô-đun
- ✅ **Xem xét** tất cả các đầu vào và đầu ra trước khi triển khai
- ✅ **Bật** đo từ xa: `enable_telemetry = true`
- ✅ **Sử dụng** các mô-đun tiện ích AVM cho các mẫu phổ biến
- ✅ **Tuân theo** các yêu cầu và ràng buộc của nhà cung cấp AzureRM

### Chất lượng mã

- ✅ **Luôn luôn** chạy `terraform fmt` sau khi thực hiện thay đổi
- ✅ **Luôn luôn** chạy `terraform validate` sau khi thực hiện thay đổi
- ✅ **Sử dụng** tên biến và mô tả có ý nghĩa
- ✅ **Thêm** các thẻ (tag) và siêu dữ liệu (metadata) phù hợp
- ✅ **Ghi lại tài liệu** cho các cấu hình phức tạp

### Yêu cầu xác thực

Trước khi tạo hoặc cập nhật bất kỳ pull request nào:

```bash
# Định dạng mã
terraform fmt -recursive

# Xác thực cú pháp
terraform validate

# Xác thực dành riêng cho AVM (BẮT BUỘC)
./avm pre-commit
./avm tflint
./avm pr-check
```

## Tích hợp công cụ

### Sử dụng các công cụ có sẵn

- **Hướng dẫn triển khai**: Sử dụng công cụ `azure_get_deployment_best_practices`
- **Tài liệu dịch vụ**: Sử dụng công cụ `microsoft.docs.mcp` để có hướng dẫn cụ thể về dịch vụ Azure
- **Thông tin Schema**: Sử dụng `azure_get_schema_for_Bicep` cho tài nguyên Bicep

### Tích hợp GitHub Copilot

Khi làm việc với các kho lưu trữ AVM:

1.  Luôn kiểm tra các mô-đun hiện có trước khi tạo tài nguyên mới
2.  Sử dụng các ví dụ chính thức làm điểm khởi đầu
3.  Chạy tất cả các bài kiểm tra xác thực trước khi commit
4.  Ghi lại tài liệu về bất kỳ tùy chỉnh hoặc sai lệch nào so với các ví dụ

## Các mẫu phổ biến

### Mô-đun Nhóm tài nguyên

```hcl
module "resource_group" {
  source  = "Azure/avm-res-resources-resourcegroup/azurerm"
  version = "~> 0.1"

  enable_telemetry = true
  location         = var.location
  name            = var.resource_group_name
}
```

### Mô-đun Mạng ảo

```hcl
module "virtual_network" {
  source  = "Azure/avm-res-network-virtualnetwork/azurerm"
  version = "~> 0.1"

  enable_telemetry    = true
  location            = module.resource_group.location
  name                = var.vnet_name
  resource_group_name = module.resource_group.name
  address_space       = ["10.0.0.0/16"]
}
```

## Khắc phục sự cố

### Các vấn đề thường gặp

1.  **Xung đột phiên bản**: Luôn kiểm tra tính tương thích giữa phiên bản mô-đun và nhà cung cấp
2.  **Thiếu phụ thuộc**: Đảm bảo tất cả các tài nguyên cần thiết được tạo trước
3.  **Lỗi xác thực**: Chạy các công cụ xác thực AVM trước khi commit
4.  **Tài liệu**: Luôn tham khảo tài liệu mô-đun mới nhất

### Nguồn hỗ trợ

- **Tài liệu AVM**: `https://azure.github.io/Azure-Verified-Modules/`
- **Vấn đề trên GitHub**: Báo cáo sự cố trong kho lưu trữ GitHub của mô-đun cụ thể
- **Cộng đồng**: Thảo luận trên GitHub của Azure Terraform Provider

## Danh sách kiểm tra tuân thủ

Trước khi gửi bất kỳ mã nào liên quan đến AVM:

- [ ] Phiên bản mô-đun đã được ghim
- [ ] Đo từ xa đã được bật
- [ ] Mã đã được định dạng (`terraform fmt`)
- [ ] Mã đã được xác thực (`terraform validate`)
- [ ] Kiểm tra pre-commit của AVM đã qua (`./avm pre-commit`)
- [ ] Kiểm tra TFLint đã qua (`./avm tflint`)
- [ ] Kiểm tra PR của AVM đã qua (`./avm pr-check`)
- [ ] Tài liệu đã được cập nhật
- [ ] Các ví dụ đã được kiểm thử và hoạt động
