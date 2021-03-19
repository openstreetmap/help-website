+++
type = "question"
title = "Register dissector without particularities"
description = '''I would know if it&#x27;s possible to register a dissector for a protocol which hasn&#x27;t particularities, neither fields nor ports are usable to determine the dissector to use. The only particularity it&#x27;s the use of udp protocol. In the same idea, Is it possible to register a subdissector for a protocol wh...'''
date = "2011-03-27T13:31:00Z"
lastmod = "2011-03-27T15:42:00Z"
weight = 3159
keywords = [ "development", "dissector", "sub-dissector" ]
aliases = [ "/questions/3159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Register dissector without particularities](/questions/3159/register-dissector-without-particularities)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3159-score" class="post-score" title="current number of votes">0</div><span id="post-3159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would know if it's possible to register a dissector for a protocol which hasn't particularities, neither fields nor ports are usable to determine the dissector to use. The only particularity it's the use of udp protocol.</p><p>In the same idea, Is it possible to register a subdissector for a protocol which can use one ore more upper protocol, without to precise a port or a field?</p><p>Thank</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '11, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/a8e5c9438725b82bdee34d32a2068b80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chronidev&#39;s gravatar image" /><p><span>chronidev</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chronidev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Mar '11, 13:31</strong> </span></p></div></div><div id="comments-container-3159" class="comments-container"></div><div id="comment-tools-3159" class="comment-tools"></div><div class="clear"></div><div id="comment-3159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3164"></span>

<div id="answer-container-3164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3164-score" class="post-score" title="current number of votes">2</div><span id="post-3164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If your dissector can look at the payload of a UDP datagram and figure out if it's a packet for your protocol or not, you should make it a heuristic dissector. See the "README.heuristic" file in the doc subdirectory of the Wireshark source. If that's not possible, either give it a preference for the port to use, so the user can specify whatever port it happens to use in a particular capture, or register it as a "generic" dissector atop UDP, with "dissector_add_handle()", using "udp.port" as the dissector table name, which will allow the user to use the "Decode As..." menu to choose a particular port in a particular capture.</p><p>And, yes, it's possible to register a dissector in more than one dissector table; for example, the DNS dissector registers both atop UDP and atop TCP, and the IPv4 and IPv6 dissectors register atop many different link-layer protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3164" class="comments-container"><span id="3167"></span><div id="comment-3167" class="comment"><div id="post-3167-score" class="comment-score"></div><div class="comment-text"><p>Finally I found a way to do what I want. I just register the dissector, then I use the user preferences to activate or desactivate the dissector, with user preferences udp port.</p></div><div id="comment-3167-info" class="comment-info"><span class="comment-age">(27 Mar '11, 15:42)</span> <span class="comment-user userinfo">chronidev</span></div></div></div><div id="comment-tools-3164" class="comment-tools"></div><div class="clear"></div><div id="comment-3164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

