+++
type = "question"
title = "Criteria for display filters"
description = '''Hello, I am trying to find where I can see the criteria for the display filters. I looked in the dfilters file but that only contains 17 entries. For example &#x27;http.&#x27; as around 50 filter options, is there a file that defines the criteria that would match each option? I suppose this would be some offs...'''
date = "2017-05-16T07:07:00Z"
lastmod = "2017-05-16T13:01:00Z"
weight = 61431
keywords = [ "display-filter" ]
aliases = [ "/questions/61431" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Criteria for display filters](/questions/61431/criteria-for-display-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61431-score" class="post-score" title="current number of votes">0</div><span id="post-61431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to find where I can see the criteria for the display filters. I looked in the dfilters file but that only contains 17 entries.</p><p>For example 'http.' as around 50 filter options, is there a file that defines the criteria that would match each option?</p><p>I suppose this would be some offset and some hex value, is there a list of these values for each display filter.</p><p>Thank you, GP CC</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '17, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/68b7271b161241faff6b70c8f1769d63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GP%20CC&#39;s gravatar image" /><p><span>GP CC</span><br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GP CC has no accepted answers">0%</span></p></div></div><div id="comments-container-61431" class="comments-container"></div><div id="comment-tools-61431" class="comment-tools"></div><div class="clear"></div><div id="comment-61431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61444"></span>

<div id="answer-container-61444" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61444-score" class="post-score" title="current number of votes">0</div><span id="post-61444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GP CC has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To be precise, the "file that defines the criteria that would match each [filter]" would be the dissector. That contains the code which creates the nodes in the protocol tree to which the display filter can be applied. There is (a lot of) logic involved in that, interpreting every octet and bit in the frame to find out where what field is. So there is no hard-and-fast rules saying 'at this offset that field can be found and a display filter applied'. (layers of) network protocols are just too complex for that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '17, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61444" class="comments-container"><span id="61446"></span><div id="comment-61446" class="comment"><div id="post-61446-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the replies and assistance, I was thinking the dissector for each protocol would be a part or maybe all of the answer.</p><p>GP CC</p></div><div id="comment-61446-info" class="comment-info"><span class="comment-age">(16 May '17, 13:01)</span> <span class="comment-user userinfo">GP CC</span></div></div></div><div id="comment-tools-61444" class="comment-tools"></div><div class="clear"></div><div id="comment-61444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61441"></span>

<div id="answer-container-61441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61441-score" class="post-score" title="current number of votes">0</div><span id="post-61441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is the <a href="https://www.wireshark.org/docs/dfref/">on-line reference of all display filters</a>, if that's what you're interested in? With the Gtk version of Wireshark, you can also find the available display filters by navigating through <em>Internals -&gt; Support Protocols (slow!) -&gt; Display Filter Fields</em>, and you can also use <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> to list the fields as well via <code>tshark -G fields</code>.</p><p>Probably the easiest way to find out the display filter name is by selecting the field of interest in the packet details pane and then reading the display filter associated with that field in the bottom status bar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '17, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-61441" class="comments-container"><span id="61443"></span><div id="comment-61443" class="comment"><div id="post-61443-score" class="comment-score">1</div><div class="comment-text"><p>Oh, and the Qt based interface has them at View | Internal | Supported Protocols.</p></div><div id="comment-61443-info" class="comment-info"><span class="comment-age">(16 May '17, 12:02)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-61441" class="comment-tools"></div><div class="clear"></div><div id="comment-61441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

