import csv

def generate_html(data):
    # Template HTML dengan Bootstrap dan W3Schools builder
    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{data['Judul'][0]}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {{
                margin: 4%;
            }}
            .container {{
                margin: auto;
                width: 80%;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="text-center">{data['Judul'][0]}</h1>
            <div class="text-center">
                <img src="{data['Logo'][0]}" alt="Logo" class="img-fluid">
            </div>
            <p>{data['Teks'][0]}</p>
            <p class="font-italic">Oleh: {data['Oleh'][0]}</p>
            <p>Numerik: {data['Input Numerik'][0]}</p>
            <p>Input 1: {data['Input 1'][0]}</p>
            <p>Input 2: {data['Input 2'][0]}</p>
            <p>Tahun: {data['Tahun'][0]}</p>
        </div>
    </body>
    </html>
    """

    return template

def builder():
    with open('output.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {key: [] for key in reader.fieldnames}

        for row in reader:
            for key in reader.fieldnames:
                data[key].append(row[key].strip() if row[key] else '')

    with open('output.html', 'w', encoding='utf-8') as html_file:
        html_file.write(generate_html(data))

if __name__ == "__main__":
    builder()
