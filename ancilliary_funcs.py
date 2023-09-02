def retorna_valores(df_parcial):
    variables_continuas = df_parcial.select_dtypes(include=['float64', 'int64'])
    print("Medidas descriptivas de variables continuas")
    print(variables_continuas.describe())
    variables_discretas = df_parcial.select_dtypes(exclude=['float64', 'int64'])
    print("Freecuencia de variables discretas")
    for i in variables_discretas.columns:
        print(f"Nombre de variable: {i}, frecuencia: {df_parcial[i].value_counts()}")



def observaciones_perdidas(df_parcial, var, print_list=False):
    casos_perdidos = df_parcial[var].isna()
    if True in casos_perdidos.values:
        cantidad_casos_perdidos = casos_perdidos.value_counts()[True]
        porcentaje_casos_perdidos = df_parcial[var].isna().value_counts('%')[True]
    else:
        cantidad_casos_perdidos = 0
        porcentaje_casos_perdidos = 0
    if print_list:
        return df_parcial[df_parcial[var].isna()]
    else:
        return {"casos perdidos": cantidad_casos_perdidos, "porcentaje": porcentaje_casos_perdidos} 


#HISTOGRAMA#
def grafica_histograma(sample_df, full_df, var, sample_mean=False, true_mean=False):
    import matplotlib.pyplot as plt
    sample_df_var = sample_df[var].dropna()
    full_df_var = full_df[var].dropna()
    plt.hist(sample_df_var, density=False)
    #aplicamos las condiciones del desafío
    if sample_mean:
        plt.axvline(sample_df_var.mean(), color='tomato', label="Sample mean")
    if true_mean:
        plt.axvline(full_df_var.mean(), color='yellow', label="True mean")
    plt.title(f"Histograma de la variable {var}")
    plt.xlabel(var)
    plt.legend()




def grafica_dotplot(sample_df, full_df, plot_var, plot_by, global_stats=False, statistic='mean'):   
    import matplotlib.pyplot as plt
    if global_stats:
        var_dropna = full_df[full_df[plot_var].notna()]
        group_mean = var_dropna.groupby(plot_by)[plot_var].mean()
        group_median = var_dropna.groupby(plot_by)[plot_var].median()
    else:
        var_dropna = sample_df[sample_df[plot_var].notna()]
        group_mean = var_dropna.groupby(plot_by)[plot_var].mean()
        group_median = var_dropna.groupby(plot_by)[plot_var].median()
    plt.title(f"{plot_var} - {plot_by}")
    plt.xlabel(plot_var)
    plt.ylabel(plot_by)
    if statistic == 'mean':
        return plt.plot(group_mean.values, group_mean.index, 'o'), plt.axvline(var_dropna[plot_var].mean(), color='tomato', label='mean'), plt.legend()
    else:
        return plt.plot(group_median.values, group_median.index, 'o'), plt.axvline(var_dropna[plot_var].median(), color='tomato', label='median'), plt.legend()



def grafica_dotplot_v2(dataframe, plot_var, plot_by, statistic='mean'):   
    import matplotlib.pyplot as plt
    var_dropna = dataframe[dataframe[plot_var].notna()]
    group_mean = var_dropna.groupby(plot_by)[plot_var].mean()
    group_median = var_dropna.groupby(plot_by)[plot_var].median()
    plt.title(f"{plot_var} - {plot_by}")
    plt.xlabel(plot_var)
    plt.ylabel(plot_by)
    if statistic == 'mean':
        return plt.plot(group_mean.values, group_mean.index, 'o'), plt.axvline(var_dropna[plot_var].mean(), color='tomato', label='mean'),     plt.legend()
    else:
        return plt.plot(group_median.values, group_median.index, 'o'), plt.axvline(var_dropna[plot_var].median(), color='tomato', label='median'),     plt.legend()



