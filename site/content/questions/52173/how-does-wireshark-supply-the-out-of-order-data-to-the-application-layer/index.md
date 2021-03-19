+++
type = "question"
title = "How does wireshark supply the  out of order data to the application layer?"
description = '''Hello all, I am capturing interactive rendered streaming application over HTML5, and each video packet from the sender is 12 to 13KBytes, which is segmented by TCP to 8 or 9 TCP segments. At the receiver the video packets are also segmented by the receiving host.  I am identifying the video packets ...'''
date = "2016-05-03T05:47:00Z"
lastmod = "2016-05-18T03:09:00Z"
weight = 52173
keywords = [ "reassembly" ]
aliases = [ "/questions/52173" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does wireshark supply the out of order data to the application layer?](/questions/52173/how-does-wireshark-supply-the-out-of-order-data-to-the-application-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52173-score" class="post-score" title="current number of votes">0</div><span id="post-52173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am capturing interactive rendered streaming application over HTML5, and each video packet from the sender is 12 to 13KBytes, which is segmented by TCP to 8 or 9 TCP segments. At the receiver the video packets are also segmented by the receiving host.</p><p>I am identifying the video packets by the PTS of Matroska container format, which is written only to the first TCP segment of a video frame. In case of re-transmissions, the missing video data segment is sent after the next video frame is arrived.</p><p>Does wireshark have some mechanism to identify that the data belongs to the previous video packet? Does the application layer or the video decoder re-arrange the piece of data and wait until the right data segment is arrived to play the video stream?</p><p>Thanks in advance!</p><p>Tilak</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/6ac558d50e14e1baababd985172501e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Varisetty&#39;s gravatar image" /><p><span>Varisetty</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Varisetty has no accepted answers">0%</span></p></div></div><div id="comments-container-52173" class="comments-container"></div><div id="comment-tools-52173" class="comment-tools"></div><div class="clear"></div><div id="comment-52173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52209"></span>

<div id="answer-container-52209" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52209-score" class="post-score" title="current number of votes">0</div><span id="post-52209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Varisetty has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>At the receiver the video packets are also segmented by the receiving host.</p></blockquote><p>"Segmented" in what sense? The code that's reading from the connection on the receiving host might see all the TCP segments as the results of separate reads, or might see all the data in one read, or might see some other consolidating of segments into reads. Is that what you're referring to?</p><p>Wireshark, by the way, will not see that - it doesn't see what happens in the receiver's TCP stack. (Well, if Wireshark is running on the receiving host, and the receiver's network adapter is doing <em>de</em>segmentation, and the receiver's network stack is supplying the desegmented packets to the part of the stack that does packet capture, Wireshark will see the desegmented packets.)</p><blockquote><p>Does wireshark have some mechanism to identify that the data belongs to the previous video packet?</p></blockquote><p>If the video packets are being reassembled by Wireshark, yes - the dissector for the video packets is, somehow, identifying packet boundaries and telling the TCP dissector when it needs more data, and the TCP dissector is reassembling the data as necessary. How it identifies packet boundaries depends on the protocol - TCP does not provide any mechanism to identify higher-level packet boundaries, so it needs the help of dissectors that run atop it, for example, from each packet beginning with a length field.</p><blockquote><p>Does the application layer or the video decoder re-arrange the piece of data and wait until the right data segment is arrived to play the video stream?</p></blockquote><p>No - the rearrangement of the data is done by the receiving host's TCP implementation, and it supplies reassembled, in-order data to whatever code is reading that data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52209" class="comments-container"><span id="52711"></span><div id="comment-52711" class="comment"><div id="post-52711-score" class="comment-score"></div><div class="comment-text"><p>thanks Harris for the explanation. My question was about the segmentation and not particularly about the read call from the socket, but it is a good point to highlight.</p><p>So, you mean the application layer protocol has some dissectors that identify the packet boundaries, and communicate to TCP that the packet boundaries have not arrived yet?</p><p>Thanks! Tilak</p></div><div id="comment-52711-info" class="comment-info"><span class="comment-age">(18 May '16, 02:40)</span> <span class="comment-user userinfo">Varisetty</span></div></div><span id="52715"></span><div id="comment-52715" class="comment"><div id="post-52715-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So, you mean the application layer protocol has some dissectors that identify the packet boundaries, and communicate to TCP that the packet boundaries have not arrived yet?</p></blockquote><p>Yes, the dissector for a protocol running atop TCP identifies packet boundaries and:</p><ol><li>that dissector dissects, independently, all the packets within the data handed to it by the TCP dissector, as there may be more than one packet within a TCP segment;</li><li>if, for the last (or only) packet within the data handed to it by the TCP dissector, not all the data in that packet is present in that data, that dissector indicates to the TCP dissector that it needs more data, so that, when the TCP dissector sees the next TCP segment, it adds it to the data corresponding to that last packet and hands the resulting reassembled data to that dissector.</li></ol><p>This is somewhat similar to what an implementation of a protocol running atop TCP has to do in the receiving code, although it's somewhat simpler due to it being able to "pull" data from TCP by doing a read, rather than, as is the case with dissectors, having TCP "push" data to the subdissector, so if a protocol implementation needs only N bytes of data, it can, at least in most operating systems, read just N bytes and leave the remainder of the bytes for it to read later.</p></div><div id="comment-52715-info" class="comment-info"><span class="comment-age">(18 May '16, 03:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-52209" class="comment-tools"></div><div class="clear"></div><div id="comment-52209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

