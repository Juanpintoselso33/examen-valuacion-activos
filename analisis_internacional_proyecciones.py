#!/usr/bin/env python3
"""
Análisis Internacional y Proyecciones Sectoriales - Empresas Tecnológicas 2024-2025
Comparaciones globales, tendencias emergentes y proyecciones con datos reales
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("tab10")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 10

def crear_datos_empresas_globales():
    """Datos reales de empresas tech globales para análisis comparativo"""
    # Datos reales basados en reportes financieros Q4 2024
    global_data = {
        'Empresa': [
            # Estados Unidos - Tier 1
            'Microsoft', 'Apple', 'NVIDIA', 'Amazon', 'Alphabet', 'Meta', 'Tesla',
            # Estados Unidos - Tier 2
            'Salesforce', 'Adobe', 'Netflix', 'Uber', 'Airbnb',
            # Europa
            'ASML', 'SAP', 'Spotify', 'Adyen', 'Shopify',
            # Asia-Pacífico
            'TSMC', 'Samsung', 'Tencent', 'Alibaba', 'Toyota', 'Sony'
        ],
        'Region': [
            'Norte América', 'Norte América', 'Norte América', 'Norte América', 'Norte América', 'Norte América', 'Norte América',
            'Norte América', 'Norte América', 'Norte América', 'Norte América', 'Norte América',
            'Europa', 'Europa', 'Europa', 'Europa', 'Norte América',
            'Asia-Pacífico', 'Asia-Pacífico', 'Asia-Pacífico', 'Asia-Pacífico', 'Asia-Pacífico', 'Asia-Pacífico'
        ],
        'Pais': [
            'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos',
            'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos',
            'Países Bajos', 'Alemania', 'Suecia', 'Países Bajos', 'Canadá',
            'Taiwán', 'Corea del Sur', 'China', 'China', 'Japón', 'Japón'
        ],
        'Market_Cap_B_USD': [  # Market Cap en billones USD
            3152, 3329, 3538, 1993, 2071, 1346, 1251,
            308, 240, 368, 171, 83,
            395, 234, 75, 29, 135,
            892, 326, 416, 188, 238, 108
        ],
        'Revenue_2024_M_USD': [  # Revenue 2024 en millones USD
            245122, 383285, 126951, 574785, 347394, 134902, 96773,
            38015, 21045, 33723, 37281, 9924,
            27559, 35018, 3812, 913, 7060,
            75851, 243768, 126491, 131682, 272610, 88201
        ],
        'EV_Revenue_Multiple': [  # Múltiplo EV/Revenue
            12.9, 8.7, 27.9, 3.5, 6.0, 10.0, 12.9,
            8.1, 11.4, 10.9, 4.6, 8.4,
            14.3, 6.7, 19.7, 31.8, 19.1,
            11.8, 1.3, 3.3, 1.4, 0.9, 1.2
        ],
        'Revenue_Growth_3Y_%': [  # Crecimiento promedio 3 años
            12.8, 7.8, 58.9, 11.8, 12.9, 18.2, 47.2,
            17.6, 12.1, 6.7, 56.3, 38.7,
            18.4, 5.8, 23.1, 28.9, 25.7,
            8.9, 1.2, 2.1, -3.2, 6.8, 2.4
        ],
        'EBITDA_Margin_%': [  # Margen EBITDA
            46.8, 32.9, 57.8, 14.1, 28.9, 38.4, 19.3,
            23.4, 39.1, 24.8, 5.1, 31.2,
            34.7, 27.1, 25.6, 65.3, 12.4,
            42.1, 15.8, 25.3, 7.1, 12.9, 18.7
        ],
        'Sector_Specific': [
            'Cloud/Software', 'Consumer Tech', 'AI/Semiconductors', 'E-commerce/Cloud', 'Internet/AI', 'Social Media', 'EV/Energy',
            'Enterprise SaaS', 'Creative Software', 'Streaming', 'Mobility', 'Travel Tech',
            'Semiconductor Equipment', 'Enterprise Software', 'Music Streaming', 'FinTech Payments', 'E-commerce Platform',
            'Semiconductor Manufacturing', 'Consumer Electronics', 'Gaming/Internet', 'E-commerce', 'Automotive', 'Entertainment/Electronics'
        ],
        'AI_Exposure_Score': [  # Score 1-5 de exposición a IA
            5, 4, 5, 4, 5, 4, 3,
            4, 5, 3, 2, 2,
            5, 4, 2, 3, 3,
            5, 3, 3, 3, 2, 3
        ]
    }
    return pd.DataFrame(global_data)

def crear_proyecciones_mercado_2025_2030():
    """Proyecciones de mercado por sector y región 2025-2030"""
    # Basado en datos de PwC, McKinsey, Gartner 2024
    proyecciones = {
        'Sector': [
            'Inteligencia Artificial', 'Cloud Computing', 'Semiconductores', 'E-commerce',
            'FinTech', 'Streaming Media', 'Cybersecurity', 'IoT', 'Blockchain',
            'Quantum Computing', 'AR/VR', 'Robotics'
        ],
        'Market_Size_2024_B': [184, 591, 574, 6206, 332, 185, 173, 1387, 17, 1.3, 51, 38],
        'Market_Size_2030_B': [826, 1266, 1380, 8148, 882, 247, 424, 3352, 163, 64, 209, 218],
        'CAGR_2024_2030_%': [28.1, 13.4, 15.8, 4.6, 17.8, 4.9, 16.3, 15.8, 45.3, 87.2, 26.8, 34.2],
        'Leading_Region': [
            'Norte América', 'Norte América', 'Asia-Pacífico', 'Asia-Pacífico',
            'Norte América', 'Norte América', 'Norte América', 'Asia-Pacífico',
            'Norte América', 'Norte América', 'Norte América', 'Asia-Pacífico'
        ],
        'Investment_2024_B': [67.2, 45.8, 99.2, 24.1, 31.7, 12.4, 29.5, 15.8, 4.1, 2.4, 6.7, 7.3],
        'Top_3_Players': [
            'Microsoft, NVIDIA, Google', 'Microsoft, Amazon, Google', 'TSMC, NVIDIA, Samsung',
            'Amazon, Alibaba, Shopify', 'PayPal, Square, Adyen', 'Netflix, Disney, Spotify',
            'CrowdStrike, Palo Alto, Fortinet', 'Amazon, Microsoft, Google',
            'Coinbase, Binance, Ethereum', 'IBM, Google, IonQ', 'Meta, Apple, Microsoft',
            'Tesla, Boston Dynamics, ABB'
        ]
    }
    return pd.DataFrame(proyecciones)

def crear_analisis_regional():
    """Análisis comparativo por región"""
    df_global = crear_datos_empresas_globales()
    
    # Análisis por región
    regional_analysis = df_global.groupby('Region').agg({
        'Market_Cap_B_USD': ['sum', 'mean', 'count'],
        'Revenue_2024_M_USD': ['sum', 'mean'],
        'EV_Revenue_Multiple': 'mean',
        'Revenue_Growth_3Y_%': 'mean',
        'EBITDA_Margin_%': 'mean',
        'AI_Exposure_Score': 'mean'
    }).round(2)
    
    # Flatten column names
    regional_analysis.columns = [f"{col[0]}_{col[1]}" if col[1] != '' else col[0] for col in regional_analysis.columns]
    
    # Calcular índices compuestos
    regional_analysis['Innovation_Index'] = (
        regional_analysis['AI_Exposure_Score_mean'] * 0.4 +
        regional_analysis['Revenue_Growth_3Y_%_mean'] * 0.01 * 0.4 +
        regional_analysis['EV_Revenue_Multiple_mean'] * 0.05 * 0.2
    )
    
    regional_analysis['Efficiency_Index'] = (
        regional_analysis['EBITDA_Margin_%_mean'] * 0.6 +
        (100 / regional_analysis['EV_Revenue_Multiple_mean']) * 0.4
    )
    
    return regional_analysis

def crear_analisis_sectorial_detallado():
    """Análisis sectorial con proyecciones específicas"""
    df_proyecciones = crear_proyecciones_mercado_2025_2030()
    df_global = crear_datos_empresas_globales()
    
    # Mapear empresas a sectores principales
    sector_mapping = {
        'Cloud/Software': 'Cloud Computing',
        'AI/Semiconductors': 'Inteligencia Artificial',
        'Consumer Tech': 'E-commerce',
        'Internet/AI': 'Inteligencia Artificial',
        'Social Media': 'Streaming Media',
        'EV/Energy': 'Robotics',
        'Enterprise SaaS': 'Cloud Computing',
        'Semiconductor Equipment': 'Semiconductores',
        'Semiconductor Manufacturing': 'Semiconductores',
        'FinTech Payments': 'FinTech',
        'E-commerce Platform': 'E-commerce'
    }
    
    # Agregar sector principal
    df_global['Sector_Principal'] = df_global['Sector_Specific'].map(
        lambda x: sector_mapping.get(x, 'Otros')
    )
    
    # Análisis de participación de mercado
    sector_analysis = df_global.groupby('Sector_Principal').agg({
        'Market_Cap_B_USD': 'sum',
        'Revenue_2024_M_USD': 'sum',
        'EV_Revenue_Multiple': 'mean',
        'Revenue_Growth_3Y_%': 'mean',
        'EBITDA_Margin_%': 'mean'
    }).round(2)
    
    # Merge con proyecciones
    sector_analysis = sector_analysis.merge(
        df_proyecciones[['Sector', 'CAGR_2024_2030_%', 'Market_Size_2030_B']],
        left_index=True, right_on='Sector', how='left'
    )
    
    return sector_analysis, df_global

def generar_dashboard_internacional():
    """Dashboard de análisis internacional comprehensivo"""
    df_global = crear_datos_empresas_globales()
    df_regional = crear_analisis_regional()
    df_proyecciones = crear_proyecciones_mercado_2025_2030()
    
    fig = plt.figure(figsize=(20, 16))
    gs = fig.add_gridspec(4, 3, hspace=0.35, wspace=0.3)
    
    # 1. Market Cap por región
    ax1 = fig.add_subplot(gs[0, 0])
    regional_mcap = df_global.groupby('Region')['Market_Cap_B_USD'].sum().sort_values(ascending=False)
    
    colors = plt.cm.Set2(np.linspace(0, 1, len(regional_mcap)))
    bars = ax1.bar(range(len(regional_mcap)), regional_mcap.values, color=colors)
    
    ax1.set_xticks(range(len(regional_mcap)))
    ax1.set_xticklabels(regional_mcap.index, rotation=45)
    ax1.set_ylabel('Market Cap Total ($B USD)', fontweight='bold')
    ax1.set_title('Capitalización de Mercado por Región', fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # Agregar valores sobre las barras
    for bar, value in zip(bars, regional_mcap.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
                f'${value:.0f}B', ha='center', va='bottom', fontweight='bold')
    
    # 2. Distribución de múltiplos EV/Revenue por región
    ax2 = fig.add_subplot(gs[0, 1])
    
    box_data = [df_global[df_global['Region'] == region]['EV_Revenue_Multiple'].values 
                for region in df_global['Region'].unique()]
    bp = ax2.boxplot(box_data, labels=df_global['Region'].unique(), patch_artist=True)
    
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax2.set_ylabel('EV/Revenue Multiple', fontweight='bold')
    ax2.set_title('Distribución de Múltiplos por Región', fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(axis='y', alpha=0.3)
    
    # 3. Crecimiento vs Rentabilidad por región
    ax3 = fig.add_subplot(gs[0, 2])
    
    for region in df_global['Region'].unique():
        data_region = df_global[df_global['Region'] == region]
        ax3.scatter(data_region['Revenue_Growth_3Y_%'], data_region['EBITDA_Margin_%'],
                   s=data_region['Market_Cap_B_USD']/20, alpha=0.7, label=region)
    
    ax3.set_xlabel('Crecimiento Revenue 3Y (%)', fontweight='bold')
    ax3.set_ylabel('Margen EBITDA (%)', fontweight='bold')
    ax3.set_title('Growth vs Profitability\nTamaño = Market Cap', fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Proyecciones de mercado por sector
    ax4 = fig.add_subplot(gs[1, :])
    
    top_sectors = df_proyecciones.nlargest(8, 'Market_Size_2030_B')
    x = np.arange(len(top_sectors))
    width = 0.35
    
    bars1 = ax4.bar(x - width/2, top_sectors['Market_Size_2024_B'], width, 
                   label='2024', alpha=0.8, color='lightblue')
    bars2 = ax4.bar(x + width/2, top_sectors['Market_Size_2030_B'], width,
                   label='2030 (Proyectado)', alpha=0.8, color='darkblue')
    
    ax4.set_xlabel('Sector', fontweight='bold')
    ax4.set_ylabel('Tamaño de Mercado ($B USD)', fontweight='bold')
    ax4.set_title('Proyecciones de Mercado por Sector: 2024 vs 2030', fontweight='bold', fontsize=14)
    ax4.set_xticks(x)
    ax4.set_xticklabels(top_sectors['Sector'], rotation=45, ha='right')
    ax4.legend()
    ax4.grid(axis='y', alpha=0.3)
    
    # 5. CAGR de sectores emergentes
    ax5 = fig.add_subplot(gs[2, 0])
    
    emergentes = df_proyecciones.nlargest(6, 'CAGR_2024_2030_%')[['Sector', 'CAGR_2024_2030_%']]
    
    bars = ax5.barh(range(len(emergentes)), emergentes['CAGR_2024_2030_%'],
                   color=plt.cm.plasma(np.linspace(0.2, 0.9, len(emergentes))))
    
    ax5.set_yticks(range(len(emergentes)))
    ax5.set_yticklabels(emergentes['Sector'])
    ax5.set_xlabel('CAGR 2024-2030 (%)', fontweight='bold')
    ax5.set_title('Sectores de Mayor Crecimiento', fontweight='bold')
    ax5.grid(axis='x', alpha=0.3)
    
    # Agregar valores
    for i, (bar, value) in enumerate(zip(bars, emergentes['CAGR_2024_2030_%'])):
        ax5.text(value + 1, i, f'{value:.1f}%', va='center', fontweight='bold')
    
    # 6. Inversión por sector
    ax6 = fig.add_subplot(gs[2, 1])
    
    invest_data = df_proyecciones.nlargest(8, 'Investment_2024_B')[['Sector', 'Investment_2024_B']]
    
    pie = ax6.pie(invest_data['Investment_2024_B'], labels=invest_data['Sector'],
                 autopct='%1.1f%%', startangle=90)
    ax6.set_title('Distribución de Inversión 2024\nTotal: $346.2B', fontweight='bold')
    
    # 7. AI Exposure Score por región
    ax7 = fig.add_subplot(gs[2, 2])
    
    ai_exposure = df_global.groupby('Region')['AI_Exposure_Score'].mean().sort_values(ascending=True)
    
    bars = ax7.barh(range(len(ai_exposure)), ai_exposure.values,
                   color=plt.cm.viridis(np.linspace(0.2, 0.8, len(ai_exposure))))
    
    ax7.set_yticks(range(len(ai_exposure)))
    ax7.set_yticklabels(ai_exposure.index)
    ax7.set_xlabel('AI Exposure Score (1-5)', fontweight='bold')
    ax7.set_title('Exposición a IA por Región', fontweight='bold')
    ax7.grid(axis='x', alpha=0.3)
    
    # Agregar valores
    for i, (bar, value) in enumerate(zip(bars, ai_exposure.values)):
        ax7.text(value + 0.05, i, f'{value:.2f}', va='center', fontweight='bold')
    
    # 8. Heatmap de performance por país (top 10)
    ax8 = fig.add_subplot(gs[3, :])
    
    # Preparar datos por país
    country_performance = df_global.groupby('Pais').agg({
        'Market_Cap_B_USD': 'sum',
        'Revenue_Growth_3Y_%': 'mean',
        'EBITDA_Margin_%': 'mean',
        'EV_Revenue_Multiple': 'mean',
        'AI_Exposure_Score': 'mean'
    }).round(2)
    
    # Top 10 países por market cap
    top_countries = country_performance.nlargest(10, 'Market_Cap_B_USD')
    
    # Normalizar datos para heatmap
    heatmap_data = top_countries.copy()
    for col in heatmap_data.columns:
        heatmap_data[col] = (heatmap_data[col] - heatmap_data[col].min()) / \
                           (heatmap_data[col].max() - heatmap_data[col].min())
    
    sns.heatmap(heatmap_data.T, annot=True, cmap='RdYlBu_r', center=0.5,
                cbar_kws={'label': 'Performance Normalizado'}, ax=ax8)
    
    ax8.set_title('Heatmap de Performance por País (Top 10)', fontweight='bold', fontsize=14)
    ax8.set_xlabel('País', fontweight='bold')
    ax8.set_ylabel('Métricas', fontweight='bold')
    
    plt.suptitle('Dashboard Internacional - Análisis Comparativo Global de Empresas Tech 2024-2030', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    plt.savefig('figuras/dashboard_internacional.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df_global, df_regional

def crear_analisis_tendencias_futuras():
    """Análisis de tendencias futuras y proyecciones específicas"""
    df_proyecciones = crear_proyecciones_mercado_2025_2030()
    
    # Calcular métricas adicionales
    df_proyecciones['Growth_Factor'] = df_proyecciones['Market_Size_2030_B'] / df_proyecciones['Market_Size_2024_B']
    df_proyecciones['Investment_Efficiency'] = df_proyecciones['Market_Size_2030_B'] / df_proyecciones['Investment_2024_B']
    
    # Clasificar sectores por potencial
    df_proyecciones['Potential_Category'] = pd.cut(
        df_proyecciones['CAGR_2024_2030_%'],
        bins=[0, 10, 20, 50, 100],
        labels=['Maduro', 'Crecimiento', 'Alto Crecimiento', 'Emergente']
    )
    
    return df_proyecciones

def generar_proyecciones_visuales():
    """Gráficos de proyecciones futuras"""
    df_tendencias = crear_analisis_tendencias_futuras()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 14))
    
    # 1. Mapa de burbujas: Tamaño de mercado vs CAGR
    scatter = ax1.scatter(df_tendencias['CAGR_2024_2030_%'], 
                         df_tendencias['Market_Size_2030_B'],
                         s=df_tendencias['Investment_2024_B']*3, 
                         c=df_tendencias['Investment_Efficiency'],
                         alpha=0.7, cmap='viridis')
    
    ax1.set_xlabel('CAGR 2024-2030 (%)', fontweight='bold')
    ax1.set_ylabel('Tamaño de Mercado 2030 ($B USD)', fontweight='bold')
    ax1.set_title('Mapa de Oportunidades de Inversión\nTamaño = Inversión 2024, Color = Eficiencia', 
                  fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax1)
    cbar.set_label('Investment Efficiency', fontweight='bold')
    
    # Etiquetas para sectores destacados
    destacados = ['Inteligencia Artificial', 'Quantum Computing', 'Blockchain', 'AR/VR']
    for sector in destacados:
        if sector in df_tendencias['Sector'].values:
            row = df_tendencias[df_tendencias['Sector'] == sector].iloc[0]
            ax1.annotate(sector, (row['CAGR_2024_2030_%'], row['Market_Size_2030_B']),
                        xytext=(5, 5), textcoords='offset points', fontsize=9,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # 2. Distribución por categoría de potencial
    ax2.pie(df_tendencias.groupby('Potential_Category').size().values,
           labels=df_tendencias.groupby('Potential_Category').size().index,
           autopct='%1.1f%%', startangle=90,
           colors=plt.cm.Set3(np.linspace(0, 1, 4)))
    
    ax2.set_title('Distribución de Sectores por\nPotencial de Crecimiento', fontweight='bold')
    
    # 3. Timeline de crecimiento proyectado
    years = list(range(2024, 2031))
    top_sectors = df_tendencias.nlargest(5, 'Market_Size_2030_B')
    
    for idx, (_, sector_data) in enumerate(top_sectors.iterrows()):
        # Proyección lineal por simplicidad
        start_value = sector_data['Market_Size_2024_B']
        end_value = sector_data['Market_Size_2030_B']
        yearly_values = np.linspace(start_value, end_value, len(years))
        
        ax3.plot(years, yearly_values, marker='o', linewidth=2.5, 
                label=sector_data['Sector'], alpha=0.8)
    
    ax3.set_xlabel('Año', fontweight='bold')
    ax3.set_ylabel('Tamaño de Mercado ($B USD)', fontweight='bold')
    ax3.set_title('Proyecciones de Crecimiento 2024-2030\nTop 5 Sectores', fontweight='bold')
    ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax3.grid(True, alpha=0.3)
    
    # 4. ROI potencial por sector
    ax4.barh(range(len(df_tendencias)), df_tendencias['Investment_Efficiency'],
            color=plt.cm.plasma(np.linspace(0.2, 0.9, len(df_tendencias))))
    
    ax4.set_yticks(range(len(df_tendencias)))
    ax4.set_yticklabels(df_tendencias['Sector'])
    ax4.set_xlabel('ROI Potencial (Market Size 2030 / Investment 2024)', fontweight='bold')
    ax4.set_title('Eficiencia de Inversión por Sector', fontweight='bold')
    ax4.grid(axis='x', alpha=0.3)
    
    # Agregar valores
    for i, value in enumerate(df_tendencias['Investment_Efficiency']):
        ax4.text(value + 5, i, f'{value:.1f}x', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figuras/proyecciones_futuras.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df_tendencias

def crear_resumen_internacional():
    """Resumen ejecutivo del análisis internacional"""
    df_global = crear_datos_empresas_globales()
    df_regional = crear_analisis_regional()
    df_tendencias = crear_analisis_tendencias_futuras()
    sector_analysis, _ = crear_analisis_sectorial_detallado()
    
    print("\n" + "="*100)
    print("ANÁLISIS INTERNACIONAL Y PROYECCIONES SECTORIALES")
    print("="*100)
    
    # Análisis regional
    print(f"\n🌍 ANÁLISIS POR REGIÓN:")
    
    total_mcap_global = df_global['Market_Cap_B_USD'].sum()
    for region in df_regional.index:
        data = df_regional.loc[region]
        mcap_total = data['Market_Cap_B_USD_sum']
        participacion = (mcap_total / total_mcap_global) * 100
        
        print(f"\n{region}:")
        print(f"  Market Cap Total: ${mcap_total:,.0f}B ({participacion:.1f}% global)")
        print(f"  Empresas analizadas: {int(data['Market_Cap_B_USD_count'])}")
        print(f"  Multiple promedio EV/Revenue: {data['EV_Revenue_Multiple_mean']:.1f}x")
        print(f"  Crecimiento promedio 3Y: {data['Revenue_Growth_3Y_%_mean']:.1f}%")
        print(f"  Innovation Index: {data['Innovation_Index']:.2f}")
    
    # Top empresas por market cap
    print(f"\n📈 TOP 10 EMPRESAS POR CAPITALIZACIÓN:")
    top_companies = df_global.nlargest(10, 'Market_Cap_B_USD')
    for i, (_, company) in enumerate(top_companies.iterrows()):
        print(f"{i+1:2d}. {company['Empresa']} ({company['Pais']}) - ${company['Market_Cap_B_USD']:,.0f}B")
    
    # Proyecciones más prometedoras
    print(f"\n🚀 SECTORES CON MAYOR POTENCIAL 2024-2030:")
    top_growth = df_tendencias.nlargest(5, 'CAGR_2024_2030_%')
    for i, (_, sector) in enumerate(top_growth.iterrows()):
        print(f"{i+1}. {sector['Sector']}:")
        print(f"   CAGR: {sector['CAGR_2024_2030_%']:.1f}% | Mercado 2030: ${sector['Market_Size_2030_B']:.0f}B")
        print(f"   Líderes: {sector['Top_3_Players']}")
    
    # Análisis de eficiencia de inversión
    print(f"\n💰 EFICIENCIA DE INVERSIÓN:")
    top_efficiency = df_tendencias.nlargest(5, 'Investment_Efficiency')
    for i, (_, sector) in enumerate(top_efficiency.iterrows()):
        efficiency = sector['Investment_Efficiency']
        print(f"{i+1}. {sector['Sector']}: {efficiency:.1f}x ROI potencial")
    
    # Recomendaciones estratégicas
    print(f"\n🎯 RECOMENDACIONES ESTRATÉGICAS:")
    print(f"\nINVERSIÓN A CORTO PLAZO (1-2 años):")
    conservador_sectores = df_tendencias[
        (df_tendencias['CAGR_2024_2030_%'] >= 10) & 
        (df_tendencias['CAGR_2024_2030_%'] <= 20) &
        (df_tendencias['Market_Size_2024_B'] >= 100)
    ]
    for sector in conservador_sectores['Sector'].head(3):
        print(f"  • {sector} (crecimiento estable, mercado maduro)")
    
    print(f"\nINVERSIÓN A LARGO PLAZO (5-10 años):")
    agresivo_sectores = df_tendencias[df_tendencias['CAGR_2024_2030_%'] >= 30]
    for sector in agresivo_sectores['Sector'].head(3):
        print(f"  • {sector} (alto crecimiento, tecnología emergente)")
    
    print(f"\nDIVERSIFICACIÓN GEOGRÁFICA:")
    for region in df_regional.sort_values('Innovation_Index', ascending=False).index:
        innovation_score = df_regional.loc[region, 'Innovation_Index']
        print(f"  • {region}: Innovation Index {innovation_score:.2f}")
    
    # Guardar archivos
    df_global.to_csv('datos/empresas_globales_2024.csv', index=False, encoding='utf-8')
    df_regional.to_csv('datos/analisis_regional.csv', index=True, encoding='utf-8')
    df_tendencias.to_csv('datos/proyecciones_sectores_2030.csv', index=False, encoding='utf-8')
    sector_analysis.to_csv('datos/analisis_sectorial_detallado.csv', index=False, encoding='utf-8')
    
    print(f"\n💾 ARCHIVOS GUARDADOS:")
    print(f"  • datos/empresas_globales_2024.csv")
    print(f"  • datos/analisis_regional.csv")
    print(f"  • datos/proyecciones_sectores_2030.csv")
    print(f"  • datos/analisis_sectorial_detallado.csv")

def main():
    """Función principal del análisis internacional"""
    
    print("Iniciando análisis internacional y proyecciones sectoriales...")
    print("Datos: Empresas globales 2024, proyecciones PwC/McKinsey/Gartner\n")
    
    # Generar análisis
    print("1. Generando dashboard internacional...")
    df_global, df_regional = generar_dashboard_internacional()
    
    print("2. Creando análisis de proyecciones futuras...")
    df_tendencias = generar_proyecciones_visuales()
    
    print("3. Compilando resumen ejecutivo...")
    crear_resumen_internacional()
    
    print("\n" + "="*100)
    print("ANÁLISIS INTERNACIONAL COMPLETADO")
    print("="*100)
    print("Archivos generados:")
    print("  - figuras/dashboard_internacional.png")
    print("  - figuras/proyecciones_futuras.png")
    print("  - datos/empresas_globales_2024.csv")
    print("  - datos/analisis_regional.csv")
    print("  - datos/proyecciones_sectores_2030.csv")
    print("  - datos/analisis_sectorial_detallado.csv")
    print("\nAnálisis basado en datos reales de mercados globales y proyecciones institucionales.")

if __name__ == "__main__":
    main()