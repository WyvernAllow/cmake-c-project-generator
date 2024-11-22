from datetime import datetime
import os
import subprocess

def create_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

project_name = input('Project name: ')
license_name = input('License (zlib, MIT): ')
license_holder = input('License holder: ')
source_dir = input('Source directory: ')

GITIGNORE_CONTENT = (
    '# Visual Studio and VSCode config files\n'
    '.vscode\n'
    '.vs\n'
    '\n'
    '# Clang\n'
    '.clangd/\n'
    '.cache\n'
    '\n'
    '# CMake\n'
    'CMakeLists.txt.user\n'
    'CMakeCache.txt\n'
    'CMakeFiles\n'
    'CMakeScripts\n'
    'Testing\n'
    'Makefile\n'
    'cmake_install.cmake\n'
    'install_manifest.txt\n'
    'compile_commands.json\n'
    'CTestTestfile.cmake\n'
    '_deps\n'
    'CMakeUserPresets.json\n'
    'build/\n'
    'out/\n'
)

INITIAL_SOURCE_FILENAME = 'main.c'
INITIAL_SOURCE_CONTENT = (
    '#include <stdio.h>\n'
    '\n'
    'int main(void) {\n'
    '   printf("Hello, World!\\n");\n'
    '}\n'
)

CMAKE_CONTENT = (
    "cmake_minimum_required(VERSION 3.5)\n"
    f"project({project_name} VERSION 0.1.0 LANGUAGES C)\n"
    "\n"
    "add_executable(${PROJECT_NAME}\n"
    f"  {source_dir}/{INITIAL_SOURCE_FILENAME}\n"
    ")\n"
)

CLANG_FORMAT_CONTENT = (
    '# .clang-format\n'
    'BasedOnStyle: Google\n'
    'IndentWidth: 4\n'
    'TabWidth: 4\n'
    'UseTab: Never\n'
    'ColumnLimit: 80\n'
    'BreakBeforeBraces: Attach\n'
    'AllowShortIfStatementsOnASingleLine: false\n'
    'AllowShortFunctionsOnASingleLine: false\n'
    'SpaceBeforeParens: ControlStatements\n'
    'SpaceAfterCStyleCast: false\n'
    'AlignConsecutiveDeclarations: false\n'
    'AlignConsecutiveAssignments: false\n'
    'AlignTrailingComments: true\n'
    'PointerAlignment: Right\n'
    'DerivePointerAlignment: false\n'
    'IndentCaseLabels: false\n'
    'SpacesInParentheses: false\n'
    'SpacesInSquareBrackets: false\n'
    'SpacesInAngles: false\n'
    'SpaceInEmptyParentheses: false\n'
    'Cpp11BracedListStyle: true\n'
    'SortIncludes: true\n'
    'SeparateDefinitionBlocks: Always\n'
)

current_year = datetime.now().year

LICENSES = {
    'zlib': (
        f'Copyright (c) {current_year} {license_holder}\n'
        '\n'
        'This software is provided \'as-is\', without any express or implied\n'
        'warranty. In no event will the authors be held liable for any damages\n'
        'arising from the use of this software.\n'
        '\n'
        'Permission is granted to anyone to use this software for any purpose,\n'
        'including commercial applications, and to alter it and redistribute it\n'
        'freely, subject to the following restrictions:\n'
        '\n'
        '1. The origin of this software must not be misrepresented; you must not\n'
        '   claim that you wrote the original software. If you use this software\n'
        '   in a product, an acknowledgment in the product documentation would be\n'
        '   appreciated but is not required.\n'
        '2. Altered source versions must be plainly marked as such, and must not be\n'
        '   misrepresented as being the original software.\n'
        '3. This notice may not be removed or altered from any source distribution.\n'
    ),

    'MIT': (
        'MIT License\n'
        '\n'
        f'Copyright (c) {current_year} {license_holder}\n'
        '\n'
        'Permission is hereby granted, free of charge, to any person obtaining a copy\n'
        'of this software and associated documentation files (the "Software"), to deal\n'
        'in the Software without restriction, including without limitation the rights\n'
        'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n'
        'copies of the Software, and to permit persons to whom the Software is\n'
        'furnished to do so, subject to the following conditions:\n'
        '\n'
        'The above copyright notice and this permission notice shall be included in all\n'
        'copies or substantial portions of the Software.\n'
        '\n'
        'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
        'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
        'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n'
        'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n'
        'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
        'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n'
        'SOFTWARE.\n'
    )
}

if LICENSES.get(license_name) is None:
    LICENSE = 'MIT'
    print(f'License named {license_name} does not exist. Using MIT license instead')
else:
    LICENSE = LICENSES[license_name]

os.makedirs(f'{project_name}/{source_dir}')

create_file(f'{project_name}/.gitignore', GITIGNORE_CONTENT)
create_file(f'{project_name}/{source_dir}/{INITIAL_SOURCE_FILENAME}', INITIAL_SOURCE_CONTENT)
create_file(f'{project_name}/CMakeLists.txt', CMAKE_CONTENT)
create_file(f'{project_name}/.clang-format', CLANG_FORMAT_CONTENT)
create_file(f'{project_name}/LICENSE.txt', LICENSE)

os.chdir(project_name)
subprocess.run(['git', 'init'], check=True)
print('Done.')