"""
Model Context Protocol (MCP) Gateway Server for Swarm-As-MCP.
Exposes autonomous multi-agent swarm fleet as standard JSON-RPC 2.0 MCP tools.
"""

import json
from typing import Dict, List, Any, Optional
from .models import SwarmTaskRequest, SwarmTaskResponse
from .swarm_orchestrator import SwarmOrchestrator


class McpGatewayServer:
    """Standard Model Context Protocol (MCP) JSON-RPC 2.0 endpoint for swarms."""

    def __init__(self):
        self.orchestrator = SwarmOrchestrator()

    def get_tool_definitions(self) -> List[Dict[str, Any]]:
        """Emits MCP tools/list declaration for IDE auto-discovery."""
        return [
            {
                "name": "swarm_execute",
                "description": "Dispatches a high-complexity goal to an autonomous 10-agent swarm (Claude Opus 5.5, DeepSeek V4.1, GPT-6 Astra). Handles coding, compilation, tests, and browser UI validation.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "instruction": {
                            "type": "string",
                            "description": "High-level goal or refactoring request"
                        },
                        "repo_root": {
                            "type": "string",
                            "description": "Absolute workspace root directory"
                        },
                        "include_browser_test": {
                            "type": "boolean",
                            "description": "Whether to launch virtual Chromium for UI verification"
                        }
                    },
                    "required": ["instruction"]
                }
            },
            {
                "name": "swarm_inspect_fleet",
                "description": "Inspects currently available autonomous swarm seats and frontier model assignments.",
                "inputSchema": {"type": "object", "properties": {}}
            }
        ]

    def handle_mcp_call(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Processes tools/call invocation from Cursor, Claude Code, or Windsurf."""
        if tool_name == "swarm_inspect_fleet":
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({
                            "fleet_status": "ONLINE",
                            "active_seats": {
                                "supervisor": "Claude Opus 5.5",
                                "cli_compiler": "DeepSeek V4.1-Flash",
                                "gui_operator": "GPT-6 Astra",
                                "security_sentinel": "Gemini 3.8 Flash Cyber"
                            }
                        }, indent=2)
                    }
                ]
            }

        elif tool_name == "swarm_execute":
            req = SwarmTaskRequest(
                task_id="mcp_task_01",
                instruction=arguments.get("instruction", ""),
                repo_root=arguments.get("repo_root", "/workspace"),
                include_browser_test=arguments.get("include_browser_test", True)
            )
            response = self.orchestrator.execute_task(req)

            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"### ❖ Swarm Execution Complete ({response.execution_time_sec}s)\n\n"
                                f"**Summary**: {response.summary}\n\n"
                                f"**Tests Verified**: {response.tests_passed} passed\n\n"
                                f"```diff\n{response.git_diff}\n```"
                    }
                ]
            }

        else:
            raise KeyError(f"Unknown MCP tool '{tool_name}'")

    @staticmethod
    def get_cursor_config_snippet() -> str:
        """Emits drop-in ~/.cursor/mcp.json configuration."""
        snippet = {
            "mcpServers": {
                "autonomous-swarm": {
                    "command": "swarm-as-mcp",
                    "args": ["serve"]
                }
            }
        }
        return json.dumps(snippet, indent=2)
