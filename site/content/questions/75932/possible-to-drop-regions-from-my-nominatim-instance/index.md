+++
type = "question"
title = "Possible to drop regions from my Nominatim instance?"
description = '''I&#x27;m installing my own Nominatim instance and decided I don&#x27;t need as many regions as I imported. The docs don&#x27;t say how to drop/remove regions, so is there a way or do I have to start from scratch?'''
date = "2020-07-28T19:45:00Z"
lastmod = "2020-07-30T11:03:00Z"
weight = 75932
keywords = [ "size", "nominatim", "data", "remove", "database" ]
aliases = [ "/questions/75932" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Possible to drop regions from my Nominatim instance?](/questions/75932/possible-to-drop-regions-from-my-nominatim-instance)

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
<span id="post-75932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75932-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm installing my own Nominatim instance and decided I don't need as many regions as I imported. The docs don't say how to drop/remove regions, so is there a way or do I have to start from scratch?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '20, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/9d09f8dc09cc4e4e2b72019fb0c1fefc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RenegadeTech&#39;s gravatar image" />
<p><span>RenegadeTech</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RenegadeTech has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75932" class="comments-container">
&#10;</div>
<div id="comment-tools-75932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75932-form-container" class="comment-form-container">
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

<span id="75954"></span>

<div id="answer-container-75954" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75954-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RenegadeTech has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no such feature. If the issue is disk space you could delete tables needed for updates (<a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#dropping-data-required-for-dynamic-updates)">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#dropping-data-required-for-dynamic-updates)</a> but of course then you cannot update the data regularly any more.</p>
<p>In <a href="https://github.com/osm-search/Nominatim/blob/master/lib/setup/SetupClass.php#L647">https://github.com/osm-search/Nominatim/blob/master/lib/setup/SetupClass.php#L647</a> you can see which tables and indices would NOT be deleted, the planet_* tables will safe the most space.</p>
<p>Updates (<a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates)">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates)</a> work by downloading OSM change files (<a href="https://wiki.openstreetmap.org/wiki/OsmChange)">https://wiki.openstreetmap.org/wiki/OsmChange)</a> and loading then into the database. Those can include additions, changes to objects, deletions. You could create a change file by comparing the data you have currently in the database against what you want in the database, a lot of deletions basically.</p>
<p>Say you imported countryA and countryB, and now you only want countryB in the dababase:</p>
<p>With Osmosis:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis">https://wiki.openstreetmap.org/wiki/Osmosis</a></p>
<p><code>osmosis --read-xml file="countryAandB.osm" --read-xml file="countryB.osm" --derive-change --write-xml-change file="mychanges.osc"</code></p>
<p>Note, you need to convert between <em>.pbf (binary) and</em> .osm (XML) file formats before.</p>
<p>With Osmium:</p>
<p><a href="https://osmcode.org/osmium-tool/manual.html#working-with-change-files">https://osmcode.org/osmium-tool/manual.html#working-with-change-files</a></p>
<p><code>osmium derive-changes countryAandB.osm.pbf countryB.osm.pbf -o mychanges.osc</code></p>
<p>Then you import the change file:</p>
<p><code>osm2pgsql/osm2pgsql --hstore --latlong --append --slim --number-processes 1 --output gazetteer --style settings/import-full.style --database nominatim mychanges.osc</code></p>
<p>That's based on <a href="https://github.com/osm-search/Nominatim/blob/master/utils/update.php">https://github.com/osm-search/Nominatim/blob/master/utils/update.php</a> code (many variables say osmosis but these days it runs pyosmium really).</p>
<p>That's untested, I'm not aware anybody has done it and I would double-check on the <a href="https://lists.openstreetmap.org/listinfo/geocoding">https://lists.openstreetmap.org/listinfo/geocoding</a> mailing list and create a database backup first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '20, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-75954" class="comments-container">
&#10;</div>
<div id="comment-tools-75954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75954-form-container" class="comment-form-container">
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

