# 3D 地圖頁 - Lab 8 & 9

import solara
import leafmap.leafmap as leafmap # 關鍵：使用 ipyleaflet 後端
import os

# --- 1. 準備 DEM 資料 ---
# 這裡我們使用 leafmap 內建的範例 DEM
terrain_url = "https://github.com/opengeos/leafmap/raw/master/examples/data/terrain.tif"

# --- 2. 建立 3D 地圖物件 ---
# 關鍵：設定 pitch (傾斜) 和 bearing (方位)
m_3d = leafmap.Map(
    center=[46.9, 8.4], # 瑞士阿爾卑斯山
    zoom=11,
    pitch=60, # <-- 3D 傾斜角
    bearing=-40, # <-- 旋轉角
    layout_height="800px"
)

# --- 3. 加入 3D 地形 (網格 - Lab 8) ---
m_3d.add_terrain(terrain_url, layer_name="3D 地形")

# --- 4. 加入向量資料 (路線 - Lab 9) ---
# 載入一個範例 GPX 路線
gpx_url = "https://github.com/opengeos/leafmap/raw/master/examples/data/gpx/track.gpx"
m_3d.add_gpx(gpx_url, layer_name="GPX 路線 (Vector)")

# --- 5. 建立 Solara 元件 ---
@solara.component
def Page():
    solara.Title("3D 地形圖 | Solara GIS App")
    
    solara.Markdown("### 3D 地形圖 (Lab 9)")
    solara.Markdown("這張地圖展示了如何將 GPX 向量路線「披覆」在 `ipyleaflet` 的 3D 地形上。")
    
    # 顯示 3D 地圖
    return m_3d.element