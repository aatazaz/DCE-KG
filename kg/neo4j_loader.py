from neo4j import GraphDatabase

class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def create_indexes(self):
        with self.driver.session() as session:
            session.run("CREATE INDEX IF NOT EXISTS FOR (d:Disease) ON (d.mondo_id)")
            session.run("CREATE INDEX IF NOT EXISTS FOR (g:Gene) ON (g.ncbi_gene_id)")
            session.run("CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.drugbank_id)")

    def add_node(self, node_type, attributes):
        with self.driver.session() as session:
            query = f"MERGE (n:{node_type} {{id: $id}}) SET n += $attributes"
            session.run(query, id=attributes.get("id"), attributes=attributes)

    def add_edge(self, from_id, to_id, rel_type, attributes):
        with self.driver.session() as session:
            query = """
            MATCH (a {id: $from_id})
            MATCH (b {id: $to_id})
            MERGE (a)-[r:RELATION {type: $rel_type}]->(b)
            SET r += $attributes
            """
            session.run(query, from_id=from_id, to_id=to_id, rel_type=rel_type, attributes=attributes)