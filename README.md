# TGbot - WALL YEE

因為目前的小祕書（自家女友）工作負荷太大，所以做個 TGbot 幫他分擔工作。主要功能就是處理一些接案相關的行政工作。基本上是照著自己的需求開發。

## 許願池

> 想要什麼功能就打在這

- 取名小幫手
    - 隨機提供三音節內的英文名子
    - 可選性別
- 筆記本功能
    - syntax:
        ```
        #note title
        contents
        contents
        contents
        ```
    - 指令
        - list_notes
        - add_note
        - delete_note

## 主線功能

基本上是一個接案助理，可以幫你管理案件、提醒時程、記帳。

Command list:

```
status_listall - 顯示目前所有案件階段
status_addcase - 加入新案件
```

### 案件進度一覽

**功能：**

- [ ] 以 emoji 表示案件階段
    | emoji            | status |
    | ---------------- | ------ |
    | :eyes:           | 觀望中 |
    | :briefcase:      | 提案   |
    | :speech_balloon: | 討論中 |
    | :memo:           | 已簽約 |
- [ ] 文字是超連結，連到案件說明頁面（通常是518的網址）
- [ ] 按鍵式更改案件進度。

**範例：**

![](https://i.imgur.com/hOCwYW6.png)

**操作：**

| Command         | Description          |
| --------------- | -------------------- |
| /status_listall | 顯示目前所有案件階段 |
| /status_addcase | 加入新案件           |

- `管理狀態` 按鈕 -> 列出案件清單（僅名稱） -> 選擇案件 -> 選擇狀態

### 進度管理

**功能：**

- [ ] 延後指定專案的所有到期日

### 記帳

