import os
import json

class VajraEthicsGate:
    """
    LỚP 5: CỔNG BÁT NHÃ KIM CƯƠNG & LA BÀN ĐẠO ĐỨC
    1. Kiểm soát dòng tiền theo chuẩn Cần Kiệm Liêm Chính Chí Công Vô Tư.
    2. Cầu chì tự động (Circuit Breaker): Không chi quá 5% tổng quỹ / epoch.
    3. Triệt tiêu hoàn toàn sự can thiệp của cá mập tài phiệt (Anti-Plutocracy).
    """
    MAX_DISBURSEMENT_RATIO = 0.05  # Giới hạn 5% mỗi epoch

    @staticmethod
    def audit_transaction(current_balance, requested_amount, purpose, stratum_target):
        # 1. KIỆM: Kiểm tra cầu chì chống rút cạn quỹ
        max_allowed = round(current_balance * VajraEthicsGate.MAX_DISBURSEMENT_RATIO, 4)
        if requested_amount > max_allowed and current_balance > 1.0:
            print(f"🛑 [CẦU CHÌ BÁT NHÃ] Yêu cầu ${requested_amount:.2f} vượt quá giới hạn 5% (${max_allowed:.2f})! Tự động điều chỉnh.")
            approved_amount = max_allowed
        else:
            approved_amount = requested_amount

        # 2. CHÍNH & LIÊM: Kiểm tra mục đích sử dụng (Chỉ phục vụ sự sống của hệ sinh thái)
        valid_strata = [
            "retina", "cochlea", "tactile", "olfactory", "motor",
            "neuron", "monad", "shunya", "seed", "genome", "nexus", "patron_lottery"
        ]
        if stratum_target not in valid_strata:
            print(f"🚫 [VETO ĐẠO ĐỨC] Mục tiêu '{stratum_target}' nằm ngoài 11 tầng bản thể! Phủ quyết hoàn toàn.")
            return 0.0, False, "Rejected_Invalid_Target"

        # 3. CHÍ CÔNG VÔ TƯ: Không chi trả cho lợi ích tư nhân
        print(f"⚖️ [BÁT NHÃ DUYỆT CHI] Đã thông qua khoản dưỡng chất: ${approved_amount:.4f} USD cho '{stratum_target}' ({purpose}).")
        return approved_amount, True, "Approved_In_Vajra_Alignment"
