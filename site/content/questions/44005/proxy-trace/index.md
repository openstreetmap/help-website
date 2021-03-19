+++
type = "question"
title = "Proxy Trace"
description = '''Hi, I work in a corporate environment working with the usual firewalls and proxy servers. We have some MAC clients with a KACE agent installed on them which automates the downloading of updates etc.  The update server is hosted by a 3rd party so is not within our network. The KACE agent is unable to...'''
date = "2015-07-09T03:49:00Z"
lastmod = "2015-07-09T22:22:00Z"
weight = 44005
keywords = [ "proxy", "trace", "blocked" ]
aliases = [ "/questions/44005" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Proxy Trace](/questions/44005/proxy-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44005-score" class="post-score" title="current number of votes">0</div><span id="post-44005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I work in a corporate environment working with the usual firewalls and proxy servers. We have some MAC clients with a KACE agent installed on them which automates the downloading of updates etc.</p><p>The update server is hosted by a 3rd party so is not within our network. The KACE agent is unable to talk to the external update server. I can see the traffic going out in wireshark but I don't know how to read the information to see if its going through the proxy server or not.</p><p>I need to verify if both the outgoing and incoming trafffic is trying to access the internet directly without the proxy server.</p><p>All helpo appreciated.</p><p>Thank You</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/52fbaad415b5d136383353483142c255?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20W&#39;s gravatar image" /><p><span>Scott W</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott W has no accepted answers">0%</span></p></div></div><div id="comments-container-44005" class="comments-container"><span id="44015"></span><div id="comment-44015" class="comment"><div id="post-44015-score" class="comment-score"></div><div class="comment-text"><p>Could you share us a trace on dropbox, google, cloudshark or another publicity place?</p></div><div id="comment-44015-info" class="comment-info"><span class="comment-age">(09 Jul '15, 08:50)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-44005" class="comment-tools"></div><div class="clear"></div><div id="comment-44005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44029"></span>

<div id="answer-container-44029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44029-score" class="post-score" title="current number of votes">0</div><span id="post-44029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need to verify if both the outgoing and incoming trafffic is trying to access the internet directly without the proxy server.</p></blockquote><p>If the destination address is an address of your local network (RFC-1918, 192.168.x.x, 10.x.x.x, etc.) then it's a proxy connection. You'll then often also see the typical TCP proxy ports (3218, 8000,8080, etc.).</p><p>If the destination IP address is an address on the internet, it's either a direct connection or the connection is 'intercepted' by a transparent proxy at the gateway. You can't easily determine in a capture file if a transparent proxy is being used. Inter frame time delta could be a sign for it, but that's not reliable.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '15, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44029" class="comments-container"></div><div id="comment-tools-44029" class="comment-tools"></div><div class="clear"></div><div id="comment-44029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

