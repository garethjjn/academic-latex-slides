#!/usr/bin/env python3
"""Create a starter academic Beamer project from a bundled template."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


TEMPLATE_CHOICES = ("msu", "sjtu", "cityu", "generic")
DECK_CHOICES = ("lecture", "research-talk")
LANGUAGE_CHOICES = ("en", "zh")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--template", choices=TEMPLATE_CHOICES, required=True)
    parser.add_argument("--deck-type", choices=DECK_CHOICES, required=True)
    parser.add_argument("--language", choices=LANGUAGE_CHOICES, required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--author", required=True)
    parser.add_argument("--institute", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--force", action="store_true", help="allow writing into a non-empty directory")
    return parser.parse_args()


def short_text(value: str, fallback: str) -> str:
    compact = " ".join(value.split())
    return compact if compact else fallback


def escape_latex(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def prepare_output_dir(path: Path, force: bool) -> None:
    path.mkdir(parents=True, exist_ok=True)
    if any(path.iterdir()) and not force:
        raise SystemExit(f"Output directory is not empty: {path}")
    (path / "sections").mkdir(exist_ok=True)
    (path / "figures").mkdir(exist_ok=True)
    (path / "figures" / ".gitkeep").touch()


def copy_template_assets(template_dir: Path, output_dir: Path) -> None:
    for item in template_dir.iterdir():
        if item.name == "main.tex.template":
            continue
        destination = output_dir / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(item, destination)


def section_files(deck_type: str, language: str) -> dict[str, str]:
    if deck_type == "lecture":
        if language == "zh":
            return {
                "01_learning_goals.tex": r"""\section{学习目标}
\begin{frame}{学习目标}
  \begin{itemize}
    \item TODO：填写本讲的核心学习目标
    \item TODO：说明学生在本讲结束后应能完成什么
  \end{itemize}
\end{frame}
""",
                "02_core_content.tex": r"""\section{核心内容}
\begin{frame}{核心概念}
  \begin{itemize}
    \item TODO：插入核心概念、定义或推导
    \item TODO：根据已确认的大纲拆分为多页
  \end{itemize}
\end{frame}
""",
                "03_examples.tex": r"""\section{例子与应用}
\begin{frame}{例子或练习}
  TODO：插入经用户确认的例题、练习或讨论提示
\end{frame}
""",
                "04_summary.tex": r"""\section{总结}
\begin{frame}{本讲小结}
  \begin{itemize}
    \item TODO：总结最重要的三点
  \end{itemize}
\end{frame}
""",
            }
        return {
            "01_learning_goals.tex": r"""\section{Learning Goals}
\begin{frame}{Learning Goals}
  \begin{itemize}
    \item TODO: state the main learning objective
    \item TODO: state what students should be able to do afterwards
  \end{itemize}
\end{frame}
""",
            "02_core_content.tex": r"""\section{Core Content}
\begin{frame}{Core Concept}
  \begin{itemize}
    \item TODO: insert the central concept, notation, or derivation
    \item TODO: split dense material across approved slides
  \end{itemize}
\end{frame}
""",
            "03_examples.tex": r"""\section{Examples and Applications}
\begin{frame}{Worked Example or Exercise}
  TODO: insert the user-approved example, exercise, or discussion prompt
\end{frame}
""",
            "04_summary.tex": r"""\section{Summary}
\begin{frame}{Takeaways}
  \begin{itemize}
    \item TODO: summarize the three most important takeaways
  \end{itemize}
\end{frame}
""",
        }

    if language == "zh":
        return {
            "01_motivation.tex": r"""\section{研究动机}
\begin{frame}{研究动机}
  \begin{itemize}
    \item TODO：说明研究问题为何重要
    \item TODO：明确已有文献中的缺口
  \end{itemize}
\end{frame}
""",
            "02_design.tex": r"""\section{研究设计}
\begin{frame}{数据与方法}
  \begin{itemize}
    \item TODO：插入经用户确认的数据、样本与方法
  \end{itemize}
\end{frame}
""",
            "03_results.tex": r"""\section{主要结果}
\begin{frame}{主要结果}
  \begin{itemize}
    \item TODO：仅插入用户提供或确认过的结果
  \end{itemize}
\end{frame}
""",
            "04_conclusion.tex": r"""\section{结论}
\begin{frame}{结论}
  \begin{itemize}
    \item TODO：总结研究发现、贡献与含义
  \end{itemize}
