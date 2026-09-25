"""
Data models and typed schemas for Swarm-As-MCP.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple, Any
import time


class SwarmStage(str, Enum):
    PLANNING = "planning"
    CODING = "coding"
    COMPILING = "compiling"
    BROWSER_TEST = "browser_test"
    FINAL_VERIFIED = "final_verified"


@dataclass
class SwarmTaskRequest:
    task_id: str
    instruction: str
    repo_root: str = "/workspace"
    include_browser_test: bool = True
    timeout_sec: float = 120.0


@dataclass
class SwarmProgressEvent:
    event_id: str
    timestamp: float
    stage: SwarmStage
    agent_role: str
    model_name: str
    message: str
    progress_pct: int


@dataclass
class SwarmTaskResponse:
    task_id: str
    success: bool
    summary: str
    git_diff: str
    modified_files: List[str]
    tests_passed: int
    execution_time_sec: float
