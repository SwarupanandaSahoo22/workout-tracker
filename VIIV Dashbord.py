# VIIV Dashbord

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QVBoxLayout, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QProgressBar, QScrollArea
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QColor

class DashBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VIIV Dashboard")
        self.setMinimumSize(1100, 700)
        self.setStyleSheet("background-color: #0f0f0f;")
        self.initUI()

    def initUI(self):
        # Root layout — sidebar on left, main content on right
        root = QHBoxLayout()
        root.setContentsMargins(0, 0, 0, 0)
        root.addSpacing(0)

        # Sidebar
        sidebar = self.build_sidebar()

        # Right side - Topbar + Content stacked vertically
        right_side = QVBoxLayout()
        right_side.setContentsMargins(0, 0, 0, 0)
        right_side.addSpacing(0)

        topbar = self.build_topbar()

        # Main Content
        self.content = QWidget()
        self.content.setStyleSheet("background-color: #0f0f0f;")

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(25, 25, 25, 25)
        content_layout.setSpacing(20)

        # Stat cards
        stat_cards = self.build_stat_cards()
        content_layout.addLayout(stat_cards)

        # Order table
        order_table = self.build_order_table()
        content_layout.addWidget(order_table)

        # Inventory
        inventory = self.build_inventory()
        content_layout.addWidget(inventory)

        content_layout.addStretch()
        self.content.setLayout(content_layout)

        # Warp in scroll area
        scroll = QScrollArea()
        scroll.setWidget(self.content)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #0f0f0f;
            }
            QScrollBar:vertical {
                border-radius: 4px;
                background-color: #0f0f0f;
                width: 8px;
            }
            QScrollBar::handle:vertical {
                border-radius: 4px;
                background-color: #333333;
                min-height: 20px;
            }
            QScrollBar::handle:verical:hover{
                background-color: #555555;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical{
                height: 0px;
            }
    """)
        
        right_side.addWidget(topbar)
        right_side.addWidget(scroll, 1)

        right_widget = QWidget()
        right_widget.setLayout(right_side)
        
        root.addWidget(sidebar)
        root.addWidget(right_widget, 1)
        self.setLayout(root)

    def build_sidebar(self):
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #141414;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Brand
        brand = QLabel("VIIV")
        brand.setStyleSheet("""
        color: #6ddb8b;
        font-size: 22px;
        font-weight: bold;
        font-family: Calibri;
        padding: 30px 20px;
    """)
        layout.addWidget(brand)

        # Navigation button
        nav_btn = ["Dashboard", "Orders", "Inventory", "Customers"]

        for item in nav_btn:
            btn = QPushButton(item)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
            QPushButton{
            color: #888888;
            font-size: 15px;
            font-family: Calibri;
            font-weight: bold;
            text-align: left;
            border: 15px 25px;
            padding: none;
            background-color: transparent;
            }
                              
            QPushButton: hover{
            color: #ffffff;
            background-color: #1e1e1e;
            }
        """)
            
            layout.addWidget(btn)
        
        layout.addStretch()
        sidebar.setLayout(layout)
        return sidebar
    
    def build_topbar(self):
        topbar = QWidget()
        topbar.setMinimumHeight(70)
        topbar.setStyleSheet("""
        background-color: #141414;
        border-bottom: 1px solid #222222;
    """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(25, 0, 25, 0)

        # Page title
        title = QLabel("Dashboard")
        title.setStyleSheet("""
        color: #ffffff;
        font-size: 20px;
        font-weight: bold;
        font-family: Calibri;
    """)
        
        # Current Date
        today = QDate.currentDate().toString("dddd, MMMM d yyyy")
        date_label = QLabel(today)
        date_label.setStyleSheet("""
        color: #888888;
        font-family: Calibri;
        font-size: 13px;
    """)
        
        # Status
        status = QLabel("Live 🟢")
        status.setStyleSheet("""
        color: #6ddb8b;
        font-family: Calibri;
        font-size: 13px;
        font-weight: bold;
    """)
        
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(date_label)
        layout.addSpacing(20)
        layout.addWidget(status)

        topbar.setLayout(layout)
        return topbar
    
    def build_stat_cards(self):
        row = QHBoxLayout()
        row.setSpacing(15)

        cards =[
            ("Revenue", "$12,480",  "+8% today",  "#6ddb8b"),
            ("Orders",    "284",      "+12 today",  "#6ddb8b"),
            ("Customers", "1,042",    "+5 today",   "#6ddb8b"),
            ("Avg Order", "$43.90",   "+2% today",  "#6ddb8b"),
        ]

        for title, value, subtitle, color in cards:
            cards = self.build_single_cards(title, value, subtitle, color)
            row.addWidget(cards)

        return row
    
    def build_single_cards(self, title, value, subtitle, color):
        cards = QWidget()
        cards.setStyleSheet("""
            QWideget{
                background-color: #1a1a1a;
                border-radius: 12px;       
            }
        """)

        cards.setFixedHeight(120)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(5)

        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            color: #888888;
            font-family: Calibri;
            font-size: 13px;
            font-weight: bold;
            background-color: transparent;
            letter-spacing: 5px;              
        """)

        # Main value
        value_label = QLabel(value)
        value_label.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 28px;
            font-weight: bold;
            background-color: transparent;
    """)
        
        # Sub title
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet(f"""
            color: {color};
            font-size: 12px;
            font-family: Calibri;
            background-color: transparent;
    """)
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(subtitle_label)
        cards.setLayout(layout)

        return cards
    
    def build_order_table(self):
        container = QWidget()
        container.setStyleSheet("""
            background-color: #1a1a1a;
            border-radius: 12px;
    """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Section Title
        section_title = QLabel("Recent Orders")
        section_title.setStyleSheet("""
            color: #ffffff;
            font-size: 16px;
            font-weight: bold;
            font-family: Calibri;
            background-color: transparent;
    """)
        
        # Table
        table = QTableWidget()
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setRowCount(6)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Order ID", "Item", "Quantity", "Total", "Status"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setFocusPolicy(Qt.NoFocus)

        table.setStyleSheet("""
        QTableWidget {
            background-color: #1a1a1a;
            font-family: Calibri;
            font-size: 14px;
            border: none;
            color: #cccccc;
            gridline-color: #222222;
        }
        QTableWidegt::item {
            padding: 8px;
            border: none;
        }
        QTableWidegt::item:selected {
            background-color: #2a2a2a;
            color: #ffffff;
        }
        QHeaderView::section {
            background-color: #111111;
            font-family: Calibri;
            font-size: 13px;
            font-weight: bold;
            border: none;
            color: #888888;
            padding: 8px;
            letter-spacing: 1px;
        }
    """)
        
        # Dummy data
        orders = [
            ("#1042", "Green Surge",  "2", "$18.00", "Done"),
            ("#1041", "Berry Blast",  "1", "$9.50",  "Preparing"),
            ("#1040", "Mango Glow",   "3", "$25.50", "Done"),
            ("#1039", "Citrus Zing",  "2", "$17.00", "Cancelled"),
            ("#1038", "Green Surge",  "1", "$9.00",  "Done"),
            ("#1037", "Berry Blast",  "4", "$38.00", "Preparing"),
        ]

        status_color = {
            "Done": "#6ddb8b",
            "Preparing": "#ff9f1c",
            "Cancelled": "#ff4444",
        }

        for row, (oid, item, qty, total, status) in enumerate(orders):
            table.setItem(row, 0, QTableWidgetItem(oid))
            table.setItem(row, 1, QTableWidgetItem(item))
            table.setItem(row, 2, QTableWidgetItem(qty))
            table.setItem(row, 3, QTableWidgetItem(total))

            status_item = QTableWidgetItem(status)
            status_item.setForeground(QColor(status_color[status]))
            table.setItem(row, 4, status_item)

        layout.addWidget(section_title)
        layout.addWidget(table)
        container.setLayout(layout)
        return container
    
    def build_inventory(self):
        container = QWidget()
        container.setStyleSheet("background-color: #1a1a1a;  border-radius: 12px;")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Section Title
        section_title = QLabel("Inventory levels")
        section_title.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-weight: bold;
            font-size: 16px;
            background-color: transparent;
    """)
        layout.addWidget(section_title)

        # Stock data — (name, percentage)
        items = [
            ("Green Surge",  75),
            ("Berry Blast",  38),
            ("Mango Glow",   89),
            ("Citrus Zing",  22),
            ("Passion Fuel", 60),
    ]
        
        for name, percent in items:
            row = QHBoxLayout()
            row.setSpacing(15)

            # Item name
            name_label = QLabel(name)
            name_label.setStyleSheet(
                "color: #cccccc; font-family: Calibri; font-size: 13px; background-color: transparent;"
            )
            
            # Progress bar
            bar = QProgressBar()
            bar.setValue(percent)
            bar.setTextVisible(False)
            bar.setFixedHeight(10)

            # Color based on stock level

            if percent <= 30:
                bar_color = "#ff4444"
            elif percent <= 50:
                bar_color = "#ff9f1c"
            else:
                bar_color = "#6ddb8b"

            bar.setStyleSheet(
                "QProgressBar { background-color: #2a2a2a; border-radius: 5px; border: none; }"
                f"QProgressBar::chunk {{ background-color: {bar_color}; border-radius: 5px; }}"
            )
            
            # Percentage
            percent_label = QLabel(f"{percent}%")
            percent_label.setFixedWidth(40)
            percent_label.setStyleSheet(
                f"color: {bar_color}; font-size: 13px; font-family: Calibri; font-weight: bold; background-color: transparent;"
            )
            
            # Waring
            warning = QLabel("⚠ Low" if percent <= 30 else "")
            warning.setFixedWidth(50)
            warning.setStyleSheet(
                "color: #ff4444; font-family: Calibri; font-size: 12px; background-color: transparent;"
            )
            
            row.addWidget(name_label)
            row.addWidget(bar, 1)
            row.addWidget(percent_label)
            row.addWidget(warning)

            layout.addLayout(row)

        container.setLayout(layout)
        return container

         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashBoard()
    window.show()
    sys.exit(app.exec_())