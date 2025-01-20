from typing import Any, Literal, Optional
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("YR")

YR_API_BASE = "https://api.met.no/weatherapi/locationforecast/2.0"

async def make_weather_forecast_request(type: Literal["compact", "complete"], latitude: float, longitude: float, altitude: Optional[int] = None) -> Any:
    """Execute the weather forecast query

    Args:
        type (Literal[&quot;compact&quot;, &quot;complete&quot;]): "compact or complete weather forecast"
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
        altitude (Optional[int], optional): Optional altitude of the location. Defaults to None.

    Returns:
        Any: JSON response
    """
    url = f"{YR_API_BASE}/{type}?lat={latitude}&lon={longitude}"
    if altitude != None:
        url = f"{url}&altitude={altitude}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return "Unable to fetch weather forecast"

@mcp.tool()
async def get_weather_forecast_compact(latitude: float, longitude: float, altitude: Optional[int] = None):
    """Get a compact weather forecast for a specified location

    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
        altitude (Optional[int]): Optional altitude of the location. Defaults to None.
    """
    result = await make_weather_forecast_request(
        type='compact',
        latitude=latitude, 
        longitude=longitude
    )
    return result
        
@mcp.tool()
async def get_weather_forecast_complete(latitude: float, longitude: float, altitude: Optional[int] = None):
    """Get a complete weather forecast for a specified location

    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
        altitude (Optional[int]): Optional altitude of the location
    """
    result = await make_weather_forecast_request(
        type='complete',
        latitude=latitude, 
        longitude=longitude
    )
    return result

if __name__ == "__main__":
    mcp.run(transport="sse")
        
    
            
            