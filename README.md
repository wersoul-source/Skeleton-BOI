<p align="center"><img src="assets/usa-banner.svg" alt="USA — Universal Structural Signature: adaptive paths, stable responsibilities" width="100%"></p>

# Skeleton-BOI

USA · Universal Structural Signature

**ลายเซ็นโครงสร้างโปรแกรม — เปลี่ยนรูปร่างได้ คงหน้าที่และการทำงานร่วมกัน**

โครงสำเร็จรูปสำหรับให้ Agent ถามผู้ใช้ **5 ข้อ** แล้วสร้างแผนที่โปรแกรม ขอบเขตแต่ละส่วน และเอกสารส่งต่อให้ Dev ทันที รองรับ Web, Desktop, CLI, Service และ Data โดยปรับชื่อแฟ้มให้เหมาะกับระบบได้

USA ใน repository นี้เป็นชื่อแนวทางของโครงการ ไม่ใช่มาตรฐานสากลที่รับรองโดยองค์กรภายนอก และยังไม่ใช่แอปที่รันได้สำเร็จรูป

> โครงสร้างที่ดีต้องไม่แข็ง ต้องปรับตัวเองเข้ากับสภาพระบบได้ แต่ยังคงรูปแบบการทำงานตามโครงสร้างที่วางไว้

## เริ่มใช้งาน

ต้องมี Git และ Python **3.10 ขึ้นไป** ไม่มี dependency เพิ่มเติมสำหรับเครื่องมือสร้างโครง

```sh
git clone https://github.com/wersoul-source/Skeleton-BOI.git
cd Skeleton-BOI
```

หรือกด **Use this template → Create a new repository** บน GitHub เพื่อสร้างสำเนาในบัญชีของคุณ แล้ว clone สำเนานั้น

เปิด coding agent ในโฟลเดอร์นี้ แล้วสั่ง:

```text
อ่าน AGENTS.md และ START_HERE_AGENT.md แล้วเริ่ม workflow USA
เริ่มอ่าน → ถาม 5 ข้อรวมพื้นที่ปลายทาง → ดูตัวอย่าง → clone ไปที่เลือก
ปรับโครงและแผน ใส่เครดิต ตรวจสอบ แล้วถามหน้าตาโปรแกรม
```

Agent ที่อ่านไฟล์อัตโนมัติจะพบคำแนะนำใน AGENTS.md; Agent แบบแชตที่เข้าถึง filesystem ไม่ได้ต้องใช้เครื่องมือ clone/edit เพิ่มเติม การวางไฟล์ Markdown อย่างเดียวไม่ได้ให้สิทธิ์ Agent เข้าถึงเครื่อง

### ลองโครงตัวอย่างโดยไม่ต้องรอ Agent

```sh
python scripts/usa.py init --config examples/desktop.json --output generated/my-desktop
python scripts/usa.py init --config examples/desktop.json --output generated/my-desktop --apply
python scripts/usa.py validate --root generated/my-desktop
python -m unittest discover -s tests -v
```

คำสั่งแรกแสดงรายการก่อนเขียน คำสั่งที่สองสร้างไฟล์ และคำสั่งที่สามตรวจความตรงกันของ mapping/เอกสาร ตัวอย่างเป็นข้อมูลสาธิต ต้องแทนด้วยคำตอบจริงก่อนเริ่มผลิตภัณฑ์

## คำถามตั้งต้น 5 ข้อ

1. **Outcome:** โปรแกรมชื่ออะไร ใครใช้ แก้ปัญหาอะไร และผลสำเร็จวัดอย่างไร?
2. **Surface:** ใช้งานแบบ Web / Desktop / Mobile / CLI / Service / Data บนระบบใด และต้อง offline หรือไม่?
3. **Mechanism:** งานหลัก 3–5 อย่างคืออะไร ข้อมูลเข้า → ขั้นตอน → ผลลัพธ์เป็นอย่างไร และเชื่อมบริการใด?
4. **Constraints:** มี stack/โค้ดเดิม/path ที่ต้องรักษา ข้อมูลอ่อนไหว สิทธิ์ งบ และข้อจำกัดอะไร?
5. **Execution:** ต้องการสร้างในพื้นที่ใด (ระบุ parent path) ใช้ชื่อโฟลเดอร์อะไร ขอบเขตเวอร์ชันแรก สิ่งที่ไม่ทำ วิธีตรวจรับ สภาพแวดล้อมส่งมอบ และ Dev ผู้รับต่อคืออะไร?

ถามเป็นหนึ่งชุด ไม่เพิ่มรอบซักถามโดยอัตโนมัติ ถ้าคำตอบไม่ครบให้บันทึก `unknown` และสมมติฐานอย่างเปิดเผย; ข้อที่จำเป็นต่อการเขียนอย่างปลอดภัยยังไม่ชัด ให้หยุดเฉพาะส่วนที่ขึ้นกับข้อมูลนั้น

## แผนที่โครงสร้าง

![Role map](assets/usa-map.svg)

| หน้าที่คงที่ | ตัวอย่าง Web | ตัวอย่าง Desktop | จุดเชื่อมต่อ |
|---|---|---|---|
| interface | apps/web | desktop/ui | รับ input / ส่ง output |
| application | src/application | desktop/application | use cases และ ports |
| domain | src/domain | desktop/domain | กฎและ invariants |
| infrastructure | src/infrastructure | desktop/adapters | DB / SDK / OS adapters |
| contracts | contracts | contracts | รูปแบบข้อมูลและ interface |
| tests | tests | tests | ตรวจ behavior และ boundaries |
| operations | ops | ops | config / deploy / recovery |
| docs | docs | docs | แผนที่และเหตุผล |

