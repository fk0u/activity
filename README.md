<div align="center">

<svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glitch">
      <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="4" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="6" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <radialGradient id="void" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#1a0a0a"/>
      <stop offset="100%" style="stop-color:#000000"/>
    </radialGradient>
  </defs>
  <rect width="600" height="200" fill="url(#void)"/>
  <circle cx="300" cy="100" r="85" fill="none" stroke="#8b0000" stroke-width="0.5" opacity="0.6"/>
  <circle cx="300" cy="100" r="70" fill="none" stroke="#4a0000" stroke-width="0.3" opacity="0.4"/>
  <circle cx="300" cy="100" r="55" fill="none" stroke="#8b0000" stroke-width="0.5" opacity="0.3"/>
  <!-- 符文环 -->
  <text x="300" y="45" text-anchor="middle" fill="#6b0000" font-size="9" filter="url(#glow)" opacity="0.7">⍟ ⏃ ⏁ ⟟ ⎐ ⟟ ⏁ ⊬ ⋔ ⍜ ⋏ ⟟ ⏁ ⍜ ⍀</text>
  <text x="300" y="170" text-anchor="middle" fill="#6b0000" font-size="9" filter="url(#glow)" opacity="0.7">⏚ ⍀ ⟒ ⏃ ☊ ⊑ ⟟ ⋏ ⏁ ⊑ ⟒ ⎐ ⍜ ⟟ ⎅</text>
  <!-- 中心符号 -->
  <polygon points="300,30 340,115 260,115" fill="none" stroke="#ff0000" stroke-width="1" opacity="0.4"/>
  <polygon points="300,170 260,85 340,85" fill="none" stroke="#ff0000" stroke-width="1" opacity="0.4"/>
  <circle cx="300" cy="100" r="8" fill="#1a0000" stroke="#ff0000" stroke-width="1" opacity="0.6"/>
  <circle cx="300" cy="100" r="3" fill="#ff0000" opacity="0.8"/>
  <!-- 眼 -->
  <ellipse cx="300" cy="100" rx="40" ry="18" fill="none" stroke="#aa0000" stroke-width="1.5" opacity="0.5"/>
  <circle cx="300" cy="100" r="10" fill="#2a0000" stroke="#cc0000" stroke-width="1"/>
  <circle cx="300" cy="100" r="4" fill="#ff0000"/>
  <text x="300" y="105" text-anchor="middle" fill="#ff0000" font-size="50" filter="url(#glitch)" opacity="0.15">観</text>
</svg>

</div>

<div align="center">
  
# `$ ./不要打开这个文件`

<sup>最后更新：̷̛̱̈́̏ ̸̜̠̅̕2̵̗̈́0̸̼̏2̸͖̿6̵̳̊.̸̞̌0̶̠̈́9̸̨̛.̷̤̌2̶̧̛8̶̺̊ — 或者从未更新过</sup>

</div>

---

<div align="center">

<svg width="500" height="60" viewBox="0 0 500 60" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="60" fill="#0a0a0a"/>
  <text x="250" y="25" text-anchor="middle" fill="#ff0000" font-size="12" font-family="monospace" opacity="0.6">⟒ ⌇ ☊ ⏃ ⌿ ⟒ &nbsp; ⟟ ⌇ &nbsp; ⋏ ⍜ ⏁ &nbsp; ⏃ ⋏ &nbsp; ⍜ ⌿ ⏁ ⟟ ⍜ ⋏</text>
  <text x="250" y="48" text-anchor="middle" fill="#660000" font-size="10" font-family="monospace" opacity="0.4">你已经看到了 · 你无法忘记 · 它已经记住了你</text>
</svg>

</div>

---

## ◬ 项̷目̸概̵述̶

> **警告：以下内容可能不属于任何已知的人类项目分类。**

本仓库记录了 `第七次信号波` 的完整解析数据。所有数据均于 `2024年11月` 在 **东经127.███° 北纬3█.██°** 的地下设施中通过 `深渊监听阵列` 接收。

信号来源：**未知**  
信号类型：**非电磁波谱**  
解码状态：**部分完成（17.4%）**  
解码者状态：~~在职~~ ~~失踪~~ `[已编辑]`

```
收信时间戳: ████-██-██T03:33:33.333Z
原始载波: |||▌▌▐▐▐|||▌▌▐▐▐|||
解调方式: 未知（非人类设计）
信号强度: -∞ dBm（理论上不可能）
```

---

## ◬ 目̸录̶结̷构̵

