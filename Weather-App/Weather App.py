import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QFrame, QScrollArea
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont

# ── Mock weather data ────────────────────────────────────────────────────────

CITY_DATA = {
    "london":    {"temp": 13, "feels_like": 10, "humidity": 78, "wind": 19, "condition": "Cloudy",    "emoji": "☁️",  "high": 15, "low": 9},
    "new york":  {"temp": 22, "feels_like": 20, "humidity": 55, "wind": 14, "condition": "Sunny",     "emoji": "☀️",  "high": 25, "low": 18},
    "tokyo":     {"temp": 27, "feels_like": 30, "humidity": 82, "wind": 8,  "condition": "Humid",     "emoji": "🌫️", "high": 29, "low": 24},
    "paris":     {"temp": 18, "feels_like": 16, "humidity": 65, "wind": 11, "condition": "Partly Cloudy", "emoji": "⛅", "high": 20, "low": 14},
    "sydney":    {"temp": 24, "feels_like": 23, "humidity": 60, "wind": 22, "condition": "Windy",     "emoji": "🌬️", "high": 26, "low": 19},
    "dubai":     {"temp": 38, "feels_like": 42, "humidity": 40, "wind": 15, "condition": "Sunny",     "emoji": "☀️",  "high": 40, "low": 32},
    "moscow":    {"temp": -2, "feels_like": -7, "humidity": 85, "wind": 20, "condition": "Snowy",     "emoji": "❄️",  "high": 0,  "low": -5},
    "mumbai":    {"temp": 32, "feels_like": 37, "humidity": 88, "wind": 9,  "condition": "Stormy",    "emoji": "⛈️",  "high": 33, "low": 28},
    "berlin":    {"temp": 10, "feels_like": 7,  "humidity": 70, "wind": 16, "condition": "Rainy",     "emoji": "🌧️", "high": 12, "low": 7},
    "singapore": {"temp": 30, "feels_like": 35, "humidity": 90, "wind": 6,  "condition": "Thunderstorm","emoji":"⛈️","high": 31, "low": 27},
    "bhubaneswar":{"temp":34,"feels_like": 38,  "humidity": 75, "wind": 10, "condition": "Hot & Humid","emoji":"🌤️", "high": 36, "low": 28},
}

FORECAST_CONDITIONS = [
    ("☀️", "Sunny"),   ("⛅", "Partly Cloudy"), ("☁️", "Cloudy"),
    ("🌧️", "Rainy"),  ("⛈️", "Stormy"),        ("❄️", "Snowy"),
]

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def get_mock_weather(city: str) -> dict | None:
    key = city.strip().lower()
    if key in CITY_DATA:
        data = CITY_DATA[key].copy()
        data["city"] = city.title()
        return data
    # Generate random data for unknown cities
    cond = random.choice(FORECAST_CONDITIONS)
    temp = random.randint(-5, 40)
    return {
        "city": city.title(),
        "temp": temp,
        "feels_like": temp + random.randint(-4, 4),
        "humidity": random.randint(30, 95),
        "wind": random.randint(5, 30),
        "condition": cond[1],
        "emoji": cond[0],
        "high": temp + random.randint(1, 5),
        "low": temp - random.randint(1, 5),
    }

def get_mock_forecast(base_temp: int) -> list[dict]:
    forecast = []
    today_idx = 0
    for i in range(1, 6):
        cond = random.choice(FORECAST_CONDITIONS)
        delta = random.randint(-6, 6)
        t = base_temp + delta
        forecast.append({
            "day": DAYS[(today_idx + i) % 7],
            "emoji": cond[0],
            "condition": cond[1],
            "high": t + random.randint(1, 4),
            "low": t - random.randint(1, 4),
        })
    return forecast

# ── Fake network delay thread ────────────────────────────────────────────────

class FetchThread(QThread):
    result_ready = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, city: str):
        super().__init__()
        self.city = city

    def run(self):
        import time
        time.sleep(0.6)  # simulate network latency
        data = get_mock_weather(self.city)
        if data:
            data["forecast"] = get_mock_forecast(data["temp"])
            self.result_ready.emit(data)
        else:
            self.error.emit("City not found.")

# ── Stylesheet ───────────────────────────────────────────────────────────────

