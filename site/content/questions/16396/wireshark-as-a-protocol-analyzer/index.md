+++
type = "question"
title = "Wireshark as a Protocol Analyzer"
description = '''I was reading a Networking book that talks about packet sniffers and protocol analyzers. The book was basically saying these are two diffrent things but often get confused between one another. My question is; Is wireshark a Packet Sniffer or Protocol Analyzer or a combination of the two? I did also ...'''
date = "2012-11-28T10:34:00Z"
lastmod = "2012-11-28T11:35:00Z"
weight = 16396
keywords = [ "sniffer", "difference", "protocol", "analyzer", "packet" ]
aliases = [ "/questions/16396" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark as a Protocol Analyzer](/questions/16396/wireshark-as-a-protocol-analyzer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16396-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was reading a Networking book that talks about packet sniffers and protocol analyzers. The book was basically saying these are two diffrent things but often get confused between one another. My question is; Is wireshark a Packet Sniffer or Protocol Analyzer or a combination of the two? I did also read some products really are both a paket sniffer and protocol analyzer.<br />
</p><p>Thnak You.</p></div><div id="question-tags" class="tags-container tags">sniffer difference protocol analyzer packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '12, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/52857dcff5e05dba5f87f9670ead91b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="I_GEEK_IT&#39;s gravatar image" /><p>I_GEEK_IT<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="I_GEEK_IT has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '12, 11:41</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16396" class="comments-container"></div><div id="comment-tools-16396" class="comment-tools"></div><div class="clear"></div><div id="comment-16396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16398"></span>

<div id="answer-container-16398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16398-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question is; Is wireshark a Packet Sniffer or Protocol Analyzer or a combination of the two?</p></blockquote><p>It's both. Before you can analyze a protocol, you need to capture (sniff) some packets.</p><p>If you want to be really precise, then you would call Wireshark just a protocol analyzer, as the current version does not capture (sniff) the packets itself. It uses another tool, that is part of Wireshark: dumpcap. So one could say: dumpcap is the packet capture tool (the sniffer) and Wireshark is the analyzer.</p><blockquote><p>I did also read some products really are both a paket sniffer and protocol analyzer.</p></blockquote><p>most products (if not all) are a combination of both, due to what I said above.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '12, 11:40</p></div></div><div id="comments-container-16398" class="comments-container"></div><div id="comment-tools-16398" class="comment-tools"></div><div class="clear"></div><div id="comment-16398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

