+++
type = "question"
title = "What does referer field not being present mean?"
description = '''Hi everyone. I am kind of noob to wireshark so please bear with me for stupidity or obvious things. I am examining a network flow in WireShark which causes a drive by download. In some http (GET request) packets, the &quot;Referer&quot; field is not present. What does this mean? I mean how is the user getting...'''
date = "2013-09-08T15:04:00Z"
lastmod = "2013-09-08T15:50:00Z"
weight = 24457
keywords = [ "referer", "wireshark" ]
aliases = [ "/questions/24457" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does referer field not being present mean?](/questions/24457/what-does-referer-field-not-being-present-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24457-score" class="post-score" title="current number of votes">0</div><span id="post-24457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone. I am kind of noob to wireshark so please bear with me for stupidity or obvious things. I am examining a network flow in WireShark which causes a drive by download. In some http (GET request) packets, the "Referer" field is not present. What does this mean? I mean how is the user getting to these pages? Is he/she entering it manually?</p><p>Edit:</p><p>The URLs full request are of a PNG images. So, I don't think that entering these URLs manually would have happened.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-referer" rel="tag" title="see questions tagged &#39;referer&#39;">referer</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '13, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/a12160c79489f265830c301827815b97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheRookieLearner&#39;s gravatar image" /><p><span>TheRookieLea...</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheRookieLearner has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Sep '13, 15:10</strong> </span></p></div></div><div id="comments-container-24457" class="comments-container"></div><div id="comment-tools-24457" class="comment-tools"></div><div class="clear"></div><div id="comment-24457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24458"></span>

<div id="answer-container-24458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24458-score" class="post-score" title="current number of votes">1</div><span id="post-24458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the referrer header is not present, the URL could either have been entered manually or some script was doing the request which did not adde the referrer header. Is the User-Agent header the same for all requests?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '13, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24458" class="comments-container"><span id="24459"></span><div id="comment-24459" class="comment"><div id="post-24459-score" class="comment-score"></div><div class="comment-text"><p>Ya, its the same (which is Mozilla/4.0). Does this mean a script is making those requests? How do I verify that?</p></div><div id="comment-24459-info" class="comment-info"><span class="comment-age">(08 Sep '13, 15:50)</span> <span class="comment-user userinfo">TheRookieLea...</span></div></div></div><div id="comment-tools-24458" class="comment-tools"></div><div class="clear"></div><div id="comment-24458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

