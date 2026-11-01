def player_summary(df):
    return {"jugadores":len(df),"puntos_medios":round(float(df.points.mean()),1) if len(df) else 0}
