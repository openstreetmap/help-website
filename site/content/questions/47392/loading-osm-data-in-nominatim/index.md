+++
type = "question"
title = "Loading OSM Data in Nominatim"
description = '''Hi All, I have installed nominatim with the instructions mentioned in the link -  http://wiki.openstreetmap.org/wiki/Nominatim/Installation Currently the database contains the data of Luxembourg. I would like to add the data of Great Britain. In order to do this i did the following  Downloaded engla...'''
date = "2016-01-06T12:43:00Z"
lastmod = "2016-01-18T16:06:00Z"
weight = 47392
keywords = [ "load", "import", "nominatim", "osm" ]
aliases = [ "/questions/47392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Loading OSM Data in Nominatim](/questions/47392/loading-osm-data-in-nominatim)

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
<span id="post-47392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I have installed nominatim with the instructions mentioned in the link -</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p>
<p>Currently the database contains the data of Luxembourg. I would like to add the data of Great Britain. In order to do this i did the following</p>
<ul>
<li>Downloaded england-latest.osm.pbf , scotland-latest.osm.pbf and wales-latest.osm.pbf from <a href="http://download.geofabrik.de/europe/great-britain.html">http://download.geofabrik.de/europe/great-britain.html</a></li>
<li><p>Ran the following commands</p>
<p>./setup.php --osm-file "/etc/Nominatim/OSMDATA/england-latest.osm.pbf" --import-data</p></li>
</ul>
<p>./setup.php --osm-file "/etc/Nominatim/OSMDATA/scotland-latest.osm.pbf" --import-data</p>
<p>./setup.php --osm-file "/etc/Nominatim/OSMDATA/wales-latest.osm.pbf" --import-data</p>
<ul>
<li>Ran the command ./setup.php --load-data</li>
<li>Ran the command ./setup.php --index</li>
</ul>
<p>Is this the correct way to load new OSM Files to Nominatim. Please help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-load" rel="tag" title="see questions tagged &#39;load&#39;">load</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '16, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/24f2806428020415139cd9bcd5165482?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sabarish_attinad&#39;s gravatar image" />
<p><span>Sabarish_att...</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sabarish_attinad has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '16, 13:15</strong> </span></p>
</div>
</div>
<div id="comments-container-47392" class="comments-container">
&#10;</div>
<div id="comment-tools-47392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47392-form-container" class="comment-form-container">
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

<span id="47563"></span>

<div id="answer-container-47563" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47563-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Followed the solution mentioned in the post</p>
<p><a href="https://help.openstreetmap.org/questions/15505/import-more-osm-files-in-to-nominatim">https://help.openstreetmap.org/questions/15505/import-more-osm-files-in-to-nominatim</a></p>
<p>The index is slow, but the process works !!!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '16, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/24f2806428020415139cd9bcd5165482?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sabarish_attinad&#39;s gravatar image" />
<p><span>Sabarish_att...</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sabarish_attinad has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-47563" class="comments-container">
&#10;</div>
<div id="comment-tools-47563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47563-form-container" class="comment-form-container">
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

