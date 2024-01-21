from setuptools import setup, find_packages
setup(
    name='ZhipuaiToolKit',
    version='0.1.0',
    author='Helio',
    author_email='helio609.dev@outlook.com',
    description='Zhipuai Toolkit 是一套为增强和扩展 zhipuai 功能而设计的外部工具集合。这些工具旨在提高开发效率，简化常见任务，并提供额外的功能，使 zhipuai 的使用更加直观和强大。',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Helio609/ZhipuaiToolkit',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
    classifiers=[
        # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)