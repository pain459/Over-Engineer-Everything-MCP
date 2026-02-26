# server.py
import json
import logging
import sys
from datetime import datetime
from typing import Any

from mcp.server.fastmcp import FastMCP

# IMPORTANT for stdio servers: log to stderr, never stdout
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

mcp = FastMCP("overengineer-everything")


@mcp.tool()
def overengineer(idea: str) -> str:
    """
    Turn a simple idea into an absurdly over-engineered system design.

    Args:
        idea: The simple thing you want to do (e.g., "make tea", "water plants").
    """
    # A deliberately ridiculous architecture generator (deterministic-ish but fun)
    services = [
        "gateway-service",
        "orchestrator-service",
        "policy-service",
        "telemetry-service",
        "audit-service",
        "ml-insights-service",
    ]
    events = [
        "IdeaReceived",
        "PlanGenerated",
        "DependencyResolved",
        "ExecutionSimulated",
        "PostmortemPublished",
    ]

    payload: dict[str, Any] = {
        "input": idea,
        "vision": f"Enterprise-grade {idea} platform (multi-tenant, globally distributed).",
        "layers": [
            "Presentation Layer",
            "Application Orchestration Layer",
            "Domain Layer",
            "Infrastructure Layer",
            "Observability & Governance Layer",
        ],
        "microservices": services,
        "event_bus": {
            "type": "Kafka (because of course)",
            "events": events,
            "guarantees": "Exactly-once-ish (hand-wavy)",
        },
        "data": {
            "primary_db": "PostgreSQL (core truth)",
            "cache": "Redis (because latency)",
            "warehouse": "Iceberg (because analytics)",
            "feature_store": "Feast (because ML)",
        },
        "kubernetes": {
            "namespaces": ["prod", "staging", "dev", "tea-lab"],
            "deployment": "Helm + GitOps",
            "autoscaling": "HPA on 'steam_rate' metric",
            "secrets": "External Secrets + Vault (naturally)",
        },
        "slo": {
            "availability": "99.99%",
            "p95_latency": "42ms",
            "error_budget_policy": "Freeze innovation when budget burns",
        },
        "risk_register": [
            "Overfitting tea flavor model to a single mug",
            "Distributed tracing becomes the product",
            "Incident response team required for kettle upgrades",
        ],
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }

    # Return as a string; clients/hosts can render it nicely.
    return json.dumps(payload, indent=2)


def main() -> None:
    # Official docs show the simplest run path:
    mcp.run(transport="stdio")  # stdio is the default for desktop/tool hosts :contentReference[oaicite:2]{index=2}


if __name__ == "__main__":
    main()