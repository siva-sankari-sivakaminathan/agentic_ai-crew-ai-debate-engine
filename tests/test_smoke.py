"""Smoke tests — no API calls."""

from debate_engine.crew import DebateEngine
from debate_engine.main import get_debate_case


def test_builtin_cases_have_motion_and_documents():
    for n in (1, 2, 3, 4):
        case = get_debate_case(n)
        assert case["motion"].strip()
        assert case["case_documents"].strip()
        assert case["name"].strip()


def test_debate_engine_builds_crew():
    crew = DebateEngine().crew()
    assert crew.agents
    assert crew.tasks
