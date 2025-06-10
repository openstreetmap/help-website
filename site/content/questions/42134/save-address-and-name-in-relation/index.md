+++
type = "question"
title = "Save address and name in relation?"
description = '''Is it the right way to add the address and name of an object to the relation? Or should it be added to the outline of a building (which is part of the relation)? See for example this relation: https://www.openstreetmap.org/relation/2921268 I cannot find this building with Nominatim search via the na...'''
date = "2015-04-06T03:09:00Z"
lastmod = "2015-04-06T18:34:00Z"
weight = 42134
keywords = [ "address", "outline", "relations", "name" ]
aliases = [ "/questions/42134" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Save address and name in relation?](/questions/42134/save-address-and-name-in-relation)

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
<span id="post-42134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42134-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it the right way to add the address and name of an object to the relation? Or should it be added to the outline of a building (which is part of the relation)?</p>
<p>See for example this relation: <a href="https://www.openstreetmap.org/relation/2921268">https://www.openstreetmap.org/relation/2921268</a></p>
<p>I cannot find this building with Nominatim search via the name of the object (which is Markthalle VII) or the address (saved in the relation). Why? Is this a bug of Nominatim or bad tagging?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-outline" rel="tag" title="see questions tagged &#39;outline&#39;">outline</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '15, 03:09</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '15, 03:11</strong> </span></p>
</div>
</div>
<div id="comments-container-42134" class="comments-container">
&#10;</div>
<div id="comment-tools-42134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42134-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="42147"></span>

<div id="answer-container-42147" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When using a type=building relation, you should still put the name and all other building-related tags – especially building=yes, but also the address – on the outline. This helps applications with no building:part support to correctly interpret the data. Note that this is different from the treatment of multipolygons, where tags <em>should</em> go to the relation instead of the outer way.</p>
<p>So in your example, you should move the tags from the relation to the outline. The building relation is not strictly necessary here (it is only required if there are ambiguities otherwise), so whether you keep it is a matter of personal preference.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '15, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-42147" class="comments-container">
&#10;</div>
<div id="comment-tools-42147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42147-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42136"></span>

<div id="answer-container-42136" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42136-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if it makes any difference but instead of having the relation tagged as type=building I thought it should be tagged as type=multipolygon and building=yes</p>
<p>There is a multiple part building in my area tagged with type=multipolygon and building=yes with the addr:<em>=</em> in the relation which Nominatim finds.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '15, 03:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-42136" class="comments-container">
<span id="42148"></span>
<div id="comment-42148" class="comment">
<div id="post-42148-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Multipolygon relations are not intended as a collection of objects (in this case, building parts). They simply represent an area, and are semantically identical to an area represented by a closed way. This is a common misunderstanding for some reason.</p>
</div>
<div id="comment-42148-info" class="comment-info">
<span class="comment-age">(06 Apr '15, 17:42)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="42149"></span>
<div id="comment-42149" class="comment">
<div id="post-42149-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The samples near me are buildings with an inner courtyard so there are two ways one an "outer" and the other an "inner". I believe a multi-polygon is needed for that. Until looking at the example in the question I had not seen a relation used just to gather a number of building ways together.</p>
</div>
<div id="comment-42149-info" class="comment-info">
<span class="comment-age">(06 Apr '15, 18:29)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="42150"></span>
<div id="comment-42150" class="comment">
<div id="post-42150-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, in that case a multipolygon relation is of course appropriate. However, this is a different situation than what we have here.</p>
</div>
<div id="comment-42150-info" class="comment-info">
<span class="comment-age">(06 Apr '15, 18:34)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-42136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42136-form-container" class="comment-form-container">
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

