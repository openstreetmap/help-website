+++
type = "question"
title = "Postgis DB to osm pbf file"
description = '''Hi I would like to output changes I have made to the data in my PostGIS database to an OSM PBF file so that I can convert it to a graph file (gph) using Osm2PO. I am trying to use Osmosis for this but can&#x27;t seem to get it working. Here are some commands I have tried: osmosis --read-apidb host=&quot;local...'''
date = "2013-02-13T17:35:00Z"
lastmod = "2013-02-13T17:35:00Z"
weight = 19919
keywords = [ "export", "postgresql", "osm", "postgis", "osmosis" ]
aliases = [ "/questions/19919" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Postgis DB to osm pbf file](/questions/19919/postgis-db-to-osm-pbf-file)

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
<span id="post-19919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19919-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I would like to output changes I have made to the data in my PostGIS database to an OSM PBF file so that I can convert it to a graph file (gph) using Osm2PO.</p>
<p>I am trying to use Osmosis for this but can't seem to get it working. Here are some commands I have tried:</p>
<pre><code>osmosis --read-apidb host=&quot;localhost&quot; database=&quot;gis&quot; user=&quot;username&quot; --write-xml file=&quot;filename&quot;</code></pre>
<p>but this fails with various exceptions with an error saying:</p>
<pre><code>ERROR: relation &quot;schema_migrations&quot; does not exist</code></pre>
<p>I also tried using --read-pgsql instead of apidb but it gives an error:</p>
<pre><code>The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks.</code></pre>
<p>Anyone know the best way to do this?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '13, 17:35</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19919" class="comments-container">
&#10;</div>
<div id="comment-tools-19919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19919-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

