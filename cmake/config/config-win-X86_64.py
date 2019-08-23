import subprocess

# be sure to run "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x64 before

subprocess.check_call(["cmake", "..",
                       "-G", "Ninja",
                       "-DCMAKE_CXX_FLAGS=/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING",
                       "-DCMAKE_BUILD_TYPE=Release",
                       "-DCMAKE_CROSSCOMPILING=FALSE",
                       "-DQBDI_PLATFORM=WINDOWS",
                       "-DQBDI_ARCH=X86_64"])