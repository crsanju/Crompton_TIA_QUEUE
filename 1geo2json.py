import geopandas as gpd

def match_geojson_with_geopandas(reference_file, new_file, output_file):
    """
    Matches the schema and Coordinate Reference System (CRS) of a 
    new GeoJSON to an existing reference GeoJSON using GeoPandas.
    """
    print("Loading GeoJSON files...")
    
    # 1. Load the GeoJSON files into GeoDataFrames
    try:
        ref_gdf = gpd.read_file(reference_file)
        new_gdf = gpd.read_file(new_file)
    except Exception as e:
        print(f"Error loading files: {e}")
        return

    # 2. Match the Coordinate Reference System (CRS)
    if ref_gdf.crs != new_gdf.crs:
        print(f"Reprojecting new data from {new_gdf.crs} to match reference {ref_gdf.crs}...")
        new_gdf = new_gdf.to_crs(ref_gdf.crs)
    else:
        print(f"CRS already matches: {ref_gdf.crs}")

    # 3. Match the Tabular Schema (Columns)
    ref_columns = ref_gdf.columns.tolist()
    
    # Add any columns that are in the reference but missing in the new data
    for col in ref_columns:
        if col not in new_gdf.columns:
            # Fill missing text/number properties with None (translates to null in JSON)
            new_gdf[col] = None 

    # Subset and reorder the new dataframe to exactly match the reference dataframe
    # This automatically drops any extra columns that weren't in the reference file
    new_gdf = new_gdf[ref_columns]

    # 4. Save the matched output
    print(f"Saving matched data to {output_file}...")
    new_gdf.to_file(output_file, driver='GeoJSON')
    
    print("Done! Format perfectly matched.")

# ==========================================
# Example Usage:
# ==========================================
if __name__ == "__main__":
    # Replace these with your actual file paths
    REFERENCE_GEOJSON = 'existing_format.geojson'
    NEW_GEOJSON = 'new_data.geojson'
    OUTPUT_GEOJSON = 'matched_output.geojson'
    
    match_geojson_with_geopandas(REFERENCE_GEOJSON, NEW_GEOJSON, OUTPUT_GEOJSON)