.. GeoReport documentation master file, created by
   sphinx-quickstart on Sat Jul  5 02:20:07 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GeoReport documentation
=======================

.. image:: https://img.shields.io/pypi/pyversions/georeport
    :target: https://badge.fury.io/py/georeport
    :alt: PyPI - Python Version

.. image:: https://badge.fury.io/py/georeport.svg
    :target: https://badge.fury.io/py/georeport
    :alt: PyPI version

.. image:: https://readthedocs.org/projects/georeport/badge
    :target: https://georeport.readthedocs.io/en/latest/
    :alt: Read the Docs

.. image:: https://static.pepy.tech/badge/georeport/month
    :target: https://pepy.tech/project/georeport
    :alt: Downloads

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   reference

GeoReport is a thin Python wrapper for the Open311 GeoReport v2 API
standard.

Installing GeoReport
--------------------

GeoReport is available on PyPI:

::

   pip install georeport

Example Usage
-------------

Get the list of services in a city:

::

   from georeport import GeoReport

   client = GeoReport.from_city('Brookline, MA')
   print(client.get_service_list())

Get service requests in a city:

::

   from georeport import GeoReport

   client = GeoReport.from_city('Chicago, IL')
   print(client.get_service_requests())

Supported Features
------------------

GeoReport supports retrieval of requests in addition to service lists
and definitions. However, GeoReport **does not** currently support the
creation of new 311 service requests.