# coding: utf-8

# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Manage lifecycle of your Cloud resources using Resource Controller APIs. Resources are
provisioned globally in an account scope. Supports asynchronous provisioning of resources.
Enables consumption of a global resource through a Cloud Foundry space in any region.
"""

from datetime import datetime
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ResourceControllerV2(BaseService):
    """The resource_controller V2 service."""

    DEFAULT_SERVICE_URL = 'https://resource-controller.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'resource_controller'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ResourceControllerV2':
        """
        Return a new client for the resource_controller service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the resource_controller service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Resource Instances
    #########################


    def list_resource_instances(self,
        *,
        guid: str = None,
        name: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_plan_id: str = None,
        type: str = None,
        sub_type: str = None,
        limit: str = None,
        updated_from: str = None,
        updated_to: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of all resource instances.

        Get a list of all resource instances.

        :param str guid: (optional) When you provision a new resource in the
               specified location for the selected plan, a GUID (globally unique
               identifier) is created. This is a unique internal GUID managed by Resource
               controller that corresponds to the instance.
        :param str name: (optional) The human-readable name of the instance.
        :param str resource_group_id: (optional) Short ID of a resource group.
        :param str resource_id: (optional) The unique ID of the offering. This
               value is provided by and stored in the global catalog.
        :param str resource_plan_id: (optional) The unique ID of the plan
               associated with the offering. This value is provided by and stored in the
               global catalog.
        :param str type: (optional) The type of the instance. For example,
               `service_instance`.
        :param str sub_type: (optional) The sub-type of instance, e.g. `cfaas`.
        :param str limit: (optional) Limit on how many items should be returned.
        :param str updated_from: (optional) Start date inclusive filter.
        :param str updated_to: (optional) End date inclusive filter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceInstancesList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_resource_instances')
        headers.update(sdk_headers)

        params = {
            'guid': guid,
            'name': name,
            'resource_group_id': resource_group_id,
            'resource_id': resource_id,
            'resource_plan_id': resource_plan_id,
            'type': type,
            'sub_type': sub_type,
            'limit': limit,
            'updated_from': updated_from,
            'updated_to': updated_to
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_instance(self,
        name: str,
        target: str,
        resource_group: str,
        resource_plan_id: str,
        *,
        tags: List[str] = None,
        allow_cleanup: bool = None,
        parameters: dict = None,
        entity_lock: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create (provision) a new resource instance.

        Provision a new resource in the specified location for the selected plan.

        :param str name: The name of the instance. Must be 180 characters or less
               and cannot include any special characters other than `(space) - . _ :`.
        :param str target: The deployment location where the instance should be
               hosted.
        :param str resource_group: Short or long ID of resource group.
        :param str resource_plan_id: The unique ID of the plan associated with the
               offering. This value is provided by and stored in the global catalog.
        :param List[str] tags: (optional) Tags that are attached to the instance
               after provisioning. These tags can be searched and managed through the
               Tagging API in IBM Cloud.
        :param bool allow_cleanup: (optional) A boolean that dictates if the
               resource instance should be deleted (cleaned up) during the processing of a
               region instance delete call.
        :param dict parameters: (optional) Configuration options represented as
               key-value pairs that are passed through to the target resource brokers.
        :param str entity_lock: (optional) Indicates if the resource instance is
               locked for further update or delete operations. It does not affect actions
               performed on child resources like aliases, bindings or keys. False by
               default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceInstance` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if target is None:
            raise ValueError('target must be provided')
        if resource_group is None:
            raise ValueError('resource_group must be provided')
        if resource_plan_id is None:
            raise ValueError('resource_plan_id must be provided')
        headers = {
            'Entity-Lock': entity_lock
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_resource_instance')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'target': target,
            'resource_group': resource_group,
            'resource_plan_id': resource_plan_id,
            'tags': tags,
            'allow_cleanup': allow_cleanup,
            'parameters': parameters
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_resource_instance(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a resource instance.

        Retrieve a resource instance by ID.

        :param str id: The short or long ID of the instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceInstance` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_resource_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_resource_instance(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a resource instance.

        Delete a resource instance by ID.

        :param str id: The short or long ID of the instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_resource_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_instance(self,
        id: str,
        *,
        name: str = None,
        parameters: dict = None,
        resource_plan_id: str = None,
        allow_cleanup: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a resource instance.

        Update a resource instance by ID.

        :param str id: The short or long ID of the instance.
        :param str name: (optional) The new name of the instance. Must be 180
               characters or less and cannot include any special characters other than
               `(space) - . _ :`.
        :param dict parameters: (optional) The new configuration options for the
               instance.
        :param str resource_plan_id: (optional) The unique ID of the plan
               associated with the offering. This value is provided by and stored in the
               global catalog.
        :param bool allow_cleanup: (optional) A boolean that dictates if the
               resource instance should be deleted (cleaned up) during the processing of a
               region instance delete call.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceInstance` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_resource_instance')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'parameters': parameters,
            'resource_plan_id': resource_plan_id,
            'allow_cleanup': allow_cleanup
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def lock_resource_instance(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Lock a resource instance.

        Locks a resource instance by ID. A locked instance can not be updated or deleted.
        It does not affect actions performed on child resources like aliases, bindings or
        keys.

        :param str id: The short or long ID of the instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceInstance` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='lock_resource_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances/{0}/lock'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def unlock_resource_instance(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Unlock a resource instance.

        Unlocks a resource instance by ID.

        :param str id: The short or long ID of the instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceInstance` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='unlock_resource_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_instances/{0}/lock'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Resource Keys
    #########################


    def list_resource_keys(self,
        *,
        guid: str = None,
        name: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        limit: str = None,
        updated_from: str = None,
        updated_to: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of all of the resource keys.

        List all resource keys.

        :param str guid: (optional) When you create a new key, a GUID (globally
               unique identifier) is assigned. This is a unique internal GUID managed by
               Resource controller that corresponds to the key.
        :param str name: (optional) The human-readable name of the key.
        :param str resource_group_id: (optional) The short ID of the resource
               group.
        :param str resource_id: (optional) The unique ID of the offering. This
               value is provided by and stored in the global catalog.
        :param str limit: (optional) Limit on how many items should be returned.
        :param str updated_from: (optional) Start date inclusive filter.
        :param str updated_to: (optional) End date inclusive filter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceKeysList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_resource_keys')
        headers.update(sdk_headers)

        params = {
            'guid': guid,
            'name': name,
            'resource_group_id': resource_group_id,
            'resource_id': resource_id,
            'limit': limit,
            'updated_from': updated_from,
            'updated_to': updated_to
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_keys'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_key(self,
        name: str,
        source: str,
        *,
        parameters: 'ResourceKeyPostParameters' = None,
        role: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new resource key.

        Create a new resource key.

        :param str name: The name of the key.
        :param str source: The short or long ID of resource instance or alias.
        :param ResourceKeyPostParameters parameters: (optional) Configuration
               options represented as key-value pairs. Service defined options are passed
               through to the target resource brokers, whereas platform defined options
               are not.
        :param str role: (optional) The role name or it's CRN.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceKey` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if source is None:
            raise ValueError('source must be provided')
        if parameters is not None:
            parameters = convert_model(parameters)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_resource_key')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'source': source,
            'parameters': parameters,
            'role': role
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_keys'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_resource_key(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get resource key by ID.

        Get resource key by ID.

        :param str id: The short or long ID of the key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceKey` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_resource_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_keys/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_resource_key(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a resource key by ID.

        Delete a resource key by ID.

        :param str id: The short or long ID of the key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_resource_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_keys/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_key(self,
        id: str,
        name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a resource key.

        Update a resource key by ID.

        :param str id: The short or long ID of the key.
        :param str name: The new name of the key. Must be 180 characters or less
               and cannot include any special characters other than `(space) - . _ :`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceKey` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_resource_key')
        headers.update(sdk_headers)

        data = {
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_keys/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Resource Bindings
    #########################


    def list_resource_bindings(self,
        *,
        guid: str = None,
        name: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        region_binding_id: str = None,
        limit: str = None,
        updated_from: str = None,
        updated_to: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of all resource bindings.

        Get a list of all resource bindings.

        :param str guid: (optional) The short ID of the binding.
        :param str name: (optional) The human-readable name of the binding.
        :param str resource_group_id: (optional) Short ID of the resource group.
        :param str resource_id: (optional) The unique ID of the offering (service
               name). This value is provided by and stored in the global catalog.
        :param str region_binding_id: (optional) Short ID of the binding in the
               specific targeted environment, e.g. service_binding_id in a given IBM Cloud
               environment.
        :param str limit: (optional) Limit on how many items should be returned.
        :param str updated_from: (optional) Start date inclusive filter.
        :param str updated_to: (optional) End date inclusive filter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceBindingsList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_resource_bindings')
        headers.update(sdk_headers)

        params = {
            'guid': guid,
            'name': name,
            'resource_group_id': resource_group_id,
            'resource_id': resource_id,
            'region_binding_id': region_binding_id,
            'limit': limit,
            'updated_from': updated_from,
            'updated_to': updated_to
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_bindings'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_binding(self,
        source: str,
        target: str,
        *,
        name: str = None,
        parameters: 'ResourceBindingPostParameters' = None,
        role: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new resource binding.

        Create a new resource binding.

        :param str source: The short or long ID of resource alias.
        :param str target: The CRN of application to bind to in a specific
               environment, e.g. Dallas YP, CFEE instance.
        :param str name: (optional) The name of the binding. Must be 180 characters
               or less and cannot include any special characters other than `(space) - . _
               :`.
        :param ResourceBindingPostParameters parameters: (optional) Configuration
               options represented as key-value pairs. Service defined options are passed
               through to the target resource brokers, whereas platform defined options
               are not.
        :param str role: (optional) The role name or it's CRN.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceBinding` object
        """

        if source is None:
            raise ValueError('source must be provided')
        if target is None:
            raise ValueError('target must be provided')
        if parameters is not None:
            parameters = convert_model(parameters)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_resource_binding')
        headers.update(sdk_headers)

        data = {
            'source': source,
            'target': target,
            'name': name,
            'parameters': parameters,
            'role': role
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_bindings'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_resource_binding(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a resource binding.

        Retrieve a resource binding by ID.

        :param str id: The short or long ID of the binding.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceBinding` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_resource_binding')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_bindings/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_resource_binding(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a resource binding.

        Delete a resource binding by ID.

        :param str id: The short or long ID of the binding.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_resource_binding')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_bindings/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_binding(self,
        id: str,
        name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a resource binding.

        Update a resource binding by ID.

        :param str id: The short or long ID of the binding.
        :param str name: The new name of the binding. Must be 180 characters or
               less and cannot include any special characters other than `(space) - . _
               :`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceBinding` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_resource_binding')
        headers.update(sdk_headers)

        data = {
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_bindings/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Resource Aliases
    #########################


    def list_resource_aliases(self,
        *,
        guid: str = None,
        name: str = None,
        resource_instance_id: str = None,
        region_instance_id: str = None,
        resource_id: str = None,
        resource_group_id: str = None,
        limit: str = None,
        updated_from: str = None,
        updated_to: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of all resource aliases.

        Get a list of all resource aliases.

        :param str guid: (optional) Short ID of the alias.
        :param str name: (optional) The human-readable name of the alias.
        :param str resource_instance_id: (optional) Resource instance short ID.
        :param str region_instance_id: (optional) Short ID of the instance in a
               specific targeted environment. For example, `service_instance_id` in a
               given IBM Cloud environment.
        :param str resource_id: (optional) The unique ID of the offering (service
               name). This value is provided by and stored in the global catalog.
        :param str resource_group_id: (optional) Short ID of Resource group.
        :param str limit: (optional) Limit on how many items should be returned.
        :param str updated_from: (optional) Start date inclusive filter.
        :param str updated_to: (optional) End date inclusive filter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceAliasesList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_resource_aliases')
        headers.update(sdk_headers)

        params = {
            'guid': guid,
            'name': name,
            'resource_instance_id': resource_instance_id,
            'region_instance_id': region_instance_id,
            'resource_id': resource_id,
            'resource_group_id': resource_group_id,
            'limit': limit,
            'updated_from': updated_from,
            'updated_to': updated_to
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_aliases'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_alias(self,
        name: str,
        source: str,
        target: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new resource alias.

        Alias a resource instance into a targeted environment's (name)space.

        :param str name: The name of the alias. Must be 180 characters or less and
               cannot include any special characters other than `(space) - . _ :`.
        :param str source: The short or long ID of resource instance.
        :param str target: The CRN of target name(space) in a specific environment,
               e.g. space in Dallas YP, CFEE instance etc.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceAlias` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if source is None:
            raise ValueError('source must be provided')
        if target is None:
            raise ValueError('target must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_resource_alias')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'source': source,
            'target': target
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_aliases'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_resource_alias(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a resource alias.

        Retrieve a resource alias by ID.

        :param str id: The short or long ID of the alias.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceAlias` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_resource_alias')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_aliases/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_resource_alias(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a resource alias.

        Delete a resource alias by ID.

        :param str id: The short or long ID of the alias.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_resource_alias')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_aliases/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_alias(self,
        id: str,
        name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a resource alias.

        Update a resource alias by ID.

        :param str id: The short or long ID of the alias.
        :param str name: The new name of the alias. Must be 180 characters or less
               and cannot include any special characters other than `(space) - . _ :`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceAlias` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_resource_alias')
        headers.update(sdk_headers)

        data = {
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/resource_aliases/{0}'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Resource Reclamations
    #########################


    def list_reclamations(self,
        *,
        account_id: str = None,
        resource_instance_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of all reclamations.

        Get a list of all reclamations.

        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str resource_instance_id: (optional) The short ID of the resource
               instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReclamationsList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_reclamations')
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'resource_instance_id': resource_instance_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/reclamations'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def run_reclamation_action(self,
        id: str,
        action_name: str,
        *,
        request_by: str = None,
        comment: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Perform a reclamation action.

        Reclaim (provisionally delete) a resource so that it can no longer be used, or
        restore a resource so that it's usable again.

        :param str id: The ID associated with the reclamation.
        :param str action_name: The reclamation action name. Specify `reclaim` to
               delete a resource, or `restore` to restore a resource.
        :param str request_by: (optional) The request initiator, if different from
               the request token.
        :param str comment: (optional) A comment to describe the action.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Reclamation` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if action_name is None:
            raise ValueError('action_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='run_reclamation_action')
        headers.update(sdk_headers)

        data = {
            'request_by': request_by,
            'comment': comment
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/reclamations/{0}/actions/{1}'.format(
            *self.encode_path_vars(id, action_name))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class Credentials():
    """
    The credentials for a resource.

    :attr str apikey: (optional) The API key for the credentials.
    :attr str iam_apikey_description: (optional) The optional description of the API
          key.
    :attr str iam_apikey_name: (optional) The name of the API key.
    :attr str iam_role_crn: (optional) The Cloud Resource Name for the role of the
          credentials.
    :attr str iam_serviceid_crn: (optional) The Cloud Resource Name for the service
          ID of the credentials.
    """

    # The set of defined properties for the class
    _properties = frozenset(['apikey', 'iam_apikey_description', 'iam_apikey_name', 'iam_role_crn', 'iam_serviceid_crn'])

    def __init__(self,
                 *,
                 apikey: str = None,
                 iam_apikey_description: str = None,
                 iam_apikey_name: str = None,
                 iam_role_crn: str = None,
                 iam_serviceid_crn: str = None,
                 **kwargs) -> None:
        """
        Initialize a Credentials object.

        :param str apikey: (optional) The API key for the credentials.
        :param str iam_apikey_description: (optional) The optional description of
               the API key.
        :param str iam_apikey_name: (optional) The name of the API key.
        :param str iam_role_crn: (optional) The Cloud Resource Name for the role of
               the credentials.
        :param str iam_serviceid_crn: (optional) The Cloud Resource Name for the
               service ID of the credentials.
        :param **kwargs: (optional) Any additional properties.
        """
        self.apikey = apikey
        self.iam_apikey_description = iam_apikey_description
        self.iam_apikey_name = iam_apikey_name
        self.iam_role_crn = iam_role_crn
        self.iam_serviceid_crn = iam_serviceid_crn
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Credentials':
        """Initialize a Credentials object from a json dictionary."""
        args = {}
        if 'apikey' in _dict:
            args['apikey'] = _dict.get('apikey')
        if 'iam_apikey_description' in _dict:
            args['iam_apikey_description'] = _dict.get('iam_apikey_description')
        if 'iam_apikey_name' in _dict:
            args['iam_apikey_name'] = _dict.get('iam_apikey_name')
        if 'iam_role_crn' in _dict:
            args['iam_role_crn'] = _dict.get('iam_role_crn')
        if 'iam_serviceid_crn' in _dict:
            args['iam_serviceid_crn'] = _dict.get('iam_serviceid_crn')
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Credentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey
        if hasattr(self, 'iam_apikey_description') and self.iam_apikey_description is not None:
            _dict['iam_apikey_description'] = self.iam_apikey_description
        if hasattr(self, 'iam_apikey_name') and self.iam_apikey_name is not None:
            _dict['iam_apikey_name'] = self.iam_apikey_name
        if hasattr(self, 'iam_role_crn') and self.iam_role_crn is not None:
            _dict['iam_role_crn'] = self.iam_role_crn
        if hasattr(self, 'iam_serviceid_crn') and self.iam_serviceid_crn is not None:
            _dict['iam_serviceid_crn'] = self.iam_serviceid_crn
        for _key in [k for k in vars(self).keys() if k not in Credentials._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Credentials object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Credentials') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Credentials') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PlanHistoryItem():
    """
    An element of the plan history of the instance.

    :attr str resource_plan_id: The unique ID of the plan associated with the
          offering. This value is provided by and stored in the global catalog.
    :attr datetime start_date: The date on which the plan was changed.
    """

    def __init__(self,
                 resource_plan_id: str,
                 start_date: datetime) -> None:
        """
        Initialize a PlanHistoryItem object.

        :param str resource_plan_id: The unique ID of the plan associated with the
               offering. This value is provided by and stored in the global catalog.
        :param datetime start_date: The date on which the plan was changed.
        """
        self.resource_plan_id = resource_plan_id
        self.start_date = start_date

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PlanHistoryItem':
        """Initialize a PlanHistoryItem object from a json dictionary."""
        args = {}
        if 'resource_plan_id' in _dict:
            args['resource_plan_id'] = _dict.get('resource_plan_id')
        else:
            raise ValueError('Required property \'resource_plan_id\' not present in PlanHistoryItem JSON')
        if 'start_date' in _dict:
            args['start_date'] = string_to_datetime(_dict.get('start_date'))
        else:
            raise ValueError('Required property \'start_date\' not present in PlanHistoryItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PlanHistoryItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_plan_id') and self.resource_plan_id is not None:
            _dict['resource_plan_id'] = self.resource_plan_id
        if hasattr(self, 'start_date') and self.start_date is not None:
            _dict['start_date'] = datetime_to_string(self.start_date)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PlanHistoryItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PlanHistoryItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PlanHistoryItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Reclamation():
    """
    A reclamation.

    :attr str id: (optional) The ID associated with the reclamation.
    :attr str entity_id: (optional) The short ID of the entity for the reclamation.
    :attr str entity_type_id: (optional) The short ID of the entity type for the
          reclamation.
    :attr str entity_crn: (optional) The full Cloud Resource Name (CRN) associated
          with the binding. For more information about this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
    :attr str resource_instance_id: (optional) The short ID of the resource
          instance.
    :attr str resource_group_id: (optional) The short ID of the resource group.
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr str policy_id: (optional) The short ID of policy for the reclamation.
    :attr str state: (optional) The state of the reclamation.
    :attr str target_time: (optional) The target time that the reclamation retention
          period end.
    :attr dict custom_properties: (optional) The custom properties of the
          reclamation.
    :attr datetime created_at: (optional) The date when the reclamation was created.
    :attr str created_by: (optional) The subject who created the reclamation.
    :attr datetime updated_at: (optional) The date when the reclamation was last
          updated.
    :attr str updated_by: (optional) The subject who updated the reclamation.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 entity_id: str = None,
                 entity_type_id: str = None,
                 entity_crn: str = None,
                 resource_instance_id: str = None,
                 resource_group_id: str = None,
                 account_id: str = None,
                 policy_id: str = None,
                 state: str = None,
                 target_time: str = None,
                 custom_properties: dict = None,
                 created_at: datetime = None,
                 created_by: str = None,
                 updated_at: datetime = None,
                 updated_by: str = None) -> None:
        """
        Initialize a Reclamation object.

        :param str id: (optional) The ID associated with the reclamation.
        :param str entity_id: (optional) The short ID of the entity for the
               reclamation.
        :param str entity_type_id: (optional) The short ID of the entity type for
               the reclamation.
        :param str entity_crn: (optional) The full Cloud Resource Name (CRN)
               associated with the binding. For more information about this format, see
               [Cloud Resource
               Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
        :param str resource_instance_id: (optional) The short ID of the resource
               instance.
        :param str resource_group_id: (optional) The short ID of the resource
               group.
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str policy_id: (optional) The short ID of policy for the
               reclamation.
        :param str state: (optional) The state of the reclamation.
        :param str target_time: (optional) The target time that the reclamation
               retention period end.
        :param dict custom_properties: (optional) The custom properties of the
               reclamation.
        :param datetime created_at: (optional) The date when the reclamation was
               created.
        :param str created_by: (optional) The subject who created the reclamation.
        :param datetime updated_at: (optional) The date when the reclamation was
               last updated.
        :param str updated_by: (optional) The subject who updated the reclamation.
        """
        self.id = id
        self.entity_id = entity_id
        self.entity_type_id = entity_type_id
        self.entity_crn = entity_crn
        self.resource_instance_id = resource_instance_id
        self.resource_group_id = resource_group_id
        self.account_id = account_id
        self.policy_id = policy_id
        self.state = state
        self.target_time = target_time
        self.custom_properties = custom_properties
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Reclamation':
        """Initialize a Reclamation object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'entity_id' in _dict:
            args['entity_id'] = _dict.get('entity_id')
        if 'entity_type_id' in _dict:
            args['entity_type_id'] = _dict.get('entity_type_id')
        if 'entity_crn' in _dict:
            args['entity_crn'] = _dict.get('entity_crn')
        if 'resource_instance_id' in _dict:
            args['resource_instance_id'] = _dict.get('resource_instance_id')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'policy_id' in _dict:
            args['policy_id'] = _dict.get('policy_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'target_time' in _dict:
            args['target_time'] = _dict.get('target_time')
        if 'custom_properties' in _dict:
            args['custom_properties'] = _dict.get('custom_properties')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Reclamation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'entity_id') and self.entity_id is not None:
            _dict['entity_id'] = self.entity_id
        if hasattr(self, 'entity_type_id') and self.entity_type_id is not None:
            _dict['entity_type_id'] = self.entity_type_id
        if hasattr(self, 'entity_crn') and self.entity_crn is not None:
            _dict['entity_crn'] = self.entity_crn
        if hasattr(self, 'resource_instance_id') and self.resource_instance_id is not None:
            _dict['resource_instance_id'] = self.resource_instance_id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'policy_id') and self.policy_id is not None:
            _dict['policy_id'] = self.policy_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'target_time') and self.target_time is not None:
            _dict['target_time'] = self.target_time
        if hasattr(self, 'custom_properties') and self.custom_properties is not None:
            _dict['custom_properties'] = self.custom_properties
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Reclamation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Reclamation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Reclamation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReclamationsList():
    """
    A list of reclamations.

    :attr List[Reclamation] resources: (optional) A list of reclamations.
    """

    def __init__(self,
                 *,
                 resources: List['Reclamation'] = None) -> None:
        """
        Initialize a ReclamationsList object.

        :param List[Reclamation] resources: (optional) A list of reclamations.
        """
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReclamationsList':
        """Initialize a ReclamationsList object from a json dictionary."""
        args = {}
        if 'resources' in _dict:
            args['resources'] = [Reclamation.from_dict(x) for x in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReclamationsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReclamationsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReclamationsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReclamationsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceAlias():
    """
    A resource alias.

    :attr str id: (optional) The ID associated with the alias.
    :attr str guid: (optional) When you create a new alias, a globally unique
          identifier (GUID) is assigned. This GUID is a unique internal indentifier
          managed by the resource controller that corresponds to the alias.
    :attr str crn: (optional) The full Cloud Resource Name (CRN) associated with the
          alias. For more information about this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
    :attr str url: (optional) When you created a new alias, a relative URL path is
          created identifying the location of the alias.
    :attr str name: (optional) The human-readable name of the alias.
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr str resource_group_id: (optional) The short ID of the resource group.
    :attr str resource_group_crn: (optional) The long ID (full CRN) of the resource
          group.
    :attr str target_crn: (optional) The CRN of the target namespace in the specific
          environment.
    :attr str state: (optional) The state of the alias.
    :attr str resource_instance_id: (optional) The short ID of the resource instance
          that is being aliased.
    :attr str region_instance_id: (optional) The short ID of the instance in the
          specific target environment, e.g. `service_instance_id` in a given IBM Cloud
          environment.
    :attr str resource_instance_url: (optional) The relative path to the instance.
    :attr str resource_bindings_url: (optional) The relative path to the resource
          bindings for the alias.
    :attr str resource_keys_url: (optional) The relative path to the resource keys
          for the alias.
    :attr datetime created_at: (optional) The date when the alias was created.
    :attr datetime updated_at: (optional) The date when the alias was last updated.
    :attr datetime deleted_at: (optional) The date when the alias was deleted.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 guid: str = None,
                 crn: str = None,
                 url: str = None,
                 name: str = None,
                 account_id: str = None,
                 resource_group_id: str = None,
                 resource_group_crn: str = None,
                 target_crn: str = None,
                 state: str = None,
                 resource_instance_id: str = None,
                 region_instance_id: str = None,
                 resource_instance_url: str = None,
                 resource_bindings_url: str = None,
                 resource_keys_url: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 deleted_at: datetime = None) -> None:
        """
        Initialize a ResourceAlias object.

        :param str id: (optional) The ID associated with the alias.
        :param str guid: (optional) When you create a new alias, a globally unique
               identifier (GUID) is assigned. This GUID is a unique internal indentifier
               managed by the resource controller that corresponds to the alias.
        :param str crn: (optional) The full Cloud Resource Name (CRN) associated
               with the alias. For more information about this format, see [Cloud Resource
               Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
        :param str url: (optional) When you created a new alias, a relative URL
               path is created identifying the location of the alias.
        :param str name: (optional) The human-readable name of the alias.
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str resource_group_id: (optional) The short ID of the resource
               group.
        :param str resource_group_crn: (optional) The long ID (full CRN) of the
               resource group.
        :param str target_crn: (optional) The CRN of the target namespace in the
               specific environment.
        :param str state: (optional) The state of the alias.
        :param str resource_instance_id: (optional) The short ID of the resource
               instance that is being aliased.
        :param str region_instance_id: (optional) The short ID of the instance in
               the specific target environment, e.g. `service_instance_id` in a given IBM
               Cloud environment.
        :param str resource_instance_url: (optional) The relative path to the
               instance.
        :param str resource_bindings_url: (optional) The relative path to the
               resource bindings for the alias.
        :param str resource_keys_url: (optional) The relative path to the resource
               keys for the alias.
        :param datetime created_at: (optional) The date when the alias was created.
        :param datetime updated_at: (optional) The date when the alias was last
               updated.
        :param datetime deleted_at: (optional) The date when the alias was deleted.
        """
        self.id = id
        self.guid = guid
        self.crn = crn
        self.url = url
        self.name = name
        self.account_id = account_id
        self.resource_group_id = resource_group_id
        self.resource_group_crn = resource_group_crn
        self.target_crn = target_crn
        self.state = state
        self.resource_instance_id = resource_instance_id
        self.region_instance_id = region_instance_id
        self.resource_instance_url = resource_instance_url
        self.resource_bindings_url = resource_bindings_url
        self.resource_keys_url = resource_keys_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceAlias':
        """Initialize a ResourceAlias object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'resource_group_crn' in _dict:
            args['resource_group_crn'] = _dict.get('resource_group_crn')
        if 'target_crn' in _dict:
            args['target_crn'] = _dict.get('target_crn')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'resource_instance_id' in _dict:
            args['resource_instance_id'] = _dict.get('resource_instance_id')
        if 'region_instance_id' in _dict:
            args['region_instance_id'] = _dict.get('region_instance_id')
        if 'resource_instance_url' in _dict:
            args['resource_instance_url'] = _dict.get('resource_instance_url')
        if 'resource_bindings_url' in _dict:
            args['resource_bindings_url'] = _dict.get('resource_bindings_url')
        if 'resource_keys_url' in _dict:
            args['resource_keys_url'] = _dict.get('resource_keys_url')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'deleted_at' in _dict:
            args['deleted_at'] = string_to_datetime(_dict.get('deleted_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceAlias object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_group_crn') and self.resource_group_crn is not None:
            _dict['resource_group_crn'] = self.resource_group_crn
        if hasattr(self, 'target_crn') and self.target_crn is not None:
            _dict['target_crn'] = self.target_crn
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'resource_instance_id') and self.resource_instance_id is not None:
            _dict['resource_instance_id'] = self.resource_instance_id
        if hasattr(self, 'region_instance_id') and self.region_instance_id is not None:
            _dict['region_instance_id'] = self.region_instance_id
        if hasattr(self, 'resource_instance_url') and self.resource_instance_url is not None:
            _dict['resource_instance_url'] = self.resource_instance_url
        if hasattr(self, 'resource_bindings_url') and self.resource_bindings_url is not None:
            _dict['resource_bindings_url'] = self.resource_bindings_url
        if hasattr(self, 'resource_keys_url') and self.resource_keys_url is not None:
            _dict['resource_keys_url'] = self.resource_keys_url
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'deleted_at') and self.deleted_at is not None:
            _dict['deleted_at'] = datetime_to_string(self.deleted_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceAlias object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceAlias') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceAlias') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceAliasesList():
    """
    A list of resource aliases.

    :attr str next_url: The URL for requesting the next page of results.
    :attr List[ResourceAlias] resources: A list of resource aliases.
    :attr int rows_count: The number of resource aliases in `resources`.
    """

    def __init__(self,
                 next_url: str,
                 resources: List['ResourceAlias'],
                 rows_count: int) -> None:
        """
        Initialize a ResourceAliasesList object.

        :param str next_url: The URL for requesting the next page of results.
        :param List[ResourceAlias] resources: A list of resource aliases.
        :param int rows_count: The number of resource aliases in `resources`.
        """
        self.next_url = next_url
        self.resources = resources
        self.rows_count = rows_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceAliasesList':
        """Initialize a ResourceAliasesList object from a json dictionary."""
        args = {}
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        else:
            raise ValueError('Required property \'next_url\' not present in ResourceAliasesList JSON')
        if 'resources' in _dict:
            args['resources'] = [ResourceAlias.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceAliasesList JSON')
        if 'rows_count' in _dict:
            args['rows_count'] = _dict.get('rows_count')
        else:
            raise ValueError('Required property \'rows_count\' not present in ResourceAliasesList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceAliasesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        if hasattr(self, 'rows_count') and self.rows_count is not None:
            _dict['rows_count'] = self.rows_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceAliasesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceAliasesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceAliasesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceBinding():
    """
    A resource binding.

    :attr str id: (optional) The ID associated with the binding.
    :attr str guid: (optional) When you create a new binding, a globally unique
          identifier (GUID) is assigned. This GUID is a unique internal identifier managed
          by the resource controller that corresponds to the binding.
    :attr str crn: (optional) The full Cloud Resource Name (CRN) associated with the
          binding. For more information about this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
    :attr str url: (optional) When you provision a new binding, a relative URL path
          is created identifying the location of the binding.
    :attr str name: (optional) The human-readable name of the binding.
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr str resource_group_id: (optional) The short ID of the resource group.
    :attr str source_crn: (optional) The CRN of resource alias associated to the
          binding.
    :attr str target_crn: (optional) The CRN of target resource, e.g. application,
          in a specific environment.
    :attr str region_binding_id: (optional) The short ID of the binding in specific
          targeted environment, e.g. `service_binding_id` in a given IBM Cloud
          environment.
    :attr str state: (optional) The state of the binding.
    :attr Credentials credentials: (optional) The credentials for the binding.
          Additional key-value pairs are passed through from the resource brokers.  For
          additional details, see the service’s documentation.
    :attr bool iam_compatible: (optional) Specifies whether the binding’s
          credentials support IAM.
    :attr str resource_alias_url: (optional) The relative path to the resource alias
          that this binding is associated with.
    :attr datetime created_at: (optional) The date when the binding was created.
    :attr datetime updated_at: (optional) The date when the binding was last
          updated.
    :attr datetime deleted_at: (optional) The date when the binding was deleted.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 guid: str = None,
                 crn: str = None,
                 url: str = None,
                 name: str = None,
                 account_id: str = None,
                 resource_group_id: str = None,
                 source_crn: str = None,
                 target_crn: str = None,
                 region_binding_id: str = None,
                 state: str = None,
                 credentials: 'Credentials' = None,
                 iam_compatible: bool = None,
                 resource_alias_url: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 deleted_at: datetime = None) -> None:
        """
        Initialize a ResourceBinding object.

        :param str id: (optional) The ID associated with the binding.
        :param str guid: (optional) When you create a new binding, a globally
               unique identifier (GUID) is assigned. This GUID is a unique internal
               identifier managed by the resource controller that corresponds to the
               binding.
        :param str crn: (optional) The full Cloud Resource Name (CRN) associated
               with the binding. For more information about this format, see [Cloud
               Resource Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
        :param str url: (optional) When you provision a new binding, a relative URL
               path is created identifying the location of the binding.
        :param str name: (optional) The human-readable name of the binding.
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str resource_group_id: (optional) The short ID of the resource
               group.
        :param str source_crn: (optional) The CRN of resource alias associated to
               the binding.
        :param str target_crn: (optional) The CRN of target resource, e.g.
               application, in a specific environment.
        :param str region_binding_id: (optional) The short ID of the binding in
               specific targeted environment, e.g. `service_binding_id` in a given IBM
               Cloud environment.
        :param str state: (optional) The state of the binding.
        :param Credentials credentials: (optional) The credentials for the binding.
               Additional key-value pairs are passed through from the resource brokers.
               For additional details, see the service’s documentation.
        :param bool iam_compatible: (optional) Specifies whether the binding’s
               credentials support IAM.
        :param str resource_alias_url: (optional) The relative path to the resource
               alias that this binding is associated with.
        :param datetime created_at: (optional) The date when the binding was
               created.
        :param datetime updated_at: (optional) The date when the binding was last
               updated.
        :param datetime deleted_at: (optional) The date when the binding was
               deleted.
        """
        self.id = id
        self.guid = guid
        self.crn = crn
        self.url = url
        self.name = name
        self.account_id = account_id
        self.resource_group_id = resource_group_id
        self.source_crn = source_crn
        self.target_crn = target_crn
        self.region_binding_id = region_binding_id
        self.state = state
        self.credentials = credentials
        self.iam_compatible = iam_compatible
        self.resource_alias_url = resource_alias_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceBinding':
        """Initialize a ResourceBinding object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'source_crn' in _dict:
            args['source_crn'] = _dict.get('source_crn')
        if 'target_crn' in _dict:
            args['target_crn'] = _dict.get('target_crn')
        if 'region_binding_id' in _dict:
            args['region_binding_id'] = _dict.get('region_binding_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'credentials' in _dict:
            args['credentials'] = Credentials.from_dict(_dict.get('credentials'))
        if 'iam_compatible' in _dict:
            args['iam_compatible'] = _dict.get('iam_compatible')
        if 'resource_alias_url' in _dict:
            args['resource_alias_url'] = _dict.get('resource_alias_url')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'deleted_at' in _dict:
            args['deleted_at'] = string_to_datetime(_dict.get('deleted_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceBinding object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'source_crn') and self.source_crn is not None:
            _dict['source_crn'] = self.source_crn
        if hasattr(self, 'target_crn') and self.target_crn is not None:
            _dict['target_crn'] = self.target_crn
        if hasattr(self, 'region_binding_id') and self.region_binding_id is not None:
            _dict['region_binding_id'] = self.region_binding_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'credentials') and self.credentials is not None:
            _dict['credentials'] = self.credentials.to_dict()
        if hasattr(self, 'iam_compatible') and self.iam_compatible is not None:
            _dict['iam_compatible'] = self.iam_compatible
        if hasattr(self, 'resource_alias_url') and self.resource_alias_url is not None:
            _dict['resource_alias_url'] = self.resource_alias_url
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'deleted_at') and self.deleted_at is not None:
            _dict['deleted_at'] = datetime_to_string(self.deleted_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceBinding object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceBinding') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceBinding') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceBindingPostParameters():
    """
    Configuration options represented as key-value pairs. Service defined options are
    passed through to the target resource brokers, whereas platform defined options are
    not.

    :attr str serviceid_crn: (optional) An optional platform defined option to reuse
          an existing IAM serviceId for the role assignment.
    """

    def __init__(self,
                 *,
                 serviceid_crn: str = None) -> None:
        """
        Initialize a ResourceBindingPostParameters object.

        :param str serviceid_crn: (optional) An optional platform defined option to
               reuse an existing IAM serviceId for the role assignment.
        """
        self.serviceid_crn = serviceid_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceBindingPostParameters':
        """Initialize a ResourceBindingPostParameters object from a json dictionary."""
        args = {}
        if 'serviceid_crn' in _dict:
            args['serviceid_crn'] = _dict.get('serviceid_crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceBindingPostParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'serviceid_crn') and self.serviceid_crn is not None:
            _dict['serviceid_crn'] = self.serviceid_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceBindingPostParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceBindingPostParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceBindingPostParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceBindingsList():
    """
    A list of resource bindings.

    :attr str next_url: The URL for requesting the next page of results.
    :attr List[ResourceBinding] resources: A list of resource bindings.
    :attr int rows_count: The number of resource bindings in `resources`.
    """

    def __init__(self,
                 next_url: str,
                 resources: List['ResourceBinding'],
                 rows_count: int) -> None:
        """
        Initialize a ResourceBindingsList object.

        :param str next_url: The URL for requesting the next page of results.
        :param List[ResourceBinding] resources: A list of resource bindings.
        :param int rows_count: The number of resource bindings in `resources`.
        """
        self.next_url = next_url
        self.resources = resources
        self.rows_count = rows_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceBindingsList':
        """Initialize a ResourceBindingsList object from a json dictionary."""
        args = {}
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        else:
            raise ValueError('Required property \'next_url\' not present in ResourceBindingsList JSON')
        if 'resources' in _dict:
            args['resources'] = [ResourceBinding.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceBindingsList JSON')
        if 'rows_count' in _dict:
            args['rows_count'] = _dict.get('rows_count')
        else:
            raise ValueError('Required property \'rows_count\' not present in ResourceBindingsList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceBindingsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        if hasattr(self, 'rows_count') and self.rows_count is not None:
            _dict['rows_count'] = self.rows_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceBindingsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceBindingsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceBindingsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceInstance():
    """
    A resource instance.

    :attr str id: (optional) The ID associated with the instance.
    :attr str guid: (optional) When you create a new resource, a globally unique
          identifier (GUID) is assigned. This GUID is a unique internal identifier managed
          by the resource controller that corresponds to the instance.
    :attr str crn: (optional) The full Cloud Resource Name (CRN) associated with the
          instance. For more information about this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
    :attr str url: (optional) When you provision a new resource, a relative URL path
          is created identifying the location of the instance.
    :attr str name: (optional) The human-readable name of the instance.
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr str resource_group_id: (optional) The short ID of the resource group.
    :attr str resource_group_crn: (optional) The long ID (full CRN) of the resource
          group.
    :attr str resource_id: (optional) The unique ID of the offering. This value is
          provided by and stored in the global catalog.
    :attr str resource_plan_id: (optional) The unique ID of the plan associated with
          the offering. This value is provided by and stored in the global catalog.
    :attr str target_crn: (optional) The full deployment CRN as defined in the
          global catalog. The Cloud Resource Name (CRN) of the deployment location where
          the instance is provisioned.
    :attr str state: (optional) The current state of the instance. For example, if
          the instance is deleted, it will return removed.
    :attr str type: (optional) The type of the instance, e.g. `service_instance`.
    :attr str sub_type: (optional) The sub-type of instance, e.g. `cfaas`.
    :attr bool allow_cleanup: (optional) A boolean that dictates if the resource
          instance should be deleted (cleaned up) during the processing of a region
          instance delete call.
    :attr bool locked: (optional) A boolean that dictates if the resource instance
          is locked or not.
    :attr dict last_operation: (optional) The status of the last operation requested
          on the instance.
    :attr str dashboard_url: (optional) The resource-broker-provided URL to access
          administrative features of the instance.
    :attr List[PlanHistoryItem] plan_history: (optional) The plan history of the
          instance.
    :attr str resource_aliases_url: (optional) The relative path to the resource
          aliases for the instance.
    :attr str resource_bindings_url: (optional) The relative path to the resource
          bindings for the instance.
    :attr str resource_keys_url: (optional) The relative path to the resource keys
          for the instance.
    :attr datetime created_at: (optional) The date when the instance was created.
    :attr datetime updated_at: (optional) The date when the instance was last
          updated.
    :attr datetime deleted_at: (optional) The date when the instance was deleted.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 guid: str = None,
                 crn: str = None,
                 url: str = None,
                 name: str = None,
                 account_id: str = None,
                 resource_group_id: str = None,
                 resource_group_crn: str = None,
                 resource_id: str = None,
                 resource_plan_id: str = None,
                 target_crn: str = None,
                 state: str = None,
                 type: str = None,
                 sub_type: str = None,
                 allow_cleanup: bool = None,
                 locked: bool = None,
                 last_operation: dict = None,
                 dashboard_url: str = None,
                 plan_history: List['PlanHistoryItem'] = None,
                 resource_aliases_url: str = None,
                 resource_bindings_url: str = None,
                 resource_keys_url: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 deleted_at: datetime = None) -> None:
        """
        Initialize a ResourceInstance object.

        :param str id: (optional) The ID associated with the instance.
        :param str guid: (optional) When you create a new resource, a globally
               unique identifier (GUID) is assigned. This GUID is a unique internal
               identifier managed by the resource controller that corresponds to the
               instance.
        :param str crn: (optional) The full Cloud Resource Name (CRN) associated
               with the instance. For more information about this format, see [Cloud
               Resource Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
        :param str url: (optional) When you provision a new resource, a relative
               URL path is created identifying the location of the instance.
        :param str name: (optional) The human-readable name of the instance.
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str resource_group_id: (optional) The short ID of the resource
               group.
        :param str resource_group_crn: (optional) The long ID (full CRN) of the
               resource group.
        :param str resource_id: (optional) The unique ID of the offering. This
               value is provided by and stored in the global catalog.
        :param str resource_plan_id: (optional) The unique ID of the plan
               associated with the offering. This value is provided by and stored in the
               global catalog.
        :param str target_crn: (optional) The full deployment CRN as defined in the
               global catalog. The Cloud Resource Name (CRN) of the deployment location
               where the instance is provisioned.
        :param str state: (optional) The current state of the instance. For
               example, if the instance is deleted, it will return removed.
        :param str type: (optional) The type of the instance, e.g.
               `service_instance`.
        :param str sub_type: (optional) The sub-type of instance, e.g. `cfaas`.
        :param bool allow_cleanup: (optional) A boolean that dictates if the
               resource instance should be deleted (cleaned up) during the processing of a
               region instance delete call.
        :param bool locked: (optional) A boolean that dictates if the resource
               instance is locked or not.
        :param dict last_operation: (optional) The status of the last operation
               requested on the instance.
        :param str dashboard_url: (optional) The resource-broker-provided URL to
               access administrative features of the instance.
        :param List[PlanHistoryItem] plan_history: (optional) The plan history of
               the instance.
        :param str resource_aliases_url: (optional) The relative path to the
               resource aliases for the instance.
        :param str resource_bindings_url: (optional) The relative path to the
               resource bindings for the instance.
        :param str resource_keys_url: (optional) The relative path to the resource
               keys for the instance.
        :param datetime created_at: (optional) The date when the instance was
               created.
        :param datetime updated_at: (optional) The date when the instance was last
               updated.
        :param datetime deleted_at: (optional) The date when the instance was
               deleted.
        """
        self.id = id
        self.guid = guid
        self.crn = crn
        self.url = url
        self.name = name
        self.account_id = account_id
        self.resource_group_id = resource_group_id
        self.resource_group_crn = resource_group_crn
        self.resource_id = resource_id
        self.resource_plan_id = resource_plan_id
        self.target_crn = target_crn
        self.state = state
        self.type = type
        self.sub_type = sub_type
        self.allow_cleanup = allow_cleanup
        self.locked = locked
        self.last_operation = last_operation
        self.dashboard_url = dashboard_url
        self.plan_history = plan_history
        self.resource_aliases_url = resource_aliases_url
        self.resource_bindings_url = resource_bindings_url
        self.resource_keys_url = resource_keys_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceInstance':
        """Initialize a ResourceInstance object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'resource_group_crn' in _dict:
            args['resource_group_crn'] = _dict.get('resource_group_crn')
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        if 'resource_plan_id' in _dict:
            args['resource_plan_id'] = _dict.get('resource_plan_id')
        if 'target_crn' in _dict:
            args['target_crn'] = _dict.get('target_crn')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'sub_type' in _dict:
            args['sub_type'] = _dict.get('sub_type')
        if 'allow_cleanup' in _dict:
            args['allow_cleanup'] = _dict.get('allow_cleanup')
        if 'locked' in _dict:
            args['locked'] = _dict.get('locked')
        if 'last_operation' in _dict:
            args['last_operation'] = _dict.get('last_operation')
        if 'dashboard_url' in _dict:
            args['dashboard_url'] = _dict.get('dashboard_url')
        if 'plan_history' in _dict:
            args['plan_history'] = [PlanHistoryItem.from_dict(x) for x in _dict.get('plan_history')]
        if 'resource_aliases_url' in _dict:
            args['resource_aliases_url'] = _dict.get('resource_aliases_url')
        if 'resource_bindings_url' in _dict:
            args['resource_bindings_url'] = _dict.get('resource_bindings_url')
        if 'resource_keys_url' in _dict:
            args['resource_keys_url'] = _dict.get('resource_keys_url')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'deleted_at' in _dict:
            args['deleted_at'] = string_to_datetime(_dict.get('deleted_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceInstance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_group_crn') and self.resource_group_crn is not None:
            _dict['resource_group_crn'] = self.resource_group_crn
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'resource_plan_id') and self.resource_plan_id is not None:
            _dict['resource_plan_id'] = self.resource_plan_id
        if hasattr(self, 'target_crn') and self.target_crn is not None:
            _dict['target_crn'] = self.target_crn
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'sub_type') and self.sub_type is not None:
            _dict['sub_type'] = self.sub_type
        if hasattr(self, 'allow_cleanup') and self.allow_cleanup is not None:
            _dict['allow_cleanup'] = self.allow_cleanup
        if hasattr(self, 'locked') and self.locked is not None:
            _dict['locked'] = self.locked
        if hasattr(self, 'last_operation') and self.last_operation is not None:
            _dict['last_operation'] = self.last_operation
        if hasattr(self, 'dashboard_url') and self.dashboard_url is not None:
            _dict['dashboard_url'] = self.dashboard_url
        if hasattr(self, 'plan_history') and self.plan_history is not None:
            _dict['plan_history'] = [x.to_dict() for x in self.plan_history]
        if hasattr(self, 'resource_aliases_url') and self.resource_aliases_url is not None:
            _dict['resource_aliases_url'] = self.resource_aliases_url
        if hasattr(self, 'resource_bindings_url') and self.resource_bindings_url is not None:
            _dict['resource_bindings_url'] = self.resource_bindings_url
        if hasattr(self, 'resource_keys_url') and self.resource_keys_url is not None:
            _dict['resource_keys_url'] = self.resource_keys_url
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'deleted_at') and self.deleted_at is not None:
            _dict['deleted_at'] = datetime_to_string(self.deleted_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceInstance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceInstance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceInstance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceInstancesList():
    """
    A list of resource instances.

    :attr str next_url: The URL for requesting the next page of results.
    :attr List[ResourceInstance] resources: A list of resource instances.
    :attr int rows_count: The number of resource instances in `resources`.
    """

    def __init__(self,
                 next_url: str,
                 resources: List['ResourceInstance'],
                 rows_count: int) -> None:
        """
        Initialize a ResourceInstancesList object.

        :param str next_url: The URL for requesting the next page of results.
        :param List[ResourceInstance] resources: A list of resource instances.
        :param int rows_count: The number of resource instances in `resources`.
        """
        self.next_url = next_url
        self.resources = resources
        self.rows_count = rows_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceInstancesList':
        """Initialize a ResourceInstancesList object from a json dictionary."""
        args = {}
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        else:
            raise ValueError('Required property \'next_url\' not present in ResourceInstancesList JSON')
        if 'resources' in _dict:
            args['resources'] = [ResourceInstance.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceInstancesList JSON')
        if 'rows_count' in _dict:
            args['rows_count'] = _dict.get('rows_count')
        else:
            raise ValueError('Required property \'rows_count\' not present in ResourceInstancesList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceInstancesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        if hasattr(self, 'rows_count') and self.rows_count is not None:
            _dict['rows_count'] = self.rows_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceInstancesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceInstancesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceInstancesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceKey():
    """
    A resource key.

    :attr str id: (optional) The ID associated with the key.
    :attr str guid: (optional) When you create a new key, a globally unique
          identifier (GUID) is assigned. This GUID is a unique internal identifier managed
          by the resource controller that corresponds to the key.
    :attr str crn: (optional) The full Cloud Resource Name (CRN) associated with the
          key. For more information about this format, see [Cloud Resource
          Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
    :attr str url: (optional) When you created a new key, a relative URL path is
          created identifying the location of the key.
    :attr str name: (optional) The human-readable name of the key.
    :attr str account_id: (optional) An alpha-numeric value identifying the account
          ID.
    :attr str resource_group_id: (optional) The short ID of the resource group.
    :attr str source_crn: (optional) The CRN of resource instance or alias
          associated to the key.
    :attr str state: (optional) The state of the key.
    :attr Credentials credentials: (optional) The credentials for the key.
          Additional key-value pairs are passed through from the resource brokers.  Refer
          to service’s documentation for additional details.
    :attr bool iam_compatible: (optional) Specifies whether the key’s credentials
          support IAM.
    :attr str resource_instance_url: (optional) The relative path to the resource.
    :attr datetime created_at: (optional) The date when the key was created.
    :attr datetime updated_at: (optional) The date when the key was last updated.
    :attr datetime deleted_at: (optional) The date when the key was deleted.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 guid: str = None,
                 crn: str = None,
                 url: str = None,
                 name: str = None,
                 account_id: str = None,
                 resource_group_id: str = None,
                 source_crn: str = None,
                 state: str = None,
                 credentials: 'Credentials' = None,
                 iam_compatible: bool = None,
                 resource_instance_url: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 deleted_at: datetime = None) -> None:
        """
        Initialize a ResourceKey object.

        :param str id: (optional) The ID associated with the key.
        :param str guid: (optional) When you create a new key, a globally unique
               identifier (GUID) is assigned. This GUID is a unique internal identifier
               managed by the resource controller that corresponds to the key.
        :param str crn: (optional) The full Cloud Resource Name (CRN) associated
               with the key. For more information about this format, see [Cloud Resource
               Names](https://cloud.ibm.com/docs/overview?topic=overview-crn).
        :param str url: (optional) When you created a new key, a relative URL path
               is created identifying the location of the key.
        :param str name: (optional) The human-readable name of the key.
        :param str account_id: (optional) An alpha-numeric value identifying the
               account ID.
        :param str resource_group_id: (optional) The short ID of the resource
               group.
        :param str source_crn: (optional) The CRN of resource instance or alias
               associated to the key.
        :param str state: (optional) The state of the key.
        :param Credentials credentials: (optional) The credentials for the key.
               Additional key-value pairs are passed through from the resource brokers.
               Refer to service’s documentation for additional details.
        :param bool iam_compatible: (optional) Specifies whether the key’s
               credentials support IAM.
        :param str resource_instance_url: (optional) The relative path to the
               resource.
        :param datetime created_at: (optional) The date when the key was created.
        :param datetime updated_at: (optional) The date when the key was last
               updated.
        :param datetime deleted_at: (optional) The date when the key was deleted.
        """
        self.id = id
        self.guid = guid
        self.crn = crn
        self.url = url
        self.name = name
        self.account_id = account_id
        self.resource_group_id = resource_group_id
        self.source_crn = source_crn
        self.state = state
        self.credentials = credentials
        self.iam_compatible = iam_compatible
        self.resource_instance_url = resource_instance_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceKey':
        """Initialize a ResourceKey object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        if 'source_crn' in _dict:
            args['source_crn'] = _dict.get('source_crn')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'credentials' in _dict:
            args['credentials'] = Credentials.from_dict(_dict.get('credentials'))
        if 'iam_compatible' in _dict:
            args['iam_compatible'] = _dict.get('iam_compatible')
        if 'resource_instance_url' in _dict:
            args['resource_instance_url'] = _dict.get('resource_instance_url')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'deleted_at' in _dict:
            args['deleted_at'] = string_to_datetime(_dict.get('deleted_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceKey object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'source_crn') and self.source_crn is not None:
            _dict['source_crn'] = self.source_crn
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'credentials') and self.credentials is not None:
            _dict['credentials'] = self.credentials.to_dict()
        if hasattr(self, 'iam_compatible') and self.iam_compatible is not None:
            _dict['iam_compatible'] = self.iam_compatible
        if hasattr(self, 'resource_instance_url') and self.resource_instance_url is not None:
            _dict['resource_instance_url'] = self.resource_instance_url
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'deleted_at') and self.deleted_at is not None:
            _dict['deleted_at'] = datetime_to_string(self.deleted_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceKey object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceKey') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceKey') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceKeyPostParameters():
    """
    Configuration options represented as key-value pairs. Service defined options are
    passed through to the target resource brokers, whereas platform defined options are
    not.

    :attr str serviceid_crn: (optional) An optional platform defined option to reuse
          an existing IAM serviceId for the role assignment.
    """

    def __init__(self,
                 *,
                 serviceid_crn: str = None) -> None:
        """
        Initialize a ResourceKeyPostParameters object.

        :param str serviceid_crn: (optional) An optional platform defined option to
               reuse an existing IAM serviceId for the role assignment.
        """
        self.serviceid_crn = serviceid_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceKeyPostParameters':
        """Initialize a ResourceKeyPostParameters object from a json dictionary."""
        args = {}
        if 'serviceid_crn' in _dict:
            args['serviceid_crn'] = _dict.get('serviceid_crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceKeyPostParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'serviceid_crn') and self.serviceid_crn is not None:
            _dict['serviceid_crn'] = self.serviceid_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceKeyPostParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceKeyPostParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceKeyPostParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceKeysList():
    """
    A list of resource keys.

    :attr str next_url: The URL for requesting the next page of results.
    :attr List[ResourceKey] resources: A list of resource keys.
    :attr int rows_count: The number of resource keys in `resources`.
    """

    def __init__(self,
                 next_url: str,
                 resources: List['ResourceKey'],
                 rows_count: int) -> None:
        """
        Initialize a ResourceKeysList object.

        :param str next_url: The URL for requesting the next page of results.
        :param List[ResourceKey] resources: A list of resource keys.
        :param int rows_count: The number of resource keys in `resources`.
        """
        self.next_url = next_url
        self.resources = resources
        self.rows_count = rows_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceKeysList':
        """Initialize a ResourceKeysList object from a json dictionary."""
        args = {}
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        else:
            raise ValueError('Required property \'next_url\' not present in ResourceKeysList JSON')
        if 'resources' in _dict:
            args['resources'] = [ResourceKey.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ResourceKeysList JSON')
        if 'rows_count' in _dict:
            args['rows_count'] = _dict.get('rows_count')
        else:
            raise ValueError('Required property \'rows_count\' not present in ResourceKeysList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceKeysList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        if hasattr(self, 'rows_count') and self.rows_count is not None:
            _dict['rows_count'] = self.rows_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceKeysList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceKeysList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceKeysList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
