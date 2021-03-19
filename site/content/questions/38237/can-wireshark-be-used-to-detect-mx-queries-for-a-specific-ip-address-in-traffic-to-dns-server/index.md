+++
type = "question"
title = "Can Wireshark be used to detect mx queries  for a specific IP address in traffic  to dns server"
description = '''I suspect spam bot in the network and I had captured smtp traffic but could not find payload but just a reset from the external malicious ip address. I now want to check if it is querying the dns for a suspicious ip address so that i can get the hostname Please advise if wireshark can bet setup capt...'''
date = "2014-11-29T12:42:00Z"
lastmod = "2014-12-01T17:01:00Z"
weight = 38237
keywords = [ "query", "mx" ]
aliases = [ "/questions/38237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark be used to detect mx queries for a specific IP address in traffic to dns server](/questions/38237/can-wireshark-be-used-to-detect-mx-queries-for-a-specific-ip-address-in-traffic-to-dns-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38237-score" class="post-score" title="current number of votes">0</div><span id="post-38237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I suspect spam bot in the network and I had captured smtp traffic but could not find payload but just a reset from the external malicious ip address.</p><p>I now want to check if it is querying the dns for a suspicious ip address so that i can get the hostname</p><p>Please advise if wireshark can bet setup capture dns traffic with an mx query for specific ip in traffic to the dns server?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-mx" rel="tag" title="see questions tagged &#39;mx&#39;">mx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '14, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/06c15f5371b9ca5b8925a769727576e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shadyguy&#39;s gravatar image" /><p><span>Shadyguy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shadyguy has no accepted answers">0%</span></p></div></div><div id="comments-container-38237" class="comments-container"></div><div id="comment-tools-38237" class="comment-tools"></div><div class="clear"></div><div id="comment-38237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38238"></span>

<div id="answer-container-38238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38238-score" class="post-score" title="current number of votes">0</div><span id="post-38238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your question is unclear. If you already have the suspicious IP address and you want the associated host name, go <a href="http://remote.12dt.com/">here</a> to do a reverse DNS lookup. Enter the IP address in the input box and click "Lookup." Note that reverse lookups (IP address to host name) do not always succeed.</p><p>An MX lookup is done on a domain name, not an IP address, and it usually returns one or more host names, not IP addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '14, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-38238" class="comments-container"><span id="38241"></span><div id="comment-38241" class="comment"><div id="post-38241-score" class="comment-score"></div><div class="comment-text"><p>It does not give any results when doing a reverse lookup.</p><p>dnsqueries.com and virustotal show that there are several 1000 IP neighbours or domains hosted for the same ip address</p><p>I do not know which name the client is trying to query and hence i need to find that out</p><p>So, But back to my question. I have an bad IP eg 200.X.X.X , can i setup wireshark to detect any mx queries for domains for that IP address 200.X.X.X on email relay server</p></div><div id="comment-38241-info" class="comment-info"><span class="comment-age">(30 Nov '14, 07:35)</span> <span class="comment-user userinfo">Shadyguy</span></div></div><span id="38266"></span><div id="comment-38266" class="comment"><div id="post-38266-score" class="comment-score"></div><div class="comment-text"><blockquote><p>mx queries for domains for that IP address 200.X.X.X <strong>on email relay server</strong></p></blockquote><p>No, you can't detect MX queries (DNS traffic) on your mail server, unless that server is either your main internet router or also your DNS server and/or resolver.</p></div><div id="comment-38266-info" class="comment-info"><span class="comment-age">(01 Dec '14, 17:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-38238" class="comment-tools"></div><div class="clear"></div><div id="comment-38238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

