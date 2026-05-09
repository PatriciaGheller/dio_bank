from src.app import ma
from src.views.role import RoleSchema
from marshmallow import filds
from src.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        load_instance = True
    
class CreateUserSchema(ma.Schema):
    username = filds.Str(required=True)
    password = filds.Str(required=True)
    role_id = filds.Int(required=True, strict=True)