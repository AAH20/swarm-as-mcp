FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY swarm_as_mcp/ ./swarm_as_mcp/
COPY tests/ ./tests/

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["swarm-as-mcp"]
CMD ["demo"]
