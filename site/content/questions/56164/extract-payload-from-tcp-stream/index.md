+++
type = "question"
title = "Extract payload from TCP stream"
description = '''I am using Wireshark to capture packets generated from my simulation testbed. I want to extract the payload from the frames and store them as a raw data or csv file to use them in my machine learning algorithm. My capturing is a set of streams so and I want the payload from each of them in a separat...'''
date = "2016-10-05T07:54:00Z"
lastmod = "2016-10-05T11:47:00Z"
weight = 56164
keywords = [ "wireshark-2.0", "payload", "tcp" ]
aliases = [ "/questions/56164" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extract payload from TCP stream](/questions/56164/extract-payload-from-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56164-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark to capture packets generated from my simulation testbed. I want to extract the payload from the frames and store them as a raw data or csv file to use them in my machine learning algorithm. My capturing is a set of streams so and I want the payload from each of them in a separate file without need to manually choose stream after stream. I tried (tcp.stream eq 4) but it is a laborious take to go one by one !! IS there a quick way?</p></div><div id="question-tags" class="tags-container tags">wireshark-2.0 payload tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '16, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/8ae96c2e250a39b926c2f332cbc790fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mraseeri&#39;s gravatar image" /><p>mraseeri<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mraseeri has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '16, 11:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56164" class="comments-container"><span id="56165"></span><div id="comment-56165" class="comment"><div id="post-56165-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I get you right. Are you interested in data from all packets of a single stream and you have a problem that you have to copy them packet by packet, or you have a hundred streams in your capture and you want the data from each of them in a separate file without need to manually choose stream after stream?</p></div><div id="comment-56165-info" class="comment-info"><span class="comment-age">(05 Oct '16, 08:30)</span> sindy</div></div><span id="56167"></span><div id="comment-56167" class="comment"><div id="post-56167-score" class="comment-score"></div><div class="comment-text"><p>Yes, I should've been clear in that. I have a set of streams and I want the data from each of them in a separate file without need to manually choose stream after stream. I'll update my question</p></div><div id="comment-56167-info" class="comment-info"><span class="comment-age">(05 Oct '16, 08:43)</span> mraseeri</div></div></div><div id="comment-tools-56164" class="comment-tools"></div><div class="clear"></div><div id="comment-56164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56169"></span>

<div id="answer-container-56169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56169-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To extract data from several distinct TCP streams in a capture file, one file per stream, you need to use scripting around tshark.</p><p>First, you would run</p><p><code>tshark -r "your/capture/file" -Y usb -z conv,tcp</code></p><p>and count the number of output lines to determine the total number of tcp sessions in the capture and store it to <code>sess_count</code>. The number of sessions is the number of lines minus 6 (the table header and footer). <code>-Y usb</code> is used to prevent any individual packets from being printed.</p><p>Next, you would run, in a <code>for (i=0,i &lt; sess_count,i++)</code> cycle:</p><p><code>tshark -r "your/capture/file" -Y usb -z follow,tcp,hex,$i &gt; session_$i.hex</code></p><p>The details can be found at <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page at Wireshark wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '16, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56169" class="comments-container"></div><div id="comment-tools-56169" class="comment-tools"></div><div class="clear"></div><div id="comment-56169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56171"></span>

<div id="answer-container-56171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56171-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try using <a href="https://linux.die.net/man/1/tcpflow">tcpflow</a>, it reads a pcap file and exports each tcp stream to a separate file of the form <code>192.168.101.102.02345-010.011.012.013.45103</code> where the contents of the file would be data transmitted from host 192.168.101.102 port 2345, to host 10.11.12.13 port 45103.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '16, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56171" class="comments-container"></div><div id="comment-tools-56171" class="comment-tools"></div><div class="clear"></div><div id="comment-56171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

