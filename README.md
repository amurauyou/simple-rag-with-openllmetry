# Simple RAG pipeline with OpenLLMetry tracing
A sample RAG pipeline built with LlamaIndex and ChromaDB as a vector store auto instrumented with OpenLLMetry

Technologies used:
- Python
- uv
- Docker
- ChromaDB
- LLamaIndex
- OpenAI API
- OpenLLMetry
- Datadog 

## How to Run

### Run ChromaDB and Datadog agent with Docker Compose:

1. Set Datadog API KEY

```
export DD_API_KEY=<my-datadog-api-key>
```
   
2. Run Docker Compose services (daemon mode)
```
docker compose up -d
```

### Run the pipeline

1. Set OpenAI API key

```
export OPENAI_API_KEY=<my-openai-api-key>
```

2. Set OTel backend via TRACELOOP_BASE_URL env var (that'll be picked up by Traceloop SDK)

```
export TRACELOOP_BASE_URL=http://localhost:4318
```

3. Run the pipeline with uv

```
uv run main.py
```
