+++
type = "question"
title = "adding following support to wireshark"
description = '''I&#x27;m looking for following features   1. g729 support for VOIP calls(playback)  2. exporting call quality record to SQL These features are not available in wireshark. If i want to develop them, what specific things i should i know before attempting it. wireshark codebase is big, so any specific infor...'''
date = "2012-04-05T02:23:00Z"
lastmod = "2012-04-05T10:04:00Z"
weight = 9954
keywords = [ "g729", "sql" ]
aliases = [ "/questions/9954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [adding following support to wireshark](/questions/9954/adding-following-support-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9954-score" class="post-score" title="current number of votes">0</div><span id="post-9954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for following features 1. g729 support for VOIP calls(playback) 2. exporting call quality record to SQL</p><p>These features are not available in wireshark. If i want to develop them, what specific things i should i know before attempting it. wireshark codebase is big, so any specific information will be very helpful.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g729" rel="tag" title="see questions tagged &#39;g729&#39;">g729</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '12, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/7c7ea69631a4b9727b3f65efd09fadae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arif&#39;s gravatar image" /><p><span>arif</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arif has no accepted answers">0%</span></p></div></div><div id="comments-container-9954" class="comments-container"></div><div id="comment-tools-9954" class="comment-tools"></div><div class="clear"></div><div id="comment-9954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9957"></span>

<div id="answer-container-9957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9957-score" class="post-score" title="current number of votes">1</div><span id="post-9957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at this bug report should give you some clues on what to look for <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5619">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5619</a> note that codecs requiring licenses can't be added to the released version of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '12, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-9957" class="comments-container"><span id="9966"></span><div id="comment-9966" class="comment"><div id="post-9966-score" class="comment-score"></div><div class="comment-text"><p>"Requiring licenses" here means "requiring that the user license the codec individually from the vendor; a codec under, for example, the GNU Public License (GPL) is not a problem, but a codec requiring that the user sign a license agreement with the vendor, especially if the license vendor requires a payment for the license, will not be incorporated into the released version of Wireshark, as we do not and will not charge for it and cannot prevent others from giving their copies away as it's under the GPL.</p></div><div id="comment-9966-info" class="comment-info"><span class="comment-age">(05 Apr '12, 10:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9957" class="comment-tools"></div><div class="clear"></div><div id="comment-9957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

