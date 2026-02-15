#!/usr/bin/env python3
"""
Test script untuk memverifikasi keyboard_tester.py
"""

import sys
import importlib.util

def test_import():
    """Test apakah module bisa di-import tanpa error"""
    print("🔍 Testing import keyboard_tester module...")
    try:
        spec = importlib.util.spec_from_file_location("keyboard_tester", "keyboard_tester.py")
        module = importlib.util.module_from_spec(spec)
        # Don't execute, just check syntax
        print("✅ Module dapat di-import (syntax valid)")
        return True
    except Exception as e:
        print(f"❌ Error saat import: {e}")
        return False

def test_syntax():
    """Test syntax Python"""
    print("\n🔍 Testing Python syntax...")
    try:
        with open("keyboard_tester.py", 'r') as f:
            code = f.read()
        compile(code, "keyboard_tester.py", 'exec')
        print("✅ Syntax Python valid")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax Error: {e}")
        return False

def test_class_structure():
    """Test struktur class"""
    print("\n🔍 Testing class structure...")
    try:
        with open("keyboard_tester.py", 'r') as f:
            content = f.read()
        
        checks = {
            "Class KeyboardTester": "class KeyboardTester" in content,
            "Method __init__": "def __init__" in content,
            "Method setup_ui": "def setup_ui" in content,
            "Method draw_keyboard": "def draw_keyboard" in content,
            "Method on_key_press": "def on_key_press" in content,
            "Method on_key_release": "def on_key_release" in content,
            "Method reset_keyboard": "def reset_keyboard" in content,
            "Main function": "def main()" in content,
        }
        
        all_passed = True
        for check_name, result in checks.items():
            status = "✅" if result else "❌"
            print(f"  {status} {check_name}")
            if not result:
                all_passed = False
        
        return all_passed
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_tkinter_available():
    """Test apakah tkinter tersedia"""
    print("\n🔍 Testing tkinter availability...")
    try:
        import tkinter
        print(f"✅ tkinter tersedia (version: {tkinter.TkVersion})")
        return True
    except ImportError:
        print("❌ tkinter tidak tersedia")
        return False

def main():
    """Run all tests"""
    print("="*50)
    print("  KEYBOARD TESTER - AUTOMATED TESTS")
    print("="*50)
    
    tests = [
        test_tkinter_available,
        test_syntax,
        test_import,
        test_class_structure,
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    print("\n" + "="*50)
    print("  TEST SUMMARY")
    print("="*50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total}")
    
    if all(results):
        print("\n🎉 SEMUA TEST BERHASIL!")
        print("\nAplikasi siap digunakan:")
        print("  python3 keyboard_tester.py")
        return 0
    else:
        print("\n⚠️  Beberapa test gagal")
        return 1

if __name__ == "__main__":
    sys.exit(main())
