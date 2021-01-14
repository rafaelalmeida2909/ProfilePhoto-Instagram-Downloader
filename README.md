# Instagram Profile Photo Downloader

A program that gets the instagram profile photos of any users, developed in Python3.

## How to run?

All you need is [Python3](https://www.python.org/downloads/) installed in your machine.
If you already have, just run the file **main.py** in the terminal of your choice.

*Obs:* The downloaded photos are placed in the **ProfilePhothos** folder.

## You can change!

By default, photos are downloaded in .png, but you can change the extension to jpeg.
You just need to change the line 13 in the main.py file.
Example:
`path = path.join(getcwd(), "ProfilePhotos", f"{username}.jpeg")`

## Contributing

1. Fork it (<https://github.com/rafaelalmeida2909/ProfilePhoto-Instagram-Downloader/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
