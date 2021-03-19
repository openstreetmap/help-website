+++
type = "question"
title = "Wireshark 2.3 build missing wireshark-gtk.exe"
description = '''i was building the wireskark-2.3 after the build i was not able to find wireskark-gtk.exe in the run folder, there was only wireshark.exe present. Where can i find the wireskark-gtk.exe ? else should i do any addition on build? Advance thanks for you response!'''
date = "2017-04-20T23:02:00Z"
lastmod = "2017-04-21T02:06:00Z"
weight = 60938
keywords = [ "gtk", "wireshark-2.3" ]
aliases = [ "/questions/60938" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 2.3 build missing wireshark-gtk.exe](/questions/60938/wireshark-23-build-missing-wireshark-gtkexe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60938-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i was building the wireskark-2.3 after the build i was not able to find wireskark-gtk.exe in the run folder, there was only wireshark.exe present.</p><p>Where can i find the wireskark-gtk.exe ? else should i do any addition on build?</p><p>Advance thanks for you response!</p></div><div id="question-tags" class="tags-container tags">gtk wireshark-2.3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '17, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p>DhanuShalz<br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Apr '17, 02:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60938" class="comments-container"></div><div id="comment-tools-60938" class="comment-tools"></div><div class="clear"></div><div id="comment-60938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60941"></span>

<div id="answer-container-60941" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60941-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably you're building on Windows, in which case you missed the announcement that Windows is dropping the GTK based builds and the GTK build is no longer produced by default.</p><p>To enable the GTK build (which may or may not work as it's now unmaintained for Windows) add <code>-DBUILD_wireshark_gtk=on</code> to your CMake generation command.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '17, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60941" class="comments-container"><span id="61156"></span><div id="comment-61156" class="comment"><div id="post-61156-score" class="comment-score"></div><div class="comment-text"><p>works for me</p></div><div id="comment-61156-info" class="comment-info"><span class="comment-age">(02 May '17, 06:18)</span> a6mishra</div></div></div><div id="comment-tools-60941" class="comment-tools"></div><div class="clear"></div><div id="comment-60941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

