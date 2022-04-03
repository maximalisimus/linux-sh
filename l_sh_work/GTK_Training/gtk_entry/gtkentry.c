#include <gtk/gtk.h>
#include <stdio.h>
#include <stdlib.h>

#include <langinfo.h>
#ifdef HAVE_LOCALE_H
	#include <locale.h>
#endif

char form[]="entry.glade";
char *selectform;

typedef enum {
	OK_BTN,
	NO_BTN,
	DEFAULT
} btnCliked;

GtkWidget *vbox1;
GtkWidget *vbox2;
GtkWidget *btnbox;
GtkWidget *btncencel;
GtkWidget *btnok;
GtkWidget *entry1;
GtkWidget *label1;

btnCliked clkd = DEFAULT;

//static void on_quit( GtkWidget *widget, gpointer   data );
static void ok_cliked(GtkButton *button, gpointer   user_data);
static void cencel_cliked(GtkButton *button, gpointer   user_data);
static GtkWidget* create_entry_window(void);

/*
static void on_quit( GtkWidget *widget, gpointer   data )
{
	gtk_main_quit();
}
*/

static void ok_cliked(GtkButton *button, gpointer   user_data)
{
	char tmp[250];
	sprintf(tmp, "%s", gtk_entry_get_text(entry1));
	printf("%s",tmp);
	clkd = OK_BTN;
	gtk_main_quit();
}

static void cencel_cliked(GtkButton *button, gpointer   user_data)
{
	clkd = NO_BTN;
	gtk_main_quit();
}

static GtkWidget* create_entry_window(void)
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
		forms = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "FormsEntry"));
		// GTK_WIDGET(gtk_builder_get_object(gtkBuilder, ""));
		vbox1 = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "vbox1"));
		btnbox = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "button_box"));
		btncencel = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "cancel_button"));
		btnok = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "ok_button"));
		
		vbox2 = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "vbox2"));
		label1 = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "label1"));
		entry1 = GTK_WIDGET(gtk_builder_get_object(gtkBuilder, "entry1"));
		
		gtk_builder_connect_signals (gtkBuilder, NULL);	
		
		g_signal_connect(G_OBJECT(forms), "destroy", G_CALLBACK(gtk_main_quit), NULL);
		//g_signal_connect(GTK_BUTTON(forms), "destroy", G_CALLBACK(on_quit), NULL);
		// g_signal_connect(GTK_BUTTON(button), "clicked", G_CALLBACK(welcome), NULL);
		
		g_signal_connect(GTK_BUTTON(btnok), "clicked", G_CALLBACK(ok_cliked), NULL);
		g_signal_connect(GTK_BUTTON(btncencel), "clicked", G_CALLBACK(cencel_cliked), NULL);
		
		//gtk_entry_set_visibility(entry1, FALSE);
		//gtk_entry_set_invisible_char(entry1, '*');
		
		gtk_window_set_title(GTK_WINDOW(forms), "Title");
		//gtk_window_maximize(forms);
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
	
	window = create_entry_window();
	gtk_window_maximize(window);
	gtk_widget_show(window);
	gtk_main();
	
	if (clkd == DEFAULT)
	{
		return 255;
	} else if (clkd == OK_BTN)
	{
		return 0;
	} else 
	{
		return 1;
	}
}
