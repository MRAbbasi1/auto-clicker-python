# 🖱️ Python Auto Clicker

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.54-orange.svg)](https://pypi.org/project/PyAutoGUI/)

A simple yet powerful Python-based auto clicker that automates mouse clicks at specific screen coordinates using the `pyautogui` library. Perfect for automating repetitive clicking tasks with precision and control.

## ✨ Features

- 🎯 **Precise Clicking** - Click on up to 3 pre-defined screen positions
- ⏱️ **Customizable Delays** - Set custom intervals between clicks
- 🔄 **Repeat Control** - Specify exact number of click repetitions
- 📍 **Coordinate Helper** - Built-in tool to capture mouse coordinates
- 🛡️ **Safety Features** - Built-in failsafes to prevent accidents
- 🖥️ **Cross-Platform** - Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MRAbbasi1/auto-clicker-python.git
   cd auto-clicker-python
   ```

2. **Install dependencies:**
   ```bash
   pip install pyautogui
   ```

   Or install from requirements file:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Step 1: Get Target Coordinates
```bash
python3 get_mouse_position.py
```
- Move your mouse to the desired clicking position within 5 seconds
- The script will display the coordinates (x, y) in the terminal
- Repeat for multiple positions if needed

#### Step 2: Configure and Run Auto-Clicker
```bash
python3 auto_clicker.py
```

**⚠️ Important:** Do not move your mouse while the auto-clicker is running!

## 📁 Project Structure

```
auto-clicker-python/
├── auto_clicker.py          # Main auto-clicker script
├── get_mouse_position.py    # Coordinate capture utility
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore             # Git ignore rules
```

## ⚙️ Configuration

### Customizing Click Positions

Edit the coordinates in `auto_clicker.py`:

```python
# Define your target coordinates
positions = [
    (100, 200),  # Position 1 (x, y)
    (300, 400),  # Position 2 (x, y)
    (500, 600)   # Position 3 (x, y)
]
```

### Adjusting Click Settings

```python
# Customize these parameters
CLICK_DELAY = 1.0        # Seconds between clicks
REPEAT_COUNT = 10        # Number of times to repeat
CLICK_DURATION = 0.1     # Click hold duration
```

## 🛡️ Safety Features

- **Failsafe Protection**: Move mouse to top-left corner to emergency stop
- **Coordinate Validation**: Ensures click positions are within screen bounds
- **Error Handling**: Graceful handling of exceptions and interruptions
- **Pre-execution Delay**: 3-second countdown before starting clicks

## 🔧 Advanced Usage

### Command Line Arguments (Future Enhancement)

```bash
python3 auto_clicker.py --delay 0.5 --repeat 20 --position 100,200
```

### Keyboard Shortcuts

- `Ctrl+C`: Emergency stop during execution
- Mouse movement to `(0,0)`: Automatic failsafe trigger

## 📋 Example Use Cases

- **Software Testing**: Automated UI testing and regression testing
- **Game Automation**: Farming, idle games, and repetitive tasks
- **Productivity**: Automating repetitive office tasks
- **Web Scraping**: Automated form filling and data collection
- **Accessibility**: Assistance for users with motor difficulties

## 🚨 Important Warnings

> **Educational Use Only**: This tool is designed for educational purposes and legitimate automation tasks.

- ❌ Do not use to violate terms of service of any application or game
- ❌ Do not use for malicious purposes or unauthorized access
- ❌ Do not use to gain unfair advantages in competitive environments
- ✅ Always respect application policies and user agreements
- ✅ Use responsibly and ethically

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'pyautogui'`
```bash
# Solution
pip install --upgrade pyautogui
```

**Issue**: Permission denied on macOS
```bash
# Solution: Grant accessibility permissions
System Preferences > Security & Privacy > Accessibility
```

**Issue**: Clicks not registering
- Ensure coordinates are correct using `get_mouse_position.py`
- Check if target application is in focus
- Verify screen resolution hasn't changed

### Performance Tips

- Use appropriate delays to avoid overwhelming target applications
- Test with small repeat counts first
- Monitor system resources during execution

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/auto-clicker-python.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyAutoGUI](https://pyautogui.readthedocs.io/) - For the excellent automation library
- Python community for continuous support and resources
- Contributors who help improve this project

## 📞 Support

- 🐛 **Bug Reports**: [Create an issue](https://github.com/MRAbbasi1/auto-clicker-python/issues)
- 💡 **Feature Requests**: [Create an issue](https://github.com/MRAbbasi1/auto-clicker-python/issues)
- 📧 **Contact**: Open an issue for any questions

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/MRAbbasi1/auto-clicker-python?style=social)
![GitHub forks](https://img.shields.io/github/forks/MRAbbasi1/auto-clicker-python?style=social)
![GitHub issues](https://img.shields.io/github/issues/MRAbbasi1/auto-clicker-python)

---

<div align="center">

**Made with ❤️ by [MRAbbasi1](https://github.com/MRAbbasi1)**

⭐ **Star this repository if it helped you!** ⭐

</div>