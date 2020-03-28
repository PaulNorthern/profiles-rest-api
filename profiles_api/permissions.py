from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to edit their own profile'''

    def has_object_permission(self, request, view, obj):
        '''Check to get user own profile'''
        # GET-method
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        # GET-method
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