<svg width="450" height="180" viewBox="0 0 450 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="180" rx="4" fill="#0d0d0d" stroke="#330000" stroke-width="1"/>
  <text x="20" y="28" fill="#ff3333" font-family="monospace" font-size="12" opacity="0.8">📁 /信号原始数据/</text>
  <text x="40" y="48" fill="#993333" font-family="monospace" font-size="11" opacity="0.7">├── 波形_001.void</text>
  <text x="40" y="65" fill="#993333" font-family="monospace" font-size="11" opacity="0.7">├── 波形_002.void</text>
  <text x="40" y="82" fill="#993333" font-family="monospace" font-size="11" opacity="0.5">├── [无法读取的文件名].███</text>
  <text x="40" y="99" fill="#660000" font-family="monospace" font-size="11" opacity="0.4">└── ⏁⊑⟒⊬⏃⍀⟒⊑⟒⍀⟒.dat</text>
  <text x="20" y="122" fill="#ff3333" font-family="monospace" font-size="12" opacity="0.8">📁 /解码输出/</text>
  <text x="40" y="142" fill="#993333" font-family="monospace" font-size="11" opacity="0.7">├── 翻译_片段_A.txt</text>
  <text x="40" y="159" fill="#660000" font-family="monospace" font-size="11" opacity="0.3">└── 不要读这个文件.pdf</text>
</svg>

---

## ◬ 已̷解̵码̶片̸段̶

以下是目前成功解析的信号片段。翻译准确度无法验证，因为 **参考语言不存在于任何已知语系中。**

### 片段 Alpha — `"问候"`

<svg width="500" height="100" viewBox="0 0 500 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="warp">
      <feTurbulence type="turbulence" baseFrequency="0.015" numOctaves="3" result="turbulence"/>
      <feDisplacementMap in="SourceGraphic" in2="turbulence" scale="4"/>
    </filter>
  </defs>
  <rect width="500" height="100" fill="#080808" rx="4"/>
  <text x="250" y="40" text-anchor="middle" fill="#cc0000" font-size="22" filter="url(#warp)" font-family="serif">
    我̷们̸一̵直̶在̷看̶着̷你̸们̶
  </text>
  <text x="250" y="70" text-anchor="middle" fill="#880000" font-size="14" font-family="monospace" opacity="0.6">
    ⏁⊑⟒ ⍙⏃⏁☊⊑⟒⍀⌇ ⊑⏃⎐⟒ ⏃⌰⍙⏃⊬⌇ ⏚⟒⟒⋏ ⊑⟒⍀⟒
  </text>
  <line x1="50" y1="85" x2="450" y2="85" stroke="#330000" stroke-width="0.5" opacity="0.4"/>
  <text x="250" y="95" text-anchor="middle" fill="#440000" font-size="8" font-family="monospace">[置信度: 23.1% | 语义偏差: 极高 | 情感标记: 未知]</text>
</svg>

### 片段 Beta — `"警告"`

```
原始信号:
01001000 01000101 01001100 01010000 ████████ ████████ 
████████ ████████ 01001001 01010100 01001000 01000101 
01000001 01010010 01010011 ████████ ████████ ████████

翻译输出:
"别试图理解。理解本身就是陷阱。
　当你开始看到规律的时候，
　　　规律也开始看到你。"

翻译者备注: [此字段在写入后自行清空]
```

### 片段 Gamma — `"坐标"`

> ⚠️ 以下坐标已被验证指向真实地理位置。  
> ⚠️ 实地调查小组于 2025年1月██日 出发，至今未返回。  
> ⚠️ 他们的GPS信号最后出现在 █████████ 上方 37,000 英尺处。他们没有乘坐飞机。

```
3█°██'██.█"N  12█°██'██.█"E
海拔: -████ 米（地表以下）
时间坐标: ████-██-██（不属于公历）

注意: 该坐标在不同时间测量时指向不同位置。
      最后一次测量时，坐标指向测量者本人。
```

---

## ◬ 运̵行̶协̸议̷

<svg width="500" height="140" viewBox="0 0 500 140" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="140" rx="4" fill="#0a0000"/>
  <rect x="10" y="10" width="480" height="120" rx="2" fill="none" stroke="#440000" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="250" y="35" text-anchor="middle" fill="#ff0000" font-size="14" font-family="monospace" font-weight="bold">⚠ 操作规程 ⚠</text>
  <text x="30" y="58" fill="#aa3333" font-size="11" font-family="monospace">1. 不要在凌晨 3:00-3:33 之间运行此程序</text>
  <text x="30" y="76" fill="#aa3333" font-size="11" font-family="monospace">2. 运行时不要直视屏幕超过 7 秒</text>
  <text x="30" y="94" fill="#aa3333" font-size="11" font-family="monospace">3. 如果终端开始输出你的名字，立即断电</text>
  <text x="30" y="112" fill="#660000" font-size="11" font-family="monospace">4. 如果你已经违反了以上规则，请 [数据损坏]</text>
