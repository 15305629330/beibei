from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..base import BaseAgent

from autogpt.config import Config
from autogpt.workspace import Workspace


class WorkspaceMixin:
    """Mixin that adds workspace support to a class"""

    workspace: Workspace
    """Workspace that the agent has access to, e.g. for reading/writing files."""

    def __init__(self, **kwargs):
        config: Config = getattr(self, "config")
        if not isinstance(config, Config):
            raise ValueError(f"Cannot initialize Workspace for Agent without Config")
        if not config.workspace_path:
            raise ValueError(f"Cannot set up Workspace: no WORKSPACE_PATH in config")

        self.workspace = Workspace(config.workspace_path, config.restrict_to_workspace)

        super(WorkspaceMixin, self).__init__(**kwargs)


def get_agent_workspace(agent: BaseAgent) -> Workspace | None:
    if isinstance(agent, WorkspaceMixin):
        return agent.workspace

    return None