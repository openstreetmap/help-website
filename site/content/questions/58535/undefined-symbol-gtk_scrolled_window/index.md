+++
type = "question"
title = "undefined symbol: gtk_scrolled_window"
description = '''Hi I installed gtk+-3.22.5 from src and then installed wireshark-2.2.3 from src in Debian. but after &#x27;make&#x27; wireshark, when running &quot;./wireshark-gtk&quot; I watched this error and wireshark didn&#x27;t work: &quot;wireshark-2.2.3/.libs/lt-wireshark-gtk: symbol lookup error: /usr/src/wireshark-2.2.3/.libs/lt-wiresh...'''
date = "2017-01-05T03:54:00Z"
lastmod = "2017-01-05T09:41:00Z"
weight = 58535
keywords = [ "gtk", "scrolling", "undefined_symbol" ]
aliases = [ "/questions/58535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [undefined symbol: gtk\_scrolled\_window](/questions/58535/undefined-symbol-gtk_scrolled_window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58535-score" class="post-score" title="current number of votes">0</div><span id="post-58535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I installed gtk+-3.22.5 from src and then installed wireshark-2.2.3 from src in Debian. but after 'make' wireshark, when running "./wireshark-gtk" I watched this error and wireshark didn't work:</p><p>"wireshark-2.2.3/.libs/lt-wireshark-gtk: symbol lookup error: /usr/src/wireshark-2.2.3/.libs/lt-wireshark-gtk: undefined symbol: gtk_scrolled_window_set_overlay_scrolling"</p><p>can you help me to solve this issue? thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtk" rel="tag" title="see questions tagged &#39;gtk&#39;">gtk</span> <span class="post-tag tag-link-scrolling" rel="tag" title="see questions tagged &#39;scrolling&#39;">scrolling</span> <span class="post-tag tag-link-undefined_symbol" rel="tag" title="see questions tagged &#39;undefined_symbol&#39;">undefined_symbol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '17, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/892dcab27b762c956f68e801f8e6d555?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bita&#39;s gravatar image" /><p><span>bita</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bita has no accepted answers">0%</span></p></div></div><div id="comments-container-58535" class="comments-container"></div><div id="comment-tools-58535" class="comment-tools"></div><div class="clear"></div><div id="comment-58535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58539"></span>

<div id="answer-container-58539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58539-score" class="post-score" title="current number of votes">1</div><span id="post-58539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="https://developer.gnome.org/gtk3/unstable/GtkScrolledWindow.html#gtk-scrolled-window-set-overlay-scrolling">documentation</a> says it's there since GTK 3.16, so lets see.</p><p>First of all check that that new GTK library is indeed loaded by Wireshark. Use this command in your build direcory:</p><pre><code>ldd .libs/wireshark-gtk | grep gtk</code></pre><p>It should show the GTK library used:</p><pre><code>libgtk-3.so.0 =&gt; /usr/lib/x86_64-linux-gnu/libgtk-3.so.0 (0x00007f0f0f4ca000)</code></pre><p>If so then confirm the function is there (substitute your shared objects file):</p><pre><code>nm --dynamic  /usr/lib/x86_64-linux-gnu/libgtk-3.so.0 | grep gtk_scrolled_window_set_overlay_scrolling</code></pre><p>If it's there it shows:</p><pre><code>00000000002bbf00 T gtk_scrolled_window_set_overlay_scrolling</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '17, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58539" class="comments-container"></div><div id="comment-tools-58539" class="comment-tools"></div><div class="clear"></div><div id="comment-58539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

