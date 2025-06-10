+++
type = "question"
title = "Getting city border from osm data"
description = '''Hello, I would like to get a list of all german cities with its borders (as polygon) and name.  I started to import the data into the database by using osmosis: ./osmosis --read-pbf file=/mnt/hgfs/VM-SharedFolder/germany.osm.pbf --tf accept-nodes place=village,town,city --tf accept-ways place=villag...'''
date = "2011-09-24T13:05:00Z"
lastmod = "2011-09-28T10:26:00Z"
weight = 8117
keywords = [ "extract", "osm", "polygon", "osmosis" ]
aliases = [ "/questions/8117" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting city border from osm data](/questions/8117/getting-city-border-from-osm-data)

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
<span id="post-8117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8117-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to get a list of all german cities with its borders (as polygon) and name. I started to import the data into the database by using osmosis:</p>
<p>./osmosis --read-pbf file=/mnt/hgfs/VM-SharedFolder/germany.osm.pbf --tf accept-nodes place=village,town,city --tf accept-ways place=village,town,city --write-pgsql host=localhost database=DB_NAME user=USER password=PWD</p>
<p>This filled the database tables (nodes, relations etc.) but I do not know how to extract a polygon by using these data. Any hints?</p>
<p>Thank you, hem</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '11, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/4c477b3a0fd27f410ad23ff6224dac4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hem&#39;s gravatar image" />
<p><span>hem</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8117" class="comments-container">
&#10;</div>
<div id="comment-tools-8117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8117-form-container" class="comment-form-container">
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

<span id="8118"></span>

<div id="answer-container-8118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8118-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I cannot give you a concrete solution, but have a general look also at the blog of Jochen Topf about <a href="http://blog.jochentopf.com/2011-09-01-patchwork-of-administrative-areas.html">boundary relations</a>.</p>
<p>And if you have more detailed questions I would even recommend to ask further at the German subforum at <a href="http://forum.osm.org"></a><a href="http://forum.osm.org">forum.osm.org</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '11, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-8118" class="comments-container">
&#10;</div>
<div id="comment-tools-8118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8118-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8192"></span>

<div id="answer-container-8192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8192-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What do you mean by "extract a polygon"? You can get the name and the polygon of all the municipalities boundaries from the database with such a query:</p>
<blockquote>
<p>select name,way from "public".planet_osm_polygon where admin_level='8'</p>
</blockquote>
<p>You can also download shapefiles from <a href="http://downloads.cloudmade.com/europe/western_europe/germany#downloads_breadcrumbs">cloudmade</a> or <a href="http://download.geofabrik.de/osm/europe/germany/">geofabrik</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '11, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-8192" class="comments-container">
&#10;</div>
<div id="comment-tools-8192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8192-form-container" class="comment-form-container">
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

