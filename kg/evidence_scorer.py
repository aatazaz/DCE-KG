from collections import defaultdict

class EvidenceScorer:
    def __init__(self):
        self.triple_support = defaultdict(int)
        self.triple_total = defaultdict(int)

    def add_observation(self, triple, is_supporting=True):
        key = (triple[0], triple[1], triple[2])
        self.triple_total[key] += 1
        if is_supporting:
            self.triple_support[key] += 1

    def compute_score(self, triple):
        key = (triple[0], triple[1], triple[2])
        if self.triple_total[key] == 0:
            return 0.0
        return self.triple_support[key] / self.triple_total[key]