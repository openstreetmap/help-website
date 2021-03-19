+++
type = "question"
title = "capturing clients talking to my dns server"
description = '''Can you show me a filter i can use to see who is looking at my server for DNS resolution. I have used tcp.port == 53 but need a more refined filter showing clients talking to the DNS server only. '''
date = "2012-04-27T11:10:00Z"
lastmod = "2012-04-30T09:32:00Z"
weight = 10490
keywords = [ "dns" ]
aliases = [ "/questions/10490" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [capturing clients talking to my dns server](/questions/10490/capturing-clients-talking-to-my-dns-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10490-score" class="post-score" title="current number of votes">0</div><span id="post-10490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can you show me a filter i can use to see who is looking at my server for DNS resolution. I have used tcp.port == 53 but need a more refined filter showing clients talking to the DNS server only.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '12, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/124addd1334f0cdf1f684a3815c5dfcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bilweiser&#39;s gravatar image" /><p><span>bilweiser</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bilweiser has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10490" class="comments-container"></div><div id="comment-tools-10490" class="comment-tools"></div><div class="clear"></div><div id="comment-10490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10491"></span>

<div id="answer-container-10491" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10491-score" class="post-score" title="current number of votes">0</div><span id="post-10491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about "ip.addr == 192.168.1.1 &amp;&amp; tcp.port == 53" but substitute the address of your DNS server in place of 192.168.1.1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '12, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-10491" class="comments-container"></div><div id="comment-tools-10491" class="comment-tools"></div><div class="clear"></div><div id="comment-10491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10521"></span>

<div id="answer-container-10521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10521-score" class="post-score" title="current number of votes">0</div><span id="post-10521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're looking for a capture filter, then something like this may narrow it down (assuming standard UDP to port 53 for DNS):</p><pre><code>&quot;(dst host 192.168.1.1 and udp dst port 53) or (src host 192.168.1.1 and udp src port 53)&quot;</code></pre><p>If it's a display filter, then something like this:</p><pre><code>(ip.dst==192.168.1.1 &amp;&amp; udp.dstport==53)||(ip.src==10.4.0.249&amp;&amp;udp.srcport==53)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/da397b10ce6b1b4fcc25764ce0c9e35a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rickg421&#39;s gravatar image" /><p><span>rickg421</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rickg421 has no accepted answers">0%</span></p></div></div><div id="comments-container-10521" class="comments-container"></div><div id="comment-tools-10521" class="comment-tools"></div><div class="clear"></div><div id="comment-10521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10527"></span>

<div id="answer-container-10527" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10527-score" class="post-score" title="current number of votes">0</div><span id="post-10527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark -n port 53 and dst 192.168.30.2</p><p>0.000000 192.168.30.148 -&gt; 192.168.30.2 DNS Standard query A <a href="http://www.leo.org">www.leo.org</a></p><p>Replace 192.168.30.2 with the ip address of your DNS server.</p><p>Alternatively: tshark -n -T text -E 'separator=;' -Tfields -e ip.src -e dns.qry.name port 53 and dst 192.168.30.2</p><p>192.168.30.148;<a href="http://www.leo.org">www.leo.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '12, 13:23</strong> </span></p></div></div><div id="comments-container-10527" class="comments-container"></div><div id="comment-tools-10527" class="comment-tools"></div><div class="clear"></div><div id="comment-10527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

