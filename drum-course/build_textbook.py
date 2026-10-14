#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate a print-ready A4 HTML textbook for the 12-week bar drummer course."""

from pathlib import Path

OUT = Path(__file__).resolve().parent / "酒吧鼓手十二周复训教材.html"


CSS = r"""
:root {
  --ink: #1c1c1c;
  --muted: #4d4d4d;
  --faint: #6e6e6e;
  --line: #cfcfcf;
  --line-strong: #9a9a9a;
  --accent: #7a2430;
  --accent-soft: #f3e6e8;
  --cream: #f6f3ec;
  --navy: #1a2332;
  --paper: #ffffff;
  --hit: #1c1c1c;
}
* { box-sizing: border-box; }
html, body {
  margin: 0;
  padding: 0;
  background: #e8e8e8;
  color: var(--ink);
  font-family: "WenQuanYi Micro Hei", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.page {
  width: 210mm;
  min-height: 297mm;
  margin: 8mm auto;
  background: var(--paper);
  padding: 14mm 15mm 16mm 17mm;
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,.12);
}
.page.cover {
  padding: 0;
  background: var(--navy);
  color: #f4f1ea;
}
.running {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 8pt;
  letter-spacing: .08em;
  color: var(--faint);
  border-bottom: .4pt solid var(--line);
  padding-bottom: 3mm;
  margin-bottom: 6mm;
}
.running b { color: var(--accent); font-weight: 700; letter-spacing: .12em; }
.pgno {
  position: absolute;
  right: 15mm;
  bottom: 8mm;
  font-size: 8.5pt;
  color: var(--faint);
}
h1 { font-size: 22pt; line-height: 1.2; margin: 0 0 4mm; letter-spacing: .04em; }
h2 { font-size: 14.5pt; margin: 0 0 3.5mm; color: var(--navy); letter-spacing: .06em; }
h3 { font-size: 11.5pt; margin: 4mm 0 2mm; color: var(--accent); }
h4 { font-size: 10.5pt; margin: 3mm 0 1.5mm; }
p { margin: 0 0 2.2mm; }
ul, ol { margin: 0 0 3mm 4.5mm; padding: 0; }
li { margin: 0 0 1.1mm; }
.lead { font-size: 11.5pt; color: var(--muted); }
.kicker {
  font-size: 8.5pt;
  letter-spacing: .22em;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 2mm;
}
.columns { display: flex; gap: 6mm; }
.columns > * { flex: 1; }
.box {
  border: .6pt solid var(--line-strong);
  background: var(--cream);
  padding: 3.2mm 3.6mm;
  margin: 0 0 3.5mm;
  page-break-inside: avoid;
}
.box.accent { background: var(--accent-soft); border-color: var(--accent); }
.box h3, .box h4 { margin-top: 0; }
.rule { border: 0; border-top: .6pt solid var(--navy); margin: 4mm 0; }
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9.2pt;
  margin: 0 0 3.5mm;
}
th, td {
  border: .4pt solid var(--line-strong);
  padding: 1.4mm 1.8mm;
  vertical-align: top;
  text-align: left;
}
th { background: var(--navy); color: #f4f1ea; font-weight: 700; }
tr:nth-child(even) td { background: #fafafa; }
td.chk { width: 6mm; text-align: center; font-size: 11pt; }
.mini { font-size: 8.6pt; color: var(--muted); }
.tag {
  display: inline-block;
  border: .4pt solid var(--accent);
  color: var(--accent);
  font-size: 8pt;
  letter-spacing: .08em;
  padding: .4mm 1.6mm;
  margin-right: 1.5mm;
}
.groove-wrap { margin: 0 0 3.5mm; page-break-inside: avoid; }
.groove-title {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 9.5pt;
  font-weight: 700;
  margin-bottom: 1mm;
}
.groove-title span { font-weight: 400; color: var(--muted); font-size: 8.5pt; }
table.groove { table-layout: fixed; margin-bottom: 1mm; }
table.groove th, table.groove td {
  text-align: center;
  padding: 1mm 0;
  font-size: 8pt;
  font-family: "WenQuanYi Micro Hei Mono", "WenQuanYi Micro Hei", monospace;
}
table.groove th:first-child, table.groove td:first-child {
  text-align: left;
  width: 16mm;
  padding-left: 1.4mm;
  font-family: "WenQuanYi Micro Hei", sans-serif;
  font-weight: 700;
}
table.groove thead th { background: #2b3342; }
table.groove td.beat { background: #ececec; font-weight: 700; }
table.groove td.hit { background: #1c1c1c; color: #fff; font-weight: 700; }
table.groove td.ghost { background: #d8d8d8; color: #333; }
table.groove td.open { background: var(--accent); color: #fff; font-weight: 700; }
.caption { font-size: 8.4pt; color: var(--muted); margin: 0 0 3mm; }
.day-card {
  border: .6pt solid var(--navy);
  margin: 0 0 3.2mm;
  page-break-inside: avoid;
}
.day-head {
  background: var(--navy);
  color: #f4f1ea;
  padding: 1.6mm 3mm;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 10pt;
}
.day-head .meta { font-size: 8.5pt; opacity: .85; }
.day-body { padding: 2.4mm 3mm 1.5mm; }
.day-body table { margin-bottom: 1.5mm; }
.day-body table th { background: #3d4758; }
.checkline { color: var(--faint); letter-spacing: .3em; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.legend span { margin-right: 3.5mm; white-space: nowrap; }
.cover-inner {
  height: 297mm;
  padding: 18mm 18mm 16mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cover-top { border-top: 1.2pt solid #c4a35a; border-bottom: 1.2pt solid #c4a35a; padding: 6mm 0; }
.gold { color: #c4a35a; letter-spacing: .28em; font-size: 9.5pt; }
.cover h1 { color: #fff; font-size: 34pt; letter-spacing: .18em; margin: 8mm 0 4mm; }
.cover h1 small { display: block; font-size: 13pt; letter-spacing: .42em; margin-top: 4mm; color: #c4a35a; font-weight: 400; }
.cover-sub { font-size: 13pt; line-height: 1.6; color: #d9d3c5; }
.cover-meta { font-size: 10pt; color: #d9d3c5; line-height: 1.7; }
.cover-foot { display: flex; justify-content: space-between; border-top: .4pt solid #5a6578; padding-top: 4mm; font-size: 8.5pt; letter-spacing: .14em; color: #c4a35a; }
.toc ol { list-style: none; margin: 0; padding: 0; }
.toc li {
  display: flex;
  justify-content: space-between;
  border-bottom: .3pt dotted #bbb;
  margin: 0 0 1.8mm;
  padding-bottom: 1mm;
}
.toc .sec { color: var(--accent); font-weight: 700; margin: 3mm 0 2mm; border-bottom: none; }
.small-ol { margin-left: 5mm; }
.note { font-size: 9pt; color: var(--muted); }
.badge {
  display: inline-block;
  background: var(--navy);
  color: #fff;
  font-size: 8pt;
  padding: .3mm 1.8mm;
  margin-right: 1mm;
}
hr.light { border: 0; border-top: .3pt solid var(--line); margin: 3mm 0; }
.log-row td { height: 8.2mm; }
.log-head td { background: var(--cream); font-weight: 700; }
svg.ornament { width: 42mm; height: 42mm; }

@media print {
  html, body { background: #fff; }
  .page {
    margin: 0;
    box-shadow: none;
    page-break-after: always;
    break-after: page;
  }
  .page:last-child { page-break-after: auto; }
}
@page { size: A4; margin: 0; }
"""


SYMBOLS = {
    ".": ("", ""),
    "x": ("x", "hit"),
    "X": ("X", "open"),
    "o": ("○", "hit"),
    "g": ("g", "ghost"),
    "B": ("●", "hit"),
    "C": ("C", "open"),
    "t": ("t", "hit"),
    "T": ("F", "hit"),
    "r": ("r", "hit"),
    "-": ("–", ""),
}


def _groove_html(name, tempo, rows, beats, beat_every, caption, fill_len):
    head = "".join(f"<th>{b}</th>" for b in beats)
    body = []
    for label, pattern in rows:
        pattern = (pattern + "." * fill_len)[:fill_len]
        cells = []
        for i, ch in enumerate(pattern):
            glyph, cls = SYMBOLS.get(ch, (ch if ch not in " ." else "", "hit" if ch not in " ." else ""))
            extra = " beat" if i % beat_every == 0 else ""
            classes = " ".join(x for x in (cls, extra.strip()) if x)
            cls_attr = f' class="{classes}"' if classes else ""
            cells.append(f"<td{cls_attr}>{glyph}</td>")
        body.append(f"<tr><td>{label}</td>{''.join(cells)}</tr>")
    cap = f'<div class="caption">{caption}</div>' if caption else ""
    return f"""
<div class="groove-wrap">
  <div class="groove-title">{name}<span>{tempo}</span></div>
  <table class="groove">
    <thead><tr><th>声部</th>{head}</tr></thead>
    <tbody>{''.join(body)}</tbody>
  </table>
  {cap}
</div>
"""


def groove_table(name, tempo, rows, caption=""):
    beats = ["1", "e", "&", "a", "2", "e", "&", "a", "3", "e", "&", "a", "4", "e", "&", "a"]
    return _groove_html(name, tempo, rows, beats, 4, caption, 16)


def groove_table_12(name, tempo, rows, caption=""):
    beats = ["1", "&", "a", "2", "&", "a", "3", "&", "a", "4", "&", "a"]
    return _groove_html(name, tempo, rows, beats, 3, caption, 12)


def page(inner, number=None, running_left="酒吧鼓手十二周复训教材", running_right=""):
    num = f'<div class="pgno">{number:03d}</div>' if number else ""
    run = ""
    if running_left is not None:
        run = f"""<div class="running"><span><b>DRUM</b>  REENTRY</span><span>{running_left}</span><span>{running_right}</span></div>"""
    return f'<section class="page">{run}{inner}{num}</section>\n'


def cover():
    return """
<section class="page cover">
  <div class="cover-inner">
    <div>
      <div class="gold">TWELVE-WEEK PRACTICAL COURSE  ·  PRINTABLE WORKBOOK</div>
      <div class="cover-top">
        <div class="gold">适用：学过约两年 · 停练七至八年 · 目标酒吧 / Livehouse</div>
        <h1>酒吧鼓手复训教材<small>十二周课表</small></h1>
        <div class="cover-sub">从找回反弹和时间感开始，练到能撑一场不砸场的 set。</div>
      </div>
    </div>
    <div>
      <svg class="ornament" viewBox="0 0 120 120" fill="none" stroke="#c4a35a" stroke-width="1.6">
        <ellipse cx="60" cy="62" rx="38" ry="14"/>
        <path d="M22 62v18c0 8 17 14 38 14s38-6 38-14V62"/>
        <line x1="22" y1="62" x2="22" y2="46"/>
        <line x1="98" y1="62" x2="98" y2="46"/>
        <ellipse cx="60" cy="46" rx="38" ry="14"/>
        <circle cx="28" cy="28" r="11"/>
        <circle cx="92" cy="24" r="9"/>
        <line x1="28" y1="39" x2="36" y2="50"/>
        <line x1="92" y1="33" x2="86" y2="48"/>
        <line x1="60" y1="20" x2="60" y2="32"/>
      </svg>
    </div>
    <div>
      <div class="cover-meta">
        每日 50–90 分钟　·　每周六练一休　·　节拍器全程开启<br>
        含每日分钟拆解、谱例、曲目、过关标准、打卡表与结业测验
      </div>
      <div class="cover-foot">
        <span>架子鼓 · 酒吧驻场向</span>
        <span>可打印 · 可打卡 · 可跟练</span>
        <span>VOL. 01</span>
      </div>
    </div>
  </div>
</section>
"""


