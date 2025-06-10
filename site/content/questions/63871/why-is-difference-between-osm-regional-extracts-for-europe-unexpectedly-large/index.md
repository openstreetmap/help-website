+++
type = "question"
title = "Why is difference between OSM regional extracts for Europe unexpectedly large?"
description = '''Note: this is crosspost of https://gis.stackexchange.com/questions/284608/difference-between-osm-regional-extracts-unexpectedly-large I want to create a difference (change file) between two Europe extracts from OSM data. The files I want to compare are:  http://download.geofabrik.de/europe-180401.os...'''
date = "2018-05-30T14:34:00Z"
lastmod = "2018-06-05T15:09:00Z"
weight = 63871
keywords = [ "comparison", "osmconvert", "diff" ]
aliases = [ "/questions/63871" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is difference between OSM regional extracts for Europe unexpectedly large?](/questions/63871/why-is-difference-between-osm-regional-extracts-for-europe-unexpectedly-large)

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
<span id="post-63871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63871-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><em>Note: this is crosspost of <a href="https://gis.stackexchange.com/questions/284608/difference-between-osm-regional-extracts-unexpectedly-large">https://gis.stackexchange.com/questions/284608/difference-between-osm-regional-extracts-unexpectedly-large</a></em></p>
<p>I want to create a difference (change file) between two Europe extracts from OSM data. The files I want to compare are:</p>
<ul>
<li><a href="http://download.geofabrik.de/europe-180401.osm.pbf">http://download.geofabrik.de/europe-180401.osm.pbf</a></li>
<li><a href="http://download.geofabrik.de/europe-latest.osm.pbf">http://download.geofabrik.de/europe-latest.osm.pbf</a></li>
</ul>
<p>As the files are quite large, before running on them I have tried the processing on smaller extracts:</p>
<ul>
<li><a href="http://download.geofabrik.de/czech-republic-180401.osm.pbf">http://download.geofabrik.de/czech-republic-180401.osm.pbf</a></li>
<li><a href="http://download.geofabrik.de/czech-republic-latest.osm.pbf">http://download.geofabrik.de/czech-republic-latest.osm.pbf</a></li>
</ul>
<p>The workflow I use is:</p>
<ul>
<li>first convert <code>xxx-180401.osm.pbf</code> to <code>xxx-ref.o5m</code>, then create the diff:</li>
</ul>
<p><code>osmconvert europe-180401.osm.pbf -o=eu-ref.o5m</code></p>
<p><code>osmconvert eu-ref.o5m europe-latest.osm.pbf --diff -o=eu-changes.o5c</code></p>
<p>Or:</p>
<p><code>osmconvert czech-republic-180401.osm.pbf -o=cz-ref.o5m</code></p>
<p><code>osmconvert cz-ref.o5m czech-republic-latest.osm.pbf --diff -o=cz-changes.o5c</code></p>
<p>The process works fine with the Czech Republic data. The resulting <code>o5c</code> file looks reasonable, its size is ~30 MB (the Czech Republic input file is ~700 MB).</p>
<p>I get strange results with the Europe extract. The resuling <code>o5c</code> file is ~40 GB, while the Europe input is ~20 GB. When inspecting the file, I have found many instances of data which was not changed on OSM in this year at all, like <a href="https://www.openstreetmap.org/way/539372444">way 539372444</a>.</p>
<p>I have also tried doing the comparison using Osmium instead of Osmconvert, but the result was the same, the change file was huge.</p>
<p>Am I doing something wrong, or are the Europe extracts unsuitable for the comparison for some reason?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-comparison" rel="tag" title="see questions tagged &#39;comparison&#39;">comparison</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '18, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/2bd7c0e93b52c224e284d18ac34752b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ondrej%20Spanel&#39;s gravatar image" />
<p><span>Ondrej Spanel</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ondrej Spanel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63871" class="comments-container">
<span id="63872"></span>
<div id="comment-63872" class="comment">
<div id="post-63872-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you downloaded the 20180401 file for Europe in April, or in May?</p>
</div>
<div id="comment-63872-info" class="comment-info">
<span class="comment-age">(30 May '18, 14:50)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63873"></span>
<div id="comment-63873" class="comment">
<div id="post-63873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In May - just a few days ago, same as the Czech republic extract.</p>
</div>
<div id="comment-63873-info" class="comment-info">
<span class="comment-age">(30 May '18, 14:59)</span> <span class="comment-user userinfo">Ondrej Spanel</span>
</div>
</div>
</div>
<div id="comment-tools-63871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63871-form-container" class="comment-form-container">
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

<span id="63874"></span>

<div id="answer-container-63874" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63874-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ondrej Spanel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've likely become a casuality to GDPR-related changes on the Geofabrik download server where we've removed user information from download files. It is possible that the two files you are comparing have a different method of removing user data (one has NO user data, the other has fake user data with uid=0) and this confuses the program that computes the diffs.</p>
<p>You could either try removing the user, uid and changeset fields from both files before you compare, or you could download the old-style, complete files from osm-internal.download.geofabrik.de.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '18, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63874" class="comments-container">
<span id="63875"></span>
<div id="comment-63875" class="comment">
<div id="post-63875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Given osmcompare diff does not use content, only version numbers, how can metadata removal affect this? (Cf. <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Retrieving_the_Differences_between_two_OSM_Files)">https://wiki.openstreetmap.org/wiki/Osmconvert#Retrieving_the_Differences_between_two_OSM_Files)</a></p>
</div>
<div id="comment-63875-info" class="comment-info">
<span class="comment-age">(30 May '18, 15:15)</span> <span class="comment-user userinfo">Ondrej Spanel</span>
</div>
</div>
<span id="63876"></span>
<div id="comment-63876" class="comment">
<div id="post-63876-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Inspecting result of conversion to OSM answers this immediately: europe-180401 is completely missing <code>version</code> attribute. If this is result of GDPR data removal, I think it is oversight, as version number does not seem like a personal data to me.</p>
</div>
<div id="comment-63876-info" class="comment-info">
<span class="comment-age">(30 May '18, 15:27)</span> <span class="comment-user userinfo">Ondrej Spanel</span>
</div>
</div>
<span id="63877"></span>
<div id="comment-63877" class="comment">
<div id="post-63877-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note: it seems it is only historical data is affected by this (files like europe-180401.osm.pbf). The file europe-latest.osm.pbf seems fine. I will try historical data from <a href="https://osm-internal.download.geofabrik.de/europe.html#">https://osm-internal.download.geofabrik.de/europe.html#</a> and report the result here.</p>
</div>
<div id="comment-63877-info" class="comment-info">
<span class="comment-age">(30 May '18, 15:35)</span> <span class="comment-user userinfo">Ondrej Spanel</span>
</div>
</div>
<span id="63907"></span>
<div id="comment-63907" class="comment">
<div id="post-63907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I confirm data downloaded from this location contain the version id and work fine for my purpose.</p>
</div>
<div id="comment-63907-info" class="comment-info">
<span class="comment-age">(31 May '18, 09:41)</span> <span class="comment-user userinfo">Ondrej Spanel</span>
</div>
</div>
<span id="64029"></span>
<div id="comment-64029" class="comment">
<div id="post-64029-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://download.geofabrik.de/europe-180401.osm.pbf">http://download.geofabrik.de/europe-180401.osm.pbf</a> (MD5: 7cd103991af26a5299ccf8dd9577171f) definitely contains version numbers, I just checked.</p>
</div>
<div id="comment-64029-info" class="comment-info">
<span class="comment-age">(05 Jun '18, 15:09)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63874-form-container" class="comment-form-container">
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

