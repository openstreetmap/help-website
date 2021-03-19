+++
type = "question"
title = "NASDAQ MOLD UDP 64 Dissector?"
description = '''Anyone know of a dissector for NASDAQ&#x27;s mold UDP 64 protocol ? I regularly have to identify sequence gaps in MOLD data feeds and this came in very handy. (Link is to Chris Bidwells MOLD UDP dissector) http://www.chrisbidwell.com/moldudp/ Anyway NASDAQ are phasing this out in favor of MOLD UDP 64 and...'''
date = "2012-04-04T16:44:00Z"
lastmod = "2012-04-05T09:24:00Z"
weight = 9946
keywords = [ "nasdaq", "mold", "udp", "64-bit" ]
aliases = [ "/questions/9946" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NASDAQ MOLD UDP 64 Dissector?](/questions/9946/nasdaq-mold-udp-64-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9946-score" class="post-score" title="current number of votes">0</div><span id="post-9946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone know of a dissector for NASDAQ's mold UDP 64 protocol ? I regularly have to identify sequence gaps in MOLD data feeds and this came in very handy. (Link is to Chris Bidwells MOLD UDP dissector)</p><p><a href="http://www.chrisbidwell.com/moldudp/">http://www.chrisbidwell.com/moldudp/</a></p><p>Anyway NASDAQ are phasing this out in favor of MOLD UDP 64 and i was hoping someone might have written a similar plugin.</p><p>Any help would be greatly appreciated.</p><p>Thanks Doug.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nasdaq" rel="tag" title="see questions tagged &#39;nasdaq&#39;">nasdaq</span> <span class="post-tag tag-link-mold" rel="tag" title="see questions tagged &#39;mold&#39;">mold</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '12, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/4fa11b23a0d1151b1c71834532ee0ee7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Doug%20Barker&#39;s gravatar image" /><p><span>Doug Barker</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Doug Barker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Apr '12, 20:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9946" class="comments-container"></div><div id="comment-tools-9946" class="comment-tools"></div><div class="clear"></div><div id="comment-9946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9948"></span>

<div id="answer-container-9948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9948-score" class="post-score" title="current number of votes">0</div><span id="post-9948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know of anybody working on a dissector. One way to solicit for a dissector would be to post an enhancement request on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>; please include the URL for the protocol specification - <a href="http://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/moldudp64.pdf">http://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/moldudp64.pdf</a>. While you're at it, please also include in the enhancement request the link to Chris Bidwell's MOLD UDP dissector and the link for the MOLD UDP specification - <a href="http://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/mossudp.pdf">http://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/mossudp.pdf</a>, so that both can potentially be part of the Wireshark release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9948" class="comments-container"><span id="9950"></span><div id="comment-9950" class="comment"><div id="post-9950-score" class="comment-score"></div><div class="comment-text"><p>One or more sample captures would also be very helpful.</p></div><div id="comment-9950-info" class="comment-info"><span class="comment-age">(04 Apr '12, 23:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="9963"></span><div id="comment-9963" class="comment"><div id="post-9963-score" class="comment-score"></div><div class="comment-text"><p>Guy</p><p>Thanks for your response i will post an update an enhancement request today.</p></div><div id="comment-9963-info" class="comment-info"><span class="comment-age">(05 Apr '12, 09:24)</span> <span class="comment-user userinfo">Doug Barker</span></div></div></div><div id="comment-tools-9948" class="comment-tools"></div><div class="clear"></div><div id="comment-9948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

