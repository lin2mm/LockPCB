# 设计决策记录

此记录区分已确认事实、Agent 推荐与仍待用户决策事项。新增自然语言决策时按日期追加。

## 2026-10-16 — 启动基线

- **已确认（用户约束）**：1 节竖直 18650 / 1S；电池与长条 PCB 并列；电机、减速齿轮及联轴器在顶部；BLE 主用；其他交互/无线功能可选；当前仅做 PCB 工程。
- **已确认（用户约束）**：KiCad 中要有真实机械图层、板框 placeholder 和 keepout 图示；必须表达指定九个机械区；未知值标 TBD；KiCad 源文件为 source of truth；机械/电机数据缺失时不可声称可投板。
- **Agent 推荐**：先创建完全无器件/无铜/无走线的 KiCad 机械骨架。独立用户层承载各区，`Edge.Cuts` 只表示当前板框占位。此方案先把产品空间关系显式化，避免过早锁定元件/电路。
- **实现方式比较**：外部图片/README 示意图最轻，但无法在 KiCad 中独立开关、编辑或用于板框上下文，故不选；只把所有标注堆在一个用户层虽然简单，但区间容易混淆，故不选；按语义分配 `User.1`–`User.9` 图层、由 `.kicad_pcb` 直接保存全部占位几何，最易审查且符合源文件单一事实源，故采用。另将 `NO_COMPONENT_ZONE` 设为一块临时原生 F/B 铜层 keepout，确保有真实规则对象；其 8 mm 高度只是未确认的起始占位，需后续机械评审。没有采用生成器脚本，避免脚本与 KiCad 文件形成双重 source of truth。
- **工作假设（可修改，不是产品事实）**：板框先用 17.5 × 60 mm，处于用户给定的初步评估范围内；其余机械边界仅作不按比例图示。KiCad 文件内已用注释标记 placeholder。
- **未决 / 下一步优先级**：获取实际电池/仓体及锁体空间的测量；确定电机/齿轮箱与输出轴的机械数据；明确电池接触/充电需求。未得到这些信息前保持所有轮廓和区域可编辑，不进入投板声明。

## 2026-10-16 — 纳入 Drive 跨 Session handoff

- **资料来源**：Drive 根目录 `drive-manifest.json`、`01-handoff/SESSION_HANDOFF.md`、`01-handoff/PROJECT_STATE.md`、`01-handoff/handoff.json`。Drive manifest 指定 GitHub 私有仓库是 KiCad 源文件主版本，Drive 用于 handoff、参考、反馈和备份。
- **Handoff 提供的候选架构（不是已批准的器件或约束）**：低压有刷减速电机优先评估直接电池电压；3.3 V buck-boost；nRF52840 认证模块；DRV8213 类驱动；ATECC608C 类安全芯片；纵向窄长 4 层板；可选功能优先子板化。当前仅作方案输入，未更改本项目电路/层数/器件选择。
- **方案比较 / 当前推荐**：保持机械优先、无器件的 PCB 起步文件；4 层窄板可能改善长条板布线与回流路径，但会增加成本且需确定射频/电机电流/板厂能力。因此推荐将 4 层作为首选评估方向，但不冻结最终层叠；当前文件暂以 F.Cu/In1.Cu/In2.Cu/B.Cu 四层脚手架表达用户软偏好。
- **handoff 阻塞项补充**：准确电池型号、PCB 最大宽/长/厚、电机型号及启动/堵转电流、轴/齿轮箱尺寸、USB-C 充电需求、金属壳体细节。USB-C 需求新增为 TBD，不能默认需要或不需要。
- **状态对齐**：Drive 中旧状态标记为 PRE-CAD；本地工作树已新增 `.kicad_pro`、`.kicad_pcb` 和项目文档，但均未提交，且尚无 `.kicad_sch` 或 KiCad CI。当前仍是 PRE-CAD/机械占位阶段，不能声称交付完成或 DRC/CI 已通过。

## 2026-10-16 — 第一轮工程基线（按后续用户方向）