STYLESHEET = """
    QWidget {
        background-color: #0d1117;
        color: #e6edf3;
        font-family: Segoe UI;
    }

    QLineEdit {
        background-color: #161b22;
        border: 2px solid #30363d;
        border-radius: 10px;
        padding: 10px 16px;
        font-size: 16px;
        color: #e6edf3;
    }
    QLineEdit:focus {
        border: 2px solid #388bfd;
    }

    QPushButton#search_btn {
        background-color: #388bfd;
        color: white;
        font-size: 15px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
    }
    QPushButton#search_btn:hover   { background-color: #58a6ff; }
    QPushButton#search_btn:pressed { background-color: #1f6feb; }
    QPushButton#search_btn:disabled{ background-color: #1c2a3a; color: #4a6285; }

    QLabel#city_name {
        font-size: 36px;
        font-weight: bold;
        color: #e6edf3;
        padding-top: 10px;
    }
    QLabel#temp_main {
        font-size: 80px;
        font-weight: bold;
        color: #58a6ff;
        padding: 0px;
    }
    QLabel#condition {
        font-size: 20px;
        color: #8b949e;
    }
    QLabel#detail_val {
        font-size: 15px;
        color: #58a6ff;
        font-weight: bold;
    }
    QLabel#detail_key {
        font-size: 12px;
        color: #6e7681;
        letter-spacing: 1px;
    }
    QLabel#status {
        font-size: 13px;
        color: #6e7681;
        padding: 4px;
    }
    QLabel#section_title {
        font-size: 11px;
        letter-spacing: 3px;
        color: #6e7681;
        padding: 6px 0px 2px 0px;
    }

    QFrame#card {
        background-color: #161b22;
        border: 1px solid #21262d;
        border-radius: 14px;
    }

    QFrame#forecast_card {
        background-color: #161b22;
        border: 1px solid #21262d;
        border-radius: 10px;
        padding: 4px;
    }

    QLabel#forecast_day   { font-size: 13px; color: #8b949e; font-weight: bold; }
    QLabel#forecast_emoji { font-size: 22px; }
    QLabel#forecast_temp  { font-size: 13px; color: #58a6ff; }

    QListWidget {
        background-color: #161b22;
        border: 1px solid #21262d;
        border-radius: 10px;
        padding: 4px;
        font-size: 14px;
        color: #8b949e;
    }
    QListWidget::item { padding: 6px 10px; border-radius: 6px; }
    QListWidget::item:hover    { background-color: #1c2128; color: #e6edf3; }
    QListWidget::item:selected { background-color: #1f3a5f; color: #58a6ff; }

    QScrollArea { border: none; background: transparent; }
    QScrollBar:vertical {
        background: #0d1117; width: 6px; border-radius: 3px;
    }
    QScrollBar::handle:vertical {
        background: #30363d; border-radius: 3px;
    }
"""

