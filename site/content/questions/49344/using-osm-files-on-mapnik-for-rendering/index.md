+++
type = "question"
title = "using .osm files on mapnik for rendering"
description = '''Hello,  So after I installed and tried the two tutorials of Mapnik I found on the wiki (with success). I noted that all tutorials I seen on the web are basically using shapefiles. My question is : Is it possible to render on mapnik using .osm files ? If yes, please suggest me some tutorials showing ...'''
date = "2016-04-21T14:57:00Z"
lastmod = "2016-04-21T20:00:00Z"
weight = 49344
keywords = [ "rendering", "mapnik-german", "mapnik", ".osm" ]
aliases = [ "/questions/49344" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [using .osm files on mapnik for rendering](/questions/49344/using-osm-files-on-mapnik-for-rendering)

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
<span id="post-49344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>So after I installed and tried the two tutorials of Mapnik I found on the wiki (with success). I noted that all tutorials I seen on the web are basically using shapefiles. My question is : Is it possible to render on mapnik using .osm files ? If yes, please suggest me some tutorials showing it.</p>
<p>Thank you in advance for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik-german" rel="tag" title="see questions tagged &#39;mapnik-german&#39;">mapnik-german</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '16, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/88a84abc16f8b57c4922bdbe057ebd81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IDRI%20Sofiane&#39;s gravatar image" />
<p><span>IDRI Sofiane</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IDRI Sofiane has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49344" class="comments-container">
&#10;</div>
<div id="comment-tools-49344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49344-form-container" class="comment-form-container">
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

<span id="49346"></span>

<div id="answer-container-49346" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49346-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my experience, it used to work but no longer does and you'll need to put your .osm files into a Postgresql database.</p>
<p>I have some scripts that build topo maps for areas I hike that mix OSM data and elevation data (from other sources). Those scripts broke at some update of Mapnik about two years and I had to rewrite them all to pull the OSM data from a database instead of a .osm file. I recall asking on a Mapnik forum about that and was basically told they weren't interested in supporting/fixing .osm file support.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '16, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-49346" class="comments-container">
<span id="49349"></span>
<div id="comment-49349" class="comment">
<div id="post-49349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your clarification <a href="http://help.openstreetmap.org/users/5918/stf">@stf</a></p>
</div>
<div id="comment-49349-info" class="comment-info">
<span class="comment-age">(21 Apr '16, 20:00)</span> <span class="comment-user userinfo">IDRI Sofiane</span>
</div>
</div>
</div>
<div id="comment-tools-49346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49346-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49345"></span>

<div id="answer-container-49345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49345-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I might be misunderstanding what you're asking, but isn't that what <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> is essentially doing?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '16, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-49345" class="comments-container">
&#10;</div>
<div id="comment-tools-49345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49345-form-container" class="comment-form-container">
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

