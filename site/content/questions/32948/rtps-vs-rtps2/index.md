+++
type = "question"
title = "RTPS vs. RTPS2"
description = '''The RTPS dissector does not seem to be fully compliant with the latest RTPS 1.2 version from OMG. In earlier versions of Wireshark there was an RTPS2 dissector which had been updated. The &quot;Display Filter Reference&quot; page lists them both as  rtps: Real-Time Publish-Subscribe Wire Protocol (1.0.0 to 1....'''
date = "2014-05-21T04:51:00Z"
lastmod = "2014-05-21T14:05:00Z"
weight = 32948
keywords = [ "dissector" ]
aliases = [ "/questions/32948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTPS vs. RTPS2](/questions/32948/rtps-vs-rtps2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32948-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The RTPS dissector does not seem to be fully compliant with the latest RTPS 1.2 version from OMG. In earlier versions of Wireshark there was an RTPS2 dissector which had been updated. The "Display Filter Reference" page lists them both as rtps: Real-Time Publish-Subscribe Wire Protocol (1.0.0 to 1.10.7, 152 fields) rtps2: Real-Time Publish-Subscribe Wire Protocol 2.x (1.2.0 to 1.8.14, 47 fields)</p><p>Does this mean that the RTPS2 dissector was abandoned after release 1.8.14 and if so, why was that? There seems to have been some kind of discussion about this back in 2009 (<a href="http://www.wireshark.org/lists/wireshark-dev/200903/msg00029.html">http://www.wireshark.org/lists/wireshark-dev/200903/msg00029.html</a>)</p><p>The RTPS dissector wrongly thinks that there is a length error in the INFO_DST submessage. It expects the octetsToNextHeader to be 8 bytes when it's actually 12 bytes which is according to the RTPS spec and what the RTPS2 dissector did expect.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/bdff67253774ab582a0506e2fa20dfdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bb500cc&#39;s gravatar image" /><p>bb500cc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bb500cc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '14, 04:54</p></div></div><div id="comments-container-32948" class="comments-container"><span id="32991"></span><div id="comment-32991" class="comment"><div id="post-32991-score" class="comment-score"></div><div class="comment-text"><p>I'd suggest opening a bug report attaching a sample trace exhibiting the problem and a reference to the relevant portion of the standard document possibly with a link to the document.</p></div><div id="comment-32991-info" class="comment-info"><span class="comment-age">(22 May '14, 06:37)</span> Anders ♦</div></div></div><div id="comment-tools-32948" class="comment-tools"></div><div class="clear"></div><div id="comment-32948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32961"></span>

<div id="answer-container-32961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32961-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Commit <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=48727">http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=48727</a> incorporates RTPS2 into RTPS as far as I can tell. So whatever packet-rtps2.c supported should still be supportted. whether that includes RTPS 1.2 I don't know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32961" class="comments-container"></div><div id="comment-tools-32961" class="comment-tools"></div><div class="clear"></div><div id="comment-32961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

