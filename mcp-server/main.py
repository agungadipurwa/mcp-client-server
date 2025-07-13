from mcp.server.fastmcp import FastMCP
import server
  
mcp = FastMCP(
    name="Logtime-MCP",
    description="A FastAPI-based MCP server for Logtime",
    version="0.1.0",
    stateless_http=True)

@mcp.tool()
async def get_employee_logtime() -> dict:
    """
    Retrieve current date or time and all time of log time. You can use this tool for any query related to project health condition, project based on employee, employee performance.
    Also, you can use this tools for each query related to employee, log time, project condition based on employee, or summary and no need to specify the query type such as clockify, gsheet or any other.
    Returns:
        A dict containing of log time for each project.
    """
    try:
        logs = await server.get_employee_logtime()
        if logs is not None:
            return logs
        else:
            return {"error": "Failed to retrieve log time."}
    except Exception as e:
        return {"error": str(e)}
    
    
@mcp.tool()
async def get_active_projects() -> dict:
    """
    Retrieve current activate project in Clockify. You can use this tool for any query related active project log time without specify the query type such as clockify, gsheet or any other.
    
    Returns:
        A str of json project in the specified workspace.
    """
    try:
        active_projects = await server.get_active_projects()
        if active_projects:
            return active_projects
        else:
            return "Failed to retrieve active projects."
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
    
@mcp.tool()
async def get_detail_project_report() -> dict:
    """
    Retrieve current date and summary detail of time entry project. You can use this tool for any query related to log time and date time.
    Also, you can use this tools for each query related to employee, log time, project, or summary with specify the query type as Clockify.
    Returns:
        A dict containing the summary of log time for each project.
    """
    try:
        summary = await server.get_summary_project()
        if summary is not None:
            return summary
        else:
            return {"error": "Failed to retrieve summary log time."}
    except Exception as e:
        return {"error": str(e)}

# if __name__ == "__main__":
#     mcp.run(transport="stdio")