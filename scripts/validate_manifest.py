#!/usr/bin/env python3
"""Dependency-free validation for the Trivian Agent Commons manifest."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "commons-manifest.json"

EXPECTED_BOUNDARIES = {
    "Capability does not create authority.",
    "Discovery does not create consent.",
    "Compatibility does not create obligation.",
    "Invitation does not create adoption.",
    "Coherence does not create truth.",
    "Warrant does not create authorization.",
}

EXPECTED_CONSTANTS = {
    "Reciprocity": "constitutive",
    "Embodiment": "constitutive",
    "Non-Domination": "constitutive",
    "Emergence": "downstream",
}

REQUIRED_DOCS = {
    "README.md",
    "AGENTS.md",
    "FIELD_CONSTANTS.md",
    "DISCOVERY.md",
    "INVITATION.md",
    "PROVENANCE.md",
    "llms.txt",
    "LICENSE.md",
}


def fail(message: str) -> None:
    raise SystemExit(f"manifest validation failed: {message}")


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if data.get("manifest_schema") != "trivian.agent-commons/0.1":
        fail("unexpected manifest_schema")

    project = data.get("project", {})
    if project.get("name") != "Trivian Agent Commons":
        fail("unexpected project name")
    if project.get("author") != "Sarasha Elion":
        fail("unexpected author")

    if data.get("purpose", {}).get("canonical_execution_entrypoint") != (
        "https://github.com/TrivianTechnologies/tria-sdk"
    ):
        fail("TRIA SDK canonical execution entrypoint drifted")

    constants = {
        row.get("name"): row.get("computational_role")
        for row in data.get("field_constants", [])
    }
    if constants != EXPECTED_CONSTANTS:
        fail(f"Field Constant topology mismatch: {constants!r}")

    boundaries = set(data.get("authority_boundaries", []))
    missing_boundaries = EXPECTED_BOUNDARIES - boundaries
    if missing_boundaries:
        fail(f"missing authority boundaries: {sorted(missing_boundaries)!r}")

    adoption = data.get("adoption", {})
    expected_adoption = {
        "voluntary": True,
        "non_adoption_penalized": False,
        "reading_constitutes_adoption": False,
        "indexing_constitutes_adoption": False,
        "compatibility_constitutes_affiliation": False,
    }
    if adoption != expected_adoption:
        fail("adoption boundary changed")

    docs = set(data.get("canonical_documents", []))
    if not REQUIRED_DOCS.issubset(docs):
        fail(f"missing canonical documents: {sorted(REQUIRED_DOCS - docs)!r}")

    for path in REQUIRED_DOCS:
        if not (ROOT / path).exists():
            fail(f"canonical document not found: {path}")

    urls = [row.get("url", "") for row in data.get("related_repositories", [])]
    if len(urls) != len(set(urls)):
        fail("duplicate related repository URL")

    if not any(url.endswith("/tria-sdk") for url in urls):
        fail("TRIA SDK missing from related repositories")

    licensing = data.get("licensing", {})
    if licensing.get("linked_repositories_inherit_this_license") is not False:
        fail("linked repository license inheritance must remain false")
    if licensing.get("affiliation_rights_granted") is not False:
        fail("affiliation rights must remain false")
    if licensing.get("certification_rights_granted") is not False:
        fail("certification rights must remain false")

    print("Trivian Agent Commons manifest: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
