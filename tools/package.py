#!/usr/bin/env python3
"""
tools/package.py

Empaqueta el contenido del repositorio en un tar.gz llamado por defecto
"guia2-alma.de.litio.tar.gz". Este script es multiplataforma y detecta
el sistema operativo para mostrar información útil, pero usa la librería
standard `tarfile` para crear el archivo, por lo que funciona tanto en
Windows como en Linux/macOS siempre que Python esté disponible.

Exclusiones comunes: .git, __pycache__, .venv, venv, *.tar.gz, .ipynb_checkpoints

Uso:
  python tools/package.py --output guia2-alma.de.litio.tar.gz
"""
from __future__ import annotations

import argparse
import os
import platform
import tarfile
from pathlib import Path
from typing import Iterable, List


EXCLUDE_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", "venv", ".venv"}
EXCLUDE_SUFFIXES = {".tar.gz", ".zip"}


def should_exclude(path: Path) -> bool:
    # Exclude hidden VCS and virtual env folders, and output archives
    parts = {p.name for p in path.parents} | {path.name}
    if parts & EXCLUDE_DIRS:
        return True
    if any(path.name.endswith(suf) for suf in EXCLUDE_SUFFIXES):
        return True
    return False


def iter_files(root: Path) -> Iterable[Path]:
    for p in sorted(root.rglob("*")):
        # Skip directories themselves; tarfile will add files with relative paths
        if p.is_dir():
            continue
        # Skip the script itself if it's inside tools/
        if p.resolve() == Path(__file__).resolve():
            continue
        if should_exclude(p):
            continue
        yield p


def create_archive(output: Path, root: Path) -> List[str]:
    included: List[str] = []
    with tarfile.open(output, "w:gz") as tar:
        for f in iter_files(root):
            # Store files with relative paths
            arcname = f.relative_to(root)
            tar.add(f, arcname=str(arcname))
            included.append(str(arcname))
    return included


def main() -> int:
    parser = argparse.ArgumentParser(description="Crear paquete de entrega (tar.gz)")
    parser.add_argument("--output", "-o", default="guia2-alma.de.litio.tar.gz",
                        help="Nombre del archivo de salida (tar.gz)")
    parser.add_argument("--root", "-r", default=".", help="Carpeta raíz a empaquetar")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output).resolve()

    print(f"Sistema operativo detectado: {platform.system()} ({platform.platform()})")
    print(f"Empaquetando desde: {root}")
    print(f"Salida: {output}")

    if output.exists():
        print(f"Aviso: {output} ya existe y será sobrescrito")
        output.unlink()

    included = create_archive(output, root)

    print(f"Archivo creado: {output} — contiene {len(included)} archivos")
    # Mostrar un resumen corto (hasta 20 entradas)
    for name in included[:20]:
        print(f"  - {name}")
    if len(included) > 20:
        print(f"  ... (+{len(included)-20} archivos más)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
