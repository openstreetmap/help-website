+++
type = "question"
title = "Basic method for downloading ways within a region"
description = '''Hi,  I&#x27;m writing a Java Android app that requires me to download all the ways within a certain region but can find no example of a method for doing so. Could anyone point me in the right direction? Many thanks'''
date = "2020-02-26T01:58:00Z"
lastmod = "2020-02-26T11:38:00Z"
weight = 73233
keywords = [ "ways", "android", "java" ]
aliases = [ "/questions/73233" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Basic method for downloading ways within a region](/questions/73233/basic-method-for-downloading-ways-within-a-region)

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
<span id="post-73233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73233-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm writing a Java Android app that requires me to download all the ways within a certain region but can find no example of a method for doing so.</p>
<p>Could anyone point me in the right direction?</p>
<p>Many thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '20, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/754e2add86ca3b2c635d07dd996f616c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wally&#39;s gravatar image" />
<p><span>Wally</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wally has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73233" class="comments-container">
&#10;</div>
<div id="comment-tools-73233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73233-form-container" class="comment-form-container">
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

<span id="73237"></span>

<div id="answer-container-73237" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73237-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Large scale <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extracts</a> are served by several providers based on the main <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">planet file</a>.</p>
<p>Any filtering for the feature types you're after will probably need to be done on your servers according to your specific criteria. (<a href="">Osmosis</a> seems frequently mentions in this forum for such taks but I have no first hand knowledge of this.)</p>
<p>I believe the likes of OsmAnd pull whole planet dumps and keep them updated with the minutely diffs. These are then run through their conversion software and then split into the region's their users can download in app. For subscription customers this is done on an hourly basis.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis">https://wiki.openstreetmap.org/wiki/Osmosis</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '20, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-73237" class="comments-container">
&#10;</div>
<div id="comment-tools-73237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73237-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73239"></span>

<div id="answer-container-73239" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73239-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure you only want the ways - without the accompanying nodes you will not know the geometry of the ways (just "there is a street named X with speed limit Y somewhere in the area I requested")? And without the relations you will also miss some semantic information - what looks to you like two featureless ways can turn out to be a building if you look at the relation that combines the two.</p>
<p>A common tool for downloading data in an area is Overpass. Its query language is described here <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a> and an example that does what you want is here <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Usage_examples:_All_data_in_a_bounding_box.">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Usage_examples:_All_data_in_a_bounding_box.</a> There are a couple of free and public Overpass servers (see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances)">https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances)</a> however if your app makes intensive use of the service and/or you need to rely on it you should probably set up your own server (everything is Open Source).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '20, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73239" class="comments-container">
<span id="73242"></span>
<div id="comment-73242" class="comment">
<div id="post-73242-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the replies.</p>
<p>Basically what I'm after is all the walkable highways - i.e. roads and paths - within a region and I want to be able to extract the routes as sequences of coordinates which, as I understand it I can extract from the nodes.</p>
<p>I should say I'm very new to OSM and am finding it hard to find a straightforward introduction to the data types and how they can be used within a java program.</p>
<p>Many thanks for your help.</p>
</div>
<div id="comment-73242-info" class="comment-info">
<span class="comment-age">(26 Feb '20, 11:38)</span> <span class="comment-user userinfo">Wally</span>
</div>
</div>
</div>
<div id="comment-tools-73239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73239-form-container" class="comment-form-container">
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

