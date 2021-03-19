+++
type = "question"
title = "How to make a high level flow graph from a network capture"
description = '''Hello, I have a network capture that contains all the exchanges between a device and some remote servers, there are a lot of exchanges, on different destinations, on different protocols (ntp, http, https, etc.) and I would like to build a Flow Graph but at a macro level, that shows only the interact...'''
date = "2016-01-18T08:28:00Z"
lastmod = "2016-01-19T07:26:00Z"
weight = 49327
keywords = [ "174" ]
aliases = [ "/questions/49327" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to make a high level flow graph from a network capture](/questions/49327/how-to-make-a-high-level-flow-graph-from-a-network-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49327-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a network capture that contains all the exchanges between a device and some remote servers, there are a lot of exchanges, on different destinations, on different protocols (ntp, http, https, etc.) and I would like to build a Flow Graph but at a macro level, that shows only the interactions between my device and the remote servers. For instance one arrow that represents exchanges for NTP trafic between my device and destination A, if possible with FQDN and not with IP address, one arrow for HTTPS traffic exchanges with destination B, and so on. Is anybody knows how to achieve this ? Thanks in advance. Regards.<br />
</p></div><div id="question-tags" class="tags-container tags">174</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '16, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/4e1562eadfbc47cea9fac52608e6b9e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giraudeau&#39;s gravatar image" /><p>giraudeau<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giraudeau has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-49327" class="comments-container"></div><div id="comment-tools-49327" class="comment-tools"></div><div class="clear"></div><div id="comment-49327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49351"></span>

<div id="answer-container-49351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49351-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does <a href="http://www.ntop.org">ntop</a> help here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '16, 21:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-49351" class="comments-container"></div><div id="comment-tools-49351" class="comment-tools"></div><div class="clear"></div><div id="comment-49351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49372"></span>

<div id="answer-container-49372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49372-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a very similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/41185/how-can-i-draw-a-network-graph-with-wireshark">https://ask.wireshark.org/questions/41185/how-can-i-draw-a-network-graph-with-wireshark</a><br />
</p></blockquote><p>Plus:</p><blockquote><p><a href="http://visitrend.tumblr.com/post/127988124661/visitrend-vs-splunk-for-pcap-analytics">http://visitrend.tumblr.com/post/127988124661/visitrend-vs-splunk-for-pcap-analytics</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '16, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-49372" class="comments-container"></div><div id="comment-tools-49372" class="comment-tools"></div><div class="clear"></div><div id="comment-49372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

