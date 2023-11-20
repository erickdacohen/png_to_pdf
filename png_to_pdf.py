import os
import sys
import img2pdf


def png_to_pdf(input_path: str, output_path: str) -> int:
    """
    Given a folder path, converts all the images into PDF format
    """
    if len(sys.argv) < 3:
        print("Missing arguments. Please provide input and output paths")
        return 2
    elif len(sys.argv) > 3:
        print("Too many arguments. Please provide an input and output path only")
        return 3
    else:
        # get the files that end with ".png"
        img_files = [file for file in os.listdir(input_path) if file.endswith(".png")]

        # iterate through each image file
        for img_file in img_files:
            # replace the extension with ".pdf" as new output file name
            pdf_file_name = img_file[:-3] + "pdf"

            # convert the file to pdf
            pdf_file_data = img2pdf.convert(input_path + img_file)

            # write to output file path location
            with open(output_path + pdf_file_name, "wb") as f:
                f.write(pdf_file_data)

            print(f"{img_file} converted to {pdf_file_name}.\n")

        print(f"\nOutputs found in {output_path}")
        return 0


if __name__ == "__main__":
    png_to_pdf(input_path=sys.argv[1], output_path=sys.argv[2])
