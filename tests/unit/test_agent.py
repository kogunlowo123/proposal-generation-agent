"""Proposal Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_proposal():
    """Test Generate a customized sales proposal from template and deal data."""
    tools = AgentTools()
    result = await tools.generate_proposal(deal_id="test", template="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_configure_pricing():
    """Test Configure pricing for a proposal based on deal parameters."""
    tools = AgentTools()
    result = await tools.configure_pricing(products="test", discount_level="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_add_case_studies():
    """Test Select and add relevant case studies to the proposal."""
    tools = AgentTools()
    result = await tools.add_case_studies(industry="test", use_case="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_send_proposal():
    """Test Send proposal with tracking and e-signature."""
    tools = AgentTools()
    result = await tools.send_proposal(proposal_id="test", recipients="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.proposal_generation_agent_agent import ProposalGenerationAgentAgent
    agent = ProposalGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
