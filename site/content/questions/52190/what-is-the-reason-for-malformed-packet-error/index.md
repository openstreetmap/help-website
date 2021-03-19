+++
type = "question"
title = "What is the reason for Malformed Packet Error ?"
description = '''Hi Folks,  Kindly share the exact reason for below wireshark Errors.  Malformed GSM Over IP (Malformed Packet Exception Occurred) Malformed RSL (Malformed Packet Exception Occurred) Malformed T.38 (Malformed Packet Exception Occurred) Malformed Bundle (Malformed Packet Exception Occurred) '''
date = "2016-05-03T13:28:00Z"
lastmod = "2016-05-03T13:46:00Z"
weight = 52190
keywords = [ "malformed_packet" ]
aliases = [ "/questions/52190" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the reason for Malformed Packet Error ?](/questions/52190/what-is-the-reason-for-malformed-packet-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52190-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>Kindly share the exact reason for below wireshark Errors.</p><ol><li>Malformed GSM Over IP (Malformed Packet Exception Occurred)</li><li>Malformed RSL (Malformed Packet Exception Occurred)</li><li>Malformed T.38 (Malformed Packet Exception Occurred)</li><li>Malformed Bundle (Malformed Packet Exception Occurred)</li></ol></div><div id="question-tags" class="tags-container tags">malformed_packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/ece77729d42d373e99fee1742f36bedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimmy2016&#39;s gravatar image" /><p>jimmy2016<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimmy2016 has no accepted answers">0%</span></p></div></div><div id="comments-container-52190" class="comments-container"><span id="52194"></span><div id="comment-52194" class="comment"><div id="post-52194-score" class="comment-score"></div><div class="comment-text"><p>This cannot be answered without the respective capture files, as there may be many different reasons.</p><p>In general, any frame (or part of it) is marked as malformed if the dissector finds data in it which do not match the grammar the dissector uses to dissect the frame. So data may be missing due to packet truncation, or there may be some protocol extension unknown to the dissector, or the actual protocol may be a different one than the dissector expects - e.g. as soon as an SDP re-negotiation changes the codec from G.729 to T.38, Wireshark starts applying a T.38 dissector to any UDP packet to/from the media sockets of the session, but in fact the change may not have happened that quickly, so still a couple of G.729 packets follow the SDP re-negotiation before real udptl/t38 packets occur.</p><p>And, of course, there may also be a bug in the dissector code.</p></div><div id="comment-52194-info" class="comment-info"><span class="comment-age">(03 May '16, 13:48)</span> sindy</div></div><span id="52198"></span><div id="comment-52198" class="comment"><div id="post-52198-score" class="comment-score"></div><div class="comment-text"><p>Thanks Buddy !</p><p>Could you also please help me find out the reason for Warning 1. "TCP: ACKed segment that wasn't captured (common at capture start)"<br />
2. HTTP: Unencrypted HTTP protocol detected over encrypted port, could indicate a dangerous misconfiguration"</p></div><div id="comment-52198-info" class="comment-info"><span class="comment-age">(03 May '16, 14:28)</span> jimmy2016</div></div></div><div id="comment-tools-52190" class="comment-tools"></div><div class="clear"></div><div id="comment-52190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52193"></span>

<div id="answer-container-52193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52193-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The reasons why a "Malformed Packet" error occurs are either</p><ol><li>the packet isn't valid according to the specification for the protocol</li><li>the packet <em>is</em> valid but the Wireshark dissector for it has a bug;</li><li>the packet isn't a packet for the protocol in question but is being dissected as a packet for that protocol by Wireshark.</li></ol><p>The answer could be different for those four examples; we would have to see the actual network traces to see, for each of them, what the reason is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-52193" class="comments-container"></div><div id="comment-tools-52193" class="comment-tools"></div><div class="clear"></div><div id="comment-52193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

