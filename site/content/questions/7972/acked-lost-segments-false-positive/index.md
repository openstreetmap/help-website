+++
type = "question"
title = "ACKed lost segments - false positive?"
description = '''Hi,  not sure if I am too dumb to get that right, but I am puzzled by that finding:  In a 30-sec trace I found quite a few packet pairs, each one for another socket/stream (and the only packets for those sockets(/streams during the captured period at all) like that one: Time Source Destination Proto...'''
date = "2011-12-14T09:48:00Z"
lastmod = "2011-12-14T12:36:00Z"
weight = 7972
keywords = [ "ack", "lost", "tcp" ]
aliases = [ "/questions/7972" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ACKed lost segments - false positive?](/questions/7972/acked-lost-segments-false-positive)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7972-score" class="post-score" title="current number of votes">0</div><span id="post-7972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>not sure if I am too dumb to get that right, but I am puzzled by that finding:</p><p>In a 30-sec trace I found quite a few packet pairs, each one for another socket/stream (and the only packets for those sockets(/streams during the captured period at all) like that one:</p><pre><code>Time                       Source                Destination           Protocol Info
407 2011-12-14 17:17:30.182151 172.17.55.50          172.17.55.73          TCP      48730 &gt; 33779 [ACK] Seq=1 Ack=1 Win=294 Len=0 TSV=3645344977 TSER=2526914065
408 2011-12-14 17:17:30.182199 172.17.55.73          172.17.55.50          TCP      [TCP ACKed lost segment] 33779 &gt; 48730 [ACK] Seq=1 Ack=2 Win=63 Len=0 TSV=2526974281 TSER=3645284761</code></pre><p>This is not quite clear to me: packet 407 comes with a sequence number of 1. In 408, the reply means: got all data up to seq 1, expect at least seq 2 ... Can't see why that is not a perfect ACK to the preceeding packet.</p><p>Another question is of course where that SeqNumber 1 comes from. Would not carry the SYN-ACK and the following ACK during session establishment already seq number 1? So - as the socket was established before the capture apparently, the only explanation would be a wraparound of the seq number. But: for all the seen suspicious ACK pairs where Wireshark sees ACKs for lost segments, the seq.nums and ACKs have the same values (1, 2) ! If however the initial SeqNumber is 0, the numbers in those packets would be ok, but then Wireshark should flag the first of the packets as ACKed lost segment (as the preceeding one in that stream is indeed not captured !), shouldn't it?</p><p>Any advice welcome.</p><p>Uwe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '11, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/79f833616dc05e5e83e524c8513ad2e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ufalke&#39;s gravatar image" /><p><span>ufalke</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ufalke has no accepted answers">0%</span></p></div></div><div id="comments-container-7972" class="comments-container"></div><div id="comment-tools-7972" class="comment-tools"></div><div class="clear"></div><div id="comment-7972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7975"></span>

<div id="answer-container-7975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7975-score" class="post-score" title="current number of votes">3</div><span id="post-7975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Lets first start with the value of the SEQ and ACK. By default Wireshark will show relative sequence numbers. This means, it takes the sequence number of the SYN and SYN/ACK packets as reference and calculates the difference. The result is shown. You can verify this by clicking on the SEQ or ACK field and look at the 4 bytes in the hex pane, they show a different number. If Wireshark did not see the SYN, the SEQ and ACK of the first packet of the conversation will be shown as 1.</p><p>Now for the "ACK lost segment", the SEQ in frame 407 is 1, but its tcp length is 0, so the next expected sequence number would again be 1. So when the ACK in frame 408 comes with a value of 2, there must have been (at least) one frame lost. This can also be seen by looking at the TCP Timestamp options. The TSER in frame frame 408 is the "echo" of the last seen TSV from the other side. As the TSV in frame 407 is smaller than the TSER in frame 408, this means there must have been at least one other packet on the network in between those packets.</p><p>Then for the grande finale, since these two frames come right after one-another in the tracefile, the only logical conclusion would be that the capture process was not able to capture all packets to disk during the capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '11, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7975" class="comments-container"><span id="7979"></span><div id="comment-7979" class="comment"><div id="post-7979-score" class="comment-score"></div><div class="comment-text"><p>Thank you (knew it was my fault :-). If I got that right, it could only be that tcpdump (which I used to capture) did drop packets. If the network (switch/cables) would have dropped anything, we would see retransmits (which we don't), right? The rel. ACK number of 2 means that he TCP layer has received something on that socket in between . So : would it be correct to not suppose switch or cable problems (that is of interest as there is a slight suspicion towards a switch )?<br />
</p><p>many thanks again Uwe</p></div><div id="comment-7979-info" class="comment-info"><span class="comment-age">(14 Dec '11, 12:05)</span> <span class="comment-user userinfo">ufalke</span></div></div><span id="7981"></span><div id="comment-7981" class="comment"><div id="post-7981-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment" as that is the way this site works best, please see the FAQ)</p><p>You are right in the statement that the switch did not discard the packet between the communicating systems. However, the switch might have discarded the packet on the spanport. This happens for instance if you create a monitor session of a 100 Mbit/s Full Duplex port that is both receiving as sending &gt;50 Mbit/s. The resulting load on the monitor port would become &gt; 100 Mbit/s. So if your monitor device is connected @ 100Mbit/s, then you would see drops on the spanport of the switch.</p></div><div id="comment-7981-info" class="comment-info"><span class="comment-age">(14 Dec '11, 12:22)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="7982"></span><div id="comment-7982" class="comment"><div id="post-7982-score" class="comment-score"></div><div class="comment-text"><p>thanks for fixing me up :-&gt; the capture was done on an 1GbE NIC on one of the related Linux box (i.e. on an endpoint), not on the switch. So, if anything has dropped packets, it must have been tcpdump. Looking closely at the example, there are just about 48us between the two frames. That is about the typical TCP/IP over Ethernet round trip latency, isn't it? The overall packet rate was not seen as I filtered for just 4 target hosts. I might capture all traffic instead, may be the on-the-fly fileter for a set of 4 peer IP addresses causes packet drops?</p></div><div id="comment-7982-info" class="comment-info"><span class="comment-age">(14 Dec '11, 12:36)</span> <span class="comment-user userinfo">ufalke</span></div></div></div><div id="comment-tools-7975" class="comment-tools"></div><div class="clear"></div><div id="comment-7975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

