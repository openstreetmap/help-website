+++
type = "question"
title = "Correct Island Tagging"
description = '''I&#x27;ve just been checking out &#x27;Hamilton Island, Queensland&#x27; https://www.openstreetmap.org/node/313418906 Currently the islands have their coastline marked as natural=coastline, and a point somewhere in the island marked place=island,name=Hamilton Island. The wiki says the name and place=island should ...'''
date = "2019-02-04T06:05:00Z"
lastmod = "2019-02-04T11:31:00Z"
weight = 67855
keywords = [ "islands", "tagging", "island" ]
aliases = [ "/questions/67855" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Correct Island Tagging](/questions/67855/correct-island-tagging)

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
<span id="post-67855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just been checking out 'Hamilton Island, Queensland' https://www.openstreetmap.org/node/313418906</p>
<p>Currently the islands have their coastline marked as natural=coastline, and a point somewhere in the island marked place=island,name=Hamilton Island.</p>
<p>The wiki says the name and place=island should probably be on the coastline. I note that if you do a search for it on the website it simply highlights the point and not the whole island which isn't ideal.</p>
<p>I thought it would be best to double check before tweaking it, what is the correct way of handling the island?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '19, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0aa50e7695ec5f78dcacab82bc1cd81e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cheater512&#39;s gravatar image" />
<p><span>cheater512</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cheater512 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67855" class="comments-container">
&#10;</div>
<div id="comment-tools-67855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67855-form-container" class="comment-form-container">
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

<span id="67858"></span>

<div id="answer-container-67858" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cheater512 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer to that depends, to some extent, on who you ask and on some other poorly-defined criteria. A node and place=island does the job but cannot meaningfully illustrate the size of the island, as you've pointed out. But if the island is quite large, assembling all the snippets of coastline as members of a relation can be burdensome for the OSM servers in both storing and assembling the various members during the rendering process.</p>
<p>In this case, Hamilton Island is so small it can simply be defined by the coastline as it was drawn and the node removed. Simply copy the node tags to the coastline, and delete the node. That's what I would do. But however you decide to do it, it's more or less your choice. There was a long discussion about a similar topic, that of creating a relation to define water features like bays and straits. Check it out if you want to understand more about the the pros and cons of using relations this way:</p>
<p><a href="https://lists.openstreetmap.org/pipermail/tagging/2018-November/040911.html">https://lists.openstreetmap.org/pipermail/tagging/2018-November/040911.html</a></p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '19, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '19, 09:25</strong> </span></p>
</div>
</div>
<div id="comments-container-67858" class="comments-container">
<span id="67860"></span>
<div id="comment-67860" class="comment">
<div id="post-67860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great thanks! Yep intuitively that's what I was thinking. Upon further review I spotted a couple of the place=island nodes weren't even inside the coastline so a tidy up was certainly needed.</p>
</div>
<div id="comment-67860-info" class="comment-info">
<span class="comment-age">(04 Feb '19, 11:31)</span> <span class="comment-user userinfo">cheater512</span>
</div>
</div>
</div>
<div id="comment-tools-67858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67858-form-container" class="comment-form-container">
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

