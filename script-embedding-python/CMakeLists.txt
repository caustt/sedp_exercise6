cmake_minimum_required(VERSION 3.6)
project(sedp_exercise6)

set(CMAKE_CXX_STANDARD 20)
# must set python library version and location
set(PYTHON_VERSION python3.8)
set(PYTHON_LIBRARY_PATH /usr/include/python3.8/)

add_executable(script-embedding-python
    main.cpp
)

target_include_directories(script-embedding-python
        PRIVATE
        ${PYTHON_LIBRARY_PATH}
)

#set_target_properties(script-embedding-python
#    PROPERTIES
#    ${DEFAULT_PROJECT_OPTIONS}
#)

target_link_libraries(script-embedding-python
        ${PYTHON_VERSION}
)
