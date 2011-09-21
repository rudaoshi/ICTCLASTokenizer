cmake_minimum_required(VERSION 2.8)

project(pyICTCLASCore)

include_directories(${CMAKE_SOURCE_DIR}/ictclas/Source)

set(srcfiles 
	ictclas/Source/ContextStat.cpp
	ictclas/Source/Dictionary.cpp
	ictclas/Source/DynamicArray.cpp
	ictclas/Source/NShortPath.cpp
	ictclas/Source/Queue.cpp
	ictclas/Source/Result.cpp
	ictclas/Source/SegGraph.cpp
	ictclas/Source/Segment.cpp
	ictclas/Source/Span.cpp
	ictclas/Source/UnknowWord.cpp
	ictclas/Source/Utility.cpp
	pyictclas.cpp
)


IF(NOT CMAKE_BUILD_TYPE)
  #SET(CMAKE_BUILD_TYPE "DEBUG")
  SET(CMAKE_BUILD_TYPE "RELEASE")
  #SET(CMAKE_BUILD_TYPE "RELWITHDEBINFO")
  #SET(CMAKE_BUILD_TYPE "MINSIZEREL")
ENDIF()

FIND_PACKAGE(Boost 1.47.0)

IF(NOT Boost_FOUND)
  MESSAGE(FATAL_ERROR "Unable to find correct Boost version. Did you set BOOST_ROOT?")
ENDIF()

SET(Boost_USE_STATIC_LIBS OFF)
SET(Boost_USE_MULTITHREADED ON)
SET(Boost_USE_STATIC_RUNTIME OFF)
FIND_PACKAGE(Boost 1.47.0 COMPONENTS python)

find_package(PythonLibs REQUIRED)
include_directories()

INCLUDE_DIRECTORIES(${CMAKE_SOURCE_DIR}/ictclas/Source/ ${PYTHON_INCLUDE_DIRS} "${Boost_INCLUDE_DIRS}")

ADD_LIBRARY(pyICTCLASCore SHARED ${srcfiles})
TARGET_LINK_LIBRARIES(pyICTCLASCore ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} )


IF(CMAKE_COMPILER_IS_GNUCXX)
  ADD_DEFINITIONS("-Wall")
ELSE()
  MESSAGE(FATAL_ERROR "CMakeLists.txt has not been tested/written for your compiler.")
ENDIF()




