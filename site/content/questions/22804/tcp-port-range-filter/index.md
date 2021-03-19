+++
type = "question"
title = "TCP port range filter"
description = '''Hello, How might I write a display filter for a tcp port range? I&#x27;m wanting to filter two sets of ranges. TCP/8600-8619 and TCP/8400-8402 thanks, J'''
date = "2013-07-10T06:43:00Z"
lastmod = "2015-11-25T11:49:00Z"
weight = 22804
keywords = [ "filter", "range", "tcp" ]
aliases = [ "/questions/22804" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TCP port range filter](/questions/22804/tcp-port-range-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22804-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>How might I write a display filter for a tcp port range?</p><p>I'm wanting to filter two sets of ranges. TCP/8600-8619 and TCP/8400-8402</p><p>thanks,</p><p>J</p></div><div id="question-tags" class="tags-container tags">filter range tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '13, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/791c3a844bb1629d3a685adab364e2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTech_17&#39;s gravatar image" /><p>JTech_17<br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTech_17 has no accepted answers">0%</span></p></div></div><div id="comments-container-22804" class="comments-container"></div><div id="comment-tools-22804" class="comment-tools"></div><div class="clear"></div><div id="comment-22804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22806"></span>

<div id="answer-container-22806" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22806-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p><code>(tcp.dstport &gt;= 8600 and tcp.dstport &lt;= 8619) or (tcp.dstport &gt;= 8400 and tcp.dstport &lt;= 8402)</code><br />
</p></blockquote><p>HINT: That will only show traffic in <strong>one direction</strong>, which is from client --&gt; server. However, that should be enough the figure out the tcp stream number, and then filter on that in a second step, possibly with tshark.</p><blockquote><p>tshark -nr input.pcap -R "(tcp.dstport &gt;= 8400 and tcp.dstport &lt;= 8402) or (tcp.dstport &gt;= 8400 and tcp.dstport &lt;= 8402)" -T fields -e tcp.stream | sort</p></blockquote><p>Then use that output and filter on tcp.stream</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '13, 07:20</p></div></div><div id="comments-container-22806" class="comments-container"><span id="22812"></span><div id="comment-22812" class="comment"><div id="post-22812-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the extra Tshark component, very nice.</p><p>J</p></div><div id="comment-22812-info" class="comment-info"><span class="comment-age">(10 Jul '13, 07:57)</span> JTech_17</div></div></div><div id="comment-tools-22806" class="comment-tools"></div><div class="clear"></div><div id="comment-22806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47992"></span>

<div id="answer-container-47992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With newer versions of libpcap (0.9.1 and later):</p><pre><code>(tcp portrange 8600-8619) or (tcp portrange 8400-8402)</code></pre><p>You can break it down further if you care about source or destination ports. As an example:</p><pre><code>(tcp dst portrange 8600-8619) or (tcp src portrange 8400-8402)</code></pre><p>More information can be found on the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">manpages</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/8ceec9f7f83e3c12a72b6442393bde2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwDevMan81&#39;s gravatar image" /><p>SwDevMan81<br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwDevMan81 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '15, 11:54</p></div></div><div id="comments-container-47992" class="comments-container"><span id="48013"></span><div id="comment-48013" class="comment"><div id="post-48013-score" class="comment-score"></div><div class="comment-text"><p>That's a capture filter, not a display filter; it's useful, but it doesn't solve this particular problem.</p></div><div id="comment-48013-info" class="comment-info"><span class="comment-age">(26 Nov '15, 13:44)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-47992" class="comment-tools"></div><div class="clear"></div><div id="comment-47992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

