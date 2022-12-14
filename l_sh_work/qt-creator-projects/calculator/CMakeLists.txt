cmake_minimum_required(VERSION 3.2)
project(calculator VERSION 1.1 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED on)
set(CC "gcc")
set(CXX "g++")
set(CMAKE_GENERATOR "Unix Makefiles")
set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(QT_USE_QTGUI TRUE)
set(QT_USE_QTXML TRUE)

find_package(Qt5Widgets REQUIRED)
find_package(Qt5 COMPONENTS Gui REQUIRED)
find_package(Qt5 COMPONENTS Core REQUIRED)

if(${CMAKE_SYSTEM_NAME} STREQUAL Windows)
	set(CMAKE_BUILD_TYPE Release)
	# set(CMAKE_BUILD_TYPE Debug)
	set(CMAKE_CONFIGURATION_TYPES "Release" CACHE STRING "" FORCE)
	# set(CMAKE_CONFIGURATION_TYPES "Debug" CACHE STRING "" FORCE)
	# set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall -o0 -g -mwindows")
	set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall -o2 -s -DNDEBUG -mwindows")
else()
	set(CMAKE_BUILD_TYPE Release)
	# set(CMAKE_BUILD_TYPE Debug)
	set(CMAKE_CONFIGURATION_TYPES "Release" CACHE STRING "" FORCE)
	# set(CMAKE_CONFIGURATION_TYPES "Debug" CACHE STRING "" FORCE)
	# set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall -o0 -g")
	set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall -o2 -s -DNDEBUG")
endif()

set(SOURCES main.cpp mywindow.cpp)
qt5_add_resources(SOURCES res.qrc)

add_executable(calculator ${SOURCES})

qt5_use_modules(calculator Widgets Gui Core)
