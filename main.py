import qrcode

def main():
    data = input("Enter the text or URL to generate QR code: ").strip()
    if not data:
        print("No input provided. Exiting.")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = "qrcode.png"
    img.save(filename)

    print(f"✅ QR Code generated: {filename}")

if __name__ == "__main__":
    main()
