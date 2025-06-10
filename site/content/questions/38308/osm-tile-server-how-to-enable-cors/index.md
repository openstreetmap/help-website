+++
type = "question"
title = "OSM Tile Server: how to enable CORS?"
description = '''I&#x27;ve set up an OSM Tile Server, as described here. The server is up and running, and I&#x27;m able to open the default map page in the browser (http://tile-server-ip/osm/slippymap.html) and see the map. However, when I try to pull map data from Tile Server on a page from another site using OpenLayers lib...'''
date = "2014-11-04T12:53:00Z"
lastmod = "2015-09-12T16:36:00Z"
weight = 38308
keywords = [ "tileserver", "openlayers", "cors" ]
aliases = [ "/questions/38308" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Tile Server: how to enable CORS?](/questions/38308/osm-tile-server-how-to-enable-cors)

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
<span id="post-38308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38308-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've set up an OSM Tile Server, as described <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">here</a>.</p>
<p>The server is up and running, and I'm able to open the default map page in the browser (<a href="http://tile-server-ip/osm/slippymap.html"><code>http://tile-server-ip/osm/slippymap.html</code></a>) and see the map.</p>
<p>However, when I try to pull map data from Tile Server on a page from another site using OpenLayers library, I get:</p>
<pre><code>Image from origin &#39;http://tile-server-ip&#39; has been blocked from loading by Cross-Origin Resource Sharing policy: No &#39;Access-Control-Allow-Origin&#39; header is present on the requested resource. Origin &#39;http://my-other-site&#39; is therefore not allowed access.</code></pre>
<p>So, I need to enable CORS on Tile Server.</p>
<p>I tried adding CORS to Apache configuration (<code>/etc/apache2/sites-enabled/tileserver_site.conf</code>):</p>
<pre><code>Header set Access-Control-Allow-Origin &quot;*&quot;</code></pre>
<p>, but that has no effect. I tried modifying <code>/etc/renderd.conf</code> and adding:</p>
<pre><code>CORS=*</code></pre>
<p>to <code>[default]</code> section, but that, again, has no effect.</p>
<p>So, the question is: how to enable CORS on Tile Server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-cors" rel="tag" title="see questions tagged &#39;cors&#39;">cors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '14, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/806b9e518fe7c9dce5472637fa4a20f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weekens&#39;s gravatar image" />
<p><span>weekens</span><br />
<span class="score" title="101 reputation points">101</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weekens has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '14, 13:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38308" class="comments-container">
&#10;</div>
<div id="comment-tools-38308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38308-form-container" class="comment-form-container">
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

<span id="38309"></span>

<div id="answer-container-38309" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38309-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem was actually solved by providing <code>crossOrigin: null</code> to OpenLayers OSM source:</p>
<pre><code>layers: [
  new ol.layer.Tile({
    source: new ol.source.OSM({
      url: &#39;http://tile-server-ip/osm/{z}/{x}/{y}.png&#39;,
      crossOrigin: null
    })
  })
],</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '14, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/806b9e518fe7c9dce5472637fa4a20f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weekens&#39;s gravatar image" />
<p><span>weekens</span><br />
<span class="score" title="101 reputation points">101</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weekens has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38309" class="comments-container">
&#10;</div>
<div id="comment-tools-38309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38309-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45209"></span>

<div id="answer-container-45209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45209-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have the same problem. Solved in this way: Add Header set Access-Control-Allow-Origin "*" In /etc/apache2/conf-available/security.conf</p>
<p>and change the server name in tileservice_site.con ServerName map.MYSERVER.it ServerAlias a.map.MYSERVER.it b.map.MYSERVER.it c.map.MYSERVER.it</p>
<p>Hope this help...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '15, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ac5e40f6af3e5b68d069a65b60c07fd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maurisor&#39;s gravatar image" />
<p><span>maurisor</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maurisor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45209" class="comments-container">
&#10;</div>
<div id="comment-tools-45209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45209-form-container" class="comment-form-container">
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

