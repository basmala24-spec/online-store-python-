from datetime import datetime
class Discount:
    def __init__(self, code, type_, value, min_spend=0):
        self.code = code.upper()
        self.type = type_      # percent / fixed
        self.value = value
        self.min_spend = min_spend
        self.active = True

    def apply(self, total):
        if not self.active:
            return 0

        if total < self.min_spend:
            return 0

        if self.type == "percent":
            return total * self.value / 100

        return min(self.value, total)

class DiscountSystem:
    def __init__(self):
        self.codes = {}
        self._load_defaults()

    def _load_defaults(self):
        self.codes = {
            "WELCOME10": Discount("WELCOME10", "percent", 10),
            "LOYAL20": Discount("LOYAL20", "percent", 20, 200),
            "SAVE50": Discount("SAVE50", "fixed", 50, 300),
            "GROUP10": Discount("GROUP10", "percent", 10),
        }

    def list_discounts(self):
        print("\n=== Available Discounts ===")
        for code, d in self.codes.items():
            kind = f"{d.value}%" if d.type == "percent" else f"{d.value} EGP"
            print(f"{code} -> {kind} | min: {d.min_spend}")

    def apply_code(self, code, total):
        code = code.upper()

        if code not in self.codes:
            return total, 0, "❌ Invalid code"

        discount = self.codes[code]

        if total < discount.min_spend:
            return total, 0, "❌ Minimum spend not reached"

        saved = discount.apply(total)
        final = total - saved

        return final, saved, f"✔ You saved {saved:.2f} EGP"

    def auto_discount(self, total, guests=0):
        saved = 0

        # weekend discount
        if datetime.today().weekday() >= 4:
            saved += total * 0.05

        # group discount
        if guests >= 5:
            saved += total * 0.10

        return saved