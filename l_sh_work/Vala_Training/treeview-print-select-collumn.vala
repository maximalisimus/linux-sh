/*
	treeview-list.vala - Vala TreeView list example

	Build with:
	valac --pkg gtk+-3.0 --pkg posix treeview-print-select-collumn.vala
	* valac --pkg gtk+-3.0 --pkg posix --disable-warnings treeview-print-select-collumn.vala
	valac --pkg gtk+-3.0 --pkg posix --pkg gee-0.8 treeview-print-select-collumn.vala
*/

//using Gtk;
//using GLib;
//using Gee;

[CCode (has_type_id = false)]
public enum Statuses {
	OK,
	Cencel,
	Default
}

Statuses mystatus = Statuses.Default;

static int main (string[] args) {
	Gtk.init (ref args);
	var app = new App ();
	app.start ();
	Gtk.main ();
	if (mystatus == Statuses.OK) { return 0; }
	else if (mystatus == Statuses.Cencel) { return 1; }
	else { return 255; }
}

public class App: Object {

	Gtk.Window window;
	Gtk.TreeView treeview;
	Gtk.ListStore liststore;
	Gtk.Label msg_label;
	Gtk.ButtonBox btn_box;
	Gtk.Button button;

	struct Person {
		int id;
		string name;
		string city;
		string country;

		public string to_string () {
			return @"$(id), $(name), $(city), $(country)";
		}
	}
	
	Person[] data = {
		Person() {id=1, name="Joe Bloggs", city="London", country="England"},
		Person() {id=2, name="Bill Smith", city="Auckland", country="New Zealand"},
		Person() {id=3, name="Joan Miller", city="Boston", country="USA"}
	};

	construct {
		var builder = new Gtk.Builder();
		try {
			builder.add_from_file("treeview-print-select-collumn.ui");
		}
		catch (Error e) {
			stderr.printf (@"$(e.message)\n");
			Posix.exit(1);
		}
		builder.connect_signals (this);
		this.window = builder.get_object("window") as Gtk.Window;
		this.msg_label = builder.get_object("msg-label") as Gtk.Label;
		this.treeview = builder.get_object ("treeview") as Gtk.TreeView;
		this.btn_box = builder.get_object("btnbox") as Gtk.ButtonBox;
		this.button = builder.get_object("button") as Gtk.Button;
		// Load list data.
		this.liststore = builder.get_object ("liststore") as Gtk.ListStore;
		this.liststore.clear ();
		foreach (Person p in this.data) {
			Gtk.TreeIter iter;
			this.liststore.append (out iter);
			this.liststore.set (iter, 0, p.id, 1, p.name, 2, p.city, 3, p.country);
		}
		// Monitor list double-clicks.
		this.treeview.row_activated.connect (on_row_activated);
		// Monitor list selection changes.
		this.treeview.get_selection().changed.connect (on_selection);
		this.window.destroy.connect (Gtk.main_quit);
		this.button.clicked.connect(on_returned_list);
	}

	public void start () {
		this.window.show_all ();
	}


	private static Person get_selection (Gtk.TreeModel model, Gtk.TreeIter iter) {
		var p = Person();
		model.get (iter, 0, out p.id, 1, out p.name, 2, out p.city, 3, out p.country);
		return p;
	}

	/* List item double-click handler. */
	private void on_row_activated (Gtk.TreeView treeview , Gtk.TreePath path, Gtk.TreeViewColumn column) {
		Gtk.TreeIter iter;
		if (treeview.model.get_iter (out iter, path)) {
			Person p = get_selection (treeview.model, iter);
			this.msg_label.label = @"Double-clicked: $(p)";
		}
	}

	/* List item selection handler. */
	private void on_selection (Gtk.TreeSelection selection) {
		Gtk.TreeModel model;
		Gtk.TreeIter iter;
		if (selection.get_selected (out model, out iter)) {
			Person p = get_selection (model, iter);
			this.msg_label.label = @"Selected: $(p)";
		}
	}
	
	public void on_returned_list () {
		//stdout.printf("Привет, мир!\n");
		stdout.printf("%s\n",this.msg_label.label);
		Gtk.TreeSelection myselect;
		myselect = this.treeview.get_selection();
		Gtk.TreeModel model;
		Gtk.TreeIter iter;
		if (myselect.get_selected (out model, out iter)) {
			Person p = get_selection (model, iter);
			string outtext;
			outtext = @"$(p)";
			stdout.printf("%s\n",outtext);
		}
		mystatus = Statuses.OK;
		Gtk.main_quit();
	}
}
