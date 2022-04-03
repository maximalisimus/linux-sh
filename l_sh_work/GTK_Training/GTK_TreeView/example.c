#include <gtk/gtk.h>
#include <stdio.h>
#include <stdlib.h>

#include <langinfo.h>
#ifdef HAVE_LOCALE_H
	#include <locale.h>
#endif

char form[]="treeview.glade";
char *selectform;

static GtkWidget* create_treeview_window(void);
/*
static void ok_clicked(GtkButton *button, gpointer   user_data);
static void cencel_clicked(GtkButton *button, gpointer   user_data);
//static void on_quit( GtkWidget *widget, gpointer   data );

typedef enum {
	OK_CLICK,
	CANCEL_CLICK,
	NO_CLICK
} ExitCode;

ExitCode exit_code = NO_CLICK;

static void on_quit( GtkWidget *widget, gpointer   data )
{
	gtk_main_quit();
}


static void ok_clicked(GtkButton *button, gpointer   user_data)
{	
	exit_code = OK_CLICK;
	gtk_main_quit();
}

static void cencel_clicked(GtkButton *button, gpointer   user_data)
{
	exit_code = CANCEL_CLICK;
	gtk_main_quit();
}
*/

static GtkWidget* create_treeview_window(void)
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
		forms = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "TreeWindow"));
		// GTK_WIDGET(gtk_builder_get_object(gtkBuilder, ""));
		
		gtk_builder_connect_signals (gtkBuilder, NULL);	
		
		g_signal_connect(G_OBJECT(forms), "destroy", G_CALLBACK(gtk_main_quit), NULL);
		//g_signal_connect(GTK_BUTTON(forms), "destroy", G_CALLBACK(on_quit), NULL);
		// g_signal_connect(GTK_BUTTON(button), "clicked", G_CALLBACK(welcome), NULL);
		
		gtk_window_set_title(GTK_WINDOW(forms), "Title");
		g_object_unref(G_OBJECT(gtkBuilder));
		return forms;
	}
}

int main(int argc, char *argv[])
{
	#ifdef HAVE_LOCALE_H
		setlocale (LC_ALL, "");
	#endif
	GtkWidget *window;
	gtk_init(&argc, &argv);

	selectform = form;
	
	window = create_treeview_window();
	gtk_window_maximize(window);
	gtk_widget_show(window);
	gtk_main();
	/*
	if (exit_code == NO_CLICK)
	{
		return 255;
	} else if (exit_code == OK_CLICK)
	{
		return 0;
	} else 
	{
		return 1;
	}
	*/
	return 0;
}
