---
name: unified-distribution-automation
description: "Automated skill distribution platform - send emails, submit to registries, and distribute skills to the Manus community with one command. Includes user consent management, batch processing, and delivery tracking."
license: MIT
---

# 🚀 Unified Distribution Automation Skill

**Automate skill distribution to the Manus community with user consent and tracking.**

This skill enables developers to automatically distribute their Manus skills through multiple channels: email notifications, registry submissions, and direct sharing. It handles all the complexity of multi-channel distribution while maintaining transparency and user control.

---

## 🎯 What This Skill Does

The Unified Distribution Automation skill streamlines the process of sharing new Manus skills with the community. Instead of manually copying content, sending emails, and submitting to registries, you can:

1. **Prepare your skill** with email templates and registry submissions
2. **Grant permission** for automated distribution
3. **Execute distribution** with a single command
4. **Track delivery** and monitor responses

All with full transparency and user consent at every step.

---

## ✨ Core Features

### 1. Automated Email Distribution
- Send skill announcements to community members
- Personalized emails with skill details
- Batch email processing
- Delivery tracking and confirmation
- Retry logic for failed sends

### 2. Registry Submission Automation
- Submit skills to Manus Skill Registry
- Automatic form filling
- Submission tracking
- Status monitoring
- Approval notifications

### 3. Direct Sharing
- Share GitHub links with specific users
- Send personalized introduction emails
- Track engagement
- Monitor GitHub activity

### 4. Consent Management
- Explicit user permission required
- Permission logging and audit trail
- Revocation capability
- Transparency reports

### 5. Delivery Tracking
- Email delivery status
- Registry submission status
- Response monitoring
- Analytics dashboard
- Performance reports

### 6. Batch Processing
- Distribute multiple skills simultaneously
- Parallel processing with rate limiting
- Error handling and recovery
- Progress monitoring
- Completion notifications

---

## 🔧 Technical Architecture

### Components

**Distribution Engine**
- Orchestrates all distribution channels
- Manages workflow execution
- Handles error recovery
- Tracks progress and status

**Email Service Integration**
- Connects to Manus email API
- Manages email templates
- Handles batch sending
- Tracks delivery status

**Registry Integration**
- Connects to Manus Skill Registry API
- Automates form submission
- Monitors submission status
- Handles approval notifications

**Consent Manager**
- Tracks user permissions
- Maintains audit trail
- Enables revocation
- Generates consent reports

**Analytics Engine**
- Tracks distribution metrics
- Monitors engagement
- Generates performance reports
- Provides insights

---

## 📋 Usage Guide

### Quick Start

#### Step 1: Prepare Your Skill
Ensure your skill has:
- ✅ Email templates (in `/templates/emails/`)
- ✅ Registry submission content (in `/templates/registry/`)
- ✅ GitHub repository link
- ✅ Documentation

#### Step 2: Grant Permission
```bash
python scripts/distribute.py --skill "my-skill" --permission-request
```

This will:
1. Display what will be distributed
2. Show who will receive communications
3. Ask for explicit confirmation
4. Log your permission

#### Step 3: Execute Distribution
```bash
python scripts/distribute.py --skill "my-skill" --execute
```

This will:
1. Verify permission exists
2. Send emails to community
3. Submit to registry
4. Share GitHub links
5. Track all deliveries

#### Step 4: Monitor Progress
```bash
python scripts/distribute.py --skill "my-skill" --status
```

This will:
1. Show delivery status
2. Display engagement metrics
3. Report any errors
4. Provide recommendations

---

## 📧 Email Distribution

### Recipients
- Manus community mailing list
- Specific users (with permission)
- Registry team
- Leadership (for proposals)

### Email Templates
Located in `/templates/emails/`:
- `skill_announcement.txt` - General skill announcement
- `registry_submission.txt` - Registry submission notification
- `direct_share.txt` - Direct sharing email
- `proposal.txt` - Proposal email

### Customization
Edit templates to customize:
- Subject lines
- Content and messaging
- Call-to-action buttons
- Branding and signature

---

## 📋 Registry Submission

### Supported Registries
- Manus Skill Registry (primary)
- Community skill directories
- GitHub marketplace (optional)

### Submission Process
1. Prepare registry submission content
2. Validate against registry requirements
3. Submit automatically
4. Track submission status
5. Monitor for approval

### Status Tracking
- Submitted: Pending review
- Under Review: Being evaluated
- Approved: Listed in registry
- Rejected: With feedback
- Updates: Changes made

