from django.shortcuts import render


def model_blog_query_all():
    blogs = []
    # TODO query the database instead of this
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    lorem_ipsum += "Sed non risus. "
    lorem_ipsum += "Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, "
    lorem_ipsum += "ultricies sed, dolor. Cras elementum ultrices diam. "
    lorem_ipsum += "Maecenas ligula massa, varius a, semper congue, euismod non, mi. "
    lorem_ipsum += "Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, "
    lorem_ipsum += "non fermentum diam nisl sit amet erat. Duis semper. "
    lorem_ipsum += "Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. "
    lorem_ipsum += "Pellentesque congue. Ut in risus volutpat libero pharetra tempor. "
    lorem_ipsum += "Cras vestibulum bibendum augue. Praesent egestas leo in pede. "
    lorem_ipsum += "Praesent blandit odio eu enim. "
    lorem_ipsum += "Pellentesque sed dui ut augue blandit sodales. "
    lorem_ipsum += "Vestibulum ante ipsum primis in faucibus orci luctus "
    lorem_ipsum += "et ultrices posuere cubilia Curae; "
    lorem_ipsum += "Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. "
    lorem_ipsum += "Maecenas adipiscing ante non diam sodales hendrerit."
    blogs.append({"title": "New Post", "date": "JAN 23, 2020", "text": "Hey there!"})
    blogs.append(
        {
            "title": "What's New in Django 3?",
            "date": "JAN 16, 2020",
            "text": lorem_ipsum,
        }
    )
    # End of TODO
    return blogs


def all_blogs(request):
    blogs = model_blog_query_all()
    return render(request, "all_blogs.html", {"blogs": blogs})
