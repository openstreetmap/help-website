+++
type = "question"
title = "How to monitor a Firefox addon?"
description = '''I have a FF addon (Windows 10 Pro 64bit) that offers a translation service when holding Ctrl+C after selection of text. I would like to know what information is sent back and forth when I trigger the addon by hitting/holding Ctrl+C. How would I do this in Wireshark? Thank you so much for your hints....'''
date = "2016-11-10T10:29:00Z"
lastmod = "2016-11-10T11:07:00Z"
weight = 57271
keywords = [ "addons", "firefox" ]
aliases = [ "/questions/57271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to monitor a Firefox addon?](/questions/57271/how-to-monitor-a-firefox-addon)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57271-score" class="post-score" title="current number of votes">0</div><span id="post-57271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a FF addon (Windows 10 Pro 64bit) that offers a translation service when holding Ctrl+C after selection of text. I would like to know what information is sent back and forth when I trigger the addon by hitting/holding Ctrl+C. How would I do this in Wireshark? Thank you so much for your hints. Cheers!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-addons" rel="tag" title="see questions tagged &#39;addons&#39;">addons</span> <span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '16, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/653dad3de459aefb0fcef14eb75dbd85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharktooth&#39;s gravatar image" /><p><span>sharktooth</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharktooth has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '16, 10:48</strong> </span></p></div></div><div id="comments-container-57271" class="comments-container"></div><div id="comment-tools-57271" class="comment-tools"></div><div class="clear"></div><div id="comment-57271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57272"></span>

<div id="answer-container-57272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57272-score" class="post-score" title="current number of votes">0</div><span id="post-57272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since you can only capture on network interfaces, where all external traffic passes through from all applications and services, you need to very tightly control your test environment. All, and I mean all, non-required applications and services, which may generate network traffic should be stopped. Then you can run firefox and run your test. From there you have to match you actions to the packets captured to try to distinguish your target traffic from the rest. Try it a couple of times to better recognise the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '16, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57272" class="comments-container"><span id="57273"></span><div id="comment-57273" class="comment"><div id="post-57273-score" class="comment-score"></div><div class="comment-text"><p>Thank you, well understood. Is there a way (e.g. a "personal firewall" - yeah, please don't beat me for this - I have none installed) to block network traffic from any Windows program/application, except for FF?</p></div><div id="comment-57273-info" class="comment-info"><span class="comment-age">(10 Nov '16, 11:07)</span> <span class="comment-user userinfo">sharktooth</span></div></div></div><div id="comment-tools-57272" class="comment-tools"></div><div class="clear"></div><div id="comment-57272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

