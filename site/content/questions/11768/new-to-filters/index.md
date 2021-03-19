+++
type = "question"
title = "new to filters"
description = '''I&#x27;m new to filters in wireshark. Any filter I try like tcp or http or ip clears all packets. I&#x27;m specifically trying to see only broadcasts with the filter eth.addr == ff:ff:ff:ff:ff:ff . Applying this filter clears all packets. When I remove the filter, I see all kinds of broadcast packets. I&#x27;m run...'''
date = "2012-06-08T07:33:00Z"
lastmod = "2012-06-08T08:05:00Z"
weight = 11768
keywords = [ "filters" ]
aliases = [ "/questions/11768" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [new to filters](/questions/11768/new-to-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11768-score" class="post-score" title="current number of votes">0</div><span id="post-11768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to filters in wireshark. Any filter I try like tcp or http or ip clears all packets. I'm specifically trying to see only broadcasts with the filter eth.addr == ff:ff:ff:ff:ff:ff . Applying this filter clears all packets. When I remove the filter, I see all kinds of broadcast packets. I'm running wireshark 1.6.7 as root, capturing on wlan0.mon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/6c9c672f81f575d8e424e604246ad707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbagg&#39;s gravatar image" /><p><span>jbagg</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbagg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '12, 07:34</strong> </span></p></div></div><div id="comments-container-11768" class="comments-container"></div><div id="comment-tools-11768" class="comment-tools"></div><div class="clear"></div><div id="comment-11768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11769"></span>

<div id="answer-container-11769" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11769-score" class="post-score" title="current number of votes">2</div><span id="post-11769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jbagg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're capturing on the wlan0.mon interface, then your packets are probably not Ethernet encapsulated, but IEEE 802.11 encapsulated. Try a filter of <code>wlan.da == ff:ff:ff:ff:ff:ff</code> instead, assuming that's the field you're interested in.</p><p>Remember that you can always left-click within the packet details pane on the field that you are interested in and see what the filter name is for that field in the status bar. You can also right-click on the field and choose either the "Apply as Filter" or "Prepare a Filter" options from the menu to avoid some extra typing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11769" class="comments-container"><span id="11770"></span><div id="comment-11770" class="comment"><div id="post-11770-score" class="comment-score"></div><div class="comment-text"><p>Thank you, wlan.addr works!</p></div><div id="comment-11770-info" class="comment-info"><span class="comment-age">(08 Jun '12, 08:05)</span> <span class="comment-user userinfo">jbagg</span></div></div></div><div id="comment-tools-11769" class="comment-tools"></div><div class="clear"></div><div id="comment-11769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

