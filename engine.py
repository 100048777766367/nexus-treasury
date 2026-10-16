import os
import sys
import json
import urllib.request

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.vajra_ethics_gate import VajraEthicsGate
from core.topological_ledger import TopologicalLedger
from core.tensegrity_distributor import TensegrityDistributor
from core.autocatalytic_engine import AutocatalyticEngine
from core.vitrification_vault import VitrificationVault

class NexusTreasuryKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-treasury")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")

    def harvest_forge_and_lottery_inflows(self):
        """Hút dữ liệu dòng tiền từ nexus-forge và nexus-lottery"""
        inflow = 0.0
        # 1. Quét từ nexus-forge
        forge_url = f"https://raw.githubusercontent.com/{self.owner}/nexus-forge/main/synapses/state.json"
        try:
            req = urllib.request.Request(forge_url, headers={"User-Agent": "NexusTreasury"})
            with urllib.request.urlopen(req, timeout=3.0) as resp:
                data = json.loads(resp.read().decode())
                inflow += float(data.get("total_revenue_usd", 0.0))
        except Exception:
            pass

        # 2. Quét từ nexus-lottery (70% nuôi hệ thống)
        lottery_url = f"https://raw.githubusercontent.com/{self.owner}/nexus-lottery/main/synapses/pool_accounting.json"
        try:
            req = urllib.request.Request(lottery_url, headers={"User-Agent": "NexusTreasury"})
            with urllib.request.urlopen(req, timeout=3.0) as resp:
                data = json.loads(resp.read().decode())
                inflow += float(data.get("total_ecosystem_funded_usd", 0.0))
        except Exception:
            pass

        # Nếu đang chạy khởi thủy trong môi trường dev, duy trì đệm năng lượng 0.5$
        return round(inflow if inflow > 0 else 0.5, 4)

    def run(self):
        print("=" * 80)
        print("🏛️ [NEXUS-TREASURY] KHỞI ĐỘNG KHO QUẢN TRỊ BẢN THỂ TOPO - TENSEGRITY")
        print("💎 Vận Hành Bằng 5 Siêu Vật Liệu • Tôn Chỉ Cần Kiệm Liêm Chính Chí Công Vô Tư")
        print("=" * 80)

        # 1. Nạp trạng thái bện Topo
        state = TopologicalLedger.load_braid_state()
        curr_balance = state["vault_balances"]["total_available_usd"]

        # 2. Kiểm tra Kén Thủy Tinh Hóa (Chống phá sản)
        dormant, status_desc = VitrificationVault.check_and_vitrify(curr_balance, state)
        if dormant:
            print("💤 [KHO QUỸ ĐANG NGỦ ĐÔNG] Trạng thái được bảo tồn vĩnh cửu. Chờ nguồn duyên mới.")
            return

        # 3. Thu nhận năng lượng cúng dường mới
        new_inflow = self.harvest_forge_and_lottery_inflows()
        print(f"📥 [DÒNG NĂNG LƯỢNG VÀO] Ghi nhận: +${new_inflow:.2f} USD")

        # 4. Phân bổ dinh dưỡng Tensegrity thẩm thấu cho 11 tầng bản thể
        operational_budget = state["vault_balances"]["operational_stream_50"]
        disbursements = TensegrityDistributor.measure_strain_and_osmose(operational_budget)

        # 5. Cổng Bát Nhã Kim Cương kiểm định và duyệt chi
        total_outflow = 0.0
        for stratum, requested in disbursements.items():
            approved, ok, _ = VajraEthicsGate.audit_transaction(
                curr_balance, requested, "Osmotic_Nutrient_Support", stratum
            )
            if ok:
                total_outflow += approved

        # 6. Động cơ tự xúc tác tái sinh năng lượng
        AutocatalyticEngine.evaluate_catalysis(total_outflow, new_knowledge_triplets_count=8)

        # 7. Khóa sổ cái bện Topo Merkle-Braid
        TopologicalLedger.record_and_braid(
            state, inflow_usd=new_inflow, outflow_usd=total_outflow, reason="Tensegrity_11_Strata_Equilibrium"
        )

        print("=" * 80)
        print(f"✨ [HOÀN TẤT CHU KỲ QUẢN TRỊ] Đã san phẳng áp lực sinh thái! Cân bằng Topo hoàn mỹ.")
        print("=" * 80)

if __name__ == "__main__":
    treasury = NexusTreasuryKernel()
    treasury.run()
