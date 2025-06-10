+++
type = "question"
title = "OSM data and dates"
description = '''Hi, I&#x27;m trying to export data from Tacloban city and Palo in Philippines for a period of time, from 7th to 25th of November. Could anyone tell me how to select data depending on the upload date? I&#x27;m also having problems with the Export options'''
date = "2013-12-10T09:31:00Z"
lastmod = "2013-12-12T10:24:00Z"
weight = 28951
keywords = [ "osmdate" ]
aliases = [ "/questions/28951" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM data and dates](/questions/28951/osm-data-and-dates)

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
<span id="post-28951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28951-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to export data from Tacloban city and Palo in Philippines for a period of time, from 7th to 25th of November. Could anyone tell me how to select data depending on the upload date? I'm also having problems with the Export options</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmdate" rel="tag" title="see questions tagged &#39;osmdate&#39;">osmdate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '13, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/5ce44dbf703bf8ddd04e69d3248fa560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udonezar&#39;s gravatar image" />
<p><span>udonezar</span><br />
<span class="score" title="45 reputation points">45</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udonezar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28951" class="comments-container">
&#10;</div>
<div id="comment-tools-28951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28951-form-container" class="comment-form-container">
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

<span id="28955"></span>

<div id="answer-container-28955" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28955-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Two quick answers: there is no way to extract data for a given time interval through API calls; you are probably trying to use the export option with too large a set of data.</p>
<p>From time to time OSM history export files <a href="https://wiki.openstreetmap.org/wiki/Planet.osm/full">are made</a>: these contain the history of every object. I dont think there is a recent one.</p>
<p>Probably the best way to achieve what you want is to download a Philippines extract from November at <a href="http://download.geofabrik.de/asia/philippines.html#">Geofabrik</a>. Intermediate states can be achieved by applying these <a href="http://download.geofabrik.de/asia/philippines-updates/000/000/">OSM change</a> files in sequence using <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>.</p>
<p>If you are planning to make a video of changes over this period I would recommend following Derick Rethans talk at <a href="http://lanyrd.com/2013/sotm/scpkgh/">SotM</a> in Birmingham.</p>
<p>If you want to store every change in PostGIS then you will need to do some (significant) work on your own. There are some hints in an old blog post of <a href="http://sk53-osm.blogspot.com/2011/05/on-histories-of-openstreetmap-data.html">mine</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '13, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '13, 10:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-28955" class="comments-container">
<span id="28957"></span>
<div id="comment-28957" class="comment">
<div id="post-28957-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is in fact software that can import a full history file into PostgreSQL an make animations from it, see <a href="https://github.com/MaZderMind/osm-history-renderer">https://github.com/MaZderMind/osm-history-renderer</a> - you might have to cut out a region before using <a href="https://github.com/MaZderMind/osm-history-splitter.">https://github.com/MaZderMind/osm-history-splitter.</a> Currently the latest full history file available is from 05 November.</p>
</div>
<div id="comment-28957-info" class="comment-info">
<span class="comment-age">(10 Dec '13, 10:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="28958"></span>
<div id="comment-28958" class="comment">
<div id="post-28958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much. I still have the doubt: how can I open .osc files? I have already Quantum GIS downloaded and it seems to work well with .osm files, but it does not recognize osc, does it?</p>
</div>
<div id="comment-28958-info" class="comment-info">
<span class="comment-age">(10 Dec '13, 11:19)</span> <span class="comment-user userinfo">udonezar</span>
</div>
</div>
<span id="29001"></span>
<div id="comment-29001" class="comment">
<div id="post-29001-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>An .osc will only contain the changes, not the complete data set, so that would mean nothing to QGIS. If you want to use OSM data you need to use complete dumps or extracts.</p>
</div>
<div id="comment-29001-info" class="comment-info">
<span class="comment-age">(12 Dec '13, 10:24)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-28955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28955-form-container" class="comment-form-container">
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

