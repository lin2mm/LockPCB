# 项目启动简报

## 固定事实（本项目约束）

- 目标：室内改装式、免打孔/免布线、极限小型化的“火柴盒门锁”；结构简单是核心卖点。
- 电源：单节 1S 锂电。早期产品简述写 18650；设计师确认的工厂功能 TXT 写 18500，STEP 中 `DC-18650-SX` 网格约 18 × 18 × 50 mm，支持 18500 尺寸级。实物样机/BOM 确认前，最终电芯 SKU 仍未关闭。
- 总体概念：电池仓与长条 PCB 并列；电机、减速齿轮和联轴器位于顶部。
- BLE 为主；NFC、键盘、指纹、Wi-Fi 是可选模块/子板，尚未定接口/实现。
- 此阶段只做 PCB 工程；不做固件烧录、打样、下单或真实硬件测试。
- KiCad 源文件为 source of truth；Gerber 是后续导出物。
- 未知尺寸、封装和电气参数必须保持 TBD/placeholder；不得据此宣称可投板。

## 结构化启动基线

- `Edge.Cuts` 已按设计师确认稿转换的 DWG 轮廓迁入 **14 × 50 mm** 异形外形，孔位参考在 (7,10) 与 (7,47) mm；DWG 标注 1.20 mm 板厚。DXF 转换有告警且单位头为 inch，需在制造前以原生 mm CAD 复核。`PCB_MAX_OUTLINE` 标记该 14 × 50 mm 来源包络；旧 17.5 × 60 / 20 × 65 mm Agent 测试值已废止，不作为产品几何。当前仍未验证与已组装外壳的 PCB fit / tolerance。
- 板框通过 KiCad `Edge.Cuts` 绘出；同时在 `User.3` 标注 `PCB_MAX_OUTLINE`。
- 机械区用 KiCad `User.1` 至 `User.9` 独立用户图层表达，并以层内文字标出规定名称；另以 `Edge.Cuts` 表示板框。它们是 PCB 文件中的真实可编辑 KiCad 图形对象，不是截图或外部示意图。`NO_COMPONENT_ZONE` 另有一块 F/B 铜层的 KiCad 原生 keepout，占位范围与 `User.9` 对应；这是未验证的临时规则，不代表已确定最终禁布尺寸。其余区（尤其电池仓区）为机械边界图示，不能当成板内电气 keepout。

| KiCad 图层 | 图层标注 |
|---|---|
| `User.1` | `BATTERY_KEEP_OUT` |
| `User.2` | `BATTERY_CONTACT_ZONE` |
| `User.3` | `PCB_MAX_OUTLINE` |
| `User.4` | `MOTOR_GEARBOX_ZONE` |
| `User.5` | `SHAFT_AXIS` |
| `User.6` | `NFC_ANTENNA_ZONE` |
| `User.7` | `METAL_LOCKBODY_ZONE` |
| `User.8` | `SERVICE_ACCESS_ZONE` |
| `User.9` | `NO_COMPONENT_ZONE` |
- 当前板上不放置器件、焊盘、铜皮、网络或走线；没有原理图/电路设计。KiCad PCB 当前按 4 层软偏好建立 F.Cu/In1.Cu/In2.Cu/B.Cu 脚手架；这不是最终层数/叠层批准。板厚、铜厚、材料仍 TBD。KiCad schematic 现在是可编辑的文字架构/信号意图草案，无电气符号引脚和真实连接。
- 电池真实尺寸、接触形式、齿轮/电机尺寸、轴线基准、锁体内部空间、天线距离等输入均待确认。

## 验收标准

1. 仓库中存在 KiCad 工程与 PCB 文件；`Edge.Cuts` 是按确认 DWG 转入的 source-derived 轮廓，仍须 native-CAD/fit 验证。
2. PCB 有独立机械用户图层并分别明确表达：`BATTERY_KEEP_OUT`、`BATTERY_CONTACT_ZONE`、`PCB_MAX_OUTLINE`、`MOTOR_GEARBOX_ZONE`、`SHAFT_AXIS`、`NFC_ANTENNA_ZONE`、`METAL_LOCKBODY_ZONE`、`SERVICE_ACCESS_ZONE`、`NO_COMPONENT_ZONE`。
3. 所有未确认信息均清楚标记 TBD/placeholder；不将示意尺寸包装成最终规格。
4. BOM、DRC、制造文件和投板准备状态不虚报；机械尺寸和电机数据缺失时明确标注不可投板。
5. 每轮自然语言决策更新 `DESIGN_DECISIONS.md`，并保留开放项，不替用户臆定产品需求。

## 当前推荐实现（软偏好 / 待验证）

- 首轮采用纵向单板、4 层叠层脚手架；单板优先，极限尺寸不允许时再比较顶部电机小板或外围子板。
- 低压有刷减速电机尽量用 1S VBAT 经 H-bridge 驱动；独立 3.3 V Buck-Boost 供 BLE/逻辑。所有 MPN 与额定/峰值参数 TBD。
- BLE 核心优先，评估认证 nRF52840 模块；DRV8213 类电机驱动与 ATECC608C 类安全元件仅是 BOM 候选。
- 电机电流区与 RF/天线区域尽量在板上分离；当前 KiCad 功能区边界为说明性占位，不等于经验证间距/布局。
- 功耗预算以公式表达，实测/数据表数值待输入。详见 [`POWER_TREE_AND_BUDGET.md`](POWER_TREE_AND_BUDGET.md)、[`CORE_ZONING.md`](CORE_ZONING.md)、`BOM_DRAFT.csv`、`PINOUT_DRAFT.csv`、`NETLIST_DRAFT.csv`。

## 后续自然语言决策

优先用实际电池/电池仓、可用外形、锁体金属结构及电机/齿轮数据减少返工。Agent 对软偏好方案比较并推荐；遇到器件/尺寸/充电等开放决策先以可追溯 placeholder 推进，只对用户列出的六类真正阻塞输入征求确认。
