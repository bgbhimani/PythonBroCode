import PyPDF2

def create_booklet(input_pdf_path, output_pdf_path):
    # Open the input PDF file in binary read mode
    with open(input_pdf_path, 'rb') as input_pdf_file:
        # Read the input PDF using PyPDF2 PdfReader
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        
        # Get the total number of pages in the PDF
        total_pages = len(pdf_reader.pages)

        # Calculate how many pages to add to make the total divisible by 4
        # Booklet requires the number of pages to be a multiple of 4
        pages_to_add = (4 - total_pages % 4) % 4

        # Rearranging pages for booklet format
        # We need to pair the first page with the last, second with second-last, and so on
        # Initialize booklet_order as an empty list to store the order of pages
        booklet_order = []

        # Left starts from the first page (index 0), right starts from the last page
        left = 0
        right = total_pages + pages_to_add - 1  # right includes the blank pages we're going to add

        # We now alternate between the left and right page indices
        # The loop continues until left and right meet or cross
        while left < right:
            booklet_order.append(left)   # Add the current front (left) page
            booklet_order.append(right)  # Add the current back (right) page
            left += 1
            right -= 1

        # Create a PDF writer object to write the new PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through the booklet_order to add pages in the specified order
        for page_index in booklet_order:
            if page_index < total_pages:
                # If the index is within the original number of pages, add the actual page
                pdf_writer.add_page(pdf_reader.pages[page_index])
            else:
                # If the index exceeds the original number of pages, add a blank page
                pdf_writer.add_blank_page()

        # Write the ordered pages to a new output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

# Path to your input PDF file (replace with your actual file path)
input_pdf = r"D:\Blank pages.pdf"

# Path to save the output booklet PDF
output_pdf = r"D:\Booklet_blank_pages.pdf"

# Call the create_booklet function to create the booklet from the input PDF
create_booklet(input_pdf, output_pdf)

print("Booklet created successfully!")