from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer, MoveSerializer, \
    UpdateParentSerializer, MarkSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = []

    @action(detail=False, methods=['post'])
    def move(self, request) -> Response:
        serializer = MoveSerializer(data=request.data)
        if serializer.is_valid():
            to = Todo.objects.get(id=serializer.validated_data['to'])
            node = Todo.objects.get(id=serializer.validated_data['node'])
            pos = serializer.validated_data['pos']

            node.move(to, pos)
            return Response({'status': 200})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get','post'])
    def branch_status(self, request, pk=None) -> Response:
        # example http://localhost:8000/todo/1/branch_status/
        # http://localhost:8000/todo/7/branch_status/

        node = Todo.objects.get(id=pk)
        if request.method == 'GET':
            is_complete = node.is_complete or False

            if is_complete:
                children = node.get_descendants()
                for child in children:
                    print(child.id, child.is_complete)
                    if not child.is_complete:
                        # there is at least one incomplete child. We don't need not look
                        # any further
                        is_complete = False
                        break

            return Response({
                "status": 200, "is_complete": is_complete
            })
        else:
            serializer = MarkSerializer(data=request.data)
            if serializer.is_valid():
                node.is_complete = serializer.validated_data['complete']
                node.save()
                children = node.get_descendants()
                for child in children:
                    child.is_complete = node.is_complete
                    child.save()
                return Response({
                    "status": 200, "is_complete": node.is_complete
                })
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def update_parent(self, request) -> Response:
        serializer = UpdateParentSerializer(data=request.data)
        if serializer.is_valid():
            node = Todo.objects.get(id=serializer.validated_data['node'])

            ancestors = node.get_ancestors()
            for element in ancestors:
                element.is_complete = node.is_complete
                element.save()

            return Response({'status': 200})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)




