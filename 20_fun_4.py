#without parameter without return 
import platform

def info():
    print("=== System Information ===\n")
    print("System:", platform.system())
    print("Node Name:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

info()
