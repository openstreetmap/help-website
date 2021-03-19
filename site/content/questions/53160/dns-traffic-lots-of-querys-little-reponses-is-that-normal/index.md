+++
type = "question"
title = "DNS Traffic. Lots of querys little reponses. Is that normal?"
description = '''Hello guys! I&#x27;m trying to find the root cause of a slow wifi network. It&#x27;s a public wifi hotspot. Before users are free to browse they have to authenticate themselves on a captive portal. The issue is that for some users this captive portal opens very fast and to others are very slow. So slow that t...'''
date = "2016-06-02T19:03:00Z"
lastmod = "2016-06-03T14:34:00Z"
weight = 53160
keywords = [ "dns" ]
aliases = [ "/questions/53160" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DNS Traffic. Lots of querys little reponses. Is that normal?](/questions/53160/dns-traffic-lots-of-querys-little-reponses-is-that-normal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53160-score" class="post-score" title="current number of votes">0</div><span id="post-53160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys!</p><p>I'm trying to find the root cause of a slow wifi network. It's a public wifi hotspot. Before users are free to browse they have to authenticate themselves on a captive portal. The issue is that for some users this captive portal opens very fast and to others are very slow. So slow that they have to try again and voilá! Fast!</p><p>I sniffed a lot and one thing that got my attention is the amount of DNS querys and response ratio. Uder "Statistics --&gt; DNS". Se the image below:</p><p><img src="http://i.imgur.com/MuwwpXh.png" alt="alt text" /></p><p>Is my understanding correct? Does that mean that in this particular capture there were 227 querys but only 101 responses? And if that's right is this DNS normal behavior? To ignore some querys for no good reason?</p><p>Because that would explain what we experience. When users try to connect to the wifi they have to be redirected to a portal to create an account. And on some captures I saw (one that the user couldn't open the portal) there were a query for the captive portal but there was no answer.</p><p>Thanks in advance, Rafael</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '16, 19:03</strong></p><img src="https://secure.gravatar.com/avatar/6a24e499a575770e6ba8e4c74d822420?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafaelbn&#39;s gravatar image" /><p><span>rafaelbn</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafaelbn has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53160" class="comments-container"></div><div id="comment-tools-53160" class="comment-tools"></div><div class="clear"></div><div id="comment-53160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53161"></span>

<div id="answer-container-53161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53161-score" class="post-score" title="current number of votes">1</div><span id="post-53161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Lacking more detailed information I think you've answered it already.</p><p><em>And on some captures I saw (one that the user couldn't open the portal) there were a query for the captive portal but there was no answer.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '16, 23:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53161" class="comments-container"><span id="53172"></span><div id="comment-53172" class="comment"><div id="post-53172-score" class="comment-score"></div><div class="comment-text"><p>But is my reading on that statistics panel correct?</p></div><div id="comment-53172-info" class="comment-info"><span class="comment-age">(03 Jun '16, 04:00)</span> <span class="comment-user userinfo">rafaelbn</span></div></div></div><div id="comment-tools-53161" class="comment-tools"></div><div class="clear"></div><div id="comment-53161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53173"></span>

<div id="answer-container-53173" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53173-score" class="post-score" title="current number of votes">1</div><span id="post-53173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the DNS statistic is a bit misleading - you expect it to cover DNS, while it also seems to cover other name resolution protocols, e.g. LLMNR. I tested this with a capture where 4 DNS packets are present, and it showed 12 packets in the statistics. It turned out I had 8 LLMNR packets in the trace, which changed the statistic.</p><p>if you want to see the real DNS stats (meaning, the stuff on port 53), apply a Display Filter at the bottom saying "dns".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-53173" class="comments-container"><span id="53174"></span><div id="comment-53174" class="comment"><div id="post-53174-score" class="comment-score"></div><div class="comment-text"><p>I just added an enhancement request in the bug tracker to rename the statistic to "Name Resolution" instead of "DNS": <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12492">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12492</a></p></div><div id="comment-53174-info" class="comment-info"><span class="comment-age">(03 Jun '16, 04:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="53188"></span><div id="comment-53188" class="comment"><div id="post-53188-score" class="comment-score"></div><div class="comment-text"><p>Since I didn't know if that statistic was what I thought it was I did exactly that and saw that the number was close. Still, I just don't know if that is the normal behavior or something sketchy is going on my DNS infra.</p></div><div id="comment-53188-info" class="comment-info"><span class="comment-age">(03 Jun '16, 14:34)</span> <span class="comment-user userinfo">rafaelbn</span></div></div></div><div id="comment-tools-53173" class="comment-tools"></div><div class="clear"></div><div id="comment-53173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

