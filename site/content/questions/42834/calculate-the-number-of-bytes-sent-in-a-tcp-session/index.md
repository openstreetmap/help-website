+++
type = "question"
title = "Calculate the number of bytes sent in a tcp session"
description = '''I have been asked to find how many bytes were sent from the responder to the initiator of a TCP session on wireshark. any idea as to how this can be done? thank you!'''
date = "2015-06-02T18:48:00Z"
lastmod = "2015-06-03T02:31:00Z"
weight = 42834
keywords = [ "bytes", "tcp", "wireshark" ]
aliases = [ "/questions/42834" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate the number of bytes sent in a tcp session](/questions/42834/calculate-the-number-of-bytes-sent-in-a-tcp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42834-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been asked to find how many bytes were sent from the responder to the initiator of a TCP session on wireshark. any idea as to how this can be done?</p><p>thank you!</p></div><div id="question-tags" class="tags-container tags">bytes tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '15, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/6f3742ead9a38a8164e1edb9bfd44d53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amit%20Chauhan&#39;s gravatar image" /><p>Amit Chauhan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amit Chauhan has no accepted answers">0%</span></p></div></div><div id="comments-container-42834" class="comments-container"></div><div id="comment-tools-42834" class="comment-tools"></div><div class="clear"></div><div id="comment-42834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42835"></span>

<div id="answer-container-42835" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42835-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>1) Open the capture file and use filters to left only tcp packets from sender - you can use following string "ip.src=X.X.X.X&amp;&amp;tcp.len&gt;0" where X.X.X.X your server(sender) ip address</p><p>2) Save filtered file: save as -&gt; check checkbox "Displayed" -&gt; save</p><p>3) Check the size of resulting Wireshark file</p><p>If you are interested in only in clear payload size, than</p><p>4) Open resulting file</p><p>5) Check the total number of frames in it (just scroll down the file and check values in the first column)</p><p>6) Calculate total size of headers - multiply number of frames in capture by 54 (14 byte Ether header + 20 byte Ip header + 20 byte TCP header)**</p><p>7) Subtract from the total size of resulting file total size of headers the result will be payload size</p><p>** If captured packets contain MPLS headers, vlan tags, gre headers or any other additional headers add them to calculation of total size of headers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '15, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/4f86795c7a782fccae8a0b7bd270d1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mongolio&#39;s gravatar image" /><p>mongolio<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mongolio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jun '15, 20:39</p></div></div><div id="comments-container-42835" class="comments-container"></div><div id="comment-tools-42835" class="comment-tools"></div><div class="clear"></div><div id="comment-42835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42838"></span>

<div id="answer-container-42838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42838-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apply a display filter to show only packets from the sender, for example "ip.src==192.168.1.1". If there is more than one TCP conversation in the trace, add the stream index to the display filter so that you're seeing only packets from the sender on the conversation of interest, so something like: "ip.src==192.168.1.1 and tcp.stream==5".</p><p>To see total bytes transmitted, bring up the Summary dialog (Statistics &gt; Summary). Near the bottom, read the value for "Bytes" in the "Displayed" column. This is the total number of bytes transferred. It includes the Ethernet, IP, and TCP headers, and also the Ethernet Frame Check Sequence, if it is present in the trace. Not all systems pass the Frame Check Sequence to Wireshark, so it is often <em>not</em> present in the trace.</p><p>If you want to know only how many data bytes were transmitted, not including Ethernet, IP, or TCP headers, then make sure Wireshark's TCP preference "Relative sequence numbers" is enabled. (This is the default.) Go to the very last packet from the sender and see what the sequence number is. This is the total number of data bytes transferred.</p><p>When "Relative sequence numbers" is enabled, Wireshark makes the relative initial sequence number 0, regardless of what the actual absolute initial sequence number really is. The sender increments the sequence number by 1 for every byte of data transmitted, so the final sequence number is equal to the amount of data sent. (Ok, subtract one byte for the phantom byte during connection establishment if you want to be <em>really</em> accurate.)</p><p>Note that the sequence number is a finite number, so if enough data is transferred, eventually the sequence number will wrap around. This technnique assumes that the sequence number has not wrapped, which is usually true. The sequence number is a 32-bit number, so it takes 4 GB of data transfer before the sequence number wraps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-42838" class="comments-container"></div><div id="comment-tools-42838" class="comment-tools"></div><div class="clear"></div><div id="comment-42838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42839"></span>

<div id="answer-container-42839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42839-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd just open Statistics -&gt; Conversations, find the TCP conversation and read either Bytes A-&gt;B or the other way around, depending on what you're interested in. Of course that does includes all header overhead, so if you need data bytes, check Jim's answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42839" class="comments-container"></div><div id="comment-tools-42839" class="comment-tools"></div><div class="clear"></div><div id="comment-42839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