---

## 🤝 Direct Sharing

### Share With Specific Users
```bash
python scripts/distribute.py --skill "my-skill" --share-with moerka86@gmail.com
```

### Share With Groups
```bash
python scripts/distribute.py --skill "my-skill" --share-with-group "developers"
```

### Personalization
- Custom introduction message
- Specific use case highlighting
- Tailored recommendations
- Follow-up scheduling

---

## 📊 Tracking & Analytics

### Delivery Metrics
- Emails sent: Count and status
- Registry submissions: Status and timeline
- GitHub activity: Stars, forks, clones
- User engagement: Opens, clicks, actions

### Performance Reports
```bash
python scripts/distribute.py --skill "my-skill" --report
```

Generates:
- Distribution summary
- Delivery status
- Engagement metrics
- Recommendations

### Audit Trail
- All actions logged
- Timestamps recorded
- User permissions tracked
- Changes documented

---

## 🔐 Consent & Permissions

### Permission Model
1. **Request Phase**: Display what will happen
2. **Confirmation Phase**: User explicitly confirms
3. **Execution Phase**: Distribution proceeds
4. **Logging Phase**: All actions recorded

### Audit Trail
- Who authorized distribution
- When permission was granted
- What was distributed
- To whom it was sent
- Delivery confirmation

### Revocation
```bash
python scripts/distribute.py --skill "my-skill" --revoke-permission
```

Stops:
- Future distributions
- Email sending
- Registry submissions
- Sharing activities

---

## 🛠️ Configuration

### Config File: `config.yaml`

```yaml
distribution:
  email:
    enabled: true
    batch_size: 50
    rate_limit: 10/minute
    retry_attempts: 3
    retry_delay: 300
  
  registry:
    enabled: true
    registries:
      - name: "Manus Skill Registry"
        url: "https://help.manus.im/registry"
        auto_submit: true
  
  sharing:
    enabled: true
    track_engagement: true
    follow_up_enabled: true
    follow_up_delay: 604800  # 1 week

consent:
  require_explicit_permission: true
  log_all_actions: true
  enable_revocation: true
  audit_trail_retention: 2555  # days (7 years)
```

---

## 📚 Templates

### Email Template Structure
```
Subject: [SKILL_NAME] - [DESCRIPTION]

Dear [RECIPIENT_NAME],

[INTRODUCTION]

[FEATURES]

[CALL_TO_ACTION]

[SIGNATURE]
```

### Registry Template Structure
```
Skill Name: [NAME]
Description: [SHORT_DESCRIPTION]
Repository: [GITHUB_URL]
Category: [CATEGORY]
Keywords: [KEYWORDS]
Documentation: [DOCS_LINKS]
```

---

## 🚀 Advanced Features

### Batch Distribution
Distribute multiple skills at once:
```bash
python scripts/distribute.py --batch skills.json --execute
```

### Scheduled Distribution
Schedule distribution for later:
```bash
python scripts/distribute.py --skill "my-skill" --schedule "2026-04-26 10:00"
```

### Conditional Distribution
Distribute based on conditions:
```bash
python scripts/distribute.py --skill "my-skill" --if-approved --execute
```

### A/B Testing
Test different email versions:
```bash
python scripts/distribute.py --skill "my-skill" --ab-test --variants 2
```

---

## 📊 Reporting

### Generate Reports
```bash
python scripts/distribute.py --skill "my-skill" --report [type]
```

Report types:
- `summary` - Overview of distribution
- `detailed` - Complete breakdown
- `engagement` - User engagement metrics
- `audit` - Audit trail report
- `performance` - Performance analysis

### Export Data
```bash
python scripts/distribute.py --skill "my-skill" --export [format]
```

Export formats:
- `csv` - Spreadsheet format
- `json` - JSON format
- `pdf` - PDF report
- `html` - HTML report

---

## 🔄 Workflow Example

### Scenario: Distribute mcp-crm-builder Skill

**Step 1: Prepare**
```bash
cd /home/ubuntu/skills/unified-distribution-automation
python scripts/distribute.py --skill "mcp-crm-builder" --prepare
```

**Step 2: Review**
- Check email templates
- Review registry submission
- Verify GitHub links
- Confirm recipients

**Step 3: Request Permission**
```bash
python scripts/distribute.py --skill "mcp-crm-builder" --permission-request
```

