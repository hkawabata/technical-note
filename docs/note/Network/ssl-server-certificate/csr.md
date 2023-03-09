---
title: CSR
title-en: CSR
---

= Certificate Signing Request

# CSR とは

証明書を導入するサーバ上で生成する、証明書の署名要求（Certificate Signing Request）。  
生成した CSR は、SSL サーバ証明書を発行するため、認証局に送信する。

```
-----BEGIN CERTIFICATE REQUEST-----
MIIBpDCCAQ0CAQAwZDELMAkGA1UEBhMCSlAxDjAMBgNVBAgTBVRva3lvMRMwEQYD
...
pj10tZdLyYDNraCNYi6nO87P1l62oFa+tckDi8wmATdsS4T5GJY5DA==
-----END CERTIFICATE REQUEST-----
```

または

```
-----BEGIN NEW CERTIFICATE REQUEST-----
MIIBpDCCAQ0CAQAwZDELMAkGA1UEBhMCSlAxDjAMBgNVBAgTBVRva3lvMRMwEQYD
...
pj10tZdLyYDNraCNYi6nO87P1l62oFa+tckDi8wmATdsS4T5GJY5DA==
-----END NEW CERTIFICATE REQUEST-----
```

のような形式。

# 生成方法

## 必要な情報

| 情報 | 説明 | 例 |
| :-- | :-- | :-- |
| コモンネーム<br>Common Name | サーバ証明書を導入し SSL 暗号化通信を行うサイトの URL（FQDN）を指定。<br>SSL 接続の際にブラウザで指定する URL と一致させる必要がある。  <br>例） https://www.example.com　→ www.example.com | www.example.com |
| 組織<br>Organization | ウェブサイトを運営する組織名 |  |
| 部門名<br>Organizational Unit | 部門・部署名など、任意の識別名称 |  |
| 市区町村郡名<br>Locality | 市区町村郡名 |  |
| 都道府県名<br>State or Province | 都道府県名 |  |
| 国名 | 国コード |  |
|  |  |  |
|  |  |  |

## openssl による生成

秘密鍵作成

```bash
sudo openssl genrsa -out private.key 2048
```

ssl.conf

```
[ req ]
default_bits           = 2048
default_md             = sha256
distinguished_name     = req_distinguished_name
req_extensions         = v3_req
 
[ req_distinguished_name ]
countryName                     = Country Name (2 letter code)
countryName_min                 = 2
countryName_max                 = 2
countryName_default             = JP
stateOrProvinceName             = State or Province Name (full name)
stateOrProvinceName_default     = Tokyo
localityName                    = Locality Name (eg, city)
localityName_default            = Chiyoda-ku
0.organizationName              = Organization Name (eg, company)
0.organizationName_default      = Example Corporation
 
[ v3_req ]
subjectAltName = @alt_names
   
[alt_names]
DNS.1 = <証明書のCommonNameを記載する>
DNS.2 = 2個目があれば連番で記載していく
DNS.3 = 3個目…
```

CSR 作成

```bash
$ openssl req -new -key ./private.key -out ./gmh.csr -config ./ssl.conf

Country Name (2 letter code) [JP]:                      ---> Enter
State or Province Name (full name) [Tokyo]:             ---> Enter
Locality Name (eg, city) [Chiyoda-ku]:                  ---> Enter
Organization Name (eg, company) [Example Corporation]:  ---> Enter
---> alt_namesに記載したドメインのうちの1つを記載
```

