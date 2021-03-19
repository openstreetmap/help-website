+++
type = "question"
title = "QoS in TCP and UDP protocol"
description = '''I have two files of captured traffic in wireshark.  at the source (say 192.168.100.1) and the other is on the destination (192.168.100.6) and I want to ask you some questions about the QoS parameters in wireshark. end-to-end delay, jitter, throughput, and packet loss. I have two scenarios, transfer ...'''
date = "2014-12-25T07:28:00Z"
lastmod = "2014-12-25T09:42:00Z"
weight = 38705
keywords = [ "delay", "jitter", "qos", "throughput", "packetloss" ]
aliases = [ "/questions/38705" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [QoS in TCP and UDP protocol](/questions/38705/qos-in-tcp-and-udp-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38705-score" class="post-score" title="current number of votes">0</div><span id="post-38705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two files of captured traffic in wireshark. at the source (say 192.168.100.1) and the other is on the destination (192.168.100.6) and I want to ask you some questions about the QoS parameters in wireshark. <strong>end-to-end delay, jitter, throughput, and packet loss.</strong></p><p>I have two scenarios, transfer files between computers and a video streaming using VLC (via RTSP protocol)</p><p>I believe that the file transfer use TCP protocol and video streaming use UDP and RTP protocol.</p><p>so far,</p><ul><li><strong>Transfer files (TCP)</strong></li></ul><p><strong>throughput</strong> - in the Statistics -&gt; Summary (done)</p><p><strong>end-to-end delay</strong>, <strong>jitter</strong>, <strong>packet loss</strong> - I have no idea how to find that parameters.</p><ul><li><strong>video streaming (RTP)</strong></li></ul><p><strong>throughput</strong> - Statistics -&gt; Summary (done)</p><p><strong>packet loss</strong> - Telephony -&gt; RTP -&gt; Show all streams</p><p>detected two RTP streams, &lt;5% packet loss and the other has &gt;40% packet loss (which one is correct?)</p><p><strong>jitter</strong> and max delta has a value of 0 (is there another way to find this?) is this correct for an RTP protocol?<br />
</p><p><strong>end-to-end delay</strong> - I have no idea how to find this parameter</p><p>Is there a way to find these missing parameters? I hope to get an answer here because I already posted a question before but did not get a response.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-jitter" rel="tag" title="see questions tagged &#39;jitter&#39;">jitter</span> <span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span> <span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Dec '14, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/e5f4e771b25d4df0b74c7a1c9deeef05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aikaza&#39;s gravatar image" /><p><span>aikaza</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aikaza has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-38705" class="comments-container"></div><div id="comment-tools-38705" class="comment-tools"></div><div class="clear"></div><div id="comment-38705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38707"></span>

<div id="answer-container-38707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38707-score" class="post-score" title="current number of votes">1</div><span id="post-38707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Wireshark is primarily intended for network packet dissection its capabilities for high level analysis are somewhat limited. Anything that needs information from both captures it cannot analyze for you. Some protocols have relevant information in their information stream which helps analysis (eg. TCP retransmissions, RTP sequence numbering). If we go through these itemized:</p><ul><li>TCP throughput: that can be derived from the protocol interaction at a single endpoint, hence is available.</li><li>TCP e2e delay, jitter, packet loss: Hard to do based on a single capture, apart from the packet loss maybe, as retransmissions would indicate as such. Not aware of a ready made analysis function right now.</li><li>RTP throughput: that can be derived from the protocol interaction at a single endpoint, hence is available.</li><li>RTP packet loss: Be aware, you use an Telephony analysis feature for video, that doesn't work. Unfortunately the RTP statistics are not profile aware and geared towards telephony only. And even then only the simplest cases.</li><li>RTP e2e delay: Hard to do based on a single capture.</li></ul><p>So, even though it doesn't help you in the short run, it shows you that you need to go and understand how the analysis is done. Then, with the exported raw data, you could setup the analysis from that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '14, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-38707" class="comments-container"><span id="38710"></span><div id="comment-38710" class="comment"><div id="post-38710-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap for your quick answer.</p><p>I apologize for the lack of information on my question. I mean I have two files (as a server and client) in both scenarios, so I have a total of 4 files.</p><p>Related to packet loss, do I really have packet loss if the retransmission successfully sent to the destination?</p><p>Since I have two files are needed, what parameters should be considered to obtain e2e delay, packet loss and jitter both TCP and RTP?</p><p>Last but not the least, where I can find the RTP packet loss and jitter other than through telephony analysis?</p></div><div id="comment-38710-info" class="comment-info"><span class="comment-age">(25 Dec '14, 09:42)</span> <span class="comment-user userinfo">aikaza</span></div></div></div><div id="comment-tools-38707" class="comment-tools"></div><div class="clear"></div><div id="comment-38707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

