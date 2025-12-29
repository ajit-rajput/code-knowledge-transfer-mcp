from pydantic import BaseModel, Field
from typing import List


class CodeKnowledge(BaseModel):
    subject: str = Field(
        ..., description="The code component or concept being explained"
    )

    purpose: str = Field(
        ..., description="What this component exists to do"
    )

    historical_reasoning: str = Field(
        ..., description="Why this component was introduced or evolved"
    )

    key_mechanics: List[str] = Field(
        ..., description="Step-by-step explanation of how it works internally"
    )

    design_tradeoffs: List[str] = Field(
        default_factory=list,
        description="Explicit trade-offs made in the design"
    )

    known_failure_modes: List[str] = Field(
        default_factory=list,
        description="Known ways this component has failed historically"
    )

    safe_change_zones: List[str] = Field(
        default_factory=list,
        description="Areas considered safe for modification"
    )

    high_risk_zones: List[str] = Field(
        default_factory=list,
        description="Areas where changes are historically risky"
    )

    supporting_evidence: List[str] = Field(
        default_factory=list,
        description="Commits, PRs, issues, or docs supporting claims"
    )

    confidence: float = Field(
        ..., ge=0.0, le=1.0,
        description="Confidence in the explanation"
    )