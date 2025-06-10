+++
type = "question"
title = "Trying to import POIs into OsmAnd"
description = '''I have over the years created, on my TomTom GO Live 825, 4 groups of ov2 waypoints (850 in all) of places I want to visit or have visited. I have exported them to my computer, then converted them to kml format for importing into Magic Earth navigator. That works fine and all waypoints appear in the ...'''
date = "2021-09-22T17:53:00Z"
lastmod = "2021-09-24T19:08:00Z"
weight = 81860
keywords = [ "imports", "osmand" ]
aliases = [ "/questions/81860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to import POIs into OsmAnd](/questions/81860/trying-to-import-pois-into-osmand)

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
<span id="post-81860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have over the years created, on my TomTom GO Live 825, 4 groups of ov2 waypoints (850 in all) of places I want to visit or have visited. I have exported them to my computer, then converted them to kml format for importing into Magic Earth navigator. That works fine and all waypoints appear in the original 4 POI folders. Now I am trying to do the same thing with OsmAnd. So I have converted the ov2 folders to gpx folders and tried to import them, only to be faced with the message "Import tracks Cannot import specified GPX file". Does anyone know if I'm just being dense, because I'm trying to do the impossible, or could it be that until I download all the relevant maps (France, England, Scotland, Wales, Germany, Belgium, Holland, Switzerland and Italy) the app won't accept the files because most of them won't have a 'home'. I have tried changing the name of the folder to favourites.gpx (to match the folder name that the favourites that I have created in the app are saved to); I have tried creating a new My Places folder to match the name of the folder that my waypoints are stored in. But I still get the same error message. Anyone got any ideas? Thank you Maxdot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imports" rel="tag" title="see questions tagged &#39;imports&#39;">imports</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '21, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/dfdf8972b88b383c2d936c5320bf2f6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maxdot&#39;s gravatar image" />
<p><span>Maxdot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maxdot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81860" class="comments-container">
&#10;</div>
<div id="comment-tools-81860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81860-form-container" class="comment-form-container">
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

<span id="81942"></span>

<div id="answer-container-81942" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81942-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the past I have successfully merged two <code>favourites.gpx</code> files from two devices to give a single set of favourites. My sync solution seems to indicate that it is still being used for favourites storage (at least on my version of Android).</p>
<p>I don't think what maps you have downloaded should matter as far as favourites are concerned.</p>
<p>I'm a little confused about your use of the word folder. The <code>favourites.gpx</code> file exits in the top level of the OsmAnd folder structure and contains all points. The folders shown in OsmAnd appear to reflect the contents of a <code>type</code> entry in the individual <code>wpt</code> points. If you have another file with other points you may need to do a bit of manual copy pasting to merge them in your preferred text editor.</p>
<p>If the import procedure described <a href="https://docs.osmand.net/en/main@latest/osmand/personal/favorites#export--import">here</a> doesn't work for you. Then you might need to have a deeper look at the gpx file your other software is exporting to make sure they're in as points and not tracks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '21, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-81942" class="comments-container">
&#10;</div>
<div id="comment-tools-81942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81942-form-container" class="comment-form-container">
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

