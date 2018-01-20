from conans import ConanFile


class CMakeFindBoost(ConanFile):
    name = "cmake-findboost"
    version = "0.2.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Supports CMake's findBoost methode for the bincrafters'Boost packages."
    generators = "cmake"
    exports_sources = "FindBoost.cmake"

    def package(self):
        self.copy("FindBoost.cmake", dst=".", keep_path=False)
