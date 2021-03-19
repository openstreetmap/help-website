+++
type = "question"
title = "how to select first N packets of flows?"
description = '''I have a pcap file that has 700 udp flows.  I want to select first N (say 5) packets of each flow and discard other packets of that flow and then merge them into 1 pcap. So the pcap file would have (700*5) packets and each 5 packets belong to one flow. Is there any program to do this?  If not, what&#x27;...'''
date = "2015-10-01T00:00:00Z"
lastmod = "2015-10-01T01:54:00Z"
weight = 46300
keywords = [ "pcap" ]
aliases = [ "/questions/46300" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to select first N packets of flows?](/questions/46300/how-to-select-first-n-packets-of-flows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46300-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file that has 700 udp flows.</p><p>I want to select first N (say 5) packets of each flow and discard other packets of that flow and then merge them into 1 pcap. So the pcap file would have (700*5) packets and each 5 packets belong to one flow.</p><p>Is there any program to do this?</p><p>If not, what's the easiest way to do it.</p><p>The OS i am using is Linux.</p></div><div id="question-tags" class="tags-container tags">pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '15, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/9e053a5f1fab9eb384815f14b62db05b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminSo&#39;s gravatar image" /><p>AminSo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminSo has no accepted answers">0%</span></p></div></div><div id="comments-container-46300" class="comments-container"></div><div id="comment-tools-46300" class="comment-tools"></div><div class="clear"></div><div id="comment-46300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46303"></span>

<div id="answer-container-46303" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46303-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use a script to filter the original capture file through tshark using filter 'udp.stream == x' where x is 0...699.</p><p>This gives you 700 individual capture files with one stream each. Then use editcap to shorten each to N packets.</p><p>This gives you 700 individual capture files with start start of one stream each. Then use mergecap to compile them into one capture file.</p><p>That's a basic approach, which may require fine tuning.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '15, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46303" class="comments-container"><span id="46304"></span><div id="comment-46304" class="comment"><div id="post-46304-score" class="comment-score"></div><div class="comment-text"><p>Thank u very much. i had such a idea but wasn't sure about it.</p></div><div id="comment-46304-info" class="comment-info"><span class="comment-age">(01 Oct '15, 02:00)</span> AminSo</div></div><span id="46305"></span><div id="comment-46305" class="comment"><div id="post-46305-score" class="comment-score"></div><div class="comment-text"><p>Just one thing. could you please write the tshark command that i should use? I wrote this:</p><p>tshark -r input.pcap -w output.pcap -R "udp.stream == 0"</p><p>it works but says: "-R without -2 is deprecated. For single-pass filtering use -Y"</p></div><div id="comment-46305-info" class="comment-info"><span class="comment-age">(01 Oct '15, 02:10)</span> AminSo</div></div><span id="46306"></span><div id="comment-46306" class="comment"><div id="post-46306-score" class="comment-score"></div><div class="comment-text"><p>By the way, "udp.stream" doesn't exist in wireshark. it has just tcp.stream</p></div><div id="comment-46306-info" class="comment-info"><span class="comment-age">(01 Oct '15, 02:28)</span> AminSo</div></div><span id="46308"></span><div id="comment-46308" class="comment"><div id="post-46308-score" class="comment-score"></div><div class="comment-text"><p>What's your Wireshark version? udp.stream was introduced by commit <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=7e0645563a2b91ea241eb89f5b97ee58924b6cb0">7e064556</a>, using <code>git tag --contains 7e064556</code> shows that the first stable version to include it was 1.12.0.</p></div><div id="comment-46308-info" class="comment-info"><span class="comment-age">(01 Oct '15, 03:57)</span> grahamb ♦</div></div><span id="46320"></span><div id="comment-46320" class="comment"><div id="post-46320-score" class="comment-score"></div><div class="comment-text"><p>Thanks. i have updated wireshark and it has now udp.stream</p></div><div id="comment-46320-info" class="comment-info"><span class="comment-age">(01 Oct '15, 11:50)</span> AminSo</div></div></div><div id="comment-tools-46303" class="comment-tools"></div><div class="clear"></div><div id="comment-46303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

