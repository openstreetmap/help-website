+++
type = "question"
title = "How do I capture only VOIP packets, is there a filter option?"
description = '''I have magicjack set up on this machine and would like to capture VOIP packets, but usually I can only capture all packets and it captures a lot of other useless stuff like internet downloads and web pages and that sort of thing (this computer is used for web surfing as well as VOIP, its not a dedic...'''
date = "2011-07-06T09:36:00Z"
lastmod = "2011-07-06T14:37:00Z"
weight = 4929
keywords = [ "filter", "capture", "capture-filter", "voip" ]
aliases = [ "/questions/4929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I capture only VOIP packets, is there a filter option?](/questions/4929/how-do-i-capture-only-voip-packets-is-there-a-filter-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have magicjack set up on this machine and would like to capture VOIP packets, but usually I can only capture all packets and it captures a lot of other useless stuff like internet downloads and web pages and that sort of thing (this computer is used for web surfing as well as VOIP, its not a dedicated machine) I have some problems with the quality and want to analyze calls. Whenever a call comes in if I then start the capture it is too late somehow wireshark would not recognize it when I got o the voip decode... so therefore I need wireshark to be capturing always on BEFORE the calls come in for it to work. But without a way to filter out only VOIP packets it becomes quickly unmanageable.</p><p>Is there a way to set a filter in the capture to configure it to ONLY capture voip packets and filter it to not capture any of the other stuff?</p></div><div id="question-tags" class="tags-container tags">filter capture capture-filter voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '11, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/201c350e50bc8806cb05897e515214b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EAM&#39;s gravatar image" /><p>EAM<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EAM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jul '11, 09:37</p></div></div><div id="comments-container-4929" class="comments-container"></div><div id="comment-tools-4929" class="comment-tools"></div><div class="clear"></div><div id="comment-4929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4933"></span>

<div id="answer-container-4933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4933-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're looking at the signaling packets only <a href="http://en.wikibooks.org/wiki/MagicJack/Support_Resources/How-To/Proxy_Find2">this</a> page suggests a capture filter like</p><pre><code>udp port 5070</code></pre>But if you need to voice packets as well (which I suspect you do) there's no capture filter available to you. This is result of the fact that the voice packets are transported on an dynamic port number, and the capture filter cannot recognize RTP.<p>An other way to do this is to run dumpcap with a multiple file option. After your call pick up the capture file(s) you need and analyze them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4933" class="comments-container"><span id="4938"></span><div id="comment-4938" class="comment"><div id="post-4938-score" class="comment-score"></div><div class="comment-text"><p>It is possible that the RTP packets always appear on the same port(range) if that's the case you can filter on UDP and the port(range).</p></div><div id="comment-4938-info" class="comment-info"><span class="comment-age">(07 Jul '11, 01:32)</span> Anders ♦</div></div><span id="4943"></span><div id="comment-4943" class="comment"><div id="post-4943-score" class="comment-score"></div><div class="comment-text"><p>According to the MagicJack page that @Jaap linked the RTP port range is big (10000 to 30000). You might be able to match bits in the UDP payload that look like RTP, e.g. <code>udp[1] &amp; 1 != 1 &amp;&amp; udp[3] &amp; 1 != 1 &amp;&amp; udp[8] &amp; 0x80 == 0x80 &amp;&amp; length &lt; 250</code></p></div><div id="comment-4943-info" class="comment-info"><span class="comment-age">(07 Jul '11, 09:15)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-4933" class="comment-tools"></div><div class="clear"></div><div id="comment-4933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

