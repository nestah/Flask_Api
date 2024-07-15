# import modules
from flask import Flask
from flask_restful import Api, Resource , reqparse, fields, marshal_with , abort
from flask_sqlalchemy import SQLAlchemy

# create flask app
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# create some models
class videoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"video(name={self.name}, views={self.views}, likes={self.likes})"

# db.create_all()  # delete or comment the db.create_all() after running this script for the first time to avoid overiding db  

# create argument parsers
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video required", required=True)
video_put_args.add_argument("views", type=str, help="views of the video", required=True)
video_put_args.add_argument("likes", type=str, help="likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="name of video required")
video_update_args.add_argument("views", type=str, help="views of the video")
video_update_args.add_argument("likes", type=str, help="likes of the video")
      
# create resource fields
resource_fields = {
    'id': fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer,
}
# Function for video resources         
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = videoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="could not find video with that id...")
        return result
    @marshal_with(resource_fields)
    def put(self,video_id):
        
        args = video_put_args.parse_args()
        result = videoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video id taken...")
        video = videoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    # update videoModel
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result= videoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video does not exist, can not update...")
        if args['name']:
            result.name=args['name']
        if args['views']:
            result.views=args['views'] 
        if args['likes']:
            result.likes=args['likes']       
        db.session.commit()   
        return result 
    # delete video
    def delete(self, video_id):
        result = videoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video does not exist, can not delete...")
        db.session.delete(result)
        db.session.commit()  
        return '', 204  

# resource to handle getting all videos

class videoList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        results = videoModel.query.all()
        return results
    
api.add_resource(Video, "/video/<int:video_id>")    
api.add_resource(videoList, "/videos")
     

# initialize and start flask app
if __name__ == "__main__":
    app.run(debug=True) # only run with debug=True in development environment
