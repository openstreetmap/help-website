+++
type = "question"
title = "Keep buildings only in osm file"
description = '''Hello! I&#x27;m trying to convert osm to kmz. I&#x27;ve found one solution, but I need to make osm much smaller.  How can I keep only buildings in osm file? It will be perfect to keep buildings outline only with height visulization like on screenshot.'''
date = "2016-12-19T13:48:00Z"
lastmod = "2016-12-21T16:41:00Z"
weight = 53610
keywords = [ "osmfilter" ]
aliases = [ "/questions/53610" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Keep buildings only in osm file](/questions/53610/keep-buildings-only-in-osm-file)

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
<span id="post-53610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53610-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I'm trying to convert osm to kmz. I've found one solution, but I need to make osm much smaller. <img src="https://lh6.googleusercontent.com/-0azPV5xcqRU/UThetPP9JCI/AAAAAAAAAMM/4WYBEnYzP0M/s800/buildings_big.jpg" alt="https://lh6.googleusercontent.com/-0azPV5xcqRU/UThetPP9JCI/AAAAAAAAAMM/4WYBEnYzP0M/s800/buildings_big.jpg" /></p>
<p>How can I keep only buildings in osm file? It will be perfect to keep buildings outline only with height visulization like on screenshot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '16, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/31fafeca5ba9d7301e05003775b9c81a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="squadgazzz&#39;s gravatar image" />
<p><span>squadgazzz</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="squadgazzz has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '16, 13:49</strong> </span></p>
</div>
</div>
<div id="comments-container-53610" class="comments-container">
<span id="53612"></span>
<div id="comment-53612" class="comment">
<div id="post-53612-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What is your current solution?</p>
</div>
<div id="comment-53612-info" class="comment-info">
<span class="comment-age">(19 Dec '16, 15:38)</span> <span class="comment-user userinfo">skorbut</span>
</div>
</div>
<span id="53619"></span>
<div id="comment-53619" class="comment">
<div id="post-53619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>convert OSM to OBJ &gt; convert OBJ to KMZ</p>
</div>
<div id="comment-53619-info" class="comment-info">
<span class="comment-age">(21 Dec '16, 06:18)</span> <span class="comment-user userinfo">squadgazzz</span>
</div>
</div>
</div>
<div id="comment-tools-53610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53610-form-container" class="comment-form-container">
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

<span id="53623"></span>

<div id="answer-container-53623" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53623-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="squadgazzz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> a very simple tool for such task:</p>
<pre><code>osmfilter my-data.osm --keep=building=* -o=my-data-buildings.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '16, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-53623" class="comments-container">
<span id="53624"></span>
<div id="comment-53624" class="comment">
<div id="post-53624-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you! do you maybe know a better way to visualize buildings height and convert file to kmz/kml for google earth? now I'm doing this - convert OSM to OBJ &gt; convert OBJ to KMZ. It doesnt work for files more than 100mb size. After filtering buildings I have 500mb size file..</p>
</div>
<div id="comment-53624-info" class="comment-info">
<span class="comment-age">(21 Dec '16, 11:38)</span> <span class="comment-user userinfo">squadgazzz</span>
</div>
</div>
<span id="53628"></span>
<div id="comment-53628" class="comment">
<div id="post-53628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you just want a visualization you can take a look at <a href="http://osm2world.org/">OSM2World</a>.</p>
</div>
<div id="comment-53628-info" class="comment-info">
<span class="comment-age">(21 Dec '16, 12:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53636"></span>
<div id="comment-53636" class="comment">
<div id="post-53636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/13098/squadgazzz">@squadgazz</a> I have not worked on OSM 3D building, so can not suggest on this.</p>
</div>
<div id="comment-53636-info" class="comment-info">
<span class="comment-age">(21 Dec '16, 16:41)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
</div>
<div id="comment-tools-53623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53623-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53618"></span>

<div id="answer-container-53618" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53618-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you familiar with the Overpass API? I've used Overpass Turbo to visualise a simple query to extract only building=* in your area:</p>
<p><a href="http://overpass-turbo.eu/s/kMy">http://overpass-turbo.eu/s/kMy</a></p>
<p>You can also get KML or geoJSON directly from the overpass API to import in Google Earth. In Overpass Turbo, go to 'Export', then choose the format you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '16, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/aace33beb0d1a608b0763ac8a2404049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stereo&#39;s gravatar image" />
<p><span>Stereo</span><br />
<span class="score" title="356 reputation points">356</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stereo has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '16, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-53618" class="comments-container">
<span id="53620"></span>
<div id="comment-53620" class="comment">
<div id="post-53620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cool,thanks. but how to visualize buildings height like on screenshot?</p>
</div>
<div id="comment-53620-info" class="comment-info">
<span class="comment-age">(21 Dec '16, 06:28)</span> <span class="comment-user userinfo">squadgazzz</span>
</div>
</div>
<span id="53621"></span>
<div id="comment-53621" class="comment">
<div id="post-53621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>also I have a problem with export the whole city. Moscow for example.. I already have osm file of this city(1500mb size). But don't know how to keep buildings only to make file much smaller</p>
</div>
<div id="comment-53621-info" class="comment-info">
<span class="comment-age">(21 Dec '16, 06:46)</span> <span class="comment-user userinfo">squadgazzz</span>
</div>
</div>
</div>
<div id="comment-tools-53618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53618-form-container" class="comment-form-container">
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

