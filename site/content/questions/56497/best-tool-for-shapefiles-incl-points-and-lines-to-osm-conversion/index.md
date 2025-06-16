+++
type = "question"
title = "Best tool for shapefiles (incl. points and lines) to osm conversion"
description = '''Hi folks, I have a self-tailored line shapefile from Mapzen and a self-generated point shapefile, which match perfectly after testing in QGIS. Now, I would like to convert both shapefiles into an OSM file, either .pbf or .xml I found the link, but got confused which tool is better for such a convers...'''
date = "2017-06-07T15:55:00Z"
lastmod = "2017-06-08T05:52:00Z"
weight = 56497
keywords = [ "shapefile", "osm" ]
aliases = [ "/questions/56497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best tool for shapefiles (incl. points and lines) to osm conversion](/questions/56497/best-tool-for-shapefiles-incl-points-and-lines-to-osm-conversion)

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
<span id="post-56497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi folks, I have a self-tailored line shapefile from Mapzen and a self-generated point shapefile, which match perfectly after testing in QGIS. Now, I would like to convert both shapefiles into an OSM file, either .pbf or .xml</p>
<p>I found the <a href="https://wiki.openstreetmap.org/wiki/Software_comparison/Import_a_shapefile">link</a>, but got confused which tool is better for such a conversion.</p>
<p>P.S.: I tried on Merkaartor on Windows, and all versions (0.18.2 and 0.18.3) cannot load my files.</p>
<p>Thank you very much for your time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '17, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d929519d4deb8e8e5c66df7517118484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gchen36&#39;s gravatar image" />
<p><span>gchen36</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gchen36 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56497" class="comments-container">
<span id="56498"></span>
<div id="comment-56498" class="comment">
<div id="post-56498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM works!</p>
</div>
<div id="comment-56498-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 17:55)</span> <span class="comment-user userinfo">gchen36</span>
</div>
</div>
</div>
<div id="comment-tools-56497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56497-form-container" class="comment-form-container">
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

<span id="56505"></span>

<div id="answer-container-56505" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56505-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>I can tell you the process for JOSM in Windows. Download and install JOSM. Open it. Go to Edit --&gt; Preference --&gt; Plugins Search for the "OpenData" plugin. Check the box beside it and press ok to download and install it. Drag and drop the shape file into JOSM and press Ctrl + S to save it as an OSM file. This OSM file itself is a XML file. Just change the .osm to .xml and you are good to go.</p>
<p>Check the below links for more:</p>
<p><a href="https://gis.stackexchange.com/questions/177371/how-to-convert-osm-file-into-xml">https://gis.stackexchange.com/questions/177371/how-to-convert-osm-file-into-xml</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/OSM_XML">https://wiki.openstreetmap.org/wiki/OSM_XML</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 05:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-56505" class="comments-container">
&#10;</div>
<div id="comment-tools-56505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56505-form-container" class="comment-form-container">
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

