+++
type = "question"
title = "why cant ./configure find gtk on my armhf system"
description = '''i installed it /usr/include/gtk-3.0/ /usr/include/gtk-2.0/ seen something where configure is looking in /opt for it ? configure: error: Neither Qt nor GTK+ 2.12.0 or later are available, so Wireshark can&#x27;t be compiled ./configure --without-qt cant use qt because of an error with qreal = float tossin...'''
date = "2015-05-04T16:35:00Z"
lastmod = "2015-05-04T19:58:00Z"
weight = 42069
keywords = [ "gtk+", "qt", "configuring", "error" ]
aliases = [ "/questions/42069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why cant ./configure find gtk on my armhf system](/questions/42069/why-cant-configure-find-gtk-on-my-armhf-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i installed it /usr/include/gtk-3.0/ /usr/include/gtk-2.0/ seen something where configure is looking in /opt for it ? configure: error: Neither Qt nor GTK+ 2.12.0 or later are available, so Wireshark can't be compiled ./configure --without-qt cant use qt because of an error with qreal = float tossing an error no matching function for call to 'qBound(double, qreal&amp;, double)'</p><p>this is a pain lol</p><p>more information</p><pre><code>[email protected]:/usr/lib/pkgconfig# pkg-config --list-all | grep gtk
avahi-ui-gtk3                       avahi-ui - Avahi Multicast DNS Responder (Common GTK3 UI support)
libcanberra-gtk3                    libcanberra-gtk3 - Gtk3 Event Sound API
gtk+-3.0                            GTK+ - GTK+ Graphical UI Library
gtk+-unix-print-2.0                 GTK+ - GTK+ Unix print support
javascriptcoregtk-3.0               JavaScriptCoreGTK+ - GTK+ version of the JavaScriptCore engine
webkitgtk-3.0                       WebKit - Web content engine for GTK+
gtk+-x11-2.0                        GTK+ - GTK+ Graphical UI Library (x11 target)
indicate-gtk3-0.7                   libindicate-gtk3 - Helpers for libindicate that require GTK+ dependencies.
gtk+-unix-print-3.0                 GTK+ - GTK+ Unix print support
dbusmenu-gtk3-0.4                   libdbusmenu-gtk3 - libdbusmenu-gtk3.
gtk+-x11-3.0                        GTK+ - GTK+ Graphical UI Library
gtk+-2.0                            GTK+ - GTK+ Graphical UI Library (x11 target)</code></pre><p>i see gtk+-3.0 there but wireshark dont see it ?</p></div><div id="question-tags" class="tags-container tags">gtk+ qt configuring error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '15, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/1c81f290beb1043f82e0d6354f5013eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wulfman&#39;s gravatar image" /><p>Wulfman<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wulfman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 May '15, 19:56</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42069" class="comments-container"></div><div id="comment-tools-42069" class="comment-tools"></div><div class="clear"></div><div id="comment-42069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42072"></span>

<div id="answer-container-42072" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42072-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You probably need to install <em>development</em> packages for GTK+ 2.x or 3.x, whichever one you want to use - it will probably have a name with "gtk+" and "dev" or "devel" in it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '15, 19:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-42072" class="comments-container"></div><div id="comment-tools-42072" class="comment-tools"></div><div class="clear"></div><div id="comment-42072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

