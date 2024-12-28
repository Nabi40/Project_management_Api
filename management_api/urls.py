from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('project-members', ProjectMemberViewSet)
router.register('tasks', TaskViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
