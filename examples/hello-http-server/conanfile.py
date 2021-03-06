from conans import ConanFile, CMake, tools


class HelloHttpServerConanFile(ConanFile):
    build_requires = "cmake/3.17.3"
    requires = "uwebsockets/18.3.0", "nlohmann_json/3.9.1"
    settings = "arch", "build_type", "compiler"
    generators = "cmake"
    build_folder = "build"
        
    def build(self):
        self.build_folder = "build"
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

