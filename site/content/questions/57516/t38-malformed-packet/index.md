+++
type = "question"
title = "T38 Malformed Packet"
description = '''Hi  I have been doing a wireshark traces as were are having an issue with faxes being recived , the fax comes through as blank. On the trace it shows [Malformed Packet: T.38] I have never seen this before can anyone explain what this means.'''
date = "2016-11-21T03:33:00Z"
lastmod = "2016-11-21T04:35:00Z"
weight = 57516
keywords = [ "fax", "t.38", "malformedpacket" ]
aliases = [ "/questions/57516" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [T38 Malformed Packet](/questions/57516/t38-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57516-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have been doing a wireshark traces as were are having an issue with faxes being recived , the fax comes through as blank. On the trace it shows [Malformed Packet: T.38]</p><p>I have never seen this before can anyone explain what this means.</p></div><div id="question-tags" class="tags-container tags">fax t.38 malformedpacket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '16, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/0bfabb44c662192bed32f1818643c715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattG&#39;s gravatar image" /><p>MattG<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattG has no accepted answers">0%</span></p></div></div><div id="comments-container-57516" class="comments-container"></div><div id="comment-tools-57516" class="comment-tools"></div><div class="clear"></div><div id="comment-57516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57517"></span>

<div id="answer-container-57517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57517-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It means that wireshark detected that there was something in the data that it coulnd not make sense off. This either means there was something wrong in the received data or the T.38 dissector is not able to read the T.38 packet correctly (either because something was not implemented yet or correctly).</p><p>I looked at the source code and there are a couple of places where Wireshark might report a Malformed T.38 packet. It all depends on the pcap data you have. Are you able to share a tracefile? (see @Jasper's <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">blogpost about sharing files</a> for details)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '16, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '16, 07:04</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-57517" class="comments-container"><span id="57528"></span><div id="comment-57528" class="comment"><div id="post-57528-score" class="comment-score"></div><div class="comment-text"><p>Other than that, it may also mean that the sender of the T.38 (udptl) packets continued to send audio RTP a while after a switchover to T.38 has been renegotiated; Wireshark's telephony analyzer expects an immediate switchover so it assumes that the very first media packet after the renegotiation is already a T.38 one and dissects it as such. But if this is the case, you should see only first few packets marked as malformed, and the rest would be clean T.38.</p><p>Oh, and I've fixed the collision of formatting in @SYN-bit's Answer, so the link to the tutorial is now clickable as it should be.</p></div><div id="comment-57528-info" class="comment-info"><span class="comment-age">(21 Nov '16, 07:09)</span> sindy</div></div><span id="57529"></span><div id="comment-57529" class="comment"><div id="post-57529-score" class="comment-score"></div><div class="comment-text"><p>Oops, did not check the link, thanks for the correction @sindy. And also for the useful addition (I don't see T.38 packets often ;-))</p></div><div id="comment-57529-info" class="comment-info"><span class="comment-age">(21 Nov '16, 07:15)</span> SYN-bit ♦♦</div></div><span id="57530"></span><div id="comment-57530" class="comment"><div id="post-57530-score" class="comment-score"></div><div class="comment-text"><p>if you use <code>[@username text][1]</code>, the <code>@username</code> obviously wins over the <code>[][1]</code>.</p></div><div id="comment-57530-info" class="comment-info"><span class="comment-age">(21 Nov '16, 07:17)</span> sindy</div></div></div><div id="comment-tools-57517" class="comment-tools"></div><div class="clear"></div><div id="comment-57517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

