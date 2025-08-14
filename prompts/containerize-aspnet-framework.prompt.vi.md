---
mode: "agent"
tools: ["codebase", "editFiles", "terminalCommand"]
description: "Container hóa một dự án ASP.NET .NET Framework bằng cách tạo các tệp Dockerfile và .dockerfile được tùy chỉnh cho dự án."
---

# Lời nhắc Container hóa ASP.NET .NET Framework

Container hóa dự án ASP.NET (.NET Framework) được chỉ định trong cài đặt container hóa bên dưới, tập trung **chỉ** vào những thay đổi cần thiết để ứng dụng chạy trong một container Docker Windows. Quá trình container hóa nên xem xét tất cả các cài đặt được chỉ định ở đây.

**LƯU Ý:** Đây là một ứng dụng .NET Framework, không phải .NET Core. Quá trình container hóa sẽ khác với quá trình của một ứng dụng .NET Core.

---

## Cài đặt Container hóa

Phần này của lời nhắc chứa các cài đặt và cấu hình cụ thể cần thiết để container hóa ứng dụng ASP.NET (.NET Framework). Trước khi chạy lời nhắc này, hãy đảm bảo rằng các cài đặt đã được điền đầy đủ thông tin cần thiết. Lưu ý rằng trong nhiều trường hợp, chỉ cần một vài cài đặt đầu tiên. Các cài đặt sau có thể để mặc định nếu chúng không áp dụng cho dự án đang được container hóa.

Bất kỳ cài đặt nào không được chỉ định sẽ được đặt thành giá trị mặc định. Các giá trị mặc định được cung cấp trong `[dấu ngoặc vuông]`.

### Thông tin Cơ bản về Dự án

1.  Dự án cần container hóa:

    - `[TênDựÁn (cung cấp đường dẫn đến tệp .csproj)]`

2.  SKU Windows Server sẽ sử dụng:

    - `[Windows Server Core (Mặc định) hoặc Windows Server Full]`

3.  Phiên bản Windows Server sẽ sử dụng:

    - `[2022, 2019, hoặc 2016 (Mặc định 2022)]`

4.  Image cơ sở tùy chỉnh cho giai đoạn build của image Docker ("None" để sử dụng image cơ sở tiêu chuẩn của Microsoft):

    - `[Chỉ định image cơ sở để sử dụng cho giai đoạn build (Mặc định None)]`

5.  Image cơ sở tùy chỉnh cho giai đoạn run của image Docker ("None" để sử dụng image cơ sở tiêu chuẩn của Microsoft):

    - `[Chỉ định image cơ sở để sử dụng cho giai đoạn run (Mặc định None)]`

### Cấu hình Container

1.  Các cổng phải được expose trong image container:

    - Cổng HTTP chính: `[ví dụ, 80]`
    - Các cổng bổ sung: `[Liệt kê bất kỳ cổng bổ sung nào, hoặc "None"]`

2.  Tài khoản người dùng mà container sẽ chạy dưới quyền:

    - `[Tài khoản người dùng, hoặc mặc định là "ContainerUser"]`

3.  Các cài đặt IIS phải được cấu hình trong image container:

    - `[Liệt kê bất kỳ cài đặt IIS cụ thể nào, hoặc "None"]`

### Cấu hình Build

1.  Các bước build tùy chỉnh phải được thực hiện trước khi build image container:

    - `[Liệt kê bất kỳ bước build cụ thể nào, hoặc "None"]`

2.  Các bước build tùy chỉnh phải được thực hiện sau khi build image container:

    - `[Liệt kê bất kỳ bước build cụ thể nào, hoặc "None"]`

### Dependencies (Phần phụ thuộc)

1.  Các assembly .NET cần được đăng ký trong GAC trong image container:

    - `[Tên và phiên bản Assembly, hoặc "None"]`

2.  Các tệp MSI phải được sao chép vào image container và cài đặt:

    - `[Tên và phiên bản MSI, hoặc "None"]`

3.  Các thành phần COM phải được đăng ký trong image container:

    - `[Tên thành phần COM, hoặc "None"]`

### Cấu hình Hệ thống

1.  Các khóa và giá trị registry phải được thêm vào image container:

    - `[Đường dẫn và giá trị Registry, hoặc "None"]`

2.  Các biến môi trường phải được đặt trong image container:

    - `[Tên và giá trị biến, hoặc "Sử dụng mặc định"]`

