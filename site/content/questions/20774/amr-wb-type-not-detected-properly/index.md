+++
type = "question"
title = "AMR-WB type not detected properly"
description = '''I have wireshark capture for VoIP with AMR-WB. My capture does not have SIP transactions. So I have set the RTP preference field to decode the RTP packets with appropriate payload type as AMR-WB, octat aligned. I am able to see decoded packets. However, the protocol field shows it as only AMR. The f...'''
date = "2013-04-24T11:31:00Z"
lastmod = "2013-04-24T12:21:00Z"
weight = 20774
keywords = [ "dissector", "rtp", "voip", "wireshark" ]
aliases = [ "/questions/20774" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [AMR-WB type not detected properly](/questions/20774/amr-wb-type-not-detected-properly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have wireshark capture for VoIP with AMR-WB. My capture does not have SIP transactions. So I have set the RTP preference field to decode the RTP packets with appropriate payload type as AMR-WB, octat aligned. I am able to see decoded packets. However, the protocol field shows it as only AMR. The field type bits are properly decoded though to AMR-WB 12.2 kbits. Again, for SID frametype (value 9), I get illegal Frametype - For future use (9). I am using version 1.8.6</p></div><div id="question-tags" class="tags-container tags">dissector rtp voip wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/64692527faaf37e7a717e0cecb4612f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tecMav&#39;s gravatar image" /><p>tecMav<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tecMav has no accepted answers">0%</span></p></div></div><div id="comments-container-20774" class="comments-container"></div><div id="comment-tools-20774" class="comment-tools"></div><div class="clear"></div><div id="comment-20774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20776"></span>

<div id="answer-container-20776" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20776-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>the protocol field shows it as only AMR</p></blockquote><p>That's the way it's designed, the protocol is AMR.</p><blockquote><p>for SID frametype (value 9), I get illegal Frametype - For future use (9).</p></blockquote><p>Sounds like a bug could you raise a bug report and include a small sample trace and indicate which packet to look at and how preferences should be set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-20776" class="comments-container"><span id="20788"></span><div id="comment-20788" class="comment"><div id="post-20788-score" class="comment-score"></div><div class="comment-text"><p>I have one another capture with SIP packets, where the protocol is detected and shown as AMR-WB (in the protocol field I mean)?</p></div><div id="comment-20788-info" class="comment-info"><span class="comment-age">(24 Apr '13, 19:59)</span> tecMav</div></div><span id="20790"></span><div id="comment-20790" class="comment"><div id="post-20790-score" class="comment-score"></div><div class="comment-text"><p>Ok more info for the bug :-)</p></div><div id="comment-20790-info" class="comment-info"><span class="comment-age">(24 Apr '13, 22:58)</span> Anders ♦</div></div></div><div id="comment-tools-20776" class="comment-tools"></div><div class="clear"></div><div id="comment-20776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

