import time

def stress_test():
    print("--- Memulai Simulasi Beban Resource ---")
    data = []
    
    try:
        for i in range(1, 11):
            # 1. Alokasi Memori (Menambah sekitar 50MB setiap iterasi)
            print(f"Langkah {i}: Menambah beban memori...")
            data.append(' ' * (50 * 1024 * 1024)) 
            
            # 2. Komputasi CPU (Looping intensif selama 3 detik)
            print(f"Langkah {i}: Menjalankan komputasi CPU intensif...")
            end_time = time.time() + 3
            while time.time() < end_time:
                pass  # Ini akan membuat penggunaan CPU melonjak
                
            time.sleep(1) # Istirahat sejenak
            
    except MemoryError:
        print("\n[STOP] Error: Memori sudah penuh!")
    except Exception as e:
        print(f"\n[STOP] Terjadi error: {e}")

if __name__ == "__main__":
    stress_test()
    