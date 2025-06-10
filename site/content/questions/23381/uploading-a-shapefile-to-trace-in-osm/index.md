+++
type = "question"
title = "Uploading a shapefile to trace in OSM"
description = '''Hi there, I am wondering if it is possible to upload a shapefile to edit vertices of a boundary layer in OSM and then delete the shapefile I used to trace on.  There is a small section of the international boundary between Chile and Argentina that is very generalized and I would like to make it more...'''
date = "2013-06-14T21:19:00Z"
lastmod = "2013-06-17T00:50:00Z"
weight = 23381
keywords = [ "shapefile", "tracing", "editing" ]
aliases = [ "/questions/23381" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Uploading a shapefile to trace in OSM](/questions/23381/uploading-a-shapefile-to-trace-in-osm)

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
<span id="post-23381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23381-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am wondering if it is possible to upload a shapefile to edit vertices of a boundary layer in OSM and then delete the shapefile I used to trace on.</p>
<p>There is a small section of the international boundary between Chile and Argentina that is very generalized and I would like to make it more accurate.</p>
<p>Is this possible to do in OSM and if so how is the best way to do it.</p>
<p>Thanks</p>
<p>Ross</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-tracing" rel="tag" title="see questions tagged &#39;tracing&#39;">tracing</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '13, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/37535b669c1d85f4a122171b8a1507f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maps%20for%20Good&#39;s gravatar image" />
<p><span>Maps for Good</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maps for Good has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23381" class="comments-container">
<span id="23432"></span>
<div id="comment-23432" class="comment">
<div id="post-23432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>not your question - but please be sure that your intended use of the shapefiles (I do not know from where you got them) is complying with the license of the shapefile and with <span>OSM's</span> license/<a href="http://www.osmfoundation.org/wiki/License/Contributor_Terms">contributor terms</a>.</p>
</div>
<div id="comment-23432-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 00:36)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="23433"></span>
<div id="comment-23433" class="comment">
<div id="post-23433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(I did not really find this question to be a duplicate, but) you should also have a look at <span>previous questions on shapefiles</span> - may be useful.</p>
</div>
<div id="comment-23433-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 00:50)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23381-form-container" class="comment-form-container">
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

<span id="23426"></span>

<div id="answer-container-23426" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23426-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Open Potlatch 2 for the relevant area</li>
<li>In the 'Background' menu, click 'Vector data...'</li>
<li>Under 'Add new vector layer', click 'Shapefile'.</li>
<li>By 'File', click 'Open...' and locate a .zip of your shapefile (i.e. .shp, .shx and .dbf files).</li>
<li>When the file has loaded, find it in the list above, and change the style from 'Potlatch' to 'GPS'.</li>
<li>Close the dialogue box. Your shapefile should be displayed in the background in light blue.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '13, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23426" class="comments-container">
&#10;</div>
<div id="comment-tools-23426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23426-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23420"></span>

<div id="answer-container-23420" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23420-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some hints in the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Shapefiles">shapefiles</a> ... consider how to load a shapefile in an editor like JOSM or similar, ideally in a single layer.</p>
<p>Then try to modify the existing boundary according to the underlying shapefile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '13, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-23420" class="comments-container">
&#10;</div>
<div id="comment-tools-23420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23420-form-container" class="comment-form-container">
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

