{
  pkgs ? import <nixpkgs> {}
}:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.python310Packages.pip
  ];

  shellHook = ''
    echo "📦 Установка зависимостей из requirements.txt..."
    pip install --no-cache-dir -r requirements.txt
  '';
}
