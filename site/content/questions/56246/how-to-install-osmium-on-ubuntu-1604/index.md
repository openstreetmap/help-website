+++
type = "question"
title = "How to install osmium on ubuntu 16.04?"
description = '''I&#x27;m using ubuntu 16.04 and looking to install osmium. I first tried to use the package that&#x27;s in Ubuntu, but that&#x27;s significantly old and doesn&#x27;t include osmium&#x27;s extract function.  I then read its README, but it requires a few packages that I have to manually build myself (rapidjson, Libosmium).  A...'''
date = "2017-05-21T21:55:00Z"
lastmod = "2017-05-21T22:50:00Z"
weight = 56246
keywords = [ "osmium", "ubuntu" ]
aliases = [ "/questions/56246" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to install osmium on ubuntu 16.04?](/questions/56246/how-to-install-osmium-on-ubuntu-1604)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56246-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using ubuntu 16.04 and looking to install osmium. I first tried to use the package that's in Ubuntu, but that's significantly old and doesn't include <a href="https://github.com/osmcode/osmium-tool/releases/tag/v1.5.0">osmium's extract function</a>.</p>
<p>I then read its README, but it requires a few packages that I have to manually build myself (rapidjson, Libosmium).</p>
<p>Are there any packages or do I have to manually build everything?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '17, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-56246" class="comments-container">
&#10;</div>
<div id="comment-tools-56246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56246-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56247"></span>

<div id="answer-container-56247" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56247-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>libosmium is a header-only library so you can simply check that out from github. The build process is clever enough to find it if you have a directory structure where libosmium sits in parallel with osmium-tool. And rapidjson doesn't have to be installed separately, it is included in the osmium-tool checkout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '17, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56247" class="comments-container">
&#10;</div>
<div id="comment-tools-56247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56247-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

