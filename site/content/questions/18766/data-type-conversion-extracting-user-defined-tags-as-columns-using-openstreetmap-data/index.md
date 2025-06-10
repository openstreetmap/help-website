+++
type = "question"
title = "data type conversion extracting user defined tags as columns using Openstreetmap data"
description = '''we have an ,osm data in which we have used some tags that we defined ourselves like, age, roof_type, roof_slope . we want to convert this file to shapefile, in which the roof_type tag appears as a column name and its values as attributes. we have tried: QGIS: install plugin, only creates column of 7...'''
date = "2012-12-30T06:56:00Z"
lastmod = "2013-01-04T11:09:00Z"
weight = 18766
keywords = [ "export" ]
aliases = [ "/questions/18766" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [data type conversion extracting user defined tags as columns using Openstreetmap data](/questions/18766/data-type-conversion-extracting-user-defined-tags-as-columns-using-openstreetmap-data)

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
<span id="post-18766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18766-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>we have an ,osm data in which we have used some tags that we defined ourselves like, age, roof_type, roof_slope . we want to convert this file to shapefile, in which the roof_type tag appears as a column name and its values as attributes.</p>
<p>we have tried:</p>
<p>QGIS: install plugin, only creates column of 7 tags, others are grouped into one column called tags</p>
<p>OSM2GIS: online tools, selects area on map, has many tags, but not user defined ones</p>
<p>Geoconverter: online tools, input a supported file and it will export a supported file, but not user defined ones</p>
<p>OSMembrane: frontend for Osmosis, still learning (connection problem to postgis)</p>
<p>osm2shp.c: still learning (having problem in running the program)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '12, 06:56</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-18766" class="comments-container">
&#10;</div>
<div id="comment-tools-18766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18766-form-container" class="comment-form-container">
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

<span id="18789"></span>

<div id="answer-container-18789" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18789-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the command line programm <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">Osmconvert</a> ... it has a feature to output OSM elements in CSV files.</p>
<p>You can define manually what columns are to be generated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '12, 07:43</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-18789" class="comments-container">
<span id="18837"></span>
<div id="comment-18837" class="comment">
<div id="post-18837-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, it solved the case.</p>
</div>
<div id="comment-18837-info" class="comment-info">
<span class="comment-age">(04 Jan '13, 09:26)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="18839"></span>
<div id="comment-18839" class="comment">
<div id="post-18839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could You also have a look at <a href="https://help.openstreetmap.org/questions/18838/joining-osm-csv-file-to-same-file-in-qgis">this</a></p>
</div>
<div id="comment-18839-info" class="comment-info">
<span class="comment-age">(04 Jan '13, 11:09)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
</div>
<div id="comment-tools-18789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18789-form-container" class="comment-form-container">
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

