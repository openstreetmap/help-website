+++
type = "question"
title = "Slow Transfer, Dup Ack, Packets out of order - Only one direction"
description = '''I have a client that I am seeing very weird behavior on their network. When I transfer data TO the site in Phoenix across the MPLS everything is great, full bandwidth beautiful packet captures. When I transfer data FROM the Phoenix site across the MPLS I get 1/3 bandwidth and ugly packet captures, m...'''
date = "2016-05-12T09:42:00Z"
lastmod = "2016-06-04T14:11:00Z"
weight = 52475
keywords = [ "dup-ack", "slow", "tcp-out-of-order" ]
aliases = [ "/questions/52475" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Slow Transfer, Dup Ack, Packets out of order - Only one direction](/questions/52475/slow-transfer-dup-ack-packets-out-of-order-only-one-direction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52475-score" class="post-score" title="current number of votes">0</div><span id="post-52475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client that I am seeing very weird behavior on their network. When I transfer data TO the site in Phoenix across the MPLS everything is great, full bandwidth beautiful packet captures. When I transfer data FROM the Phoenix site across the MPLS I get 1/3 bandwidth and ugly packet captures, missed packets, 100s of DUP ACKS and packets out of order.</p><p>I don't see anything wrong with layer 1, 2, or 3, but I have seen that the window size tanks pretty early on the transfers FROM Phoenix. I've got packet captures, I'll get them posted here shortly.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-tcp-out-of-order" rel="tag" title="see questions tagged &#39;tcp-out-of-order&#39;">tcp-out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/0f30104fd8f4591ab7bdd587835b0d78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NoanCares&#39;s gravatar image" /><p><span>NoanCares</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NoanCares has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 May '16, 10:46</strong> </span></p></div></div><div id="comments-container-52475" class="comments-container"></div><div id="comment-tools-52475" class="comment-tools"></div><div class="clear"></div><div id="comment-52475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52491"></span>

<div id="answer-container-52491" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52491-score" class="post-score" title="current number of votes">0</div><span id="post-52491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It could be either a MPLS routing issue or perhaps a load balancer issue.</p><p>Perform tracert and tracetcp (including port number) and compare. Do this on both sides to see if there are any route differences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '16, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-52491" class="comments-container"></div><div id="comment-tools-52491" class="comment-tools"></div><div class="clear"></div><div id="comment-52491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53203"></span>

<div id="answer-container-53203" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53203-score" class="post-score" title="current number of votes">0</div><span id="post-53203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've sent a traceroute over to the ISP and they confirmed that it is going over the correct path, even though they do show differently. I paid for a subscription to cloudshark so that I could upload these.</p><p>I did a port span on the switch because I wasn't sure the test machine had enough CPU to capture and process the iPerf test.</p><p>When the client is in San Diego sending to the iperf server in Scottsdale everything is beautiful. <a href="https://www.cloudshark.org/captures/6c93d681ff72">https://www.cloudshark.org/captures/6c93d681ff72</a></p><p>When the client is in Scottsdale sending to San Diego, it all goes to crap. <a href="https://www.cloudshark.org/captures/93d5799d876b">https://www.cloudshark.org/captures/93d5799d876b</a></p><p>Just for posterity here are the paths that I show across the MPLS as well.</p><pre><code> San Diego Network to Scottsdale Network
  1     1 ms    &lt;1 ms    &lt;1 ms  192.168.1.2
  2     8 ms     7 ms     8 ms  10.67.1.61
  3    22 ms    19 ms    20 ms  82.197.9.72.static.ip.tnltd.net [72.9.197.82]
  4    20 ms    20 ms    19 ms  10.251.27.216.static.ip.tnltd.net [216.27.251.10]
  5    19 ms    19 ms    19 ms  server.scottsdale [192.168.0.19]

Scottsdale to San Diego Network
  1     1 ms     1 ms     1 ms  192.168.0.1
  2    &lt;1 ms    &lt;1 ms    &lt;1 ms  192.168.0.2
  3     2 ms     2 ms     2 ms  10.254.4.201
  4     *        *        *     Request timed out.
  5     *        *        *     Request timed out.
  6    12 ms    11 ms    11 ms  10.67.1.61
  7    19 ms    19 ms    19 ms  10.67.1.62
  8    19 ms    20 ms    19 ms  server.san.diego [192.168.1.6]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '16, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/0f30104fd8f4591ab7bdd587835b0d78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NoanCares&#39;s gravatar image" /><p><span>NoanCares</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NoanCares has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jun '16, 14:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53203" class="comments-container"></div><div id="comment-tools-53203" class="comment-tools"></div><div class="clear"></div><div id="comment-53203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