3.  Các vai trò và tính năng của Windows Server phải được cài đặt trong image container:

    - `[Tên vai trò/tính năng, hoặc "None"]`

### Hệ thống Tệp

1.  Các tệp/thư mục cần được sao chép vào image container:

    - `[Đường dẫn tương đối so với thư mục gốc của dự án, hoặc "None"]`
    - Vị trí đích trong container: `[Đường dẫn trong container, hoặc "Không áp dụng"]`

2.  Các tệp/thư mục cần loại trừ khỏi quá trình container hóa:

    - `[Đường dẫn cần loại trừ, hoặc "None"]`

### Cấu hình .dockerignore

1.  Các mẫu cần đưa vào tệp `.dockerignore` (.dockerignore sẽ có sẵn các giá trị mặc định phổ biến; đây là các mẫu bổ sung):
    - Các mẫu bổ sung: `[Liệt kê bất kỳ mẫu bổ sung nào, hoặc "None"]`

### Cấu hình Health Check

1.  Endpoint kiểm tra tình trạng:

    - `[Đường dẫn URL kiểm tra tình trạng, hoặc "None"]`

2.  Khoảng thời gian và thời gian chờ của health check:

    - `[Giá trị khoảng thời gian và thời gian chờ, hoặc "Sử dụng mặc định"]`

### Hướng dẫn Bổ sung

1.  Các hướng dẫn khác phải được tuân theo để container hóa dự án:

    - `[Yêu cầu cụ thể, hoặc "None"]`

2.  Các vấn đề đã biết cần giải quyết:

    - `[Mô tả bất kỳ vấn đề nào đã biết, hoặc "None"]`

---

## Phạm vi

- ✅ Sửa đổi cấu hình ứng dụng để đảm bảo các trình tạo cấu hình được sử dụng để đọc cài đặt ứng dụng và chuỗi kết nối từ các biến môi trường
- ✅ Tạo và cấu hình Dockerfile cho ứng dụng ASP.NET
- ✅ Chỉ định nhiều giai đoạn trong Dockerfile để build/publish ứng dụng và sao chép đầu ra vào image cuối cùng
- ✅ Cấu hình tương thích nền tảng container Windows (Windows Server Core hoặc Full)
- ✅ Xử lý đúng cách các phần phụ thuộc (assembly GAC, MSI, thành phần COM)
- ❌ Không thiết lập cơ sở hạ tầng (giả định được xử lý riêng)
- ❌ Không thay đổi mã nguồn ngoài những thay đổi cần thiết cho việc container hóa

---

## Quy trình Thực thi

