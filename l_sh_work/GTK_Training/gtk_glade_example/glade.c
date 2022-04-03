#include <gtk/gtk.h>

char form1[]="forms.glade";
char form2[]="forms2.glade";
char *selectform;

static GtkWidget* create_window(void)
{
	GtkBuilder *gtkBuilder;
	GtkWidget *forms;
	GError* error = NULL;	
	gtkBuilder = gtk_builder_new();
	if (!gtk_builder_add_from_file (gtkBuilder, selectform, &error))
	{
		g_critical ("Ошибка загрузки файла: %s", error->message);
		g_error_free (error);
	} else {
		forms = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "Main"));
		if (!forms)
		{
			g_critical ("Ошибка при получении виджета окна");
		}
		gtk_builder_connect_signals (gtkBuilder, NULL);	
		g_object_unref(G_OBJECT(gtkBuilder));
		
		g_signal_connect(G_OBJECT(forms), "destroy", G_CALLBACK(gtk_main_quit), NULL);
		// // g_signal_connect(GTK_BUTTON(button), "clicked", G_CALLBACK(welcome), NULL);
		gtk_window_set_title(GTK_WINDOW(forms), "Title");
		//gtk_window_maximize(forms);
		return forms;
	}
}

int main(int argc, char *argv[])
{
	GtkWidget *window;
	gtk_init(&argc, &argv);
	/*
	GtkBuilder *gtkBuilder;
	
	gtkBuilder = gtk_builder_new();
	gtk_builder_add_from_file(gtkBuilder, "forms.glade", NULL);
	window = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "Main"));
	if (!window)
	{
		g_critical ("Ошибка при получении виджета окна");
	}
	gtk_builder_connect_signals (gtkBuilder, NULL);	
	g_object_unref(G_OBJECT(gtkBuilder));
	
	g_signal_connect(G_OBJECT(window), "destroy", G_CALLBACK(gtk_main_quit), NULL);
	// // g_signal_connect(GTK_BUTTON(button), "clicked", G_CALLBACK(welcome), NULL);
	gtk_window_set_title(GTK_WINDOW(window), "Title");
	gtk_window_maximize(window);
	*/
	
	selectform = form2;
	//puts(selectform);
	//printf("\n");
	
	window = create_window();
	gtk_window_maximize(window);
	gtk_widget_show(window);
	gtk_main();
	
	return 0;
}
