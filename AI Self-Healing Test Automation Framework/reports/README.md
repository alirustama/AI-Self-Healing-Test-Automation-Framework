# Test Reports Directory

This directory stores test execution reports and artifacts:

- **report.html** - Main test report (HTML format)
- **screenshots/** - Screenshots captured during test failures
- **logs/** - Test execution logs

## Accessing Reports

After running tests:

```bash
# View the HTML report
open reports/report.html
```

## Report Contents

- Test execution summary
- Pass/Fail status for each test
- Execution time
- Error messages and stack traces
- Associated screenshots for failed tests

## CI/CD Integration

Reports are automatically uploaded as artifacts in GitHub Actions workflows.
