+++
type = "question"
title = "How to clear the gui.window_title option from the command-line?"
description = '''I am running Wireshark 1.6.6 on Windows XP SP3 (32-bit). Previously, a custom window title had been added through the Edit -&amp;gt; Preferences -&amp;gt; Layout -&amp;gt; Custom window title preference. Now I want to be able to start Wireshark from the command-line (or a Windows shortcut) and have that window ...'''
date = "2012-04-12T14:01:00Z"
lastmod = "2012-04-13T22:00:00Z"
weight = 10095
keywords = [ "window_title", "preference", "command-line" ]
aliases = [ "/questions/10095" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to clear the gui.window\_title option from the command-line?](/questions/10095/how-to-clear-the-guiwindow_title-option-from-the-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10095-score" class="post-score" title="current number of votes">0</div><span id="post-10095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark 1.6.6 on Windows XP SP3 (32-bit). Previously, a custom window title had been added through the <code>Edit -&gt; Preferences -&gt; Layout -&gt; Custom window title</code> preference. Now I want to be able to start Wireshark from the command-line (or a Windows shortcut) and have that window title cleared out, but I have been unsuccessful at doing so. I have tried as many combinations of single &amp; double quotations, escaped and not escaped, as I can think of, but to no avail.</p><p>Ultimately my goal is to create an installer that ensures the window title is cleared, so I will need to take what works from the command-line then modify the relevant <code>CreateShortCut</code> entries in the <code>wireshark.nsi</code> file, and from what I've seen, the quotation requirements might be different there as well.</p><p>Some things I've tried that fail:</p><ul><li><strong><code>-o "gui.window_title:"</code></strong> This results in <code>"wireshark: Invalid -o flag "gui.window_title:"</code></li><li><strong><code>-o "gui.window_title:"""</code></strong> Wireshark displays, <code>["]</code></li><li><strong><code>-o "gui.window_title:\"\""</code></strong> Wireshark displays, <code>[""]</code></li><li><strong><code>-o 'gui.window_title:'</code></strong> Wireshark displays the old window title that I'm trying to clear away</li><li><strong><code>-o 'gui.window_title:'''</code></strong> Wireshark displays the old window title that I'm trying to clear away</li><li><strong><code>-o 'gui.window_title:\'\''</code></strong> Wireshark displays the old window title that I'm trying to clear away</li><li><strong><code>-o "gui.window_title:''"</code></strong> Wireshark displays, <code>['']</code></li><li><strong><code>-o "gui.window_title:\'\'"</code></strong> Wireshark displays, <code>[\\'\\']</code></li><li><strong><code>-o 'gui.window_title:""'</code></strong> Wireshark displays the old window title that I'm trying to clear away</li><li><strong><code>-o 'gui.window_title:\"\"'</code></strong> Wireshark displays the old window title that I'm trying to clear away</li><li><strong><code>-o 'gui.window_title: '</code></strong> This results in <code>"wireshark: Invalid -o flag "'gui.window_title:"</code></li><li><strong><code>-o 'gui.window_title: '''</code></strong> This results in <code>"wireshark: Invalid -o flag "'gui.window_title:"</code></li><li><strong><code>-o 'gui.window_title: \'\''</code></strong> This results in <code>"wireshark: Invalid -o flag "'gui.window_title:"</code></li></ul><p>... and several other variants as well, none of which worked either.</p><p>Does anyone have any ideas? Thanks, Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window_title" rel="tag" title="see questions tagged &#39;window_title&#39;">window_title</span> <span class="post-tag tag-link-preference" rel="tag" title="see questions tagged &#39;preference&#39;">preference</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '12, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-10095" class="comments-container"></div><div id="comment-tools-10095" class="comment-tools"></div><div class="clear"></div><div id="comment-10095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10146"></span>

<div id="answer-container-10146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10146-score" class="post-score" title="current number of votes">1</div><span id="post-10146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks to me like Wireshark's only allows you to set a window title, not to clear it. I think your first attempt (<em>-o "gui.window_title:"</em>) should have worked. It seems like Wireshark's error checking is interpreting this as a null/invalid window title and disallowing it. I tried using a single space for the window title, and Wireshark choked on that as well, but it allowed me to use any other single character that I tried. I think this should go on <a href="http://bugzilla.wireshark.org">bugzilla.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-10146" class="comments-container"></div><div id="comment-tools-10146" class="comment-tools"></div><div class="clear"></div><div id="comment-10146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

