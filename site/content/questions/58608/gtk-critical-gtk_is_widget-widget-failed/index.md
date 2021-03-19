+++
type = "question"
title = "Gtk-CRITICAL : GTK_IS_WIDGET (widget)&#x27; failed"
description = '''Hi i&#x27;m using wireshark on debian jessie. sometimes while capturing packets, it starts to print this errors and after a lot of prints, wireshark closes suddenly!: (wireshark:7724): Gtk-CRITICAL **: gtk_widget_hide: assertion &#x27;GTK_IS_WIDGET (widget)&#x27; failed  (wireshark:7724): Gtk-CRITICAL **: gtk_widg...'''
date = "2017-01-09T02:27:00Z"
lastmod = "2017-01-09T06:15:00Z"
weight = 58608
keywords = [ "gtk_is_widget", "gtk-critical" ]
aliases = [ "/questions/58608" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Gtk-CRITICAL : GTK\_IS\_WIDGET (widget)' failed](/questions/58608/gtk-critical-gtk_is_widget-widget-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>i'm using wireshark on debian jessie. sometimes while capturing packets, it starts to print this errors and after a lot of prints, wireshark closes suddenly!:</p><pre><code>(wireshark:7724): Gtk-CRITICAL **: gtk_widget_hide: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed

(wireshark:7724): Gtk-CRITICAL **: gtk_widget_get_visible: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed

(wireshark:7724): Gtk-CRITICAL **: gtk_widget_get_visible: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed

(wireshark:7724): Gtk-CRITICAL **: gtk_widget_get_visible: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed

(wireshark:7724): Gtk-CRITICAL **: gtk_window_set_transient_for: assertion &#39;GTK_IS_WINDOW (window)&#39; failed

(wireshark:7724): Gtk-CRITICAL **: gtk_widget_hide: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed

(wireshark:7724): Gtk-CRITICAL **: gtk_widget_hide: assertion &#39;GTK_IS_WIDGET (widget)&#39; failed</code></pre><p>do you can help me?</p><p>my wireshark version is 1.12.1 ,and these packages of gtk are installed: libgtk-3-0(3.14.5-1) - libgtk2.0-0 (2.24.25-3)</p><p>thank you</p></div><div id="question-tags" class="tags-container tags">gtk_is_widget gtk-critical</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '17, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/892dcab27b762c956f68e801f8e6d555?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bita&#39;s gravatar image" /><p>bita<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bita has no accepted answers">0%</span></p></div></div><div id="comments-container-58608" class="comments-container"></div><div id="comment-tools-58608" class="comment-tools"></div><div class="clear"></div><div id="comment-58608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58612"></span>

<div id="answer-container-58612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58612-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the <a href="https://wiki.wireshark.org/Development/LifeCycle">lifecycle page</a> the 1.12 version of Wireshark went end of life last year, so the upstream project won't be making fixes anymore (even though we have a 1.12-lts tree). On the other hand the Debian project, from which this package came, does maintain it's version, through <a href="https://packages.debian.org/jessie/wireshark">their package system</a>. If you report a bug there it will be handled within the right context, and with the right information.</p><p>PS: The Debian Developer is involved in all of this, so it should end up in the right hands.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '17, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58612" class="comments-container"></div><div id="comment-tools-58612" class="comment-tools"></div><div class="clear"></div><div id="comment-58612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

