#!/usr/bin/env python3
"""
Keyboard Tester Application
Aplikasi untuk testing keyboard dengan GUI modern
Mendukung Linux dan Windows
"""

import tkinter as tk
from tkinter import ttk
import platform

class KeyboardTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Tester")
        self.root.geometry("1100x500")
        self.root.configure(bg='#1e1e2e')
        
        # Set minimum window size
        self.root.minsize(900, 450)
        
        # Key states tracking
        self.pressed_keys = set()  # Keys ever pressed
        self.current_keys = set()  # Keys currently pressed
        
        # Color scheme (Catppuccin-inspired modern theme)
        self.colors = {
            'bg': '#1e1e2e',
            'surface': '#313244',
            'overlay': '#45475a',
            'text': '#ffffff',
            'never_pressed': '#4a4a5e',
            'pressed_before': '#5e9fff',
            'currently_pressed': '#4ade80',
            'border': '#6c7086'
        }
        
        # Keyboard layouts
        self.keyboard_layouts = {
            'Full Size (100%)': self.get_fullsize_layout(),
            'TKL (80%)': self.get_tkl_layout(),
            '60%': self.get_60_layout()
        }
        
        self.current_layout = 'Full Size (100%)'
        self.key_buttons = {}
        
        self.setup_ui()
        self.bind_keyboard_events()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Top section - Title and Info
        top_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        top_frame.pack(fill=tk.X, pady=(0, 15))
        
        title_label = tk.Label(
            top_frame,
            text="⌨️ KEYBOARD TESTER",
            font=('Segoe UI', 16, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            top_frame,
            text="Tekan tombol keyboard untuk menguji",
            font=('Segoe UI', 9),
            bg=self.colors['bg'],
            fg=self.colors['border']
        )
        subtitle_label.pack()
        
        # Control panel
        control_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Layout selector
        layout_frame = tk.Frame(control_frame, bg=self.colors['bg'])
        layout_frame.pack(side=tk.LEFT)
        
        tk.Label(
            layout_frame,
            text="Ukuran Keyboard:",
            font=('Segoe UI', 9),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(side=tk.LEFT, padx=(0, 8))
        
        self.layout_var = tk.StringVar(value=self.current_layout)
        layout_combo = ttk.Combobox(
            layout_frame,
            textvariable=self.layout_var,
            values=list(self.keyboard_layouts.keys()),
            state='readonly',
            width=15,
            font=('Segoe UI', 9)
        )
        layout_combo.pack(side=tk.LEFT)
        layout_combo.bind('<<ComboboxSelected>>', self.change_layout)
        
        # Reset button
        reset_btn = tk.Button(
            control_frame,
            text="🔄 Reset",
            command=self.reset_keyboard,
            font=('Segoe UI', 9, 'bold'),
            bg=self.colors['overlay'],
            fg=self.colors['text'],
            activebackground=self.colors['surface'],
            activeforeground=self.colors['text'],
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor='hand2',
            borderwidth=2
        )
        reset_btn.pack(side=tk.LEFT, padx=15)
        
        # Current key display
        self.current_key_label = tk.Label(
            control_frame,
            text="Tombol Terakhir: -",
            font=('Segoe UI', 9),
            bg=self.colors['surface'],
            fg=self.colors['text'],
            padx=15,
            pady=5,
            relief=tk.FLAT
        )
        self.current_key_label.pack(side=tk.LEFT)
        
        # Legend
        legend_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        legend_frame.pack(fill=tk.X, pady=(0, 10))
        
        legends = [
            ("Belum Ditekan", self.colors['never_pressed']),
            ("Pernah Ditekan", self.colors['pressed_before']),
            ("Sedang Ditekan", self.colors['currently_pressed'])
        ]
        
        for text, color in legends:
            legend_item = tk.Frame(legend_frame, bg=self.colors['bg'])
            legend_item.pack(side=tk.LEFT, padx=15)
            
            color_box = tk.Label(
                legend_item,
                bg=color,
                width=3,
                relief=tk.FLAT,
                borderwidth=1
            )
            color_box.pack(side=tk.LEFT, padx=(0, 5))
            
            tk.Label(
                legend_item,
                text=text,
                font=('Segoe UI', 9),
                bg=self.colors['bg'],
                fg=self.colors['text']
            ).pack(side=tk.LEFT)
        
        # Keyboard container with scrollbar
        keyboard_container = tk.Frame(main_frame, bg=self.colors['bg'])
        keyboard_container.pack(fill=tk.BOTH, expand=True)
        
        # Canvas for scrolling
        self.canvas = tk.Canvas(
            keyboard_container,
            bg=self.colors['bg'],
            highlightthickness=0
        )
        scrollbar = tk.Scrollbar(
            keyboard_container,
            orient=tk.VERTICAL,
            command=self.canvas.yview
        )
        
        self.keyboard_frame = tk.Frame(self.canvas, bg=self.colors['bg'])
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.canvas_frame = self.canvas.create_window(
            (0, 0),
            window=self.keyboard_frame,
            anchor=tk.NW
        )
        
        self.keyboard_frame.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Draw keyboard
        self.draw_keyboard()
        
        # Statistics
        self.stats_label = tk.Label(
            main_frame,
            text="Total tombol ditekan: 0",
            font=('Segoe UI', 9),
            bg=self.colors['bg'],
            fg=self.colors['border']
        )
        self.stats_label.pack(pady=(10, 0))
        
    def on_frame_configure(self, event=None):
        """Reset scroll region when frame size changes"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def on_canvas_configure(self, event):
        """Center the keyboard frame when canvas is resized"""
        canvas_width = event.width
        frame_width = self.keyboard_frame.winfo_reqwidth()
        
        if frame_width < canvas_width:
            x_position = (canvas_width - frame_width) // 2
        else:
            x_position = 0
            
        self.canvas.coords(self.canvas_frame, x_position, 0)
        
    def draw_keyboard(self):
        """Draw the keyboard layout"""
        # Clear existing buttons
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()
        self.key_buttons.clear()
        
        layout = self.keyboard_layouts[self.current_layout]
        
        for row_idx, row in enumerate(layout):
            row_frame = tk.Frame(self.keyboard_frame, bg=self.colors['bg'])
            row_frame.pack(pady=0)
            
            for key_info in row:
                key_name = key_info['key']
                width = key_info.get('width', 1)
                is_spacer = key_info.get('spacer', False)
                
                if is_spacer or key_name == '':
                    # Create invisible spacer
                    spacer = tk.Label(
                        row_frame,
                        text='',
                        bg=self.colors['bg'],
                        width=int(width * 3),
                        height=1
                    )
                    spacer.pack(side=tk.LEFT)
                    continue
                
                # Create key button
                # Dynamic font size based on key name length
                if len(key_name) > 6:
                    font_size = 6
                elif len(key_name) > 4:
                    font_size = 7
                else:
                    font_size = 8
                
                key_btn = tk.Label(
                    row_frame,
                    text=key_name,
                    font=('Arial', font_size, 'bold'),
                    bg=self.colors['never_pressed'],
                    fg=self.colors['text'],
                    relief=tk.RAISED,
                    borderwidth=1,
                    width=int(width * 3),
                    height=1,
                    cursor='arrow',
                    padx=1,
                    pady=1
                )
                key_btn.pack(side=tk.LEFT, padx=1, pady=0)
                
                # Store button reference with normalized key name
                normalized_key = self.normalize_key(key_name)
                self.key_buttons[normalized_key] = key_btn
                
    def normalize_key(self, key):
        """Normalize key name for consistent matching"""
        # Map display names to event.keysym values
        key_map = {
            # Special keys
            'Esc': 'Escape',
            'Tab': 'Tab',
            'CapsLock': 'Caps_Lock',
            'Caps': 'Caps_Lock',
            'Enter': 'Return',
            'Bksp': 'BackSpace',
            'Space': 'space',
            
            # Modifiers
            'LShift': 'Shift_L',
            'RShift': 'Shift_R',
            'LCtrl': 'Control_L',
            'RCtrl': 'Control_R',
            'LAlt': 'Alt_L',
            'RAlt': 'Alt_R',
            'LWin': 'Super_L',
            'RWin': 'Super_R',
            'Menu': 'Menu',
            
            # Navigation
            'Insert': 'Insert',
            'Delete': 'Delete',
            'Home': 'Home',
            'End': 'End',
            'PgUp': 'Prior',
            'PgDn': 'Next',
            
            # Arrow keys
            '↑': 'Up',
            '↓': 'Down',
            '←': 'Left',
            '→': 'Right',
            
            # System keys
            'PrtSc': 'Print',
            'ScrLk': 'Scroll_Lock',
            'Pause': 'Pause',
            'Break': 'Break',
            
            # Lock keys
            'NumLk': 'Num_Lock',
            
            # Numpad - These are critical!
            'KP0': 'KP_0',
            'KP1': 'KP_1',
            'KP2': 'KP_2',
            'KP3': 'KP_3',
            'KP4': 'KP_4',
            'KP5': 'KP_5',
            'KP6': 'KP_6',
            'KP7': 'KP_7',
            'KP8': 'KP_8',
            'KP9': 'KP_9',
            'KP/': 'KP_Divide',
            'KP*': 'KP_Multiply',
            'KP-': 'KP_Subtract',
            'KP+': 'KP_Add',
            'KP.': 'KP_Decimal',
            'KPEnter': 'KP_Enter',
        }
        
        return key_map.get(key, key)
                
    def bind_keyboard_events(self):
        """Bind keyboard events"""
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.bind('<KeyRelease>', self.on_key_release)
        
    def on_key_press(self, event):
        """Handle key press event"""
        key = event.keysym
        
        # Update current key display
        display_name = self.get_display_name(key)
        self.current_key_label.config(text=f"Tombol Terakhir: {display_name}")
        
        # Add to pressed keys sets
        self.pressed_keys.add(key)
        self.current_keys.add(key)
        
        # Update key visual
        self.update_key_visual(key)
        
        # Update statistics
        self.update_statistics()
        
    def on_key_release(self, event):
        """Handle key release event"""
        key = event.keysym
        
        # Remove from current keys
        if key in self.current_keys:
            self.current_keys.remove(key)
            
        # Update key visual
        self.update_key_visual(key)
        
    def update_key_visual(self, key):
        """Update the visual state of a key"""
        # Try to find the button for this key
        if key in self.key_buttons:
            btn = self.key_buttons[key]
            
            if key in self.current_keys:
                # Currently pressed
                btn.config(bg=self.colors['currently_pressed'], relief=tk.SUNKEN)
            elif key in self.pressed_keys:
                # Previously pressed
                btn.config(bg=self.colors['pressed_before'], relief=tk.RAISED)
            else:
                # Never pressed
                btn.config(bg=self.colors['never_pressed'], relief=tk.RAISED)
        else:
            # Try alternative mappings
            for btn_key, btn in self.key_buttons.items():
                if self.keys_match(key, btn_key):
                    if key in self.current_keys:
                        btn.config(bg=self.colors['currently_pressed'], relief=tk.SUNKEN)
                    elif key in self.pressed_keys:
                        btn.config(bg=self.colors['pressed_before'], relief=tk.RAISED)
                    break
                    
    def keys_match(self, key1, key2):
        """Check if two keys represent the same physical key"""
        # Handle modifier keys
        shift_keys = {'Shift_L', 'Shift_R'}
        ctrl_keys = {'Control_L', 'Control_R'}
        alt_keys = {'Alt_L', 'Alt_R'}
        super_keys = {'Super_L', 'Super_R'}
        
        if key1 in shift_keys and key2 in shift_keys:
            return True
        if key1 in ctrl_keys and key2 in ctrl_keys:
            return True
        if key1 in alt_keys and key2 in alt_keys:
            return True
        if key1 in super_keys and key2 in super_keys:
            return True
            
        # Handle letter keys (case insensitive)
        if len(key1) == 1 and len(key2) == 1:
            if key1.isalpha() and key2.isalpha():
                return key1.upper() == key2.upper()
        
        # Exact match for everything else
        return key1 == key2
        
    def get_display_name(self, key):
        """Get friendly display name for a key"""
        display_map = {
            'Escape': 'Esc',
            'Caps_Lock': 'Caps Lock',
            'Shift_L': 'Left Shift',
            'Shift_R': 'Right Shift',
            'Control_L': 'Left Ctrl',
            'Control_R': 'Right Ctrl',
            'Alt_L': 'Left Alt',
            'Alt_R': 'Right Alt',
            'Super_L': 'Left Win',
            'Super_R': 'Right Win',
            'Return': 'Enter',
            'BackSpace': 'Backspace',
            'Prior': 'Page Up',
            'Next': 'Page Down',
            'Scroll_Lock': 'Scroll Lock',
            'Num_Lock': 'Num Lock',
            'Print': 'Print Screen',
            'space': 'Space',
            'Up': '↑',
            'Down': '↓',
            'Left': '←',
            'Right': '→',
        }
        
        # Numpad keys
        if key.startswith('KP_'):
            num = key.replace('KP_', '')
            return f"Numpad {num}"
        
        return display_map.get(key, key)
        
    def update_statistics(self):
        """Update statistics display"""
        total_pressed = len(self.pressed_keys)
        self.stats_label.config(text=f"Total tombol ditekan: {total_pressed}")
        
    def reset_keyboard(self):
        """Reset all key states"""
        self.pressed_keys.clear()
        self.current_keys.clear()
        self.current_key_label.config(text="Tombol Terakhir: -")
        
        # Reset all button colors
        for btn in self.key_buttons.values():
            btn.config(bg=self.colors['never_pressed'], relief=tk.RAISED)
            
        self.update_statistics()
        
    def change_layout(self, event=None):
        """Change keyboard layout"""
        self.current_layout = self.layout_var.get()
        self.draw_keyboard()
        
        # Reapply key states to new layout
        for key in self.pressed_keys:
            self.update_key_visual(key)
            
    def get_fullsize_layout(self):
        """Get full-size keyboard layout (100%) - Based on standard ANSI layout"""
        return [
            # Function row
            [
                {'key': 'Esc'},
                {'key': '', 'width': 0.75, 'spacer': True},
                {'key': 'F1'}, {'key': 'F2'}, {'key': 'F3'}, {'key': 'F4'},
                {'key': '', 'width': 0.5, 'spacer': True},
                {'key': 'F5'}, {'key': 'F6'}, {'key': 'F7'}, {'key': 'F8'},
                {'key': '', 'width': 0.5, 'spacer': True},
                {'key': 'F9'}, {'key': 'F10'}, {'key': 'F11'}, {'key': 'F12'},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'PrtSc'}, {'key': 'ScrLk'}, {'key': 'Pause'},
            ],
            # Spacing row
            [{'key': '', 'width': 1, 'spacer': True}],
            # Number row
            [
                {'key': '`'}, {'key': '1'}, {'key': '2'}, {'key': '3'}, {'key': '4'},
                {'key': '5'}, {'key': '6'}, {'key': '7'}, {'key': '8'}, {'key': '9'},
                {'key': '0'}, {'key': '-'}, {'key': '='}, {'key': 'Bksp', 'width': 2},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'Insert'}, {'key': 'Home'}, {'key': 'PgUp'},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'NumLk'}, {'key': 'KP/'}, {'key': 'KP*'}, {'key': 'KP-'},
            ],
            # QWERTY row
            [
                {'key': 'Tab', 'width': 1.5}, 
                {'key': 'Q'}, {'key': 'W'}, {'key': 'E'}, {'key': 'R'}, {'key': 'T'}, 
                {'key': 'Y'}, {'key': 'U'}, {'key': 'I'}, {'key': 'O'}, {'key': 'P'}, 
                {'key': '['}, {'key': ']'}, {'key': '\\', 'width': 1.5},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'Delete'}, {'key': 'End'}, {'key': 'PgDn'},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'KP7'}, {'key': 'KP8'}, {'key': 'KP9'}, {'key': 'KP+', 'width': 1},
            ],
            # ASDF row
            [
                {'key': 'CapsLock', 'width': 1.75}, 
                {'key': 'A'}, {'key': 'S'}, {'key': 'D'}, {'key': 'F'}, {'key': 'G'}, 
                {'key': 'H'}, {'key': 'J'}, {'key': 'K'}, {'key': 'L'}, 
                {'key': ';'}, {'key': "'"}, {'key': 'Enter', 'width': 2.25},
                {'key': '', 'width': 3.5, 'spacer': True},
                {'key': 'KP4'}, {'key': 'KP5'}, {'key': 'KP6'}, {'key': '', 'width': 1, 'spacer': True},
            ],
            # ZXCV row
            [
                {'key': 'LShift', 'width': 2.25}, 
                {'key': 'Z'}, {'key': 'X'}, {'key': 'C'}, {'key': 'V'}, {'key': 'B'}, 
                {'key': 'N'}, {'key': 'M'}, {'key': ','}, {'key': '.'}, {'key': '/'}, 
                {'key': 'RShift', 'width': 2.75},
                {'key': '', 'width': 1.25, 'spacer': True},
                {'key': '↑'},
                {'key': '', 'width': 1.25, 'spacer': True},
                {'key': 'KP1'}, {'key': 'KP2'}, {'key': 'KP3'}, {'key': 'KPEnter', 'width': 1},
            ],
            # Bottom row
            [
                {'key': 'LCtrl', 'width': 1.25}, {'key': 'LWin', 'width': 1.25}, {'key': 'LAlt', 'width': 1.25}, 
                {'key': 'Space', 'width': 6.25}, 
                {'key': 'RAlt', 'width': 1.25}, {'key': 'RWin', 'width': 1.25}, 
                {'key': 'Menu', 'width': 1.25}, {'key': 'RCtrl', 'width': 1.25},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': '←'}, {'key': '↓'}, {'key': '→'},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'KP0', 'width': 2}, {'key': 'KP.'}, {'key': '', 'width': 1, 'spacer': True},
            ],
        ]
        
    def get_tkl_layout(self):
        """Get TKL keyboard layout (80%) - Tenkeyless"""
        return [
            # Function row
            [
                {'key': 'Esc'},
                {'key': '', 'width': 0.75, 'spacer': True},
                {'key': 'F1'}, {'key': 'F2'}, {'key': 'F3'}, {'key': 'F4'},
                {'key': '', 'width': 0.5, 'spacer': True},
                {'key': 'F5'}, {'key': 'F6'}, {'key': 'F7'}, {'key': 'F8'},
                {'key': '', 'width': 0.5, 'spacer': True},
                {'key': 'F9'}, {'key': 'F10'}, {'key': 'F11'}, {'key': 'F12'},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'PrtSc'}, {'key': 'ScrLk'}, {'key': 'Pause'},
            ],
            # Spacing row
            [{'key': '', 'width': 1, 'spacer': True}],
            # Number row
            [
                {'key': '`'}, {'key': '1'}, {'key': '2'}, {'key': '3'}, {'key': '4'},
                {'key': '5'}, {'key': '6'}, {'key': '7'}, {'key': '8'}, {'key': '9'},
                {'key': '0'}, {'key': '-'}, {'key': '='}, {'key': 'Bksp', 'width': 2},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'Insert'}, {'key': 'Home'}, {'key': 'PgUp'},
            ],
            # QWERTY row
            [
                {'key': 'Tab', 'width': 1.5}, 
                {'key': 'Q'}, {'key': 'W'}, {'key': 'E'}, {'key': 'R'}, {'key': 'T'}, 
                {'key': 'Y'}, {'key': 'U'}, {'key': 'I'}, {'key': 'O'}, {'key': 'P'}, 
                {'key': '['}, {'key': ']'}, {'key': '\\', 'width': 1.5},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': 'Delete'}, {'key': 'End'}, {'key': 'PgDn'},
            ],
            # ASDF row
            [
                {'key': 'CapsLock', 'width': 1.75}, 
                {'key': 'A'}, {'key': 'S'}, {'key': 'D'}, {'key': 'F'}, {'key': 'G'}, 
                {'key': 'H'}, {'key': 'J'}, {'key': 'K'}, {'key': 'L'}, 
                {'key': ';'}, {'key': "'"}, {'key': 'Enter', 'width': 2.25},
            ],
            # ZXCV row
            [
                {'key': 'LShift', 'width': 2.25}, 
                {'key': 'Z'}, {'key': 'X'}, {'key': 'C'}, {'key': 'V'}, {'key': 'B'}, 
                {'key': 'N'}, {'key': 'M'}, {'key': ','}, {'key': '.'}, {'key': '/'}, 
                {'key': 'RShift', 'width': 2.75},
                {'key': '', 'width': 1.25, 'spacer': True},
                {'key': '↑'},
            ],
            # Bottom row
            [
                {'key': 'LCtrl', 'width': 1.25}, {'key': 'LWin', 'width': 1.25}, {'key': 'LAlt', 'width': 1.25}, 
                {'key': 'Space', 'width': 6.25}, 
                {'key': 'RAlt', 'width': 1.25}, {'key': 'RWin', 'width': 1.25}, 
                {'key': 'Menu', 'width': 1.25}, {'key': 'RCtrl', 'width': 1.25},
                {'key': '', 'width': 0.25, 'spacer': True},
                {'key': '←'}, {'key': '↓'}, {'key': '→'},
            ],
        ]
        
    def get_60_layout(self):
        """Get 60% keyboard layout"""
        return [
            # Number row
            [
                {'key': 'Esc'}, 
                {'key': '1'}, {'key': '2'}, {'key': '3'}, {'key': '4'},
                {'key': '5'}, {'key': '6'}, {'key': '7'}, {'key': '8'}, {'key': '9'},
                {'key': '0'}, {'key': '-'}, {'key': '='}, {'key': 'Bksp', 'width': 2},
            ],
            # QWERTY row
            [
                {'key': 'Tab', 'width': 1.5}, 
                {'key': 'Q'}, {'key': 'W'}, {'key': 'E'}, {'key': 'R'}, {'key': 'T'}, 
                {'key': 'Y'}, {'key': 'U'}, {'key': 'I'}, {'key': 'O'}, {'key': 'P'}, 
                {'key': '['}, {'key': ']'}, {'key': '\\', 'width': 1.5},
            ],
            # ASDF row
            [
                {'key': 'CapsLock', 'width': 1.75}, 
                {'key': 'A'}, {'key': 'S'}, {'key': 'D'}, {'key': 'F'}, {'key': 'G'}, 
                {'key': 'H'}, {'key': 'J'}, {'key': 'K'}, {'key': 'L'}, 
                {'key': ';'}, {'key': "'"}, {'key': 'Enter', 'width': 2.25},
            ],
            # ZXCV row
            [
                {'key': 'LShift', 'width': 2.25}, 
                {'key': 'Z'}, {'key': 'X'}, {'key': 'C'}, {'key': 'V'}, {'key': 'B'}, 
                {'key': 'N'}, {'key': 'M'}, {'key': ','}, {'key': '.'}, {'key': '/'}, 
                {'key': 'RShift', 'width': 2.75},
            ],
            # Bottom row
            [
                {'key': 'LCtrl', 'width': 1.25}, {'key': 'LWin', 'width': 1.25}, {'key': 'LAlt', 'width': 1.25}, 
                {'key': 'Space', 'width': 6.25}, 
                {'key': 'RAlt', 'width': 1.25}, {'key': 'RWin', 'width': 1.25}, 
                {'key': 'Menu', 'width': 1.25}, {'key': 'RCtrl', 'width': 1.25},
            ],
        ]


def main():
    """Main function to run the application"""
    root = tk.Tk()
    
    # Configure ttk style for modern look
    style = ttk.Style()
    style.theme_use('clam')
    
    # Configure combobox style
    style.configure('TCombobox',
                   fieldbackground='#313244',
                   background='#313244',
                   foreground='#cdd6f4',
                   arrowcolor='#cdd6f4',
                   borderwidth=0)
    
    app = KeyboardTester(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