def toc():
    items = [
        ("前言与如何使用", "003"),
        ("十条训练原则 / 装备与护具", "004"),
        ("记谱符号 / 每日时间块", "005"),
        ("手法、踏板与节拍器用法", "006"),
        ("十二周总览", "007"),
        ("第 1 周　把身体喊醒", "008"),
        ("第 2 周　锁死 2 和 4", "012"),
        ("第 3 周　动态与段落意识", "016"),
        ("第 4 周　恢复期验收", "020"),
        ("第 5 周　十六分踩镲", "024"),
        ("第 6 周　Disco 四踩", "028"),
        ("第 7 周　鬼音与放克口袋", "032"),
        ("第 8 周　Shuffle 与抒情", "036"),
        ("第 9 周　把律动打成歌", "040"),
        ("第 10 周　半拍、停顿与重音", "044"),
        ("第 11 周　风格切换与假现场", "048"),
        ("第 12 周　结业驻场测验", "052"),
        ("附录 A　律动词典", "056"),
        ("附录 B　加花词典（先只用这些）", "057"),
        ("附录 C　五十首分级曲库", "058"),
        ("附录 D　结业评分表", "059"),
        ("附录 E　可复印练功日志", "060"),
        ("附录 F　十二周之后", "062"),
    ]
    left, right = items[:13], items[13:]
    def col(arr):
        lis = []
        for t, n in arr:
            lis.append(f"<li><span>{t}</span><span>{n}</span></li>")
        return "<ol>" + "".join(lis) + "</ol>"
    inner = f"""
<div class="kicker">CONTENTS</div>
<h2>目录</h2>
<p class="lead">建议双面打印、短边翻转、装订左侧。封面可彩色，内页黑白也可读。</p>
<div class="columns toc">
  <div>{col(left)}</div>
  <div>{col(right)}</div>
</div>
<div class="box accent">
  <h4>这本教材在解决什么</h4>
  <p>你不是零基础。你缺的是停练七八年后的反弹、脚、时间感和“为歌曲服务”的习惯。十二周的任务不是把 rudiment 打到考试级，而是把你重新练成<strong>酒吧眼里合格的鼓手</strong>：稳、懂段落、能跟贝斯、能撑场。</p>
</div>
<p class="mini">页码按打印成品估算；若你的打印机缩放不是 100%，以页脚实际页码为准。请用 A4、实际大小、背景图形开启。</p>
"""
    return page(inner, 2, "目录", "002")


def intro_pages():
    p3 = page("""
<div class="kicker">HOW TO USE</div>
<h2>写在前面</h2>
<p>这十二周按「学过两年架子鼓、搁置七到八年、目标至少达到酒吧驻唱/Livehouse 能用」来排。前四周当复健，第五周才加十六分踩镲，第七周才碰放克鬼音。加花全程克制——酒吧买的是稳，不是你的十六分绕鼓。</p>
<div class="grid-2">
  <div class="box">
    <h4>默认条件（未另行说明时）</h4>
    <ul>
      <li>每天 <strong>第 1–4 周 55 分钟</strong>，<strong>第 5–8 周 80 分钟</strong>，<strong>第 9–12 周 90 分钟</strong></li>
      <li>每周一至六上课，周日休息或只录音回听</li>
      <li>有节拍器（手机 App 即可），有一套五鼓三镲或练习垫+踏板</li>
      <li>双踩不是本教材内容，单踩足够酒吧</li>
      <li>曲风按华语流行 + 摇滚驻场混合</li>
    </ul>
  </div>
  <div class="box">
    <h4>每天怎么用这一页</h4>
    <ol>
      <li>先读本周「只准练的新内容」，不要超纲。</li>
      <li>按表格分钟数走，用厨房定时器也行。</li>
      <li>所有律动必须开节拍器。建议一耳音乐、一耳嘀嗒。</li>
      <li>打完在「☐」上打勾。漏练不补堆，挪到次日热身里 5 分钟即可。</li>
      <li>周六连打，周日听录音，只改一个最大的毛病。</li>
    </ol>
  </div>
</div>
<h3>若某天只有 40 分钟</h3>
<p>保留：热手 8 + 时间感 8 + 当日律动 15 + 跟奏 9。删加花。宁可缩短，不要无表乱砸。</p>
<h3>疼痛规则</h3>
<p>肌肉酸可以继续；手腕、虎口、前臂<strong>刺痛、发麻、起床仍痛</strong>则立刻减半量并只打垫子。停了多年最容易靠手臂死砸，那是受伤最快的路。</p>
<div class="box">
  <h4>打印说明</h4>
  <p>纸张 A4；双面；装订边在左；缩放 100%（实际大小）；开启「背景图形」。封面彩色更像教材，内页黑白完全可用。附录 E 的日志页可另复印 12 份，一周贴一张在鼓房墙上。</p>
</div>
""", 3, "如何使用", "003")

    p4 = page("""
<div class="kicker">PRINCIPLES</div>
<h2>十条训练原则</h2>
<ol>
  <li><strong>军鼓 2 和 4 是法律。</strong> 任何花样都以它不漂为前提。</li>
  <li><strong>越打越赶，就立刻降 10 bpm。</strong> 停练多年的第一大病是抢拍。</li>
  <li><strong>慢的平均，比快的糊更值钱。</strong> 酒吧中板（80–110）才是主战场。</li>
  <li><strong>先模仿，再个性。</strong> 跟奏时 90% 贴原鼓，不要发明。</li>
  <li><strong>加花短、准、接得回 1。</strong> 默认只用附录 B 的五个加花。</li>
  <li><strong>主歌必须比副歌空。</strong> 层次比密度重要。</li>
  <li><strong>脚比手更生，每天先救脚。</strong></li>
  <li><strong>录音比感觉诚实。</strong> 每周至少听一次自己。</li>
  <li><strong>为贝斯和歌手服务。</strong> 你的 1 要对着他们的 1。</li>
  <li><strong>耳塞是技术的一部分。</strong> 夜场不戴，细活一年后会下降。</li>
</ol>
<div class="columns">
  <div class="box">
    <h4>装备清单</h4>
    <ul>
      <li>☐ 5 鼓 3 镲（或练习套件）+ 军鼓垫</li>
      <li>☐ 一对 5A 或 5B 鼓棒，再备一对比着练</li>
      <li>☐ 束棒（lyric/慢歌用，第 8 周起）</li>
      <li>☐ 节拍器 App，能细分到 16 分、能静音小节</li>
      <li>☐ 隔音耳塞或鼓手耳塞</li>
      <li>☐ 手机支架（录音用，放身前 1.5 米）</li>
      <li>☐ 耳机一条（一耳听表或伴奏）</li>
    </ul>
  </div>
  <div class="box">
    <h4>调鼓（小场酒吧向）</h4>
    <ul>
      <li>军鼓：短、亮、略闷边，不要太散。</li>
      <li>底鼓：不要过轰，点要清楚，贝斯才跟得上。</li>
      <li>通鼓：中等闷音，加花时能听出音高即可。</li>
      <li>踩镲：能轻轻啄，也能副歌打开。</li>
      <li>大钹：片不要太大太响，小场很吃亏。</li>
    </ul>
    <p class="mini">没有调到完美不要停下来。本教材 90% 的进步来自时间感，不是来自鼓皮。</p>
  </div>
</div>
""", 4, "原则与装备", "004")

    p5 = page(f"""
<div class="kicker">NOTATION</div>
<h2>记谱符号</h2>
<p>全书律动按一小节 4/4、十六分网格记写。拍点列（1 2 3 4）底色更深。黑底白字是正常击打，灰底 <em>g</em> 是鬼音，红底 <em>X / C</em> 是开镲或大钹。</p>
<table>
  <tr><th>符号</th><th>含义</th><th>符号</th><th>含义</th></tr>
  <tr><td>●　B</td><td>底鼓</td><td>○　o</td><td>军鼓（重）</td></tr>
  <tr><td>g</td><td>军鼓鬼音（很轻）</td><td>x</td><td>闭镲 / 骑钹</td></tr>
  <tr><td>X</td><td>开镲</td><td>C</td><td>大钹（通常带底鼓）</td></tr>
  <tr><td>t</td><td>高通</td><td>F　T</td><td>地板通</td></tr>
  <tr><td>R / L</td><td>右 / 左手</td><td>–　空</td><td>休止</td></tr>
</table>
{groove_table("范例：基础八分摇滚", "bpm 80–110", [
    ("踩镲", "x.x.x.x.x.x.x.x."),
    ("军鼓", "....o.......o..."),
    ("底鼓", "B.......B......."),
], "军鼓锁在 2 和 4，底鼓在 1 和 3。这是后面所有变化的母格。")}
<div class="columns">
  <div class="box">
    <h4>每日时间块（对照用）</h4>
    <p><span class="badge">A</span> 手法热手　<span class="badge">B</span> 脚　<span class="badge">C</span> 时间感</p>
    <p><span class="badge">D</span> 当日律动　<span class="badge">E</span> 加花/段式　<span class="badge">F</span> 跟奏/连打</p>
    <p class="mini">第 1–4 周无独立 E 块，加花最多 2 拍过门。第 9 周起 F 块加长。</p>
  </div>
  <div class="box">
    <h4>速度怎么加</h4>
    <ul>
      <li>指定区间内，从最低速开始。</li>
      <li>能连续 2 分钟不抢、不僵，再 +4～6 bpm。</li>
      <li>一糊、一赶、肩耸起来：退回上一档。</li>
      <li>不要用「今天心情好」当理由跳速。</li>
    </ul>
  </div>
</div>
""", 5, "记谱与时间块", "005")

    p6 = page("""
<div class="kicker">FOUNDATION</div>
<h2>手法、踏板、节拍器</h2>
<div class="columns">
  <div>
    <h3>握棍（复健版）</h3>
    <p>用你以前学过的匹配握法即可，不要突然改成传统握法。要点只有四句：</p>
    <ol>
      <li>虎口轻夹，不要死捏。</li>
      <li>击打来自手腕，小臂跟随，不要砸肩膀。</li>
      <li>棍子打下去要自己弹回来，你是在「放」，不是在「按」。</li>
      <li>轻音用手指和手腕控制，重音才打开一点前臂。</li>
    </ol>
    <h3>热手 A 的固定菜单</h3>
    <ul>
      <li>单跳 RLRL　60→目标速</li>
      <li>双跳 RRLL</li>
      <li>帕拉迪德尔 RLRR LRLL</li>
      <li>重音移位：每 4 下把重音往后移一位</li>
    </ul>
  </div>
  <div>
    <h3>底鼓踏板</h3>
    <p>本教材默认 heel up：脚跟微离踏板，踩下去立刻松，让锤子回弹。踩死在板上是脚会废、速度上不去的原因。</p>
    <ul>
      <li>先练四分、八分平均。</li>
      <li>十六分要「粒粒分开」，不要连成嗡声。</li>
      <li>酒吧够用的脚：清楚的 1、3 和 &amp;，不是金属双踩。</li>
    </ul>
    <h3>节拍器四种开法（必须轮换）</h3>
    <ol>
      <li><strong>四分嘀嗒：</strong>你打八分。暴露抢拍。</li>
      <li><strong>八分嘀嗒：</strong>入门稳速。</li>
      <li><strong>十六分嘀嗒：</strong>练平的十六分踩镲。</li>
      <li><strong>二分嘀嗒 + 静音小节：</strong>只在 1、3 响；或 4 小节有表 / 4 小节静音再接回。</li>
    </ol>
  </div>
</div>
<div class="box accent">
  <h4>跟奏的标准流程（每首新歌都走一遍）</h4>
  <ol>
    <li>听两遍，只数结构：前奏 / 主歌 / 预副歌 / 副歌 / 桥 / 间奏 / 尾。</li>
    <li>在本周日志里用符号记录：底鼓 x、军鼓 o、加花 F、重音 &gt;。</li>
    <li>80% 速度跟三遍（可用变速 App）。</li>
    <li>原速跟三遍。</li>
    <li>把原鼓音量拧小或用伴奏，自己扛两遍。</li>
    <li>能完整过就算「B 组」；不看任何提示能过算「A 组」。</li>
  </ol>
</div>
""", 6, "基础复训", "006")

    p7 = page("""
<div class="kicker">MAP</div>
<h2>十二周总览</h2>
<table>
  <tr><th>周</th><th>阶段</th><th>每日</th><th>主题</th><th>过关一句话</th></tr>
  <tr><td>1</td><td>恢复</td><td>55′</td><td>反弹、基本摇滚、慢歌骨架</td><td>80 bpm 打 4 分钟不往上漂</td></tr>
  <tr><td>2</td><td>恢复</td><td>55′</td><td>底鼓四种变体，踩镲四分/八分</td><td>军鼓 2、4 在变底鼓时仍锁死</td></tr>
  <tr><td>3</td><td>恢复</td><td>55′</td><td>主歌轻/副歌重，大钹进段</td><td>能听出两层动态</td></tr>
  <tr><td>4</td><td>验收</td><td>60′</td><td>六首连打，恢复期测验</td><td>连续 20 分钟不崩</td></tr>
  <tr><td>5</td><td>重建</td><td>80′</td><td>十六分踩镲</td><td>90 bpm 右手像缝纫机</td></tr>
  <tr><td>6</td><td>重建</td><td>80′</td><td>Disco 四踩 + 开镲</td><td>100 bpm 四踩 2 分钟</td></tr>
  <tr><td>7</td><td>重建</td><td>80′</td><td>鬼音、简单放克</td><td>重音和鬼音能分开</td></tr>
  <tr><td>8</td><td>重建</td><td>80′</td><td>Shuffle / 12/8 抒情</td><td>三连音不变成十六分</td></tr>
  <tr><td>9</td><td>语汇</td><td>90′</td><td>完整段式、预示、count-in</td><td>16 小节主歌/副歌像一首歌</td></tr>
  <tr><td>10</td><td>语汇</td><td>90′</td><td>半拍、break、hits</td><td>停得干净、进得齐</td></tr>
  <tr><td>11</td><td>上台</td><td>90′</td><td>风格连切，45 分钟假现场</td><td>八首连打中间不重来</td></tr>
  <tr><td>12</td><td>结业</td><td>90′</td><td>十二至十五首 set + 录音评分</td><td>达到教材末页合格线</td></tr>
</table>
<div class="box">
  <h4>三阶段你听起来应该像什么</h4>
  <p><strong>第 4 周末：</strong>很久没打但底子还在。朋友排练可以跟着简单歌，还不能接夜场。</p>
  <p><strong>第 8 周末：</strong>常用酒吧节奏都见过一遍。加花仍须限制，但已经能交货给练习室乐队。</p>
  <p><strong>第 12 周末：</strong>酒吧眼里的入门合格线——set 不砸，歌手觉得稳，临时听前奏能进来。之后用曲库和合奏把 20 首变成 50 首。</p>
</div>
<p>每周结构相同：周一学新格子，周二巩固，周三变体或动态，周四歌曲，周五弱点+加花，周六假现场，周日休息/听录音。</p>
<div class="box accent">
  <h4>全期总曲目任务</h4>
  <p>十二周结束至少 <strong>A 组 8 首</strong>（不看提示能演）+ <strong>B 组 10 首</strong>（听前奏能进）+ <strong>C 组 6 首</strong>（看着结构纸能扛）。合计 24 首。真正驻场再花 3–6 个月扩到 50 首。</p>
</div>
""", 7, "十二周总览", "007")
    return p3 + p4 + p5 + p6 + p7


