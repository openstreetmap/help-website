+++
type = "question"
title = "How long does it take to extract a city from the OSM globe?"
description = '''I just downloaded the OSM globe, and am testing out running an extract using the demonstration code and osmosis:  bzcat downloaded.osm.bz2 | osmosis&#92;  --read-xml enableDateParsing=no file=-&#92;  --bounding-box top=49.5138 left=10.9351 bottom=49.3866 right=11.201 --write-xml file=-&#92;  | bzip2 &amp;gt; extrac...'''
date = "2011-05-04T18:28:00Z"
lastmod = "2011-05-06T10:01:00Z"
weight = 4994
keywords = [ "extract", "osmosis" ]
aliases = [ "/questions/4994" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How long does it take to extract a city from the OSM globe?](/questions/4994/how-long-does-it-take-to-extract-a-city-from-the-osm-globe)

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
<span id="post-4994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4994-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just downloaded the OSM globe, and am testing out running an extract using the demonstration <a href="http://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes">code</a> and osmosis:</p>
<pre><code> bzcat downloaded.osm.bz2 | osmosis\
  --read-xml enableDateParsing=no file=-\
  --bounding-box top=49.5138 left=10.9351 bottom=49.3866 right=11.201 --write-xml file=-\
  | bzip2 &gt; extracted.osm.bz2</code></pre>
<p>Roughly, how long does it take to get this extract? I'm using a computer with four 2.6 GHz cores, and 4 GB of ram and using Ubuntu 10.10. I'm curious whether this should take 4 hours or 4 days...</p>
<p>This the output from my terminal:</p>
<pre><code>user@computer:~/Downloads$  bzcat downloaded.osm.bz2 | osmosis\
&gt;   --read-xml enableDateParsing=no file=-\
&gt;   --bounding-box top=49.5138 left=10.9351 bottom=49.3866 right=11.201 --write-xml file=-\
&gt;   | bzip2 &gt; extracted.osm.bz2
May 4, 2011 11:36:20 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.34
log4j:WARN No appenders could be found for logger (org.java.plugin.ObjectFactory).
log4j:WARN Please initialize the log4j system properly.
May 4, 2011 11:36:21 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
May 4, 2011 11:36:21 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
May 4, 2011 11:36:21 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.</code></pre>
<p>It is now 13.37, and nothing else has appeared in the terminal. I'm not in a rush - I just want to check that this is a reasonable amount of time to wait, or whether there is something I have done incorrectly. I'm completely new to running queries on data-sets of this size, and osmosis in general. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '11, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/eb61b8ace91c7e390160ce80bb8ee13b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="celenius&#39;s gravatar image" />
<p><span>celenius</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="celenius has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '11, 18:38</strong> </span></p>
</div>
</div>
<div id="comments-container-4994" class="comments-container">
&#10;</div>
<div id="comment-tools-4994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4994-form-container" class="comment-form-container">
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

<span id="4995"></span>

<div id="answer-container-4995" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4995-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-4995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't tell you for sure, but I would expect it to take hours rather than days.</p>
<p>However, there are two potential ways of speeding things up.</p>
<p>1) Use the binary format <a href="http://planet.openstreetmap.org/pbf-experimental/">.osm.pbf</a> instead of the xml encoded version of the planet file. It is much more efficient to parse.</p>
<p>2) If you only need a city, you probably don't want to start off with the whole planet. There are <a href="http://wiki.openstreetmap.org/wiki/Planet#Downloading">country sized extracts of the planet</a> available that are much more manageable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '11, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-4995" class="comments-container">
<span id="4996"></span>
<div id="comment-4996" class="comment">
<div id="post-4996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@apmon</span> Can I just download the .osm.pbf format, and run the query in the same way if I change the file name? I did look for country level extracts to use after the test city runs, however I want data for singapore, and did not see any regional extracts.</p>
</div>
<div id="comment-4996-info" class="comment-info">
<span class="comment-age">(04 May '11, 18:47)</span> <span class="comment-user userinfo">celenius</span>
</div>
</div>
<span id="4997"></span>
<div id="comment-4997" class="comment">
<div id="post-4997-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://downloads.cloudmade.com/asia/south-eastern_asia/singapore#downloads_breadcrumbs">http://downloads.cloudmade.com/asia/south-eastern_asia/singapore#downloads_breadcrumbs</a></p>
<p><a href="http://download.geofabrik.de/osm/asia.osm.pbf">http://download.geofabrik.de/osm/asia.osm.pbf</a></p>
<p>Otherwise, yes you should be able to run the command the same way. Although you will presumably have to replace the --read-xml with something like --read-pbf</p>
</div>
<div id="comment-4997-info" class="comment-info">
<span class="comment-age">(05 May '11, 01:00)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="5002"></span>
<div id="comment-5002" class="comment">
<div id="post-5002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the links - I previously looked at cloudmade and geofabrik and they are missing a lot of information. I'll try the <code>--read-pbf</code></p>
</div>
<div id="comment-5002-info" class="comment-info">
<span class="comment-age">(05 May '11, 15:45)</span> <span class="comment-user userinfo">celenius</span>
</div>
</div>
</div>
<div id="comment-tools-4995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4995-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5011"></span>

<div id="answer-container-5011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also use bboxSplit, which is much faster than osmosis.</p>
<pre><code>wget http://svn.openstreetmap.org/applications/rendering/gosmore/bboxSplit.cpp
g++ -O2 bboxSplit.cpp -o bboxSplit</code></pre>
<p>To run it:</p>
<pre><code>bzcat planet-latest.osm.bz2 |  ./bboxSplit \
  -85.05113   73.12500    9.44906  180.00000 gzip someRegion.osm.gz \
  ...</code></pre>
<p>The 4 values are minlat, minlon maxlat and maxlon. If a node is in the bbox it is included in someRegion. If a way refers to 1 or more nodes in the bbox it is included in someRegion. If a relation refers to 1 or more node or way that has already been included in someRegion then that relation is also include in someRegion. I think osmosis follows the same rules.</p>
<p>If you don't want to compress the output, change gzip to cat.</p>
<p>You can have as many regions as you like. (I've tested up to 200)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '11, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-5011" class="comments-container">
&#10;</div>
<div id="comment-tools-5011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5011-form-container" class="comment-form-container">
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