# ── Main Window ──────────────────────────────────────────────────────────────

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.search_history: list[str] = []
        self.fetch_thread = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather")
        self.setStyleSheet(STYLESHEET)
        self.setMinimumSize(820, 620)

        # ── Search bar ──
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search city…  (try London, Tokyo, Mumbai…)")
        self.search_input.returnPressed.connect(self.do_search)

        self.search_btn = QPushButton("Search")
        self.search_btn.setObjectName("search_btn")
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.clicked.connect(self.do_search)

        search_row = QHBoxLayout()
        search_row.setSpacing(10)
        search_row.addWidget(self.search_input)
        search_row.addWidget(self.search_btn)

        # ── Status ──
        self.status_label = QLabel("Enter a city name to get started.")
        self.status_label.setObjectName("status")
        self.status_label.setAlignment(Qt.AlignCenter)

        # ── Weather card ──
        self.weather_card = self._build_weather_card()
        self.weather_card.hide()

        # ── Forecast row ──
        self.forecast_title = QLabel("5-DAY FORECAST")
        self.forecast_title.setObjectName("section_title")
        self.forecast_title.hide()

        self.forecast_row = QHBoxLayout()
        self.forecast_row.setSpacing(8)
        self.forecast_widgets = []
        for _ in range(5):
            w = self._build_forecast_card()
            self.forecast_row.addWidget(w)
            self.forecast_widgets.append(w)
            w.hide()

        forecast_container = QWidget()
        forecast_container.setLayout(self.forecast_row)

        # ── History ──
        history_title = QLabel("RECENT SEARCHES")
        history_title.setObjectName("section_title")

        self.history_list = QListWidget()
        self.history_list.setMaximumHeight(130)
        self.history_list.itemClicked.connect(self.search_from_history)

        # ── Root layout ──
        root = QVBoxLayout()
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(10)
        root.addLayout(search_row)
        root.addWidget(self.status_label)
        root.addWidget(self.weather_card)
        root.addWidget(self.forecast_title)
        root.addWidget(forecast_container)
        root.addWidget(history_title)
        root.addWidget(self.history_list)
        root.addStretch()
        self.setLayout(root)

    # ── Card builders ────────────────────────────────────────────────

    def _build_weather_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")

        self.city_label     = QLabel()
        self.city_label.setObjectName("city_name")
        self.city_label.setAlignment(Qt.AlignCenter)

        self.temp_label     = QLabel()
        self.temp_label.setObjectName("temp_main")
        self.temp_label.setAlignment(Qt.AlignCenter)

        self.cond_label     = QLabel()
        self.cond_label.setObjectName("condition")
        self.cond_label.setAlignment(Qt.AlignCenter)

        # Detail row: feels like / humidity / wind / hi-lo
        self.detail_widgets = {}
        detail_row = QHBoxLayout()
        detail_row.setSpacing(0)
        for key in ["Feels Like", "Humidity", "Wind", "Hi / Lo"]:
            col = QVBoxLayout()
            col.setAlignment(Qt.AlignCenter)
            val = QLabel("--")
            val.setObjectName("detail_val")
            val.setAlignment(Qt.AlignCenter)
            lbl = QLabel(key.upper())
            lbl.setObjectName("detail_key")
            lbl.setAlignment(Qt.AlignCenter)
            col.addWidget(val)
            col.addWidget(lbl)
            self.detail_widgets[key] = val

            wrapper = QWidget()
            wrapper.setLayout(col)
            detail_row.addWidget(wrapper)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(4)
        layout.addWidget(self.city_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.cond_label)
        layout.addSpacing(10)
        layout.addLayout(detail_row)
        card.setLayout(layout)
        return card

    def _build_forecast_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("forecast_card")

        day   = QLabel("---");  day.setObjectName("forecast_day");  day.setAlignment(Qt.AlignCenter)
        emoji = QLabel("--");   emoji.setObjectName("forecast_emoji"); emoji.setAlignment(Qt.AlignCenter)
        temp  = QLabel("--/--"); temp.setObjectName("forecast_temp"); temp.setAlignment(Qt.AlignCenter)

        col = QVBoxLayout()
        col.setContentsMargins(10, 10, 10, 10)
        col.setSpacing(4)
        col.addWidget(day)
        col.addWidget(emoji)
        col.addWidget(temp)
        card.setLayout(col)
        card._day   = day
        card._emoji = emoji
        card._temp  = temp
        return card

    # ── Search logic ─────────────────────────────────────────────────

    def do_search(self):
        city = self.search_input.text().strip()
        if not city:
            return
        self.status_label.setText(f"Fetching weather for {city.title()}…")
        self.status_label.show()
        self.search_btn.setEnabled(False)

        self.fetch_thread = FetchThread(city)
        self.fetch_thread.result_ready.connect(self.on_data)
        self.fetch_thread.error.connect(self.on_error)
        self.fetch_thread.start()

    def search_from_history(self, item: QListWidgetItem):
        city = item.text().strip()
        self.search_input.setText(city)
        self.do_search()

    # ── Data handlers ────────────────────────────────────────────────

    def on_data(self, data: dict):
        self.search_btn.setEnabled(True)
        self.status_label.hide()

        # Main card
        self.city_label.setText(f"{data['emoji']}  {data['city']}")
        self.temp_label.setText(f"{data['temp']}°C")
        self.cond_label.setText(data["condition"])
        self.detail_widgets["Feels Like"].setText(f"{data['feels_like']}°C")
        self.detail_widgets["Humidity"].setText(f"{data['humidity']}%")
        self.detail_widgets["Wind"].setText(f"{data['wind']} km/h")
        self.detail_widgets["Hi / Lo"].setText(f"{data['high']}° / {data['low']}°")

        # Forecast
        for i, fc in enumerate(data["forecast"]):
            w = self.forecast_widgets[i]
            w._day.setText(fc["day"])
            w._emoji.setText(fc["emoji"])
            w._temp.setText(f"{fc['high']}° / {fc['low']}°")
            w.show()

        self.weather_card.show()
        self.forecast_title.show()

        # History
        city = data["city"]
        if city not in self.search_history:
            self.search_history.insert(0, city)
            self.history_list.insertItem(0, city)
        if len(self.search_history) > 10:
            self.search_history.pop()
            self.history_list.takeItem(self.history_list.count() - 1)

    def on_error(self, msg: str):
        self.search_btn.setEnabled(True)
        self.status_label.setText(f"⚠️  {msg}")
        self.status_label.show()


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())