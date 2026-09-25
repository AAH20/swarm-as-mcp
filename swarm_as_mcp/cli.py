"""
CLI & IDE Simulation for Swarm-As-MCP.
"""

import sys
import json
from .models import SwarmTaskRequest, SwarmProgressEvent
from .mcp_gateway_server import McpGatewayServer
from .swarm_orchestrator import SwarmOrchestrator


def run_demo() -> None:
    print("\n" + "=" * 70)
    print("❖ SWARM-AS-MCP: UNIVERSAL MULTI-AGENT SWARM EXPOSER FOR IDEs")
    print("=" * 70)
    print("Frontier Swarm Fleet: Claude Opus 5.5 + DeepSeek V4.1-Flash + GPT-6 Astra")
    print("Target IDEs:          Cursor, Windsurf, Claude Code, OpenAI Operator")
    print("-" * 70)

    server = McpGatewayServer()

    print("[STEP 1] EXPORTING 1-LINE CURSOR / CLAUDE CODE CONFIG SNIPPET...")
    print(server.get_cursor_config_snippet())

    print("-" * 70)
    print("[STEP 2] IDE CALLS `@swarm_execute` VIA STANDARD MCP JSON-RPC 2.0...")
    instruction = "Refactor payment service to reject non-positive amounts and test in UI"
    print(f" • Instruction: '{instruction}'")
    print()

    orchestrator = SwarmOrchestrator()

    def on_progress(evt: SwarmProgressEvent):
        pct_bar = "█" * (evt.progress_pct // 5) + "░" * (20 - (evt.progress_pct // 5))
        print(f" [{pct_bar}] {evt.progress_pct:>3}% | {evt.agent_role:<12} ({evt.model_name}): {evt.message}")

    req = SwarmTaskRequest(
        task_id="cursor_task_001",
        instruction=instruction,
        include_browser_test=True
    )

    response = orchestrator.execute_task(req, on_progress=on_progress)

    print("-" * 70)
    print("[STEP 3] MCP TOOL RESULT RETURNED DIRECTLY TO IDE EDITOR:")
    print(f" ✓ Execution Time: {response.execution_time_sec}s")
    print(f" ✓ Tests Passed:   {response.tests_passed} tests")
    print(f" ✓ Summary:        {response.summary}")
    print()
    print(response.git_diff.strip())
    print("=" * 70 + "\n")


def main() -> None:
    run_demo()


if __name__ == "__main__":
    main()
