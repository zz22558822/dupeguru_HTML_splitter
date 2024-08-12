# dupeguru HTML splitter
## dupeguru HTML報告分割器

![dupeguru HTML splitter cover](https://github.com/zz22558822/dupeguru_HTML_splitter/blob/main/img/dupeguru_HTML_splitter.png)

---
## 介紹:
使用 [dupeguru](https://github.com/arsenetar/dupeguru "dupeguru Github") 完成後產出HTML報告，  
但超大量的資料導致瀏覽器無法正常瀏覽，  
因此需要做切割後才可正常瀏覽。  


## 使用方法:
1. 使用 dupeguru_HTML_splitter.exe  
2. 輸入要分割的檔案路徑 (或將檔案拖曳至exe啟動)  
3. 輸入分割行數 (建議預設30000)  
4. 等待運行完成後即可查看  

## 檔案結構
File/
├── output/
│&nbsp;&nbsp;&nbsp;&nbsp;└── File name/
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── export_part1...
├── dupeguru_HTML_splitter.exe
└── header.txt

output/ → 資料分割後的存放位置  
dupeguru_HTML_splitter.exe → 主程序  
header.txt → 填充HTML用(未來更新版面調整可僅改此部分)  

---

## Releases 有打包完成的版本(建議使用)
