from io_csv import load_csv
from clean import basic_clean
from segment import simple_stats
from baseline import save, load
from compare import deltas, color_flag
from report import text_report, pdf_report

VEHICLE_ID = "demo_vehicle"

if __name__ == "__main__":
    # 1) build baseline from healthy.csv
    df_h = load_csv("data/healthy.csv")
    df_h = basic_clean(df_h)
    base_stats = simple_stats(df_h)
    save(VEHICLE_ID, base_stats)

    # 2) compare newscan to baseline
    df_n = load_csv("data/newscan.csv")
    df_n = basic_clean(df_n)
    new_stats = simple_stats(df_n)

    base = load(VEHICLE_ID)
    d = deltas(new_stats, base)

    # console output
    print(text_report(VEHICLE_ID, d))
    print("\nFlags:")
    flags = {}
    for k, delta in d.items():
        f = color_flag(delta, k)  # pass pid
        flags[k] = f
        print(k, f)

    # 3) -------- PDF output --------
    meta = {"Baseline file": "data/healthy.csv", "New scan": "data/newscan.csv"}
    pdf_report("report.pdf", VEHICLE_ID, d, flags, meta)
    print("\nSaved PDF: report.pdf")
