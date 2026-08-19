from aionui_recovery import RecoveryPolicy, ToolOutcome
p=RecoveryPolicy({"qa.example.test"})
d=p.begin("https://qa.example.test/x"); print(f"{d.action}: {d.reason}")
d=p.finish(ToolOutcome(True,True)); print(f"{d.state}: {d.reason}")