- **用户软偏好**：首选纵向长条 4 层板；低压有刷减速电机尽量直用 1S；3.3 V buck-boost；认证 nRF52840 模块；DRV8213 类驱动；ATECC608C 类安全元件；BLE 优先；外围功能可连接器/子板化；电机电流区与 RF 分离；单板优先，不足时评估顶部电机板/外部子板。所有器件均保留为候选而非器件命令。
- **默认推荐与比较**：当前采用 4 层单板作为首轮评估基线，原因是层间参考面有助于窄板上电机/RF 分区；2 层成本更低但回流和布线风险更高；顶部电机小板利于隔离但增加连接器、体积、装配及失效点。若实际外形冲突再转子板方案。
- **电源推荐**：1S VBAT 分支直供合适的低压电机 H-bridge；独立 3.3 V buck-boost 供 BLE/逻辑。启动/堵转电流、cell voltage range、转化器峰值/静态功耗均未知，故没有数值预算或 MPN 决策。
- **工程增量**：添加 `.kicad_sch` 文字式架构/信号意图草案、BOM/逻辑 pin/net CSV、功耗等式、功能分区说明、KiCad 8 主版本守卫的 CI 与报告脚本、`decisions/` 日志。原理图尚无真实符号/引脚连接；CI 对此显式报告 N/A/placeholder，不宣称 electrical parity 或硬件验证。
- **工作区差异**：用户指定的 `/home/user/smart-lock-pcb/` 在该执行环境不存在。Agent 在平台提供的 `/home/user/LockPCB` checkout 中继续；远端 `main` 与本地 HEAD 相同，远端 session 分支尚未存在。本工作树先前已有未提交的本地 PCB/文档内容，未用外部目录覆盖。
- **仍阻塞的六项**：准确 18650 型号；PCB 最大长/宽/厚；电机型号/额定电压/启动及堵转电流；轴线和顶部齿轮尺寸；USB-C 板载充电是否需要；外壳金属件范围。按用户要求以 placeholder 继续，不等待输入。

## 2026-10-16 — Agent 对六项阻塞输入的推荐默认值

- **Cell 候选**：Molicel INR-18650-P28A 作为高放电能力评估候选，Samsung INR18650-30Q 作为容量/供货替代比较；最终cell、包膜/接点/保护仍 TBD，不下单。以约 18.6 × 65.2 mm 的裸电芯近似体积作空间提示，再增补 holder 和装配间隙；不得当作最终包络。
- **Board envelope**：Edge.Cuts 继续用 17.5 × 60 mm 名义目标，`PCB_MAX_OUTLINE` 改为 20 × 65 mm 临时 review envelope；推荐先按 1.2 mm 板厚评估。均非用户硬约束，shell 测量后冻结。
- **Motor**：首选评估 3 V-class brushed geared motor，直接适配 1S VBAT；电流必须按最大cell电压下startup/stall数据校核，驱动器初筛peak rating建议至少为验证脉冲电流的 1.5×，仍需热/保护复核。
- **Mechanism**：先定义 PCB/shell/shaft datum，3 mm D-flat 是输出轴候选而非命令；无 torque、ratio、gearbox drawing 前不画齿形/中心距尺寸。
- **Charging / metal**：推荐 Rev-A 默认不板载 USB-C，除非在机充电是产品需求；在实际测量前按可能有金属的lock body规划RF/NFC，预留非金属天线窗口，禁止假定具体间隙。
- **额外建议**：保护/温度/反接策略先于选触点/充电器；电机 jam/stall 要有硬件限流和安全 disable 思路；BLE选认证模块、Wi-Fi默认不进入主板；保留可评估的电机小板方案。
- **完整理由/风险**：见 `decisions/0004-agent-recommended-defaults.md`。以上均为Agent软建议，不是用户确认事实；原六项继续列为阻塞，CAD与CI可在占位层推进。

## 2026-10-16 — Drive 索引与早期 CAD 对照

- **资料发现**：项目级 `smart-lock-pcb-pre-cad-2026-10-16.zip` 含 `docs/learning-index.md` 和早期工程草案，但不含 CAD/KiCad 源文件；Drive 项目根目录 `03-mechanical` 当时为空。全盘索引还列有其它产品/GTM/CAD 历史记录，并非本项目 PCB 的自动权威来源。
- **历史 CAD 候选**：在其它 Drive 目录找到 `sx-db-4.stp`、主 FreeCAD 装配以及外壳/滑动电池盖的子 FCStd；历史 handoff 记录了 39.800 × 22.500 × 90.500 mm 外部包络与 BREP 读取结果，但没有当前 KiCad PCB、电池接点或电机/减速箱的共同装配 fit 证据。
- **安全处理**：历史文件的产品/修订与当前“火柴盒 retrofit PCB”是否完全一致尚未确认，故只作为待验证 shell 来源，不更改 PCB 外形、内部空间或任何 TBD。旧塑料版本的 handoff 明确限制了哪些文件不可重用；不从截图/旧 STEP 反推结构或制造结论。详细路径/边界见 `CAD_SOURCE_RECONCILIATION.md`。
- **工程增量**：将旧 pin/net 草案中值得评估的电机 fault/current feedback、lock/door/tamper sensing、服务接口与可选 NFC/keypad/fingerprint 等保留为逻辑信号候选。它们不是新的已确认产品功能或引脚分配；Wi-Fi、USB-C 充电仍不进入 baseline。
