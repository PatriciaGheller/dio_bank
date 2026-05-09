from src.app import ma
from src.views.role import RoleSchema
from marshmallow import filds

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'role')
    role = ma.Nested('RoleSchema', only=['id', 'name'])
    
class CreateUserSchema(ma.Schema):
    username = filds.Str(required=True)
    password = filds.Str(required=True)
    role_id = filds.Int(required=True, strict=True)