import spacy
import requests
from typing import List, Dict

class EntityExtractor:
    def __init__(self, model_name="en_core_sci_sm", bioportal_api_key=None):
        self.nlp = spacy.load(model_name)
        self.bioportal_api_key = bioportal_api_key  # Get free from bioportal.bioontology.org

    def extract_entities(self, text: str) -> List[Dict]:
        doc = self.nlp(text)
        entities = []
        for ent in doc.ents:
            node_type = self._map_label(ent.label_)
            ontology_id = self._link_entity(ent.text, node_type)
            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "node_type": node_type,
                "ontology_id": ontology_id,
                "start": ent.start_char,
                "end": ent.end_char
            })
        return entities

    def _map_label(self, label: str) -> str:
        mapping = {"GENE": "Gene", "CHEMICAL": "Drug", "DISEASE": "Disease", "PHENOTYPE": "Phenotype"}
        return mapping.get(label, "Unknown")

    def _link_entity(self, text: str, node_type: str) -> str:
        if not self.bioportal_api_key:
            return "UNKNOWN"
        # Placeholder: implement BioPortal call if needed
        return "MONDO:0004975"