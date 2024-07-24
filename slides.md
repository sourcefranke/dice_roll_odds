---
theme: seriph
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
title: Dice Roll Odds
mdc: true
---

<style>
    .sources {
        @apply flex justify-end text-xs align-self-end mt-2;
    }
</style>

# Dice Roll Odds
## About techniques of presenting for developers 

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2 items-baseline opacity-50">
    <span class="text-s">
        (c) 2024 Lukas Tietenberg,
        v2024-01-10
    </span>
    <a href="https://github.com/sourcefranke/session_software_licenses" target="_blank" alt="GitHub"
        class="text-xl slidev-icon-btn !border-none !hover:text-white">
        <carbon-logo-github />
    </a>
</div>


---

# License
Some obligatory stuff, you know ;)

<div class="flex justify-center">
<div class="text-xs" style="width: 80%">
MIT License

Copyright (c) 2024 Lukas Tietenberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</div>
</div>

<div class="sources">
    <span>
        Source:
        <a href="https://github.com/sourcefranke/dice_roll_odds?tab=MIT-1-ov-file">
            https://github.com/sourcefranke/dice_roll_odds
        </a>
    </span>
</div>


---

# The Notebook

<iframe style="height: 80%; width: 100%; border-style: solid; border-width: thin;" src="odds/odds.html"></iframe>

<div class="sources">
    <span>Powered by <a href="https://jupyter.org/">Jupyter Notebook</a></span>
</div>


---

# Closer look (1)

````python
def cartesian(die, number_dice=1, acc_func=lambda x, y: x + y):
    """
    :param die: list of possible values of one die roll
    :param number_dice: how many dice to be used
    :param acc_func: function for accumulating the values from both dice
    :return: list of all possible combinations of results for the dice roll
    """
    if number_dice < 1:
        return []

    if number_dice == 1:
        return die

    accumulated = []
    for x in cartesian(die, number_dice - 1, acc_func):
        for y in die:
            accumulated.append(acc_func(x, y))

    return accumulated
````


---

# Closer look (1)

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAjIAAAHHCAYAAACle7JuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy80BEi2AAAACXBIWXMAAA9hAAAPYQGoP6dpAABNu0lEQVR4nO3de3zO9f/H8cdlbMxONmbDMKfI+Zxj0py+JVI5zTEpcgihlAol0UGpyCGnsuhAZ+dCTuW0L0pCRDmGbbYxs31+f7y/9ms5bWz7XNe15/12u27f7/vz+ey6XrZqT++jw7IsCxEREREXlMfuAkRERERuloKMiIiIuCwFGREREXFZCjIiIiLishRkRERExGUpyIiIiIjLUpARERERl6UgIyIiIi5LQUZERERcloKMiORKY8aMweFwpLtWunRpevXqZU9BInJTFGREJMv8/PPPdOvWjeLFi+Pl5UWxYsWIjIzk559/trs0EXFTee0uQETcw+LFi+nSpQuBgYH06dOH8PBwDh06xPvvv8+nn37KwoULuf/+++0u87r27t1Lnjz6+52IK1GQEZFbduDAAbp3706ZMmVYt24dRYoUSbv3xBNP0KRJE7p3787OnTspU6aMjZVen5eXl90liEgm6a8eInLLXn31VRITE5kxY0a6EANQuHBhpk+fTkJCApMmTUq7fnmOyv79++nVqxcBAQH4+/vTu3dvEhMTr/iMDz/8kNq1a1OgQAECAwPp3LkzR44cyVB969evp27duuTPn5+yZcsyffr0qz53tTkyMTExDBkyhLCwMLy8vChXrhwTJ04kNTU1Q58tItlLPTIicsu++uorSpcuTZMmTa56v2nTppQuXZpvvvnminsdO3YkPDycCRMmsH37dmbNmkVwcDATJ05Me2b8+PE899xzdOzYkUceeYRTp07x9ttv07RpU3bs2EFAQMA1a9u1axctW7akSJEijBkzhkuXLvHCCy9QtGjRG/65EhMTufPOO/nrr7947LHHKFmyJBs3bmTUqFEcO3aMN99884bvISLZzBIRuQUxMTEWYLVr1+66z913330WYMXFxVmWZVkvvPCCBVgPP/xwuufuv/9+KygoKK196NAhy8PDwxo/fny653bt2mXlzZv3iuv/1r59eyt//vzWH3/8kXbtl19+sTw8PKx//yewVKlSVs+ePdPaL774olWw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"/>