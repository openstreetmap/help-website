+++
type = "question"
title = "Ethernet Adapter not showing source capture"
description = '''When I use my Ethernet adapter to run a capture I get no source info from my Ethernet adapter. I receive capture information when my Ethernet adapter is the destination and when a broadcast comes to my adapter as the source. I&#x27;m using Windows 7 64bit. '''
date = "2015-02-26T08:43:00Z"
lastmod = "2015-02-26T08:56:00Z"
weight = 40100
keywords = [ "source", "outbound", "capture" ]
aliases = [ "/questions/40100" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet Adapter not showing source capture](/questions/40100/ethernet-adapter-not-showing-source-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40100-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I use my Ethernet adapter to run a capture I get no source info from my Ethernet adapter. I receive capture information when my Ethernet adapter is the destination and when a broadcast comes to my adapter as the source. I'm using Windows 7 64bit.</p></div><div id="question-tags" class="tags-container tags">source outbound capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '15, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/fa1d0ead7169c61a85dbddb17df4819d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hurleykyle&#39;s gravatar image" /><p>hurleykyle<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hurleykyle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '15, 14:00</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-40100" class="comments-container"><span id="40104"></span><div id="comment-40104" class="comment"><div id="post-40104-score" class="comment-score"></div><div class="comment-text"><p>"No Source info" does that mean no transmitted frames, only received frames?</p><p>Also please state Wireshark version.</p></div><div id="comment-40104-info" class="comment-info"><span class="comment-age">(26 Feb '15, 08:59)</span> Jaap ♦</div></div><span id="40106"></span><div id="comment-40106" class="comment"><div id="post-40106-score" class="comment-score"></div><div class="comment-text"><p>Yes, I'm not seeing my adapter as the source, but I see my adapter as the destination. Wireshark 1.12.3</p></div><div id="comment-40106-info" class="comment-info"><span class="comment-age">(26 Feb '15, 09:29)</span> hurleykyle</div></div></div><div id="comment-tools-40100" class="comment-tools"></div><div class="clear"></div><div id="comment-40100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40102"></span>

<div id="answer-container-40102" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40102-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at similar questions tagged "outbound" e.g. <a href="https://ask.wireshark.org/tags/outbound/">here</a>. The culprit is usually VPN or Endpoint protection software.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40102" class="comments-container"><span id="40126"></span><div id="comment-40126" class="comment"><div id="post-40126-score" class="comment-score"></div><div class="comment-text"><p>After installing sonic wall client on my PC the DNE Lightweight Filter feature had been added to my NIC. I unchecked this feature and now I can see my NIC as a source in my traces. Thanks...</p></div><div id="comment-40126-info" class="comment-info"><span class="comment-age">(27 Feb '15, 06:01)</span> hurleykyle</div></div><span id="40127"></span><div id="comment-40127" class="comment"><div id="post-40127-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40127-info" class="comment-info"><span class="comment-age">(27 Feb '15, 06:20)</span> grahamb ♦</div></div></div><div id="comment-tools-40102" class="comment-tools"></div><div class="clear"></div><div id="comment-40102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

