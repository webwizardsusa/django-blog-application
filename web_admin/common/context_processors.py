def user_permissions(request):
    has_perm = request.user.has_perm

    return {
        'can_add_tag': has_perm('tag.add_tag'),
        'can_edit_tag': has_perm('tag.change_tag'),
        'can_delete_tag': has_perm('tag.delete_tag'),
        'can_view_tag': has_perm('tag.view_tag'),
        'can_add_category': has_perm('category.add_category'),
        'can_edit_category': has_perm('category.change_category'),
        'can_delete_category': has_perm('category.delete_category'),
        'can_view_category': has_perm('category.view_category'),
        'can_add_post': has_perm('post.add_post'),
        'can_edit_post': has_perm('post.change_post'),
        'can_delete_post': has_perm('post.delete_post'),
        'can_view_post': has_perm('post.view_post'),
        'can_add_group': has_perm('auth.add_group'),
        'can_edit_group': has_perm('auth.change_group'),
        'can_delete_group': has_perm('auth.delete_group'),
        'can_view_group': has_perm('auth.view_group'),
        'can_add_user': has_perm('auth.add_user'),
        'can_edit_user': has_perm('auth.change_user'),
        'can_delete_user': has_perm('auth.delete_user'),
        'can_view_user': has_perm('auth.view_user'),
    }