+++
type = "question"
title = "Set maximum packet count."
description = '''For example, I hope to display the newest 65535 packets and drop the oldest ones, in order to save memory when I am waiting some event that happens randomly. I cannot find the option on this. Is it possible or no this feature currently? Sorry for my poor English.'''
date = "2011-10-04T22:48:00Z"
lastmod = "2011-10-05T01:20:00Z"
weight = 6729
keywords = [ "count", "maximum" ]
aliases = [ "/questions/6729" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Set maximum packet count.](/questions/6729/set-maximum-packet-count)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6729-score" class="post-score" title="current number of votes">1</div><span id="post-6729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For example, I hope to display the newest 65535 packets and drop the oldest ones, in order to save memory when I am waiting some event that happens randomly. I cannot find the option on this. Is it possible or no this feature currently?</p><p>Sorry for my poor English.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-maximum" rel="tag" title="see questions tagged &#39;maximum&#39;">maximum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '11, 22:48</strong></p><img src="https://secure.gravatar.com/avatar/20a49b6b367684c9465f712637295c0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OstCollector&#39;s gravatar image" /><p><span>OstCollector</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OstCollector has no accepted answers">0%</span></p></div></div><div id="comments-container-6729" class="comments-container"></div><div id="comment-tools-6729" class="comment-tools"></div><div class="clear"></div><div id="comment-6729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6730"></span>

<div id="answer-container-6730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6730-score" class="post-score" title="current number of votes">1</div><span id="post-6730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is the option of using multiple files (see the capture options dialog). Still that doesn't really solve your memory problem since Wireshark collects state on the frames seen. If you have to option to detect the 'event' in another way, it's preferable to use dumpcap, the command line tool that just captures frames and dumps them in files. Also here the multiple file option helps. Once you know the rough timestamp of the 'event' you can pick up the relevant capture files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '11, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6730" class="comments-container"><span id="6731"></span><div id="comment-6731" class="comment"><div id="post-6731-score" class="comment-score"></div><div class="comment-text"><p>It works. Although not perfect enough. :-) Thank you very much.</p></div><div id="comment-6731-info" class="comment-info"><span class="comment-age">(05 Oct '11, 01:20)</span> <span class="comment-user userinfo">OstCollector</span></div></div></div><div id="comment-tools-6730" class="comment-tools"></div><div class="clear"></div><div id="comment-6730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

