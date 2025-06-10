+++
type = "question"
title = "Filter ways/features by many Changesets to view in QGIS."
description = '''I&#x27;m familiar with OSMCha (great tool) to see features per changeset but I&#x27;m stumped with how to view/analyze this data in QGIS.  I have dozens of changesets which I&#x27;ve brought into QGIS (downloaded bounding coords from planet.osm-Athena) and now I want to see only the ways which have been modified/c...'''
date = "2018-05-01T02:10:00Z"
lastmod = "2018-05-02T14:56:00Z"
weight = 63246
keywords = [ "qgis", "changeset", "features" ]
aliases = [ "/questions/63246" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter ways/features by many Changesets to view in QGIS.](/questions/63246/filter-waysfeatures-by-many-changesets-to-view-in-qgis)

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
<span id="post-63246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63246-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm familiar with OSMCha (great tool) to see features per changeset but I'm stumped with how to view/analyze this data in QGIS.</p>
<p>I have dozens of changesets which I've brought into QGIS (downloaded bounding coords from planet.osm-Athena) and now I want to see only the ways which have been modified/created for matching changeset. Keep in mind that I can't use overpass API because I'm covering a lot of area and data (again, dozens of changesets).</p>
<p>I have downloaded data via geofabrik and uploaded to Postgres to bring OSM data into QGIS but no way to identify which ways are tied to which changeset. Is this even possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '18, 02:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f2fb91bd7678c527e5b14594835a42a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="map_cascadia&#39;s gravatar image" />
<p><span>map_cascadia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="map_cascadia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63246" class="comments-container">
&#10;</div>
<div id="comment-tools-63246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63246-form-container" class="comment-form-container">
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

<span id="63248"></span>

<div id="answer-container-63248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63248-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have full OSM data (that is data including the metda-data) each OSM element (nodes, ways, and relations) have the changeset id of the changeset in which the element version was created as an attribute. Random example in XML format</p>
<pre><code>&lt;node id=&quot;471552&quot; lat=&quot;47.8467688&quot; lon=&quot;16.1908387&quot; version=&quot;3&quot; timestamp=&quot;2011-01-10T14:21:55Z&quot; changeset=&quot;6926751&quot; uid=&quot;289334&quot; user=&quot;Soldier Boy&quot;&gt;
  &lt;tag k=&quot;source&quot; v=&quot;survey&quot;/&gt;
&lt;/node&gt;</code></pre>
<p>You need to make sure that</p>
<p>a) your dataset actually has the changeset id attribute (standard geofabrik downloads currently have them)</p>
<p>b) your import to postgres actually imported them (which tool did you use for importing?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '18, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-63248" class="comments-container">
<span id="63263"></span>
<div id="comment-63263" class="comment">
<div id="post-63263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have downloaded from geofabrik and imported into postgres with osmosis and osm2pgsql. I've seen the command [--extra attributes] to bring in the changeset username and id but still no luck and seeing this in my tables. Is the metadata buried in hstore column? Maybe if I figure out github I can install ChangesetMD or Osmium (<a href="http://docs.osmcode.org/osmium/latest/osmium-changeset-filter.html)?">http://docs.osmcode.org/osmium/latest/osmium-changeset-filter.html)?</a></p>
<p>Either way, it would be really cool if I can just query out ways by username or a series of changeset IDs, is this possible?</p>
</div>
<div id="comment-63263-info" class="comment-info">
<span class="comment-age">(02 May '18, 01:19)</span> <span class="comment-user userinfo">map_cascadia</span>
</div>
</div>
<span id="63278"></span>
<div id="comment-63278" class="comment">
<div id="post-63278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The osm2pgsql import should have a key - value pair in the tags hstore column with the key "osm_changeset" if every thing worked (it probably makes sense to create an index on the value if you are going to do lots of queries).</p>
<p>The other thing of note is that the normal data dumps will not contain this information going forward, it will however still be available but you need to realize that you may be acting as a data controller according to the GDPR.</p>
</div>
<div id="comment-63278-info" class="comment-info">
<span class="comment-age">(02 May '18, 14:56)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63248-form-container" class="comment-form-container">
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

