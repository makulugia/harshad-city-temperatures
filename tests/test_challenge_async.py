import pytest
import sys
# append the parent folder
sys.path.append('./')
from src.coding_challenge import runReport

@pytest.mark.asyncio
async def test_challenge_async():
    r1, r2, r3 = await runReport('San')
    assert r1.lower().find('san') != -1
    assert r2.lower().find('san') != -1
    assert len(r3) > 0

@pytest.mark.asyncio
async def test_challenge_noresult_async():
    r1, r2, r3 = await runReport('S')
    assert r1.lower().find('na') != -1
    assert r2.lower().find('na') != -1
    assert len(r3) == 0