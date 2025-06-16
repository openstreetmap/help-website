+++
type = "question"
title = "Filters in osmfilter; a lot of unwanted data"
description = '''I want to filter the national borders of the countries in Europe, thus admin_level=2. I composed the following query for OSMfilter (the chevrons allow to feed multiple lines into the Windows Command Prompt) osmfilter ^  --verbose ^  &quot;D:/GIS Data/Data/europe-latest.o5m&quot; ^  --keep-relations=&quot;boundary=...'''
date = "2016-02-05T03:38:00Z"
lastmod = "2016-02-06T01:11:00Z"
weight = 47932
keywords = [ "osmfilter", "osm2pgsql", "ogr2ogr" ]
aliases = [ "/questions/47932" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filters in osmfilter; a lot of unwanted data](/questions/47932/filters-in-osmfilter-a-lot-of-unwanted-data)

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
<span id="post-47932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to filter the national borders of the countries in Europe, thus admin_level=2. I composed the following query for OSMfilter (the chevrons allow to feed multiple lines into the Windows Command Prompt)</p>
<pre><code>osmfilter ^
  --verbose ^
  &quot;D:/GIS Data/Data/europe-latest.o5m&quot; ^
  --keep-relations=&quot;boundary=administrative AND admin_level=2&quot; ^
  --keep-nodes= ^
  --keep-ways= ^
  -o=&quot;D:/GIS Data/Tijdelijk/countrieseurope.osm&quot;</code></pre>
<p>When I convert/import this file (~ 970 MB) using either osm2pgsql or ogr2ogr, the countries are rendered correctly. But there are also al lot of boundaries from provinces and municipalities (admin_level &gt; 2) rendered. The happens for instance in Spain, Portugal and Belgium; thousands of local boundaries are rendered. On the other hand for instance in The Netherlands, Slovenia and Norway only the national borders are rendered (which is correct).</p>
<p>It seems to me both osm2pgsql and ogr2ogr are rendering the OSM file correctly (checked the OSM file manually). So the data of the unwanted local boundaries have to be in the OSM file extracted with OSMfilter. Then I executed the following query:</p>
<pre><code>osmfilter ^
  --verbose ^
  &quot;D:/GIS Data/Data/europe-latest.o5m&quot; ^
  --keep-relations=&quot;boundary=administrative AND admin_level=2&quot; ^
  --ignore-dependencies ^
  -o=&quot;D:/GIS Data/Tijdelijk/countrieseuroperelation.osm&quot;</code></pre>
