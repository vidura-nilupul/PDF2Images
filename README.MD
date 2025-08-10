# PDF2Images

A desktop application that converts single or multiple PDF documents into high-quality images. It's a simple, efficient tool designed to handle both individual files and entire folders of PDFs.

## Table of Contents

**1.About the Project**

**2.Screenshots**

**3.Getting Started**

**4.Usage**

**5.Contributing**

**6.License**

## About the Project

This project is a graphical user interface (GUI) application built with Python. Its primary function is to convert PDF pages into images, with the converted images being saved alongside the original PDF files. The application is built using the following key technologies:

**PyMuPDF**: A powerful library used for handling the PDF conversion process.

**ttkbootstrap**: A theme extension for tkinter, which provides a modern, professional look and feel for the application's interface.

## Screenshots

The screenshot below shows the main interface of the application, where you can select a PDF file or a folder containing multiple PDFs for conversion.

https://github.com/vidura-nilupul/PDF2Images/blob/main/assets/Screenshot.png

## Getting Started

To get the application up and running on your local machine, follow these simple steps.

## Prerequisites

You will need to have Python installed on your system. This application requires the following Python libraries, which can be installed using 

    pip.PyMuPDF==1.22.5
    
    ttkbootstrap==1.12.2

## Installation

**1.Clone the repository**

    git clone https://github.com/vidura-nilupul/PDF2Images.git

**2.Navigate to the project directory**

    cd PDF2Images

**3.Install dependencies**

    pip install -r requirements.txt

This command will install the necessary libraries listed in the `requirements.txt` file.

## Usage

To run the application, execute the following command from the project directory:

    python PDF2image.py

The application will launch with a simple GUI where you can:

**Click** a button to select a single PDF file.

**Click** another button to select a folder with multiple PDF files.

After selection, the application will automatically convert the PDFs and save the images with the original file name as a suffix.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.Fork the ProjectCreate your Feature Branch (`git checkout -b feature/AmazingFeature`)

2.Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

3.Push to the Branch (`git push origin feature/AmazingFeature`)

4.Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.md` for more information.