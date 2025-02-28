.. :changelog:

History
-------

0.6.1 (2024-11-15)
__________________
* Resolved the problem with cookie management and re-authentication upon cookie expiration #384;
* Dropped support for Python versions below 3.6 #384;


0.6.0 (2022-11-18)
__________________
* Added support for Python version 3.9 #352;
* Removed support for Python version below 3.0 #352;

0.5.2 (2022-10-12)
__________________
* Added Certificate based authentication logic #330;
* Fixed use of EA inheritance in IP Objects #318;
* Fixed missing fields ('ipv4addr', 'ipv6addr') for 'class Member()' #345;

0.5.1 (2022-03-14)
__________________
* Updated connector's urlencoding logic for proper array encoding #287;
* Updated InfobloxObject's fetch method to raise `InfobloxFetchGotMultipleObjects` exception #288;
* Fix a bug when calling abstracted class from_dict with V4 & V6 subclass #282;
* Fix a bug when updating DNSZone object exception was raised and field not allowed to update #331;
* Fix a bug when ARecord and AAAARecord object skips updating the updatable fields #334, #328;
* Raised an exception while searching with non searchable fields #339;
* Fix errors generated for the client using sphinx with make docs #343;

**0.5.0 (2020-05-14)**
______________________
* Majorly Updated objects with around 380+ NIOS object calls supported now.(Find the infoblox_client/objects.py file to list the supported objects and its descriptions)
* Bug Fixes
* python-six dependency set to >=1.11.0

0.4.25 (2020-03-12)
___________________
* Bug Fixes

0.4.24 (2020-02-25)
___________________
* Added some extra fields(ms_server) for Fixed Address
* Supporting MX record
* Bug Fixes - PTR records now return an IP

0.4.23 (2019-09-10)
___________________

* Added some extra fields for network class
* Fixed update option for A Record
* Adding fields for fixed address

0.4.22 (2019-02-21)
___________________

* Supported returning default fileds plus user required fields reflecting WAPI
* Supporting 'aliases' parameter of HOST record for DNS

0.4.21 (2019-01-18)
___________________

* Supporting wapi version 2.10 or above

0.4.20 (2018-03-27)
___________________

* Updated default WAPI version from 1.4 to 2.1

0.4.19 (2018-02-06)
___________________

* Changed logging of failure on object search from Error to Warning

0.4.18 (2017-11-20)
___________________

* Fix bug related to temporary unavailable status code

0.4.17 (2017-11-09)
___________________

* Added pagination support for wapi calls

0.4.15 (2017-07-18)
___________________

* Changed logic of generate duid using only mac address

0.4.14 (2017-05-18)
___________________

* Add function to check object is created or reused

0.4.13 (2017-03-01)
___________________
* Add TTL field to HostRecordV*
* Add CNAME record support
* Specify return fields for an SRV record

0.4.12 (2016-12-08)
___________________
* Allow search all fields
* Remove ptrdname from PTR record search attributes

0.4.11 (2016-10-31)
___________________
* Add search HostRecords by MAC

0.4.10 (2016-10-24)
___________________
* Updated history and author

0.4.9 (2016-10-24)
__________________
* Add function to get fixed addresses by mac

0.4.8 (2016-10-10)
__________________
* Add ptrdname search option to PtrRecord objects

0.4.7 (2016-07-14)
__________________
* Add zones extensible attribute update support

0.4.6 (2016-07-01)
__________________
* Add network_view support for host records

0.4.5 (2016-06-13)
__________________
* Allow raising exception in create_ea_definition
* Add pep8 check to tox
* Add pep8 check to Travis CI
* Add examples of searching by regular expression

0.4.4 (2016-05-11)
__________________
* Pass only_ref option to update_from_dict
* Do not fail on processing unknown fields
* Fetch only object reference for service restart
* Update README with example of using EA

0.4.3 (2016-03-28)
__________________
* Add default fields for Member
* Update docstring for create_network
* Add  fields to FixedAddressV4 and IPAddress

0.4.2 (2016-03-04)
__________________
* Add max_retries option to connector
* Log failure on get with Error log level

0.4.1 (2016-02-26)
__________________
* Add 'max_results' as connector option

**0.4.0 (2016-02-19)**
______________________
* Add max_results option to connector and objects
* Add Tenant object
* Update README.rst with more examples


0.3.9 (2016-02-18)
__________________
* Add 'configure_for_dns' field for HostRecord

0.3.8 (2016-02-17)
__________________
* Add 'extattrs' to DNSZone/DNSView return_fields