\end{frame}
""",
        }
    return {
        "01_motivation.tex": r"""\section{Motivation}
\begin{frame}{Motivation}
  \begin{itemize}
    \item TODO: explain why the question matters
    \item TODO: state the gap in prior work
  \end{itemize}
\end{frame}
""",
        "02_design.tex": r"""\section{Research Design}
\begin{frame}{Data and Method}
  \begin{itemize}
    \item TODO: insert user-confirmed data, sample, and method
  \end{itemize}
\end{frame}
""",
        "03_results.tex": r"""\section{Main Results}
\begin{frame}{Main Results}
  \begin{itemize}
    \item TODO: insert only user-supplied or user-confirmed findings
  \end{itemize}
\end{frame}
""",
        "04_conclusion.tex": r"""\section{Conclusion}
\begin{frame}{Conclusion}
  \begin{itemize}
    \item TODO: summarize findings, contribution, and implications
  \end{itemize}
\end{frame}
""",
    }


def write_sections(output_dir: Path, deck_type: str, language: str) -> list[str]:
    files = section_files(deck_type, language)
    for filename, content in files.items():
        (output_dir / "sections" / filename).write_text(content, encoding="utf-8")
    appendix = output_dir / "sections" / "90_appendix.tex"
    appendix.write_text(
        "\\appendix\n% TODO: add appendix slides only when requested or needed.\n",
        encoding="utf-8",
    )
    return [*files.keys(), "90_appendix.tex"]


def render_main(
    template_text: str,
    title: str,
    subtitle: str,
    author: str,
    institute: str,
    date: str,
    section_names: list[str],
) -> str:
    escaped_title = escape_latex(title)
    escaped_subtitle = escape_latex(subtitle)
    escaped_author = escape_latex(author)
    escaped_institute = escape_latex(institute)
    escaped_date = escape_latex(date)
    values = {
        "{{TITLE}}": escaped_title,
        "{{SHORT_TITLE}}": short_text(escaped_title, "Slides"),
        "{{SUBTITLE}}": escaped_subtitle,
        "{{AUTHOR}}": escaped_author,
        "{{INSTITUTE}}": escaped_institute,
        "{{SHORT_INSTITUTE}}": short_text(escaped_institute, "Institute"),
        "{{DATE}}": escaped_date,
        "{{SECTION_INPUTS}}": "\n".join(
            f"\\input{{sections/{Path(name).stem}}}" for name in section_names
        ),
    }
    rendered = template_text
    for placeholder, value in values.items():
        rendered = rendered.replace(placeholder, value)
    if not subtitle.strip():
        # An empty subtitle renders as `\subtitle{ }`. The SJTU cover treats
        # that whitespace as a non-empty subtitle and then crashes on a
        # trailing `\\` ("There's no line here to end"). Drop the line so
        # `\insertsubtitle` stays genuinely empty. Behaviour is unchanged for
        # the other variants, where an empty subtitle shows nothing anyway.
        rendered = re.sub(
            r"(?m)^[ \t]*\\subtitle\{[ \t]*\}[ \t]*\n", "", rendered
        )
    return rendered


def write_references(output_dir: Path) -> None:
    (output_dir / "references.bib").write_text(
        "% Add user-supplied bibliography entries here.\n"
        "% Used for inline author-year citations (e.g., Gul, Wu, and Yang 2013).\n"
        "% No references/bibliography slide is generated by default; add one only if requested.\n"
        "% Do not invent references to fill space.\n",
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    skill_root = Path(__file__).resolve().parents[1]
    template_dir = skill_root / "assets" / "templates" / args.template
    prepare_output_dir(args.output_dir, args.force)
    copy_template_assets(template_dir, args.output_dir)
    sections = write_sections(args.output_dir, args.deck_type, args.language)
    template_text = (template_dir / "main.tex.template").read_text(encoding="utf-8")
    main_tex = render_main(
        template_text=template_text,
        title=args.title,
        subtitle=args.subtitle,
        author=args.author,
        institute=args.institute,
        date=args.date,
        section_names=sections,
    )
    (args.output_dir / "main.tex").write_text(main_tex, encoding="utf-8")
    write_references(args.output_dir)
    print(f"Created {args.deck_type} starter project with the {args.template} template at {args.output_dir}")


if __name__ == "__main__":
    main()
