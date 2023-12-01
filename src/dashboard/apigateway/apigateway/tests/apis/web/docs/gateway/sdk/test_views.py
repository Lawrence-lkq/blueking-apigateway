#
# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - API 网关(BlueKing - APIGateway) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.
#


class TestSDKListApi:
    def test_list(self, request_view, fake_sdk):
        resp = request_view(
            method="GET",
            view_name="docs.gateway.sdk.list",
            data={
                "language": fake_sdk.language,
            },
        )
        result = resp.json()

        assert resp.status_code == 200
        assert len(result["data"]["results"]) >= 1
        assert result["data"]["results"][0]["gateway"]
        assert result["data"]["results"][0]["sdk"]
        assert result["data"]["results"][0]["resource_version"]


class TestSDKDocApi:
    def test_retrieve(self, request_view):
        resp = request_view(
            method="GET",
            view_name="docs.gateway.sdk.retrieve_doc",
            data={
                "language": "python",
            },
        )
        result = resp.json()

        assert resp.status_code == 200
        assert result["data"]["content"]
