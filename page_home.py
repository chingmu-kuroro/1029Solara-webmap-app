# 這是一個簡單的靜態頁面，作為 App 的入口。
import solara

@solara.component
def Page():
    # 設定瀏覽器標籤頁的標題
    solara.Title("首頁 | Solara GIS App")
    
    solara.Markdown(
        """
        # 歡迎來到 Solara GIS 儀表板
        
        這是一個使用 Solara、GitHub Codespaces 和 Hugging Face Spaces 建立的互動式地圖應用程式。
        
        請使用左側的導覽選單來探索：
        
        * **2D 互動地圖**: 包含向量 (國家) 和網格 (DEM) 圖層。
        * **3D 地形圖**: 展示如何將 GPX 向量路線「披覆」在 3D 地形上。
        """
    )