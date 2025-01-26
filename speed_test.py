#!/usr/bin/env python3
import speedtest
from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def test_speed():
    console.print("[bold blue]بدء اختبار سرعة الشبكة...[/bold blue]")
    
    try:
        st = speedtest.Speedtest()
        
        with Progress() as progress:
            # اختيار أفضل خادم
            task1 = progress.add_task("[cyan]جاري اختيار أفضل خادم...", total=1)
            st.get_best_server()
            progress.update(task1, completed=1)
            
            # قياس سرعة التحميل
            task2 = progress.add_task("[green]قياس سرعة التحميل...", total=1)
            download_speed = st.download() / 1_000_000  # تحويل إلى ميجابت/ثانية
            progress.update(task2, completed=1)
            
            # قياس سرعة الرفع
            task3 = progress.add_task("[yellow]قياس سرعة الرفع...", total=1)
            upload_speed = st.upload() / 1_000_000  # تحويل إلى ميجابت/ثانية
            progress.update(task3, completed=1)
            
            # قياس زمن الاستجابة
            task4 = progress.add_task("[magenta]قياس زمن الاستجابة...", total=1)
            ping = st.results.ping
            progress.update(task4, completed=1)
        
        # عرض النتائج
        console.print("\n[bold green]== نتائج اختبار السرعة ==[/bold green]")
        console.print(f"[cyan]سرعة التحميل:[/cyan] {download_speed:.2f} Mbps")
        console.print(f"[yellow]سرعة الرفع:[/yellow] {upload_speed:.2f} Mbps")
        console.print(f"[magenta]زمن الاستجابة:[/magenta] {ping:.2f} ms")
        
    except Exception as e:
        console.print(f"[bold red]حدث خطأ:[/bold red] {str(e)}")

if __name__ == "__main__":
    test_speed()
