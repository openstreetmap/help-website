+++
type = "question"
title = "What is not last buffer"
description = '''What do it mean (not last buffer) is it something I need to worry about?'''
date = "2014-06-12T18:03:00Z"
lastmod = "2014-06-12T19:42:00Z"
weight = 33755
keywords = [ "buffer", "last" ]
aliases = [ "/questions/33755" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is not last buffer](/questions/33755/what-is-not-last-buffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33755-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What do it mean (not last buffer) is it something I need to worry about?</p></div><div id="question-tags" class="tags-container tags">buffer last</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '14, 18:03</strong></p><img src="https://secure.gravatar.com/avatar/c449d5c3ef6a43d3606e2f19dfa0a2dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BigD&#39;s gravatar image" /><p>BigD<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BigD has no accepted answers">0%</span></p></div></div><div id="comments-container-33755" class="comments-container"></div><div id="comment-tools-33755" class="comment-tools"></div><div class="clear"></div><div id="comment-33755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33757"></span>

<div id="answer-container-33757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33757-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://msdn.microsoft.com/en-us/library/dd304523.aspx">Tabular Data Stream</a> protocol has two layers - the "NETLIB" layer, which carries <a href="http://msdn.microsoft.com/en-us/library/dd305039.aspx">low-layer packets</a>, and the TDS layer, which carries messages that might be contained in one NETLIB packet or that might be reassembled from multiple NETLIB packets.</p><p>"(Not last buffer)" indicates that the packet in question is a NETLIB packet that's part of a TDS message and that is not the <em>last</em> NETLIB packet for that TDS message. Wireshark will both reassemble TCP segments as necessary to make NETLIB packets and reassemble NETLIB packets to make TDS messages, and will dissect both.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 19:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33757" class="comments-container"></div><div id="comment-tools-33757" class="comment-tools"></div><div class="clear"></div><div id="comment-33757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

