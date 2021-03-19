+++
type = "question"
title = "Server Based Application Dissectors"
description = '''Hello, My co-worker and I are tasked with building dissectors for our firms protocols. My coworker is doing the coding. He has the development build installed We assign a port range to each of our customers. From which they can access multiple applications residing on multiple servers. These protoco...'''
date = "2016-05-20T07:13:00Z"
lastmod = "2016-05-20T08:35:00Z"
weight = 52804
keywords = [ "application", "server", "based", "dissectors" ]
aliases = [ "/questions/52804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Server Based Application Dissectors](/questions/52804/server-based-application-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52804-score" class="post-score" title="current number of votes">0</div><span id="post-52804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, My co-worker and I are tasked with building dissectors for our firms protocols. My coworker is doing the coding. He has the development build installed We assign a port range to each of our customers. From which they can access multiple applications residing on multiple servers. These protocols are either tcp or udp. Meaning the dissectors need to be created based on an IP range and a Port Range.<br />
I know this is not a supported function of WS, but does anyone have an idea on how to work around this to create these Server Based Application Dissectors?</p><p>thanks Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-based" rel="tag" title="see questions tagged &#39;based&#39;">based</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '16, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/575922bd3f5d72b465eac18a045acfd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve_merc&#39;s gravatar image" /><p><span>steve_merc</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve_merc has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '16, 07:14</strong> </span></p></div></div><div id="comments-container-52804" class="comments-container"><span id="52805"></span><div id="comment-52805" class="comment"><div id="post-52805-score" class="comment-score">1</div><div class="comment-text"><p>Not sure I quite understand the issue here. Are you saying that the protocols used depend on both IP and port?</p><p>Do the protocols have any magic identifiers so that they could be used heuristically? If so, then you don't need to register per port, just heuristically and check the traffic and return 0 if not your protocol.</p></div><div id="comment-52805-info" class="comment-info"><span class="comment-age">(20 May '16, 07:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52806"></span><div id="comment-52806" class="comment"><div id="post-52806-score" class="comment-score">1</div><div class="comment-text"><p>Can the PDUs of these protocols be identified based on their contents as well, particularly the first couple of bytes? Then you could go the route of heuristic dissectors, which can get all packets of your particular transport (TCP, UDP, etc) and can then determine if it's their protocol.</p></div><div id="comment-52806-info" class="comment-info"><span class="comment-age">(20 May '16, 07:54)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52807"></span><div id="comment-52807" class="comment"><div id="post-52807-score" class="comment-score"></div><div class="comment-text"><p>Grahamb, Yes these are based on both IP and Port. Each customer is assigned a range of tcp 30 Ports to access multiple applications residing on different servers. I was mistaken this would be only for TCP traffic. Our UDP is outbound to customers on a specific port per application (much easier)!</p><p>JAAP, There is not always the same data after the TCP header. IE FIX or our proprietary session management protocol (which has many child apps under it)... I think what you are saying to instead of defining them by the app server ip, to build dissectors for each child of TCP. If so, since they would be using a non standard port range, is it possible to define a port range? ty Steve</p></div><div id="comment-52807-info" class="comment-info"><span class="comment-age">(20 May '16, 08:18)</span> <span class="comment-user userinfo">steve_merc</span></div></div></div><div id="comment-tools-52804" class="comment-tools"></div><div class="clear"></div><div id="comment-52804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52809"></span>

<div id="answer-container-52809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52809-score" class="post-score" title="current number of votes">1</div><span id="post-52809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><span>@steve_merc</span>,</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>Dissectors can register for a port range, see README.dissector section 1.7.1 and the dissector_add_uint_range() registration call.</p><p>I'm still of a mind that using a heuristic approach would be easier though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '16, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52809" class="comments-container"></div><div id="comment-tools-52809" class="comment-tools"></div><div class="clear"></div><div id="comment-52809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

