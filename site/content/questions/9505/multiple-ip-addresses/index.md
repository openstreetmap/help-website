+++
type = "question"
title = "multiple ip addresses"
description = '''I tried to capture traffic to a site with multiple ip addresses, and got very few results. Obviously, if I state a pcap filter like &quot;host facebook.com&quot;, this creates a filter with one ip address returned from dns at the time I start the capture. How should I capture that traffic correctly?'''
date = "2012-03-13T00:18:00Z"
lastmod = "2012-03-16T23:17:00Z"
weight = 9505
keywords = [ "multiple-ip" ]
aliases = [ "/questions/9505" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [multiple ip addresses](/questions/9505/multiple-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9505-score" class="post-score" title="current number of votes">0</div><span id="post-9505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to capture traffic to a site with multiple ip addresses, and got very few results. Obviously, if I state a pcap filter like "host <a href="http://facebook.com">facebook.com</a>", this creates a filter with one ip address returned from dns at the time I start the capture. How should I capture that traffic correctly?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple-ip" rel="tag" title="see questions tagged &#39;multiple-ip&#39;">multiple-ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '12, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/2a0d9f17afa936fe9558e9e32ba91b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wurzelsepp&#39;s gravatar image" /><p><span>Wurzelsepp</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wurzelsepp has no accepted answers">0%</span></p></div></div><div id="comments-container-9505" class="comments-container"></div><div id="comment-tools-9505" class="comment-tools"></div><div class="clear"></div><div id="comment-9505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9507"></span>

<div id="answer-container-9507" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9507-score" class="post-score" title="current number of votes">1</div><span id="post-9507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could create a filter with all IP addresses that are involved, like "host 1.2.3.4 or 1.2.3.5 or 1.2.3.6" etc, but that would require you to already know which IPs will be contacted (which you usually don't, especially not for large scale websites that link to tons of external resources).</p><p>A better approach might be not to filter on anything and capture it all, and then making sure that the client will only communicate with the website you want - meaning: shut down all other programs that could add packets to the capture and only run the one client program (in your case probably the web browser) which is necessary to access the ressource.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '12, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9507" class="comments-container"></div><div id="comment-tools-9507" class="comment-tools"></div><div class="clear"></div><div id="comment-9507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9517"></span>

<div id="answer-container-9517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9517-score" class="post-score" title="current number of votes">1</div><span id="post-9517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Obviously, if I state a pcap filter like "host <a href="http://facebook.com">facebook.com</a>", this creates a filter with one ip address returned from dns at the time I start the capture.</p></blockquote><p>Actually, no, it doesn't, because DNS returns multiple IP addresses for <a href="http://facebook.com">facebook.com</a>:</p><pre><code>$ host facebook.com
facebook.com has address 66.220.149.11
facebook.com has address 69.171.224.11
facebook.com has address 69.171.229.11
facebook.com mail is handled by 10 smtpin.mx.facebook.com.
$ tcpdump -i en0 -d ip host facebook.com
tcpdump: WARNING: en0: no IPv4 address assigned
(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 11
(002) ld       [26]
(003) jeq      #0x45abe50b      jt 10   jf 4
(004) jeq      #0x42dc950b      jt 10   jf 5
(005) jeq      #0x45abe00b      jt 10   jf 6
(006) ld       [30]
(007) jeq      #0x45abe50b      jt 10   jf 8
(008) jeq      #0x42dc950b      jt 10   jf 9
(009) jeq      #0x45abe00b      jt 10   jf 11
(010) ret      #65535
(011) ret      #0</code></pre><p>(I used "ip host" rather than "host" to eliminate distracting BPF code that also checks for ARP packets.) Note that it's checking for all three IP addresses as both source and destination addresses.</p><p>If the site's DNS entry has multiple IP addresses, all of them will be checked for. If, however, the DNS server only returns one IP address at a time, and returns different IP addresses for different requests, you would need to get a complete list of all its IP addresses and construct the filter by hand, e.g.</p><pre><code>host 66.120.149.11 or host 69.171.224.11 or host 69.171.229.11</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '12, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9517" class="comments-container"><span id="9530"></span><div id="comment-9530" class="comment"><div id="post-9530-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I will try with the 3 addresses found for <a href="http://facebook.com">facebook.com</a> and one more for <a href="http://www.facebook.com">www.facebook.com</a>. However, there are certainly services which use many more IP addresses than just 3 or 4. I once tried to understand the traffic generated by a single windows machine, and it turned out that it was talking to a multitude of kaspersky-related sites. At that time I would have liked to capture "not host <em>.kaspersky.</em>" <span>@Jasper</span>: sometimes it is hardly possible to observe a system in isolation....</p></div><div id="comment-9530-info" class="comment-info"><span class="comment-age">(13 Mar '12, 22:23)</span> <span class="comment-user userinfo">Wurzelsepp</span></div></div><span id="9531"></span><div id="comment-9531" class="comment"><div id="post-9531-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, <code>not host .kaspersky.com</code> (which is what I assume you meant) would be <em>EXTREMELY</em> difficult, if not impossible, to implement. It would probably require a zone transfer of <em>all</em> A and AAAA or A6 or whatever they're called records from the <a href="http://kaspersky.com">kaspersky.com</a> domain and construct a large and complicated BPF program that is <code>not host</code> <em>first</em> <code>and not host</code> <em>second</em> <code>and</code>...</p><p>If a given <em>DNS host name</em> has many more IP addresses than just 3 or 4, that's not, in principle, a problem, as long as a DNS query for that host name returns all the IP addresses.</p></div><div id="comment-9531-info" class="comment-info"><span class="comment-age">(13 Mar '12, 22:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9591"></span><div id="comment-9591" class="comment"><div id="post-9591-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>my current problem (facebook) seems to be solved with the four ip addresses (3 for <a href="http://facebook.com">facebook.com</a> and another one for <a href="http://www.facebook.com">www.facebook.com</a>) There are, however, hosts where dns , at any moment in time, only annonces part of the available addresses. So I had the vague idea that a listener might follow dns traffic and then readjust the pcap filter</p></div><div id="comment-9591-info" class="comment-info"><span class="comment-age">(16 Mar '12, 22:41)</span> <span class="comment-user userinfo">Wurzelsepp</span></div></div><span id="9593"></span><div id="comment-9593" class="comment"><div id="post-9593-score" class="comment-score"></div><div class="comment-text"><p>It might be possible to write such a listener, although it wouldn't be able to instantly readjust the filter, so there would be a window in which traffic to the new IP address might be missed.</p><p>In any case, neither tcpdump nor Wireshark are such a listener, and neither is likely to become one any time soon.</p></div><div id="comment-9593-info" class="comment-info"><span class="comment-age">(16 Mar '12, 23:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9517" class="comment-tools"></div><div class="clear"></div><div id="comment-9517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

