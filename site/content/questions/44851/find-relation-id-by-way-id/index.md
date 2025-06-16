+++
type = "question"
title = "Find relation id by way id"
description = '''When searching for a particular street, I obtained a &#x27;way&#x27; object ( https://www.openstreetmap.org/way/23497173 ) which consists out of 7 nodes. The api ( https://www.openstreetmap.org/api/0.6/way/23497173 ) gives a nice overview of the result, but without the link to the relation (the whole street). I...'''
date = "2015-08-20T20:26:00Z"
lastmod = "2015-08-20T20:29:00Z"
weight = 44851
keywords = [ "api", "relation", "way" ]
aliases = [ "/questions/44851" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Find relation id by way id](/questions/44851/find-relation-id-by-way-id)

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
<span id="post-44851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44851-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When searching for a particular street, I obtained a 'way' object ( <a href="https://www.openstreetmap.org/way/23497173">https://www.openstreetmap.org/way/23497173</a> ) which consists out of 7 nodes. The api ( <a href="https://www.openstreetmap.org/api/0.6/way/23497173">https://www.openstreetmap.org/api/0.6/way/23497173</a> ) gives a nice overview of the result, but without the link to the relation (the whole street).</p>
<p>Is there a manner to find the relation id by use of the api link?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '15, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/51da372f5cfba5ade32199774a0dcfca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matsli&#39;s gravatar image" />
<p><span>Matsli</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matsli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '15, 21:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-44851" class="comments-container">
&#10;</div>
<div id="comment-tools-44851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44851-form-container" class="comment-form-container">
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

<span id="44852"></span>

<div id="answer-container-44852" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44852-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-44852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Matsli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/api/0.6/way/23497173/relations">https://www.openstreetmap.org/api/0.6/way/23497173/relations</a> is what you're looking for. It is documented <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Relations_for_element:_GET_.2Fapi.2F0.6.2F.5Bnode.7Cway.7Crelation.5D.2F.23id.2Frelations">on the Wiki.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '15, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44852" class="comments-container">
&#10;</div>
<div id="comment-tools-44852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44852-form-container" class="comment-form-container">
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

