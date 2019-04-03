from datetime import datetime
from introflask import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __bind_key__ = 'two'
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

#####################################################################

class Post(db.Model):
    __bind_key__ = 'two'
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

#####################################################################

class Artists(db.Model):
    __tablename__ = 'artists'

    ArtistId = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(120))

    def __repr__(self):
        return f"Artists('{self.Name}')"

#####################################################################

class Album(db.Model):
    __tablename__ = 'albums'

    AlbumId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(160))
    ArtistId = db.Column(db.Integer, db.ForeignKey("artists.ArtistId"))

    def __repr__(self):
        return f"Album('{self.Title}', '{self.ArtistId}')"

#####################################################################

class Tracks(db.Model):

    TrackId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    AlbumId = db.Column(db.Integer, db.ForeignKey("album.AlbumId"))
    MediaTypeId = db.Column(db.Integer, db.ForeignKey("media_type.MediaTypeId"))
    GenreId = db.Column(db.Integer, db.ForeignKey("genres.GenreId"))
    Composer = db.Column(db.String(220))
    Milliseconds = db.Column(db.Integer)
    Bytes = db.Column(db.Integer)
    UnitPrice = db.Column(db.Numeric)

    def __repr__(self):
        return f"Tracks('{self.TrackId}', '{self.AlbumId}', '{self.Name}')"
#
# #####################################################################

class Genres(db.Model):


     GenreId = db.Column(db.Integer, primary_key=True)
     Name = db.Column(db.String(120))

     def __repr__(self):
        return f"Genres('{self.GenreId}', '{self.Name}')"

# #####################################################################

class MediaTypes(db.Model):


     MediaTypeId = db.Column(db.Integer, primary_key=True)
     Name = db.Column(db.String(120))

     def __repr__(self):
        return f"MediaTypes('{self.MediaTypeId}', '{self.Name}')"
#
# #####################################################################
#
class Playlists(db.Model):


     PlaylistId = db.Column(db.Integer, primary_key=True)
     Name = db.Column(db.String(120))
     PlaylistTrack = db.relationship('PlaylistTrack', backref = 'playlists', lazy = 'dynamic')

     def __repr__(self):
        return f"Playlists('{self.PlaylistId}', '{self.Name}')"
#
# #####################################################################
#
class PlaylistTrack(db.Model):


     Playlist_Id = db.Column(db.Integer, db.ForeignKey("playlists.PlaylistId"), primary_key = True)
     Track_Id = db.Column(db.Integer, db.ForeignKey("tracks.TrackId"), primary_key = True)


     def __repr__(self):
        return f"PlaylistTrack('{self.PlaylistId}', '{self.TrackId}')"
#
# #####################################################################

class Invoice_Items(db.Model):

     InvoiceLineId = db.Column(db.Integer, primary_key=True)
     InvoiceId = db.Column(db.Integer, db.ForeignKey("invoices.InvoiceId"))
     TrackId = db.Column(db.Integer, db.ForeignKey("tracks.TrackId"))
     UnitPrice = db.Column(db.Numeric(10,2))
     Quantity = db.Column(db.Integer)

     def __repr__(self):
        return f"Invoice_Items('{self.InvoiceLineId}', '{self.InvoiceId}', '{self.TrackId}')"

# #####################################################################

class Invoices(db.Model):


     InvoiceId = db.Column(db.Integer, primary_key=True, nullable=False)
     CustomerId = db.Column(db.Integer, db.ForeignKey("customers.CustomerId"), nullable=False)
     InvoiceDate = db.Column(db.DateTime, nullable=False)
     BillingAddress = db.Column(db.String(70))
     BillingCity = db.Column(db.String(40))
     BillingState = db.Column(db.String(40))
     BillingCountry = db.Column(db.String(40))
     BillingPostalCode = db.Column(db.String(10))

     def __repr__(self):
         return f"Invoices('{self.InvoiceId}', '{self.CustomerId}')"

# #####################################################################

class Customers(db.Model):


     CustomerId = db.Column(db.Integer, primary_key=True, nullable=False)
     FirstName = db.Column(db.String(40), nullable=False)
     LastName = db.Column(db.String(20), nullable=False)
     Company = db.Column(db.String(80))
     Address = db.Column(db.String(70))
     City = db.Column(db.String(40))
     State = db.Column(db.String(40))
     Country = db.Column(db.String(40))
     PostalCode = db.Column(db.String(10))
     Phone = db.Column(db.String(24))
     Fax = db.Column(db.String(24))
     Email = db.Column(db.String(60), nullable=False)
     SupportRepId = db.Column(db.Integer, db.ForeignKey("employees.SupportRepId"))

     def __repr__(self):
         return f"Customers('{self.CustomerId}', '{self.FirstName}', '{self.LastName}')"

# #####################################################################

class Employees(db.Model):


     EmployeeId = db.Column(db.Integer, primary_key=True, nullable=False)
     FirstName = db.Column(db.String(20), nullable=False)
     LastName = db.Column(db.String(20), nullable=False)
     Title = db.Column(db.String(30))
     ReportsTo = db.Column(db.Integer, db.ForeignKey("employees.ReportsTo"))
     BirthDate = db.Column(db.DateTime)
     HireDate = db.Column(db.DateTime)
     Address = db.Column(db.String(70))
     City = db.Column(db.String(40))
     State = db.Column(db.String(40))
     Country = db.Column(db.String(40))
     PostalCode = db.Column(db.String(10))
     Phone = db.Column(db.String(24))
     Fax = db.Column(db.String(24))
     Email = db.Column(db.String(60))

     def __repr__(self):
         return f"Employees('{self.EmployeeId}', '{self.FirstName}', '{self.LastName}')"


# #####################################################################
