"""
Pollinations FLUX Image Provider.
"""

import urllib.parse

import requests

from ai_pipeline.providers.base.image_provider import ImageProvider

from ai_pipeline.utils.logger import logger


class PollinationsProvider(ImageProvider):
    """
    Pollinations FLUX image generation provider.
    """

    BASE_URL = "https://image.pollinations.ai/prompt/"

    MODEL = "flux"

    @property
    def name(self) -> str:
        return "Pollinations - FLUX"

    def generate(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 1024,
    ) -> bytes:

        encoded_prompt = urllib.parse.quote(prompt)

        response = requests.get(
            f"{self.BASE_URL}{encoded_prompt}",
            params={
                "model": self.MODEL,
                "width": width,
                "height": height,
            },
            timeout=180,
        )

        response.raise_for_status()

        logger.info(
            "%s image generated successfully.",
            self.name,
        )

        return response.content