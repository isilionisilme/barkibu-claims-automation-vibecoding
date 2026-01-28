"""
Example regression test demonstrating end-to-end testing.

This test simulates real client behavior (frontend → backend interaction).
"""

import pytest
from httpx import AsyncClient
from backend.app.main import app


@pytest.mark.asyncio
@pytest.mark.timeout(30)
async def test_api_health_check():
    """
    Regression test: Verify API health check endpoint.
    
    This simulates a frontend checking if the backend is available.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Frontend makes health check request
        response = await client.get("/health")
        
        # Verify response
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


@pytest.mark.asyncio
@pytest.mark.timeout(30)
async def test_api_root_endpoint():
    """
    Regression test: Verify root endpoint returns expected data.
    
    This simulates a frontend fetching API information.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Frontend makes request to root endpoint
        response = await client.get("/")
        
        # Verify response
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert data["version"] == "0.1.0"


@pytest.mark.asyncio
@pytest.mark.timeout(30)
async def test_full_workflow_simulation():
    """
    Regression test: Simulate complete user workflow.
    
    This test represents a typical user journey:
    1. Check API health
    2. Get API information
    3. (Future: Upload document, process, retrieve results)
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Step 1: Health check
        health_response = await client.get("/health")
        assert health_response.status_code == 200
        
        # Step 2: Get API info
        info_response = await client.get("/")
        assert info_response.status_code == 200
        
        # Future steps would include:
        # - Document upload
        # - Processing status check
        # - Results retrieval
        # - Data validation
        
        # For now, verify basic connectivity works
        assert True, "Basic workflow completed successfully"