**ชื่อ folder ไม่ใช่สัญญา — หน้าที่และทิศทาง dependency คือสัญญา** ดู [ARCHITECTURE.md](ARCHITECTURE.md) และ [SIGNATURE.md](docs/SIGNATURE.md)

## สิ่งที่อยู่ใน repository

```text
AGENTS.md                  กติกาปฏิบัติงานของ Agent
START_HERE_AGENT.md         clone → understand → edit → validate → handoff
ARCHITECTURE.md             แผนที่ของ template และ generated project
MANIFEST.md                 ลำดับโหลด context และเจ้าของข้อมูล
docs/                      signature, initialization, validation, sources
examples/                  คำตอบสาธิตและ path สำหรับแต่ละ profile
scripts/usa.py             dry-run / สร้างโครง / ตรวจ consistency
tests/test_usa.py           ตรวจ safeguards และ profile
assets/                    ภาพ SVG ต้นฉบับของ USA
.github/workflows/         structural validation CI
```

## ปรับใช้กับโปรแกรมของคุณ

คัดลอก JSON ตัวอย่างที่เหมาะสมไปเป็น config ใหม่ กรอก `answers.q1`–`q5` ตั้ง project slug และเลือก `profile` สามารถ override `paths` เช่น `interface: "window"` ได้ ใช้ path แบบ relative คั่นด้วย `/` เท่านั้น

สำหรับ Mobile ให้เริ่มจาก desktop profile แล้ว map interface ไป `mobile/ui` หรือใช้ layout ของ framework เดิม สำหรับ monorepo ให้เลือกโครงตาม package และลง ADR ก่อนแบ่ง services เพิ่ม ห้ามสร้าง backend/database ถ้างานไม่ต้องใช้

Agent ดูตัวอย่างแล้ว clone ไป **ปลายทางใหม่ที่ผู้ใช้เลือก** จากนั้น generate โครงใน staging แยกต่างหาก ตรวจแล้วนำเข้า clone อย่างมี diff ปรับชื่อ folder, role paths, README.md, AGENTS.md, ARCHITECTURE.md และแผน PLAN.md/SYSTEM_FLOW.md ตามคำตอบจริง พร้อมเครดิตลิงก์ต้นแบบท้ายเอกสาร ดูขั้นตอนครบใน [START_HERE_AGENT.md](START_HERE_AGENT.md)

เมื่อผ่านการตรวจ ให้แจ้ง **“เตรียมโครงสร้างเสร็จแล้ว ต้องการหน้าตาโปรแกรมแบบไหนครับ”** และรอคำตอบก่อนเริ่ม UI

Agent ที่อ่าน AGENTS.md จะเริ่ม workflow นี้ทันที; การเปิดหน้าเว็บ repo อย่างเดียวไม่เรียกใช้ Agent หาก Agent ไม่โหลดไฟล์อัตโนมัติให้ส่งคำสั่งเริ่มด้านบน

## ขอบเขตความปลอดภัยและการตรวจรับ

- ไม่ติดตั้ง package, รันคำสั่งจากคำตอบ, deploy หรือใช้เครือข่ายใน generator
- ปฏิเสธ absolute path, traversal, symlink, role path ซ้อนกัน และไฟล์ที่มีเนื้อหาขัดกัน
- รันซ้ำด้วย config เดิมได้; config เปลี่ยนให้ใช้ output ใหม่และตรวจ diff
- `.env`, credentials และข้อมูลจริงไม่ควร commit; ใช้ตัวอย่างที่ไม่มี secret
- CI ตรวจ generator และตัวอย่างโครง **ไม่ได้พิสูจน์ application, security หรือ production readiness**
- Dev ต้องเพิ่ม build/run, behavior/integration tests และหลักฐาน acceptance ตามคำตอบข้อ 5

อ่าน [VALIDATION.md](docs/VALIDATION.md), [INITIALIZATION.md](docs/INITIALIZATION.md) และ [CONTRIBUTING.md](CONTRIBUTING.md)

## แนวคิดอ้างอิง

นำแนวคิดจาก [AGENTS.md](https://agents.md/), [ARCHITECTURE.md](https://architecture.md/), [ReadMe](https://readme.com/), [Manifest](https://readthemanifest.net/), [AI-First SSOT](https://github.com/artificial-intelligence-first/ssot) และ [MIT CommKit](https://mitcommlab.mit.edu/broad/commkit/file-structure/) มาปรับใช้กับ USA แบบสรุปและเชื่อมแหล่งต้นทาง ดูขอบเขตการศึกษาและ tag ที่ Agent ควรอ่านใน [SOURCES.md](docs/SOURCES.md)

## License

MIT — ใช้ ปรับ และแจกจ่ายได้ตาม [LICENSE](LICENSE) ภาพ SVG เขียนขึ้นสำหรับโครงการนี้ ไม่มี stock asset หรือภาระซื้อ license เพิ่ม

Credit: [Skeleton-BOI](https://github.com/wersoul-source/Skeleton-BOI)
