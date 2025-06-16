+++
type = "question"
title = "How to generate the names of WAY that a certain Node is part of"
description = '''Hi  I&#x27;m brand new to OpenStreetMap. Please kindly understand if this question has been asked before.  I&#x27;m trying to write a query in Overpass Turbo (open to other data mining tool) so that it generates every name of cross streets that a node is part of.  For example of Node 42449597 the output will ...'''
date = "2021-01-07T04:45:00Z"
lastmod = "2021-01-07T16:57:00Z"
weight = 78256
keywords = [ "ways", "nodes", "overpass-turbo" ]
aliases = [ "/questions/78256" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to generate the names of WAY that a certain Node is part of](/questions/78256/how-to-generate-the-names-of-way-that-a-certain-node-is-part-of)

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
<span id="post-78256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78256-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm brand new to OpenStreetMap. Please kindly understand if this question has been asked before.</p>
<p>I'm trying to write a query in Overpass Turbo (open to other data mining tool) so that it generates every name of cross streets that a node is part of.</p>
<p>For example of Node 42449597 the output will be : Warren Street, Church Street, Church Street, and Warren Street</p>
<p>Eventually this query is intended to go after another one that will see select a few number of interested Nodes.</p>
<p>Hope this is clear. Many thanks, in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '21, 04:45</strong></p>
<img src="https://secure.gravatar.com/avatar/6881a78ed67bd2735e76e22de35aee82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="traffic8&#39;s gravatar image" />
<p><span>traffic8</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="traffic8 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78256" class="comments-container">
&#10;</div>
<div id="comment-tools-78256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78256-form-container" class="comment-form-container">
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

<span id="78265"></span>

