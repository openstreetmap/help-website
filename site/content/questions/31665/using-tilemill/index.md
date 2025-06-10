+++
type = "question"
title = "Using TileMill"
description = '''How do load OpenStreetMap data into TileMill? How can I get the style to match Mapnik, could I use the Mapnik style directly. If you can, where do I get the stylesheet from?  If you can&#x27;t where can I get a style that exactly matches or is as close as possible to the Mapnik style used on web OSM map.'''
date = "2014-03-18T14:46:00Z"
lastmod = "2014-03-22T11:31:00Z"
weight = 31665
keywords = [ "tilemill", "osm", "style" ]
aliases = [ "/questions/31665" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using TileMill](/questions/31665/using-tilemill)

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
<span id="post-31665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31665-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do load OpenStreetMap data into TileMill? How can I get the style to match Mapnik, could I use the Mapnik style directly. If you can, where do I get the stylesheet from?<br />
</p>
<p>If you can't where can I get a style that exactly matches or is as close as possible to the Mapnik style used on web OSM map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '14, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/cd6f9338a5588f839cbaa01a3e21aad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deco2208&#39;s gravatar image" />
<p><span>deco2208</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deco2208 has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-31665" class="comments-container">
&#10;</div>
<div id="comment-tools-31665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31665-form-container" class="comment-form-container">
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

<span id="31667"></span>

<div id="answer-container-31667" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31667-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You do not download OSM data into TileMill. You load OSM data into a PostGIS database (which you install beforehand) using the osm2pgsql utility (which you install beforehand), and then you can use that database as a source for your map layers.</p>
<p>The style that powers openstreetmap.org is available <a href="https://github.com/gravitystorm/openstreetmap-carto">on GitHub;</a> be sure to follow the README carefully.</p>
<p>Note that this style cannot be modified in TileMill without some tricks, as it involves more files than fit into TileMill's tabbed edit pane.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '14, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31667" class="comments-container">
<span id="31756"></span>
<div id="comment-31756" class="comment">
<div id="post-31756-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to add a little bit to Frederik's answer, "using TileMill to work with data in a PostGIS database" is one of the steps in the <a href="https://www.mapbox.com/tilemill/docs/crashcourse/introduction/">TileMill "crash course"</a>. It's probably worth following that if you're interested in using TileMill with OSM data and the OSM "standard" map style.<br />
</p>
<p>Don't let "this style cannot be modified in TileMill without some tricks" put you off, as the main trick is to use an external editor to edit the relevant files, and TileMill is quite good at detecting external changes to files.</p>
</div>
<div id="comment-31756-info" class="comment-info">
<span class="comment-age">(22 Mar '14, 11:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31667" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31667-form-container" class="comment-form-container">
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

