+++
type = "question"
title = "dns.time from FIRST DNS Request"
description = '''I am trying to track down the source of some browsing issues and I believe I have narrowed it down to a DNS issue. I can filter on a specific transaction ID and manually calculate the time between the first request and the reply, but I am looking for a way to automatically calculate the data and cre...'''
date = "2013-06-02T15:50:00Z"
lastmod = "2013-06-05T20:54:00Z"
weight = 21694
keywords = [ "dns.time", "dns", "time" ]
aliases = [ "/questions/21694" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dns.time from FIRST DNS Request](/questions/21694/dnstime-from-first-dns-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21694-score" class="post-score" title="current number of votes">0</div><span id="post-21694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to track down the source of some browsing issues and I believe I have narrowed it down to a DNS issue. I can filter on a specific transaction ID and manually calculate the time between the first request and the reply, but I am looking for a way to automatically calculate the data and create an IO graph. Using dns.time only shows the time since the last request and the reply, whereas I would like to see the time between the first request and reply. For example if a DNS request is retransmitted twice, the time from the first request to the reply may be 3.5 sec, but dns.time will show .5 sec since that is the amount of time since the last retransmission. Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns.time" rel="tag" title="see questions tagged &#39;dns.time&#39;">dns.time</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '13, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/f34d607a61f7d20195afc4c30ce6784d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Moran&#39;s gravatar image" /><p><span>John Moran</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Moran has no accepted answers">0%</span></p></div></div><div id="comments-container-21694" class="comments-container"></div><div id="comment-tools-21694" class="comment-tools"></div><div class="clear"></div><div id="comment-21694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21747"></span>

<div id="answer-container-21747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21747-score" class="post-score" title="current number of votes">0</div><span id="post-21747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try to create the required relation between the DNS request and the response with <a href="http://wiki.wireshark.org/Mate">MATE</a>, then add a field ('delta_time') and draw an I/O graph based on that field.</p><p>See also here:</p><blockquote><p><code>http://wiki.wireshark.org/Mate/Manual</code><br />
<code>http://wiki.wireshark.org/Mate/Library</code> (see DNS example)<br />
</p></blockquote><p>HOWEVER: MATE is quite complex ...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21747" class="comments-container"><span id="21785"></span><div id="comment-21785" class="comment"><div id="post-21785-score" class="comment-score"></div><div class="comment-text"><p>I'm wondering if, more simply, something like <code>tshark -R dns -T fields -e frame.time -e dns.id</code> could just be piped to an awk script to take first and last of each dns.id value, subtract min from max frame time in the corresponding column, and output the results in a time-sorted x;y format that you could then plot out of excel.</p><p>That's probably just a few lines of code. I might look at it tomorrow night but this should be relatively straightforward.</p></div><div id="comment-21785-info" class="comment-info"><span class="comment-age">(05 Jun '13, 20:54)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-21747" class="comment-tools"></div><div class="clear"></div><div id="comment-21747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

