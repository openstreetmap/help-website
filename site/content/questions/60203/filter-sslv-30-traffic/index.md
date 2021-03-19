+++
type = "question"
title = "Filter SSLv 3.0 traffic"
description = '''Is there any way we can filter only SSLv3.0 traffic from a capture?'''
date = "2017-03-20T14:46:00Z"
lastmod = "2017-03-20T15:34:00Z"
weight = 60203
keywords = [ "filter", "protocol", "sslv3" ]
aliases = [ "/questions/60203" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter SSLv 3.0 traffic](/questions/60203/filter-sslv-30-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60203-score" class="post-score" title="current number of votes">0</div><span id="post-60203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way we can filter only SSLv3.0 traffic from a capture?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-sslv3" rel="tag" title="see questions tagged &#39;sslv3&#39;">sslv3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '17, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/9a8cace9c1d4bf4f790328ca93e8c58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WireSharrkUser&#39;s gravatar image" /><p><span>WireSharrkUser</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WireSharrkUser has no accepted answers">0%</span></p></div></div><div id="comments-container-60203" class="comments-container"></div><div id="comment-tools-60203" class="comment-tools"></div><div class="clear"></div><div id="comment-60203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60204"></span>

<div id="answer-container-60204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60204-score" class="post-score" title="current number of votes">1</div><span id="post-60204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a bit more complicated than usual to do this, because you need to do it in two steps. First, you need to find all conversations that use SSLv3, gathering their tcp stream indexes. In a second run, filter those away (or everything else, depending on what you mean by "filter only SSLv3").</p><p>Example, filtering on Handshakes (content_type 22) from the server (handshake type 2) and SSL version 3 (version 0x0300:</p><pre><code>tshark -r demo.pcapng -Y &quot;ssl and ssl.record.content_type == 22 and ssl.handshake.type == 2 and ssl.record.version == 0x0300&quot; -Tfields -e tcp.stream
7672
10374
10858
11509</code></pre><p>Second, run tshark again (or use Wireshark to load your pcap), and filter on the stream indexes:</p><pre><code>tcp.stream==7672 or tcp.stream==10374 or tcp.stream==10858 or tcp.stream==11509</code></pre><p>If you <strong>don't</strong> want to see the SSLv3 flows, negate the filter:</p><pre><code>not (tcp.stream==7672 or tcp.stream==10374 or tcp.stream==10858 or tcp.stream==11509)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '17, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60204" class="comments-container"></div><div id="comment-tools-60204" class="comment-tools"></div><div class="clear"></div><div id="comment-60204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

