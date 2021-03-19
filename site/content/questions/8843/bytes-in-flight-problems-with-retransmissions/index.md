+++
type = "question"
title = "Bytes in flight - Problems with retransmissions?"
description = '''Hey I&#x27;ve read that wireshark had problems with the bytes in flight value, when retransmissions occur. This bug was fixed in version 1.4.1. Well, but I&#x27;ve got a trace, where the values does not seem to bee correct. The link to this .pcap file is: http://uploading.com/files/ce18d69a/bytes_in_flight_pr...'''
date = "2012-02-06T04:59:00Z"
lastmod = "2012-02-07T16:34:00Z"
weight = 8843
keywords = [ "retransmissions", "tcp-bytes-in-flight" ]
aliases = [ "/questions/8843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes in flight - Problems with retransmissions?](/questions/8843/bytes-in-flight-problems-with-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8843-score" class="post-score" title="current number of votes">0</div><span id="post-8843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey</p><p>I've read that wireshark had problems with the bytes in flight value, when retransmissions occur. This bug was fixed in version 1.4.1. Well, but I've got a trace, where the values does not seem to bee correct. The link to this .pcap file is: http://uploading.com/files/ce18d69a/bytes_in_flight_problem.pcap/<br />
In this trace the calculation of bytes in flight is correct until frame 17, where it is 1714. I calculated manually the bytes in flight values of this trace and my result would be 1460 for frame 17! It seems that the retransmission is not taken into account when it is acknowledged. After this frame the calculation of Wireshark is correct again. So does wireshark 1.6.5 has problems too with this calculation when retransmissions occur?</p><p>Thanks for your answer! Best regards, mario</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp-bytes-in-flight" rel="tag" title="see questions tagged &#39;tcp-bytes-in-flight&#39;">tcp-bytes-in-flight</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '12, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/128b142c3a9292444f555b1aad741960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dranigl&#39;s gravatar image" /><p><span>dranigl</span><br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dranigl has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-8843" class="comments-container"><span id="8846"></span><div id="comment-8846" class="comment"><div id="post-8846-score" class="comment-score"></div><div class="comment-text"><p>It appears that the hosting service you have used for your capture is now demanding payment before I can download it.</p><p>Putting your capture on somewhere more accessible, e.g. <a href="http://www.cloudshark.org">CloudShark</a> would be more helpful.</p></div><div id="comment-8846-info" class="comment-info"><span class="comment-age">(06 Feb '12, 07:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="8867"></span><div id="comment-8867" class="comment"><div id="post-8867-score" class="comment-score"></div><div class="comment-text"><p>I have now uploaded the capture file to cloudshark, the link is</p><p>https://www.cloudshark.org/captures/01e4d4ac94cf</p></div><div id="comment-8867-info" class="comment-info"><span class="comment-age">(06 Feb '12, 23:30)</span> <span class="comment-user userinfo">dranigl</span></div></div><span id="8871"></span><div id="comment-8871" class="comment"><div id="post-8871-score" class="comment-score"></div><div class="comment-text"><p>From what I see 1.6.5 has the same issue. I looked at the trace at the whole flow and cannot find a reason for that.</p><p>I could imagine, that wireshark has problems with that trace, because the way this 10.114.x.y machine sends out acknowledgements is totally different to every other TCP implementation I know especially by sending unneeded ACKs without any more incoming data to acknowledge. Maybe the bytes_in_flight algorithm simply does not expect such behaviour</p></div><div id="comment-8871-info" class="comment-info"><span class="comment-age">(07 Feb '12, 00:53)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="8872"></span><div id="comment-8872" class="comment"><div id="post-8872-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer. So do you think that this is a bug which should be posted at bugs.wireshark.org?</p></div><div id="comment-8872-info" class="comment-info"><span class="comment-age">(07 Feb '12, 01:07)</span> <span class="comment-user userinfo">dranigl</span></div></div></div><div id="comment-tools-8843" class="comment-tools"></div><div class="clear"></div><div id="comment-8843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8880"></span>

<div id="answer-container-8880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8880-score" class="post-score" title="current number of votes">0</div><span id="post-8880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug. The retransmitted data in frame 12 spans more than the original transmitted segments (frames 4, 9 &amp; 10 plus new data) and the ACK in frame 16 is only for part of the data in frame 12. The code that calculates the bytes in flight uses the whole of frame 12 in calculating the value, so in frame 17 is doing so from the sequence number 1359412875 up to the 'next' sequence number for frame 17 which is 1359414589 giving the displayed value (4589 - 2875 = 1714).</p><p>The code works by keeping a linked list of unacked segments, but doesn't handle partially acked segments as in frame 12.</p><p><strong>Edit:</strong> Hopefully this is fixed in any rev later than 40929.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '12, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Feb '12, 04:50</strong> </span></p></div></div><div id="comments-container-8880" class="comments-container"></div><div id="comment-tools-8880" class="comment-tools"></div><div class="clear"></div><div id="comment-8880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

