"""GUIDE Phần 1 - Định nghĩa subagent (tác tử con).   >>> SINH VIÊN CÀI ĐẶT <<<

Pseudo-code: guides/pseudocode/02_subagents.md
Kiểm tra:    pytest tests/test_02_agent.py
"""


def get_subagents() -> list[dict]:
    """Trả về danh sách subagent (ít nhất 2, tên khác nhau).

    Mỗi phần tử là một dict có các khóa bắt buộc:
      "name":          tên duy nhất (chữ thường, có thể có dấu gạch ngang)
      "description":   khi nào tác tử chính nên giao việc cho subagent này (viết như một hướng dẫn hành động)
      "system_prompt": chỉ dẫn cho subagent
    Gợi ý vai trò: explorer (đọc và báo cáo), implementer (thực hiện), reviewer (kiểm tra độc lập).
    """
    return [
        {
            "name": "explorer",
            "description": "Use when you need to inspect task instructions, documentation, or input files before deciding on an implementation. Report findings only; do not modify files.",
            "system_prompt": "Inspect the requested files carefully and return a concise factual report. Do not edit files or claim work you did not verify.",
        },
        {
            "name": "implementer",
            "description": "Use when a well-scoped implementation, data transformation, or test run needs to be completed in the sandbox.",
            "system_prompt": "Implement the requested change in the sandbox, run relevant verification when possible, and report exactly which files changed and what the verification showed.",
        },
        {
            "name": "reviewer",
            "description": "Use after a proposed solution exists and you need an independent check against the task requirements or edge cases.",
            "system_prompt": "Review the current sandbox against the supplied requirements and edge cases. Do not edit files; report verified problems and checks you ran.",
        },
    ]
