+++
type = "question"
title = "time-to-live exceeded"
description = '''Team The trace below is displaying time-to-live exceeded what does that indicate,  When I see the error, the page fails, but when this does not occur, you do not see and error on the webpage I have no idea what the time-to-live means how does this occur on the internet Help please thanks https://www...'''
date = "2014-03-20T21:12:00Z"
lastmod = "2014-03-24T09:01:00Z"
weight = 31036
keywords = [ "ttl_expired" ]
aliases = [ "/questions/31036" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [time-to-live exceeded](/questions/31036/time-to-live-exceeded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31036-score" class="post-score" title="current number of votes">0</div><span id="post-31036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Team The trace below is displaying time-to-live exceeded what does that indicate, When I see the error, the page fails, but when this does not occur, you do not see and error on the webpage I have no idea what the time-to-live means how does this occur on the internet Help please thanks</p><p><a href="https://www.cloudshark.org/captures/2ec18fc1305a">https://www.cloudshark.org/captures/2ec18fc1305a</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ttl_expired" rel="tag" title="see questions tagged &#39;ttl_expired&#39;">ttl_expired</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '14, 21:12</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p><span>ejohnson7</span><br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-31036" class="comments-container"></div><div id="comment-tools-31036" class="comment-tools"></div><div class="clear"></div><div id="comment-31036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31037"></span>

<div id="answer-container-31037" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31037-score" class="post-score" title="current number of votes">2</div><span id="post-31037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It means your IP packets (the ones carrying your web HTTP traffic, which is over TCP), have crossed too many router hops. Each router will decrement the TTL field in your sent IP packets, and when it reaches 0 the last router will drop the IP packet and respond with an ICMP packet with a TTL exceeded error code.</p><p>This usually happens if there's a loop in the router topology somewhere between you and the web server, either due to a misconfiguration, or a micro-loop due to a router reconvergence event. The latter don't usually last long (a few minutes at most), while the former can last a long time until someone fixes it.</p><p>To see where it's getting looped, do a traceroute to the web server's IP address you're trying to reach (in your example, 195.35.91.71). It appears to be somewhere in London, off of Level-3's network, named worldpay.com maybe? It's not exceeding TTL for me, so it's probably a local issue near you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31037" class="comments-container"><span id="31041"></span><div id="comment-31041" class="comment"><div id="post-31041-score" class="comment-score">2</div><div class="comment-text"><p>The TTL exceeded would usually come from a different IP, than the target system. So, in this case something is faking those frames, maybe a firewall or a QoS device. Especially the delta time between the first SYN and the TTL exceeded, makes me believe it's the local firewall of the OP.</p></div><div id="comment-31041-info" class="comment-info"><span class="comment-age">(20 Mar '14, 23:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31043"></span><div id="comment-31043" class="comment"><div id="post-31043-score" class="comment-score">2</div><div class="comment-text"><p>The ICMP's TTL is 251 when it arrives at your host so I'd say the router detecting the loop is 4 hops away. The RESET packet from the same (webserver's) IP address arrives with a TTL of 255 so your adjacent Cisco router obviously does NAT/FW for you.</p></div><div id="comment-31043-info" class="comment-info"><span class="comment-age">(21 Mar '14, 00:30)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="31061"></span><div id="comment-31061" class="comment"><div id="post-31061-score" class="comment-score">1</div><div class="comment-text"><p>I also found it interesting that the TARGET was replying with the TTL ICMP and not the intermediate router.</p></div><div id="comment-31061-info" class="comment-info"><span class="comment-age">(21 Mar '14, 10:14)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="31090"></span><div id="comment-31090" class="comment"><div id="post-31090-score" class="comment-score"></div><div class="comment-text"><p>thanks much for the help</p></div><div id="comment-31090-info" class="comment-info"><span class="comment-age">(22 Mar '14, 21:08)</span> <span class="comment-user userinfo">ejohnson7</span></div></div><span id="31121"></span><div id="comment-31121" class="comment"><div id="post-31121-score" class="comment-score"></div><div class="comment-text"><p><strong>Hint:</strong> If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-31121-info" class="comment-info"><span class="comment-age">(24 Mar '14, 09:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31037" class="comment-tools"></div><div class="clear"></div><div id="comment-31037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

