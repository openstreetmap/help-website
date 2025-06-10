+++
type = "question"
title = "Extract relations with all members in an area"
description = '''Is there a way to select a relation with all of its members belonging to a specific area? I&#x27;m currently working with hiking routes and I want to store all the hiking tracks for a given input area. As far as I understand from the docs, even if a relation has only one member in the selected area it wi...'''
date = "2021-06-01T01:13:00Z"
lastmod = "2021-06-05T09:15:00Z"
weight = 80373
keywords = [ "boundaries", "overpass", "relations", "area" ]
aliases = [ "/questions/80373" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Extract relations with all members in an area](/questions/80373/extract-relations-with-all-members-in-an-area)

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
<span id="post-80373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80373-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to select a relation with all of its members belonging to a specific area?</p>
<p>I'm currently working with hiking routes and I want to store all the hiking tracks for a given input area. As far as I understand from the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">docs</a>, even if a relation has only one member in the selected area it will be included. Is there any simple workaround to avoid that?</p>
<p><a href="http://overpass-turbo.eu/s/17XY">Here</a> is a basic example, any suggestion would be much appreciated. I'm quite new to OSM and OverpassQL, sorry in advance if this is elementary stuff.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '21, 01:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ccc7ed6843807f47ec4e4ad6d8a52e02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Debo790&#39;s gravatar image" />
<p><span>Debo790</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Debo790 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80373" class="comments-container">
<span id="80376"></span>
<div id="comment-80376" class="comment">
<div id="post-80376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to make sure we understand each other: You want to extract all relations of which all members are inside a certain area. If any member is outside that area you want to exclude the whole relation. Is that the correct understanding?</p>
</div>
<div id="comment-80376-info" class="comment-info">
<span class="comment-age">(01 Jun '21, 08:10)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="80377"></span>
<div id="comment-80377" class="comment">
<div id="post-80377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, correct. In the example provided the difference is minimal, but considering a larger area (e.g. a region, or a province) you may end up including routes that cover all the nation. This is an issue for me at the moment and I didn't find anything useful in other questions.</p>
</div>
<div id="comment-80377-info" class="comment-info">
<span class="comment-age">(01 Jun '21, 08:59)</span> <span class="comment-user userinfo">Debo790</span>
</div>
</div>
</div>
<div id="comment-tools-80373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80373-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="80391"></span>

<div id="answer-container-80391" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80391-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Debo790 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One approach is to use <code>around:0</code> to detect where routes cross the members of the query area. Proof of concept: <a href="http://overpass-turbo.eu/s/1812">http://overpass-turbo.eu/s/1812</a></p>
<p>I didn't look at the output to see if it was entirely correct, but it at least goes in the right direction. I'm not sure if it would work to use the relation as one of the inputs (using the member ways ensures that only intersections with the boundary are considered; it may work the same with the relation as the input).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '21, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-80391" class="comments-container">
<span id="80392"></span>
<div id="comment-80392" class="comment">
<div id="post-80392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems to work fine, it becomes quite heavy scaling the boundaries up to provinces but keeping admin_level=8 results are good even in terms of time. I've perfomed some tests with cities full of hiking routes and also with cities that shows no routes at all, results seems correct in both cases. Thanks a lot!</p>
</div>
<div id="comment-80392-info" class="comment-info">
<span class="comment-age">(02 Jun '21, 01:09)</span> <span class="comment-user userinfo">Debo790</span>
</div>
</div>
</div>
<div id="comment-tools-80391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80391-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80418"></span>

<div id="answer-container-80418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80418-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>area[name=Spoleto][admin_level=8]-&gt;.Spoleto; //Search Area
rel(pivot.Spoleto)-&gt;.Bound; //convert to way to render
.Bound out geom;
(
rel[route=hiking](area.Spoleto)-&gt;.Within; // All hikes within search area
-  
rel .Within(around.Bound:0); //Remove those which cross boundary
);  
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '21, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80418" class="comments-container">
<span id="80423"></span>
<div id="comment-80423" class="comment">
<div id="post-80423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This now retrieves the correct results, but it doesn't check for multiple cities (e.g. Milano or Roma). The code provided in the question (and in answer of maxerickson) deals with it using this: <a href="https://help.openstreetmap.org/questions/64305/overpass-api-get-city-boundaries-within-a-country-slow-query/70342">https://help.openstreetmap.org/questions/64305/overpass-api-get-city-boundaries-within-a-country-slow-query/70342</a></p>
<p>Obviously this decreases performances, but it's the best I came up with so far. Thanks for your effort anyway, your solution is the way to go when dealing with cities with no homonyms.</p>
</div>
<div id="comment-80423-info" class="comment-info">
<span class="comment-age">(05 Jun '21, 09:15)</span> <span class="comment-user userinfo">Debo790</span>
</div>
</div>
</div>
<div id="comment-tools-80418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80403"></span>

<div id="answer-container-80403" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80403-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The nearest I've ever been able to trim to a boundary is to <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">Recurse</a> down to the way members &amp; then search within the area, but this includes ways which overlap the boundary.</p>
<pre><code>area[name=Spoleto][admin_level=8]-&gt;.Spoleto;
rel[route=hiking](area.Spoleto);
way(r)(area.Spoleto);
out geom;
rel(pivot.Spoleto);
out geom;</code></pre>
<p>PS I wish OP had a global area option similar to bbox. It would save a lot of typing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '21, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80403" class="comments-container">
<span id="80411"></span>
<div id="comment-80411" class="comment">
<div id="post-80411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is actually faster, but it includes ways relations that shouldn't appear. An example is in the comment above the query: <a href="http://overpass-turbo.eu/s/185E">http://overpass-turbo.eu/s/185E</a> The aim is to find relations with all the members inside the given area, if some of those members are outside then the whole relation should be discarded.</p>
</div>
<div id="comment-80411-info" class="comment-info">
<span class="comment-age">(04 Jun '21, 00:18)</span> <span class="comment-user userinfo">Debo790</span>
</div>
</div>
</div>
<div id="comment-tools-80403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80403-form-container" class="comment-form-container">
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

