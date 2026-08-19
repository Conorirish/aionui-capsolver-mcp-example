import json, unittest
from pathlib import Path
from aionui_recovery import RecoveryPolicy, ToolOutcome

class T(unittest.TestCase):
    def test_paths(self):
        p=RecoveryPolicy({"qa.example.test"})
        self.assertEqual(p.begin("https://qa.example.test/x").action,"call_mcp_tool")
        self.assertEqual(p.finish(ToolOutcome(True,True)).state,"completed")
        self.assertEqual(p.begin("https://qa.example.test/x").state,"budget_exhausted")
    def test_denied(self):
        self.assertEqual(RecoveryPolicy({"qa.example.test"}).begin("https://other.example/x").state,"denied")
    def test_error_and_persist(self):
        p=RecoveryPolicy({"qa.example.test"}); p.begin("https://qa.example.test/x")
        self.assertEqual(p.finish(ToolOutcome(False)).state,"tool_error")
        q=RecoveryPolicy({"qa.example.test"}); q.begin("https://qa.example.test/x")
        self.assertEqual(q.finish(ToolOutcome(True,False)).state,"challenge_persisted")
    def test_config(self):
        s=json.loads(Path("config/aionui.mcp.json").read_text())["mcpServers"]["capsolver"]
        self.assertEqual(s["command"],"capsolver-mcp")
        self.assertEqual(s["env"]["CAPSOLVER_API_KEY"],"YOUR_API_KEY")
        self.assertNotIn("url",s)
