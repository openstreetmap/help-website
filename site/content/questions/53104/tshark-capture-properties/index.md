+++
type = "question"
title = "TShark Capture Properties"
description = '''Is there a way to export the Capture File Properties with TShark? Specifically I would like to get the following data out of a pcap or pcapng file:  First Packet Time Second Packet Time Elapsed Statics: Number of Packets Statics: Average bytes/s Comment  Thanks'''
date = "2016-06-01T06:36:00Z"
lastmod = "2016-06-01T06:43:00Z"
weight = 53104
keywords = [ "tshark" ]
aliases = [ "/questions/53104" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TShark Capture Properties](/questions/53104/tshark-capture-properties)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53104-score" class="post-score" title="current number of votes">0</div><span id="post-53104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to export the Capture File Properties with TShark?</p><p>Specifically I would like to get the following data out of a pcap or pcapng file:</p><ul><li>First Packet Time</li><li>Second Packet Time</li><li>Elapsed</li><li>Statics: Number of Packets</li><li>Statics: Average bytes/s</li><li>Comment</li></ul><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p><span>Rob B</span><br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div></div><div id="comments-container-53104" class="comments-container"></div><div id="comment-tools-53104" class="comment-tools"></div><div class="clear"></div><div id="comment-53104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53107"></span>

<div id="answer-container-53107" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53107-score" class="post-score" title="current number of votes">2</div><span id="post-53107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rob B has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried <a href="https://www.wireshark.org/docs/man-pages/capinfos.html"><code>capinfos</code></a>? I believe it provides everything you're looking for, but if there is some useful information that is not currently available with the tool, you can file an <a href="https://bugs.wireshark.org/bugzilla/">enhancement bug request</a> to ask for it to be added.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-53107" class="comments-container"></div><div id="comment-tools-53107" class="comment-tools"></div><div class="clear"></div><div id="comment-53107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53108"></span>

<div id="answer-container-53108" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53108-score" class="post-score" title="current number of votes">1</div><span id="post-53108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try capinfos, which should be installed right alongside tshark:</p><pre><code>capinfos C:\Users\xxx\Downloads\http-bug.pcap

File name:           C:\Users\xxx\Downloads\http-bug.pcap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Ethernet
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 262144 bytes
Number of packets:   9000
File size:           9722 kB
Data size:           9578 kB
Capture duration:    14.434019 seconds
First packet time:   2011-10-20 23:54:45.106241
Last packet time:    2011-10-20 23:54:59.540260
Data byte rate:      663 kBps
Data bit rate:       5308 kbps
Average packet size: 1064.27 bytes
Average packet rate: 623 packets/s
SHA1:                6703d741c6be2dfe78ad41a56559a2bfa8817b03
RIPEMD160:           8d1c5fa446a4f8fc168eacdc36648f28208ac55a
MD5:                 901c1a9b00e3df07098df1f3ca2762d5
Strict time order:   True
Number of interfaces in file: 1
Interface #0 info:
                     Name = UNKNOWN
                     Description = NONE
                     Encapsulation = Ethernet (1/1 - ether)
                     Speed = 18446744073709551615
                     Capture length = 262144
                     FCS length = -1
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Time resolution = 0x06
                     Filter string = NONE
                     Operating system = UNKNOWN
                     Comment = NONE
                     BPF filter length = 0
                     Number of stat entries = 0
                     Number of packets = 9000</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53108" class="comments-container"></div><div id="comment-tools-53108" class="comment-tools"></div><div class="clear"></div><div id="comment-53108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

