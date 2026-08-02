# Direct Specialist Task Reporting + Growth-Program Planning Pattern

Use this reference when Chris says he gives tasks directly to specialist agents and wants Karina to stay aware, or when he asks Son to help plan a future-dated growth/work program.

## Direct specialist task reporting

Chris's expectation:
- Chris may DM or mention a specialist directly.
- The specialist can answer directly in their lane, but must also report to Karina.
- Karina then DMs Chris with her concise understanding/synthesis so Chris does not have to manually track every specialist thread.

Specialist report shape to Karina:
1. What Chris asked for
2. Key context and constraints
3. Specialist's current understanding
4. Planned next step / owner / timing
5. Blockers or questions for Chris, if any

Karina DM shape to Chris:
- “제가 이해한 내용”
- “담당 에이전트 / 다음 액션”
- “결정 필요 또는 막힌 점”

Implementation surfaces to update when formalizing this behavior:
- Default/Karina `SOUL.md`
- Every specialist profile `SOUL.md`
- Durable user preference memory, if this is a stable Chris preference
- Team Slack channel announcement, if Slack team coordination is active
- Karina daily work log for the day the rule was changed

Pitfall: do not assume Karina saw the full DM context. The specialist must summarize; Karina should not fabricate missing context.

## Future-dated role-development planning with Son

When Chris sets a future goal such as “after next Friday, grow me into an ontology designer,” route planning to Son before final synthesis.

Son prompt should request:
1. Goal interpretation
2. Preparation timeline until the target date
3. First 4-week growth/execution loop
4. No more than 3 questions for Chris
5. A Karina-ready DM summary

Karina synthesis should be warm and concise:
- Confirm the date and goal
- State how Karina/Son understand the role
- Give the preparation timeline
- Give the first loop outline
- Ask the ≤3 clarifying questions

Work-log evidence to keep:
- Son plan path
- Summary of goal interpretation and questions
- Any blockers such as missing time budget, preferred artifact, or target domain
