from conans import ConanFile, CMake, tools


class FindConanBoost(ConanFile):
    name = "FindConanBoost"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description here>"
    generators = "cmake"
    exports_sources = "FindBoost.cmake"

    def package(self):
        self.copy("FindBoost.cmake", dst=".", keep_path=False)
