+++
type = "question"
title = "Console warnings and &quot;Running as root&quot; dangerous"
description = '''When I run Wireshark as root in Backtrack Linux, I see these warnings from the console: root@bt: ~# wireshark (wireshark:4751): GLib-GOBject-WARNING **: invalid cast from `GtkMenuItem&#x27; to `GtkMenu&#x27; (wireshark:4751): Gtk-CRITICAL **: gtk_menu_get_attach_widget: assertion `GTK_IS_MENU (menu)&#x27; failed (...'''
date = "2012-01-07T13:52:00Z"
lastmod = "2012-01-08T00:24:00Z"
weight = 8268
keywords = [ "backtrack-linux", "ubuntu", "root", "troubleshooting", "linux" ]
aliases = [ "/questions/8268" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Console warnings and "Running as root" dangerous](/questions/8268/console-warnings-and-running-as-root-dangerous)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8268-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run Wireshark as <code>root</code> in <a href="http://www.backtrack-linux.org/">Backtrack Linux</a>, I see these warnings from the console:</p><pre><code>[email protected]: ~# wireshark
(wireshark:4751): GLib-GOBject-WARNING **: invalid cast from `GtkMenuItem&#39; to `GtkMenu&#39;
(wireshark:4751): Gtk-CRITICAL **: gtk_menu_get_attach_widget: assertion `GTK_IS_MENU (menu)&#39; failed
(wireshark:4751): Gtk-CRITICAL **: gtk_widget_set_sensitive: assertion `GTK_IS_WIDGET (widget)&#39; failed</code></pre><p><br />
I also see a message box with this warning:</p><pre><code>Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.</code></pre><p><br />
How do I address these warnings? See <a href="http://i41.tinypic.com/25jxfrd.jpg">screenshot</a>.</p></div><div id="question-tags" class="tags-container tags">backtrack-linux ubuntu root troubleshooting linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '12, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/f0fa92719694e28211a97a92123e8e39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SoNiC&#39;s gravatar image" /><p>SoNiC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SoNiC has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '12, 11:44</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-8268" class="comments-container"></div><div id="comment-tools-8268" class="comment-tools"></div><div class="clear"></div><div id="comment-8268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8273"></span>

<div id="answer-container-8273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's no "this problem"; from the title and the screenshot, there appear to be two unrelated problems.</p><p>"Wireshark:5164" doesn't appear anywhere in that screenshot. Some "wireshark:4751" warnings appear; they're probably bugs in Wireshark wherein it's doing something incorrect with the GTK+ GUI toolkit it uses. If this happens with an <em>UNMODIFIED</em> version of Wireshark, report those bugs on <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>; give the full output of "wireshark -v", and an indication of what you were doing with the GUI at the moment tose messages were logged. If it happens with a version you've modified, and you've changed GUI code, make sure it isn't happening only in <em>your</em> version by trying it with an unmodified version; if it only happens in your version, you fix it by making your modified code use GTK+ correctly.</p><p>"Running as user "root" and group "root"" is a statement of fact, as is "This could be dangerous". To get Wireshark not to report that, don't run it as root. If you can't capture traffic when you don't run Wireshark as root, see <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">the CaptureSetup/CapturePrivileges</a> page of the Wireshark Wiki; you appear to be running on some Linux distribution, so check the "GNU/Linux distributions, Wireshark is installed using a package manager" and/or the "Other Linux based systems or other installation methods" sections.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '12, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8273" class="comments-container"></div><div id="comment-tools-8273" class="comment-tools"></div><div class="clear"></div><div id="comment-8273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

