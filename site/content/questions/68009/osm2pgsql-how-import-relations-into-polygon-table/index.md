+++
type = "question"
title = "osm2pgsql how import relations into polygon table"
description = '''I&#x27;m trying to import a relation of type multipolygon into a PostGreSQL DB using osm2pgsql. I use the result of this query as OSM file: http://overpass-turbo.eu/s/G7r which contains one way https://www.openstreetmap.org/way/25210902 and one relation https://www.openstreetmap.org/way/25210902 with the...'''
date = "2019-02-14T15:46:00Z"
lastmod = "2019-02-16T06:48:00Z"
weight = 68009
keywords = [ "overpass-turbo", "osm2pgsql", "relations", "multipolygon" ]
aliases = [ "/questions/68009" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql how import relations into polygon table](/questions/68009/osm2pgsql-how-import-relations-into-polygon-table)

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
<span id="post-68009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to import a relation of type multipolygon into a PostGreSQL DB using osm2pgsql.</p>
<p>I use the result of this query as OSM file: <a href="http://overpass-turbo.eu/s/G7r">http://overpass-turbo.eu/s/G7r</a> which contains one way <a href="https://www.openstreetmap.org/way/25210902">https://www.openstreetmap.org/way/25210902</a> and one relation <a href="https://www.openstreetmap.org/relation/1697460">https://www.openstreetmap.org/way/25210902</a> with the default.style and this command: <code>osm2pgsql --slim --username xy --database gis --style default.style export.osm</code></p>
<p>While the way item is going nicely into the table planet_osm_polygon, the relation doesn't import into planet_osm_polygon (or any other table), but is present in planet_osm_rels.</p>
<p>Also, there seems to be no error in the shape of the relation which would prevent the import, as checked on <a href="http://tools.geofabrik.de/osmi/?view=areas&amp;lon=9.59871&amp;lat=47.23608&amp;zoom=16">http://tools.geofabrik.de/osmi/?view=areas&amp;lon=9.59871&amp;lat=47.23608&amp;zoom=16</a></p>
<p><em>My question:</em> Is it by design that multipolygons do not end up in planet_osm_polygon or do I have to change the default.style or is there a problem with relation 1697460 (Although I also tested other multipolygon relations with the same (negative) result.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '19, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/294306ca43317574c542930a91e30ab6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r1tter&#39;s gravatar image" />
<p><span>r1tter</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r1tter has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '19, 08:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-68009" class="comments-container">
&#10;</div>
<div id="comment-tools-68009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68009-form-container" class="comment-form-container">
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

<span id="68017"></span>

<div id="answer-container-68017" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68017-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, the problem was the order of the data in the OSM XML file provided by overpass-turbo.eu (I selected "Export/Data/Download as raw OSM Data): When the relations appear BEFORE the nodes and ways, the relations won't be imported into planet_osm_polygon by osm2pgsql. Putting the relations AFTER the nodes and ways solved therefor the problem.</p>
<p>(Importing the OSM XML from overpass-turbo to <a href="http://level0.osmz.ru/">level0.osmz.ru</a> and then exporting the data as OSM corrected the order, btw)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '19, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/294306ca43317574c542930a91e30ab6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r1tter&#39;s gravatar image" />
<p><span>r1tter</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r1tter has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-68017" class="comments-container">
<span id="68023"></span>
<div id="comment-68023" class="comment">
<div id="post-68023-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for the self-answer! Is there anything left unclear or can we close this question?</p>
</div>
<div id="comment-68023-info" class="comment-info">
<span class="comment-age">(15 Feb '19, 20:59)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="68027"></span>
<div id="comment-68027" class="comment">
<div id="post-68027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can close it. Thanks!</p>
</div>
<div id="comment-68027-info" class="comment-info">
<span class="comment-age">(16 Feb '19, 06:48)</span> <span class="comment-user userinfo">r1tter</span>
</div>
</div>
</div>
<div id="comment-tools-68017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68017-form-container" class="comment-form-container">
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

