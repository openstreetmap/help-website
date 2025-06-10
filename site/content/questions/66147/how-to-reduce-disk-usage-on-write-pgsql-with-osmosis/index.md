+++
type = "question"
title = "how to reduce disk usage on write-pgsql with osmosis?"
description = '''I am using osmosis version 0.44.1 (after simple apt install at UBUNTU 16 LTS) and fresh PostGIS, there are only few relations (and few Gb on PostGIS geometry) but this command use all my ~60Gb of free disk: osmosis --read-pbf file=brazil-latest.osm.pbf --tag-filter &#92;  accept-relations admin_level=4,...'''
date = "2018-10-03T14:41:00Z"
lastmod = "2018-10-03T14:41:00Z"
weight = 66147
keywords = [ "disk_usage", "osmosis" ]
aliases = [ "/questions/66147" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to reduce disk usage on write-pgsql with osmosis?](/questions/66147/how-to-reduce-disk-usage-on-write-pgsql-with-osmosis)

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
<span id="post-66147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66147-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using osmosis version 0.44.1 (after simple <code>apt install</code> at UBUNTU 16 LTS) and fresh PostGIS, there are only few relations (and few Gb on PostGIS geometry) but this command use all my ~60Gb of free disk:</p>
<pre><code>osmosis --read-pbf file=brazil-latest.osm.pbf --tag-filter \
   accept-relations admin_level=4,boundary=administrative  \
   --write-pgsql host=localhost database=pgsnapshot \
   user=postgres password=&quot;myPass&quot;  &amp;</code></pre>
<p>How to reduce the disk consume?</p>
<hr />
<p>Example of relation that need: <a href="https://www.openstreetmap.org/relation/298204#map=6/-22.675/-48.625&amp;layers=T">here</a>.</p>
<hr />
<p>Dump of error messages:</p>
<pre><code>org.springframework.beans.factory.xml.XmlBeanDefinitionReader loadBeanDefinitions
...
SEVERE: Thread for task 1-read-pbf failed
org.springframework.dao.DataAccessResourceFailureException: StatementCallback; SQL [CREATE INDEX idx_way_nodes_node_id ON way_nodes USING btree (node_id)]; ERROR: could not extend file &quot;base/340840/351416.1&quot;: wrote only 4096 of 8192 bytes at block 167425
&#10;  Hint: Check free disk space.; nested exception is org.postgresql.util.PSQLException: ERROR: could not extend file &quot;base/340840/351416.1&quot;: wrote only 4096 of 8192 bytes at block 167425
  Hint: Check free disk space.</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '18, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '18, 16:04</strong> </span></p>
</div>
</div>
<div id="comments-container-66147" class="comments-container">
&#10;</div>
<div id="comment-tools-66147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66147-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

