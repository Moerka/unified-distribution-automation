# Unified Distribution Automation Skill

**Automate skill distribution to the Manus community with user consent and tracking.**

This Manus skill enables developers to automatically distribute their skills through multiple channels: email notifications, registry submissions, and direct sharing. It handles all the complexity of multi-channel distribution while maintaining transparency and user control.

## 🚀 Quick Start

### 1. Request Permission
```bash
python scripts/distribute.py --skill "my-skill" --permission-request
```

This displays what will be distributed and asks for explicit confirmation.

### 2. Execute Distribution
```bash
python scripts/distribute.py --skill "my-skill" --execute
```

This automatically:
- Sends emails to Manus community
- Submits to Manus Skill Registry
- Shares GitHub links
- Tracks all deliveries

### 3. Monitor Status
```bash
python scripts/distribute.py --skill "my-skill" --status
```

This shows:
- Email delivery status
- Registry submission status
- GitHub activity
- Engagement metrics

## ✨ Key Features

- **Automated Email Distribution** - Send announcements to community
- **Registry Submission** - Auto-submit to Manus Skill Registry
- **Direct Sharing** - Share with specific users
- **Consent Management** - Explicit permission required
- **Delivery Tracking** - Monitor all communications
- **Audit Trail** - Complete logging of all actions
- **Batch Processing** - Distribute multiple skills
- **Analytics** - Engagement and performance metrics

## 🔒 Consent & Permissions

This skill requires **explicit user permission** before any distribution:

1. **Request Phase** - Display what will happen
2. **Confirmation Phase** - User explicitly confirms
3. **Execution Phase** - Distribution proceeds
4. **Logging Phase** - All actions recorded

All permissions are logged with timestamps and can be revoked at any time.

## 📊 Usage Examples

### Distribute a Single Skill
```bash
python scripts/distribute.py --skill "mcp-crm-builder" --permission-request
python scripts/distribute.py --skill "mcp-crm-builder" --execute
```

### Check Distribution Status
```bash
python scripts/distribute.py --skill "mcp-crm-builder" --status
```

### View All Permissions
```bash
python scripts/distribute.py --skill "any-skill" --show-permissions
```

### Revoke Permission
```bash
python scripts/distribute.py --skill "my-skill" --revoke-permission
```

## 📚 Documentation

- **SKILL.md** - Complete skill documentation
- **references/ARCHITECTURE.md** - Technical architecture
- **references/WORKFLOW.md** - Detailed workflow guide
- **references/API.md** - API reference

## 🔧 Configuration

Edit `config.yaml` to customize:
- Email batch size and rate limits
- Registry endpoints
- Sharing preferences
- Consent requirements
- Audit trail retention

## 📊 Tracking & Analytics

The skill tracks:
- Email delivery status
- Registry submission progress
- GitHub activity (stars, forks, clones)
- User engagement (opens, clicks)
- Response times
- Community adoption

## 🎯 Use Cases

- **Single Skill Distribution** - Distribute one new skill
- **Batch Distribution** - Multiple skills simultaneously
- **Targeted Sharing** - Share with specific users
- **Proposal Submission** - Submit to leadership
- **Engagement Tracking** - Monitor community response
- **Periodic Updates** - Schedule regular distributions

## 🔐 Security

- All communications encrypted
- User data protected
- Consent logged and audited
- GDPR compliant
- Rate limiting to prevent spam
- Audit trail maintained

## 📞 Support

For issues or questions:
- Check SKILL.md for detailed documentation
- Review references/ for guides
- Contact: help.manus.im

## 📝 License

MIT License - See LICENSE.txt for details

## 🎉 Getting Started

1. Read SKILL.md for complete documentation
2. Prepare your skill with templates
3. Request permission with `--permission-request`
4. Execute distribution with `--execute`
5. Monitor results with `--status`

**Ready to automate your skill distribution?** Start now!

---

**Version:** 1.0.0  
**Status:** Production Ready ✅
