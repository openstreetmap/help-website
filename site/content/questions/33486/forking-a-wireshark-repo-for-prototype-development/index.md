+++
type = "question"
title = "Forking a wireshark repo for prototype development"
description = '''Hi. My organization is currently developing a Wireshark dissector for a still rapidly evolving IEEE standard. Since quite a few changes to the standard are planned to happen within the coming months, we are not sure if we want to push this into the trunk of the main Wireshark repo. Instead, we want ...'''
date = "2014-06-05T15:42:00Z"
lastmod = "2014-06-06T04:25:00Z"
weight = 33486
keywords = [ "dissector" ]
aliases = [ "/questions/33486" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Forking a wireshark repo for prototype development](/questions/33486/forking-a-wireshark-repo-for-prototype-development)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33486-score" class="post-score" title="current number of votes">0</div><span id="post-33486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. My organization is currently developing a Wireshark dissector for a still rapidly evolving IEEE standard. Since quite a few changes to the standard are planned to happen within the coming months, we are not sure if we want to push this into the trunk of the main Wireshark repo. Instead, we want to take the latest stable load and make a fork and host it in GitHub for people across the globe to contribute. Once the standard is approved, we will make sure the dissector fits into the Wireshark coding development practices before pushing the changes to the general Wireshark community.</p><p>Are there any guidelines to this?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '14, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/088b63a47c37bd9935520a8e9191196c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frankh-c4mi&#39;s gravatar image" /><p><span>frankh-c4mi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frankh-c4mi has no accepted answers">0%</span></p></div></div><div id="comments-container-33486" class="comments-container"></div><div id="comment-tools-33486" class="comment-tools"></div><div class="clear"></div><div id="comment-33486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33492"></span>

<div id="answer-container-33492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33492-score" class="post-score" title="current number of votes">0</div><span id="post-33492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't have to fork a whole new Wireshark repository. It's sufficient to create a new GitHub Repo for your dissector code, unless you have to modify the Wireshark code to make your dissector work. If you do it this way you'll have to add some information about how to add your dissector to the Wireshark build process.</p><blockquote><p><a href="https://help.github.com/articles/create-a-repo">https://help.github.com/articles/create-a-repo</a></p></blockquote><p>If you still think you need a fork</p><blockquote><p><a href="https://help.github.com/articles/fork-a-repo">https://help.github.com/articles/fork-a-repo</a></p></blockquote><p>Or search only: GitHub fork tutorial</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '14, 21:51</strong> </span></p></div></div><div id="comments-container-33492" class="comments-container"><span id="33500"></span><div id="comment-33500" class="comment"><div id="post-33500-score" class="comment-score">1</div><div class="comment-text"><p>Why not just use Gerrit and mark it as [WIP] work-in-progress in that way you can rebase and keep it up to date with Wireshark sources.</p></div><div id="comment-33500-info" class="comment-info"><span class="comment-age">(06 Jun '14, 04:25)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-33492" class="comment-tools"></div><div class="clear"></div><div id="comment-33492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

