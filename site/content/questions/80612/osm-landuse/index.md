+++
type = "question"
title = "OSM landuse"
description = '''In recent years I have been making use of the OSM land use polygon layer in my work. However, it can be quite patchy. In the UK there are huge areas missing and in the Netherlands the polygons overlap. The online map OSMlanduse.org exists and is far more comprehensive. Is this a map connected with t...'''
date = "2021-06-18T08:14:00Z"
lastmod = "2021-06-18T16:57:00Z"
weight = 80612
keywords = [ "landuse" ]
aliases = [ "/questions/80612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSM landuse](/questions/80612/osm-landuse)

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
<span id="post-80612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80612-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In recent years I have been making use of the OSM land use polygon layer in my work. However, it can be quite patchy. In the UK there are huge areas missing and in the Netherlands the polygons overlap. The online map OSMlanduse.org exists and is far more comprehensive.</p>
<p>Is this a map connected with the open street map layers? If so is it waiting for someone to implement them?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '21, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/7e13807c5ea6f83e9faffa9755118cf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blaiseo&#39;s gravatar image" />
<p><span>Blaiseo</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blaiseo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80612" class="comments-container">
<span id="80615"></span>
<div id="comment-80615" class="comment">
<div id="post-80615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I emailed Alexander Zipf last year and he replied to say the improvements would be available soon but no more details. I emailed again the other day to check.</p>
<p>However, this team has put a huge amount of effort into improving the accuracy of the landuse model, I don't want to nag them to add to OSM. I was wondering if there is already some collaboration? When this data is available (to my mind it is already very accurate and does not need to wait for checking) who would implement the changes?</p>
</div>
<div id="comment-80615-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 09:31)</span> <span class="comment-user userinfo">Blaiseo</span>
</div>
</div>
<span id="80620"></span>
<div id="comment-80620" class="comment">
<div id="post-80620-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's a fair amount of additional material about how to use OSM Landuse elsewhere: for instance I looked at how OSM compared with the CEC Urban Atlas for various places. Presentation at SotM-11. Igor Brekic also looked at Vienna some time past. The basic approach as by the Heidelberg term is: some basic conversion of tags to landuse categories, sensible defaults (farmland works well in lowland Britain), a polygon merge &amp; clipping process, based on an order priority of categories (a simple painter's algorithm worked for me). Additional processes for recognising urban areas have also been documented. Lastly some judicious use of other sources can fill some voids (e.g., Corine woodland in Ireland, other national datasets).</p>
</div>
<div id="comment-80620-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 12:10)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80626"></span>
<div id="comment-80626" class="comment">
<div id="post-80626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting to know. I will look up the CEC atlas.</p>
<p>What I am mainly getting at is the osmlanduse website is called OSM, implying it is some how connected with the OSM geofabrik data.</p>
<p>In any case rather than trying to replicate the work of Heidelberg, would it be possible to use the dataset they have put together?</p>
</div>
<div id="comment-80626-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 14:02)</span> <span class="comment-user userinfo">Blaiseo</span>
</div>
</div>
<span id="80627"></span>
<div id="comment-80627" class="comment">
<div id="post-80627-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If they haven't released it then you can't use it other than as a WMS. Yes of course the site is based on OSM data, but they enhance it using their own, probably proprietary, algorithms. They may of course provide some kind of paid service too (after all if you are using it for commercial purposes, it's not unreasonable).</p>
<p>OSM data is likely to be much better than CLC Corine when it is more than imported Corine data (which is why coverage of landuse is good in many EU countries). OSM is more likely to be properly aligned at changes in landuse; is often more granular, and because it is generally not dependent on remote sensing avoids some classification errors.</p>
</div>
<div id="comment-80627-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 16:16)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80628"></span>
<div id="comment-80628" class="comment">
<div id="post-80628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The accuracy and resolution of osmlanduse.org is far and away better than what is currently available from geofabrik for the UK and NL.</p>
</div>
<div id="comment-80628-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 16:57)</span> <span class="comment-user userinfo">Blaiseo</span>
</div>
</div>
</div>
<div id="comment-tools-80612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

