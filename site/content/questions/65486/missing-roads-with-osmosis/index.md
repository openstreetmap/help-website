+++
type = "question"
title = "Missing roads with osmosis"
description = '''I am currently trying to extract road networks from OpenStreetMap dumps downloaded on Geofabrik. I am using the following osmosis (version 0.45) command to extract roads: osmosis &#92; --rbf input.osm.pbf &#92; --tf reject-relations &#92; --tf accept-ways highway=motorway,motorway_link,trunk,trunk_link,primary,...'''
date = "2018-08-21T13:23:00Z"
lastmod = "2019-11-19T15:18:00Z"
weight = 65486
keywords = [ "road", "osmosis" ]
aliases = [ "/questions/65486" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing roads with osmosis](/questions/65486/missing-roads-with-osmosis)

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
<span id="post-65486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently trying to extract road networks from OpenStreetMap dumps downloaded on <a href="http://download.geofabrik.de/">Geofabrik</a>. I am using the following osmosis (version 0.45) command to extract roads:</p>
<pre><code>osmosis \
--rbf input.osm.pbf \
--tf reject-relations \
--tf accept-ways highway=motorway,motorway_link,trunk,trunk_link,primary,primary_link,secondary,secondary_link,tertiary,tertiary_link,unclassified,residential \
--tf reject-ways highway=construction \
--lp --wb output_roads.osm.pbf</code></pre>
<p>This should return a file containing all car roads except service roads.</p>
<p>However, some (and sometimes a lot of) roads are missing. I have tried this command on 3 input files:</p>
<ul>
<li>"Midi-Pyrénées" French region: the road network seems almost complete. The attribute table contains 72010 elements.</li>
<li>all of France: a lot of roads are missing. The attribute table contains only 65803 elements (less than a single region). All types of highways are impacted: primary to residential. There is no any obvious pattern for the missing roads.</li>
<li>all of Europe: almost all roads are missing. The attribute table contains 62092 elements (less than all of France...).</li>
</ul>
<p>I guess there is some limitation I am not aware of, either on the osmosis command or on the output file. What am I doing wrong here?</p>
<p>This may be unrelated but I have tried using the <code>--used-node</code> option in order to reduce the size of the output files, but this always generates an error (<code>org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to create object stream writing to temporary file null.</code>). I have no idea why.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '18, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/56d3ea5daee43229ad00fc628fe1b624?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArMoraer&#39;s gravatar image" />
<p><span>ArMoraer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArMoraer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65486" class="comments-container">
&#10;</div>
<div id="comment-tools-65486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65486-form-container" class="comment-form-container">
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

<span id="71731"></span>

<div id="answer-container-71731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71731-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, Im back to this post because I have exactly the same issue with osmosis...</p>
<p>I looked at this post : <a href="https://gis.stackexchange.com/questions/293348/missing-roads-from-openstreetmap-data-with-osmosis">https://gis.stackexchange.com/questions/293348/missing-roads-from-openstreetmap-data-with-osmosis</a></p>
<p>So its seems that there is a limitation to 65356 elements.</p>
<p>Did you manage to download all the roads you wanted ? and if so, how ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '19, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/9c06fcfeddbfcb3c387af39e460cf56e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ludixx&#39;s gravatar image" />
<p><span>Ludixx</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ludixx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71731" class="comments-container">
&#10;</div>
<div id="comment-tools-71731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71731-form-container" class="comment-form-container">
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

