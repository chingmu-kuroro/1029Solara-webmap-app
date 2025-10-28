# 這個頁面包含了 2D 向量和 2D 網格資料。
import solara
import leafmap.leafmap as leafmap # 關鍵：使用 ipyleaflet 後端
import geopandas as gpd

# --- 1. 建立地圖物件 (m) ---
# 我們在地圖載入時就建立它，這樣它就只會被建立一次
m = leafmap.Map(
    center=[24.0, 121.0],
    zoom=4,
    pitch=0, # 2D 模式
    layout_height="800px" # Solara 中建議用 layout_height
)

# --- 2. 載入向量資料 (Lab 6) ---
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
gdf = gpd.read_file(url)
m.add_gdf(gdf, layer_name="國家 (Vector)", style={"fillOpacity": 0.2})

# --- 3. 加入網格資料 (Lab 7) ---
cog_url = "https://github.com/opengeos/leafmap/raw/master/examples/data/cog.tif"
m.add_raster(cog_url, palette="terrain", layer_name="Global DEM (Raster)")

# --- 4. 加入圖層控制器 ---
m.add_layer_control()

# --- 5. 建立 Solara 元件 ---
@solara.component
def Page():
    solara.Title("2D 地圖 | Solara GIS App")
    
    # 關鍵：使用 .element 將 ipywidget (我們的地圖 m) 轉換為 Solara 元件
    # Solara 會自動處理所有雙向通訊
    return m.element