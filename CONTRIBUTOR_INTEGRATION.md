# Contributor Integration Guide

**How to use the Unified Distribution Automation skill as a contributor**

---

## 🎯 Overview

This guide explains how to integrate the Unified Distribution Automation skill into your workflow as a contributor to Manus skills.

---

## 🚀 Quick Start for Contributors

### Step 1: Clone the Skill Repository

```bash
git clone https://github.com/Moerka/unified-distribution-automation.git
cd unified-distribution-automation
```

### Step 2: Install Dependencies

```bash
# Python 3.7+ required
python3 --version

# Install required packages (if any)
pip install -r requirements.txt  # (if requirements.txt exists)
```

### Step 3: Use the Skill

```bash
# Request permission to distribute your skill
python scripts/distribute.py --skill "your-skill-name" --permission-request

# Execute distribution
python scripts/distribute.py --skill "your-skill-name" --execute

# Check status
python scripts/distribute.py --skill "your-skill-name" --status
```

---

## 📋 Workflow for Contributors

### Creating a New Skill

1. **Create your skill** in `/home/ubuntu/skills/your-skill-name/`
2. **Prepare documentation:**
   - `SKILL.md` - Main documentation
   - `README.md` - Quick start
   - `TEST_SCENARIO.md` - Test walkthrough
3. **Create templates:**
   - Email templates in `templates/emails/`
   - Registry submission in `templates/registry/`
4. **Test your skill** thoroughly
5. **Use distribution automation:**
   ```bash
   python /home/ubuntu/skills/unified-distribution-automation/scripts/distribute.py \
     --skill "your-skill-name" \
     --permission-request
   ```

### Distributing Your Skill

**Step 1: Request Permission**
```bash
python scripts/distribute.py --skill "your-skill-name" --permission-request
```

You'll see:
```
DISTRIBUTION PERMISSION REQUEST
================================

Skill: your-skill-name
This will:
  ✉️  Send emails to Manus community
  📋 Submit to Manus Skill Registry
  🔗 Share GitHub links
  📊 Track all deliveries

Recipients:
  • moerka86@gmail.com
  • Manus community mailing list
  • Manus Skill Registry team

Do you authorize this distribution? (yes/no):
```

**Step 2: Confirm**
```
yes
```

**Step 3: Execute Distribution**
```bash
python scripts/distribute.py --skill "your-skill-name" --execute
```

**Step 4: Monitor**
```bash
python scripts/distribute.py --skill "your-skill-name" --status
```

---

## 🔐 Permission Management

### Grant Permission
```bash
python scripts/distribute.py --skill "your-skill" --permission-request
```

### Check Permission Status
```bash
python scripts/distribute.py --skill "your-skill" --show-permissions
```

### Revoke Permission
```bash
python scripts/distribute.py --skill "your-skill" --revoke-permission
```

---

## 📊 Tracking Your Distribution

### Check Distribution Status
```bash
python scripts/distribute.py --skill "your-skill" --status
```

**Output includes:**
- Email delivery status
- Registry submission status
- GitHub activity
- Engagement metrics

### View Audit Trail
```bash
python scripts/distribute.py --skill "your-skill" --show-permissions
```

**Shows:**
- All actions taken
- Timestamps
- Consent IDs
- Complete history

---

## 🎯 Best Practices for Contributors

### 1. Prepare Your Skill First
- ✅ Complete documentation
- ✅ Test thoroughly
- ✅ Create email templates
- ✅ Prepare registry submission

### 2. Request Permission Before Distribution
- Always use `--permission-request` first
- Review what will be distributed
- Confirm all details
- Grant explicit permission

### 3. Execute Distribution
- Use `--execute` to distribute
- Monitor the process
- Track delivery status
- Gather feedback

### 4. Monitor Results
- Check status regularly
- Review engagement metrics
- Respond to feedback
- Plan improvements

### 5. Maintain Audit Trail
- Keep permission logs
- Document all distributions
- Track responses
- Maintain records

---

## 📧 Email Templates

### For Contributors

Create email templates in your skill's `templates/emails/` directory:

**Example: skill_announcement.txt**
```
Subject: [SKILL_NAME] - [DESCRIPTION]

Dear Manus Community,

I'm excited to introduce [SKILL_NAME]...

[FEATURES]

[CALL_TO_ACTION]

Best regards,
[YOUR_NAME]
```

### Template Variables
- `[SKILL_NAME]` - Your skill name
- `[DESCRIPTION]` - Short description
- `[FEATURES]` - Key features
- `[CALL_TO_ACTION]` - What users should do
- `[YOUR_NAME]` - Your name

---

## 🔗 GitHub Integration

### Share Your Repository
```bash
python scripts/distribute.py --skill "your-skill" --execute
```

This automatically:
- Shares your GitHub link
- Tracks repository activity
- Monitors stars and forks
- Reports engagement

### Track GitHub Activity
```bash
python scripts/distribute.py --skill "your-skill" --status
```

