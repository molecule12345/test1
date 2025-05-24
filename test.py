import streamlit as st
from streamlit_elements import elements, dashboard, mui, nivo, html

# 设置页面配置
st.set_page_config(page_title="Streamlit-elements使用案例", layout="wide")

# 定义布局
layout = [
    dashboard.Item("面积图", 0, 0, 3, 2),
    dashboard.Item("漏斗图", 3, 0, 3, 2),
    dashboard.Item("曲线图", 0, 2, 3, 2),
    dashboard.Item("柱状图", 3, 2, 3, 2),
    dashboard.Item("雷达图", 0, 4, 3, 2),
    dashboard.Item("饼图", 3, 4, 3, 2),
]

# 使用elements创建一个可拖拽的仪表板
with elements("demo"):
    # 创建一个dashboard
    with dashboard.Grid(layout=layout):
        # 面积图
        with mui.Card(key="面积图"):
            with mui.CardContent:
                nivo.Area(
                    data=[
                        {"x": "A", "y": 10},
                        {"x": "B", "y": 20},
                        {"x": "C", "y": 30},
                    ],
                    keys=["y"],
                    indexBy="x",
                    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
                    padding=0.3,
                    colors=["#61B35A", "#F48FB1", "#FFD700"],
                    borderColor="#FFFFFF",
                    enableGridX=True,
                    enableGridY=True,
                    enableLabel=True,
                    label="y",
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#333333",
                    labelFontSize=12,
                    labelFontWeight="bold",
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#333333",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#333333",
                            }
                        }
                    }
                )

        # 漏斗图
        with mui.Card(key="漏斗图"):
            with mui.CardContent:
                nivo.Funnel(
                    data=[
                        {"label": "A", "value": 100},
                        {"label": "B", "value": 80},
                        {"label": "C", "value": 60},
                    ],
                    keys=["value"],
                    indexBy="label",
                    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
                    colors=["#61B35A", "#F48FB1", "#FFD700"],
                    borderColor="#FFFFFF",
                    enableLabel=True,
                    label="value",
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#333333",
                    labelFontSize=12,
                    labelFontWeight="bold",
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#333333",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#333333",
                            }
                        }
                    }
                )

        # 曲线图
        with mui.Card(key="曲线图"):
            with mui.CardContent:
                nivo.Line(
                    data=[
                        {"x": "A", "y": 10},
                        {"x": "B", "y": 20},
                        {"x": "C", "y": 30},
                    ],
                    keys=["y"],
                    indexBy="x",
                    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
                    padding=0.3,
                    colors=["#61B35A", "#F48FB1", "#FFD700"],
                    borderColor="#FFFFFF",
                    enableGridX=True,
                    enableGridY=True,
                    enableLabel=True,
                    label="y",
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#333333",
                    labelFontSize=12,
                    labelFontWeight="bold",
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#333333",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#333333",
                            }
                        }
                    }
                )

        # 柱状图
        with mui.Card(key="柱状图"):
            with mui.CardContent:
                nivo.Bar(
                    data=[
                        {"x": "A", "y": 10},
                        {"x": "B", "y": 20},
                        {"x": "C", "y": 30},
                    ],
                    keys=["y"],
                    indexBy="x",
                    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
                    padding=0.3,
                    colors=["#61B35A", "#F48FB1", "#FFD700"],
                    borderColor="#FFFFFF",
                    enableLabel=True,
                    label="y",
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#333333",
                    labelFontSize=12,
                    labelFontWeight="bold",
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#333333",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#333333",
                            }
                        }
                    }
                )

        # 雷达图
        with mui.Card(key="雷达图"):
            with mui.CardContent:
                nivo.Radar(
                    data=[
                        {"label": "A", "value": 0.5},
                        {"label": "B", "value": 0.8},
                        {"label": "C", "value": 0.3},
                    ],
                    keys=["value"],
                    indexBy="label",
                    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
                    colors=["#61B35A", "#F48FB1", "#FFD700"],
                    borderColor="#FFFFFF",
                    enableLabel=True,
                    label="value",
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#333333",
                    labelFontSize=12,
                    labelFontWeight="bold",
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#333333",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#333333",
                            }
                        }
                    }
                )

        # 饼图
        with mui.Card(key="饼图"):
            with mui.CardContent:
                nivo.Pie(
                    data=[
                        {"label": "A", "value": 10},
                        {"label": "B", "value": 20},
                        {"label": "C", "value": 30},
                    ],
                    keys=["value"],
                    indexBy="label",
                    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
                    colors=["#61B35A", "#F48FB1", "#FFD700"],
                    borderColor="#FFFFFF",
                    enableLabel=True,
                    label="value",
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#333333",
                    labelFontSize=12,
                    labelFontWeight="bold",
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#333333",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#333333",
                            }
                        }
                    }
                )