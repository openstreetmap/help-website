+++
type = "question"
title = "destport and payload"
description = '''What is the commands that allows the extraction of port destination and payload of packet'''
date = "2016-05-11T12:50:00Z"
lastmod = "2016-05-11T13:07:00Z"
weight = 52443
keywords = [ "tshark", "port", "payload" ]
aliases = [ "/questions/52443" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [destport and payload](/questions/52443/destport-and-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52443-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the commands that allows the extraction of port destination and payload of packet</p></div><div id="question-tags" class="tags-container tags">tshark port payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '16, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/279908d3c8338ae7ec02baa9f51a3c1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khadidja%20Khadidja&#39;s gravatar image" /><p>Khadidja Kha...<br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khadidja Khadidja has no accepted answers">0%</span></p></div></div><div id="comments-container-52443" class="comments-container"></div><div id="comment-tools-52443" class="comment-tools"></div><div class="clear"></div><div id="comment-52443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52444"></span>

<div id="answer-container-52444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52444-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried to read <a href="https://www.wireshark.org/docs/man-pages/tshark.html">the tshark documentation page</a>?</p><p>In short, the field names can be used both to compose the display filter (<code>-Y udp.dstport == 1234</code> in tshark parameters) and to indicate fields which should be displayed instead of the default dissection (<code>-T fields -e udp.dstport -e udp.srcport</code>). To find the field names, you can click at the line representing the field in the packet dissection pane, and you'll see the field name in the left bottom corner of the Wireshark window. Or, if you can only use tshark for some reason, have a look at <a href="https://www.wireshark.org/docs/dfref/u/udp.html">the online display filter reference</a>.</p><p>You'll have to elaborate on what exactly you mean by "payload".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '16, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52444" class="comments-container"><span id="52446"></span><div id="comment-52446" class="comment"><div id="post-52446-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot for your response, it is helpful for me payload of packet I mean it the data itself that needs to transfer (usually the user's data).</p></div><div id="comment-52446-info" class="comment-info"><span class="comment-age">(11 May '16, 13:32)</span> Khadidja Kha...</div></div><span id="52447"></span><div id="comment-52447" class="comment"><div id="post-52447-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>by "payload of packet" I mean the data itself that need to be transported</p></blockquote><p>This is exactly the wording I didn't want to see :-)</p><p>The transport (protocol) in most cases doesn't transport just a plain byte stream; a typical payload of a transport protocol is some application protocol, or is at least <em>structured</em> in some way, and Wireshark can dissect these payload types in most (well, at least many) cases. So a single "filterable field" like <code>udp.payload</code> doesn't exist as normally no one needs it. Therefore,</p><ul><li><p>for application protocols which can be dissected (like RTP), you have to use the corresponding filterable field names to access individual fields of these protocols,</p></li><li><p>the part of a packet which cannot be dissected is sometimes accessible as a filterable field named <code>data</code>. This may be the case even for udp if neither the source or destination port, nor analysis of an associated control communication captured, nor any heuristic allows Wireshark (tshark) to determine which dissector to feed the payload to.</p></li></ul><p>What you could do, but would probably find it useless, would be to disable dissection of all protocols, and then enable just ethernet,ip,tcp and udp. That way, Wireshark would be prohibited from dissecting the payload, and anything following the tcp or udp headers would be available as <code>data</code> (and, most likely, totally incomprehensible).</p></div><div id="comment-52447-info" class="comment-info"><span class="comment-age">(11 May '16, 13:54)</span> sindy</div></div><span id="52449"></span><div id="comment-52449" class="comment"><div id="post-52449-score" class="comment-score"></div><div class="comment-text"><p>I am grateful to you for your explanation :) thank you but how I can disable dissection of all protocols, and enable just ethernet,ip,tcp and udp. :)</p></div><div id="comment-52449-info" class="comment-info"><span class="comment-age">(11 May '16, 14:19)</span> Khadidja Kha...</div></div></div><div id="comment-tools-52444" class="comment-tools"></div><div class="clear"></div><div id="comment-52444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