def day_card(day, minutes, title, rows, note=""):
    trs = []
    for chk, dur, mod, detail in rows:
        trs.append(
            f"<tr><td class='chk'>{'☐' if chk else ''}</td><td style='width:14mm'>{dur}</td><td style='width:18mm'>{mod}</td><td>{detail}</td></tr>"
        )
    note_html = f"<p class='note'>{note}</p>" if note else ""
    return f"""
<div class="day-card">
  <div class="day-head"><span>{day}　{title}</span><span class="meta">合计 {minutes}</span></div>
  <div class="day-body">
    <table>
      <tr><th></th><th>时间</th><th>模块</th><th>内容（照着做）</th></tr>
      {''.join(trs)}
    </table>
    {note_html}
  </div>
</div>
"""


def week_pass_box(items):
    lis = "".join(f"<li>☐ {x}</li>" for x in items)
    return f'<div class="box accent"><h4>本周过关（周日逐条勾）</h4><ul>{lis}</ul></div>'


def week_header(num, title, phase, minutes, thesis):
    return f"""
<div class="kicker">WEEK {num:02d}　{phase}</div>
<h2>第 {num} 周　{title}</h2>
<p class="lead">{thesis}</p>
<p><span class="tag">每日 {minutes}</span><span class="tag">一至六上课</span><span class="tag">周日回听</span></p>
"""


# -------------------- WEEK CONTENTS --------------------

