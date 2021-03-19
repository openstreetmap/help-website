+++
type = "question"
title = "Duplicate ACKs + delayed retransmission (part 2)"
description = '''This is a followup question from an earlier post whihc was answered by SYN-bit: I just realized something that does not make sense to me in the capture: Wireshark and the program I am using to perform the nttcp test (nttcp under Cygwin) are executed on the same machine: how is it possible that Wires...'''
date = "2015-02-18T13:03:00Z"
lastmod = "2015-02-21T22:13:00Z"
weight = 39935
keywords = [ "duplicateacks", "821" ]
aliases = [ "/questions/39935" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate ACKs + delayed retransmission (part 2)](/questions/39935/duplicate-acks-delayed-retransmission-part-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39935-score" class="post-score" title="current number of votes">0</div><span id="post-39935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a followup question from an <a href="https://ask.wireshark.org/questions/39898/duplicate-acks-delayed-retransmission">earlier post</a> whihc was answered by SYN-bit: I just realized something that does not make sense to me in the capture: Wireshark and the program I am using to perform the nttcp test (nttcp under Cygwin) are executed on the same machine: how is it possible that Wireshark captures all packets, but my nttcp program misses them? Or am I misinterpreting the results here?</p><p>The capture is <a href="https://www.cloudshark.org/captures/faff95c615f6">located here</a>.</p><p>Thanks! Dirk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicateacks" rel="tag" title="see questions tagged &#39;duplicateacks&#39;">duplicateacks</span> <span class="post-tag tag-link-821" rel="tag" title="see questions tagged &#39;821&#39;">821</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '15, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/bdcd60c8f4bd21eda021aa35fc76b4d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djbuijs&#39;s gravatar image" /><p><span>djbuijs</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djbuijs has no accepted answers">0%</span></p></div></div><div id="comments-container-39935" class="comments-container"></div><div id="comment-tools-39935" class="comment-tools"></div><div class="clear"></div><div id="comment-39935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40001"></span>

<div id="answer-container-40001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40001-score" class="post-score" title="current number of votes">0</div><span id="post-40001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"... how is it possible that Wireshark captures all packets, but my nttcp program misses them?"<br />
The application received all bytes that were sent on the data connection. The ack number in the FIN packet is is the number of bytes received (plus 2 for SYN and FIN bit).<br />
Using TCP protocol, the application is not aware of packets but just passes a byte-stream to the send buffer. TCP will segment the data and send it in IP packets over the network. In case a packet get lost, TCP as a reliable transport will take care of re-transmitting the packet (without any notification/intervention of the application).<br />
So the difference of the data see in your application and the data that was traced should only be the retransmitted packets, packets 51 and and 124 in your capture.<br />
Regards Matthias</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_276.png" alt="alt text" /></p><hr /><p><em>" but there's still the issue of the Duplicate ACKS, which suggests that somewhere in a lower layer packets got dropped. However, Wireshark seems to have managed to capture all packets!"</em></p><p>Well, this trace does not contain all packets that were actually flowing as dumpcap couldn't keep up with the amount of traffic. And, the packets are not necessarily 'dropped in the lower layer'.</p><p>In your case the packets are dropped in the TCP layer of Windows7 because the TCP checksum is incorrect in packets that caused the duplicate ACKs. _ws.expert.severity gt "warn" will yield those packets if you enable TCP checksum validation in the protocol preferences.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-29.4711_direct_stripped.pcapng.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '15, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Feb '15, 02:20</strong> </span></p></div></div><div id="comments-container-40001" class="comments-container"><span id="40014"></span><div id="comment-40014" class="comment"><div id="post-40014-score" class="comment-score"></div><div class="comment-text"><p>Hi Matthias, Thanks for your help on this. It's still a bit of a mystery what is going on exactly. I understand the way TCP is basically a pipe when seem from the application layer, but there's still the issue of the Duplicate ACKS, which suggests that somewhere in a lower layer packets got dropped. However, Wireshark seems to have managed to capture all packets!</p><p>Regards, Dirk</p></div><div id="comment-40014-info" class="comment-info"><span class="comment-age">(21 Feb '15, 22:13)</span> <span class="comment-user userinfo">djbuijs</span></div></div></div><div id="comment-tools-40001" class="comment-tools"></div><div class="clear"></div><div id="comment-40001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

