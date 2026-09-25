"""
Swarm-As-MCP: Universal Multi-Agent Swarm Exposer for Cursor, Windsurf, and Claude Code.
Exposes autonomous multi-agent engineering fleets as a single native Model Context Protocol (MCP) server.
"""

from .models import (
    SwarmStage,
    SwarmTaskRequest,
    SwarmProgressEvent,
    SwarmTaskResponse,
)
from .swarm_orchestrator import SwarmOrchestrator
from .mcp_gateway_server import McpGatewayServer

__version__ = "1.0.0"
__all__ = [
    "SwarmStage",
    "SwarmTaskRequest",
    "SwarmProgressEvent",
    "SwarmTaskResponse",
    "SwarmOrchestrator",
    "McpGatewayServer",
]
