# LockPCB — 火柴盒门锁 PCB 工程

这是室内改装式、免打孔/免布线门锁的 PCB 工程起点。KiCad 工程已纳入设计师确认稿的 source-derived 14 × 50 mm PCB 外形与孔位参考；Agent 的功能分区和电气架构仍是待评审提案。尚无电气焊盘/网络实现、真实原理图连接、PCB 布线、制造输出或硬件验证。

## 开始

- 在 KiCad 中打开 `pcb/LockPCB.kicad_pro`；同目录含 `.kicad_sch` 与 `.kicad_pcb`。
- 需求、机械输入、功耗预算、功能分区及候选决策见 `docs/` 与 `decisions/`。
- CI workflow：`.github/workflows/kicad-ci.yml`；CI 明确固定并校验 KiCad 8 主版本。
- `pcb/LockPCB.kicad_pcb` 是本仓库 Agent 工程设计的编辑源：Edge.Cuts 与孔位图形参考已按设计师确认稿迁入；功能区域仍属 Agent 提案。它不是电气闭合或制造发布的 PCB。设计师机械事实以 Drive 确认的 CAD/DWG/STEP 为准，见 `docs/FACTORY_PROTOTYPE_GEOMETRY_REPORT.md`。

## Visual overview

[![Agent-generated capability-test overview of PRE-CAD placeholders and proposed 1S power architecture](docs/previews/engineering-overview.png)](https://github.com/lin2mm/LockPCB/blob/arena/3b84c22f-lockpcb/docs/previews/engineering-overview.png)

[Open the full-size preview directly on GitHub](https://github.com/lin2mm/LockPCB/blob/arena/3b84c22f-lockpcb/docs/previews/engineering-overview.png) · [Open the raw PNG](https://raw.githubusercontent.com/lin2mm/LockPCB/arena/3b84c22f-lockpcb/docs/previews/engineering-overview.png)

> Agent-generated capability-test graphic only; not designer-confirmed, not to scale, and not a substitute for the confirmed Drive CAD/DWG/STEP sources or mechanical validation. The direct GitHub link may require repository access. See [`docs/previews/README.md`](docs/previews/README.md).

## 当前状态

**Source-aligned PRE-CAD 阶段，不可投板。** `Edge.Cuts` 已按 DWG 轮廓迁入 **14 × 50 mm** 包络（含边缘台阶/缺口），`Dwgs.User` 标出 2 × Ø3.1 孔及 Ø5 圆环参考；孔位/环形并非已完成的 KiCad 钻孔与电气焊盘定义。板厚有 DWG **1.20 mm** 标注。DWG 转换的单位/告警仍需以干净原生 CAD 复核。电池 SKU、触点实现、器件、net、zone 的工程实现和 PCB 到已装配外壳的 fit / 公差验证仍未完成。原理图仅表达架构/信号意图，无 pin-level connectivity。
