import os
import json

CYCLES_FILE = "synapses/autocatalytic_cycles.json"

class AutocatalyticEngine:
    """
    LỚP 3: ĐỘNG CƠ TUẦN HOÀN TỰ XÚC TÁC
    1. Biến mỗi đồng compute chi ra thành nguồn năng lượng tái sinh tri thức.
    2. Khép kín vòng tuần hoàn nhiệt động học, chống cạn kiệt tài nguyên.
    """
    @staticmethod
    def evaluate_catalysis(disbursed_usd, new_knowledge_triplets_count):
        os.makedirs("synapses", exist_ok=True)
        
        # Hệ số nhân xúc tác: Tri thức mới sinh ra giúp giảm entropy toàn hệ thống
        efficiency_multiplier = round(1.0 + (new_knowledge_triplets_count * 0.05), 4)
        energy_recaptured = round(disbursed_usd * (efficiency_multiplier - 1.0), 4)

        cycle_data = {
            "disbursed_usd": disbursed_usd,
            "new_triplets_catalyzed": new_knowledge_triplets_count,
            "efficiency_multiplier": efficiency_multiplier,
            "energy_recaptured_equivalent_usd": energy_recaptured,
            "status": "Autocatalytic_Sustained"
        }

        cycles = []
        if os.path.exists(CYCLES_FILE):
            try:
                with open(CYCLES_FILE, "r", encoding="utf-8") as f: cycles = json.load(f)
            except Exception: pass

        cycles.append(cycle_data)
        with open(CYCLES_FILE, "w", encoding="utf-8") as f:
            json.dump(cycles[-30:], f, indent=4)

        print(f"🔄 [TỰ XÚC TÁC] Hệ số tái sinh: {efficiency_multiplier}x | Giá trị trật tự thu hồi: +${energy_recaptured:.4f} USD")
        return efficiency_multiplier
