+++
type = "question"
title = "CALL DISSECTOR BASED ON IP:"
description = '''Is it possible to Call my custom Dissector based on 4 different IP addresses?'''
date = "2013-01-14T11:41:00Z"
lastmod = "2013-01-16T20:28:00Z"
weight = 17671
keywords = [ "ip", "dissector" ]
aliases = [ "/questions/17671" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [CALL DISSECTOR BASED ON IP:](/questions/17671/call-dissector-based-on-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17671-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to Call my custom Dissector based on 4 different IP addresses?</p></div><div id="question-tags" class="tags-container tags">ip dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '13, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/1f51b148d3f1f063aa95114ceea3b70f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jballard1979&#39;s gravatar image" /><p>jballard1979<br />
<span class="score" title="20 reputation points">20</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jballard1979 has no accepted answers">0%</span></p></div></div><div id="comments-container-17671" class="comments-container"></div><div id="comment-tools-17671" class="comment-tools"></div><div class="clear"></div><div id="comment-17671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17732"></span>

<div id="answer-container-17732" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17732-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does your protocol run directly atop IP (in which case it <em>should</em> have an IP protocol number assigned to it), or does it run atop a protocol that runs atop IP, such as TCP or UDP? If it runs atop TCP or UDP, you would register your dissector as a heuristic dissector in the "tcp" or "udp" heuristic dissector table, and it would check to see whether:</p><ul><li><p>the packet has at least one byte of data available;</p></li><li><p>the packet's "reported length" (actual length on the wire) is the same as its "captured length" (amount of data that was captured);</p></li></ul><p>and if both are the case, it would look at the first and last bytes and, if the first byte is 0x01 and the last byte is 0x0d, dissect the packet and return TRUE, otherwise return FALSE.</p><p>(Note that this is harder if it runs over TCP, as a packet could be split between two TCP segments, in which case your dissector wouldn't see the first and last bytes.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '13, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '13, 20:28</p></div></div><div id="comments-container-17732" class="comments-container"><span id="17757"></span><div id="comment-17757" class="comment"><div id="post-17757-score" class="comment-score"></div><div class="comment-text"><p>I hard coded all the ports in my handoff registration. I was making it way to difficult. Thanks a ton for you response. :)</p></div><div id="comment-17757-info" class="comment-info"><span class="comment-age">(17 Jan '13, 11:16)</span> jballard1979</div></div></div><div id="comment-tools-17732" class="comment-tools"></div><div class="clear"></div><div id="comment-17732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17682"></span>

<div id="answer-container-17682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17682-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not without some hack to the IP dissector, it sounds wierd that a protocol should be tied to an IP address. You could set up a dissector table in packet-ip.c based on IP(GUINT32) and have your dissector register to it. Are you sure there is no better way to find your dissector based on port or information in the packet from the previous protocol in the stack? If your protocol sits directly on top of IP you should use the protocol byte for your protocol e.g set it to the unique value of your protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-17682" class="comments-container"><span id="17691"></span><div id="comment-17691" class="comment"><div id="post-17691-score" class="comment-score"></div><div class="comment-text"><p>That's a great idea, The data per my custom protocol always begins with a byte value of 01 and ends with 0d. Are there any examples that would show the aforementioned technique?</p></div><div id="comment-17691-info" class="comment-info"><span class="comment-age">(15 Jan '13, 03:36)</span> jballard1979</div></div></div><div id="comment-tools-17682" class="comment-tools"></div><div class="clear"></div><div id="comment-17682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

