+++
type = "question"
title = "weird tcp packets not data not ack !"
description = '''Hi i was capturing packets with wireshark and i traced some of the packets and i came upon very weird packet and it happened more than once, this packet (Not in the 3-way handshake) has no data and it has Len=0 and it&#x27;s [ACK] BUT IT IS NOT ACKNOWLEDGING ANY PACKETS !  Usually in an ack packet in the...'''
date = "2015-06-23T08:26:00Z"
lastmod = "2015-06-24T08:58:00Z"
weight = 43476
keywords = [ "ack", "iperf", "packets", "tcp", "wireshark" ]
aliases = [ "/questions/43476" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [weird tcp packets not data not ack !](/questions/43476/weird-tcp-packets-not-data-not-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43476-score" class="post-score" title="current number of votes">0</div><span id="post-43476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i was capturing packets with wireshark and i traced some of the packets and i came upon very weird packet and it happened more than once, this packet (Not in the 3-way handshake) has no data and it has Len=0 and it's [ACK] BUT IT IS NOT ACKNOWLEDGING ANY PACKETS ! Usually in an ack packet in the TCP, in the options and in the [SEQ/ACK analysis] i have information that this is an ack packet to the segment x in frame number xx ...now i don't even have [SEQ/ACK analysis] in this weird packet .. so what packet is this i don't get it !<br />
</p><p>This is a link to the whole pcap file on dropbox -&gt;<br />
<a href="https://www.dropbox.com/s/18zhiqlvlili349/new.pcap?dl=0">https://www.dropbox.com/s/18zhiqlvlili349/new.pcap?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-iperf" rel="tag" title="see questions tagged &#39;iperf&#39;">iperf</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '15, 05:27</strong> </span></p></div></div><div id="comments-container-43476" class="comments-container"><span id="43477"></span><div id="comment-43477" class="comment"><div id="post-43477-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. CloudShark, Google Drive, Dropbox?</p></div><div id="comment-43477-info" class="comment-info"><span class="comment-age">(23 Jun '15, 08:42)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43500"></span><div id="comment-43500" class="comment"><div id="post-43500-score" class="comment-score"></div><div class="comment-text"><p>hi christian i added the whole file in dropbox please check it and try to help me out !</p></div><div id="comment-43500-info" class="comment-info"><span class="comment-age">(24 Jun '15, 05:28)</span> <span class="comment-user userinfo">yas1234</span></div></div></div><div id="comment-tools-43476" class="comment-tools"></div><div class="clear"></div><div id="comment-43476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43478"></span>

<div id="answer-container-43478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43478-score" class="post-score" title="current number of votes">1</div><span id="post-43478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the ACK number is pointing into the middle of a previous segment it may be due to tcp segmentation offload being enabled.</p><hr /><p>Your trace shows that the tcp.len on outbound packets exceeds the MSS, an indication that TCP Segmentation Offload is enabled. The client acknowledges 7240 bytes (5 segments a 1448 bytes) that it received - after the ethernet cards segmented them to fit on the ethernet.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-271.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '15, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '15, 07:49</strong> </span></p></div></div><div id="comments-container-43478" class="comments-container"><span id="43508"></span><div id="comment-43508" class="comment"><div id="post-43508-score" class="comment-score"></div><div class="comment-text"><p>I voted, because you were even yesterday right. (yetserday we had no trace)</p></div><div id="comment-43508-info" class="comment-info"><span class="comment-age">(24 Jun '15, 08:58)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-43478" class="comment-tools"></div><div class="clear"></div><div id="comment-43478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

