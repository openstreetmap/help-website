+++
type = "question"
title = "How To Bulk Update Incline Tags"
description = '''Hi Everyone,  I am currently working on a project to optimize the wheelchair navigation routes using OpenStreetMap and one way I thought of is to complete the inclination details of each line segment using elevation models. Would it be possible to find and update the osmids and update the incline ta...'''
date = "2022-04-20T00:39:00Z"
lastmod = "2022-04-25T07:22:00Z"
weight = 84229
keywords = [ "osm.pbf", "incline", "tagging", "routing" ]
aliases = [ "/questions/84229" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How To Bulk Update Incline Tags](/questions/84229/how-to-bulk-update-incline-tags)

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
<span id="post-84229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84229-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Everyone,</p>
<p>I am currently working on a project to optimize the wheelchair navigation routes using OpenStreetMap and one way I thought of is to complete the inclination details of each line segment using elevation models. Would it be possible to find and update the osmids and update the incline tag value by bulk on my local osm file? What should I need to use for that?</p>
<p>I have downloaded the data from OSM and I wanted to edit the data on that file and use it for my local navigation to check if it works. I tried using QGIS but it seems that it cannot make everything to .osm again after transforming the data to osm2pgsql as it does not work on my local OpenRouteService as the relationship of the nodes and way segments are gone.</p>
<p>Please Advise, Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span> <span class="post-tag tag-link-incline" rel="tag" title="see questions tagged &#39;incline&#39;">incline</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '22, 00:39</strong></p>
<img src="https://secure.gravatar.com/avatar/bf533d13343aa3f444473fb0b21ab35b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metono&#39;s gravatar image" />
<p><span>Metono</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metono has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84229" class="comments-container">
&#10;</div>
<div id="comment-tools-84229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84229-form-container" class="comment-form-container">
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

<span id="84233"></span>

<div id="answer-container-84233" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84233-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I cannot answer on the technical aspects. But I'd like to voice my view on the approach in general.</p>
<p>Firstly, information that gets added to the OSM database should be <a href="https://wiki.openstreetmap.org/wiki/Good_practice#Map_what.27s_on_the_ground">observable on the ground</a> and <a href="https://wiki.openstreetmap.org/wiki/Verifiability">verifiable</a>. This includes that the mappers themselves only map what they have surveyed or can objectively derive from other sources. Elevation models lack the precision which is needed to correctly add information to small local objects in my opinion. Relying on the statistics and technical limitations in elevation models contradicts ground truth.</p>
<p>There are many services that add elevation model data to the OSM data during their processing chain (e.g. to add contour lines on maps or as in your case to find routes with minimal inclination), though, without adding the additional data into the main OSM database. One router doing it I know of is <a href="https://brouter.de/">BRouter</a> but there are probably more. Please also investigate that direction.</p>
<p>Secondly, bulk editing anything is not an easy task. There are guidelines that govern how bulk uploads have to be handled (<a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a>, <a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">Automated Edits code of conduct</a>). Please read and understand those before you continue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '22, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-84233" class="comments-container">
<span id="84234"></span>
<div id="comment-84234" class="comment">
<div id="post-84234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your insight regarding this matter, Although the approach I am currently checking would most probably not go to the main OSM servers to our local OSM server only, this is to see and compare how our modelled routing algorithms fair with public ones such as Google and other routing applications.</p>
<p>But would you know if it would be possible to edit the local osm file by bulk for example add incline values to osmids? I have tried using osm2pgsql but I am not sure how to export back to an osm file.</p>
</div>
<div id="comment-84234-info" class="comment-info">
<span class="comment-age">(20 Apr '22, 21:48)</span> <span class="comment-user userinfo">Metono</span>
</div>
</div>
<span id="84240"></span>
<div id="comment-84240" class="comment">
<div id="post-84240-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think OSRM has this functionality via a call in LUA (process_way), see <a href="https://github.com/Project-OSRM/osrm-backend/blob/41dda32546399f1dc12af1de41668993de44c7dc/docs/profiles.md">https://github.com/Project-OSRM/osrm-backend/blob/41dda32546399f1dc12af1de41668993de44c7dc/docs/profiles.md</a> and search for elevation</p>
</div>
<div id="comment-84240-info" class="comment-info">
<span class="comment-age">(21 Apr '22, 13:47)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84233-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84266"></span>

<div id="answer-container-84266" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84266-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So just to update others that might need also a way to do this.</p>
<p>I was able to update tags of the local osm.pbf file using osmosis(import) -&gt; postgres (edit all tags in hstore) -&gt; osmosis (export to .osm) -&gt; josm save file as .osm.pbf</p>
<p>The problem now is that the overpass API does not recognize the updated tags, Does someone have any experience in making a custom tag for a local overpass API server?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '22, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/bf533d13343aa3f444473fb0b21ab35b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metono&#39;s gravatar image" />
<p><span>Metono</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metono has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84266" class="comments-container">
<span id="84267"></span>
<div id="comment-84267" class="comment">
<div id="post-84267-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sounds like you should ask a new question about this :)</p>
</div>
<div id="comment-84267-info" class="comment-info">
<span class="comment-age">(25 Apr '22, 07:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84266-form-container" class="comment-form-container">
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

