+++
type = "question"
title = "Rendering of roofs above highway=pedestrian areas"
description = '''I&#x27;ve recently added an area that&#x27;s reserved for pedestrians as a multi-polygon here: https://www.openstreetmap.org/#map=19/47.39726/8.59632 However the area for the pedestrians gets drawn over the roofs within it. I&#x27;ve added the roofs as &quot;inner&quot; for now, however that does not feel right, since the ro...'''
date = "2016-04-22T09:40:00Z"
lastmod = "2016-04-22T12:29:00Z"
weight = 49356
keywords = [ "pedestrian", "area", "rendering", "roof", "multi-polygon" ]
aliases = [ "/questions/49356" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering of roofs above highway=pedestrian areas](/questions/49356/rendering-of-roofs-above-highwaypedestrian-areas)

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
<span id="post-49356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49356-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've recently added an area that's reserved for pedestrians as a multi-polygon here: <a href="https://www.openstreetmap.org/#map=19/47.39726/8.59632">https://www.openstreetmap.org/#map=19/47.39726/8.59632</a></p>
<p>However the area for the pedestrians gets drawn over the roofs within it. I've added the roofs as "inner" for now, however that does not feel right, since the roofs just cover the pedestrian area below them. I can't add one of the roofs as inner anyways, so there has to be another solution.</p>
<p>The area is a multi-polygon because of the other cut-out bits and the building in the middle.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-roof" rel="tag" title="see questions tagged &#39;roof&#39;">roof</span> <span class="post-tag tag-link-multi-polygon" rel="tag" title="see questions tagged &#39;multi-polygon&#39;">multi-polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '16, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ee063af1be72074de3d1e195c26d0fcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freaktechnik&#39;s gravatar image" />
<p><span>freaktechnik</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freaktechnik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49356" class="comments-container">
&#10;</div>
<div id="comment-tools-49356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49356-form-container" class="comment-form-container">
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

<span id="49362"></span>

<div id="answer-container-49362" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49362-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-49362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="freaktechnik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a known bug, see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/885">this issue</a> which is marked as a duplicate of the more general <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/688">issue</a>. The latter issue has been open for awhile, but is not fixed yet.</p>
<p>Nevertheless, you should add the layer tags (as hendrikklaas already wrote)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '16, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '16, 12:31</strong> </span></p>
</div>
</div>
<div id="comments-container-49362" class="comments-container">
&#10;</div>
<div id="comment-tools-49362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49362-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49358"></span>

<div id="answer-container-49358" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49358-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-49358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, the renderer does not understand what’s going on here; everything is on the same level. Tag the roofs layer=1, add the bicycle parking as well. It looks like the train is beneath the pedestrian area but there no layer tag either and it should get one. A roof is not an area its just a roof with layer=1, the shops beneath a roof can get a tag like covered=yes since the roof is no part of the building its self. You could make the buildings standing on the pedestrian level as inner in the multi of pedestrian area. Remember don’t tag for the renderer you should tag what’s there. And try not to connect nodes in different levels / layers the nodes of a roof should not be connected to the nodes of the platforms.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '16, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '16, 10:52</strong> </span></p>
</div>
</div>
<div id="comments-container-49358" class="comments-container">
<span id="49361"></span>
<div id="comment-49361" class="comment">
<div id="post-49361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had the roofs tagged as layer 1 at one point, which did not fix the rendering (so it's either a bug in the renderer or I never got updated tiles and hit old ones from the caching layer). However aren't roofs technically a thing inbetween layers? Layers make perfect sense to me for streets &amp; paths, but in this case it just doesn't feel right.</p>
<p>The shops are in actual buildings so that,s correctly tagged for what I know.</p>
<p>Most of the infrastructure (including all platforms and roofs) was tagged before, but I guess I should clean up some of their tagging too (i.e. making the underground stuff truly underground).</p>
</div>
<div id="comment-49361-info" class="comment-info">
<span class="comment-age">(22 Apr '16, 11:34)</span> <span class="comment-user userinfo">freaktechnik</span>
</div>
</div>
</div>
<div id="comment-tools-49358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49358-form-container" class="comment-form-container">
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

