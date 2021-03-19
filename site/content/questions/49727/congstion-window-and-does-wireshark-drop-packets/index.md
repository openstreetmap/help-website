+++
type = "question"
title = "Congstion window and does wireshark drop packets?"
description = '''Hello, I am working on an experimental network and analyse the congestion window using tcpprobe and I notice that the congestion window drops periodically and no duplicate acks, or timeouts are seen at the sender in my wireshark trace. This does not fit with the TCP congestion window theory. I am us...'''
date = "2016-02-02T07:32:00Z"
lastmod = "2016-02-03T13:15:00Z"
weight = 49727
keywords = [ "congestion-control" ]
aliases = [ "/questions/49727" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Congstion window and does wireshark drop packets?](/questions/49727/congstion-window-and-does-wireshark-drop-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49727-score" class="post-score" title="current number of votes">0</div><span id="post-49727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am working on an experimental network and analyse the congestion window using tcpprobe and I notice that the congestion window drops periodically and no duplicate acks, or timeouts are seen at the sender in my wireshark trace. This does not fit with the TCP congestion window theory. I am using the default congestion control algorithm in linux, cubic. Is there a Linux implementation which allows the congestion window to drop when it is larger than ssthresh? Ideally the channel capacity is 100Mbit and the video traffic is 2Mbps, which should not lead to packet loss. I am not sure if wireshark drops some packets.</p><p>Any thoughts on this is highly appreciated!</p><p>Thanks in advance! Tilak</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-congestion-control" rel="tag" title="see questions tagged &#39;congestion-control&#39;">congestion-control</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/6ac558d50e14e1baababd985172501e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Varisetty&#39;s gravatar image" /><p><span>Varisetty</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Varisetty has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '16, 08:00</strong> </span></p></div></div><div id="comments-container-49727" class="comments-container"><span id="49792"></span><div id="comment-49792" class="comment"><div id="post-49792-score" class="comment-score"></div><div class="comment-text"><p>Knowing nothing about your capturing machine (hardware, OS, process load), it is hard to guess whether Wireshark is dropping packets or not. But try using tcpdump (if on linux) or dumpcap to store the captured packets into a file without analysing them while capturing; not only that these applications lower the CPU and memory load as compared to Wireshark or tshark, but they would also tell you whether they have failed to process some packets due to lack of CPU power or memory. They won't tell you, however, about packets that haven't even reached them.</p><p>On Windows, there are many security applications known to affect WinPcap's ability to see all packets (search this site for details); on Linux, I could think about some rate limiting setup of <a href="http://www.lartc.org/howto/lartc.qdisc.html">tc</a> to limit the throughput beyond the congestion control of the tcp stack itself, but not Wireshark's/tcpdump's ability to capture the packets which have really passed through the network adaptor. TCP processing offloading (chimney) may be responsible for not showing all packets to Wireshark at both OSes - again, look around at this site for this type of issues.</p></div><div id="comment-49792-info" class="comment-info"><span class="comment-age">(03 Feb '16, 13:15)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49727" class="comment-tools"></div><div class="clear"></div><div id="comment-49727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

