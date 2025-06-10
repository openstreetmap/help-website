+++
type = "question"
title = "National Park Rendering over Oceans"
description = '''So I have been going on a mapping spree lately mapping the outer banks of North Carolina, but What I have begun to notice is the national park boundaries are covering up all the detail out there. Many parts of islands are simply specifically their coastlines, are covered with these giant green blobs...'''
date = "2016-06-16T02:43:00Z"
lastmod = "2016-06-16T18:20:00Z"
weight = 50241
keywords = [ "national_park", "rendering", "coastline" ]
aliases = [ "/questions/50241" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [National Park Rendering over Oceans](/questions/50241/national-park-rendering-over-oceans)

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
<span id="post-50241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50241-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I have been going on a mapping spree lately mapping the outer banks of North Carolina, but What I have begun to notice is the national park boundaries are covering up all the detail out there. Many parts of islands are simply specifically their coastlines, are covered with these giant green blobs called National Parks. Here is an example at <a href="http://www.openstreetmap.org/#map=13/35.0409/-76.0822">Portsmouth Island</a></p>
<p>What is even more frustrating, is this rendering issue has already been solved, when looking at lakes around borders of national parks, we see the green get covered by the water, with only a green shaded line remaining above the water to represent the border of the national park. Here is an example at <a href="http://www.openstreetmap.org/#map=14/35.4555/-83.7635">Fontana Lake</a>. Is there anyway we can fix this, It seems like a simple fix, just get national parks over oceans to render the same way as national parks over lakes.</p>
<p>Is there any reason this cant be done?</p>
<p>I have thought of a couple work arounds, like making the border of the national parks the islands, or putting an area of water over the area affected by the green blob issue, so it would be rendered correctly, but I realized that this would be mapping for the render which is a no no.</p>
<p>So how do we get this fixed?</p>
<p>Edit: I figured out the problem, it had been labeled leisure=park I checked the description page wiki for Leisure= park and it clearly says do not label national parks with this so i think i found my answer, take the leisure=park off since its not supposed to be there any way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-national_park" rel="tag" title="see questions tagged &#39;national_park&#39;">national_park</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '16, 02:43</strong></p>
<img src="https://secure.gravatar.com/avatar/57d91a34d5000cb058777743aa82dc24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sunfishtommy&#39;s gravatar image" />
<p><span>Sunfishtommy</span><br />
<span class="score" title="111 reputation points">111</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sunfishtommy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '16, 18:21</strong> </span></p>
</div>
</div>
<div id="comments-container-50241" class="comments-container">
<span id="50246"></span>
<div id="comment-50246" class="comment">
<div id="post-50246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are we talking about the "Standard" rendering? In that rendering, national parks are rendered with only a green border and no fill, and I don't see a problem in either of the linked locations (other than Great Smoky Mountains National Park being tagged as a leisure=park). Can you post a screenshot of what you consider to be a problem?</p>
</div>
<div id="comment-50246-info" class="comment-info">
<span class="comment-age">(16 Jun '16, 16:39)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="50251"></span>
<div id="comment-50251" class="comment">
<div id="post-50251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yea I figured out that was the problem, it had been labeled leisure=park I checked the description page wiki for Leisure= park and it clearly says do not label national parks with this so i think i found my answer, take the leisure=park off since its not supposed to be there any way.</p>
</div>
<div id="comment-50251-info" class="comment-info">
<span class="comment-age">(16 Jun '16, 18:19)</span> <span class="comment-user userinfo">Sunfishtommy</span>
</div>
</div>
</div>
<div id="comment-tools-50241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50241-form-container" class="comment-form-container">
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

<span id="50244"></span>

<div id="answer-container-50244" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50244-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sunfishtommy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is due to the way the OSM main map is rendered, and appears to be similar to a known, open issue: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/426">https://github.com/gravitystorm/openstreetmap-carto/issues/426</a>. If you have ideas on how to fix, feel free to add them there. However, <a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">don't change the data just so it looks "right"</a> according to you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '16, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-50244" class="comments-container">
<span id="50245"></span>
<div id="comment-50245" class="comment">
<div id="post-50245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yet, matkoniecz's lastest comment "We moved to ocean polygons" sounds like this issue could be fixed. I suggest to create a new issue at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/">https://github.com/gravitystorm/openstreetmap-carto/issues/</a> and mention related issue 426.</p>
</div>
<div id="comment-50245-info" class="comment-info">
<span class="comment-age">(16 Jun '16, 16:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50252"></span>
<div id="comment-50252" class="comment">
<div id="post-50252-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I figured out the problem, it had been labeled leisure=park I checked the description page wiki for Leisure= park and it clearly says do not label national parks with this so i think i found my answer, take the leisure=park off since its not supposed to be there any way.</p>
<p>So problem is fixed now, since leisure=park should not have been there anyway.</p>
</div>
<div id="comment-50252-info" class="comment-info">
<span class="comment-age">(16 Jun '16, 18:20)</span> <span class="comment-user userinfo">Sunfishtommy</span>
</div>
</div>
</div>
<div id="comment-tools-50244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50244-form-container" class="comment-form-container">
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

