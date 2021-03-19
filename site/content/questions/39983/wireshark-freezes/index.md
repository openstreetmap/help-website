+++
type = "question"
title = "Wireshark Freezes"
description = '''I&#x27;m using wireshark on Ubuntu 14.04 LTS and everytime I press Start, wireshark freezes. I have tried &#x27;export LIBOVERLAY_SCROLLBAR=0&#x27; with no result. Errors: OBJECT (object)&#x27; failed (wireshark:3669): Gtk-CRITICAL **: gtk_widget_set_name: assertion &#x27;GTK_IS_WIDGET (widget)&#x27; failed (wireshark:3669): GLi...'''
date = "2015-02-20T09:17:00Z"
lastmod = "2015-02-21T16:47:00Z"
weight = 39983
keywords = [ "ubuntu", "freeze", "error" ]
aliases = [ "/questions/39983" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Freezes](/questions/39983/wireshark-freezes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark on Ubuntu 14.04 LTS and everytime I press Start, wireshark freezes. I have tried 'export LIBOVERLAY_SCROLLBAR=0' with no result.</p><p>Errors:</p><pre><code>OBJECT (object)&#39; failed
(wireshark:3669): Gtk-CRITICAL **: gtk_widget_set_name: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GObject&#39;
(wireshark:3669): GLib-GObject-CRITICAL **: g_object_set_qdata_full: assertion &#39;G_IS_OBJECT (object)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkRange&#39;
(wireshark:3669): Gtk-CRITICAL **: gtk_range_get_adjustment: assertion &#39;GTK_IS_RANGE (range)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkOrientable&#39;
(wireshark:3669): Gtk-CRITICAL **: gtk_orientable_get_orientation: assertion &#39;GTK_IS_ORIENTABLE (orientable)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkScrollbar&#39;
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkWidget&#39;
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GObject&#39;
(wireshark:3669): GLib-GObject-CRITICAL **: g_object_get_qdata: assertion &#39;G_IS_OBJECT (object)&#39; failed
(wireshark:3669): Gtk-CRITICAL **: gtk_widget_set_name: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GObject&#39;
(wireshark:3669): GLib-GObject-CRITICAL **: g_object_set_qdata_full: assertion &#39;G_IS_OBJECT (object)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkRange&#39;
(wireshark:3669): Gtk-CRITICAL **: gtk_range_get_adjustment: assertion &#39;GTK_IS_RANGE (range)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkOrientable&#39;
(wireshark:3669): Gtk-CRITICAL **: gtk_orientable_get_orientation: assertion &#39;GTK_IS_ORIENTABLE (orientable)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkScrollbar&#39;
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkWidget&#39;
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GObject&#39;
(wireshark:3669): GLib-GObject-CRITICAL **: g_object_get_qdata: assertion &#39;G_IS_OBJECT (object)&#39; failed
(wireshark:3669): Gtk-CRITICAL **: gtk_widget_set_name: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GObject&#39;
(wireshark:3669): GLib-GObject-CRITICAL **: g_object_set_qdata_full: assertion &#39;G_IS_OBJECT (object)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkRange&#39;
(wireshark:3669): Gtk-CRITICAL **: gtk_range_get_adjustment: assertion &#39;GTK_IS_RANGE (range)&#39; failed
(wireshark:3669): GLib-GObject-WARNING **: invalid unclassed pointer in cast to &#39;GtkOrientable&#39;
(wireshark:3669): Gtk-CRITICAL **: gtk_orientable_get_orientation: assertion &#39;GTK_IS_ORIENTABLE</code></pre><p>It just repeats.</p></div><div id="question-tags" class="tags-container tags">ubuntu freeze error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '15, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/8714e5bc6674de07480f21186a6a8ce8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnysh&#39;s gravatar image" /><p>sunnysh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnysh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '15, 09:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39983" class="comments-container"></div><div id="comment-tools-39983" class="comment-tools"></div><div class="clear"></div><div id="comment-39983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40011"></span>

<div id="answer-container-40011" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40011-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Solved, I initially installed wireshark from another source which was an older version. Got an official version from wireshark using the ppa given by grahamb.</p><p>Below are solutions to all the problems that I ran into while installing Wireshark.</p><p>1)To install stable wireshark on Debian/Ubuntu (I installed on 14.04):<br />
<code> sudo add-get-repository ppa:wireshark-dev/stable sudo apt-get update. sudo apt-get install wireshark</code><br />
</p><p>2)I first ran into a problem where my interfaces (eth0, wlan0 etc.) where not showing up. In order to get them to show up. If your interfaces are not showing up enter the code below:<br />
</p><p><code>sudo usermod -a -G wireshark $USER sudo reboot</code><br />
</p><p>3)Wireshark freezing when clicking start after selecting an interface. If you type <code>wireshark</code> in your terminal, you would be able to see any errors that might come up which is helpful. I had the errors show up as shown above and were fixed by the code shown below. Make sure you install the stable version because the errors I've listed above had no fix since i was not using an official and stable version:<br />
</p><p><code>export LIBOVERLAY_SCROLLBAR=0</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '15, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/8714e5bc6674de07480f21186a6a8ce8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnysh&#39;s gravatar image" /><p>sunnysh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnysh has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-40011" class="comments-container"><span id="40469"></span><div id="comment-40469" class="comment"><div id="post-40469-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Using only:</p><pre><code>export LIBOVERLAY_SCROLLBAR=0</code></pre><p>solved entirely my problem where the latest build of wireshark-gtk fails entirely and core dumps after a while.</p></div><div id="comment-40469-info" class="comment-info"><span class="comment-age">(11 Mar '15, 04:43)</span> lowdef</div></div></div><div id="comment-tools-40011" class="comment-tools"></div><div class="clear"></div><div id="comment-40011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

