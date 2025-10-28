import solara

# 1. 匯入您所有的「頁面」檔案
import page_home
import page_map
import page_3dmap

# --- 2. 定義路由 (網站地圖) ---
# 這是您 App 的核心
# 它將 URL 路徑連結到您匯入的 Python 元件
routes = [
    # 路徑 "/" 會執行 page_home.py 裡的 Page 元件
    solara.Route(path="/", component=page_home.Page, label="專案首頁"),
    
    # 路徑 "/map" 會執行 page_map.py 裡的 Page 元件
    solara.Route(path="/map", component=page_map.Page, label="2D 互動地圖"),

    # 路徑 "/map-3d" 會執行 page_3dmap.py 裡的 Page 元件 (Lab 9)
    solara.Route(path="/map-3d", component=page_3dmap.Page, label="3D 地形圖 (Lab 9)"),
]

# --- 3. 定義主佈局 (Layout)，包含導覽 ---
@solara.component
def Layout(main_content):
    # 取得路由控制器，以便我們可以點擊按鈕來切換頁面
    router = solara.use_router()
    
    # 建立一個頂部的 App Bar
    with solara.AppBar(color="primary"):
        solara.Markdown("### 🌍 我的 Solara GIS App (Codespaces)")

    # 建立一個側邊欄
    with solara.Sidebar():
        solara.Markdown("## 導覽選單")
        
        # --- 手動建立導覽按鈕 ---
        # 迴圈遍歷我們上面定義的 routes 列表
        with solara.ButtonGroup(vertical=True, classes=["nav-buttons"]):
            for route in routes:
                solara.Button(
                    label=route.label,
                    # 關鍵：點擊時，使用 router.push() 來更改瀏覽器的 URL
                    on_click=lambda r=route: router.push(r.path),
                    text=True, # 讓按鈕看起來像連結
                    icon_name="mdi-chevron-right"
                )

    # 顯示目前 URL 所對應的主內容
    # (這將由 Solara Router 自動傳入)
    return main_content

# --- 4. 建立 App ---
# Solara 會自動尋找名為 Page 的元件作為進入點
@solara.component
def Page():
    # Solara 的 Router 會：
    # 1. 讀取 `routes` 列表
    # 2. 查看當前瀏覽器 URL
    # 3. 找到對應的 `component` (例如 page_map.Page)
    # 4. 執行該元件，並將結果傳遞給 `layout`
    return solara.Router(routes=routes, layout=Layout)