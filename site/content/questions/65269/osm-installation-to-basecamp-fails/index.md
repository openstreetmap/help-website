+++
type = "question"
title = "OSM installation to BaseCamp fails"
description = '''I have an OSM map for a small portion (about 100 km squared) of Senegal (in the following I will call this the small map). A few months ago I succeeded in moving it into BaseCamp using MKGMAP and MapSetToolKit. I am using Windows 7 Professional and BaseCamp 4.6.2. All was fine until I tried to insta...'''
date = "2018-08-11T09:24:00Z"
lastmod = "2018-08-12T16:47:00Z"
weight = 65269
keywords = [ "mapsettoolkit", "basecamp" ]
aliases = [ "/questions/65269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM installation to BaseCamp fails](/questions/65269/osm-installation-to-basecamp-fails)

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
<span id="post-65269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65269-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an OSM map for a small portion (about 100 km squared) of Senegal (in the following I will call this the small map). A few months ago I succeeded in moving it into BaseCamp using MKGMAP and MapSetToolKit. I am using Windows 7 Professional and BaseCamp 4.6.2.</p>
<p>All was fine until I tried to install another OSM map of a larger area including the smaller one (I got it by using splitter to divide the too-large Senegal and Gambia OSM map into 4 sub-maps to use with Garmiin). I installed this map (which in the following I will cll the large map) with MapSetToolKit (using another family ID), and it said OK, but I could not see it in JaVaWa GMTK or in BaseCamp (but I could still switch between and use the small map and the Global Map).</p>
<p>I tried uninstalling with MapSetToolKit both the large map and the small map, and now I can't install either one of these maps separately (MapSetToolKit says the installation is complete, but I can't see the installed map in either JaVaWa GMTK or BaseCamp.</p>
<p>When all OSM maps are uninstalled with MapSetToolKit, there are no remaining references to the maps in the Registry. No improvement if reboot the system.</p>
<p>Hope that someone can give me some ideas on what to do, thanks and best wishes, John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapsettoolkit" rel="tag" title="see questions tagged &#39;mapsettoolkit&#39;">mapsettoolkit</span> <span class="post-tag tag-link-basecamp" rel="tag" title="see questions tagged &#39;basecamp&#39;">basecamp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '18, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/3175f25352985a6a23ae68f364e3deaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Rose&#39;s gravatar image" />
<p><span>John_Rose</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Rose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65269" class="comments-container">
&#10;</div>
<div id="comment-tools-65269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65269-form-container" class="comment-form-container">
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

<span id="65287"></span>

<div id="answer-container-65287" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65287-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This problem was due to the fact that MapSetToolKit apparently has to be executed as Administrator. Else, even though it can add the appropriate registry items to access the new map, the map is not installed. Sorry and thanks for your attention, John</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '18, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/3175f25352985a6a23ae68f364e3deaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Rose&#39;s gravatar image" />
<p><span>John_Rose</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Rose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65287" class="comments-container">
&#10;</div>
<div id="comment-tools-65287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65287-form-container" class="comment-form-container">
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

