+++
type = "question"
title = "reason for warning ?"
description = '''Hello Friends. Also searching reason for below Warning   TCP: ACKed segment that wasn&#x27;t captured (common at capture start). HTTP: Unencrypted HTTP protocol detected over encrypted port, could indicate a dangerous misconfiguration&quot; '''
date = "2016-05-03T14:51:00Z"
lastmod = "2016-05-04T12:32:00Z"
weight = 52199
keywords = [ "warning_reason" ]
aliases = [ "/questions/52199" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [reason for warning ?](/questions/52199/reason-for-warning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52199-score" class="post-score" title="current number of votes">0</div><span id="post-52199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Friends.</p><p>Also searching reason for below Warning</p><ol><li>TCP: ACKed segment that wasn't captured (common at capture start).</li><li>HTTP: Unencrypted HTTP protocol detected over encrypted port, could indicate a dangerous misconfiguration"</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-warning_reason" rel="tag" title="see questions tagged &#39;warning_reason&#39;">warning_reason</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/ece77729d42d373e99fee1742f36bedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimmy2016&#39;s gravatar image" /><p><span>jimmy2016</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimmy2016 has no accepted answers">0%</span></p></div></div><div id="comments-container-52199" class="comments-container"></div><div id="comment-tools-52199" class="comment-tools"></div><div class="clear"></div><div id="comment-52199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52201"></span>

<div id="answer-container-52201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52201-score" class="post-score" title="current number of votes">1</div><span id="post-52201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1) The dissector saw an ACK in the TCP stream for a segment it didn't see come by in that stream. A common occurrence when a capture is started on an already opened TCP stream; the segment has gone by before the capture started, and once it was the ACK for that segment was captured.</p><p>2) TCP port 443 is associated with HTTPS. Seeing HTTP traffic on that port could be an indication of misconfiguration of the web server involved, serving unprotected content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52201" class="comments-container"><span id="52202"></span><div id="comment-52202" class="comment"><div id="post-52202-score" class="comment-score"></div><div class="comment-text"><p>hi,</p><p>Thanks for prompt reply !</p><p>What is the possible solution to fix the issue due point # 2 (2.HTTP: Unencrypted HTTP protocol detected over encrypted port, could indicate a dangerous misconfiguration")</p></div><div id="comment-52202-info" class="comment-info"><span class="comment-age">(03 May '16, 15:28)</span> <span class="comment-user userinfo">jimmy2016</span></div></div><span id="52234"></span><div id="comment-52234" class="comment"><div id="post-52234-score" class="comment-score"></div><div class="comment-text"><p>It depends on how the client has got the information that it should send HTTP requests to server tcp port 443 rather than the usual 80 or (also frequently used) 8080. If it was manually entered (<a href="http://my.site.org:443">http://my.site.org:443</a>), it is not a matter of configuration at all; if the client has first sent a DNS SRV query for the http service for that fqdn (which is rather a theoretical case), the DNS response could have indicated that port. Or the initial http request could have been sent to the "well-known" port 80 but the server (or load balancer in front of it) could have responded such a request with a 302 redirection, indicating a new url with "http://" (not "https://") but with port 443 specified.</p><p>The Wireshark capture should give you the answer which of the variants is true, as you should see there the whole process (the DNS query and response, the initial HTTP GET and the response to it, etc.)</p><p>Looking at both your Questions, they resemble a homework assignment to me.</p></div><div id="comment-52234-info" class="comment-info"><span class="comment-age">(04 May '16, 12:32)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52201" class="comment-tools"></div><div class="clear"></div><div id="comment-52201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

