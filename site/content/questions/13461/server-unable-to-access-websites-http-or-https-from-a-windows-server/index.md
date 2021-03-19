+++
type = "question"
title = "Server unable to access websites (HTTP or HTTPS) from a windows server"
description = '''Scenario. The customer has a number of server and workstations all of which go out through the same gateway firewall. One of the server is unable to access the internet via HTTP or HTTPS. I&#x27;ve tested different browsers and via telnet and I get the same results. SSH, DNS and everything else I&#x27;ve trie...'''
date = "2012-08-08T03:44:00Z"
lastmod = "2012-08-08T04:25:00Z"
weight = 13461
keywords = [ "rst", "ack", "http", "https" ]
aliases = [ "/questions/13461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Server unable to access websites (HTTP or HTTPS) from a windows server](/questions/13461/server-unable-to-access-websites-http-or-https-from-a-windows-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13461-score" class="post-score" title="current number of votes">0</div><span id="post-13461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Scenario. The customer has a number of server and workstations all of which go out through the same gateway firewall. One of the server is unable to access the internet via HTTP or HTTPS. I've tested different browsers and via telnet and I get the same results.</p><p>SSH, DNS and everything else I've tried works fine, just HTTP and HTTPS which fail.</p><p>Below is a capture from the server while I was attempting to browse to <a href="http://google.co.uk">google.co.uk</a> via its IP address. (I'm getting the same results when attempting to access any internet based webpage. I can access web pages on the local network fine.)</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
 124251 2119.040147 192.168.0.5           173.194.34.159        TCP      66     61952 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

No.     Time        Source                Destination           Protocol Length Info
 124313 2122.042518 192.168.0.5           173.194.34.159        TCP      66     61952 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1

No.     Time        Source                Destination           Protocol Length Info
 124411 2128.042411 192.168.0.5           173.194.34.159        TCP      62     61952 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1

No.     Time        Source                Destination           Protocol Length Info
 124952 2159.374787 173.194.34.159        192.168.0.5           TCP      60     http &gt; 61952 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre><p>Here's the traffic traversing the firewall.</p><p>13 08/08/2012 11:15:30.720 X0*(i) X1 192.168.0.5 173.194.34.159 IP TCP 61952,80 FORWARDED 66[66]</p><p>14 08/08/2012 11:15:33.720 X0*(i) X1 192.168.0.5 173.194.34.159 IP TCP 61952,80 FORWARDED 66[66]</p><p>15 08/08/2012 11:15:39.720 X0*(i) X1 192.168.0.5 173.194.34.159 IP TCP 61952,80 FORWARDED 62[62]</p><p>16 08/08/2012 11:16:11.064 -- X0*(s) 173.194.34.159 192.168.0.5 IP TCP 80,61952 GENERATED 54[54]</p><p>Can anyone point me in the right direction as to what's occurring here?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '12, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/9a681b257488a1a0aa7942f055e3cc9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aka-Goose&#39;s gravatar image" /><p><span>aka-Goose</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aka-Goose has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '12, 03:51</strong> </span></p></div></div><div id="comments-container-13461" class="comments-container"></div><div id="comment-tools-13461" class="comment-tools"></div><div class="clear"></div><div id="comment-13461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13463"></span>

<div id="answer-container-13463" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13463-score" class="post-score" title="current number of votes">1</div><span id="post-13463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can anyone point me in the right direction as to what's occurring here?</p></blockquote><p>Packets (SYN) are sent out, but no response comes back. Probably you forgot to add a NAT for your HTTP/HTTPS traffic (or for the server network) on the SonicWall.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '12, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '12, 04:02</strong> </span></p></div></div><div id="comments-container-13463" class="comments-container"><span id="13465"></span><div id="comment-13465" class="comment"><div id="post-13465-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Kurt, while not providing the exact answer you did point me in the right direction. There were a couple of dodge NAT rules which alter the port of the outbound traffic..</p><p>Many thanks.</p></div><div id="comment-13465-info" class="comment-info"><span class="comment-age">(08 Aug '12, 04:25)</span> <span class="comment-user userinfo">aka-Goose</span></div></div></div><div id="comment-tools-13463" class="comment-tools"></div><div class="clear"></div><div id="comment-13463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

