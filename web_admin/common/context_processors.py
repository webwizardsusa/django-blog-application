def user_permissions(request):
    has_perm = request.user.has_perm

    return {
        'can_add_tag': has_perm('tag.add_tag'),
        'can_edit_tag': has_perm('tag.change_tag'),
        'can_delete_tag': has_perm('tag.delete_tag'),
        'can_view_tag': has_perm('tag.view_tag'),
    }