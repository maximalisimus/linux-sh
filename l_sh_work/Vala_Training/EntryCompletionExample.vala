public class Application : Gtk.Window {

	public Application () {
			// Prepare Gtk.Window:
			this.title = "My Gtk.EntryCompletion";
			this.window_position = Gtk.WindowPosition.CENTER;
			this.destroy.connect (Gtk.main_quit);
			this.set_default_size (350, 70);

			// The Entry:
			Gtk.Entry entry = new Gtk.Entry ();
			this.add (entry);

			// The EntryCompletion:
			Gtk.EntryCompletion completion = new Gtk.EntryCompletion ();
			entry.set_completion (completion);

			// Create, fill & register a ListStore:
			Gtk.ListStore list_store = new Gtk.ListStore (2, typeof (string), typeof (string));
			completion.set_model (list_store);
			completion.set_text_column (0);

			var cell = new Gtk.CellRendererText ();
			completion.pack_start(cell, false);
			completion.add_attribute(cell, "text", 1);

			Gtk.TreeIter iter;

			list_store.append (out iter);
			list_store.set (iter, 0, "Burgenland", 1, "Austria");
			list_store.append (out iter);
			list_store.set (iter, 0, "Berlin", 1, "Germany");
			list_store.append (out iter);
			list_store.set (iter, 0, "Lower Austria", 1, "Austria");
			list_store.append (out iter);
			list_store.set (iter, 0, "Upper Austria", 1, "Austria");
			list_store.append (out iter);
			list_store.set (iter, 0, "Salzburg", 1, "Austria");
			list_store.append (out iter);
			list_store.set (iter, 0, "Styria", 1, "Austria");
			list_store.append (out iter);
			list_store.set (iter, 0, "Tehran", 1, "Iran");
			list_store.append (out iter);
			list_store.set (iter, 0, "Vorarlberg", 1, "Austria");
			list_store.append (out iter);
			list_store.set (iter, 0, "Vienna", 1, "Austria");
	}

	public static int main (string[] args) {
			Gtk.init (ref args);

			Application app = new Application ();
			app.show_all ();
			Gtk.main ();
			return 0;
	}
}