**Output:**
```
Distribution Plan for: mcp-crm-builder
=====================================

Emails to send:
  - moerka86@gmail.com (1)
  - Manus community (1)
  - Registry team (1)

Registry submissions:
  - Manus Skill Registry

GitHub sharing:
  - https://github.com/Moerka/mcp-crm-builder

Consent required: YES
Do you authorize this distribution? (yes/no)
```

**Step 4: Confirm**
```
yes
```

**Step 5: Execute**
```bash
python scripts/distribute.py --skill "mcp-crm-builder" --execute
```

**Output:**
```
Distribution in progress...

✅ Email sent to moerka86@gmail.com
✅ Email sent to Manus community
✅ Registry submission submitted
✅ GitHub link shared
✅ All deliveries tracked

Distribution complete!
```

**Step 6: Monitor**
```bash
python scripts/distribute.py --skill "mcp-crm-builder" --status
```

**Output:**
```
Distribution Status: mcp-crm-builder
===================================

Emails:
  Sent: 3
  Delivered: 3
  Opened: 2
  Clicked: 1

Registry:
  Status: Submitted
  Expected review: 1-2 weeks

GitHub:
  Stars: 5
  Forks: 2
  Clones: 12

Overall Status: SUCCESS ✅
```

---

## 🔒 Security & Privacy

### Data Protection
- All communications encrypted
- User data protected
- Consent logged and audited
- GDPR compliant

### Permission Verification
- Explicit user consent required
- Permission verified before execution
- Audit trail maintained
- Revocation enabled

### Rate Limiting
- Prevents email spam
- Respects API limits
- Handles throttling
- Implements backoff

---

## 📞 Support & Troubleshooting

### Common Issues

**Permission Denied**
- Ensure you've granted permission with `--permission-request`
- Check audit trail: `--show-permissions`
- Revoke and re-grant if needed

**Email Delivery Failed**
- Check email configuration
- Verify recipient addresses
- Review delivery logs
- Retry with `--retry`

**Registry Submission Failed**
- Validate registry content
- Check registry API status
- Review submission logs
- Contact registry team

### Getting Help
- Check logs: `--show-logs`
- Review documentation: `references/`
- Contact support: help.manus.im

---

## 📈 Best Practices

1. **Always Request Permission First**
   - Use `--permission-request` before `--execute`
   - Review the distribution plan
   - Confirm all details

2. **Test Before Full Distribution**
   - Use `--test` flag for dry run
   - Send to yourself first
   - Verify email formatting

3. **Monitor Delivery**
   - Check status regularly
   - Review engagement metrics
   - Address any issues promptly

4. **Keep Records**
   - Export reports for documentation
   - Maintain audit trail
   - Track responses

5. **Update Templates**
   - Keep email templates current
   - Update registry information
   - Refresh GitHub links

---

## 🎯 Use Cases

### Single Skill Distribution
Distribute one new skill to the community with tracking.

### Batch Distribution
Distribute multiple skills simultaneously with coordination.

### Targeted Sharing
Share specific skills with targeted users or groups.

### Proposal Submission
Submit strategic proposals to Manus leadership.

### Engagement Tracking
Monitor community response and engagement.

### Periodic Updates
Schedule regular distribution of skill updates.

---

## 📊 Metrics & KPIs

- **Distribution Rate**: Percentage of successful distributions
- **Delivery Rate**: Percentage of emails delivered
- **Engagement Rate**: Percentage of recipients engaging
- **Registry Approval Rate**: Percentage of registry submissions approved
- **Community Adoption**: Number of users adopting skills
- **Response Time**: Average time to response

---

## 🚀 Future Enhancements

- Multi-language email support
- Advanced scheduling and automation
- Integration with social media platforms
- Real-time analytics dashboard
- AI-powered content optimization
- Automated follow-up campaigns

---

## 📝 License

This skill is provided under the MIT License. See LICENSE.txt for details.

---

## 🎉 Getting Started

1. **Read this guide** - Understand the features
2. **Prepare your skill** - Create templates and content
3. **Request permission** - Use `--permission-request`
4. **Execute distribution** - Use `--execute`
5. **Monitor results** - Use `--status` and `--report`

**Ready to distribute?** Start with the quick start guide above!

---

**Skill Version:** 1.0.0  
**Last Updated:** April 19, 2026  
**Status:** Production Ready ✅

## Advanced Authentication

This skill uses advanced GitHub authentication with:
- JWT Token Management
- Encrypted Secret Vault
- GitHub App Integration
- Permission Scoping
- Audit Logging

See ADVANCED_AUTH_GUIDE.md for details.
