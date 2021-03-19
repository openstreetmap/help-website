+++
type = "question"
title = "Protocol registration in spite of protocol being disabled"
description = '''Hello. I observed a quite strange behaviour. If I disable dissectors over [Analyze-&amp;gt;Enabled Protocols] panel, they still are registered on their BTP/UDP/TCP... ports in [Internals-&amp;gt;Dissector tables-&amp;gt;Integer tables]. Is it a bug or a feature? :-) Best regards  Ewgenij'''
date = "2013-01-08T06:41:00Z"
lastmod = "2013-01-08T08:51:00Z"
weight = 17563
keywords = [ "register", "disabled", "dissector", "protocol", "registration" ]
aliases = [ "/questions/17563" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Protocol registration in spite of protocol being disabled](/questions/17563/protocol-registration-in-spite-of-protocol-being-disabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17563-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I observed a quite strange behaviour. If I disable dissectors over [Analyze-&gt;Enabled Protocols] panel, they still are registered on their BTP/UDP/TCP... ports in [Internals-&gt;Dissector tables-&gt;Integer tables]. Is it a bug or a feature? :-)</p><p>Best regards</p><p>Ewgenij</p></div><div id="question-tags" class="tags-container tags">register disabled dissector protocol registration</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p>Ewgenijkkg<br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-17563" class="comments-container"></div><div id="comment-tools-17563" class="comment-tools"></div><div class="clear"></div><div id="comment-17563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17571"></span>

<div id="answer-container-17571" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17571-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known bug. There was a <a href="http://www.wireshark.org/lists/wireshark-dev/201209/msg00046.html">discussion</a> about it on the wireshark-dev mailing list last year, but no formal bug report has been opened for it yet. Feel free to <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">open</a> one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '13, 08:52</p></div></div><div id="comments-container-17571" class="comments-container"></div><div id="comment-tools-17571" class="comment-tools"></div><div class="clear"></div><div id="comment-17571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17567"></span>

<div id="answer-container-17567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17567-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A feature ...</p><p>They are registered but disabled. (IOW: a dissector registered on a port but disabled is not called thus allowing another dissector (e.g., a heuristic dissector) to be called).</p><p>The entries shown for disabled protocols should probably have an indication as being disabled.</p><p>Feel free to file an enhancement request at bugs.wireshark.ord :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '13, 08:14</p></div></div><div id="comments-container-17567" class="comments-container"><span id="17569"></span><div id="comment-17569" class="comment"><div id="post-17569-score" class="comment-score"></div><div class="comment-text"><p>The problem is that no other dissector/plugin can register on these ports then! And that should be possible in my opinion. Disabled dissectors should not block anything...</p></div><div id="comment-17569-info" class="comment-info"><span class="comment-age">(08 Jan '13, 08:14)</span> Ewgenijkkg</div></div><span id="17570"></span><div id="comment-17570" class="comment"><div id="post-17570-score" class="comment-score"></div><div class="comment-text"><p>I think a bit of thought and work might be required to do something like this.</p><p>As noted, feel free to file an enhancement request....</p></div><div id="comment-17570-info" class="comment-info"><span class="comment-age">(08 Jan '13, 08:18)</span> Bill Meier ♦♦</div></div><span id="17574"></span><div id="comment-17574" class="comment"><div id="post-17574-score" class="comment-score"></div><div class="comment-text"><p>Done :) Thanks!</p><p>BR Ewgenij</p></div><div id="comment-17574-info" class="comment-info"><span class="comment-age">(08 Jan '13, 09:12)</span> Ewgenijkkg</div></div></div><div id="comment-tools-17567" class="comment-tools"></div><div class="clear"></div><div id="comment-17567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

