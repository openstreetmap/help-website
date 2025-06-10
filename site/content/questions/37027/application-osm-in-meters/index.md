+++
type = "question"
title = "Application OSM in meters"
description = '''Hello,  I am currently working on an application which would display a map and our position indoors. Not to go in precise details, we would like to display everything in meters from an fixed position (x,y) inside the building, so that we can get rid of latitude and longitude.  To do so, I have my .o...'''
date = "2014-09-24T14:57:00Z"
lastmod = "2014-09-24T17:20:00Z"
weight = 37027
keywords = [ "convert", "osm" ]
aliases = [ "/questions/37027" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Application OSM in meters](/questions/37027/application-osm-in-meters)

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
<span id="post-37027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37027-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am currently working on an application which would display a map and our position indoors. Not to go in precise details, we would like to display everything in meters from an fixed position (x,y) inside the building, so that we can get rid of latitude and longitude.</p>
<p>To do so, I have my .osm files filled with latitudes and longitudes. I would like to create a new file (.osm or .csv) which would give for each node an (x,y) position.</p>
<p>Am I obliged to use osmconvert or is there a quicker solution with java (like parsing the osm file and creating a new sml file) ? My problem is that I do not know how to only take the information latitude or longitude given the disposition of the osm file....</p>
<p>I hope I've been clear enough ... Can anyone help ?!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '14, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/28eeb69e71a847b72b512618901472a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laVial&#39;s gravatar image" />
<p><span>laVial</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laVial has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37027" class="comments-container">
&#10;</div>
<div id="comment-tools-37027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37027-form-container" class="comment-form-container">
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

<span id="37035"></span>

<div id="answer-container-37035" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37035-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unless you need very high optimisations (in which case you probably don't want to use an unconverted *.osm file anyway), I wouldn't bother modifying the input file, it looks like too many opportunities for confusion.</p>
<p>Convert the coordinates at load time instead, if you really need to (I'm not sure I see the usecase). Use a library like <a href="http://trac.osgeo.org/proj4j/">proj4j</a> (you didn't specify what language you were using), choose your <a href="https://en.wikipedia.org/wiki/List_of_map_projections">projection</a> (equirectangular will probably suit you best in this case), and translate all nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '14, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-37035" class="comments-container">
&#10;</div>
<div id="comment-tools-37035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37035-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37034"></span>

<div id="answer-container-37034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37034-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Consult the <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">documentation of osmconvert</a> in the OSM wiki.</p>
<p>It has a feature to export a CSV file e.g. with x and y coordinates of each OSM data element from an OSM xml source file.</p>
<p>And: osmconvert is (next to osmfilter) a very fast tool, compared to osmosis ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '14, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-37034" class="comments-container">
&#10;</div>
<div id="comment-tools-37034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37034-form-container" class="comment-form-container">
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