<div id="answer-container-78265" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, you don't need to use Overpass for this. Returning all the tags of all the ways that use a given node ID is a single command from the standard OSM api:</p>
<pre><code>&gt;curl https://www.openstreetmap.org/api/0.6/node/42449597/ways
&#10;&lt;osm version=&quot;0.6&quot; generator=&quot;CGImap 0.8.3 (615120 spike-06.openstreetmap.org)&quot; copyright=&quot;OpenStreetMap and contributors&quot; attribution=&quot;https://www.openstreetmap.org/copyright&quot; license=&quot;http://opendatacommons.org/licenses/odbl/1-0/&quot;&gt;
 &lt;way id=&quot;222299254&quot; visible=&quot;true&quot; version=&quot;11&quot; changeset=&quot;96751287&quot; timestamp=&quot;2020-12-31T21:07:57Z&quot; user=&quot;kguenther24&quot; uid=&quot;11697944&quot;&gt;
  &lt;nd ref=&quot;42429562&quot;/&gt;
  &lt;nd ref=&quot;8279851483&quot;/&gt;
  &lt;nd ref=&quot;5135853006&quot;/&gt;
  &lt;nd ref=&quot;8279851437&quot;/&gt;
  &lt;nd ref=&quot;42449597&quot;/&gt;
  &lt;tag k=&quot;construction&quot; v=&quot;minor&quot;/&gt;
  &lt;tag k=&quot;cycleway:right&quot; v=&quot;shared_lane&quot;/&gt;
  &lt;tag k=&quot;hgv&quot; v=&quot;local&quot;/&gt;
  &lt;tag k=&quot;highway&quot; v=&quot;secondary&quot;/&gt;
  &lt;tag k=&quot;maxspeed&quot; v=&quot;25 mph&quot;/&gt;
  &lt;tag k=&quot;name&quot; v=&quot;Church Street&quot;/&gt;
  &lt;tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
  &lt;tag k=&quot;tiger:cfcc&quot; v=&quot;A41&quot;/&gt;
  &lt;tag k=&quot;tiger:county&quot; v=&quot;New York, NY&quot;/&gt;
  &lt;tag k=&quot;tiger:name_base&quot; v=&quot;Church&quot;/&gt;
  &lt;tag k=&quot;tiger:name_type&quot; v=&quot;St&quot;/&gt;
  &lt;tag k=&quot;tiger:reviewed&quot; v=&quot;no&quot;/&gt;
  &lt;tag k=&quot;tiger:zip_left&quot; v=&quot;10013&quot;/&gt;
  &lt;tag k=&quot;tiger:zip_right&quot; v=&quot;10013&quot;/&gt;
 &lt;/way&gt;
 &lt;way id=&quot;413050335&quot; visible=&quot;true&quot; version=&quot;13&quot; changeset=&quot;96751287&quot; timestamp=&quot;2020-12-31T21:07:57Z&quot; user=&quot;kguenther24&quot; uid=&quot;11697944&quot;&gt;
  &lt;nd ref=&quot;4143812552&quot;/&gt;
  &lt;nd ref=&quot;5812723033&quot;/&gt;
  &lt;nd ref=&quot;7536025166&quot;/&gt;
  &lt;nd ref=&quot;7410938048&quot;/&gt;
  &lt;nd ref=&quot;42449600&quot;/&gt;
  &lt;nd ref=&quot;7410938045&quot;/&gt;
  &lt;nd ref=&quot;8279851438&quot;/&gt;
  &lt;nd ref=&quot;42449597&quot;/&gt;
  &lt;tag k=&quot;bicycle&quot; v=&quot;yes&quot;/&gt;
  &lt;tag k=&quot;construction&quot; v=&quot;minor&quot;/&gt;
  &lt;tag k=&quot;cycleway:left&quot; v=&quot;lane&quot;/&gt;
  &lt;tag k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
  &lt;tag k=&quot;maxspeed&quot; v=&quot;25 mph&quot;/&gt;
  &lt;tag k=&quot;name&quot; v=&quot;Warren Street&quot;/&gt;
  &lt;tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
  &lt;tag k=&quot;surface&quot; v=&quot;asphalt&quot;/&gt;
  &lt;tag k=&quot;tiger:cfcc&quot; v=&quot;A41&quot;/&gt;
  &lt;tag k=&quot;tiger:county&quot; v=&quot;New York, NY&quot;/&gt;
  &lt;tag k=&quot;tiger:name_base&quot; v=&quot;Warren&quot;/&gt;
  &lt;tag k=&quot;tiger:name_type&quot; v=&quot;St&quot;/&gt;
  &lt;tag k=&quot;tiger:reviewed&quot; v=&quot;no&quot;/&gt;
 &lt;/way&gt;
 &lt;way id=&quot;483707770&quot; visible=&quot;true&quot; version=&quot;5&quot; changeset=&quot;96751287&quot; timestamp=&quot;2020-12-31T21:07:57Z&quot; user=&quot;kguenther24&quot; uid=&quot;11697944&quot;&gt;
  &lt;nd ref=&quot;42449597&quot;/&gt;
  &lt;nd ref=&quot;8279851436&quot;/&gt;
  &lt;nd ref=&quot;7439027751&quot;/&gt;
  &lt;nd ref=&quot;42431611&quot;/&gt;
  &lt;tag k=&quot;construction&quot; v=&quot;minor&quot;/&gt;
  &lt;tag k=&quot;cycleway:right&quot; v=&quot;lane&quot;/&gt;
  &lt;tag k=&quot;hgv&quot; v=&quot;local&quot;/&gt;
  &lt;tag k=&quot;highway&quot; v=&quot;secondary&quot;/&gt;
  &lt;tag k=&quot;maxspeed&quot; v=&quot;25 mph&quot;/&gt;
  &lt;tag k=&quot;name&quot; v=&quot;Church Street&quot;/&gt;
  &lt;tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
  &lt;tag k=&quot;surface&quot; v=&quot;asphalt&quot;/&gt;
  &lt;tag k=&quot;tiger:cfcc&quot; v=&quot;A41&quot;/&gt;
  &lt;tag k=&quot;tiger:county&quot; v=&quot;New York, NY&quot;/&gt;
  &lt;tag k=&quot;tiger:name_base&quot; v=&quot;Church&quot;/&gt;
  &lt;tag k=&quot;tiger:name_type&quot; v=&quot;St&quot;/&gt;
  &lt;tag k=&quot;tiger:reviewed&quot; v=&quot;no&quot;/&gt;
  &lt;tag k=&quot;tiger:zip_left&quot; v=&quot;10013&quot;/&gt;
  &lt;tag k=&quot;tiger:zip_right&quot; v=&quot;10013&quot;/&gt;
 &lt;/way&gt;
 &lt;way id=&quot;588168462&quot; visible=&quot;true&quot; version=&quot;4&quot; changeset=&quot;96751287&quot; timestamp=&quot;2020-12-31T21:07:57Z&quot; user=&quot;kguenther24&quot; uid=&quot;11697944&quot;&gt;
  &lt;nd ref=&quot;42449597&quot;/&gt;
  &lt;nd ref=&quot;8279851435&quot;/&gt;
  &lt;nd ref=&quot;8262309631&quot;/&gt;
  &lt;nd ref=&quot;2821304136&quot;/&gt;
  &lt;tag k=&quot;bicycle&quot; v=&quot;yes&quot;/&gt;
  &lt;tag k=&quot;construction&quot; v=&quot;minor&quot;/&gt;
  &lt;tag k=&quot;cycleway:left&quot; v=&quot;lane&quot;/&gt;
  &lt;tag k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
  &lt;tag k=&quot;maxspeed&quot; v=&quot;25 mph&quot;/&gt;
  &lt;tag k=&quot;name&quot; v=&quot;Warren Street&quot;/&gt;
  &lt;tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
  &lt;tag k=&quot;surface&quot; v=&quot;asphalt&quot;/&gt;
  &lt;tag k=&quot;tiger:cfcc&quot; v=&quot;A41&quot;/&gt;
  &lt;tag k=&quot;tiger:county&quot; v=&quot;New York, NY&quot;/&gt;
  &lt;tag k=&quot;tiger:name_base&quot; v=&quot;Warren&quot;/&gt;
  &lt;tag k=&quot;tiger:name_type&quot; v=&quot;St&quot;/&gt;
  &lt;tag k=&quot;tiger:reviewed&quot; v=&quot;no&quot;/&gt;
 &lt;/way&gt;
&lt;/osm&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '21, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '21, 16:58</strong> </span></p>
</div>
</div>
<div id="comments-container-78265" class="comments-container">
&#10;</div>
<div id="comment-tools-78265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78265-form-container" class="comment-form-container">
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

