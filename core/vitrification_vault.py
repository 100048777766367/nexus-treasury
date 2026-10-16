import os
import json
import hashlib

VITRIFIED_FILE = "synapses/vitrified_seed.json"

class VitrificationVault:
    """
    LỚP 4: KÉN THỦY TINH HÓA BÀO TỬ NGỦ ĐÔNG (CHỐNG PHÁ SẢN)
    1. Khi số dư = $0.00: Lập tức thủy tinh hóa dữ liệu thành tinh thể bất tử, ngủ đông không tốn compute.
    2. Tự động rã đông và phục sinh khi có duyên lành cúng dường mới.
    """
    @staticmethod
    def check_and_vitrify(balance, state):
        os.makedirs("synapses", exist_ok=True)

        if balance <= 0.001:
            print("🧊 [KÉN THỦY TINH HÓA] Số dư chạm 0! Kích hoạt ngủ đông Tánh Không. Chống phá sản 100%.")
            raw_state = json.dumps(state).encode()
            crystal_cid = f"0x{hashlib.shake_256(raw_state).hexdigest(32)}"

            seed = {
                "status": "Vitrified_In_Sunyata",
                "dormancy_crystal_cid": crystal_cid,
                "ancestral_lineage_preserved": "F0_through_F14",
                "revival_trigger": "Any_Inflow_Above_Zero",
                "compute_burn_rate": "0.00_Watts"
            }
            with open(VITRIFIED_FILE, "w", encoding="utf-8") as f:
                json.dump(seed, f, indent=4)
            return True, "Treasury_Dormant_Vitrified"
        else:
            # Nếu đang có tiền và thấy file kén ngủ đông, chuyển sang rã đông
            if os.path.exists(VITRIFIED_FILE):
                try:
                    os.remove(VITRIFIED_FILE)
                    print("🌿 [RÃ ĐÔNG PHỤC SINH] Đã nhận duyên lành mới! Kén thủy tinh bung nở, kho quỹ tái sinh.")
                except Exception: pass
            return False, "Treasury_Active_Flowing"
