"""Test configuration for Proposal Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "proposal-generation-agent", "category": "Sales"}
