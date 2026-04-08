# def validate_signal(signal):
#     if not signal.get("type"):
#         print("❌ Validation failed: missing type")
#         return False

#     if not signal.get("symbol"):
#         print("❌ Validation failed: missing symbol")
#         return False

#     if signal.get("entry") is None:
#         print("❌ Validation failed: missing entry")
#         return False

#     if not signal.get("sl"):
#         print("❌ Validation failed: missing sl")
#         return False

#     if not signal.get("tp"):
#         print("❌ Validation failed: missing tp")
#         return False

#     print("✅ Signal validated")
#     return True






def validate_signal(signal):
    if not signal:
        print("❌ Validation failed: signal is None")
        return False

    if not signal.get("type"):
        print("❌ Validation failed: missing type")
        return False

    if not signal.get("symbol"):
        print("❌ Validation failed: missing symbol")
        return False

    if signal.get("entry") is None:
        print("❌ Validation failed: missing entry")
        return False

    if signal.get("sl") is None:
        print("❌ Validation failed: missing sl")
        return False

    if not signal.get("tp"):
        print("❌ Validation failed: missing tp")
        return False

    print("✅ Signal validated")
    return True