<p>This yields an OSM file with relations of the national borders of about 60 countries, which is correct. So it seems to me the unwanted data is filtered when OSMfilter is resolving the child relations, ways and nodes of these 60 relations. Why is this unwanted data included by OSM filter? Should I change my query? Or is perhaps the data insufficiently tagged in some countries (as the problem only occurs in about half of the countries).</p>
<p>BTW: This question is related to my question about <a href="/questions/47931/filters-in-osmosis-filtering-administrative-boundaries">Osmosis</a>. I tried to do the same query in Osmosis to see if the dependencies on the 60 relations are resolved in another fashion by Osmosis.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-ogr2ogr" rel="tag" title="see questions tagged &#39;ogr2ogr&#39;">ogr2ogr</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '16, 03:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '16, 03:40</strong> </span></p>
</div>
</div>
<div id="comments-container-47932" class="comments-container">
<span id="47936"></span>
<div id="comment-47936" class="comment">
<div id="post-47936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You know you can download the boundaries from <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> ?</p>
</div>
<div id="comment-47936-info" class="comment-info">
<span class="comment-age">(05 Feb '16, 07:43)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="47947"></span>
<div id="comment-47947" class="comment">
<div id="post-47947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I already filtered the correct data with QGIS. ;) However, I want to know why osmfilter returns so much data not related to the admin_level=2 boundaries. This way I hope to learn more about OSMfilter.</p>
</div>
<div id="comment-47947-info" class="comment-info">
<span class="comment-age">(05 Feb '16, 11:41)</span> <span class="comment-user userinfo">Steijn</span>
</div>
</div>
</div>
<div id="comment-tools-47932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47932-form-container" class="comment-form-container">
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

<span id="47953"></span>

<div id="answer-container-47953" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47953-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think it is probably a result of shared boundary ways that are included in the relations, like</p>
<p><a href="https://www.openstreetmap.org/way/362763546">https://www.openstreetmap.org/way/362763546</a></p>
<p>Which is a member of Spain, Portugal and several lesser boundaries.</p>
<p>Edit: Actually, it sounds like this is the issue:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Talk:Osmfilter#Drop_specific_dependencies">https://wiki.openstreetmap.org/wiki/Talk:Osmfilter#Drop_specific_dependencies</a></p>
<p>There are relations included as members of the Spain relation.</p>
<p>If I understand correctly, osmfilter does not do what I speculated above, it resolves subordinate dependencies only, it doesn't seek out parents of included objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '16, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '16, 15:19</strong> </span></p>
</div>
</div>
<div id="comments-container-47953" class="comments-container">
<span id="47954"></span>
<div id="comment-47954" class="comment">
<div id="post-47954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds logic to me. So osmfilter also resolves all parent relations that use a certain way as a child, rather than resolving only the child-relations, child-ways and child-nodes of those relations containing an admin_level=2 tag. This cascades in resolving all parent-relations/ways in Spain and Portugal. So as I understand it, a solution would be to prevent osmfilter from resolving parent-relations/ways. Is this possible in osmfilter (or Osmosis?).</p>
</div>
<div id="comment-47954-info" class="comment-info">
<span class="comment-age">(05 Feb '16, 13:26)</span> <span class="comment-user userinfo">Steijn</span>
</div>
</div>
</div>
<div id="comment-tools-47953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47953-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47970"></span>

<div id="answer-container-47970" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47970-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Another update:</strong></p>
<p>I got Osmosis working in the correct fashion (for the solution see: <a href="/questions/47931/filters-in-osmosis-filtering-administrative-boundaries">https://help.openstreetmap.org/questions/47931/filters-in-osmosis-filtering-administrative-boundaries</a> ), so now I can compare the results of Osmosis to the results from OSMfilter.</p>
<p>I downloaded the Geofabrik file of Portugal as Portugal got improperly filtered by OSMfilter (see above). I filtered for boundaries=administrative AND admin_level=2.</p>
<p>OSMfilter:</p>
<pre><code>osmfilter ^
  --verbose ^
  &quot;D:/GIS Data/Tijdelijk/portugal-latest.o5m&quot; ^
  --keep-relations=&quot;boundary=administrative AND admin_level=2&quot; ^
  --keep-ways= ^
  --keep-nodes= ^
  -o=&quot;D:/GIS Data/Tijdelijk/portugaladmin2osmfilter.o5m&quot;</code></pre>
<p>Osmosis (3 separate steps):</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Tijdelijk/portugal-latest.osm.pbf&quot; ^
  --tf accept-relations boundary=administrative ^
  --tf accept-relations admin_level=2 ^
  --write-pbf file=&quot;D:/GIS Data/Tijdelijk/step1.osm.pbf&quot;
&#10;osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Tijdelijk/step1.osm.pbf&quot; ^
  --used-way ^
  --write-pbf file=&quot;D:/GIS Data/Tijdelijk/step2.osm.pbf&quot;
&#10;osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Tijdelijk/step2.osm.pbf&quot; ^
  --used-node ^
  --write-pbf file=&quot;D:/GIS Data/Tijdelijk/step3.osm.pbf&quot;</code></pre>
<p>Using Osmosis the problem is gone<strong>!</strong> Osmosis correctly resolves the necessary child-ways and child-nodes for rendering the relations with boundaries=administrative AND admin_level=2, while OSMfilter also resolves parent-relations of child-ways and parent-ways of child-nodes, leading to much unnecessary data being selected. This becomes evident when comparing the file sizes.</p>
<p>File sizes:</p>
<ul>
<li>Osmosis method (OSM file format): 1536 kB</li>
<li>Osmfilter method (OSM file format): 61568 kB</li>
</ul>
<p>BTW: Any ideas to improve the rather tedious Osmosis method I used? :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '16, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '16, 01:18</strong> </span></p>
</div>
</div>
<div id="comments-container-47970" class="comments-container">
&#10;</div>
<div id="comment-tools-47970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47970-form-container" class="comment-form-container">
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