def weeks():
    html = []

    # WEEK 1
    html.append(page(week_header(1, "把身体喊醒", "恢复期", "55 分钟",
        "这一周禁止加花。目标只有三个：棍子会弹、脚会松、军鼓在 2 和 4。")
        + groove_table("W1 母格　八分摇滚", "bpm 70–80", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.......B......."),
        ], "连续打时肩膀放松。如果越打越快，只降速度，不要加底鼓。")
        + groove_table("W1 底鼓变体 A　1 和 3+", "bpm 70–80", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.......B.B....."),
        ])
        + """<div class="box"><h4>本周只做的热手 A（10 分钟，每天相同）</h4>
        <p>垫子或军鼓。全程 60–80 bpm。单跳 3′ → 双跳 2′ → paradiddle 2′ → 重音移位 3′。轻响对比必须听得见。</p></div>
        <div class="box"><h4>本周歌曲</h4>
        <p><strong>必跟：</strong>《晴天》主歌骨架（只打 2/4 军鼓 + 稀疏底鼓）、Seven Nation Army 军鼓 2/4 骨架。<strong>禁止：</strong>副歌加花、通鼓轮奏。</p></div>
        """, 8, "第 1 周", "008"))

    html.append(page(
        day_card("周一", "55′", "找回反弹", [
            (1, "10′", "A 热手", "按本周固定菜单，60–70 bpm，不要超过 80。"),
            (1, "8′", "B 脚", "底鼓四分：60/70/80 各 1′；八分 70 bpm 2′；踩镲脚四分 2′。踩完立刻松。"),
            (1, "7′", "C 时间感", "节拍器八分嘀嗒。只打军鼓 2 和 4，70 bpm。其余声部全停。"),
            (1, "18′", "D 律动", "母格 70 bpm 连续 6′；休息 30″；再 6′。最后 6′ 改打变体 A。"),
            (1, "12′", "F 跟奏", "《晴天》主歌两遍，只打骨架。掉拍就停，数四拍再进，不要边掉边追。"),
        ], "今天成功的标准：打完手不僵，速度没有自己往上爬。")
        + day_card("周二", "55′", "脚比手更生", [
            (1, "10′", "A 热手", "同上。若虎口发红，再轻一点，不要减时间。"),
            (1, "10′", "B 脚", "底鼓：1 和 3 各 2′；只踩 2 和 4 各 2′（故意反着踩，看会不会晃）；八分 70 bpm 2′；十六分 60 bpm 2′，粒粒分开。"),
            (1, "7′", "C 时间感", "改开四分嘀嗒，你打八分踩镲（不打军鼓底鼓）70 bpm。这是本周最重要的 7 分钟。"),
            (1, "16′", "D 律动", "母格 72–76 bpm。每 4 小节把踩镲改成四分音符 4 小节，再改回八分。"),
            (1, "12′", "F 跟奏", "Seven Nation Army 两遍。军鼓必须像钉子。"),
        ])
        + day_card("周三", "55′", "变体还要锁军鼓", [
            (1, "10′", "A", "热手菜单。加入 1′ 的极轻单跳（几乎只有嘀声）。"),
            (1, "8′", "B", "底鼓变体：B...B.B. 与 B.B..... 各 3′（70 bpm，配军鼓 2/4）。"),
            (1, "7′", "C", "二分嘀嗒（只 1、3）。你把军鼓放在 2、4。70 bpm。"),
            (1, "18′", "D", "母格 4 小节 + 变体 A 4 小节，循环。军鼓音量保持一致。"),
            (1, "12′", "F", "两首各一遍。今天开始用手机录音 1 首歌，先不听，周五听。"),
        ]), 9, "第 1 周", "009"))

    html.append(page(
        day_card("周四", "55′", "歌曲日", [
            (1, "8′", "A", "缩短热手：单跳 3′ 双跳 2′ paradiddle 3′。"),
            (1, "6′", "C", "有表 4 小节 / 静音 4 小节，只打母格 70 bpm。接不回来就降到 66。"),
            (1, "25′", "F", "《晴天》结构走一遍（主歌空、副歌仍不要加花，只允许踩镲稍重）。Seven Nation Army 完整两三遍。"),
            (1, "16′", "D", "把两首歌的底鼓型慢练：从歌里抽 1 小节，循环 8 遍再换。"),
        ], "歌曲日仍然开节拍器。原曲速度若赶，用 App 降到 90%。")
        + day_card("周五", "55′", "回听与修补", [
            (1, "10′", "A", "热手菜单 70–80 bpm。"),
            (1, "8′", "B", "八分底鼓 70、76、80 各约 2′，剩下时间松脚踝。"),
            (1, "7′", "C", "听周三的录音。只找一件事：军鼓是早、晚还是准。写在日志上。"),
            (1, "18′", "D", "针对录音里的问题：若抢拍，只打军鼓 2/4 + 踩镲四分，72 bpm 10′；其余打母格。"),
            (1, "12′", "F", "两首各一遍，刻意放在嘀嗒后面一点点（靠后的口袋）。"),
        ])
        + day_card("周六", "55′", "假现场（短）", [
            (1, "8′", "A", "热手。"),
            (1, "40′", "F", "连打：母格 4′ →《晴天》2 遍 → 休息 30″ → Seven Nation Army 2 遍 → 母格 4′。中间不许停下来重来。错了就接着走。"),
            (1, "7′", "收", "80 bpm 四分音符全套件轻打，给手降温。喝水。"),
        ], "周日完全不打。只把本周过关项勾掉。可以听下周两首歌，画结构。"), 10, "第 1 周", "010"))

    html.append(page(
        week_pass_box([
            "80 bpm 母格连续 4 分钟，身体不僵，速度不往上漂",
            "闭眼打 4 小节再看表，没有整小节地溜走",
            "《晴天》主歌和 Seven Nation Army 能跟完，不加花",
            "手腕无刺痛；若有，第 2 周改全部垫上练习",
        ])
        + """<h3>常见失败与当场处理</h3>
        <table>
          <tr><th>现象</th><th>原因</th><th>当场怎么改</th></tr>
          <tr><td>越打越快</td><td>肩膀发力、听歌不听表</td><td>降 8–10 bpm；改打四分踩镲；只留军鼓</td></tr>
          <tr><td>底鼓闷成一坨</td><td>踩死不回弹</td><td>脚立刻离开，只打四分</td></tr>
          <tr><td>军鼓有时在 &amp;</td><td>手比脚抢</td><td>关掉底鼓和踩镲，只钉 2、4</td></tr>
          <tr><td>想加花</td><td>旧肌肉记忆</td><td>本周加花 = 0。把欲望写在日志里下周再说</td></tr>
        </table>
        <div class="box"><h4>周日日志（手写）</h4>
        <p>今天最稳的速度是 ______ bpm。最常抢的位置是第 ____ 拍。下周第一件要修的事：________________。</p>
        <p class="checkline">________________________________________________</p>
        <p class="checkline">________________________________________________</p>
        </div>
        <p class="mini">第 1 周结束时你不会「进步得很好听」。如果只是更稳，这周就满分。</p>
        """, 11, "第 1 周", "011"))

    # WEEK 2
    html.append(page(week_header(2, "锁死 2 和 4", "恢复期", "55 分钟",
        "底鼓开始换型，军鼓不许跟着晃。踩镲会四分和八分两种。仍几乎不加花。")
        + groove_table("变体 B　1+ 和 3", "bpm 72–84", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.B.....B......."),
        ])
        + groove_table("变体 C　四四拍摇滚常用", "bpm 72–88", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.....B.B.....B."),
        ], "1　2+　3　4+。很多华语摇滚副歌用这个。")
        + groove_table("四分踩镲母格（更难稳住）", "bpm 72–80", [
            ("踩镲", "x...x...x...x..."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.......B......."),
        ], "右手变少后，抢拍会原形毕露。")
        + "<div class='box'><h4>本周歌曲</h4><p>《海阔天空》主歌与副歌骨架（副歌只加密底鼓，不加花）；Wonderwall 八分吉他型，鼓打母格即可。</p></div>",
        12, "第 2 周", "012"))

    html.append(page(
        day_card("周一", "55′", "四种底鼓", [
            (1, "10′", "A", "热手 70–85 bpm。重音移位作为重点。"),
            (1, "8′", "B", "变体 B、C 的底鼓单独踩，72 bpm，各 4′。"),
            (1, "7′", "C", "四分嘀嗒 + 八分踩镲。"),
            (1, "18′", "D", "母格 / A / B / C 各 4 小节轮换，72–76 bpm。每换型军鼓音量不变。"),
            (1, "12′", "F", "《海阔天空》主歌，底鼓尽量少。"),
        ])
        + day_card("周二", "55′", "四分踩镲", [
            (1, "10′", "A", "热手。加 2′ 单跳极慢 50 bpm，看反弹。"),
            (1, "8′", "B", "八分底鼓 76 bpm 4′；十六分 66 bpm 4′。"),
            (1, "7′", "C", "二分嘀嗒放军鼓。"),
            (1, "18′", "D", "四分踩镲母格 10′；再八分 8′。对比哪一种你更抢。"),
            (1, "12′", "F", "Wonderwall 两遍。"),
        ])
        + day_card("周三", "55′", "换型不换军鼓", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "踏板：3 下密 + 1 下疏，72 bpm，练控制不是练速度。"),
            (1, "7′", "C", "静音小节练习。"),
            (1, "18′", "D", "每 2 小节换一个底鼓型，循环 A-B-C-母格。"),
            (1, "12′", "F", "两首各一遍，录音。"),
        ]), 13, "第 2 周", "013"))

    html.append(page(
        day_card("周四", "55′", "歌曲结构", [
            (1, "8′", "A", "短热手。"),
            (1, "6′", "C", "时间感。"),
            (1, "28′", "F", "《海阔天空》：主歌母格，副歌改变体 C，过门只准在第 4 拍打两下军鼓。Wonderwall 保持从头到尾几乎同一格，只在副歌稍重。"),
            (1, "13′", "D", "把「主歌母格 / 副歌变体 C」8+8 小节循环。"),
        ])
        + day_card("周五", "55′", "修抢拍", [
            (1, "10′", "A", "热手，轻响对比。"),
            (1, "8′", "B", "脚。"),
            (1, "7′", "C", "听录音，在日志写：抢 / 拖 / 准。"),
            (1, "18′", "D", "故意靠后：军鼓贴嘀嗒后沿。72–80 bpm。"),
            (1, "12′", "F", "慢速跟奏。"),
        ])
        + day_card("周六", "55′", "假现场", [
            (1, "8′", "A", "热手。"),
            (1, "40′", "F", "母格 3′ → 海阔天空 2 遍 → Wonderwall 2 遍 → 四种底鼓展示 8 小节×4 → 母格 3′。不许重来。"),
            (1, "7′", "收", "慢打放松。"),
        ]), 14, "第 2 周", "014"))

    html.append(page(week_pass_box([
            "四种底鼓型能轮换，军鼓仍在 2 和 4",
            "四分踩镲 76 bpm 打 2 分钟不抢",
            "两首新歌能跟完骨架",
            "已经连续两周周六不重来地连打",
        ]) + """
        <h3>本周思想</h3>
        <p>底鼓变化是「说话」，军鼓是「心跳」。心跳一乱，话没人听。如果你发现换底鼓时军鼓提前，说明手在帮忙数拍——把它改成脚数拍、手只负责 2 和 4。</p>
        <div class="box"><h4>周日听歌作业（不打鼓）</h4>
        <p>听《温柔》（五月天）和《突然好想你》。画出：哪里开始变重，大钹砸在哪一拍。下周要用。</p>
        </div>
        """, 15, "第 2 周", "015"))

    # WEEK 3
    html.append(page(week_header(3, "动态与段落意识", "恢复期", "55 分钟",
        "同样的格子，主歌轻、副歌重。学会在副歌第 1 拍给大钹。加花仍不超过 2 拍。")
        + groove_table("副歌推进格（开镲或骑钹）", "bpm 76–92", [
            ("镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.....B.B.....B."),
            ("大钹", "C..............."),
        ], "大钹只打段落第一拍，通常与底鼓重叠。不要每小节都砸。")
        + groove_table("2 拍过门（本周唯一准用的加花）", "bpm 76–88", [
            ("军鼓", "............oooo"),
            ("底鼓", "B..............."),
            ("大钹", "................"),
        ], "只占第 3、4 拍的十六分军鼓，下一小节 1 必须回到底鼓+大钹。先慢到 70。")
        + """<div class="box"><h4>动态口令（每天 D 块都要用）</h4>
        <p>4 小节 <strong>p</strong>（轻，腕力 30%）→ 4 小节 <strong>mf</strong>（中）→ 4 小节 <strong>f</strong>（副歌，腕力 70%，不是 100%）→ 2 拍过门 → 回到 p。死砸 100% 在小场又丑又累。</p></div>
        <div class="box"><h4>本周歌曲</h4><p>《温柔》《突然好想你》。重点不是鼓点难，是主歌几乎只有空气，副歌才打开。</p></div>
        """, 16, "第 3 周", "016"))

    html.append(page(
        day_card("周一", "55′", "两层音量", [
            (1, "10′", "A", "热手，特别练轻音。单跳里每 4 下只有 1 下重。"),
            (1, "8′", "B", "脚保持平均，不要为了副歌把踏板踩死。"),
            (1, "7′", "C", "四分嘀嗒。"),
            (1, "18′", "D", "母格做 p/mf/f 循环，76 bpm。录音 2 分钟。"),
            (1, "12′", "F", "《温柔》主歌，刻意打轻到自己觉得「是不是太小声」。"),
        ])
        + day_card("周二", "55′", "大钹进段", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "底鼓变体 C。"),
            (1, "7′", "C", "静音小节。"),
            (1, "18′", "D", "每 8 小节的第 9 小节 1 砸大钹。砸完立刻回到原音量。"),
            (1, "12′", "F", "《突然好想你》找副歌第一拍。"),
        ])
        + day_card("周三", "55′", "2 拍过门", [
            (1, "10′", "A", "热手。帕拉迪德尔 4′。"),
            (1, "8′", "B", "脚。"),
            (1, "7′", "C", "时间感。"),
            (1, "18′", "D", "3 小节律动 + 2 拍过门 + 回 1。循环 12 分钟。回不了 1 就降速。"),
            (1, "12′", "F", "两首歌的过门处用这一个加花，其它地方不许加。"),
        ]), 17, "第 3 周", "017"))

    html.append(page(
        day_card("周四", "55′", "整首动态", [
            (1, "8′", "A", "短热手。"),
            (1, "6′", "C", "时间感。"),
            (1, "30′", "F", "两首完整跟奏。主歌踩镲改为四分或极轻八分；副歌八分+变体 C；段落 1 给大钹。"),
            (1, "11′", "D", "默写《温柔》结构：有几段主歌、副歌、桥。"),
        ])
        + day_card("周五", "55′", "听层次", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "脚。"),
            (1, "10′", "C", "听本周录音。问：闭上眼睛能否听出哪是副歌？若不能，动态失败。"),
            (1, "15′", "D", "把对比再拉大：主歌更轻。"),
            (1, "12′", "F", "再录《温柔》一遍。"),
        ])
        + day_card("周六", "60′", "四首歌短 set", [
            (1, "8′", "A", "热手。"),
            (1, "45′", "F", "晴天 → 海阔天空 → 温柔 → Wonderwall。歌与歌之间只数四拍。模拟报歌但不要停手超过 10 秒。"),
            (1, "7′", "收", "放松。"),
        ]), 18, "第 3 周", "018"))

    html.append(page(week_pass_box([
            "同一律动能打出至少两层音量",
            "副歌第一拍能稳定给大钹",
            "2 拍过门十次里九次回到 1",
            "四首旧歌能连着过，中间不重来",
        ]) + """
        <div class="box"><h4>第 4 周预告</h4>
        <p>下周是恢复期验收：会有一份可打分的测验。本周把前三周格子都过一遍，不要学新花样。</p></div>
        <p>若动态仍然拉不开，问题通常不是手没力，而是主歌打太重。把主歌当成「伴奏给歌手喘气」。</p>
        """, 19, "第 3 周", "019"))

    # WEEK 4
    html.append(page(week_header(4, "恢复期验收", "验收周", "60 分钟",
        "不学新格子。把第 1–3 周变成能连续演奏的东西。周末做恢复期测验。")
        + """<div class="box accent"><h4>本周原则</h4>
        <p>速度回到你最稳的那一档，而不是最快的那一档。测验看的是稳、动态、不重来，不看花。</p></div>
        <h3>要能随时叫出的四格</h3>
        """
        + groove_table("① 母格", "最稳速度", [("踩镲", "x.x.x.x.x.x.x.x."), ("军鼓", "....o.......o..."), ("底鼓", "B.......B.......")])
        + groove_table("② 变体 C", "副歌", [("踩镲", "x.x.x.x.x.x.x.x."), ("军鼓", "....o.......o..."), ("底鼓", "B.....B.B.....B.")])
        + "<p class='caption'>③ 四分踩镲母格　④ 3+1 小节里的 2 拍军鼓过门。谱见第 1–3 周。</p>"
        + "<div class='box'><h4>本周曲目（六首）</h4><p>晴天、Seven Nation Army、海阔天空、Wonderwall、温柔、突然好想你。全部骨架+动态，加花只有 2 拍过门。</p></div>",
        20, "第 4 周", "020"))

    html.append(page(
        day_card("周一", "60′", "四格复习", [
            (1, "10′", "A", "热手 70–90 bpm 阶梯。"),
            (1, "8′", "B", "脚：四分/八分/变体 C。"),
            (1, "8′", "C", "四种节拍器开法各 2′。"),
            (1, "20′", "D", "四格各 5′，最稳速度。"),
            (1, "14′", "F", "六首里抽两首。"),
        ])
        + day_card("周二", "60′", "耐力萌芽", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "八分底鼓 80 bpm 2×2′。"),
            (1, "7′", "C", "时间感。"),
            (1, "20′", "D", "母格 80 bpm 连续 5′ 不中断。崩了记下第几分钟。"),
            (1, "15′", "F", "两首。"),
        ])
        + day_card("周三", "60′", "六首过一遍", [
            (1, "8′", "A", "短热手。"),
            (1, "6′", "C", "时间感。"),
            (1, "46′", "F", "六首各一遍。每首只打结构，错了不回头。旁边放纸，打叉记哪首掉拍。"),
        ]), 21, "第 4 周", "021"))

    html.append(page(
        day_card("周四", "60′", "修补日", [
            (1, "10′", "A", "热手。"),
            (1, "10′", "C", "针对掉拍的歌，静音小节。"),
            (1, "20′", "D", "只练打叉最多的那一格。"),
            (1, "20′", "F", "只重练最差的两首。"),
        ])
        + day_card("周五", "60′", "预演录音", [
            (1, "10′", "A", "热手。"),
            (1, "45′", "F", "按周六测验顺序走一遍并录音。中间可休息一次 1 分钟。"),
            (1, "5′", "收", "放松。晚上听一遍，不打鼓。"),
        ])
        + day_card("周六", "70′", "恢复期测验（必做）", [
            (1, "10′", "A", "热手，不要打太爆。"),
            (1, "50′", "测验", "见下页评分表。一次过，不重录。"),
            (1, "10′", "收", "拉伸手腕、前臂、脚踝。"),
        ], "周日休息。把分数抄进日志。低于合格线不重读教材，第 5 周仍继续，但十六分踩镲速度再降一档。"), 22, "第 4 周", "022"))

    html.append(page("""
<div class="kicker">EXAM 01</div>
<h2>恢复期测验</h2>
<p>节拍器可开。录音。每项 0–2 分：0 无、1 勉强、2 稳定。满分 20，<strong>14 分合格</strong>。</p>
<table>
  <tr><th>项</th><th>内容</th><th>分</th></tr>
  <tr><td>1</td><td>母格 80 bpm 连续 4 分钟，无明显加速</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>2</td><td>变体 B、C 各 8 小节，军鼓不漂</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>3</td><td>四分踩镲 76 bpm 1 分钟</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>4</td><td>p / f 交替，旁人能听出层次</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>5</td><td>2 拍过门 8 次，至少 7 次回到 1</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>6</td><td>静音 4 小节再接回，没有整拍误差</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>7</td><td>六首中任选三首连打，不重来</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>8</td><td>副歌第 1 拍大钹，没有砸错段</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>9</td><td>肩膀、手腕打完可酸不可刺痛</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
  <tr><td>10</td><td>录音里 2 和 4 总体在拍上</td><td>☐ 0 ☐ 1 ☐ 2</td></tr>
</table>
<p>总分 ______　合格 / 不合格　　日期 ________　最弱一项：________________</p>
<div class="box"><h4>测验曲目顺序（建议）</h4>
<p>① 母格 4′　② Seven Nation Army　③ 温柔　④ 海阔天空　⑤ 两项技术（四分踩镲 + 过门）　⑥ 自由选一首补动态</p></div>
<p class="mini">即使不合格也进入第 5 周。把最弱一项写成第 5–8 周每周五的固定修补题。</p>
""", 23, "第 4 周", "023"))

    # WEEK 5
    html.append(page(week_header(5, "十六分踩镲", "重建期", "80 分钟",
        "右手开始做华语流行里最常见的「缝纫机」。军鼓底鼓反而更要少而准。从本周起启用完整 A–F 结构。")
        + groove_table("十六分闭镲流行格", "bpm 76–96，先 80", [
            ("踩镲", "xxxxxxxxxxxxxxxx"),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.......B......."),
        ], "右手平均是唯一任务。左手军鼓仍只打 2、4。不要让右手带着军鼓变快。")
        + groove_table("十六分 + 底鼓 3+", "bpm 80–96", [
            ("踩镲", "xxxxxxxxxxxxxxxx"),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.......B.B....."),
        ])
        + """<div class="box"><h4>右手训练口诀</h4>
        <p>手腕小动作，贴着镲片，不要抬多高。像擦，不像砍。肩沉肘垂。一出现「一快一慢的波浪」，立刻降速。</p></div>
        <div class="box"><h4>本周歌曲</h4><p>《稻香》《爱情转移》。大量十六分或密八分的华语中板。</p></div>
        <p>热手 A 从本周起 12 分钟：单跳可推到 100–120（垫上），但套件律动速度仍按谱例。</p>
        """, 24, "第 5 周", "024"))

    html.append(page(
        day_card("周一", "80′", "缝纫机", [
            (1, "12′", "A", "单跳 80→120 阶梯；双跳；paradiddle；重音。"),
            (1, "10′", "B", "八分底鼓 80；十六分底鼓 70 粒开。"),
            (1, "8′", "C", "十六分嘀嗒，只打右手踩镲，80 bpm 4′；再加军鼓 2/4 共 4′。"),
            (1, "25′", "D", "十六分闭镲母格 80–84。每 4′ 休息 20″。"),
            (1, "10′", "E", "仍只用 2 拍军鼓过门，但过门时右手可停。"),
            (1, "15′", "F", "《稻香》主歌。"),
        ])
        + day_card("周二", "80′", "加上底鼓 3+", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "脚。重点 3+。"),
            (1, "8′", "C", "四分嘀嗒，你打十六分踩镲——很难，降速是正常的。"),
            (1, "25′", "D", "母格与 3+ 变体交替。"),
            (1, "10′", "E", "过门。"),
            (1, "15′", "F", "《爱情转移》。"),
        ])
        + day_card("周三", "80′", "动态十六分", [
            (1, "12′", "A", "热手，轻十六分。"),
            (1, "10′", "B", "脚。"),
            (1, "8′", "C", "静音小节 + 十六分踩镲。"),
            (1, "25′", "D", "主歌极轻十六分，副歌稍加重但不加速。"),
            (1, "10′", "E", "过门回 1。"),
            (1, "15′", "F", "两首，录音。"),
        ]), 25, "第 5 周", "025"))

    html.append(page(
        day_card("周四", "80′", "歌曲日", [
            (1, "10′", "A", "短热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "12′", "D", "十六分格巩固。"),
            (1, "10′", "E", "过门。"),
            (1, "40′", "F", "两首完整，含结构。主歌轻、副歌密。"),
        ])
        + day_card("周五", "80′", "修波浪", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "脚。"),
            (1, "10′", "C", "听录音：右手是否一波一波？"),
            (1, "25′", "D", "降 8 bpm 打平。用十六分嘀嗒盯死。"),
            (1, "8′", "E", "过门。"),
            (1, "15′", "F", "慢速跟奏。"),
        ])
        + day_card("周六", "80′", "假现场", [
            (1, "10′", "A", "热手。"),
            (1, "60′", "F", "八分摇滚两首 + 十六分两首连打。风格切换时先数四拍，再换右手密度。"),
            (1, "10′", "收", "放松。"),
        ]), 26, "第 5 周", "026"))

    html.append(page(week_pass_box([
            "90 bpm 十六分闭镲能打 2 分钟基本平均",
            "加上军鼓底鼓后右手不乱",
            "两首新歌能跟完",
            "从八分切到十六分不会加速",
        ]) + """
        <div class="box"><h4>重要提醒</h4>
        <p>十六分踩镲不是「打满就高级」。很多副歌用它，主歌仍应回到八分或四分。会切换，才像乐手。</p></div>
        """, 27, "第 5 周", "027"))

    # WEEK 6
    html.append(page(week_header(6, "Disco 四踩", "重建期", "80 分钟",
        "酒吧欢场、舞曲、婚礼、蹦迪翻唱的命根。底鼓打在每一拍，体能和平均比花样重要。")
        + groove_table("四踩 Disco 基础", "bpm 96–112，先 100", [
            ("骑钹/开镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B...B...B...B..."),
        ], "底鼓四下要一样重。不要 1 很重后面三下发虚。")
        + groove_table("四踩 + 第四拍开镲", "bpm 100–110", [
            ("踩镲", "x.x.x.x.x.x.x.X."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B...B...B...B..."),
        ], "第 4 拍 &amp; 打开镲，是舞曲最便宜的「闪亮」。")
        + groove_table("四踩 + 军鼓后十六点缀（可选）", "bpm 100", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "....o.g.....o.g."),
            ("底鼓", "B...B...B...B..."),
        ], "若鬼音还不稳，本周跳过此格，第 7 周再来。")
        + "<div class='box'><h4>本周歌曲</h4><p>Billie Jean（四踩变体，实际底鼓是经典线，先用四踩骨架跟上再贴原鼓）；Stayin’ Alive 或任何 100–110 舞曲；一首华语欢场（如《干杯》副歌推起来的四踩感）。</p></div>",
        28, "第 6 周", "028"))

    html.append(page(
        day_card("周一", "80′", "四下一样重", [
            (1, "12′", "A", "热手。"),
            (1, "12′", "B", "只踩四分底鼓 100 bpm 3×2′，组间休息 40″。这是体能课。"),
            (1, "8′", "C", "四分嘀嗒对齐四踩。"),
            (1, "23′", "D", "Disco 基础格 96–100。"),
            (1, "10′", "E", "2 拍过门，回 1 时四踩不要断。"),
            (1, "15′", "F", "Billie Jean 骨架。"),
        ])
        + day_card("周二", "80′", "开镲闪亮", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "四踩 100、104、108 阶梯。"),
            (1, "8′", "C", "时间感。"),
            (1, "25′", "D", "第四拍开镲格。开镲长短要收得住。"),
            (1, "10′", "E", "过门。"),
            (1, "15′", "F", "舞曲一首。"),
        ])
        + day_card("周三", "80′", "Billie Jean 线", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "把 Billie Jean 底鼓单独慢练（听原曲，1 和 &amp; 的位置）。"),
            (1, "8′", "C", "时间感。"),
            (1, "25′", "D", "先四踩骨架 10′，再贴原底鼓 15′。"),
            (1, "10′", "E", "过门克制，这首尤其不要花。"),
            (1, "15′", "F", "跟奏录音。"),
        ]), 29, "第 6 周", "029"))

    html.append(page(
        day_card("周四", "80′", "欢场歌", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "20′", "D", "四踩 100–108 耐力 2×3′。"),
            (1, "42′", "F", "三首舞/欢场。副歌开镲，主歌可改闭镲但仍四踩或回到八分摇滚——按原曲。"),
        ])
        + day_card("周五", "80′", "体能 + 修补", [
            (1, "12′", "A", "热手。"),
            (1, "15′", "B", "四踩 3×3′ / 休息 1′。脚可以酸，膝不要拧。"),
            (1, "8′", "C", "听录音：四踩有没有 1 重 234 虚。"),
            (1, "20′", "D", "平均力度。"),
            (1, "10′", "E", "过门。"),
            (1, "15′", "F", "最弱一首。"),
        ])
        + day_card("周六", "85′", "假现场：摇滚切蹦迪", [
            (1, "10′", "A", "热手。"),
            (1, "65′", "F", "温柔（抒情）→ 海阔天空（摇滚）→ Billie Jean（舞）→ 干杯或欢场。练的就是当晚酒吧最真实的切换。"),
            (1, "10′", "收", "拉伸小腿和髋。"),
        ]), 30, "第 6 周", "030"))

    html.append(page(week_pass_box([
            "100 bpm 四踩连续 2 分钟，四下力度接近",
            "会在第 4 拍 &amp; 打开镲并收住",
            "Billie Jean 能用骨架撑完，不求完全一样",
            "从慢歌切到舞曲不会抢第一小节",
        ]) + "<p>四踩是体力活。如果周末脚抽筋，第 7 周把体能组改成 2×2′，不要硬撑成伤。</p>",
        31, "第 6 周", "031"))

    # WEEK 7
    html.append(page(week_header(7, "鬼音与放克口袋", "重建期", "80 分钟",
        "军鼓开始「说话」：2 和 4 是重音，e 和 a 上的 g 是气声。酒吧不需要很难的线性放克，但要听得出口袋。")
        + groove_table("鬼音基础（先不加底鼓花样）", "bpm 80–92", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "..g.o.g...g.o.g."),
            ("底鼓", "B.......B......."),
        ], "g 只有重音的 20–30% 音量。听不见就稍加点；像第二颗军鼓就太重。")
        + groove_table("简单放克底鼓", "bpm 84–96", [
            ("踩镲", "x.x.x.x.x.x.x.x."),
            ("军鼓", "..g.o.g...g.o.g."),
            ("底鼓", "B.....B.B......."),
        ])
        + groove_table("十六分踩镲 + 鬼音（进阶，周五再碰）", "bpm 84–90", [
            ("踩镲", "xxxxxxxxxxxxxxxx"),
            ("军鼓", "..g.o.g...g.o.g."),
            ("底鼓", "B.......B.B....."),
        ])
        + "<div class='box'><h4>本周歌曲</h4><p>Uptown Funk 骨架；《牛仔很忙》一类带点跳的华语；Superstition 可听但只抠 2 小节底鼓+鬼音，整首不作为必过。</p></div>",
        32, "第 7 周", "032"))

    html.append(page(
        day_card("周一", "80′", "先把 g 做轻", [
            (1, "12′", "A", "热手。军鼓垫上：重轻轻轻 5′。"),
            (1, "10′", "B", "脚保持简单。"),
            (1, "8′", "C", "只打军鼓：2/4 重，其余可能的 g，80 bpm。"),
            (1, "25′", "D", "鬼音基础格。录音对比 g 和 o。"),
            (1, "10′", "E", "过门里不要鬼音，过门要干净。"),
            (1, "15′", "F", "Uptown Funk 骨架，鬼音能加再加。"),
        ])
        + day_card("周二", "80′", "口袋靠后", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "简单放克底鼓单独踩。"),
            (1, "8′", "C", "军鼓贴嘀嗒后沿。"),
            (1, "25′", "D", "简单放克格。"),
            (1, "10′", "E", "过门。"),
            (1, "15′", "F", "牛仔很忙类。"),
        ])
        + day_card("周三", "80′", "独立性", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "脚。"),
            (1, "8′", "C", "时间感。"),
            (1, "25′", "D", "右手八分不动，左手加 g。右手一乱就去掉一半 g。"),
            (1, "10′", "E", "过门。"),
            (1, "15′", "F", "录音。"),
        ]), 33, "第 7 周", "033"))

    html.append(page(
        day_card("周四", "80′", "歌曲", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "20′", "D", "三格复习。"),
            (1, "42′", "F", "Uptown Funk + 华语跳拍一首。宁可少 g，不要糊。"),
        ])
        + day_card("周五", "80′", "十六分踩镲 + 鬼音", [
            (1, "12′", "A", "热手。"),
            (1, "10′", "B", "脚。"),
            (1, "8′", "C", "十六分嘀嗒。"),
            (1, "25′", "D", "进阶格，84 bpm。失败就回到八分踩镲。"),
            (1, "10′", "E", "过门。"),
            (1, "15′", "F", "修补。"),
        ])
        + day_card("周六", "80′", "假现场", [
            (1, "10′", "A", "热手。"),
            (1, "60′", "F", "摇滚 → 十六分流行 → 四踩 → 放克骨架。四首四种味道。"),
            (1, "10′", "收", "放松。"),
        ]), 34, "第 7 周", "034"))

    html.append(page(week_pass_box([
            "能听出 o 和 g 是两种音量",
            "简单放克格 88 bpm 打 1 分钟不糊",
            "Uptown Funk 用骨架能撑，不求所有重音",
            "口袋不往前抢（录音验证）",
        ]) + """<div class="box"><h4>放克在酒吧的分寸</h4>
        <p>客人点的是歌。鬼音是调味，不是主菜。原曲没有密集鬼音就不要自行加满。第 8 周会完全换味道（三连音），鬼音先放一放。</p></div>""",
        35, "第 7 周", "035"))

    # WEEK 8
    html.append(page(week_header(8, "Shuffle 与抒情", "重建期", "80 分钟",
        "三连音感觉：蓝调、老摇滚、大量华语慢歌的 12/8。打成十六分就算失败。本周可改用束棒打抒情。")
        + groove_table_12("八分 Shuffle（每拍三连音，打第 1 与第 3）", "bpm 70–88，节拍器开 triplet", [
            ("踩镲", "x.xx.xx.xx.x"),
            ("军鼓", "...o.....o.."),
            ("底鼓", "B.....B....."),
        ], "感觉是「哒　哒」，中间那下靠后。若打成均匀十六分，这格就算失败。")
        + groove_table_12("12/8 抒情（每拍三下都打）", "慢歌，束棒更佳", [
            ("骑钹", "xxxxxxxxxxxx"),
            ("军鼓", "...o.....o.."),
            ("底鼓", "B.....B....."),
        ], "主歌极轻。军鼓仍在 2 和 4（三连音组的第 2、第 4 组）。")
        + """<div class="box"><h4>本周唯一新加花</h4>
        <p>通鼓下行八分：军鼓 – 高通 – 地板通 – 地板通，占 2 拍，回 1 砸大钹。仍禁止一小节满填。</p></div>
        <div class="box"><h4>本周歌曲</h4><p>《好久不见》或《我怀念的》；一首 12/8 慢歌（如部分版本《红豆》）；一首慢蓝调或老摇滚 shuffle。</p></div>
        """, 36, "第 8 周", "036"))

    html.append(page(
        day_card("周一", "80′", "triplet 进身体", [
            (1, "12′", "A", "热手改三连音单跳：每拍 RLR 或 LRL，70 bpm。"),
            (1, "10′", "B", "底鼓仍打四分，平均。"),
            (1, "10′", "C", "节拍器 triplet。只打踩镲 shuffle 8′。"),
            (1, "23′", "D", "Shuffle 母格。"),
            (1, "10′", "E", "通鼓下行 2 拍。"),
            (1, "15′", "F", "慢蓝调或 shuffle 歌。"),
        ])
        + day_card("周二", "80′", "12/8 抒情", [
            (1, "12′", "A", "热手，换束棒 5′ 找轻响。"),
            (1, "10′", "B", "脚轻踩。"),
            (1, "8′", "C", "triplet 表。"),
            (1, "25′", "D", "12/8 骑钹。空，再空一点。"),
            (1, "10′", "E", "抒情过门更短：第 4 拍两下通鼓即可。"),
            (1, "15′", "F", "好久不见 / 我怀念的。"),
        ])
        + day_card("周三", "80′", "别打回十六分", [
            (1, "12′", "A", "三连音热手。"),
            (1, "10′", "B", "脚。"),
            (1, "8′", "C", "在 shuffle 和直八分之间每 8 小节切换，体会完全不同。"),
            (1, "25′", "D", "两种都要稳。"),
            (1, "10′", "E", "加花。"),
            (1, "15′", "F", "录音，检查有没有把 shuffle 打直。"),
        ]), 37, "第 8 周", "037"))

    html.append(page(
        day_card("周四", "80′", "歌曲", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "triplet。"),
            (1, "20′", "D", "shuffle + 12/8。"),
            (1, "42′", "F", "两首慢歌完整，束棒或轻棍。歌手气口处不要填。"),
        ])
        + day_card("周五", "80′", "重建期总复习", [
            (1, "12′", "A", "热手直拍（不要 triplet）。"),
            (1, "10′", "B", "四踩 2×2′ 维持体能。"),
            (1, "8′", "C", "时间感直拍。"),
            (1, "25′", "D", "十六分踩镲、四踩、鬼音各 8′，看哪格生了。"),
            (1, "10′", "E", "两种过门。"),
            (1, "15′", "F", "生的那首。"),
        ])
        + day_card("周六", "90′", "重建期小测验 set", [
            (1, "10′", "A", "热手。"),
            (1, "70′", "F", "六种味道各一首：八分摇滚、十六分流行、Disco、放克骨架、Shuffle、12/8。中间只数拍。"),
            (1, "10′", "收", "拉伸。"),
        ], "周日听整场录音。能听出六种味道就算重建期成功。"), 38, "第 8 周", "038"))

    html.append(page(week_pass_box([
            "Shuffle 不再打成直十六分",
            "12/8 慢歌能轻、能留白",
            "通鼓下行 2 拍能回 1",
            "六种味道连打能换得过来",
        ]) + """
        <div class="box accent"><h4>重建期结束时的你</h4>
        <p>可以进练习室当乐队鼓手了。还不是驻场，因为曲库不够、临场语言（count-in、停顿、hits）还没系统练。那是第 9–12 周的事。</p></div>
        <p>把目前会的歌列成 A/B/C 三组，抄在日志扉页。第 9 周开始每首必须能回答：速度、军鼓在 2/4 还是半拍、主歌用什么镲、副歌砸不砸大钹、怎么收。</p>
        """, 39, "第 8 周", "039"))

    # WEEK 9
    html.append(page(week_header(9, "把律动打成歌", "语汇期", "90 分钟",
        "从本周起，技术服从结构。每天都要打一段 16 小节「像歌」的形式。学会 count-in 和副歌预示。")
        + """<div class="box"><h4>16 小节强制模板（每日 E 或 D）</h4>
        <ol>
          <li>4 小节主歌：闭镲，轻，底鼓少</li>
          <li>4 小节预副歌：加密底鼓或改八分更满</li>
          <li>4 小节副歌：骑钹或开镲，第 1 拍大钹，底鼓变体 C 或四踩</li>
          <li>2 小节过门加花（仍短）</li>
          <li>2 小节突然变空或全停 1 拍再进下一轮主歌</li>
        </ol></div>
        """
        + groove_table("预示：副歌前一拍的开镲", "任意律动的最后一拍", [
            ("踩镲", "x.x.x.x.x.x.x.X."),
            ("军鼓", "....o.......o..."),
            ("底鼓", "B.......B.....B."),
            ("大钹", "................"),
        ], "X 给乐队信号：下一小节是副歌。比加花更像会吃饭的人。")
        + """<div class="box"><h4>Count-in</h4>
        <p>木棒互点或军鼓边：1 2 3 4。第四下不许赶。快歌给八拍（1 2 3 4 2 2 3 4）。每天 F 块每首歌开头都数，不要直接跟着进。</p></div>
        <div class="box"><h4>本周歌曲</h4><p>《倔强》（完整结构）、《光辉岁月》、《夜空中最亮的星》。要求画出结构纸。</p></div>
        """, 40, "第 9 周", "040"))

    html.append(page(
        day_card("周一", "90′", "模板内化", [
            (1, "10′", "A", "热手 12′ 里取 10′，直拍。"),
            (1, "8′", "B", "脚。"),
            (1, "8′", "C", "时间感（含静音）。"),
            (1, "25′", "D", "用母格走 16 小节模板，80–90 bpm，循环。"),
            (1, "12′", "E", "只练预示开镲 + count-in 20 次。"),
            (1, "27′", "F", "《倔强》画结构并跟主歌副歌。"),
        ])
        + day_card("周二", "90′", "预副歌", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "脚。"),
            (1, "8′", "C", "时间感。"),
            (1, "25′", "D", "模板。预副歌必须能听出来。"),
            (1, "12′", "E", "count-in 快慢各 10 次。"),
            (1, "27′", "F", "光辉岁月。"),
        ])
        + day_card("周三", "90′", "三首歌的地图", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "20′", "D+E", "模板两轮。"),
            (1, "52′", "F", "三首各走结构。纸上标记大钹位置，打的时候只准砸这些位置。"),
        ]), 41, "第 9 周", "041"))

    html.append(page(
        day_card("周四", "90′", "自己扛", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "15′", "D", "模板。"),
            (1, "57′", "F", "原鼓拧到几乎没有，三首自己扛。掉结构就在纸上打叉，不要用加花掩盖。"),
        ])
        + day_card("周五", "90′", "修补结构", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "脚。"),
            (1, "8′", "C", "时间感。"),
            (1, "25′", "D", "针对打叉最多的段落类型（多半是桥或减半拍的预副歌）。"),
            (1, "12′", "E", "预示与过门。"),
            (1, "27′", "F", "只打最差一首，打到结构不错。"),
        ])
        + day_card("周六", "90′", "假现场", [
            (1, "10′", "A", "热手。"),
            (1, "70′", "F", "三首新 + 两首旧。每首必须 count-in。歌间 10 秒内给下一首速度。"),
            (1, "10′", "收", "听其中一首的开头 4 小节：第四下 count-in 赶了没有。"),
        ]), 42, "第 9 周", "042"))

    html.append(page(week_pass_box([
            "16 小节模板不看纸也能走两轮",
            "每首歌会 count-in，第四下不赶",
            "副歌前有预示，乐队（哪怕是假想）能听懂",
            "三首新歌有结构纸，并能跟完",
        ]) + """<div class="box"><h4>结构纸范例（手抄到日志）</h4>
        <p>《倔强》　速度约 ____　｜前奏 8　主 16　副 16　主 16　副 16　桥 ____　副 ____　尾 ____　｜大钹：每段副歌 1　｜收：________</p>
        <p class="mini">不会写标准总谱没关系。能让三个月后的你看懂就行。</p></div>
        """, 43, "第 9 周", "043"))

    # WEEK 10
    html.append(page(week_header(10, "半拍、停顿与重音", "语汇期", "90 分钟",
        "半拍（军鼓在 3）让副歌更宽。Break 和 hits 是酒吧鼓手的职业语言：停得干净，进得整齐。")
        + groove_table("半拍慢摇", "bpm 60–76 的慢四，或中板的半拍", [
            ("踩镲/骑钹", "x.x.x.x.x.x.x.x."),
            ("军鼓", "........o......."),
            ("底鼓", "B..............."),
        ], "军鼓只在 3。空是特点。不要手痒把 2、4 补回来，除非原曲如此。")
        + groove_table("Hit：全员在 1", "从静音进", [
            ("大钹", "C..............."),
            ("军鼓", "o..............."),
            ("底鼓", "B..............."),
        ], "三件套同时。不要底鼓先到。")
        + groove_table("Break：停 2 拍再进", "律动中突然", [
            ("全套", "x.x.o...--------"),
            ("底鼓", "B.......--------"),
        ], "后两拍完全静音，下一小节 1 一起回来。静音时双手停在空中，不要做多余小音。")
        + "<div class='box'><h4>本周歌曲</h4><p>《洋葱》或同类半拍抒情；Use Somebody；找一首有明显停顿的歌（很多华语副歌前会空一拍）。</p></div>",
        44, "第 10 周", "044"))

    html.append(page(
        day_card("周一", "90′", "半拍", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "底鼓更少，更重。"),
            (1, "8′", "C", "二分嘀嗒，把军鼓放在 3。"),
            (1, "25′", "D", "半拍格，主歌更空。"),
            (1, "12′", "E", "从半拍切回 2/4 军鼓：这是副歌常用手段。每 8 小节切一次。"),
            (1, "27′", "F", "洋葱类。"),
        ])
        + day_card("周二", "90′", "Hits", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "脚。"),
            (1, "8′", "C", "时间感。"),
            (1, "25′", "D", "8 小节律动 + 1 下 hit + 空 3 拍 + 再进。"),
            (1, "12′", "E", "hit 在 1、在 &amp;、在 4 各练。"),
            (1, "27′", "F", "Use Somebody。"),
        ])
        + day_card("周三", "90′", "Break", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "脚。"),
            (1, "8′", "C", "静音小节（这周的核心能力）。"),
            (1, "25′", "D", "停 1 拍、2 拍、整 4 拍。"),
            (1, "12′", "E", "停完回 1 必须齐：大钹+底鼓。"),
            (1, "27′", "F", "带停顿的歌。"),
        ]), 45, "第 10 周", "045"))

    html.append(page(
        day_card("周四", "90′", "三种收尾", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "20′", "E", "收在 1；收在 4；渐慢收。各 8 次，数出来。"),
            (1, "52′", "F", "三首，每首用不同结尾。"),
        ], "结尾砸散是业余的标志。宁可少一下。")
        + day_card("周五", "90′", "切来切去", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "脚。"),
            (1, "8′", "C", "时间感。"),
            (1, "30′", "D+E", "半拍主歌 → 2/4 副歌 → break → hit 进下一轮。"),
            (1, "34′", "F", "把这个套到本周歌里。"),
        ])
        + day_card("周六", "90′", "假现场", [
            (1, "10′", "A", "热手。"),
            (1, "70′", "F", "七首歌，必须含：一次半拍、一次明显停顿、一次 count-in、一次干净结尾。录音。"),
            (1, "10′", "收", "回听所有停顿：有没有多余的呱呱声。"),
        ]), 46, "第 10 周", "046"))

    html.append(page(week_pass_box([
            "半拍格能稳住，不偷偷加 2、4 军鼓",
            "break 时完全静音",
            "hit 三件套同时",
            "会三种结尾",
        ]) + "<p>职业鼓手被夸奖「稳」，经常是因为他会停。第 11 周要把这些放进 45 分钟不中断的 set。</p>",
        47, "第 10 周", "047"))

    # WEEK 11
    html.append(page(week_header(11, "风格切换与假现场", "上台期", "90 分钟",
        "技术不再加新格子。任务是：连续演奏、快速进歌、出错不回头。开始按夜场省力。")
        + """<div class="box accent"><h4>省力规则（从此常驻）</h4>
        <ul>
          <li>主歌腕力 30–40%，副歌 60–70%。</li>
          <li>副歌的亮靠开镲和底鼓重量，不靠手臂砸骑钹。</li>
          <li>通鼓加花能 2 拍解决的不要 4 拍。</li>
          <li>肩沉。耸肩 10 分钟后音准和速度都会崩。</li>
        </ul></div>
        <h3>本周每日固定 8 首菜单（顺序可排）</h3>
        <table>
          <tr><th>#</th><th>类型</th><th>从你的曲库选</th></tr>
          <tr><td>1</td><td>中板八分摇滚</td><td>海阔天空 / Don’t Look Back in Anger / 干杯</td></tr>
          <tr><td>2</td><td>华语十六分</td><td>稻香 / 爱情转移</td></tr>
          <tr><td>3</td><td>抒情 12/8 或极空</td><td>好久不见 / 温柔</td></tr>
          <tr><td>4</td><td>Disco / 舞</td><td>Billie Jean</td></tr>
          <tr><td>5</td><td>半拍</td><td>洋葱 / Use Somebody</td></tr>
          <tr><td>6</td><td>放克骨架</td><td>Uptown Funk</td></tr>
          <tr><td>7</td><td>乐队摇滚结构</td><td>倔强 / 光辉岁月</td></tr>
          <tr><td>8</td><td>自选补弱</td><td>本周最生的一首</td></tr>
        </table>
        <p>没有原曲某首就换同类型。关键是八种味道都要在一场里出现。</p>
        """, 48, "第 11 周", "048"))

    html.append(page(
        day_card("周一", "90′", "进歌速度", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "四踩 2′ 唤醒脚。"),
            (1, "8′", "C", "时间感。"),
            (1, "20′", "D", "随机抽类型报「舞曲 / 半拍 / shuffle」，4 小节内进入。"),
            (1, "44′", "F", "8 首各只打前 16 小节 + 副歌 8 小节。练进歌，不练完整。"),
        ])
        + day_card("周二", "90′", "完整两首精修", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "12′", "D", "弱格 12′。"),
            (1, "60′", "F", "8 首里最重要的两首打完整，各至少两遍，第二遍原鼓拧小。"),
        ])
        + day_card("周三", "90′", "45 分钟不中断预演", [
            (1, "10′", "A", "热手充分，今天是体能日。"),
            (1, "70′", "F", "连打约 45–50 分钟（6–8 首）。歌间只许 15 秒。错了接着。录音。"),
            (1, "10′", "收", "拉伸，立刻记下崩在第几首。"),
        ]), 49, "第 11 周", "049"))

    html.append(page(
        day_card("周四", "90′", "只修崩点", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "若崩在四踩，先做 2×3′ 体能。"),
            (1, "8′", "C", "时间感。"),
            (1, "30′", "D+E", "崩点段落（通常是抒情切舞曲的第一小节，或半拍切回 2/4）。"),
            (1, "34′", "F", "从崩的那首前一首接过去，连打三首。"),
        ])
        + day_card("周五", "90′", "临场事故演习", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "72′", "F", "故意制造状况：① count-in 数完发现速度不对，下一小节内修正；② 假想吉他手数错拍，你把 1 砸清楚捞回来；③ 某首临时跳过，15 秒内起下一首。"),
        ], "驻场不是打准练习室那一遍，是出事还能把场圆回去。")
        + day_card("周六", "100′", "正式假夜场", [
            (1, "12′", "A", "热手稍长。"),
            (1, "75′", "F", "8 首完整 set，录音。中间一次喝水 30 秒。必须含 count-in、至少一次 break、干净结尾。"),
            (1, "13′", "回听", "只评三件事：抢拍、层次、切换。"),
        ], "周日休息。列第 12 周结业 setlist（12–15 首）并排打印顺序。"), 50, "第 11 周", "050"))

    html.append(page(week_pass_box([
            "45 分钟连打不重来",
            "八种味道能在 4 小节内切换进入",
            "出现错误会接着走，并在下一句对齐",
            "打完手腕可酸，没有刺痛发麻",
        ]) + """<div class="box"><h4>第 12 周 setlist 怎么排（抄这套逻辑）</h4>
        <ol>
          <li>开场：中板稳的摇滚，让手热、让场热。</li>
          <li>第二首：更熟、可唱的华语。</li>
          <li>中前段：上一个小高潮（乐队歌）。</li>
          <li>中间：抒情，给所有人喘气，你改束棒或轻打。</li>
          <li>中后：舞曲/四踩把场拉起来。</li>
          <li>再抒情或半拍一首做对比。</li>
          <li>后段：两首连着的高能量。</li>
          <li>收：大家都熟的合唱，结尾干净。</li>
        </ol>
        <p>不要开场就 Disco 四踩 110，也不要连续三首 12/8。</p></div>
        """, 51, "第 11 周", "051"))

    # WEEK 12
    html.append(page(week_header(12, "结业驻场测验", "结业周", "90 分钟",
        "本周只有一件事：把 12 周练成一场能交出去的 set。周六做结业录音，用附录 D 评分。")
        + """<div class="box accent"><h4>结业 set 最低配置（12 首）</h4>
        <table>
          <tr><th>顺序</th><th>类型</th><th>你的歌名（手写）</th></tr>
          <tr><td>1</td><td>开场摇滚</td><td></td></tr>
          <tr><td>2</td><td>华语流行</td><td></td></tr>
          <tr><td>3</td><td>乐队结构歌</td><td></td></tr>
          <tr><td>4</td><td>十六分流行</td><td></td></tr>
          <tr><td>5</td><td>抒情 / 12/8</td><td></td></tr>
          <tr><td>6</td><td>半拍</td><td></td></tr>
          <tr><td>7</td><td>Disco / 舞</td><td></td></tr>
          <tr><td>8</td><td>放克骨架</td><td></td></tr>
          <tr><td>9</td><td>华语合唱</td><td></td></tr>
          <tr><td>10</td><td>摇滚高潮</td><td></td></tr>
          <tr><td>11</td><td>自选</td><td></td></tr>
          <tr><td>12</td><td>收场（干净结尾）</td><td></td></tr>
        </table>
        </div>
        <p>每首旁边用铅笔标速度和起手：闭镲 / 骑钹 / 四踩 / 束棒。周六只看这张纸，不看手机。</p>
        """, 52, "第 12 周", "052"))

    html.append(page(
        day_card("周一", "90′", "定稿 setlist", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "72′", "F", "12 首各打开头 8 小节 + 副歌进段，确认起手和速度。写在 setlist 上。不要纠结加花。"),
        ])
        + day_card("周二", "90′", "上半场 1–6", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "C", "时间感。"),
            (1, "72′", "F", "1–6 首完整连打两轮。第一轮可看结构纸，第二轮尽量不看。"),
        ])
        + day_card("周三", "90′", "下半场 7–12", [
            (1, "10′", "A", "热手。"),
            (1, "8′", "B", "四踩预热，因下半场通常更跳。"),
            (1, "8′", "C", "时间感。"),
            (1, "64′", "F", "7–12 连打两轮。收场结尾练 8 次。"),
        ]), 53, "第 12 周", "053"))

    html.append(page(
        day_card("周四", "90′", "全程预演", [
            (1, "12′", "A", "热手充分。"),
            (1, "70′", "F", "12 首一遍，录音。歌间 10–15 秒。中场可喝水一次 40 秒。"),
            (1, "8′", "笔记", "列出三处最差：第几首、什么问题。"),
        ])
        + day_card("周五", "70′", "只修三处 + 养手", [
            (1, "10′", "A", "轻热手。"),
            (1, "40′", "F", "只打那三处前后各一首，连起来。"),
            (1, "20′", "养", "慢速母格 80 bpm 轻打。早睡。不要突击新歌。"),
        ], "结业前一天加新歌，是业余最爱干的蠢事。")
        + day_card("周六", "110′", "结业测验", [
            (1, "15′", "A", "热手到出汗即可，不要打废。"),
            (1, "80′", "测验", "12 首一遍，一次录音，不重来。规则见附录 D。"),
            (1, "15′", "收", "拉伸。当周不要再暴打。周日只评分、写总结。"),
        ]), 54, "第 12 周", "054"))

    html.append(page("""
<div class="kicker">WEEK 12 CLOSE</div>
<h2>结业后怎么读自己的分数</h2>
<div class="columns">
  <div class="box">
    <h4>达到合格线</h4>
    <p>你已经是「练习室可用、小场可上」的鼓手。离稳定驻场还差：曲库 50 首、3–4 小时体能、真人贝斯合奏。按附录 F 进入维持期，每周至少一次合奏或 Jam。</p>
  </div>
  <div class="box">
    <h4>未到合格线</h4>
    <p>不要从头重练 12 周。把附录 D 里低于 1 分的项目抽出来，用第 5–11 周对应的周五修补法，专修 3 周，再把结业 set 重录一次。</p>
  </div>
</div>
<h3>给自己写的三句话（周日必填）</h3>
<p>1. 我现在最稳的风格是：________________________________</p>
<p>2. 我在酒吧会砸场的隐患是：________________________________</p>
<p>3. 下个月每周固定合奏时间：________________________________</p>
<div class="box accent">
  <h4>可以接的场 / 还不要接的场</h4>
  <p><strong>可以：</strong>朋友乐队排练、校园、餐厅不插电、一次 45–70 分钟的小 live、曲目事先给定的局。</p>
  <p><strong>还不要：</strong>无曲目清单的即兴驻唱、连续 3 小时点歌、大量拉丁/爵士即兴、金属双踩夜场。</p>
</div>
<p>把本教材附录 E 再复印 12 张，作为第 13–24 周曲库期日志。真正拉开和第二年鼓手差距的，是你接下来有没有每周把新歌变成 A 组。</p>
""", 55, "第 12 周", "055"))

    return "".join(html)


