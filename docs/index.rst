.. GeoReport documentation master file, created by
   sphinx-quickstart on Sat Jul  5 02:20:07 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GeoReport documentation
=======================

.. raw:: html
   <a href="https://badge.fury.io/py/georeport">
      <img src="https://img.shields.io/pypi/pyversions/georeport" alt = "PyPI - Python Version">
   </a>

.. raw:: html
   <a href="https://badge.fury.io/py/georeport">
      <img src="https://badge.fury.io/py/georeport.svg" alt = "PyPI version">
   </a>

.. raw:: html
   <a href="https://georeport.readthedocs.io/en/latest/">
      <img src="https://readthedocs.org/projects/georeport/badge" alt = "Read the Docs">
   </a>

.. raw:: html
   <a href="https://pepy.tech/project/georeport">
      <img src="https://static.pepy.tech/badge/georeport/month" alt = "Downloads">
   </a>

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