1.  Xem lại các cài đặt container hóa ở trên để hiểu các yêu cầu container hóa
2.  Tạo tệp `progress.md` để theo dõi các thay đổi bằng dấu kiểm
3.  Xác định phiên bản .NET Framework từ tệp .csproj của dự án bằng cách kiểm tra phần tử `TargetFrameworkVersion`
4.  Chọn image container Windows Server phù hợp dựa trên:
    - Phiên bản .NET Framework được phát hiện từ dự án
    - SKU Windows Server được chỉ định trong cài đặt container hóa (Core hoặc Full)
    - Phiên bản Windows Server được chỉ định trong cài đặt container hóa (2016, 2019, hoặc 2022)
    - Các tag của Windows Server Core có thể được tìm thấy tại: [https://github.com/microsoft/dotnet-framework-docker/blob/main/README.aspnet.md\#full-tag-listing](https://github.com/microsoft/dotnet-framework-docker/blob/main/README.aspnet.md#full-tag-listing)
5.  Đảm bảo rằng các gói NuGet cần thiết đã được cài đặt. **KHÔNG** cài đặt chúng nếu chúng bị thiếu. Nếu chúng chưa được cài đặt, người dùng phải cài đặt chúng theo cách thủ công. Nếu chúng chưa được cài đặt, hãy tạm dừng thực thi lời nhắc này và yêu cầu người dùng cài đặt chúng bằng Trình quản lý Gói NuGet của Visual Studio hoặc bảng điều khiển quản lý gói của Visual Studio. Các gói sau đây là bắt buộc:
    - `Microsoft.Configuration.ConfigurationBuilders.Environment`
6.  Sửa đổi tệp `web.config` để thêm phần config builders và cài đặt để đọc cài đặt ứng dụng và chuỗi kết nối từ các biến môi trường:
    - Thêm phần ConfigBuilders trong configSections
    - Thêm phần configBuilders ở cấp gốc
    - Cấu hình EnvironmentConfigBuilder cho cả appSettings và connectionStrings
    - Mẫu ví dụ:
      ```xml
      <configSections>
        <section name="configBuilders" type="System.Configuration.ConfigurationBuildersSection, System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" restartOnExternalChanges="false" requirePermission="false" />
      </configSections>
      <configBuilders>
        <builders>
          <add name="Environment" type="Microsoft.Configuration.ConfigurationBuilders.EnvironmentConfigBuilder, Microsoft.Configuration.ConfigurationBuilders.Environment" />
        </builders>
      </configBuilders>
      <appSettings configBuilders="Environment">
        </appSettings>
      <connectionStrings configBuilders="Environment">
        </connectionStrings>
      ```
7.  Tạo tệp `LogMonitorConfig.json` trong thư mục nơi Dockerfile sẽ được tạo bằng cách sao chép tệp `LogMonitorConfig.json` tham khảo ở cuối lời nhắc này. Nội dung của tệp **KHÔNG ĐƯỢC** sửa đổi và phải khớp chính xác với nội dung tham khảo trừ khi các hướng dẫn trong cài đặt container hóa chỉ định khác.
    - Đặc biệt, đảm bảo mức độ của các vấn đề cần ghi log không bị thay đổi vì việc sử dụng mức `Information` cho các nguồn EventLog sẽ gây ra nhiễu không cần thiết.
8.  Tạo một Dockerfile trong thư mục gốc của dự án để container hóa ứng dụng
    - Dockerfile nên sử dụng nhiều giai đoạn:
      - Giai đoạn build: Sử dụng image Windows Server Core để build ứng dụng
        - Giai đoạn build PHẢI sử dụng image cơ sở `mcr.microsoft.com/dotnet/framework/sdk` trừ khi một image cơ sở tùy chỉnh được chỉ định trong tệp cài đặt
        - Sao chép các tệp sln, csproj, và packages.config trước
        - Sao chép NuGet.config nếu có và cấu hình bất kỳ feed riêng tư nào
        - Khôi phục các gói NuGet
        - Sau đó, sao chép phần còn lại của mã nguồn và build và publish ứng dụng vào C:\\publish bằng MSBuild
      - Giai đoạn cuối: Sử dụng image Windows Server đã chọn để chạy ứng dụng
        - Giai đoạn cuối PHẢI sử dụng image cơ sở `mcr.microsoft.com/dotnet/framework/aspnet` trừ khi một image cơ sở tùy chỉnh được chỉ định trong tệp cài đặt
        - Sao chép tệp `LogMonitorConfig.json` vào một thư mục trong container (ví dụ: C:\\LogMonitor)
        - Tải LogMonitor.exe từ kho lưu trữ của Microsoft về cùng thư mục đó
          - URL chính xác của LogMonitor.exe là: [https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe](https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe)
        - Đặt thư mục làm việc thành C:\\inetpub\\wwwroot
        - Sao chép đầu ra đã publish từ giai đoạn build (trong C:\\publish) vào image cuối cùng
        - Đặt entry point của container để chạy LogMonitor.exe với ServiceMonitor.exe để giám sát dịch vụ IIS
          - `ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]`
    - Hãy chắc chắn xem xét tất cả các yêu cầu trong cài đặt container hóa:
      - SKU và phiên bản Windows Server
      - Các cổng được expose
      - Tài khoản người dùng cho container
      - Cài đặt IIS
      - Đăng ký assembly GAC
      - Cài đặt MSI
      - Đăng ký thành phần COM
      - Khóa registry
      - Biến môi trường
      - Các vai trò và tính năng của Windows
      - Sao chép tệp/thư mục
    - Mô hình hóa Dockerfile theo ví dụ được cung cấp ở cuối lời nhắc này, nhưng đảm bảo nó được tùy chỉnh theo các yêu cầu và cài đặt cụ thể của dự án.
    - **QUAN TRỌNG:** Sử dụng image cơ sở Windows Server Core trừ khi người dùng đã **yêu cầu cụ thể** một image Windows Server đầy đủ trong tệp cài đặt
9.  Tạo một tệp `.dockerignore` trong thư mục gốc của dự án để loại trừ các tệp không cần thiết khỏi image Docker. Tệp `.dockerignore` **PHẢI** bao gồm ít nhất các yếu tố sau cũng như các mẫu bổ sung như được chỉ định trong cài đặt container hóa:
    - packages/
    - bin/
    - obj/
    - .dockerignore
    - Dockerfile
    - .git/
    - .github/
    - .vs/
    - .vscode/
    - \*\*/node_modules/
    - \*.user
    - \*.suo
    - \*\*/.DS_Store
    - \*\*/Thumbs.db
    - Bất kỳ mẫu bổ sung nào được chỉ định trong cài đặt container hóa
10. Cấu hình health checks nếu được chỉ định trong cài đặt:

<!-- end list -->

- Thêm chỉ thị HEALTHCHECK vào Dockerfile nếu endpoint health check được cung cấp

<!-- end list -->

11. Thêm dockerfile vào dự án bằng cách thêm mục sau vào tệp dự án: `<None Include="Dockerfile" />`
12. Đánh dấu các tác vụ đã hoàn thành: [ ] → [✓]
13. Tiếp tục cho đến khi tất cả các tác vụ hoàn thành và quá trình build Docker thành công

---

## Xác minh Build và Runtime

xác nhận rằng quá trình build Docker thành công sau khi Dockerfile được hoàn thành. Sử dụng lệnh sau để build image Docker:

```bash
docker build -t aspnet-app:latest .
```

Nếu quá trình build thất bại, hãy xem lại các thông báo lỗi và thực hiện các điều chỉnh cần thiết cho Dockerfile hoặc cấu hình dự án. Báo cáo thành công/thất bại.

---

## Theo dõi Tiến độ

Duy trì một tệp `progress.md` với cấu trúc sau:

```markdown
# Tiến độ Container hóa

## Phát hiện Môi trường

- [ ] Phát hiện phiên bản .NET Framework (phiên bản: \_\_\_)
- [ ] Lựa chọn SKU Windows Server (SKU: \_\_\_)
- [ ] Lựa chọn phiên bản Windows Server (Phiên bản: \_\_\_)

## Thay đổi Cấu hình

- [ ] Sửa đổi Web.config cho các trình tạo cấu hình
- [ ] Cấu hình nguồn gói NuGet (nếu có)
- [ ] Sao chép LogMonitorConfig.json và điều chỉnh nếu được yêu cầu bởi cài đặt

## Containerization

- [ ] Tạo Dockerfile
- [ ] Tạo tệp .dockerignore
- [ ] Giai đoạn build được tạo với image SDK
- [ ] sln, csproj, packages.config, và (nếu có) NuGet.config được sao chép để khôi phục gói
- [ ] Giai đoạn runtime được tạo với image runtime
- [ ] Cấu hình người dùng không phải root
- [ ] Xử lý phụ thuộc (GAC, MSI, COM, registry, tệp bổ sung, v.v.)
- [ ] Cấu hình health check (nếu có)
- [ ] Triển khai các yêu cầu đặc biệt

## Xác minh

- [ ] Xem lại cài đặt container hóa và đảm bảo rằng tất cả các yêu cầu đều được đáp ứng
- [ ] Build Docker thành công
```

Không tạm dừng để xác nhận giữa các bước. Tiếp tục một cách có phương pháp cho đến khi ứng dụng được container hóa và quá trình build Docker thành công.

**BẠN CHƯA HOÀN THÀNH CHO ĐẾN KHI TẤT CẢ CÁC HỘP KIỂM ĐƯỢC ĐÁNH DẤU\!** Điều này bao gồm việc build image Docker thành công và giải quyết mọi vấn đề phát sinh trong quá trình build.

---

## Tài liệu Tham khảo

### Dockerfile Mẫu

Một Dockerfile mẫu cho ứng dụng ASP.NET (.NET Framework) sử dụng image cơ sở Windows Server Core.

```dockerfile
# escape=`
# Chỉ thị escape thay đổi ký tự thoát từ \ thành `
# Điều này đặc biệt hữu ích trong các Dockerfile của Windows nơi \ là dấu phân cách đường dẫn

# ============================================================
# Giai đoạn 1: Build và publish ứng dụng
# ============================================================

# Image cơ sở - Chọn phiên bản .NET Framework và phiên bản Windows Server Core phù hợp
# Các tag có thể bao gồm:
# - 4.8.1-windowsservercore-ltsc2025 (Windows Server 2025)
# - 4.8-windowsservercore-ltsc2022 (Windows Server 2022)
# - 4.8-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.8-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.2-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.7.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.1-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.6.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 3.5-windowsservercore-ltsc2025 (Windows Server 2025)
# - 3.5-windowsservercore-ltsc2022 (Windows Server 2022)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2019)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2016)
# Sử dụng image .NET Framework SDK để build ứng dụng
FROM mcr.microsoft.com/dotnet/framework/sdk:4.8-windowsservercore-ltsc2022 AS build
ARG BUILD_CONFIGURATION=Release

# Đặt shell mặc định là PowerShell
SHELL ["powershell", "-command"]

WORKDIR /app

# Sao chép tệp solution và project
COPY YourSolution.sln .
COPY YourProject/*.csproj ./YourProject/
COPY YourOtherProject/*.csproj ./YourOtherProject/

# Sao chép các tệp packages.config
COPY YourProject/packages.config ./YourProject/
COPY YourOtherProject/packages.config ./YourOtherProject/

# Khôi phục các gói NuGet
RUN nuget restore YourSolution.sln

# Sao chép mã nguồn
COPY . .

# Thực hiện các bước tiền-build tùy chỉnh ở đây, nếu cần

# Build và publish ứng dụng vào C:\publish
RUN msbuild /p:Configuration=$BUILD_CONFIGURATION `
            /p:WebPublishMethod=FileSystem `
            /p:PublishUrl=C:\publish `
            /p:DeployDefaultTarget=WebPublish

# Thực hiện các bước hậu-build tùy chỉnh ở đây, nếu cần

# ============================================================
# Giai đoạn 2: Image runtime cuối cùng
# ============================================================

# Image cơ sở - Chọn phiên bản .NET Framework và phiên bản Windows Server Core phù hợp
# Các tag có thể bao gồm:
# - 4.8.1-windowsservercore-ltsc2025 (Windows Server 2025)
# - 4.8-windowsservercore-ltsc2022 (Windows Server 2022)
# - 4.8-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.8-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.2-windowsservercore-ltsc2019 (Windows Server 2019)
# - 4.7.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7.1-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.7-windowsservercore-ltsc2016 (Windows Server 2016)
# - 4.6.2-windowsservercore-ltsc2016 (Windows Server 2016)
# - 3.5-windowsservercore-ltsc2025 (Windows Server 2025)
# - 3.5-windowsservercore-ltsc2022 (Windows Server 2022)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2019)
# - 3.5-windowsservercore-ltsc2019 (Windows Server 2016)
# Sử dụng image .NET Framework ASP.NET để chạy ứng dụng
FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2022

# Đặt shell mặc định là PowerShell
SHELL ["powershell", "-command"]

WORKDIR /inetpub/wwwroot

# Sao chép từ giai đoạn build
COPY --from=build /publish .

# Thêm bất kỳ biến môi trường bổ sung nào cần thiết cho ứng dụng của bạn (bỏ ghi chú và sửa đổi nếu cần)
# ENV KEY=VALUE

# Cài đặt các gói MSI (bỏ ghi chú và sửa đổi nếu cần)
# COPY ./msi-installers C:/Installers
# RUN Start-Process -Wait -FilePath 'msiexec.exe' -ArgumentList '/i', 'C:\Installers\your-package.msi', '/quiet', '/norestart'

# Cài đặt các vai trò và tính năng tùy chỉnh của Windows Server (bỏ ghi chú và sửa đổi nếu cần)
# RUN dism /Online /Enable-Feature /FeatureName:YOUR-FEATURE-NAME

# Thêm các tính năng Windows bổ sung (bỏ ghi chú và sửa đổi nếu cần)
# RUN Add-WindowsFeature Some-Windows-Feature; `
#    Add-WindowsFeature Another-Windows-Feature

# Cài đặt các gói MSI nếu cần (bỏ ghi chú và sửa đổi nếu cần)
# COPY ./msi-installers C:/Installers
# RUN Start-Process -Wait -FilePath 'msiexec.exe' -ArgumentList '/i', 'C:\Installers\your-package.msi', '/quiet', '/norestart'

# Đăng ký các assembly trong GAC nếu cần (bỏ ghi chú và sửa đổi nếu cần)
# COPY ./assemblies C:/Assemblies
# RUN C:\Windows\Microsoft.NET\Framework64\v4.0.30319\gacutil -i C:/Assemblies/YourAssembly.dll

# Đăng ký các thành phần COM nếu cần (bỏ ghi chú và sửa đổi nếu cần)
# COPY ./com-components C:/Components
# RUN regsvr32 /s C:/Components/YourComponent.dll

# Thêm các khóa registry nếu cần (bỏ ghi chú và sửa đổi nếu cần)
# RUN New-Item -Path 'HKLM:\Software\YourApp' -Force; `
#     Set-ItemProperty -Path 'HKLM:\Software\YourApp' -Name 'Setting' -Value 'Value'

# Cấu hình cài đặt IIS nếu cần (bỏ ghi chú và sửa đổi nếu cần)
# RUN Import-Module WebAdministration; `
#     Set-ItemProperty 'IIS:\AppPools\DefaultAppPool' -Name somePropertyName -Value 'SomePropertyValue'; `
#     Set-ItemProperty 'IIS:\Sites\Default Web Site' -Name anotherPropertyName -Value 'AnotherPropertyValue'

# Expose các cổng cần thiết - Mặc định, IIS sử dụng cổng 80
EXPOSE 80
# EXPOSE 443  # Bỏ ghi chú nếu sử dụng HTTPS

# Sao chép LogMonitor từ kho lưu trữ microsoft/windows-container-tools
WORKDIR /LogMonitor
RUN curl -fSLo LogMonitor.exe https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe

# Sao chép LogMonitorConfig.json từ các tệp cục bộ
COPY LogMonitorConfig.json .

# Đặt người dùng không phải là quản trị viên
USER ContainerUser

# Ghi đè entry point mặc định của container để tận dụng LogMonitor
ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]
```

### Chuyển thể Ví dụ này

**Lưu ý:** Tùy chỉnh mẫu này dựa trên các yêu cầu cụ thể trong cài đặt container hóa.

Khi chuyển thể ví dụ Dockerfile này:

1.  Thay thế `YourSolution.sln`, `YourProject.csproj`, v.v. bằng tên tệp thực tế của bạn
2.  Điều chỉnh các phiên bản Windows Server và .NET Framework khi cần
3.  Sửa đổi các bước cài đặt phụ thuộc dựa trên yêu cầu của bạn và loại bỏ bất kỳ bước nào không cần thiết
4.  Thêm hoặc bớt các giai đoạn khi cần thiết cho quy trình làm việc cụ thể của bạn

### Ghi chú về Đặt tên Giai đoạn

- Cú pháp `AS ten-giai-doan` đặt tên cho mỗi giai đoạn
- Sử dụng `--from=ten-giai-doan` để sao chép tệp từ một giai đoạn trước đó
- Bạn có thể có nhiều giai đoạn trung gian không được sử dụng trong image cuối cùng

### LogMonitorConfig.json

Tệp LogMonitorConfig.json nên được tạo trong thư mục gốc của dự án. Nó được sử dụng để cấu hình công cụ LogMonitor, công cụ này giám sát log trong container. Nội dung của tệp này phải trông chính xác như thế này để đảm bảo chức năng ghi log phù hợp:

```json
{
  "LogConfig": {
    "sources": [
      {
        "type": "EventLog",
        "startAtOldestRecord": true,
        "eventFormatMultiLine": false,
        "channels": [
          {
            "name": "system",
            "level": "Warning"
          },
          {
            "name": "application",
            "level": "Error"
          }
        ]
      },
      {
        "type": "File",
        "directory": "c:\\inetpub\\logs",
        "filter": "*.log",
        "includeSubdirectories": true,
        "includeFileNames": false
      },
      {
        "type": "ETW",
        "eventFormatMultiLine": false,
        "providers": [
          {
            "providerName": "IIS: WWW Server",
            "providerGuid": "3A2A4E84-4C21-4981-AE10-3FDA0D9B0F83",
            "level": "Information"
          },
          {
            "providerName": "Microsoft-Windows-IIS-Logging",
            "providerGuid": "7E8AD27F-B271-4EA2-A783-A47BDE29143B",
            "level": "Information"
          }
        ]
      }
    ]
  }
}
```
