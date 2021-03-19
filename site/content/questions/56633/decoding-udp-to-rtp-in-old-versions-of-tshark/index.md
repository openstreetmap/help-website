+++
type = "question"
title = "Decoding UDP to RTP in old versions of tshark"
description = '''I have a pcap file containing RTP over UDP packets Using thark 2.0.2 I can decode this using:  tshark -r capture.pcap -d udp.port==1-65535,rtp -Y ip.src==xxxx -T fields -e rtp.seq Using 1.0.15 the decode fails, and though data is printed to screen, it is the undecoded UDP An obvious solution would b...'''
date = "2016-10-25T01:14:00Z"
lastmod = "2016-10-25T03:04:00Z"
weight = 56633
keywords = [ "udp", "rtp", "tshark" ]
aliases = [ "/questions/56633" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding UDP to RTP in old versions of tshark](/questions/56633/decoding-udp-to-rtp-in-old-versions-of-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56633-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file containing RTP over UDP packets Using thark 2.0.2 I can decode this using:</p><p>tshark -r capture.pcap -d udp.port==1-65535,rtp -Y ip.src==xxxx -T fields -e rtp.seq</p><p>Using 1.0.15 the decode fails, and though data is printed to screen, it is the undecoded UDP</p><p>An obvious solution would be to upgrade tshark on the second system, but for various reasons this is problematic...is there any alternative?</p></div><div id="question-tags" class="tags-container tags">udp rtp tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '16, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/ed56b38042032c7d46130c321dbcbd7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbrb2&#39;s gravatar image" /><p>dbrb2<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbrb2 has no accepted answers">0%</span></p></div></div><div id="comments-container-56633" class="comments-container"><span id="56634"></span><div id="comment-56634" class="comment"><div id="post-56634-score" class="comment-score"></div><div class="comment-text"><p>maybe this will help?</p><p><a href="https://ask.wireshark.org/questions/10440/how-to-decode-the-udp-to-rtp-in-command-line">https://ask.wireshark.org/questions/10440/how-to-decode-the-udp-to-rtp-in-command-line</a></p></div><div id="comment-56634-info" class="comment-info"><span class="comment-age">(25 Oct '16, 02:51)</span> koundi</div></div><span id="56635"></span><div id="comment-56635" class="comment"><div id="post-56635-score" class="comment-score"></div><div class="comment-text"><p>you might want to check this as well! <a href="https://ask.wireshark.org/questions/50226/how-to-decode-udp-as-rtp-tshark-only">https://ask.wireshark.org/questions/50226/how-to-decode-udp-as-rtp-tshark-only</a></p></div><div id="comment-56635-info" class="comment-info"><span class="comment-age">(25 Oct '16, 02:54)</span> koundi</div></div></div><div id="comment-tools-56633" class="comment-tools"></div><div class="clear"></div><div id="comment-56633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56638"></span>

<div id="answer-container-56638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56638-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably in the settings, there's one called 'Try to decode RTP outside of conversations" in the ui. You can also set this from the command line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '16, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56638" class="comments-container"><span id="56639"></span><div id="comment-56639" class="comment"><div id="post-56639-score" class="comment-score"></div><div class="comment-text"><p>from one of your own answers it is this i guess "-o rtp.heuristic_rtp:TRUE"</p></div><div id="comment-56639-info" class="comment-info"><span class="comment-age">(25 Oct '16, 03:06)</span> koundi</div></div><span id="56640"></span><div id="comment-56640" class="comment"><div id="post-56640-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately this fails on some streams with older wireshark.</p><p>I will try to use a newer release...</p></div><div id="comment-56640-info" class="comment-info"><span class="comment-age">(25 Oct '16, 03:39)</span> dbrb2</div></div></div><div id="comment-tools-56638" class="comment-tools"></div><div class="clear"></div><div id="comment-56638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