Shows:
- GitHub stars
- Forks
- Clones
- Activity metrics

---

## 📋 Registry Submission

### Automatic Registry Submission
```bash
python scripts/distribute.py --skill "your-skill" --execute
```

This automatically:
- Prepares registry submission
- Submits to Manus Skill Registry
- Tracks submission status
- Notifies on approval

### Check Registry Status
```bash
python scripts/distribute.py --skill "your-skill" --status
```

Shows:
- Submission status
- Expected review timeline
- Approval notifications

---

## 🤝 Collaboration for Contributors

### Multiple Contributors

If multiple contributors are working on a skill:

1. **Coordinator requests permission:**
   ```bash
   python scripts/distribute.py --skill "shared-skill" --permission-request
   ```

2. **All contributors confirm:**
   - Review the distribution plan
   - Ensure all contributions are included
   - Confirm distribution

3. **Execute distribution:**
   ```bash
   python scripts/distribute.py --skill "shared-skill" --execute
   ```

4. **Track together:**
   ```bash
   python scripts/distribute.py --skill "shared-skill" --status
   ```

---

## 📊 Metrics & Analytics

### Distribution Metrics
- **Distribution Rate** - % of successful distributions
- **Delivery Rate** - % of emails delivered
- **Engagement Rate** - % of recipients engaging
- **Adoption Rate** - Number of users adopting skill

### Performance Metrics
- **Email Opens** - How many opened emails
- **Click Rate** - How many clicked links
- **Response Time** - Average time to response
- **GitHub Activity** - Stars, forks, clones

### Track Your Metrics
```bash
python scripts/distribute.py --skill "your-skill" --status
```

---

## 🔒 Security & Privacy

### Your Consent is Required
- Explicit permission needed before distribution
- You control what gets sent
- You can revoke anytime
- Complete audit trail maintained

### Data Protection
- Your data is protected
- Audit logs are maintained
- GDPR compliant
- Transparent tracking

### Revocation Anytime
```bash
python scripts/distribute.py --skill "your-skill" --revoke-permission
```

---

## 📞 Support for Contributors

### Getting Help

1. **Read the documentation:**
   - SKILL.md - Complete guide
   - README.md - Quick start
   - TEST_SCENARIO.md - Examples

2. **Check the audit trail:**
   ```bash
   python scripts/distribute.py --skill "your-skill" --show-permissions
   ```

3. **Contact support:**
   - help.manus.im
   - GitHub issues
   - Community forums

---

## 🎯 Example: Distribute Your Skill

### Scenario: You Created "my-awesome-skill"

**Step 1: Prepare**
```bash
cd /home/ubuntu/skills/my-awesome-skill
# Ensure SKILL.md, README.md, TEST_SCENARIO.md exist
# Ensure templates are ready
```

**Step 2: Request Permission**
```bash
python /home/ubuntu/skills/unified-distribution-automation/scripts/distribute.py \
  --skill "my-awesome-skill" \
  --permission-request
```

**Step 3: Review & Confirm**
```
Do you authorize this distribution? (yes/no): yes
```

**Step 4: Execute**
```bash
python /home/ubuntu/skills/unified-distribution-automation/scripts/distribute.py \
  --skill "my-awesome-skill" \
  --execute
```

**Step 5: Monitor**
```bash
python /home/ubuntu/skills/unified-distribution-automation/scripts/distribute.py \
  --skill "my-awesome-skill" \
  --status
```

**Result:**
```
✅ Emails sent: 3
✅ Registry submitted: 1
✅ GitHub links shared: 1
✅ All deliveries tracked
```

---

## 🚀 Next Steps

1. **Create your skill** following Manus guidelines
2. **Prepare documentation** (SKILL.md, README.md, etc.)
3. **Test thoroughly** using TEST_SCENARIO.md
4. **Use distribution automation:**
   ```bash
   python scripts/distribute.py --skill "your-skill" --permission-request
   python scripts/distribute.py --skill "your-skill" --execute
   ```
5. **Monitor and gather feedback**
6. **Iterate and improve**

---

## 📝 Checklist for Contributors

- [ ] Skill created and tested
- [ ] SKILL.md documentation complete
- [ ] README.md created
- [ ] TEST_SCENARIO.md created
- [ ] Email templates prepared
- [ ] Registry submission prepared
- [ ] GitHub repository ready
- [ ] Permission requested
- [ ] Distribution executed
- [ ] Status monitored
- [ ] Feedback gathered
- [ ] Improvements planned

---

## 🎉 You're Ready!

You now have everything you need to:
- ✅ Create professional Manus skills
- ✅ Distribute them automatically
- ✅ Track engagement
- ✅ Maintain audit trails
- ✅ Collaborate with others

**Ready to create and share your skills?** Let's go! 🚀

---

**Version:** 1.0.0  
**Last Updated:** April 19, 2026  
**For:** Manus Skill Contributors
