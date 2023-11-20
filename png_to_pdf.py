import os
import sys
import img2pdf


def png_to_pdf(input_path: str, output_path: str, combine_into_one: bool) -> int:
    """
    Converts all png images into PDF format

    ----------
    input_path: str -> directory of images to combine
    output_path: str -> directory for output(s)
    combine_into_one: bool -> If true, combines into one pdf in output path,
                              else individually converts each
    """
    # Check for sys args correct number of arguments
    if len(sys.argv) < 4:
        print(
            "Missing arguments. Please provide input and output paths and whether to combine into one"
        )
        return 2
    elif len(sys.argv) > 4:
        print("Too many arguments")
        return 3
    else:
        # get the files that end with ".png"
        img_files = [
            input_path + file
            for file in os.listdir(input_path)
            if file.endswith(".png")
        ]

        # If combine_into_one make one pdf file
        if combine_into_one:
            # get the pdf data
            pdf_data = img2pdf.convert(img_files)

            # write into one results file
            with open(output_path + "combined_file.pdf", "wb") as f:
                f.write(pdf_data)

            print(
                """
                \n\n
                *******************************************************************
                ** Converted and combined into one pdf file found in output path **
                *******************************************************************
                """
            )

        else:
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
    png_to_pdf(
        input_path=sys.argv[1],
        output_path=sys.argv[2],
        combine_into_one=bool(sys.argv[3]),
    )
