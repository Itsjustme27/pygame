{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312Full
    pkgs.python312Packages.pygame
  ];

  shellHook = ''
    echo "Pygame environment is ready!"
    python3 --version
  '';
}

