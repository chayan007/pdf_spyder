import os

TARGET_URLS = [
    'https://www.privacy.gov.ph/data-privacy-act-primer/',
    'https://www.privacy.gov.ph/memorandum-circulars/',
    'https://www.privacy.gov.ph/advisories/',
    'https://www.privacy.gov.ph/advisory-opinions/',
    'https://www.privacy.gov.ph/commission-issued-orders/'
]

BASE_URI = 'https://www.privacy.gov.ph'
STRIP_STRING = '../'
PDF_EXTENSION = '.pdf'


class Selectors:
    """Record all selectors."""

    HREF_XPATH = "//a[contains(@href, '.pdf')]/@href"
