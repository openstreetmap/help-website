+++
type = "question"
title = "Packet size limited during capture: xxxxxx truncated"
description = '''Hello all, I am opening a pcap file and see the following message with some packets marked as: [Packet size limited during capture: xxxxxx truncated] I searched the web but there isn&#x27;t much information on it and hoping I could get the reason for the error. Thanks.'''
date = "2016-03-10T15:04:00Z"
lastmod = "2016-03-11T05:45:00Z"
weight = 50808
keywords = [ "limited", "during", "capture", "packet", "size" ]
aliases = [ "/questions/50808" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet size limited during capture: xxxxxx truncated](/questions/50808/packet-size-limited-during-capture-xxxxxx-truncated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50808-score" class="post-score" title="current number of votes">0</div><span id="post-50808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am opening a pcap file and see the following message with some packets marked as:</p><p>[Packet size limited during capture: xxxxxx truncated]</p><p>I searched the web but there isn't much information on it and hoping I could get the reason for the error.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-limited" rel="tag" title="see questions tagged &#39;limited&#39;">limited</span> <span class="post-tag tag-link-during" rel="tag" title="see questions tagged &#39;during&#39;">during</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '16, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/818d640e25f3c8f3050a5beb68af1d40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MYSLTN&#39;s gravatar image" /><p><span>MYSLTN</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MYSLTN has no accepted answers">0%</span></p></div></div><div id="comments-container-50808" class="comments-container"></div><div id="comment-tools-50808" class="comment-tools"></div><div class="clear"></div><div id="comment-50808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50809"></span>

<div id="answer-container-50809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50809-score" class="post-score" title="current number of votes">0</div><span id="post-50809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture mechanisms used by Wireshark, e.g. libpcap or WinPcap allow the length of capture packets to be limited, usually for performance reasons, as often all that's needed is the IP\TCP\UDP headers and not the payload.</p><p>When packets are limited this way, with the <code>snaplen</code> option, then Wireshark displays the information you've noticed. To capture the full packet, ensure <code>snaplen</code> is set to the default, usually 65535 in the capture options dialog for the interface the capture is made on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '16, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50809" class="comments-container"><span id="50810"></span><div id="comment-50810" class="comment"><div id="post-50810-score" class="comment-score"></div><div class="comment-text"><p>And tcpdump and other programs also use libpcap/WinPcap, and offer the same sort of length limitation (the <code>-s</code> flag to tcpdump - and TShark and Wireshark and dumpcap).</p><p>The capture mechanism used by some <em>other</em> network analyzers also offers that capability.</p><p>So the pcap file in question was probably captured with such a "snapshot length", i.e. maximum amount of packet data that will be captured and saved, configured. If you look at the "Frame" part of the dissection of one of those "Packet size limited during capture" packets, the "bytes captured" value will probably be the configured snapshot length.</p></div><div id="comment-50810-info" class="comment-info"><span class="comment-age">(10 Mar '16, 17:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="50821"></span><div id="comment-50821" class="comment"><div id="post-50821-score" class="comment-score"></div><div class="comment-text"><p>Thank you Grahamb &amp; Guy for the quick response. I will check the snapshot length for the analyzer tool.</p><p>Kind Regards.</p></div><div id="comment-50821-info" class="comment-info"><span class="comment-age">(11 Mar '16, 05:45)</span> <span class="comment-user userinfo">MYSLTN</span></div></div></div><div id="comment-tools-50809" class="comment-tools"></div><div class="clear"></div><div id="comment-50809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

