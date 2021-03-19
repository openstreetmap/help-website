+++
type = "question"
title = "SCTP DATA is not getting decoded correctly and is showing Malformed Packet"
description = '''SCTP Association is correctly setup between two linux machines. When I send Data from Machine 1 --&amp;gt; Machine 2 using SCTP ---&amp;gt; I see the following in Wireshark  Protocol Type = S1AP  Msg (Info) = id-HandoverNotification [Malformed Packet] This is followed by a SACK from second Linux machine  I ...'''
date = "2011-03-18T09:21:00Z"
lastmod = "2011-03-18T10:18:00Z"
weight = 2922
keywords = [ "sctp", "data", "sack", "malformed", "linux" ]
aliases = [ "/questions/2922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SCTP DATA is not getting decoded correctly and is showing Malformed Packet](/questions/2922/sctp-data-is-not-getting-decoded-correctly-and-is-showing-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>SCTP Association is correctly setup between two linux machines. When I send Data from Machine 1 --&gt; Machine 2 using SCTP ---&gt; I see the following in Wireshark Protocol Type = S1AP Msg (Info) = id-HandoverNotification [Malformed Packet] This is followed by a SACK from second Linux machine</p><p>I also verified in the command prompt of the second Linux Machine that it did receive the data correctly and therefore sent the SACK back to the first Linux Machine.</p><p>Interesting thing is, when I send the DATA from Linux Machine 2 --&gt; to Linux Machine 1 then I do not see any problem in Wireshark. The DATA shows up correctly followed by a SACK from first Linux Machine.</p><p>Is there a problem/bug in wireshark for decoding the SCTP DATA in one direction?</p></div><div id="question-tags" class="tags-container tags">sctp data sack malformed linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '11, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/66b468c9e41a7facf42a464933fae604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chingu&#39;s gravatar image" /><p>chingu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chingu has no accepted answers">0%</span></p></div></div><div id="comments-container-2922" class="comments-container"><span id="2927"></span><div id="comment-2927" class="comment"><div id="post-2927-score" class="comment-score"></div><div class="comment-text"><p>If the ppid is Payload protocol identifier: S1 Application Protocol (S1AP) (18) Your application is using a ppid assigned for another protocol.</p><p>/ <em>Dissector will use SCTP PPID 18 or SCTP port. IANA assigned port = 36412</em> / If the port is 36412 your application is using a port assigned for another protocol. You can dissable s1ap or try "dissect as" if we have a dissector for the actual protocol.</p></div><div id="comment-2927-info" class="comment-info"><span class="comment-age">(18 Mar '11, 12:11)</span> Anders ♦</div></div></div><div id="comment-tools-2922" class="comment-tools"></div><div class="clear"></div><div id="comment-2922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2924"></span>

<div id="answer-container-2924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2924-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most probably you are using the port or PPID assigned to S1AP in your communication.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '11, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-2924" class="comments-container"><span id="2925"></span><div id="comment-2925" class="comment"><div id="post-2925-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt response. Will you be able to tell how/where can I check this and fix it?</p><p>thanks again</p></div><div id="comment-2925-info" class="comment-info"><span class="comment-age">(18 Mar '11, 10:22)</span> chingu</div></div></div><div id="comment-tools-2924" class="comment-tools"></div><div class="clear"></div><div id="comment-2924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

