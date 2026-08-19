from __future__ import annotations
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass(frozen=True)
class Decision:
    state: str
    action: str
    reason: str

@dataclass(frozen=True)
class ToolOutcome:
    success: bool
    challenge_cleared: bool = False
    error_code: str | None = None

class RecoveryPolicy:
    def __init__(self, allowed_hosts: set[str], max_attempts: int = 1):
        if not allowed_hosts or max_attempts < 1:
            raise ValueError("non-empty allowlist and positive budget required")
        self.allowed_hosts = {h.lower() for h in allowed_hosts}
        self.max_attempts, self.attempts, self.pending = max_attempts, 0, False

    def begin(self, target_url: str) -> Decision:
        parsed = urlparse(target_url)
        if parsed.scheme not in {"http", "https"} or (parsed.hostname or "").lower() not in self.allowed_hosts:
            return Decision("denied", "stop", "target is not allowlisted")
        if self.pending:
            return Decision("tool_error", "stop", "attempt already pending")
        if self.attempts >= self.max_attempts:
            return Decision("budget_exhausted", "stop", "attempt budget exhausted")
        self.attempts += 1
        self.pending = True
        return Decision("challenge_detected", "call_mcp_tool", f"authorized recovery attempt {self.attempts} of {self.max_attempts}")

    def finish(self, outcome: ToolOutcome) -> Decision:
        if not self.pending:
            return Decision("tool_error", "stop", "no attempt pending")
        self.pending = False
        if not outcome.success:
            return Decision("tool_error", "stop", "MCP tool returned an error")
        if not outcome.challenge_cleared:
            return Decision("challenge_persisted", "stop", "challenge remained")
        return Decision("completed", "resume_once", "challenge cleared; task may resume once")
