# Initialization contract

READ → ASK_FIVE → WAIT_ANSWERS → REVIEW_EXAMPLES → CLONE_TO_SELECTED_DESTINATION → ADAPT → VALIDATE → STRUCTURE_READY → ASK_APPEARANCE → WAIT_UI_ANSWER

Canonical workflow อยู่ใน START_HERE_AGENT.md; README สรุป 5 คำถาม; AGENTS.md ให้เริ่มทันทีเมื่อ Agent อ่าน repo เพื่อสร้างโครงการ

- ห้ามเขียนปลายทางก่อนผู้ใช้เลือก parent path/ชื่อ folder
- usa.project.json หมายถึงตั้งต้นแล้ว ไม่ถาม/clone ซ้ำ
- clone ไป final destination ใหม่ก่อนปรับ; generate ใน staging และ merge template files ด้วย diff
- รักษางานผู้ใช้ history และ LICENSE; ไม่ push ต้นแบบ
- ต้องมีแผนล่วงหน้า PLAN.md, SYSTEM_FLOW.md, map และ Credit
- หลัง validation ถาม “เตรียมโครงสร้างเสร็จแล้ว ต้องการหน้าตาโปรแกรมแบบไหนครับ” แล้วรอ

Config: exactly project (lowercase slug), profile (web/desktop/cli/service/data), answers (q1–q5 nonempty strings), paths (known role overrides). ใส่พื้นที่/ชื่อ folder ใน q5 เป็น planning text ไม่ใช่ executable code. Role paths เป็น relative portable ASCII; เนื้อหาไทยรองรับ

Unknown ยอมรับสำหรับแผน แต่ไม่ใช่ข้อเท็จจริงหรือสิทธิ์เข้าถึง งานดูแล Skeleton-BOI ไม่เริ่ม questionnaire ใหม่ เปลี่ยน config ใช้ staging ใหม่และ review migration

Credit: [Skeleton-BOI](https://github.com/wersoul-source/Skeleton-BOI)
