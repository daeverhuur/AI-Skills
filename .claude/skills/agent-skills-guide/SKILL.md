---
name: agent-skills-guide
description: Guide for creating, managing, and using Claude Code Agent Skills. Use when the user asks about Skills, wants to create a new Skill, or needs help with SKILL.md files.
---

# Agent Skills Guide

## What are Agent Skills?

Agent Skills package expertise into discoverable capabilities for Claude Code. Each Skill consists of:
- A `SKILL.md` file with instructions (required)
- Optional supporting files (scripts, templates, references)

**Key distinction**: Skills are **model-invoked** (Claude autonomously decides when to use them based on task context), unlike slash commands which are **user-invoked**.

## Skill Locations

### Personal Skills
- Path: `~/.claude/skills/<skill-name>/SKILL.md`
- Available across all projects
- Use for: Individual workflows, experimental skills, personal productivity

### Project Skills
- Path: `.claude/skills/<skill-name>/SKILL.md`
- Shared via git with team members
- Use for: Team workflows, project-specific expertise, shared utilities

### Plugin Skills
- Bundled with installed Claude Code plugins
- Automatically available when plugin is installed

## SKILL.md Structure

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
allowed-tools: Read, Grep, Glob  # Optional: restrict available tools
---

# Your Skill Name

## Instructions
Step-by-step guidance for Claude.

## Examples
Concrete examples of using this Skill.
```

### Field Requirements
- `name`: Lowercase letters, numbers, hyphens only (max 64 chars)
- `description`: What the Skill does AND when to use it (max 1024 chars)
- `allowed-tools`: Optional comma-separated list of permitted tools

## Best Practices

### Write Effective Descriptions
The description is critical for Claude to discover when to use your Skill.

**Bad** (too vague):
```yaml
description: Helps with documents
```

**Good** (specific):
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

### Keep Skills Focused
One Skill = one capability. Split broad concepts into separate Skills.

**Good**: "PDF form filling", "Excel data analysis", "Git commit messages"
**Bad**: "Document processing" (too broad)

### Multi-File Skills Structure
```
my-skill/
├── SKILL.md (required)
├── reference.md (optional documentation)
├── examples.md (optional examples)
├── scripts/
│   └── helper.py (optional utility)
└── templates/
    └── template.txt (optional template)
```

Reference files from SKILL.md - Claude loads them only when needed (progressive disclosure).

## Testing Skills

Test by asking questions that match your description:
```
# If description mentions "PDF files":
Can you help me extract text from this PDF?
```

Claude automatically activates Skills based on task context.

## Debugging Skills

### Skill Not Activating
1. Make description more specific with trigger terms
2. Verify file path is correct
3. Check YAML syntax (no tabs, correct indentation)
4. Run `claude --debug` to see loading errors

### Common Issues
- Missing opening/closing `---` in frontmatter
- Tabs instead of spaces in YAML
- Unquoted strings with special characters

## Sharing Skills

### Via Git (Project Skills)
```bash
mkdir -p .claude/skills/team-skill
# Create SKILL.md
git add .claude/skills/
git commit -m "Add team Skill"
git push
```

### Via Plugins (Recommended for Distribution)
Create a plugin with Skills in the `skills/` directory and distribute through marketplaces.

## Example Skills

### Simple Single-File Skill
```yaml
---
name: commit-helper
description: Generates clear commit messages from git diffs. Use when writing commit messages or reviewing staged changes.
---

# Commit Message Generator

## Instructions
1. Run `git diff --staged` to see changes
2. Suggest commit message with:
   - Summary under 50 characters
   - Detailed description
   - Affected components

## Best Practices
- Use present tense
- Explain what and why, not how
```

### Read-Only Skill with Tool Restrictions
```yaml
---
name: code-reviewer
description: Review code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
allowed-tools: Read, Grep, Glob
---

# Code Reviewer

## Review Checklist
1. Code organization and structure
2. Error handling
3. Performance considerations
4. Security concerns
5. Test coverage
```

## Frontend Design Skill Example

For improved UI generation, use targeted prompting across:
- **Typography**: Avoid generic fonts (Inter, Roboto), use distinctive choices
- **Color & Theme**: Commit to cohesive aesthetics, use CSS variables
- **Motion**: Animations for effects and micro-interactions
- **Backgrounds**: Create atmosphere and depth, avoid solid colors

## Commands

View available Skills:
```
What Skills are available?
```

List Skills manually:
```bash
ls ~/.claude/skills/
ls .claude/skills/
```
