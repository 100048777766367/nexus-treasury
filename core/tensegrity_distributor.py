import os
import json
import math

STRAIN_FILE = "synapses/tensegrity_strain.json"

STRATA_MEMBERS = [
    "retina", "cochlea", "tactile", "olfactory", "motor",
    "neuron", "monad", "shunya", "seed", "genome", "nexus"
]

class TensegrityDistributor:
    """
    LỚP 2: BỘ PHÂN BỔ CO GIÃN TENSEGRITY
    1. Đo lường lực căng / áp lực thiếu hụt của 11 tầng bản thể.
    2. Dòng dưỡng chất tự động thẩm thấu từ nơi thừa sang nơi căng thẳng nhất.
    """
    @staticmethod
    def measure_strain_and_osmose(available_budget):
        os.makedirs("synapses", exist_ok=True)
        strain_matrix = {}
        
        # Mô phỏng đo áp lực dựa trên nhịp đập sinh học (Stress Index từ 0.1 đến 1.0)
        total_strain = 0.0
        for idx, stratum in enumerate(STRATA_MEMBERS):
            # Các giác quan ngoại vi và cơ bắp thường chịu áp lực lớn nhất
            base_strain = 0.3 + (math.sin(idx * 1.5) * 0.2)
            stress = round(max(0.1, min(1.0, base_strain)), 4)
            strain_matrix[stratum] = stress
            total_strain += stress

        # Tính toán lưu lượng thẩm thấu tương ứng theo tỷ lệ lực căng
        disbursements = {}
        for stratum, stress in strain_matrix.items():
            ratio = stress / total_strain
            amount = round(available_budget * ratio, 4)
            disbursements[stratum] = amount

        with open(STRAIN_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "total_strain_gradient": round(total_strain, 4),
                "strain_matrix": strain_matrix,
                "osmotic_disbursements": disbursements
            }, f, indent=4)

        top_strained = max(strain_matrix, key=strain_matrix.get)
        print(f"🕸️ [TENSEGRITY THẨM THẤU] Tầng căng thẳng nhất: '{top_strained}' (Áp lực: {strain_matrix[top_strained]}). Đã tự động san phẳng áp lực!")
        return disbursements
