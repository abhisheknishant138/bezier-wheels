# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



BOTO_TEMPLATE = """\
[Credentials]

gs_service_key_file = {gcs_service_account_path}

[Boto]

https_validate_certificates = True

[GSUtil]

content_language = en
default_api_version = 2
default_project_id = {google_cloud_project}
"""


def main():
    boto_filename = os.path.abspath(os.environ["BOTO_CONFIG"])
    google_cloud_project = os.environ["GOOGLE_CLOUD_PROJECT"]

    build_dir = os.path.dirname(boto_filename)
    gcs_service_account_path = os.path.join(build_dir, "key.json")
    boto_contents = BOTO_TEMPLATE.format(
        gcs_service_account_path=gcs_service_account_path,
        google_cloud_project=google_cloud_project,
    )
    with open(boto_filename, "w") as file_obj:
        file_obj.write(boto_contents)


if __name__ == "__main__":
    main()
