CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS embeddings (
  id SERIAL PRIMARY KEY,
  login text NOT NULL UNIQUE,
  embedding vector(512) NOT NULL UNIQUE,
  created_at timestamptz DEFAULT now()
);
