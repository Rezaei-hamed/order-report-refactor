from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, kw_only=True)
class ReportConfig:
    input_path: Path
    output_dir: Path