0.3.7 (2016-02-12)
__________________
* Add return_fields to NetworkView

0.3.6 (2016-01-28)
__________________
* Add support for list and tuple values to EA object
* Remove _value_to_bool

0.3.5 (2016-01-22)
__________________
* No changes

0.3.4 (2016-01-21)
__________________
* Do not override verify flag on request level

0.3.3 (2016-01-20)
__________________
* create_required_ea_definitions return created list
* Add 'start_addr', 'end_addr' to ip detection list
* Add request type to connector logger
* Flake8 fixes

0.3.2 (2016-01-19)
__________________
* Convert strings into booleans for ssl_verify
* Update AUTHORS.rst, add contributors
* Remove unused methods from utils.py

0.3.1 (2016-01-14)
__________________
* Add 'zone' to search fields of Host Record


**0.3.0 (2016-01-14)**
______________________
* Update development status from Pre-Alpha to Alpha
* Feature/tox testing (huge changes in testing env)
* Add 'network' to search fields of FixedAddress
* Allow domain-name-servers for ipv6
* Update existent EA for network instead of replace


0.2.3 (2016-01-06)
__________________
* Return None if search failed instead of exception
* Add ip_version as a public property for objects

0.2.2 (2015-12-23)
__________________
* Fix updating object from create method
* Rework delete_all_associated_objects logic
* Fix error handling in create_object
* Do not catch exception on create_dns_zone level
* Update feature version for member_ipv6_setting

0.2.1 (2015-12-18)
__________________
* Add InfobloxMemberAlreadyAssigned exception
* Update dns record if already exists
* Add 'log_api_calls_as_info' option for connector
* Check for empty values in EA

**0.2.0 (2015-12-17)**
______________________
* Deprecate network_exists method in object_manager
* Add _global_field_processing for objects
* Add parsing 'extattrs' into EA objects for all InfobloxObject childs
* Add docs badge to README.rst
* Reworked get_network in object_manager
* Move _eq_ to BaseObject
* Check if fixed address is found before delete


0.1.4 (2015-12-08)
__________________
* Field updates for Member object
* Log all api calls in connector on debug level

0.1.3 (2015-12-04)
__________________
* Add 'network' field to ip versioned fields
* Skip adding DHCP options for IPv6 network
* Do not search IPRange before creating

0.1.2 (2015-12-02)
__________________
* Do not fail if object is not found on delete
* Raise exception with details if reply is not json
* Add 'silent_ssl_warnings' option to connector

0.1.1 (2015-12-01)
__________________
* Fix unbind_name_from_record_a

0.1.0 (2015-12-01)
__________________
* Add new field type '_updateable_search_field' to objects and fix HostRecord search
* Fix 'make docs'
* Update README.rst (fixed formatting)

0.0.11 (2015-11-25)
___________________
* Fix adding second ip to HostRecord
* Fix failing in pdb
* Convert EA values into boolean if possible
* Added 'ips' allias for ip field in HostRecord

0.0.10 (2015-11-19)
___________________
* Add utility to determine supported feature
* Update README.rst with objects interface

0.0.9 (2015-11-13)
__________________
* Add allowed_object_types field for EA Definition
* Allow to return default fields for object
* Update README.rst with list of supported objects

0.0.8 (2015-11-12)
___________________
* Add Extensible Attributes Definition support
* Fixed options processing for create_network in object_manager
* Fixed missed DNSZone object in create_dns_zone

0.0.7 (2015-10-27)
____________________
* Added 'network' to IPRange search fields
* Modified `get` method of the EA class to allow return default values

0.0.6 (2015-10-26)
____________________
* Added initial support of Extensible Attributes as sub objects
* Added search by Extensible Attributes
* Improved validation in connector
* Added delete_object_by_ref to object manager

0.0.5 (2015-10-12)
____________________
* Fixed issues in working with objects
* Added missed _get_object_type_from_ref
* Added code coverage
* Updated links to point to infobloxopen repository

0.0.4 (2015-09-23)
____________________
* Added object abstraction for interacting with NIOS objects
* Added object_manager to simplify some operations on objects

0.0.3 (2015-09-15)
____________________
* Added dependencies to package.


0.0.2 (2015-09-11)
____________________
* Fixed using dashes in package directory names that prevented package import after install.


**0.0.1 (2015-09-11)**
______________________
* Added connector to send wapi requests to NIOS, does not includes NIOS object model at this point.
* First release on PyPI.
