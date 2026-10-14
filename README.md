# 酒吧鼓手十二周复训教材

学过约两年架子鼓、停练七到八年、目标达到酒吧 / Livehouse 能用的水平。

## 打印这一份

`drum-course/酒吧鼓手十二周复训教材.pdf`

- A4，实际大小 100%
- 双面、短边翻转
- 开启「背景图形」
- 左侧装订

详细课表、谱例、打卡和测验都在 PDF 里。打印说明见 `drum-course/打印说明.md`。

若要改课表，编辑 `drum-course/build_textbook.py` 后运行：

```bash
python3 drum-course/build_textbook.py
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=drum-course/酒吧鼓手十二周复训教材.pdf \
  file://$PWD/drum-course/酒吧鼓手十二周复训教材.html
```
