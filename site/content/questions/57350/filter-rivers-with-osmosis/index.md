+++
type = "question"
title = "Filter rivers with Osmosis"
description = '''I&#x27;m trying to filter rivers, highways and water from a planet file in Osmosis as follows: osmosis &#92; --read-pbf-fast file=&quot;planet-latest.osm.pbf&quot; workers=8 &#92; --buffer &#92; --tf accept-relations natural=water waterway=riverbank highway=* &#92; --used-way &#92; --used-node &#92; --write-pbf planet-RELATIONS.osm.pbf  ...'''
date = "2017-07-29T21:11:00Z"
lastmod = "2017-07-30T12:24:00Z"
weight = 57350
keywords = [ "filter", "river", "osmosis" ]
aliases = [ "/questions/57350" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter rivers with Osmosis](/questions/57350/filter-rivers-with-osmosis)

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
<span id="post-57350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to filter rivers, highways and water from a planet file in Osmosis as follows:</p>
<pre><code>osmosis \
--read-pbf-fast file=&quot;planet-latest.osm.pbf&quot; workers=8 \
--buffer \
--tf accept-relations natural=water waterway=riverbank highway=*  \
--used-way \
--used-node \
--write-pbf planet-RELATIONS.osm.pbf
&#10;osmosis \
--read-pbf-fast file=&quot;planet-latest.osm.pbf&quot; workers=8 \
--buffer \
--tf accept-ways natural=water waterway=riverbank highway=* \
--tf reject-relations \
--used-node \
--write-pbf planet-WAYS.osm.pbf
&#10;#MERGE RELATIONS AND WAYS
osmosis \
--read-pbf-fast file=&quot;planet-RELATIONS&quot; workers=8 \
--read-pbf-fast file=&quot;planet-WAYS&quot; workers=8 \
--merge \
--write-pbf planet-MERGED-highway-water-riverbank.osm.pbf</code></pre>
<p>After that I turn the .pbf into GeoJSON with Ogr2ogr and then into .mbtiles with Tippecanoe. The highways and water work perfectly, but the rivers are messy: parts of every river works well while some parts have broken polygons, and others parts are shown as multilinestrings even though they should(?) be polygons.</p>
<p>If you have any pointers on how to filter rivers properly I'd greatly appreciate it! (If this is the wrong forum for this question please redirect me!)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '17, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/75c3ab8f3936fc21e0c00cfe9793c8fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Azei&#39;s gravatar image" />
<p><span>Azei</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Azei has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57350" class="comments-container">
&#10;</div>
<div id="comment-tools-57350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57350-form-container" class="comment-form-container">
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

<span id="57351"></span>

<div id="answer-container-57351" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57351-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-57351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Azei has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure what osmosis and ogr2ogr are doing exactly, try with <a href="http://osmcode.org/osmium-tool/">osmium</a>:</p>
<pre><code>osmium tags-filter planet-latest.osm.pbf natural=water waterway=riverbank highway \
    -o planet-highway-water-riverbank.osm.pbf</code></pre>
<p>Much easier command line and much faster than osmosis.</p>
<p>There is also an <code>osmium export</code> command that can convert this into GeoJSON, but it is not in the released version yet and only available in the <code>export</code> branch on <a href="https://github.com/osmcode/osmium-tool/tree/export">github</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '17, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-57351" class="comments-container">
<span id="57352"></span>
<div id="comment-57352" class="comment">
<div id="post-57352-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It turns out ogr2ogr was the problem, converting waterway=river to lines when doing the .pbf to .geojson conversion when really they should be converted to polygons. With osmium export I got that working, thanks alot!</p>
<p>Also for the record, osmium tags-filter turns out to be orders of magnitude faster and simpler than osmosis for anyone interested.</p>
</div>
<div id="comment-57352-info" class="comment-info">
<span class="comment-age">(30 Jul '17, 12:24)</span> <span class="comment-user userinfo">Azei</span>
</div>
</div>
</div>
<div id="comment-tools-57351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57351-form-container" class="comment-form-container">
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

