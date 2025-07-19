# Code4Training

This repository holds code samples as we progress through the week. The samples will be updated and added as we advance through different topics and exercises during the training sessions.

## How to Pull from Code Repository

To get the latest updates from this repository, you can use either the command line or GitHub Desktop.

### Option 1: Using Command Line

#### 1. Clone the Repository (First Time)
```bash
git clone https://github.com/[username]/code4training.git
cd code4training
```

#### 2. Pull Latest Changes (Subsequent Updates)
```bash
git pull origin main
```

#### 3. Check Status
```bash
git status
```

This will show you any local changes and confirm you have the latest version from the remote repository.

#### Tips:
- Always pull before starting work to ensure you have the latest code samples
- If you have local changes, consider stashing them before pulling: `git stash`
- After pulling, you can restore your changes with: `git stash pop`

### Option 2: Using GitHub Desktop

If you prefer a graphical interface, you can use GitHub Desktop:

#### 1. Download and Install
- Download GitHub Desktop from [desktop.github.com](https://desktop.github.com/)
- Install and sign in with your GitHub account

#### 2. Clone the Repository (First Time)
- Click "Clone a repository from the Internet"
- Enter the repository URL: `https://github.com/[username]/code4training.git`
- Choose where to save it on your computer
- Click "Clone"

#### 3. Pull Latest Changes (Subsequent Updates)
- Open GitHub Desktop
- Select the code4training repository from the left sidebar
- Click "Fetch origin" to check for updates
- If updates are available, click "Pull origin" to download them

#### 4. Check for Changes
- GitHub Desktop will show you any local changes in the "Changes" tab
- The "History" tab shows recent commits and updates

#### Benefits of GitHub Desktop:
- Visual representation of changes and history
- Easy to see what files have been modified
- No need to remember command line syntax
- Built-in merge conflict resolution tools

## Setting Up Your Development Environment with Conda

After cloning or pulling the repository, you'll need to set up a Python environment to run the code samples. We recommend using conda with Python 3.12.

### Prerequisites
- Install [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Miniconda is a lighter option if you prefer a minimal installation

### Creating and Activating the Environment

**Recommended: Use Anaconda Prompt** (search for "Anaconda Prompt" in your Start menu)

#### 1. Create a New Conda Environment
```bash
conda create -n code4training python=3.12
```

#### 2. Activate the Environment
```bash
conda activate code4training
```

#### 3. Verify Python Version
```bash
python --version
```
This should show Python 3.12.x

#### 4. Install Required Packages
Navigate to the specific week/project directory and install requirements:
```bash
# Example for Week1 projects
cd Week1/simple_openai
pip install -r requirements.txt
```

#### 5. Deactivate When Done
```bash
conda deactivate
```

**Note**: While you can use regular PowerShell or Command Prompt, **Anaconda Prompt is strongly recommended** as it comes pre-configured with conda and avoids many common issues.

### Tips for Conda Environment Management:
- Always activate your environment before working: `conda activate code4training`
- You can list all environments with: `conda env list`
- To remove the environment if needed: `conda env remove -n code4training`
- Each project folder may have its own `requirements.txt` file - install packages accordingly
- Consider creating separate environments for different weeks if package conflicts arise

### Troubleshooting Conda on Windows

**First Try: Use Anaconda Prompt (Strongly Recommended)**
- Search for "Anaconda Prompt" in your Start menu
- Open "Anaconda Prompt" (not regular Command Prompt or PowerShell)
- Run your conda commands from there:
```bash
conda create -n code4training python=3.12
conda activate code4training
```
This avoids most Windows-specific conda issues and is the most reliable approach.

#### If You Must Use PowerShell: Initialize Conda First
If you prefer using PowerShell, initialize conda first:
```powershell
# Run this once to initialize conda in PowerShell
conda init powershell
```
Then restart PowerShell and try the conda commands again.

#### Option 3: Add Conda to PATH (Advanced)
If conda still isn't recognized:
1. Find your Anaconda/Miniconda installation path (usually `C:\Users\[username]\anaconda3` or `C:\ProgramData\Anaconda3`)
2. Add these paths to your system PATH environment variable:
   - `C:\Users\[username]\anaconda3`
   - `C:\Users\[username]\anaconda3\Scripts`
   - `C:\Users\[username]\anaconda3\Library\bin`
3. Restart your terminal

#### Quick Test
To verify conda is working, run:
```bash
conda --version
```

#### If You Get "Run 'conda init' before 'conda activate'" Error

This is a common initialization issue. Follow these steps:

1. **First, run conda init:**
```bash
conda init
```

2. **Close and restart your terminal/Anaconda Prompt completely**

3. **Now try creating and activating your environment:**
```bash
conda create -n code4training python=3.12
conda activate code4training
```

If you're still having issues, try this alternative approach:

1. **Create the environment without activating:**
```bash
conda create -n code4training python=3.12
```

2. **Use the full path to activate (replace [username] with your actual username):**
```bash
# On Windows
C:\Users\[username]\anaconda3\Scripts\activate code4training

# Or try
conda activate code4training
```

3. **Verify you're in the correct environment:**
```bash
python --version
conda info --envs
```

The environment name should appear in your prompt like: `(code4training) C:\>`

#### If PowerShell Doesn't Show the Environment Name

If your environment is activated but PowerShell doesn't show `(code4training)` in the prompt, try these solutions:

1. **Check if conda is properly initialized for PowerShell:**
```powershell
conda init powershell
```

2. **Restart PowerShell completely** (close and reopen)

3. **Check PowerShell execution policy:**
```powershell
Get-ExecutionPolicy
```
If it shows "Restricted", change it:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

4. **Verify the environment is actually active:**
```bash
conda info --envs
python --version
```
The active environment will have an asterisk (*) next to it.

5. **Force activate with explicit path:**
```powershell
& "C:\Users\[username]\anaconda3\Scripts\activate.bat" code4training
```

6. **Alternative: Use Anaconda Prompt instead**
- Search for "Anaconda Prompt" in Start menu
- This usually shows environment names correctly by default

**Quick verification**: Even if the prompt doesn't change, you can confirm you're in the right environment by running `python --version` - it should show Python 3.12.x
