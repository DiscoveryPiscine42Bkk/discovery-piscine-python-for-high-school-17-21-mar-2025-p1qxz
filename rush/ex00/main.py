#!/bin/python3
def ตำแหน่งรอบตัว(king_pos):
    x, y = king_pos
    moves = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),             (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    return [(i, j) for i, j in moves if 0 <= i < 8 and 0 <= j < 8]

def เส้นทางระหว่าง(start, end):
    path = []
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    step_x = (dx > 0) - (dx < 0)
    step_y = (dy > 0) - (dy < 0)
    current_x = x1 + step_x
    current_y = y1 + step_y
    while (current_x, current_y) != (x2, y2):
        path.append((current_x, current_y))
        current_x += step_x
        current_y += step_y
    return path

def ตรวจสอบรุก(king_pos, attackers, all_attacks, defenders):
    print(f"ตำแหน่งกษัตริย์: {king_pos}")
    print(f"ฝ่ายตรงข้ามที่โจมตีอยู่: {attackers}")
    
    # ตรวจสอบว่ากษัตริย์มีทางหนีมั้ย
    for move in ตำแหน่งรอบตัว(king_pos):
        if move not in all_attacks and move not in defenders:
            print(f"กษัตริย์หนีไปที่ {move} ได้!")
            return "Check แต่ยังมีทางหนี!"
    
    # ตรวจสอบว่ามีตัวช่วยบังได้มั้ย
    for attacker in attackers:
        if attacker['type'] in ['rook', 'bishop', 'queen']:
            blocks = เส้นทางระหว่าง(attacker['pos'], king_pos)
            for block_pos in blocks:
                if block_pos in defenders:
                    print(f"มีตัวช่วยบังที่ {block_pos}!")
                    return "Check แต่มีตัวช่วยบัง!"
    
    # ตรวจสอบว่ามีตัวช่วยกิน attacker ได้มั้ย
    for attacker in attackers:
        if attacker['pos'] in defenders:
            print(f"มีตัวช่วยกิน attacker ที่ {attacker['pos']}!")
            return "Check แต่มีตัวช่วยกิน!"
    
    # ถ้าทำอะไรไม่ได้เลย
    print("Checkmate! ไม่มีทางหนี ไม่มีตัวช่วยบัง ไม่มีตัวช่วยกิน")
    return "Checkmate!"

# เริ่มจำลองข้อมูล
king_position = (4, 4)

# ฝ่ายตรงข้ามที่โจมตีอยู่
attackers = [
    {'type': 'rook', 'pos': (4, 0)},   # โจมตีแนวนอน
]

# ตำแหน่งทั้งหมดที่ฝ่ายตรงข้ามโจมตี
all_attacks = [
    (4, 3), (4, 2), (4, 1), (4, 0),  # โดนโจมตีในแนวเดียวกัน
    (3, 4), (5, 4),  # สมมติว่ามีตัวอื่นโจมตีจากข้าง ๆ
]

# ตำแหน่งหมากฝ่ายเราเองที่สามารถช่วยได้
defenders = [
    (4, 3),   # ตัวช่วยบังระหว่าง attacker กับ king
    (2, 2),   # ตัวอื่น (อาจไม่ช่วยอะไร)
]

# ตรวจสอบสถานการณ์
สถานะ = ตรวจสอบรุก(king_position, attackers, all_attacks, defenders)
print(f"\nผลลัพธ์: {สถานะ}")
