+++
type = "question"
title = "Not filtering out WPA setup packets in capture filter?"
description = '''Hello!  So, I am able to view/decrypt packets over my WPA network as long as I captured the setup packets. However, there are a TON of broadcast packets that junk up the captured packets. I&#x27;m just interested in the HTTP traffic. Filtering works fine, but I would much rather set up a capture filter s...'''
date = "2013-08-30T18:25:00Z"
lastmod = "2013-08-31T15:17:00Z"
weight = 24217
keywords = [ "setup", "capture-filter", "http", "wpa" ]
aliases = [ "/questions/24217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not filtering out WPA setup packets in capture filter?](/questions/24217/not-filtering-out-wpa-setup-packets-in-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24217-score" class="post-score" title="current number of votes">0</div><span id="post-24217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>So, I am able to view/decrypt packets over my WPA network as long as I captured the setup packets. However, there are a TON of broadcast packets that junk up the captured packets. I'm just interested in the HTTP traffic. Filtering works fine, but I would much rather set up a capture filter so my logs stop getting so huge and hard to manage. But if I do some sort of HTTP capture filtering (e.g. port 80), I never get the capture packets so don't even know if it IS HTTP traffic... How do I fix this?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/7826e9b5784b2c31ad45ceb5930cc3ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orisqu&#39;s gravatar image" /><p><span>orisqu</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orisqu has no accepted answers">0%</span></p></div></div><div id="comments-container-24217" class="comments-container"></div><div id="comment-tools-24217" class="comment-tools"></div><div class="clear"></div><div id="comment-24217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24244"></span>

<div id="answer-container-24244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24244-score" class="post-score" title="current number of votes">0</div><span id="post-24244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But if I do some sort of HTTP capture filtering (e.g. port 80), I never get the capture packets so don't even know if it IS HTTP traffic... <strong>How do I fix this?</strong></p></blockquote><p>You can't as the traffic is encrypted and as you already realized, there is no way to know if an encrypted packet contains a HTTP frame. Therefore you cannot build a <strong>capture filter</strong> for HTTP traffic.</p><p>To reduce at least some traffic, you can filter on the MAC address of the AP and your client. See my answer to a similar (kind of) question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/24107/filter-capture-based-on-80211-signal-strength">http://ask.wireshark.org/questions/24107/filter-capture-based-on-80211-signal-strength</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24244" class="comments-container"></div><div id="comment-tools-24244" class="comment-tools"></div><div class="clear"></div><div id="comment-24244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

