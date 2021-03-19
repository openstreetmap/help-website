+++
type = "question"
title = "How to filter packets by IP in monitor mode?"
description = '''Hi I&#x27;m trying to see if I could capture only the packets to the router admin page when accessed from my phone. I believe I&#x27;d need to capture in monitor mode, but then the source and destination are all MAC addresses and it&#x27;s not clear where the destination IP can be found. Is there a way to capture ...'''
date = "2015-08-04T11:30:00Z"
lastmod = "2015-08-05T11:03:00Z"
weight = 44831
keywords = [ "capture-filter" ]
aliases = [ "/questions/44831" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter packets by IP in monitor mode?](/questions/44831/how-to-filter-packets-by-ip-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44831-score" class="post-score" title="current number of votes">0</div><span id="post-44831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to see if I could capture only the packets to the router admin page when accessed from my phone. I believe I'd need to capture in monitor mode, but then the source and destination are all MAC addresses and it's not clear where the destination IP can be found. Is there a way to capture only the traffic to/from the router web server?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/3c16c3b7b9d89a5736de02187a6253d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mun&#39;s gravatar image" /><p><span>mun</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mun has no accepted answers">0%</span></p></div></div><div id="comments-container-44831" class="comments-container"></div><div id="comment-tools-44831" class="comment-tools"></div><div class="clear"></div><div id="comment-44831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44836"></span>

<div id="answer-container-44836" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44836-score" class="post-score" title="current number of votes">1</div><span id="post-44836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mun has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sadly, if you're capturing in monitor mode on a protected network (WEP or WPA/WPA2), the packets you receive are mostly encrypted, and don't get decrypted until Wireshark processes them, which is too late to apply a capture filter.</p><p>If the router is running some form of open-source firmware, you might be able to do the capture on the router, which wouldn't need to be done in monitor mode, and which would give you packets decrypted by the router hardware or firmware, probably before any capture filter is applied.</p><p>If your phone is running iOS, <a href="https://developer.apple.com/library/ios/qa/qa1176/_index.html#//apple_ref/doc/uid/DTS10001707-CH1-SECIOSPACKETTRACING">there are some options that might let you capture the traffic</a>. The <a href="https://developer.apple.com/library/ios/qa/qa1176/_index.html#//apple_ref/doc/uid/DTS10001707-CH1-SECRVI">remote virtual interface</a> might let you filter on the IP address.</p><p>If your phone is running Android, you might be able to run tcpdump on it and capture the traffic; there might be other options as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '15, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44836" class="comments-container"><span id="44876"></span><div id="comment-44876" class="comment"><div id="post-44876-score" class="comment-score"></div><div class="comment-text"><p>I see. No, the router isn't running a custom firmware. Suppose not running tcpdump on my phone. Is the best approach to just capture all packets and then find the EAPOL handshake between my phone and the router using my phone's MAC address? With that, find the right packets? Can all this be done within Wireshark by using the MAC address capture filter?</p></div><div id="comment-44876-info" class="comment-info"><span class="comment-age">(05 Aug '15, 10:40)</span> <span class="comment-user userinfo">mun</span></div></div><span id="44877"></span><div id="comment-44877" class="comment"><div id="post-44877-score" class="comment-score"></div><div class="comment-text"><p>If you filter using the MAC address of your phone, that should work. Try "wlan host XX:XX:XX:XX:XX:XX", and then make sure Wireshark can decrypt the traffic and then use a display filter.</p></div><div id="comment-44877-info" class="comment-info"><span class="comment-age">(05 Aug '15, 11:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-44836" class="comment-tools"></div><div class="clear"></div><div id="comment-44836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

