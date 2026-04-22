from http import HTTPStatus

from dio_bank.src.app import Role,  User, db
from dio_bank.src.controllers import user

def test_get_user_success(client):
    # Given
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()
    
    user = User(username='john-doe', password='test', role_id=role.id)
    db.session.add(user)
    db.session.commit()
    
    # When
    response = client.get(f'/users/{user.id}')
    
    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'id': user.id,
        'username': user.username,
        'role_id': user.role_id,
        'posts': []}
    
def test_get_user_not_found(client):
    # Given
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()
    
    user_id = 1
    
    # When
    response = client.get(f'/users/{user_id}')
    
    # Then
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json == {'error': 'User not found'}
    