# 🐍 Python Mini-Projects Collection

A curated collection of command-line applications and algorithmic challenges built to master Python fundamentals, control flow, and data structures.

## 🎯 Purpose
As an aspiring data analyst, this repository serves as a foundational sandbox. Each project targets specific programming paradigms essential for data manipulation, including complex state management, list/dictionary operations, variable scope, and algorithmic logic.

## 🗂️ Project Index

| Project Name                                       | Core Concepts Mastered |
|:---------------------------------------------------| :--- |
| **[Blackjack](./blackjack)**                       | Capstone Project: Complex conditional logic, dynamic list mutation (handling Aces), and asynchronous game states via nested `while` loops. |
| **[Higher Lower](./higher_lower)**                 | Lists of Dictionaries: Data extraction, comparison algorithms, and conditional variable swapping (King of the Hill variant). |
| **[Calculator](./calculator)**                     | First-Class Functions: Storing mathematical operations within dictionaries for dynamic execution, recursive application state resets. |
| **[Secret Auction](./blind_auction)**              | Dictionaries: Dynamic key-value generation, continuous user input parsing, and custom maximum-value calculation algorithms. |
| **[Number Guessing Game](./number_guessing_game)** | Variable Scope: Managing global vs. local scope, utilizing parameters and return values, and defining Global Constants for config states. |
| **[Hangman](./hangman)**                           | State Management: String manipulation, list evaluation, and multi-file modular architecture. |
| **[Caesar Cipher](./caesar_cypher)**               | List Indexing: Dynamic list index wrapping via modulo arithmetic to handle encryption/decryption state shifts. |
| **[Reeborg Maze/Hurdles](./reeborg_maze)**         | Algorithmic Logic: Developing pathfinding solutions (Right Wall Follower) using strict `while` and `if/elif` controls. |
| **[Hirst Painting](./hirst_painting)**             | External Package Integration: Extracting color palettes with `colorgram`, nested loops with modulo-based row offsets, and vector-based coordinate geometry using `turtle`. |
| [Snake Game](./snake_game) | OOP Architecture: Multi-class game engine (`Snake`, `Food`, `Scoreboard`), list segment shifts, coordinate collision detection, and persistent high-score tracking via File I/O. |
| [Pong Arcade Game](./pong_game) | 2D Vector Physics: Dual-paddle state management, dynamic speed scaling via sleep intervals, coordinate collision reflection math, and dual-player score tracking. |
| [Turtle Crossing](./turtle_crossing) | Dynamic Pipeline Mechanics: Object spawner throttling (`1-in-6` frame rolls), multi-target distance collision checks, and game-loop difficulty acceleration. |
| [Mail Merge Generator](./mail_merge) | File Processing & Batch Automation: Dynamic relative file pathing, relative I/O stream reading/writing, and string manipulation (`strip()`, `replace()`). |
| [U.S. States Game](./us_states_game) | Data Visualization & Game Logic: Pandas CSV ingestion, dynamic coordinate mapping via Turtle, and missing state export. |
| [Squirrel Census Analysis](./squirrel_census_analysis) | Data Aggregation & EDA: Pandas value counts, color filtering on NYC Central Park census data, and DataFrame CSV exports. |
| [NATO Alphabet Converter](./nato_alphabet) | Data Mapping & Comprehension: Ingesting CSV lookup tables via Pandas `.iterrows()`, dictionary comprehension construction, and string iteration mapping. |
| [Turtle Race](./turtle_race) | Interactive Event Loops: Object-oriented turtle array instantiation, user bet input state, and randomized coordinate physics (`random.randint`). |
| [Etch-A-Sketch](./etch_a_sketch) | Event-Driven Programming: Higher-order functions, event listeners (`screen.onkey`), canvas state clearing, and turtle coordinate resets. |
| [Mile to Km Converter](./tkinter) | Desktop GUI Development: Tkinter widget positioning with `.grid()`, padding, dynamic label configuration (`.config()`), and event-driven entry parsing. |
| [Pomodoro App](./pomodoro_app) | Desktop GUI & Dynamic Loops: Tkinter `Canvas` widget image layering, recursive non-blocking loops with `window.after()`, and session state management. |
| [Password Manager](./password_manager) | Desktop GUI & File Persistence: Tkinter layout, `messagebox` dialog validation, dynamic password generation, and local text/data file I/O. |
| [Flash Card App](./flash_card) | **Capstone GUI & Data Persistence**: Language learning desktop application built with Tkinter and Pandas. Features asynchronous card flipping (`window.after`), dynamic progress tracking with CSV serialization (`words_to_learn.csv`), and fallback error handling. |
| [Kanye Quotes App](./kanye_quotes) | **API Integration & Tkinter GUI**: Live REST API consumption using `requests.get()`, HTTP response validation (`raise_for_status()`), dynamic JSON payload extraction, and canvas text wrapping. |
| [ISS Overhead Notifier](./ISS_overhead) | **Automated API & SMTP Alert System**: Automated tracking of the International Space Station coordinates via Open-Notify API, sunrise/sunset calculations, position boundary checks ($\pm 5^\circ$), and email alerting via `smtplib`. |
| [Quizzler App](./quizzler) | **GUI & API Architecture**: Desktop trivia application built with Tkinter, Requests, and the Open Trivia DB API[cite: 4, 5]. Features modular OOP architecture[cite: 1, 2, 3, 4], Python type hinting[cite: 4], HTML entity unescaping (`html.unescape`)[cite: 3], and timed canvas visual feedback[cite: 4]. |
| [Monday Motivation Emailer](./monday_motivation) | **Automation & SMTPLib**: Automated weekly email dispatcher using `smtplib` and `datetime.weekday()` to parse quote files and send automated emails via secure TLS connections. |
| [Rain Alert SMS](./rain_alert) | **API Automation & SMS Notification**: Weather monitoring service consuming OpenWeatherMap API forecast data, slicing 12-hour predictive payload lists, evaluating weather condition codes (`id < 700`), and dispatching automated SMS alerts via Twilio. |
| [Stock News Alert](./stock_news) | **Multi-API Data Pipeline**: Automated financial monitoring service consuming Alpha Vantage and NewsAPI endpoints. Calculates day-over-day stock price deltas, flags volatility thresholds (>5%), and delivers contextual news briefs via Twilio. |

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Interface:** Command Line Interface (CLI)
* **Libraries Used:** `random`, `os`, `art` (custom ASCII modules)

## 🚀 How to Run
To run any of these projects locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/saicharanuchiha/python-mini-projects.git

2. Navigate into the specific project directory:

   ```bash
   cd python-mini-projects/blackjack

3. Execute the main Python file:

   ```bash
   python main.py
