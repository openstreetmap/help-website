+++
type = "question"
title = "How to filter all the TCP retransmission packets?"
description = '''Hi, I&#x27;m a college student studying wireless networking protocols. I want to filter all the TCP retransmission packets to calculate TCP retransmission rate. But my monitor mode Wireshark could only capture small fraction of all packets. I heard that filtering retransmitted TCP packet is done by tcp.a...'''
date = "2017-04-14T02:17:00Z"
lastmod = "2017-04-14T02:17:00Z"
weight = 60828
keywords = [ "filter", "frame", "802.11", "retransmissions", "tcp" ]
aliases = [ "/questions/60828" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter all the TCP retransmission packets?](/questions/60828/how-to-filter-all-the-tcp-retransmission-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60828-score" class="post-score" title="current number of votes">0</div><span id="post-60828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm a college student studying wireless networking protocols.</p><p>I want to filter all the TCP retransmission packets to calculate TCP retransmission rate. But my monitor mode Wireshark could only capture small fraction of all packets.</p><p>I heard that filtering retransmitted TCP packet is done by tcp.analysis.retransmission / tcp.analysis.fast_retransmission / tcp.analysis.spurious_retransmission filters but the filters are only look up sequence number of captured TCP packets.</p><p>So, the filters cannot be used in our test environment due to large loss rate on capturing packets..</p><p>But in 802.11 packet header, there is frame control field which contains retry flag which denotes retransmission. So, can I use 'wlan.fc.retry &amp;&amp; tcp' filter to filter retransmitted TCP packets?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '17, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/9c79dd2f8ef7fd4dc31511b1ef505e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jayheo&#39;s gravatar image" /><p><span>jayheo</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jayheo has no accepted answers">0%</span></p></div></div><div id="comments-container-60828" class="comments-container"></div><div id="comment-tools-60828" class="comment-tools"></div><div class="clear"></div><div id="comment-60828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

