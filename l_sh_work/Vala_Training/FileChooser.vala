using Gtk;

public class OpenFileDialog : FileChooserDialog {

	private string last_folder;

	public OpenFileDialog () {
		this.title = "Open File";
		this.action = FileChooserAction.OPEN;

		add_button (Stock.CANCEL, ResponseType.CANCEL);
		add_button (Stock.OPEN, ResponseType.ACCEPT);
		set_default_response (ResponseType.ACCEPT);

		if (this.last_folder != null) {
			set_current_folder (this.last_folder);
		}
	}

	public override void response (int type) {
		if (type == ResponseType.ACCEPT) {
			this.last_folder = get_current_folder ();
		}
	}

	public static void main (string[] args) {
		Gtk.init (ref args);

		var ofd = new OpenFileDialog ();

		if (ofd.run () == ResponseType.OK) {
			stdout.printf ("filename = %s\n".printf (ofd.get_filename ()));
		}
	}
}
