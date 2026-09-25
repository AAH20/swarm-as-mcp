"""
Unit tests for Swarm-As-MCP using standard unittest.
"""

import unittest
from swarm_as_mcp.models import SwarmTaskRequest, SwarmStage
from swarm_as_mcp.swarm_orchestrator import SwarmOrchestrator
from swarm_as_mcp.mcp_gateway_server import McpGatewayServer


class TestSwarmAsMcp(unittest.TestCase):
    def test_mcp_tool_definitions(self):
        server = McpGatewayServer()
        tools = server.get_tool_definitions()
        self.assertEqual(len(tools), 2)
        names = [t["name"] for t in tools]
        self.assertIn("swarm_execute", names)
        self.assertIn("swarm_inspect_fleet", names)

    def test_orchestrator_execution_and_progress_events(self):
        orch = SwarmOrchestrator()
        events = []

        req = SwarmTaskRequest("t1", "Fix auth bug", include_browser_test=True)
        res = orch.execute_task(req, on_progress=lambda e: events.append(e))

        self.assertTrue(res.success)
        self.assertIn("diff --git", res.git_diff)
        self.assertEqual(res.tests_passed, 42)
        self.assertGreater(len(events), 3)
        self.assertEqual(events[-1].stage, SwarmStage.FINAL_VERIFIED)

    def test_mcp_server_call_handling(self):
        server = McpGatewayServer()
        result = server.handle_mcp_call("swarm_inspect_fleet", {})
        self.assertIn("content", result)
        self.assertIn("Claude Opus 5.5", result["content"][0]["text"])


if __name__ == "__main__":
    unittest.main()
