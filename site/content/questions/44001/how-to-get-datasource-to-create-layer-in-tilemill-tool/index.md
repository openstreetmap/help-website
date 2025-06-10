+++
type = "question"
title = "How to get datasource to create layer in tilemill tool"
description = '''I need to add a route layer for India in tilemill tool. how do i get data source from online for my particular place?'''
date = "2015-07-06T11:22:00Z"
lastmod = "2015-07-07T00:25:00Z"
weight = 44001
keywords = [ "tilemill" ]
aliases = [ "/questions/44001" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get datasource to create layer in tilemill tool](/questions/44001/how-to-get-datasource-to-create-layer-in-tilemill-tool)

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
<span id="post-44001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44001-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to add a route layer for India in tilemill tool. how do i get data source from online for my particular place?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '15, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0ab63d5826eb4caf1559f1d14eaaa877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mayee&#39;s gravatar image" />
<p><span>Mayee</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mayee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44001" class="comments-container">
<span id="44018"></span>
<div id="comment-44018" class="comment">
<div id="post-44018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just in case you haven't see it already, I'd definitely run through TileMill's "crash course":</p>
<p><a href="https://www.mapbox.com/tilemill/docs/crashcourse/introduction/">https://www.mapbox.com/tilemill/docs/crashcourse/introduction/</a></p>
</div>
<div id="comment-44018-info" class="comment-info">
<span class="comment-age">(07 Jul '15, 00:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44001-form-container" class="comment-form-container">
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

<span id="44015"></span>

<div id="answer-container-44015" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44015-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Typically you would download the OSM data file (.osm.pbf format) either for all of India or for your region of interest, using one of the sources listed on the <a href="http://www.openstreetmap.org/export#map=5/21.923/82.749">Export tab</a> of the web site. Then you would use the osm2pgsql program to import this data into a PostGIS database they you have set up locally. Then you can use TileMill to access that database.</p>
<p>Working with <a href="http://download.geofabrik.de/asia/india.html">Shape Files</a> is an alternative to a database install but depending on what you mean by "route layer", not all information you are interested in may be present in the shape file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '15, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44015" class="comments-container">
&#10;</div>
<div id="comment-tools-44015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44015-form-container" class="comment-form-container">
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

