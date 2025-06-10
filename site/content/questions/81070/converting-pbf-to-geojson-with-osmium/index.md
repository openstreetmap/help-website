+++
type = "question"
title = "Converting .pbf to .geojson with osmium"
description = '''I&#x27;ve downloaded the United States .osm.pbf from Geofabrik. To convert the map data from .osm.pbf to GeoJSON, I used the following osmium command: osmium export UNITED_STATES.pbf -o UNITED_STATES.geojson --index-type dense_file_array The output GeoJSON appears to only contain points (e.g trees, build...'''
date = "2021-07-23T15:48:00Z"
lastmod = "2021-07-23T20:55:00Z"
weight = 81070
keywords = [ "osmium" ]
aliases = [ "/questions/81070" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Converting .pbf to .geojson with osmium](/questions/81070/converting-pbf-to-geojson-with-osmium)

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
<span id="post-81070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've downloaded the United States .osm.pbf from Geofabrik. To convert the map data from .osm.pbf to GeoJSON, I used the following osmium command:<br />
<code>osmium export UNITED_STATES.pbf -o UNITED_STATES.geojson --index-type dense_file_array</code></p>
<p>The output GeoJSON appears to only contain points (e.g trees, buildings, powerlines) and no roads/polygons.</p>
<p>The progress bar in the terminal indicates that osmium has finished.</p>
<p>Do I need to include extra arguments to export other geometries?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '21, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1bc0081b72746240873e79d9b62e4d6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tussiez&#39;s gravatar image" />
<p><span>tussiez</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tussiez has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-81070" class="comments-container">
&#10;</div>
<div id="comment-tools-81070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81070-form-container" class="comment-form-container">
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

<span id="81071"></span>

<div id="answer-container-81071" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81071-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tussiez has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The program isn't finished when the progress bar is finished but when the program is finished. The progress bar is, unfortunately, not working that great for <code>osmium export</code>. I suspect when you wait for the program to actually finish, you'll see all the data in the file.</p>
<p>Also: When using <code>dense_file_array</code>, you should add a file name: <code>--index-type dense_file_array,nodes.dat</code>. Otherwise the data goes into a file that you can't see which can be confusing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '21, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-81071" class="comments-container">
<span id="81072"></span>
<div id="comment-81072" class="comment">
<div id="post-81072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll wait longer. When adding the file name to <code>dense_file_array</code>, osmium throws an argument error.<br />
<code>Unknown index type 'dense_file_array,index.dat'. Use --show-index-types or -I to get a list.</code></p>
</div>
<div id="comment-81072-info" class="comment-info">
<span class="comment-age">(23 Jul '21, 19:14)</span> <span class="comment-user userinfo">tussiez</span>
</div>
</div>
<span id="81073"></span>
<div id="comment-81073" class="comment">
<div id="post-81073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then your osmium is too old. There was a bug in osmium a while back but that has been fixed.</p>
</div>
<div id="comment-81073-info" class="comment-info">
<span class="comment-age">(23 Jul '21, 20:55)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-81071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81071-form-container" class="comment-form-container">
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

