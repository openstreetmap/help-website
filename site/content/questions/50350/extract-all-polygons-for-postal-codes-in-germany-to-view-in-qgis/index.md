+++
type = "question"
title = "Extract all polygons for postal codes in Germany to view in QGIS"
description = '''Dear OSM community, I&#x27;d like to extract all polygons for german postcodes from a planet file. I already know about the german postcode consolidation and that all the ~8200 postcodes of Germany are available with postal_code tag. What I achieved so far is to pipe an extract Germany.pbf file through O...'''
date = "2016-06-21T09:42:00Z"
lastmod = "2016-06-24T21:05:00Z"
weight = 50350
keywords = [ "osmium", "extract", "postal_code", "polygon", "osmosis" ]
aliases = [ "/questions/50350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract all polygons for postal codes in Germany to view in QGIS](/questions/50350/extract-all-polygons-for-postal-codes-in-germany-to-view-in-qgis)

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
<span id="post-50350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSM community,</p>
<p>I'd like to extract all polygons for german postcodes from a planet file. I already know about the german postcode consolidation and that all the ~8200 postcodes of Germany are available with postal_code tag. What I achieved so far is to pipe an extract Germany.pbf file through Osmosis to get all 8200 relations with postcodes in a few-MB file. Now these do not contain polygon lat/lon data but ways/nodes references mostly and therefore QGIS is not able to plot them on a map. With JOSM I can load the missing data for single relations. I guess that fetches all data that I stripped from the relations before. However, the software fails to load all polygons at once, probably due to the limited memory of my computer. I'd like to refrain from doing the manual work of clicking on every single of the 8200 relations and storing them by hand.</p>
<p>Is there a way to extract relations of postal codes with lat/lon values from an extract? Could you provide me with links to the right tools, and maybe, a step-by-step walkthrough? How to resolve all the ways/nodes to lat/lon values?</p>
<p>Any help appreciated. Thanks in advance.</p>
<p>Kind regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-postal_code" rel="tag" title="see questions tagged &#39;postal_code&#39;">postal_code</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '16, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/7e87039bd8ec79a6d32fc7a868cb6968?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m4dbunny&#39;s gravatar image" />
<p><span>m4dbunny</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m4dbunny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50350" class="comments-container">
&#10;</div>
<div id="comment-tools-50350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50350-form-container" class="comment-form-container">
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

<span id="50358"></span>

<div id="answer-container-50358" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50358-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please go to <a href="http://overpass-turbo.eu/s/gUj">http://overpass-turbo.eu/s/gUj</a></p>
<p>Choose there "Export" &gt; "raw data from Overpass API"</p>
<p>Wait 10-15 minutes until the result arrives.</p>
<p>It is a 250 MB sized OSM file that contains all the coordinates you need. You should be able to load that file into QGIS.</p>
<p>The reason why you should neither load that into JOSM nor click "Run" in Overpass Turbo is that it will crash both JOSM or the browser due to its size.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '16, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-50358" class="comments-container">
<span id="50416"></span>
<div id="comment-50416" class="comment">
<div id="post-50416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, but that helps only partly. There might be future scenarios where I want to extract even larger data sets. I would appreciate an introduction about how to do this lookup of missing lat/lon values with batch processing on the downloaded extract. Do you have any experience with that?</p>
</div>
<div id="comment-50416-info" class="comment-info">
<span class="comment-age">(23 Jun '16, 16:31)</span> <span class="comment-user userinfo">m4dbunny</span>
</div>
</div>
<span id="50451"></span>
<div id="comment-50451" class="comment">
<div id="post-50451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if you wanto to deal with even bigger datasets, I recommand to download whole raw OSM data for a country or continent via <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">https://wiki.openstreetmap.org/wiki/Planet.osm</a> ... and use <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
</div>
<div id="comment-50451-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 21:05)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-50358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50358-form-container" class="comment-form-container">
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

