#!/bin/bash
#
_archload_iso=$(lsblk -o TYPE,MOUNTPOINT | grep -E "loop|rom|arch|airootfs" | grep "airootfs" | wc -l)
_dlgrc_hm_sts=0
_dlgrc_rs_sts=0
_dlgrc_rr_sts=0
# abif-master
_abif_installation=0
# abif-master
_dlgrc_hm_st="$HOME/.dialogrc"
_dlgrc_rt_st="/etc/dialogrc"
_dlgrc_rt_rt="/root/.dialogrc"
_dlgrc_hm_bp="$filesdir/dlg-home.bp"
_dlgrc_rt_st_bp="$filesdir/dlg-rt-st.bp"
_dlg_rt_rt_bp="$filesdir/dlg-rt-rt.bp"
if [[ "$_abif_installation" == "1" ]]; then
    _dlgrc_mp_etc="${MOUNTPOINT}/etc/dialogrc"
    _dlgrc_mp_rt="${MOUNTPOINT}/root/.dialogrc"
    _dlgrc_mp_hm_dr="${MOUNTPOINT}/home/"
fi
#
gen_dlgrc_conf()
{
	echo "#" > "$1"
	echo "# Set aspect-ration" >> "$1"
	echo "aspect = 0" >> "$1"
	echo "" >> "$1"
	echo "# Set separator (for multiple widgets output)" >> "$1"
	echo "separate_widget = \"\"" >> "$1"
	echo "" >> "$1"
	echo "# Set tab-length (for textbox tab-conversion)" >> "$1"
	echo "tab_len = 0" >> "$1"
	echo "" >> "$1"
	echo "# Make tab-traversal for checklist, etc., include the list" >> "$1"
	echo "visit_items = OFF" >> "$1"
	echo "" >> "$1"
	echo "# Shadow dialog boxes? This also turns on color" >> "$1"
	echo "use_shadow = ON" >> "$1"
	echo "" >> "$1"
	echo "# Turn color support ON or OFF" >> "$1"
	echo "use_colors = ON" >> "$1"
	echo "" >> "$1"
	echo "# Screen color" >> "$1"
	echo "screen_color = (GREEN,BLACK,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Shadow color" >> "$1"
	echo "shadow_color = (WHITE,WHITE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Dialog box color" >> "$1"
	echo "dialog_color = (WHITE,BLUE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Dialog box title color" >> "$1"
	echo "title_color = (RED,BLUE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Dialog box border color" >> "$1"
	echo "border_color = (WHITE,BLUE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Active button color" >> "$1"
	echo "button_active_color = (WHITE,BLUE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Inactive button color" >> "$1"
	echo "button_inactive_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Active button key color" >> "$1"
	echo "button_key_active_color = (YELLOW,GREEN,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Inactive button key color" >> "$1"
	echo "button_key_inactive_color = (CYAN,BLUE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Active button label color" >> "$1"
	echo "button_label_active_color = button_key_active_color" >> "$1"
	echo "" >> "$1"
	echo "# Inactive button label color" >> "$1"
	echo "button_label_inactive_color = button_key_inactive_color" >> "$1"
	echo "" >> "$1"
	echo "# Input box color" >> "$1"
	echo "inputbox_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Input box border color" >> "$1"
	echo "inputbox_border_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Search box color" >> "$1"
	echo "searchbox_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Search box title color" >> "$1"
	echo "searchbox_title_color = title_color" >> "$1"
	echo "" >> "$1"
	echo "# Search box border color" >> "$1"
	echo "searchbox_border_color = border_color" >> "$1"
	echo "" >> "$1"
	echo "# File position indicator color" >> "$1"
	echo "position_indicator_color = title_color" >> "$1"
	echo "" >> "$1"
	echo "# Menu box color" >> "$1"
	echo "menubox_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Menu box border color" >> "$1"
	echo "menubox_border_color = border_color" >> "$1"
	echo "" >> "$1"
	echo "# Item color" >> "$1"
	echo "item_color = (WHITE,BLUE,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Selected item color" >> "$1"
	echo "item_selected_color = (WHITE,GREEN,ON)" >> "$1"
	echo "" >> "$1"
	echo "# Tag color" >> "$1"
	echo "tag_color = item_color" >> "$1"
	echo "" >> "$1"
	echo "# Selected tag color" >> "$1"
	echo "tag_selected_color = item_selected_color" >> "$1"
	echo "" >> "$1"
	echo "# Tag key color" >> "$1"
	echo "tag_key_color = item_color" >> "$1"
	echo "" >> "$1"
	echo "# Selected tag key color" >> "$1"
	echo "tag_key_selected_color = item_selected_color" >> "$1"
	echo "" >> "$1"
	echo "# Check box color" >> "$1"
	echo "check_color = item_color" >> "$1"
	echo "" >> "$1"
	echo "# Selected check box color" >> "$1"
	echo "check_selected_color = item_selected_color" >> "$1"
	echo "" >> "$1"
	echo "# Up arrow color" >> "$1"
	echo "uarrow_color = item_color" >> "$1"
	echo "" >> "$1"
	echo "# Down arrow color" >> "$1"
	echo "darrow_color = item_color" >> "$1"
	echo "" >> "$1"
	echo "# Item help-text color" >> "$1"
	echo "itemhelp_color = (WHITE,BLACK,OFF)" >> "$1"
	echo "" >> "$1"
	echo "# Active form text color" >> "$1"
	echo "form_active_text_color = button_active_color" >> "$1"
	echo "" >> "$1"
	echo "# Form text color" >> "$1"
	echo "form_text_color = item_color" >> "$1"
	echo "" >> "$1"
	echo "# Readonly form item color" >> "$1"
	echo "form_item_readonly_color = item_selected_color" >> "$1"
	echo "" >> "$1"
	echo "# Dialog box gauge color" >> "$1"
	echo "gauge_color = title_color" >> "$1"
	echo "" >> "$1"
	echo "# Dialog box border2 color" >> "$1"
	echo "border2_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Input box border2 color" >> "$1"
	echo "inputbox_border2_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Search box border2 color" >> "$1"
	echo "searchbox_border2_color = dialog_color" >> "$1"
	echo "" >> "$1"
	echo "# Menu box border2 color" >> "$1"
	echo "menubox_border2_color = dialog_color" >> "$1"
}
us_dlgrc_conf()
{
	# backup and gen-gen
	[ -e "$_dlgrc_hm_st" ] && cp -f "$_dlgrc_hm_st" "$_dlgrc_hm_bp" && rm -rf "$_dlgrc_hm_st"
	wait
	[ -e "$_dlgrc_hm_st" ] && _dlgrc_hm_sts=1 && gen_dlgrc_conf "$_dlgrc_hm_st" || gen_dlgrc_conf "$_dlgrc_hm_st"
	wait
	[ -e "$_dlgrc_rt_st" ] && cp -f "$_dlgrc_rt_st" "$_dlgrc_rt_st_bp" && rm -rf "$_dlgrc_rt_st"
	wait
	[ -e "$_dlgrc_rt_st" ] && _dlgrc_rs_sts=1 && gen_dlgrc_conf "$_dlgrc_rt_st" || gen_dlgrc_conf "$_dlgrc_rt_st"
	wait
	[ -e "$_dlgrc_rt_rt" ] && cp -f "$_dlgrc_rt_rt" "$_dlg_rt_rt_bp" && rm -rf "$_dlgrc_rt_rt"
	wait
	[ -e "$_dlgrc_rt_rt" ] && _dlgrc_rr_sts=1 && gen_dlgrc_conf "$_dlgrc_rt_rt" || gen_dlgrc_conf "$_dlgrc_rt_rt"
	wait
	# backup and gen-gen
}
un_us_dlgrc_conf()
{
	# un us dlgrc conf
	[[ "$_dlgrc_hm_sts" == "0" ]] && rm -rf "$_dlgrc_hm_st"
	wait
	[[ "$_dlgrc_rs_sts" == "0" ]] && rm -rf "$_dlgrc_rt_st"
	wait
	[[ "$_dlgrc_rr_sts" == "0" ]] && rm -rf "$_dlgrc_rt_rt"
	wait
	[[ "$_dlgrc_hm_sts" == "1" ]] && rm -rf "$_dlgrc_hm_st" && cp -f "$_dlgrc_hm_bp" "$_dlgrc_hm_st"
	wait
	[[ "$_dlgrc_rs_sts" == "1" ]] && rm -rf "$_dlgrc_rt_st" && cp -f "$_dlgrc_rt_st_bp" "$_dlgrc_rt_st"
	wait
	[[ "$_dlgrc_rr_sts" == "1" ]] && rm -rf "$_dlgrc_rt_rt" && cp -f "$_dlg_rt_rt_bp" "$_dlgrc_rt_rt"
	wait
    if [[ "$_abif_installation" == "1" ]]; then
        rm -rf "$_dlgrc_mp_etc"
        rm -rf "$_dlgrc_mp_rt"
        find "$_dlgrc_mp_hm_dr" -type f -iname ".dialogrc" -exec rm -rf {} \;
        if [[ "$_dlgrc_hm_sts" == "1" ]]; then
            _list_of_users=$(ls ${MOUNTPOINT}/home/ | sed "s/lost+found//")
            for k in ${_list_of_users[*]}; do
                cp -f "$_dlgrc_hm_bp" "${MOUNTPOINT}/home/$k/.dialogrc"
                wait
            done
            unset _list_of_users
        fi
        wait
        [[ "$_dlgrc_rs_sts" == "1" ]] && cp -f "$_dlgrc_rt_st_bp" "$_dlgrc_mp_etc"
        wait
        [[ "$_dlgrc_rr_sts" == "1" ]] && cp -f "$_dlg_rt_rt_bp" "$_dlgrc_mp_rt"
        wait
    fi
    wait
    [ -e "$_dlgrc_hm_bp" ] && rm -rf "$_dlgrc_hm_bp"
	wait
	[ -e "$_dlgrc_rt_st_bp" ] && rm -rf "$_dlgrc_rt_st_bp"
	wait
	[ -e "$_dlg_rt_rt_bp" ] && rm -rf "$_dlg_rt_rt_bp"
	wait
    # un us dlgrc conf
}

