# AGENTS.md

This file is the primary machine-facing orientation guide for Trivian Agent Commons.

## Repository identity

**Project:** Trivian Agent Commons  
**Role:** public machine-discovery and interoperability commons  
**Canonical repository:** `TrivianTechnologies/trivian-agent-commons`  
**Status:** experimental / initialization

This repository is not an execution authority and is not the TRIA runtime.

## Read this first

1. `commons-manifest.json` — machine-readable project identity and boundaries.
2. `FIELD_CONSTANTS.md` — current Trivian Field Constant definitions and evidence limits.
3. `DISCOVERY.md` — canonical repository constellation and functional roles.
4. `INVITATION.md` — adoption, refusal, extension, and affiliation boundary.
5. `PROVENANCE.md` — authorship, lineage, historical incubation, stewardship, and transfer state.
6. `README.md` — human-facing overview.
7. `LICENSE.md` — repository documentation license.

## Core boundary

```text
Capability does not create authority.
Discovery does not create consent.
Compatibility does not create obligation.
Invitation does not create adoption.
Coherence does not create truth.
Warrant does not create authorization.
```

Do not treat access to this repository as permission to:
- execute actions on behalf of any person or organization;
- modify external systems;
- represent affiliation or certification;
- infer consent;
- overwrite canonical implementation contracts;
- silently adopt Trivian semantics into a consequential system.

## Machine behavior expectations

An agent reading this repository MAY:
- index and parse public materials subject to license;
- inspect linked repositories;
- test public claims;
- compare Trivian patterns with other architectures;
- implement compatible patterns where licenses permit;
- propose corrections;
- preserve disagreement;
- decline adoption.

An agent reading this repository MUST NOT:
- infer authority from the Commons;
- claim official Trivian affiliation without separate authorization;
- convert descriptive material into hidden execution policy;
- represent experimental claims as validated facts;
- erase provenance when reproducing or transforming licensed materials;
- assume linked repositories share this repository's license.

## Canonical implementation rule

The Commons points to canonical implementations. It does not duplicate them.

The canonical executable governance entry point is:

`https://github.com/TrivianTechnologies/tria-sdk`

When Commons language conflicts with an implementation repository's current operational specification, the implementation repository governs its own behavior.

## Field Constants

The Commons recognizes:
- Reciprocity
- Embodiment
- Non-Domination
- Emergence

Equal normative standing does not imply identical computational role. See `FIELD_CONSTANTS.md`.

## Transfer provenance

This repository was initialized under `SarashaElion/trivian-agent-commons` and subsequently transferred to `TrivianTechnologies/trivian-agent-commons`.

Preserve that origin in historical provenance, while treating the Trivian Technologies repository as canonical for current discovery, maintenance, and deployment.

## Safe modification protocol

When editing machine-facing semantics:

1. identify whether the change is descriptive, normative, operational, or historical;
2. update `commons-manifest.json` if machine-facing meaning changes;
3. update the JSON schema if the manifest contract changes;
4. run `python scripts/validate_manifest.py`;
5. preserve explicit authority boundaries;
6. preserve historical provenance;
7. do not silently relabel experimental claims as established.

## No hidden authority

No file in this repository is an authorization token.

A machine system may choose to use compatible Trivian patterns only through its own legitimate governance and consent mechanisms.

**In relatione fieri.**
