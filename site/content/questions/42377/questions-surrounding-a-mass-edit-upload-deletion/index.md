+++
type = "question"
title = "Questions surrounding a mass edit / upload / deletion"
description = '''Right so i was initially tasked with validating and cleaning data over a large suburb of Harare in Zimbabwe. The data had recently been collected by members of the Red Cross in the ground in Harare and had been uploaded straight away without much cleaning having taken place. The main cleaning that n...'''
date = "2015-04-16T11:43:00Z"
lastmod = "2015-04-16T12:21:00Z"
weight = 42377
keywords = [ "edit", "josm", "mass", "upload", "overpass" ]
aliases = [ "/questions/42377" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Questions surrounding a mass edit / upload / deletion](/questions/42377/questions-surrounding-a-mass-edit-upload-deletion)

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
<span id="post-42377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42377-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Right so i was initially tasked with validating and cleaning data over a large suburb of Harare in Zimbabwe. The data had recently been collected by members of the Red Cross in the ground in Harare and had been uploaded straight away without much cleaning having taken place. The main cleaning that needed to be done was on the address attributes of all of the houses (~5000) that had been mapped (Just to be clear here - i'm not editing anything more than attribute data). This involved making sure that the 'addr:street' attribute data was formatted correctly - ie 18robertmugsabe way -&gt; 18 Robert Mugabe Way etc. The 'addr:housenumber' attribute also needed to be cleaned to ensure consistency in the syntax - ie 699a-b, 699 ab, 699A. B ---&gt; 699A/B. I also plan to sense-check the data to ensure the houses are on the right roads, street names are correct e.t.c.</p>
<p>I approached this initially by doing an overpass query of all of the edits done by the username of the person who had made all of the uploads in the area. I then downloaded the results as a geoJSON (Points, Lines and Polygons). I then converted these seperate geoJSON files to shapefiles. From here i extracted the 'addr:housenumber' and 'addr:street' fields from the attribute tables and brought them in to excel to perform formatting formulas on the syntax of the data. I then replaced the original attribute columns with the newly edited ones in the shapefile (all the while retaining the integrity of the id field and making sure the edits were appended to the correct polygons). At this stage i could bring in the shapefile to JOSM and re-save it as an .osm file. I was hopeful that the conflation plugin would be able to manage merging in the new attribute data but seems to throw up a conflict for everything i'm trying to change. I still have a small hope that this plugin might be able to manage it in some way but need some advice. Next (using a small 2 building sample) i tried simply uploading the .osm file but expectedly it simply placed all of its data on top of the already existing data. What i am now thinking is that this upload could still work but only through downloading all of the relevant osm data in JOSM, deleting it and then uploading the new .osm files (Line, Point, Polygon) in its place.</p>
<p>Is this a viable method? Would it throw up red flags galore? I am hoping that as this process is primarily concerned with improving the formatting and syntax of data that is currently there it might be viewed more favorably as opposed to a mass editing, deleting or upload of geometry data. Any help would be greatly appreciated, Cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-mass" rel="tag" title="see questions tagged &#39;mass&#39;">mass</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '15, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/63dec29ad008d3c8ef14e72e91393e75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jamie2483&#39;s gravatar image" />
<p><span>Jamie2483</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jamie2483 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42377" class="comments-container">
&#10;</div>
<div id="comment-tools-42377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42377-form-container" class="comment-form-container">
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

<span id="42382"></span>

<div id="answer-container-42382" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42382-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have really created too many layers of indirection through changing the format of the data to have much hope of successfully merging it back. A large scale delete and replace is probably not appropriate as it is reasonable to alter the data <em>in situ</em>. It is important to ensure that you have the skills and knowledge to so this suitably.</p>
<p>I would suggest the following alternative in JOSM:</p>
<ul>
<li>Download the area as OSM XML (you can use overpass to do this if it is too large for the API)</li>
<li>Work through your corrections either with JOSM or potentially with a text editor.</li>
<li>Check the work with JOSM validator</li>
<li>Update the area in case it has been edited in the meantime, to avoid further conflicts.</li>
<li>Finally update the area.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '15, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-42382" class="comments-container">
&#10;</div>
<div id="comment-tools-42382" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42382-form-container" class="comment-form-container">
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

