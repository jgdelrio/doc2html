import pytest
from hamcrest import assert_that, equal_to
import aiofiles

from doc2html import config as cfg, reformat
from tests.expected import *


@pytest.mark.asyncio
async def test__plumber_convert() -> None:
    file_name = "pdf_model.pdf"
    sample = cfg.SAMPLES.joinpath(file_name)
    async with aiofiles.open(sample, 'rb') as file_obj:
        success, data = await reformat.plumber_convert(file_name, file_obj, "htm")

    assert_that(success, equal_to(True))
    assert_that( data, equal_to(EXPECTED_PDF1_PLUNDER_OUTPUT))
