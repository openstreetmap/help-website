+++
type = "question"
title = "Need help interpreting DNS packets"
description = '''I&#x27;m in the process of troubleshooting an issue which is causing some slowness in establishing connections between our Linux servers. I&#x27;ve suspected DNS, but both forward and reverse lookups using dig are extremely fast. As a test I&#x27;ve been attempting to test a web connection between two Linux server...'''
date = "2010-10-21T12:03:00Z"
lastmod = "2014-01-12T11:49:00Z"
weight = 577
keywords = [ "dns" ]
aliases = [ "/questions/577" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Need help interpreting DNS packets](/questions/577/need-help-interpreting-dns-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-577-score" class="post-score" title="current number of votes">0</div><span id="post-577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm in the process of troubleshooting an issue which is causing some slowness in establishing connections between our Linux servers. I've suspected DNS, but both forward and reverse lookups using dig are extremely fast.</p><p>As a test I've been attempting to test a web connection between two Linux servers. At a prompt I attempt to telnet to port 80 on the other box. After about a 10 second delay a connection is established, entering GET / returns HTML very quickly. SSH exhibits the same symptoms, after about a 10 second delay in connecting the connection is fast.</p><p>I've taken some packet dumps using tcpdump and am viewing my findings in Wireshark. I can't explain the output, but it is consistent between multiple DNS servers.<br />
</p><p>When I enter the telnet command to connect to port 80 on the second machine I see the following exchange. Note: In this scenario I was attempting to connect from 10.3.1.171 to academic.luzerne.edu. I have a single DNS server listed in resolv.conf, 10.3.1.166. The command entered was telnet academic.luzerne.edu 80.</p><p>Source: 10.3.1.171 Dst: 10.3.1.166 Proto: DNS Info: Standard query AAAA academic.luzerne.edu</p><p>.002 second later the reply: Source: 10.3.1.166 Dst: 10.3.1.171 Proto: DNS Info: Standard query response</p><p>.0002 seconds later another request: Source: 10.3.1.171 Dst: 10.3.1.166 Proto: DNS Info: Standard query AAAA academic.luzerne.edu.luzerne.edu</p><p>Over 2 seconds later another request (after timeout?): Source: 10.3.1.171 Dst: 10.3.1.166 Proto: DNS Info: Standard query AAAA academic.luzerne.edu.luzerne.edu</p><p>Slightly over 5 seconds later another request: Source: 10.3.1.171 Dst: 10.3.1.166 Proto: DNS Info: Standard query AAAA academic.luzerne.edu</p><p>.0002 seconds later a valid reply: Source: 10.3.1.166 Dst: 10.3.1.171 Proto: DNS Info: Standard query response A 10.3.1.41</p><p>At this point the TCP handshake occurs and the connection proceeds. The DNS delay certainly explains the slowness in my connection.</p><p>I have no idea how to interpret this. Can any give me any suggestions?</p><p>Thanks, Bob</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '10, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/681ad6cfe5e18d5d6264b9d5f464690d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobd&#39;s gravatar image" /><p><span>bobd</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobd has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-577" class="comments-container"></div><div id="comment-tools-577" class="comment-tools"></div><div class="clear"></div><div id="comment-577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="582"></span>

<div id="answer-container-582" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-582-score" class="post-score" title="current number of votes">3</div><span id="post-582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it looks like your box is asking for an IPv6 DNS record (because you have the query type "AAAA" in your first couple of requests). For an IPv4 address you should have a query type of a single "A" instead. My guess is (and I'm no IPv6 specialist yet) that your box is first trying to get an IPv6 address, doesn't get any reply, retries a couple of times after some delay, and finally tries to ask for an IPv4 Address (as seen in your last Query statement). That one succeeds and the connection is established.</p><p>My tip: disable IPv6 or at least DNS lookups for IPv6 addresses, and everything should work as quickly as expected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-582" class="comments-container"><span id="602"></span><div id="comment-602" class="comment"><div id="post-602-score" class="comment-score"></div><div class="comment-text"><p>Thanks everyone! The problem was related to the IPv6. I've disabled it on our servers and speed is back to normal.</p><p>Thanks again, Bob</p></div><div id="comment-602-info" class="comment-info"><span class="comment-age">(23 Oct '10, 09:10)</span> <span class="comment-user userinfo">bobd</span></div></div><span id="28826"></span><div id="comment-28826" class="comment"><div id="post-28826-score" class="comment-score"></div><div class="comment-text"><p>very helpful for me , thank you ^^</p></div><div id="comment-28826-info" class="comment-info"><span class="comment-age">(12 Jan '14, 11:49)</span> <span class="comment-user userinfo">pcwalid</span></div></div></div><div id="comment-tools-582" class="comment-tools"></div><div class="clear"></div><div id="comment-582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="584"></span>

<div id="answer-container-584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-584-score" class="post-score" title="current number of votes">2</div><span id="post-584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That 2 seconds pause definitely looks like is a DNS-based timeout</p><p>Look at the difference in your DNS servers response: <em>First Request --&gt;</em> Info: Standard query AAAA academic.<strong>luzerne.edu</strong> .002 second later the reply: [...] Info: Standard query response &lt;-- some answer, look into it</p><p><em>Second Request --&gt;</em> .0002 seconds later Info: Standard query AAAA academic.<strong>luzerne.edu.luzerne.edu</strong></p><p>You see the "doubled" luzerne.edu -&gt; my tip is that there might be a small problem inside the zone file (Missing "." (dot) after some statement inside maybe, resulting in this strange second request. But that's only a guess... You should definitely look at the DNS response to the first request what the server tells you inside.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-584" class="comments-container"></div><div id="comment-tools-584" class="comment-tools"></div><div class="clear"></div><div id="comment-584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="592"></span>

<div id="answer-container-592" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-592-score" class="post-score" title="current number of votes">1</div><span id="post-592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper said, disabling IPv6 will likely fix your issue. You are having to wait for the AAAA (IPv6) query to timeout before the box tries a IPv4 AAA query.</p><p>However is you want to further eliminate DNS from the issue or do some comparison, you can access the server via IP address or put in static host entries to skip the DNS resolve on your test machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/1d8eda08758411bec29092a0b8220126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter&#39;s gravatar image" /><p><span>Peter</span><br />
<span class="score" title="65 reputation points">65</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter has no accepted answers">0%</span></p></div></div><div id="comments-container-592" class="comments-container"></div><div id="comment-tools-592" class="comment-tools"></div><div class="clear"></div><div id="comment-592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

