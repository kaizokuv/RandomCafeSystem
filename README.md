# RandomCafeSystem

A CLI-based ordering system for a café with drinks, food, and desserts.

## Features
- View menu
- Order drinks, food, and desserts
- View current order and checkout
- More to come :D

## Why this exists
The first of many random posts that track my progress as a programmer. Starting off first, a simple ordering system based on python, a quick refresh on my skills for programming :D

The base of this stems from how I wanted to improve my skills in coding, and be more fluent, and so I figured, instead of being stuck in tutorial hell, might as well just code, and if something broke, I would learn to fix it.

So behold the first of many repos to come about my progress and improvement. If anyone who sees this has any tips, ideas or comments, just lemme know, all feedback is much appreciated.

## How to run
```bash
git clone https://github.com/kaizokuv/RandomCafeSystem.git
cd RandomCafeSystem
python3 main.py
```

## For those of you who are lazy and willing to tweak around with aliases
Now I don't know why you would actually want to run this, it do be a silly little program but oh well, it's your wish :D

Soooo, here are some aliases you guys can use for your terminal shells (bash, fish, zsh) to simplify calling the tool. 

Mind you you will still need to clone the repo first, and this is assuming you cloned the repo into your desktop and not a file. 

The alias will cd in a subshell so that once you're done using the tool, you'll go back to your original directory.

### For bash/zsh shell
```bash
alias rcs='(cd ~/RandomCafeSystem && python main.py)'
```
Change '~/RandomCafeSystem' to the desired file path if you want to set a custom file path

### For fish shell
```bash
function rsc
    pushd ~/RandomCafeSystem > /dev/null
    python main.py
    popd > /dev/null
end
```
Change '~/RandomCafeSystem' to the desired file path if you want to set a custom file path


# Thank you for using my tools :D
