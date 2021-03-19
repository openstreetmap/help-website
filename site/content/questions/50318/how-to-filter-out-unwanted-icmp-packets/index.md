+++
type = "question"
title = "How to filter out unwanted ICMP packets?"
description = '''I have a specific RTP steam that --for whatever reason-- has ICMP packets that I do not want. Because of this I cannot properly decode the pcap and run the necessary scripts. What tshark command can be used to ensure that no ICMP (only UDP) packets are extracted from the raw initial packet capture? ...'''
date = "2016-02-18T17:27:00Z"
lastmod = "2016-02-18T19:59:00Z"
weight = 50318
keywords = [ "filter", "udp", "icmp", "pcap", "rtp" ]
aliases = [ "/questions/50318" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter out unwanted ICMP packets?](/questions/50318/how-to-filter-out-unwanted-icmp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50318-score" class="post-score" title="current number of votes">0</div><span id="post-50318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a specific RTP steam that --for whatever reason-- has ICMP packets that I do not want. Because of this I cannot properly decode the pcap and run the necessary scripts. What tshark command can be used to ensure that no ICMP (only UDP) packets are extracted from the raw initial packet capture?</p><p>I have attempted the following command to try and NOT read ICMP packets:</p><p>tshark -r raw.pcap -o rtp.heuristic_rtp:TRUE -2 -R rtp.ssrc==0x62bf9a1d -O "h264 &amp;&amp; not icmp" -w h264.pcap</p><p>...initially I had h264 alone. I have tried other filters like "-2 -R !icmp", "-2 -R not icmp". These do not work. Anyone know how to do this? In fact, not just for ICMP, how can I make sure I am ONLY getting UDP?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p><span>testname0110</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50318" class="comments-container"><span id="50321"></span><div id="comment-50321" class="comment"><div id="post-50321-score" class="comment-score"></div><div class="comment-text"><p>The ICMP packets most likely are "Destination Port Unreachable" replies to received RTP traffic before the RTP/UDP port is available/open. Normal condition.</p></div><div id="comment-50321-info" class="comment-info"><span class="comment-age">(18 Feb '16, 19:59)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-50318" class="comment-tools"></div><div class="clear"></div><div id="comment-50318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50319"></span>

<div id="answer-container-50319" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50319-score" class="post-score" title="current number of votes">1</div><span id="post-50319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="testname0110 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>-O</code> option only controls which protocols are expanded when displayed; it does <strong>not</strong> control which protocols are written to the output file or displayed. In fact, your usage of the <code>-O</code> option is wrong as it should be a comma-separated list of protocols you want expanded. See the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more information.</p><p>To achieve what you desire, try the following:</p><pre><code>tshark -r raw.pcap -o rtp.heuristic_rtp:TRUE -Y &quot;udp and !icmp&quot; -O &quot;h264&quot; -w h264.pcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50319" class="comments-container"></div><div id="comment-tools-50319" class="comment-tools"></div><div class="clear"></div><div id="comment-50319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

