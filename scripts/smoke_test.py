from aionui_recovery import RecoveryPolicy, ToolOutcome
p=RecoveryPolicy({"qa.example.test"})
assert p.begin("https://qa.example.test/x").action=="call_mcp_tool"
assert p.finish(ToolOutcome(True,True)).state=="completed"
print("smoke test passed")
