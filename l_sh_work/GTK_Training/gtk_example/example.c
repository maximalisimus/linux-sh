#include <gtk/gtk.h>

int main(int argc, char *argv[])
{
	GtkWidget *window;
	gtk_init(&argc, &argv);
	window = gtk_window_new(GTK_WINDOW_TOPLEVEL); 
	gtk_window_set_title(GTK_WINDOW(window), "Мой тайтл!");
	g_signal_connect(G_OBJECT(window), "destroy", G_CALLBACK(gtk_main_quit), NULL);
	// g_signal_connect(GTK_BUTTON(button), "clicked", G_CALLBACK(welcome), NULL);
	gtk_window_maximize(window);
	gtk_widget_show(window);
	gtk_main();

    return 0;
}