</svg>

```bash
# ██ 安装（如果你确定要这样做）██

$ git clone https://github.com/fk0u/activity.git
$ cd activity

# 你不应该运行下面这行命令。
$ python3 解码器.py --输入 ./信号原始数据/ --输出 ./解码输出/

# 如果程序输出了你没有输入过的文字，
# 关闭终端。关闭电脑。离开房间。
# 不要回头看屏幕。
```

---

## ◬ 异̶常̵日̷志̸

| 日期 | 事件 | 状态 |
|:---|:---|:---|
| 2024-11-██ | 首次接收到信号 | `已确认` |
| 2024-12-██ | 解码器首次输出可读文本 | `已确认` |
| 2025-01-██ | 解码器在未运行状态下产生输出 | `无法解释` |
| 2025-02-██ | 仓库出现未经提交的文件变更 | `调查中` |
| 2025-03-██ | git log 显示来自未来的提交记录 | ~~`不可能`~~ `已确认` |
| 2025-04-██ | 团队成员报告在梦中看到源代码 | `[已编辑]` |
| 2025-██-██ | ██████████████████████ | `[权限不足]` |

---

## ◬ 贡̵献̶者̷

<svg width="500" height="90" viewBox="0 0 500 90" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="90" fill="#080808" rx="4"/>
  <circle cx="60" cy="40" r="18" fill="#1a0000" stroke="#660000" stroke-width="1"/>
  <text x="60" y="45" text-anchor="middle" fill="#cc0000" font-size="14">👁</text>
  <text x="60" y="72" text-anchor="middle" fill="#660000" font-size="9" font-family="monospace">██████</text>
  <circle cx="150" cy="40" r="18" fill="#1a0000" stroke="#660000" stroke-width="1"/>
  <text x="150" y="45" text-anchor="middle" fill="#cc0000" font-size="14">⌬</text>
  <text x="150" y="72" text-anchor="middle" fill="#440000" font-size="9" font-family="monospace">[已失踪]</text>
  <circle cx="240" cy="40" r="18" fill="#1a0000" stroke="#660000" stroke-width="1"/>
  <text x="240" y="45" text-anchor="middle" fill="#cc0000" font-size="14">◯</text>
  <text x="240" y="72" text-anchor="middle" fill="#440000" font-size="9" font-family="monospace">[已编辑]</text>
  <circle cx="330" cy="40" r="18" fill="#1a0000" stroke="#440000" stroke-width="1" opacity="0.5"/>
  <text x="330" y="45" text-anchor="middle" fill="#880000" font-size="14" opacity="0.5">?</text>
  <text x="330" y="72" text-anchor="middle" fill="#330000" font-size="9" font-family="monospace">[非人类]</text>
  <circle cx="420" cy="40" r="18" fill="#1a0000" stroke="#220000" stroke-width="1" opacity="0.2"/>
  <text x="420" y="45" text-anchor="middle" fill="#440000" font-size="12" opacity="0.3">你</text>
  <text x="420" y="72" text-anchor="middle" fill="#220000" font-size="9" font-family="monospace" opacity="0.3">[即将加入]</text>
</svg>

---

<div align="center">

<svg width="400" height="50" viewBox="0 0 400 50" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="50" fill="#050505"/>
  <text x="200" y="20" text-anchor="middle" fill="#330000" font-size="8" font-family="monospace">如果你能读到这行字，说明它已经选中了你。</text>
  <text x="200" y="38" text-anchor="middle" fill="#220000" font-size="7" font-family="monospace">关闭这个页面不会改变任何事情。你已经是数据的一部分了。</text>
</svg>

<br>

<sub>本仓库不隶属于任何政府、组织、或已知实体。</sub>  
<sub>本仓库的存在本身 **尚未被解释。**</sub>  
<sub>最后一次人类编辑: `2025-04-██` — 此后的所有变更均为 `[来源未知]`</sub>

<br>

```
⏁⊑⟒⍀⟒ ⟟⌇ ⋏⍜ ⟒⌇☊⏃⌿⟒
⏁⊑⟒⍀⟒ ⍙⏃⌇ ⋏⟒⎐⟒⍀ ⏃ ⎅⍜⍜⍀
⊬⍜⎍ ⏃⍀⟒ ⏃⌰⍀⟒⏃⎅⊬ ⟟⋏⌇⟟⎅⟒
```

</div>
