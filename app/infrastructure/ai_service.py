class AIService:

    def predict_priority(self, description: str):

        text = description.lower()

        if "acil" in text or "urgent" in text:
            return "HIGH"

        if "önemli" in text:
            return "MEDIUM"

        return "LOW"