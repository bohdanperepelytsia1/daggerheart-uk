# Daggerheart — українська локалізація для Foundry VTT

Переклад інтерфейсу та компендіумів системи [Daggerheart (Foundryborne)](https://github.com/Foundryborne/daggerheart). Для приватного використання групою.

## Встановлення
1. Встановіть модуль **Babele** (2.7.5+).
2. Foundry → *Add-on Modules* → *Install Module* → у полі **Manifest URL** вставте:
   `https://github.com/bohdanperepelytsia1/daggerheart-uk/releases/latest/download/module.json`
3. Увімкніть у світі **Babele** і **Daggerheart — українська локалізація**.
4. *Configure Settings* → *Core* → *Language* → **Українська**, перезавантажте.

## Що перекладено
- Інтерфейс системи (весь `lang/en.json`).
- Класи, підкласи, домени, походження, спільноти, зброя, броня, витратні речі, здобич, звірині подоби, перетворення — 100 %.
- Супротивники (264) та оточення (47) — 100 %.
- Журнали й таблиці кидків — у процесі (поки англійською).

## Оновлення системи
Переклад прив'язаний до англійських назв, тому нові версії Daggerheart не ламають модуль: нове або змінене просто лишається англійською, доки не перекладене. Максимальної версії системи в маніфесті немає.

Для перекладу нових рядків: `dev/refresh.sh <тег системи>` → перекласти `dev/work/n*.src.tsv` у `dev/tm/` → зібрати → підняти `version` у `module/module.json` і запушити в main (GitHub Actions сам створить реліз).

## Ліцензія
Код — MIT (конвертери Babele адаптовано з [fvtt-daggerheart-ru](https://github.com/bmpolonsky/fvtt-daggerheart-ru)). Текст — похідні матеріали Daggerheart SRD 2.0 © Critical Role, LLC, за DPCGL.
