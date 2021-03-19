+++
type = "question"
title = "Is there any difference between libpcap&#x27;s Packet buffer and wireshark&#x27;s tvbuff"
description = '''Is there any difference between libpcap&#x27;s Packet buffer and wireshark&#x27;s tvbuff ???'''
date = "2012-11-23T04:21:00Z"
lastmod = "2012-11-23T11:19:00Z"
weight = 16241
keywords = [ "tvbuff_t" ]
aliases = [ "/questions/16241" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any difference between libpcap's Packet buffer and wireshark's tvbuff](/questions/16241/is-there-any-difference-between-libpcaps-packet-buffer-and-wiresharks-tvbuff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16241-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any difference between libpcap's Packet buffer and wireshark's tvbuff ???</p></div><div id="question-tags" class="tags-container tags">tvbuff_t</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '12, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p>Akhil<br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '12, 09:26</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16241" class="comments-container"></div><div id="comment-tools-16241" class="comment-tools"></div><div class="clear"></div><div id="comment-16241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16258"></span>

<div id="answer-container-16258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16258-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>as that's totally different data structures, it might be better to ask if there is anything they have in common ;-).</p><p>The only two things I can see:</p><ul><li>they are both data structures that hold the bytes of network packets (somewhere in the data structure)</li><li>the language used is C</li></ul><p>What's the background of your question?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '12, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16258" class="comments-container"><span id="16290"></span><div id="comment-16290" class="comment"><div id="post-16290-score" class="comment-score"></div><div class="comment-text"><p>1.)Does both the buffers for a single packet point to the same memory location? 2.)Can wireshark dissector process packet buffer?</p></div><div id="comment-16290-info" class="comment-info"><span class="comment-age">(25 Nov '12, 20:03)</span> Akhil</div></div><span id="16297"></span><div id="comment-16297" class="comment"><div id="post-16297-score" class="comment-score"></div><div class="comment-text"><p>1)No</p><p>2)? Wireshark reads from a file and "loads" the data into a tvb.</p></div><div id="comment-16297-info" class="comment-info"><span class="comment-age">(26 Nov '12, 01:36)</span> Anders ♦</div></div><span id="16342"></span><div id="comment-16342" class="comment"><div id="post-16342-score" class="comment-score"></div><div class="comment-text"><p>1)Then what is the role of packet buffer?</p><p>2)From where does the packet comes into the file?</p><p>3)what is the name of the file?</p></div><div id="comment-16342-info" class="comment-info"><span class="comment-age">(26 Nov '12, 19:43)</span> Akhil</div></div><span id="16345"></span><div id="comment-16345" class="comment"><div id="post-16345-score" class="comment-score"></div><div class="comment-text"><p>1)You should ask the libpcap people that :-) <a href="http://www.tcpdump.org/pcap3_man.html">http://www.tcpdump.org/pcap3_man.html</a></p><p>2)Somthing like this, but you should read the code to find out. Libpcap/WinPcap-&gt;dumpcap-&gt;"file"-&gt;Wireshark</p><p>3) It's a temp file with a unique file name prefixed with WS You can find the location from the menu bar help-&gt;About folders.</p></div><div id="comment-16345-info" class="comment-info"><span class="comment-age">(27 Nov '12, 00:14)</span> Anders ♦</div></div></div><div id="comment-tools-16258" class="comment-tools"></div><div class="clear"></div><div id="comment-16258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

