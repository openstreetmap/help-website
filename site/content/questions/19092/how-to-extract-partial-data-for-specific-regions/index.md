+++
type = "question"
title = "How to extract partial data for specific regions?"
description = '''I am currently building a route planning app for runners. I&#x27;m wondering if it&#x27;s possible extract all the ways/map features (for a specific area) on which humans can walk/run? Is it also possible to download just the filtered mapping data without having to download all the other map features that nor...'''
date = "2013-01-15T00:01:00Z"
lastmod = "2013-01-15T21:59:00Z"
weight = 19092
keywords = [ "ways", "footpath", "walking", "pathways" ]
aliases = [ "/questions/19092" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract partial data for specific regions?](/questions/19092/how-to-extract-partial-data-for-specific-regions)

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
<span id="post-19092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19092-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently building a route planning app for runners. I'm wondering if it's possible extract all the ways/map features (for a specific area) on which humans can walk/run?</p>
<p>Is it also possible to download just the filtered mapping data without having to download all the other map features that normally come from the API (to save bandwidth).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-walking" rel="tag" title="see questions tagged &#39;walking&#39;">walking</span> <span class="post-tag tag-link-pathways" rel="tag" title="see questions tagged &#39;pathways&#39;">pathways</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '13, 00:01</strong></p>
<img src="https://secure.gravatar.com/avatar/361e0b98020ca3f3d7db7baa2ec6c590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sadeer&#39;s gravatar image" />
<p><span>Sadeer</span><br />
<span class="score" title="176 reputation points">176</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sadeer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '13, 22:18</strong> </span></p>
</div>
</div>
<div id="comments-container-19092" class="comments-container">
&#10;</div>
<div id="comment-tools-19092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19092-form-container" class="comment-form-container">
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

<span id="19093"></span>

<div id="answer-container-19093" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19093-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's going to be an <a href="http://wiki.openstreetmap.org/wiki/Planet">awful lot of data</a> if you want to process the whole planet. Maybe start with a smaller data <a href="http://wiki.openstreetmap.org/wiki/Planet#Country_and_area_extracts">extract</a> (perhaps for a smaller country) first?</p>
<p>One approach, as detailed <a href="http://help.openstreetmap.org/questions/9816/the-best-way-to-extract-street-list/16248">here</a>, would be to use <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> - in your case you'd want to extract ways tagged "<a href="http://wiki.openstreetmap.org/wiki/Highway">highway</a>" and then exclude from that those that people <a href="http://wiki.openstreetmap.org/wiki/Key:foot">aren't allowed to walk on</a>.</p>
<p>An alternative approach would be to throw all the OSM data data into a database and then work with it there. The instructions <a href="http://switch2osm.org/serving-tiles/">here</a> are designed to support a tile server (which you don't need) but do cover loading the planet or an extract into a database, from which you could process it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '13, 00:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19093" class="comments-container">
<span id="19094"></span>
<div id="comment-19094" class="comment">
<div id="post-19094-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See the <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">access restrictions page</a> for implicit default access values for different countries. Additionally there are various interesting hiking tags, especially <a href="http://wiki.openstreetmap.org/wiki/Key:sac_scale">sac_scale</a>, <a href="http://wiki.openstreetmap.org/wiki/Key:trail_visibility">trail_visibility</a> and of course <a href="http://wiki.openstreetmap.org/wiki/Relation:route">hiking routes</a>. The <a href="http://wiki.openstreetmap.org/wiki/Hiking">hiking wiki page</a> has more information.</p>
</div>
<div id="comment-19094-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 08:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19128"></span>
<div id="comment-19128" class="comment">
<div id="post-19128-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the answer. I think we're on the right track but I'm not trying to download the whole planet file then extract the relevant features but trying to get the mapping data for a 5-miles-radius area as specified by the user of the app and then extract the mapping features that will be needed to compute a route/path for the user.</p>
</div>
<div id="comment-19128-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 21:40)</span> <span class="comment-user userinfo">Sadeer</span>
</div>
</div>
<span id="19131"></span>
<div id="comment-19131" class="comment">
<div id="post-19131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That sort of radius should be well within the capabilities of <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> or an <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> server (perhaps one that you host along with the rest of your application)</p>
</div>
<div id="comment-19131-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 21:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19093-form-container" class="comment-form-container">
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

