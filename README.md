# Translater

A desktop translation application built with Python.

## Project Structure

- `main.py` - Main application source code.
- `main.spec` - PyInstaller spec file for building the executable.
- `icon.ico` - Application icon.
- `build/` - Output directory generated by PyInstaller, containing the packaged application and related files.

## How to Run

1. Make sure you have Python 3.11 installed.
2. Install required dependencies (if any).
3. Run the application:

   ```sh
   python main.py
   ```

## How to Build Executable

This project uses PyInstaller to create a standalone executable.

1. Install PyInstaller:

   ```sh
   pip install pyinstaller
   ```

2. Build the executable:

   ```sh
   pyinstaller main.spec
   ```

The output will be in the `build/` directory.

## License

See `tk/license.terms` for third-party license information.
