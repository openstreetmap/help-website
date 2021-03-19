+++
type = "question"
title = "Not parsing the VJ Compressed Protocol packets"
description = '''We are currently working with Wireshark version 1.0.13 to parse &quot;PPP protocol&quot; over previously recorded pcap file. When we open our pcap file, &quot;PPP headers&quot; are recognized successfully, also &quot;PPP VJ uncompressed TCP&quot; data can be parsed successfully. On the other hand, &quot;VJ compressed TCP&quot; packets are...'''
date = "2011-03-07T00:26:00Z"
lastmod = "2011-03-07T18:33:00Z"
weight = 2688
keywords = [ "vj", "compressed", "uncompressed" ]
aliases = [ "/questions/2688" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not parsing the VJ Compressed Protocol packets](/questions/2688/not-parsing-the-vj-compressed-protocol-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2688-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are currently working with Wireshark version 1.0.13 to parse "PPP protocol" over previously recorded pcap file. When we open our pcap file, "PPP headers" are recognized successfully, also "PPP VJ <strong>uncompressed</strong> TCP" data can be parsed successfully. On the other hand, "VJ <strong>compressed</strong> TCP" packets are recognized but not parsed and defines them as "unknown direction".</p><p>Does it mean that my Wireshark can not parse those packets with "VJ Compressed TCP"?</p><p>I will send a screenshot from our findings so that you can easily observe what's going on if you ask for it.</p><p>Eager to wit for your answers,</p><p>With all best,</p></div><div id="question-tags" class="tags-container tags">vj compressed uncompressed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '11, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/fe5daaa697056b93697d7c0f2ab7e692?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chinar&#39;s gravatar image" /><p>Chinar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chinar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '11, 02:34</p></div></div><div id="comments-container-2688" class="comments-container"><span id="2695"></span><div id="comment-2695" class="comment"><div id="post-2695-score" class="comment-score"></div><div class="comment-text"><p>Try dropping the capture file in <a href="http://cloudshark.org/">CloudShark</a> and see what comes out.</p></div><div id="comment-2695-info" class="comment-info"><span class="comment-age">(07 Mar '11, 04:34)</span> Jaap ♦</div></div></div><div id="comment-tools-2688" class="comment-tools"></div><div class="clear"></div><div id="comment-2688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2705"></span>

<div id="answer-container-2705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, the compression is done separately for each direction of the PPP traffic, so Wireshark needs to be able to know which direction a packet is going in; not all capture file formats provide that information (and you can't use the source and destination IP addresses to determine that, as those addresses are compressed out of the packets). Pcap format, unfortunately, is one format that doesn't provide it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '11, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2705" class="comments-container"></div><div id="comment-tools-2705" class="comment-tools"></div><div class="clear"></div><div id="comment-2705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