def appendix():
    a = []
    a.append(page("""
<div class="kicker">APPENDIX A</div>
<h2>律动词典（随时查阅）</h2>
<p>所有格子默认军鼓 2、4，除非写明半拍。速度是酒吧常用区，不是极限。</p>
"""
    + groove_table("A1 八分摇滚母格", "70–130", [("踩镲", "x.x.x.x.x.x.x.x."), ("军鼓", "....o.......o..."), ("底鼓", "B.......B.......")])
    + groove_table("A2 副歌摇滚", "80–120", [("踩镲", "x.x.x.x.x.x.x.x."), ("军鼓", "....o.......o..."), ("底鼓", "B.....B.B.....B.")])
    + groove_table("A3 十六分流行", "76–105", [("踩镲", "xxxxxxxxxxxxxxxx"), ("军鼓", "....o.......o..."), ("底鼓", "B.......B.B.....")])
    + groove_table("A4 Disco 四踩", "96–115", [("骑钹", "x.x.x.x.x.x.x.X."), ("军鼓", "....o.......o..."), ("底鼓", "B...B...B...B...")])
    + groove_table("A5 鬼音八分", "80–100", [("踩镲", "x.x.x.x.x.x.x.x."), ("军鼓", "..g.o.g...g.o.g."), ("底鼓", "B.....B.B.......")])
    + groove_table("A6 半拍", "60–90", [("骑钹", "x.x.x.x.x.x.x.x."), ("军鼓", "........o......."), ("底鼓", "B...............")])
    + "<p class='caption'>Shuffle / 12/8 见第 8 周。字典不够用时，优先把上面六格打到能聊天还不乱。</p>",
        56, "附录 A", "056"))

    a.append(page("""
<div class="kicker">APPENDIX B</div>
<h2>加花词典（十二周内先只用这些）</h2>
<p>每个加花结束的下一小节 1，必须底鼓+大钹一起。练法：3 小节律动 + 加花，循环 4 分钟。</p>
"""
    + groove_table("F1 第 4 拍两下通鼓（最常用）", "任何中板", [
        ("军鼓", "....o.......o..."),
        ("通鼓", "..............tT"),
        ("底鼓", "B.......B......."),
    ], "占 4 的 &amp; 和 a，或 4 和 &amp;。短。")
    + groove_table("F2 两拍军鼓十六分", "70–100", [
        ("军鼓", "........oooooooo"),
        ("底鼓", "B..............."),
    ])
    + groove_table("F3 下行 军-高通-地板-地板", "70–110", [
        ("军鼓", "............o..."),
        ("高通", "..............t."),
        ("地板", "...............T"),
    ], "按八分：o t T T 更常用，占两拍。")
    + groove_table("F4 一小节 paradiddle 绕桶", "70–90 先慢", [
            ("军鼓", "o.oo.oo........."),
            ("高通", "......t........."),
            ("地板", "........T.T....."),
        ], "建议 sticking：RLRR LRLL，后半小节落到通鼓。回不来 1 就停用。")
    + groove_table("F5 全停一拍再爆进", "任意", [
            ("镲/军", "x.x.o..........."),
            ("底鼓", "B..............."),
            ("大钹", "................"),
        ], "后两拍完全静音，下一小节 1：大钹与底鼓同时。这是五个里最高级的，因为它最空。")
    + """<div class="box accent"><h4>禁用清单（十二周内）</h4>
    <p>连续两小节绕鼓；双踩段落；没有回到 1 的滚奏；每一句都加花；主歌加花。</p></div>
    """, 57, "附录 B", "057"))

    a.append(page("""
<div class="kicker">APPENDIX C</div>
<h2>五十首分级曲库</h2>
<p>不是必须全会。按类型填满你的 A/B/C。★ 为十二周课内已点名。</p>
<table>
  <tr><th>类型</th><th>曲目（可替换同类型）</th></tr>
  <tr><td>八分摇滚</td><td>★海阔天空　★干杯　光辉岁月　真的爱你　Don’t Look Back in Anger　Wonderwall　七里香副歌</td></tr>
  <tr><td>十六分/流行</td><td>★稻香　★爱情转移　简单爱　修炼爱情　那些年　夜曲</td></tr>
  <tr><td>动态抒情</td><td>★温柔　★突然好想你　★好久不见　我怀念的　红豆　小幸运</td></tr>
  <tr><td>Disco/舞</td><td>★Billie Jean　Stayin’ Alive　Uptown Funk（偏放克）　欢入舞曲翻唱</td></tr>
  <tr><td>半拍/宽</td><td>★洋葱　Use Somebody　夜空中最亮的星（部分段）　某些英伦慢副歌</td></tr>
  <tr><td>结构/乐队</td><td>★倔强　拥抱　突然好想你（段式）　Mr. Brightside</td></tr>
  <tr><td>骨架入门</td><td>★晴天　★Seven Nation Army　后来（极简）</td></tr>
  <tr><td>Shuffle/老</td><td>蓝调翻唱　老摇滚 shuffle　部分 Beyond 中板</td></tr>
</table>
<div class="box">
  <h4>A / B / C 定义</h4>
  <p><strong>A</strong> 不看提示能演，中间有人solo也不丢。　<strong>B</strong> 听前奏 4 小节能进。　<strong>C</strong> 看着结构纸能扛。</p>
  <p>第 12 周目标：A≥8　B≥10　C≥6。驻场目标：合计约 50。</p>
</div>
<p class="mini">遇点歌不会：听前奏锁定速度与军鼓位置，先打母格。能撑比能花重要。下来再记进 C 组。</p>
""", 58, "附录 C", "058"))

    a.append(page("""
<div class="kicker">APPENDIX D</div>
<h2>结业评分表（第 12 周周六）</h2>
<p>每项 0–2 分。满分 30。<strong>21 分合格（酒吧入门线）</strong>；25 分以上为稳。</p>
<table>
  <tr><th>#</th><th>项目</th><th>0</th><th>1</th><th>2</th></tr>
  <tr><td>1</td><td>整场无明显持续加速</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>2</td><td>军鼓 2/4（或半拍的 3）总体锁死</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>3</td><td>主歌/副歌层次能听出来</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>4</td><td>count-in 不赶</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>5</td><td>至少一次有效预示或 break</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>6</td><td>加花短且能回 1</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>7</td><td>风格切换的第一小节不乱</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>8</td><td>四踩或舞曲段体能够用</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>9</td><td>抒情段有留白</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>10</td><td>出错后能在 4 小节内捞回</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>11</td><td>结尾干净</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>12</td><td>12 首不中断完成</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>13</td><td>无疼痛（酸可以）</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>14</td><td>set 顺序有呼吸（不是三首慢三首死砸）</td><td>☐</td><td>☐</td><td>☐</td></tr>
  <tr><td>15</td><td>录音回听：像在为歌服务</td><td>☐</td><td>☐</td><td>☐</td></tr>
</table>
<p>总分 ______　日期 ________　录音文件名 ________________</p>
<p>三项最低分对应的改进：① ________　② ________　③ ________</p>
<div class="box"><h4>合格意味着什么</h4>
<p>不是「已经是职业鼓手」。是：把你放进一个曲目事先知道的酒吧小场，你大概率不砸，歌手愿意再约。这就是本教材的终点。</p></div>
""", 59, "附录 D", "059"))

    log_table = """
<table>
  <tr><th>日</th><th>实际分钟</th><th>A</th><th>B</th><th>C</th><th>D 主题</th><th>F 歌曲</th><th>抢/拖/准</th><th>疼痛</th></tr>
""" + "\n".join(
        f"<tr class='log-row'><td>{d}</td><td></td><td>☐</td><td>☐</td><td>☐</td><td></td><td></td><td></td><td></td></tr>"
        for d in ["一", "二", "三", "四", "五", "六", "日"]
    ) + "</table>"

    a.append(page(f"""
<div class="kicker">APPENDIX E</div>
<h2>练功日志（可复印）</h2>
<p>第 ____ 周　　日期 ________ 至 ________　　本周主题 ________________</p>
{log_table}
<div class="box">
  <h4>周六录音三句话</h4>
  <p>1. ________________________________________________</p>
  <p>2. ________________________________________________</p>
  <p>3. ________________________________________________</p>
</div>
<div class="box">
  <h4>周日过关</h4>
  <p>☐ 全部过关　☐ 一项未过：________　下周修补放在周五</p>
  <p>本周 A 组新增：________　B 组新增：________</p>
</div>
<p class="mini">此页可单独再印 12 份。不要写在教材内页上，方便重用。</p>
""", 60, "附录 E", "060"))

    a.append(page(f"""
<div class="kicker">APPENDIX E</div>
<h2>练功日志（复印页 2）</h2>
<p>第 ____ 周　　日期 ________ 至 ________　　本周主题 ________________</p>
{log_table}
<h3>结构纸草稿</h3>
<p>歌名 ________　速度 ____　军鼓位置 ____</p>
<p class="checkline">前奏 ______ 主歌 ______ 预副 ______ 副歌 ______ 桥 ______ 尾 ______</p>
<p class="checkline">大钹位置 ________________________________________________</p>
<p class="checkline">结尾方式 ________________________________________________</p>
<p class="checkline">备注 ________________________________________________</p>
<p class="checkline">________________________________________________</p>
""", 61, "附录 E", "061"))

    a.append(page("""
<div class="kicker">APPENDIX F</div>
<h2>十二周之后</h2>
<h3>第 13–24 周：曲库期（驻场准备）</h3>
<ul>
  <li>每周新学 4 首，复习 6 首。走第 5 页的跟奏六步。</li>
  <li>每周 3 天技术保养（各 40′：热手+时间感+弱风格），2 天曲库，1 天合奏，1 天休息。</li>
  <li>每周一次 90′ 真人合奏；没有乐队就跟贝斯谱或原曲减鼓轨。</li>
  <li>体能：Disco 100–112 bpm，3×3′，每周三次。</li>
  <li>第 24 周末：A+B+C 合计 50 首，能连打 15 首约 60 分钟。</li>
</ul>
<h3>仍然不必优先的东西</h3>
<p>双踩、爵士骑钹独立、线性 rudiment 考试速度、超长 Solo。这些有余力再开专项，不挡你进酒吧。</p>
<h3>合奏时只盯三件事</h3>
<ol>
  <li>贝斯的 1</li>
  <li>歌手的气口</li>
  <li>副歌第一下齐不齐</li>
</ol>
<div class="rule"></div>
<p>停了七八年还能把这本写满打卡的人，已经比「一直想重新开始」的人走得远。从第 1 周周一只打军鼓 2 和 4 开始。把节拍器打开。</p>
<div class="box accent" style="margin-top:6mm">
  <h4>封面可撕下的一句</h4>
  <p style="font-size:13pt;letter-spacing:.12em;margin:2mm 0 0">稳，比花更像鼓手。</p>
</div>
<p class="mini" style="margin-top:8mm">本教材为个人复训课表，可打印自用。曲目名称为学习提示，请使用正版音频跟奏。</p>
""", 62, "附录 F", "062"))
    return "".join(a)


def build():
    parts = [
        "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'>",
        "<title>酒吧鼓手十二周复训教材</title>",
        f"<style>{CSS}</style></head><body>",
        cover(),
        toc(),
        intro_pages(),
        weeks(),
        appendix(),
        "</body></html>",
    ]
    html = "".join(parts)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    build()
