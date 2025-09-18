# KidsNetworkBuilder

This tool replaces the Powerpuff Girls video in the Sims 4 Kids Network mod with your own WebM video.

## How to use

1. Create a new repository on GitHub.
2. Upload these files into the repository (click **Add file → Upload files**).
3. Go to the **Actions** tab in your repo. GitHub will automatically build the `.exe`.
4. After the workflow finishes, download the compiled `KidsNetworkBuilder.exe` from the Actions artifacts.

## Usage

Once you have the `.exe`, put it in the same folder as:
- Your base `.package` file (e.g. `thepowerpuffgirls_Kidsnetwork_MidniteHearts.package`)
- Your new video file (e.g. `Mermaid Melody Opening 1.webm`)

Run from Command Prompt:

```bash
KidsNetworkBuilder.exe thepowerpuffgirls_Kidsnetwork_MidniteHearts.package "Mermaid Melody Opening 1.webm"
```

It will create a new `Kids-Network-1.package` ready for your Sims 4 Mods folder.
