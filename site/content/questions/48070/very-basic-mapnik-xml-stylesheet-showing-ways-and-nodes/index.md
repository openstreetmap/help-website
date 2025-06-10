+++
type = "question"
title = "Very basic Mapnik XML stylesheet showing ways and nodes"
description = '''I&#x27;m trying to create an extremely basic Mapnik XML stylesheet, so that I can display purely all ways and nodes in an OSM extract, for debugging purposes. It doesn&#x27;t need to look pretty. I am running this against a flat-file .osm file, using the Geofabrik extract suggested at: http://wiki.openstreetm...'''
date = "2016-02-12T10:36:00Z"
lastmod = "2016-02-12T16:18:00Z"
weight = 48070
keywords = [ "mapnik" ]
aliases = [ "/questions/48070" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Very basic Mapnik XML stylesheet showing ways and nodes](/questions/48070/very-basic-mapnik-xml-stylesheet-showing-ways-and-nodes)

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
<span id="post-48070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48070-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to create an extremely basic Mapnik XML stylesheet, so that I can display purely all ways and nodes in an OSM extract, for debugging purposes. It doesn't need to look pretty.</p>
<p>I am running this against a flat-file .osm file, using the Geofabrik extract suggested at: <a href="http://wiki.openstreetmap.org/wiki/Mapnik/Rendering_OSM_XML_data_directly">http://wiki.openstreetmap.org/wiki/Mapnik/Rendering_OSM_XML_data_directly</a></p>
<p>I can't get the nodes to show - what am I doing wrong? The ways are showing fine.</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;Map background-color=&quot;#f2efe9&quot; srs=&quot;+proj=latlong +datum=WGS84&quot;&gt;
&#10;       &lt;Style name=&quot;highways&quot;&gt;
                &lt;Rule&gt;
                        &lt;Filter&gt;[highway] &lt;&gt;&#39;&#39;&lt;/Filter&gt;
                        &lt;LineSymbolizer stroke=&quot;#808080&quot; stroke-width=&quot;2&quot; stroke-linejoin=&quot;round&quot; stroke-linecap=&quot;round&quot; /&gt;
                &lt;/Rule&gt;
        &lt;/Style&gt;
&#10;        &lt;Style name=&quot;nodes&quot;&gt;
               &lt;Rule&gt;
                        &lt;Filter&gt;[mapnik:geometry_type]=point&lt;/Filter&gt;
                        &lt;PointSymbolizer file=&quot;./hospital.16.svg&quot; /&gt;
                &lt;/Rule&gt;
        &lt;/Style&gt;
&lt;/Map&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '16, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/354d4e3cc1b448abb29eb4f1bbac395c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fooquency&#39;s gravatar image" />
<p><span>fooquency</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fooquency has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '16, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-48070" class="comments-container">
<span id="48071"></span>
<div id="comment-48071" class="comment">
<div id="post-48071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to say what format of data that these rules apply to. If its data imported to PostGIS to osm2pgsql then most nodes will not be represented directly.</p>
</div>
<div id="comment-48071-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 11:44)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="48074"></span>
<div id="comment-48074" class="comment">
<div id="post-48074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It'd be useful for someone to post a minimal mapnik.xml (or a minimal TileMill style) that can be used for people to start from when creating their own styles (perhaps for transparent overlay tiles).</p>
</div>
<div id="comment-48074-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 12:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48078"></span>
<div id="comment-48078" class="comment">
<div id="post-48078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/647/sk53">@SK53</a>: Have clarified that I'm using a flat-file .osm extract.</p>
</div>
<div id="comment-48078-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 16:18)</span> <span class="comment-user userinfo">fooquency</span>
</div>
</div>
</div>
<div id="comment-tools-48070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48070-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

