from django.views.generic import DetailView, ListView


from todos.models import List


# Create your views here.
class ListArchiveView(ListView):
    model = List


class ListDetailView(DetailView):
    model = List

    # def get_context_data(self, *args, **kwargs):
    #     """"""
    #     context = super(ListDetailView, self).get_context_data(*args, **kwargs)
    #
    #     context.update({})
    #
    #     return context
