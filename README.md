# LockPCB — retrofit smart-lock PCB

本仓库是室内免打孔/免新布线改装智能锁的 **PCB 工程工作区**。KiCad 板框已依据设计师确认稿迁入；Agent 的电子架构和机械分区仍是工程草案，不能当作产品批准或制造文件。

## 当前事实源

- **KiCad 编辑源：** [`pcb/LockPCB.kicad_pro`](pcb/LockPCB.kicad_pro)、[`pcb/LockPCB.kicad_sch`](pcb/LockPCB.kicad_sch)、[`pcb/LockPCB.kicad_pcb`](pcb/LockPCB.kicad_pcb)。GitHub 当前工作分支是 [`arena/3b84c22f-lockpcb`](https://github.com/lin2mm/LockPCB/tree/arena/3b84c22f-lockpcb)；不合并 `main`。
- **机械来源、证据等级与待办：** [`docs/MECHANICAL_SOURCE_BASELINE.md`](docs/MECHANICAL_SOURCE_BASELINE.md)。
- **V1 18650 目标与后续尺寸系列策略：** [`docs/PRODUCT_VARIANTS.md`](docs/PRODUCT_VARIANTS.md)。
- **本项目文件命名建议：** [`docs/FILE_NAMING_RULES.md`](docs/FILE_NAMING_RULES.md)。
- 设计决策和其他工程草案在 `decisions/` 与 `docs/`。

## 当前工程状态

**PRE-CAD/PCB engineering skeleton — not fabrication-ready.** 当前 `Edge.Cuts` 是从设计师 DWG 提取的异形板框，标称包络 **14 × 50 mm**；孔位和同心圆仍是图形参考，尚未成为已批准的钻孔、镀层或电气焊盘。没有实际器件、焊盘、网络、覆铜或走线；原理图仅为文字架构/信号意图，不含实际符号引脚连接。板与已装配外壳、电芯、触点和电机/齿轮箱的 fit 与公差均未验证。

- [打开 KiCad PCB 源文件](https://github.com/lin2mm/LockPCB/blob/arena/3b84c22f-lockpcb/pcb/LockPCB.kicad_pcb)
- [打开机械来源基线](https://github.com/lin2mm/LockPCB/blob/arena/3b84c22f-lockpcb/docs/MECHANICAL_SOURCE_BASELINE.md)
- [KiCad CI run 38902175365](https://github.com/lin2mm/LockPCB/actions/runs/38902175365)（通过；软件检查不是装配/电气/制造验证）

不执行固件烧录、采购、PCB 制造或真实硬件测试。未知项保持 TBD；不声称可投板、已 fit 或已完成电气验证。
