# Getting Started with PyCharm: A Comprehensive Guide
## INTRODUCTION :-
With Jupyter Notebook integration available in PyCharm , you can easily edit, execute, and debug notebook source code and examine execution outputs including stream data, images, and other media.

Notebook support in `PyCharm` includes:

- Coding assistance:
- Error and syntax highlighting.
- Code completion.
- Ability to create line comments Ctrl0/.
- Ability to run cells and preview execution results.
- Dedicated `Jupyter Notebook` Debugger.
- Shortcuts for basic operations with Jupyter notebooks.
- Ability to recognize .ipynb files and mark them with the ipynb file icon icon.

## Jumpstart Your Jupyter Notebook Experience in PyCharm

To start working with Jupyter notebooks in PyCharm:
- Set Up Your Environment:
- Create a new Python project.
- Specify a virtual environment.
- Install the Jupyter package.
- Open or Create a Notebook:
- Open an existing `.ipynb` file or create a new one.
- Edit and Add Cells:
- Add and edit source cells in the notebook as needed.
- Execute Code Cells:

Execute any of the code cells to start the `Jupyter server` and run your code.

## Get familiar with the user interface

Mind the following user interface features when working with Jupyter notebooks in PyCharm.

# NOTEBOOK EDITOR
![image](https://github.com/dikshant182004/dfd/assets/122460149/7c0ff961-92c6-4c3c-a070-76db2ad3ee05)


Jupyter Notebook Interface Overview:

- Jupyter Notebook Toolbar: This toolbar provides quick access to frequently used actions. While additional notebook-specific actions are available in the` Cell menu`, this toolbar offers convenient shortcuts for common tasks.
- Code Cell: A code cell within the notebook is where you write and execute executable code. These cells are where you input your Python code for `analysis, calculations, or data manipulation.`
- Cell Output: After executing a code cell, the results are displayed in the` cell output area`. This output can take various forms, including text, tables, or plots, depending on the code's purpose and the libraries used.
- Cell Toolbar: The cell toolbar, typically hidden by default, contains essential commands for managing code cells. To enable this toolbar, navigate to Project Settings `(Ctrl+Alt+S)`, go to Languages & Frameworks | Jupyter, and check the "Show cell toolbar" option. Once enabled, it provides shortcuts and options for working with code cells efficiently.

## Cell toolbar﻿

Each code cell has its configurable toolbar so that you can easily access the most popular commands and actions. By default, `cell toolbars` are disabled. To enable them, open project Settings `(Ctrl+Alt+S)`, go to Languages & Frameworks | Jupyter, and select the Show cell toolbar checkbox.

| Symbol | Toolbar Element                | Description                                                      |
| ------ | ----------------------------- | ---------------------------------------------------------------- |
| ![image](https://github.com/dikshant182004/dfd/assets/122460149/a2176411-d0db-4686-ad57-1963bf23f3e7) | Run Cell                    | Executes the code cell. You can also press Ctrl+Enter to run the code cell. |
| ![image](https://github.com/dikshant182004/dfd/assets/122460149/1382d157-bade-4d5c-801c-4f8a8911a81d) | Run Cell and Select Below    | Executes this cell and selects the cell below. Press Shift+Enter to perform the same action. |
| ![image](https://github.com/dikshant182004/dfd/assets/122460149/a321fea9-f437-432c-8046-0066c0085542) | Move Cell Up                | Moves the current cell up.                                      |
| ![image](https://github.com/dikshant182004/dfd/assets/122460149/7b254910-6817-423c-b15c-504943f5dc9a) | Move Cell Down              | Moves the current cell down.                                    |
| ![image](https://github.com/dikshant182004/dfd/assets/122460149/7f3a20d6-b884-4cb0-94e0-f222c3c80320) | Delete Cell                 | Deletes the current cell.                                        |
| ![image](https://github.com/dikshant182004/dfd/assets/122460149/33d4f96e-d250-4bcf-8cc6-02548fd79342) | More Options                | Open the list of `additional actions`:                              |
|        | Run All Above                | Executes all cells that preceded the selected cell.               |
|        | Debug Cell                   | Runs the `Debugger` for the current cell. You should set a breakpoint first. Click the gutter next to the line where you want to stop. |
|        | Merge Cell Above              | Merges the current cell with the cell above.                       |
|        | Merge Cell Below              | Merges the current cell with the cell below.                       |
|        | Split Cell                   | Splits the current cell by the selected code line.                |
|        | Convert Cell to Code         | Converts the current cell into a code cell.                       |
|        | Convert Cell to Markdown     | Converts the current cell into a Markdown cell.                   |

## Notebook toolbar
The Jupyter notebook toolbar provides quick access to all basic operations with notebooks:

![image](https://github.com/dikshant182004/dfd/assets/122460149/e94cf60b-31f1-4e92-b0e6-66279917ce9f)

| Toolbar Element                | Description                                                                                                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![New Cell](https://github.com/dikshant182004/dfd/assets/122460149/77cee660-0e4f-4d8d-a4d5-2291030d5e12)               | Adds a code cell below the selected cell.                                                                                                                                |
| ![Cut](https://github.com/dikshant182004/dfd/assets/122460149/264a9a8a-c850-4bb9-8fc1-69d495112bc3)                   | Moves the selected item or items from the current location to the clipboard. Moves the entire cell if it's selected.                                                     |
| ![Copy](https://github.com/dikshant182004/dfd/assets/122460149/4085834f-52c2-4d89-82af-69ba6b2b0f83)                  | Copies the selected item or items to the clipboard. Copies the entire cell if it's selected.                                                                          |
| ![Paste](https://github.com/dikshant182004/dfd/assets/122460149/386bd062-0a77-4fbb-8d0f-b1847cc750f3)                 | Inserts the contents of the clipboard into the selected location. If you've selected an entire cell, the contents are pasted to a new cell below the selected one.    |
| ![Move Cell Up](https://github.com/dikshant182004/dfd/assets/122460149/34c2a2d4-eb3b-4ae6-acb0-8a5703b5ee14)        | Moves the current cell up.                                                                                                                                              |
| ![Move Cell Down](https://github.com/dikshant182004/dfd/assets/122460149/660fdab2-6370-4432-8aab-aca25d00bf5f)      | Moves the current cell down.                                                                                                                                            |
| ![Run Cell](https://github.com/dikshant182004/dfd/assets/122460149/14e40858-b97b-4dcc-8593-5c08a98887cd)             | Executes this cell and selects a cell below. If there is no cell below, PyCharm will create it.                                                                      |
| ![Debug Cell](https://github.com/dikshant182004/dfd/assets/122460149/06243011-bb3a-4f80-aaae-b74a1953a729)          | Starts debugging for this cell.                                                                                                                                         |
| ![Interrupt Kernel](https://github.com/dikshant182004/dfd/assets/122460149/85657cb3-3bfc-49b9-afba-202862293ab4)  | Click this icon if you want to interrupt any cell execution.                                                                                                            |
| ![Restart Kernel](https://github.com/dikshant182004/dfd/assets/122460149/39b073e3-2b3b-4505-962e-58c8377c3114)    | Click this icon to restart the currently running kernel.                                                                                                               |
| ![Run All Cells](https://github.com/dikshant182004/dfd/assets/122460149/36bf9b8f-c3df-415c-ba6d-6e547a770298)        | Executes all cells in the notebook.                                                                                                                                     |
| ![Cell Type](https://github.com/dikshant182004/dfd/assets/122460149/5b648748-b52d-4a92-8949-67f8a287f07a)         | You can select a cell type from this list and change the type for the selected cell.                                                                                 |
| ![Remove Cell](https://github.com/dikshant182004/dfd/assets/122460149/68201e5e-2f10-4f72-ac84-eb97876ec682)      | Deletes the current cell.                                                                                                                                               |
| ![List of Jupyter Servers](https://github.com/dikshant182004/dfd/assets/122460149/0bb9aa47-627f-445b-a296-9ce7134acf5e) | The Jupyter Server widget that shows the currently used Jupyter server. Click the widget and select Configure Jupyter Server to set up another local or remote Jupyter server. |
| ![List of Jupyter Kernels](https://github.com/dikshant182004/dfd/assets/122460149/0c3fdaed-fd62-41ce-b22a-152bc7081abd) | List of the available Jupyter kernels.                                                                                                                                  |
| ![Trusted JS Widgets](https://github.com/dikshant182004/dfd/assets/122460149/2cddf707-99d9-48a1-88df-8e76d443cfd4)   | Select this checkbox to allow executing JavaScript in your Jupyter notebook.                                                                                            |
| ![Select Cell Above](https://github.com/dikshant182004/dfd/assets/122460149/30c2b5d7-5a52-4f60-86cd-cc76c8e9324a)    | This action selects the cell above.                                                                                                                                     |
| ![Select Cell Below](https://github.com/dikshant182004/dfd/assets/122460149/582bacbc-805a-4ce2-9f5f-af535fe85a11)    | This action selects the cell below.                                                                                                                                     |
| ![Open Notebook in Browser](https://github.com/dikshant182004/dfd/assets/122460149/a1c2a235-a64a-4c65-b07a-3c18a5c7784c) | You can preview the notebook in a browser.                                                                                                                              |
## Tool windows
The `Server Log` tab within the Jupyter tool window becomes accessible once you launch a Jupyter server. Within this tab, you can monitor the `real-time status` of the Jupyter server and conveniently access the link to open your notebook in a web browser.

![image](https://github.com/dikshant182004/dfd/assets/122460149/36f655ed-6151-404f-aaa3-282decf5615f)

It also provides controls to stop the running server (`Stop the server`(![image](https://github.com/dikshant182004/dfd/assets/122460149/25198203-5dd2-491d-b4a8-352cb7364ced)
)) and launch the stopped server (`Run the server`(![image](https://github.com/dikshant182004/dfd/assets/122460149/0d15e38c-eb8e-4e4c-bf14-ee83ed0dd1b7)
)).

## CONCLUSION :-
The `Jupyter Variables` tool window the detailed report about variable values of the executed cell.

![image](https://github.com/dikshant182004/dfd/assets/122460149/14130547-3a10-4bf2-abd3-bf95f13e548a)

You can use the Settings icon to [manage the variables loading policy](https://www.jetbrains.com/help/pycharm/variables-loading-policy.html)https://www.jetbrains.com/help/pycharm/variables-loading-policy.html.




