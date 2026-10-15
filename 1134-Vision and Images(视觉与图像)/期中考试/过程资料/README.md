# 过程资料说明（期中考试资料制备过程）

本文件夹保留了 2026-10-09 凌晨制备期中考试参考资料过程中的全部中间产物，供后续进一步分析。

## 目录结构

- `转换与提取/` —— 从 PPTX 到 PDF 再到文本的全部中间文件
  - `*.pdf`（17 个）—— WPS 演示组件（KWPP.Application COM）把全部英文 PPTX 转出的 PDF，与 PPT 页数一一对应
  - `chunks/` —— pypdf 按 8 页切分的分块 PDF（为绕过 u1-OCR 大文件解析失败）
  - `parts/`、`parts2/` —— 分块 OCR 的输出 MD（parts 有 49/69 块成功；parts2 仅 2 块）
  - `pptx_text/` —— python-pptx 提取的各 lecture 文本结构（公式为空缺，用于定位公式页）
  - `tiles/` —— 12 张公式页拼图（每张 3-4 页幻灯片），用于图片转录核对公式
  - `*.ps1`、`*.sh`、`*.py` —— 各步骤脚本（WPS 转换、切分、OCR 流水线、公式注入）
  - `probe/`、`tmp_chunk*/` —— OCR 服务探活与临时目录
- `PyMuPDF版本备份/` —— 7 个 lecture 的 PyMuPDF 提取 + 人工公式补全版（正文与 OCR 版等价、公式为人工核对 LaTeX 并附中文注记；OCR 版恢复可用时可对照）

## 各 lecture 最终版本的来源

| 文件（期中考试/课件提取MD/） | 提取方式 |
|---|---|
| Tutorial_01/02/03/04/06 | u1-OCR（云知声，完整公式） |
| lec01–lec06, lec13 | u1-OCR 整文件提取（公式完整） |
| lec00, lec07, lec14, lec15, lec16 | PyMuPDF 文本层 + 公式人工核对补全（OCR 服务当时不可用；关键公式页见 tiles/ 拼图核对记录） |

## 经验记录

- 本机无 Microsoft Office，`PowerPoint.Application` COM 由 WPS 顶替但接口异常；正确做法：`New-Object -ComObject KWPP.Application` → `Presentations.Open($p, $true, $false, $false)` → `SaveAs($out, 32)`，且每文件独立实例、转换后清理 wpp.exe 进程。
- PS1 脚本含中文路径时必须以 UTF-8 BOM 保存（PowerShell 5.1 默认 ANSI），否则路径乱码报 E_FAIL；用 `$PSScriptRoot` 推导路径可完全规避。
- u1-OCR 对大 PDF 偶发 `status=Failed` 或长时间排队：整文件 ≤50 页成功率尚可，更大文件用 8 页分块；服务积压时段任务可能 10 分钟以上无响应，需探活+重试。
- PPTX 中的公式是 TexPoint 图片方程（非 OMML），python-pptx 与 PDF 文本层均无法提取；可靠方案：PyMuPDF 渲染公式页 PNG → 视觉模型转录 LaTeX → 人工核对注入。
