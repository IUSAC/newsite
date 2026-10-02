#!/bin/bash
# Synchronizacja między rozmowami (telefon / komputer): przy każdym otwarciu lub wznowieniu sesji
# pobiera aktualny stan gałęzi main i wypisuje, co doszło z innych rozmów. Nigdy nie przerywa startu sesji.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0
before=$(git rev-parse HEAD 2>/dev/null)
if ! timeout 60 git fetch -q --depth=50 origin +refs/heads/main:refs/remotes/origin/main 2>/dev/null; then
  echo "SYNCHRONIZACJA: nie udało się pobrać stanu z GitHuba. Przed zmianą wykonaj: git pull --rebase origin main."
  exit 0
fi
new=$(git log --format='- %ad %s' --date=format:'%d.%m %H:%M' HEAD..origin/main 2>/dev/null | head -20)
if [ -z "$new" ]; then
  echo "SYNCHRONIZACJA: ta rozmowa ma aktualny stan gałęzi main."
  exit 0
fi
if [ -z "$(git status --porcelain 2>/dev/null)" ] && timeout 60 git rebase -q origin/main >/dev/null 2>&1; then
  echo "SYNCHRONIZACJA: pobrano zmiany z innych rozmów (telefon / komputer). Powiedz właścicielowi krótko, co doszło:"
else
  git rebase --abort >/dev/null 2>&1
  echo "SYNCHRONIZACJA: na main są nowe zmiany z innych rozmów, ale tu są niezapisane pliki. Przed dalszą pracą wykonaj git pull --rebase origin main. Nowe zmiany:"
fi
echo "$new"
echo "Przeczytaj też „Dziennik pracy” w pliku projektu (ustalenia z rozmów, których nie ma w kodzie)."
exit 0
