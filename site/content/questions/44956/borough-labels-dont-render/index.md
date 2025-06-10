+++
type = "question"
title = "Borough labels don&#x27;t render"
description = '''In Pennsylvania, most towns are defined as &quot;boroughs&quot;. However, when tagging a node as place=borough, the name does not render at all on the map. Is there a reason for this? It makes it hard to find places without the name label on the map.'''
date = "2015-08-28T20:18:00Z"
lastmod = "2015-08-31T08:15:00Z"
weight = 44956
keywords = [ "not_shown", "rendering" ]
aliases = [ "/questions/44956" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Borough labels don't render](/questions/44956/borough-labels-dont-render)

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
<span id="post-44956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44956-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Pennsylvania, most towns are defined as "boroughs". However, when tagging a node as place=borough, the name does not render at all on the map. Is there a reason for this? It makes it hard to find places without the name label on the map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '15, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/830d07454c146488ca46e4fedb8802ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pa_roads&#39;s gravatar image" />
<p><span>pa_roads</span><br />
<span class="score" title="60 reputation points">60</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pa_roads has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '15, 05:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-44956" class="comments-container">
<span id="44980"></span>
<div id="comment-44980" class="comment">
<div id="post-44980-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can try to participate in the related discussion here: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/954">https://github.com/gravitystorm/openstreetmap-carto/issues/954</a> You will need a GitHub account, though.</p>
</div>
<div id="comment-44980-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 08:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44956-form-container" class="comment-form-container">
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

<span id="44978"></span>

<div id="answer-container-44978" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44978-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nodes with place=borough will probably be rendered if they are defined as the label of an administrative boundary relation. Of course, then you will need the data of the borders between boroughs. <a href="http://wiki.openstreetmap.org/wiki/United_States_admin_level">Here is some info</a> as to what administrative devision goes into which admin_level in different states.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '15, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '15, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-44978" class="comments-container">
&#10;</div>
<div id="comment-tools-44978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44978-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44958"></span>

<div id="answer-container-44958" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You probably mean the standard style (osm-carto)? Not all tags gets rendered there and there was some discussion about adding it, but it's closed now:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/954">https://github.com/gravitystorm/openstreetmap-carto/issues/954</a></p>
<p>If you have something more to add and clarify the problem, try to write down your opinion there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '15, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-44958" class="comments-container">
<span id="44979"></span>
<div id="comment-44979" class="comment">
<div id="post-44979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to this issue the decision is to <em>not</em> render place=borough in the standard layer.</p>
</div>
<div id="comment-44979-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 08:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44958-form-container" class="comment-form-container">
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

