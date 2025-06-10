+++
type = "question"
title = "Extract city boundaries for certain locations"
description = '''So to obtain the boundary coordinates/polygon of a city I have been using the following query: ( rel[&quot;name&quot; = &quot;New Delhi&quot;];&amp;gt;;);out meta; But it ends up outputting null data for several cities(eg: &#x27;Bengaluru&#x27;, &#x27;Mumbai&#x27;, etc). Is there a way around it to get the administrative boundaries of these c...'''
date = "2017-05-13T15:10:00Z"
lastmod = "2017-05-13T15:22:00Z"
weight = 56159
keywords = [ "boundaries", "overpass", "multipolygon", "areas" ]
aliases = [ "/questions/56159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract city boundaries for certain locations](/questions/56159/extract-city-boundaries-for-certain-locations)

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
<span id="post-56159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56159-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So to obtain the boundary coordinates/polygon of a city I have been using the following query:<br />
( rel["name" = "New Delhi"];&gt;;);out meta;</p>
<p>But it ends up outputting null data for several cities(eg: 'Bengaluru', 'Mumbai', etc). Is there a way around it to get the administrative boundaries of these cities?<br />
^Much Appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '17, 15:10</strong></p>
<img src="https://secure.gravatar.com/avatar/4e8c8dc7fc9182d8fb4f4dba2e03e3f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shouryalala&#39;s gravatar image" />
<p><span>shouryalala</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shouryalala has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '17, 19:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-56159" class="comments-container">
&#10;</div>
<div id="comment-tools-56159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56159-form-container" class="comment-form-container">
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

<span id="56161"></span>

<div id="answer-container-56161" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56161-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems they are not present in the OSM data. Here's an Overpass script to search for administrative boundaries: <a href="http://overpass-turbo.eu/s/p1x">http://overpass-turbo.eu/s/p1x</a></p>
<p>As you can see, there is no entry for Mumbai.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '17, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-56161" class="comments-container">
&#10;</div>
<div id="comment-tools-56161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56161-form-container" class="comment-form-container">
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

