+++
type = "question"
title = "Tshark filter on Time frames"
description = '''Hi All I am trying to filter on time frames with tshark and send output to a new pcap file. I can&#x27;t get this to work. I am on windows 8.1 pc.  Tshark filter i am trying to get to work: tshark -r d:&#92;PCAP-DUMP&#92;input.pcap -w d:&#92;PCAP-DUMP&#92;output.pcap -Y &quot;(frame.time &amp;gt;= &quot;Dec 29, 2014 19:00:00&quot;) &amp;amp;&amp;...'''
date = "2014-12-29T03:03:00Z"
lastmod = "2014-12-30T04:32:00Z"
weight = 38763
keywords = [ "tshark" ]
aliases = [ "/questions/38763" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark filter on Time frames](/questions/38763/tshark-filter-on-time-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38763-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All I am trying to filter on time frames with tshark and send output to a new pcap file. I can't get this to work. I am on windows 8.1 pc.</p><p>Tshark filter i am trying to get to work: tshark -r d:\PCAP-DUMP\input.pcap -w d:\PCAP-DUMP\output.pcap -Y "(frame.time &gt;= "Dec 29, 2014 19:00:00") &amp;&amp; (frame.time &lt;= "Dec 29, 2014 20:00:00") &amp;&amp; ip.addr == 192.168.1.1"</p><p>The filter (frame.time &gt;= "Dec 29, 2014 19:00:00") &amp;&amp; (frame.time &lt;= "Dec 29, 2014 20:00:00") &amp;&amp; ip.src == 192.168.10.30" works fine in wireshark.</p><p>Can anyone help me out here ? What am i doing wrong ?</p><p>Best Regards Lenny</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '14, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/ed681847f798a0cbb233ade06fdab318?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Netc&#39;s gravatar image" /><p>Netc<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Netc has no accepted answers">0%</span></p></div></div><div id="comments-container-38763" class="comments-container"></div><div id="comment-tools-38763" class="comment-tools"></div><div class="clear"></div><div id="comment-38763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38790"></span>

<div id="answer-container-38790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38790-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are experiencing a DOS box quoting problem, because of the way the DOS box is handling nested double quotes.</p><p>Please try this (using double double-quotes for the date):</p><blockquote><p>tshark -r d:\PCAP-DUMP\input.pcap -w d:\PCAP-DUMP\output.pcap -Y "(frame.time &gt;= ""Dec 29, 2014 19:00:00"") &amp;&amp; (frame.time &lt;= ""Dec 29, 2014 20:00:00"") &amp;&amp; ip.addr == 192.168.1.1"</p></blockquote><p>See also my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/29949/tshark-string">https://ask.wireshark.org/questions/29949/tshark-string</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Dec '14, 04:35</p></div></div><div id="comments-container-38790" class="comments-container"><span id="38851"></span><div id="comment-38851" class="comment"><div id="post-38851-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>Thanks..that solved my problem.</p><p>Best regards</p><p>Lenny Hansson</p><p>...Happy new year...</p></div><div id="comment-38851-info" class="comment-info"><span class="comment-age">(02 Jan '15, 02:11)</span> Netc</div></div><span id="38852"></span><div id="comment-38852" class="comment"><div id="post-38852-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38852-info" class="comment-info"><span class="comment-age">(02 Jan '15, 03:24)</span> grahamb ♦</div></div></div><div id="comment-tools-38790" class="comment-tools"></div><div class="clear"></div><div id="comment-38790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

