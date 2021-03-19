+++
type = "question"
title = "Extract RTP payload from capture file using tshark"
description = '''I have a valid capture in pcap-ng format(version 1.0) using tshark command like this: tshark -i wlp2s0 -n -f &quot;host 192.168.10.48 and udp port 9078&quot; -w capture_tshark_1.pcapng  I want to extract RTP payload in binary format and store it in a file and be reproducible. I tried this to extract binary da...'''
date = "2017-02-28T03:03:00Z"
lastmod = "2017-02-28T05:46:00Z"
weight = 59725
keywords = [ "capture-file", "tshark", "packet-capture", "rtp.payload", "rtp" ]
aliases = [ "/questions/59725" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract RTP payload from capture file using tshark](/questions/59725/extract-rtp-payload-from-capture-file-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59725-score" class="post-score" title="current number of votes">0</div><span id="post-59725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a valid capture in pcap-ng format(version 1.0) using <em>tshark</em> command like this:</p><pre><code>tshark -i wlp2s0 -n -f &quot;host 192.168.10.48 and udp port 9078&quot; -w capture_tshark_1.pcapng</code></pre><p><strong>I want to extract RTP payload in binary format and store it in a file and be reproducible.</strong></p><p>I tried this to extract binary data in ASCII format:</p><pre><code>tshark -nr capture_tshark_1.pcapng -T fields -e rtp.payload &gt; captura_tshark_1_ascii_data</code></pre><p>But it produces empty output. I guess it fails because RTP packets are not detected as RTP streams, because if I open the original capture (capture_tshark_1.pcapng) with Wireshark this is what I see:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/capture_UDP.png" alt="Wireshark screenshot UDP" /></p><p>It seems that the packets are detected as UDP, not as RTP. So I guess there is no such "rtp.payload" fields to be parsed.</p><p>If this works I have a method to transform ASCII data to binary format.</p><p>So, again, <strong>how can I extract RTP payload in binary format from a capture file?</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-file" rel="tag" title="see questions tagged &#39;capture-file&#39;">capture-file</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-rtp.payload" rel="tag" title="see questions tagged &#39;rtp.payload&#39;">rtp.payload</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/43814b7dc0c1b382c7d1ac4077de9491?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="logoff&#39;s gravatar image" /><p><span>logoff</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="logoff has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '17, 04:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59725" class="comments-container"></div><div id="comment-tools-59725" class="comment-tools"></div><div class="clear"></div><div id="comment-59725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59726"></span>

<div id="answer-container-59726" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59726-score" class="post-score" title="current number of votes">0</div><span id="post-59726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check Analyze|Enabled Protocols|RTP|rtp_udp</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '17, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59726" class="comments-container"><span id="59727"></span><div id="comment-59727" class="comment"><div id="post-59727-score" class="comment-score"></div><div class="comment-text"><p>I'm using tshark, not Wireshark.</p></div><div id="comment-59727-info" class="comment-info"><span class="comment-age">(28 Feb '17, 05:46)</span> <span class="comment-user userinfo">logoff</span></div></div></div><div id="comment-tools-59726" class="comment-tools"></div><div class="clear"></div><div id="comment-59726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

