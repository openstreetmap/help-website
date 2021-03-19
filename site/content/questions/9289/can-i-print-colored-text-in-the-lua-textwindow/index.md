+++
type = "question"
title = "Can I print colored text in the Lua TextWindow?"
description = '''Is it possible to print colored text in the Wireshark Lua TextWindow?'''
date = "2012-03-01T02:29:00Z"
lastmod = "2012-03-01T15:47:00Z"
weight = 9289
keywords = [ "lua" ]
aliases = [ "/questions/9289" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I print colored text in the Lua TextWindow?](/questions/9289/can-i-print-colored-text-in-the-lua-textwindow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to print colored text in the Wireshark Lua <code>TextWindow</code>?</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '12, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/eaba5d948ba0b95759c596eb2c6e7ecb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rijith&#39;s gravatar image" /><p>Rijith<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rijith has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '12, 10:37</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9289" class="comments-container"></div><div id="comment-tools-9289" class="comment-tools"></div><div class="clear"></div><div id="comment-9289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9293"></span>

<div id="answer-container-9293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9293-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No.<br />
The <code>TextWindow</code> does not expose any functionality to perform text formatting, nor does it simulate a terminal that would accept escape sequences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-9293" class="comments-container"></div><div id="comment-tools-9293" class="comment-tools"></div><div class="clear"></div><div id="comment-9293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9297"></span>

<div id="answer-container-9297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9297-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>GTK <a href="http://developer.gnome.org/gtk/2.24/TextWidget.html#id759139">supports</a> colorizing specific text in a <a href="http://developer.gnome.org/gtk/2.24/GtkTextView.html"><code>GtkTextView</code></a> (the actual type you see in Wireshark), but Wireshark Lua does not expose that feature. You have a few options to choose from:</p><ul><li>Submit a feature request at <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">bugs.wireshark.org</a>.</li><li>Use <a href="https://github.com/LuaDist/alien">LuaAlien</a> to access libgtk (either your own copy or the one used by Wireshark) from Lua</li><li>Use <a href="http://wxlua.sourceforge.net/">wxLua</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9297" class="comments-container"></div><div id="comment-tools-9297" class="comment-tools"></div><div class="clear"></div><div id="comment-9297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

