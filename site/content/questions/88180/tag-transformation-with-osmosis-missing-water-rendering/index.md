+++
type = "question"
title = "Tag Transformation with Osmosis - Missing water rendering"
description = '''Edit: No idea why my uploaded images aren&#x27;t shown. I&#x27;m trying to host my own map with a few changes, including renaming &quot;watery&quot; areas using osmosis and this docker setup. If I only try to match water or waterway everything works as expected, just missing some areas that don&#x27;t have those tags. code ...'''
date = "2024-01-20T12:38:00Z"
lastmod = "2024-01-20T22:38:00Z"
weight = 88180
keywords = [ "tag", "transformation", "osmosis" ]
aliases = [ "/questions/88180" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tag Transformation with Osmosis - Missing water rendering](/questions/88180/tag-transformation-with-osmosis-missing-water-rendering)

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
<span id="post-88180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Edit: No idea why my uploaded images aren't shown.</p>
<p>I'm trying to host my own map with a few changes, including renaming "watery" areas using <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> and <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">this</a> docker setup. If I only try to match water or waterway everything works as expected, just missing some areas that don't have those tags.</p>
<p><a href="https://imgur.com/a/HKmoDSz">code</a></p>
<pre><code>osmosis --read-pbf bw.osm.pbf --tag-transform file=&quot;transforms.xml&quot; --write-pbf updated-bw.osm.pbf</code></pre>
<p><a href="https://imgur.com/a/qQwwa30">renamed rhine</a></p>
<p>As soon as I add any mention of <code>natural:*</code> water areas just disappear.</p>
<p><a href="https://imgur.com/a/GEjwIIF">transform xml with natural key</a><br />
<a href="https://imgur.com/a/r6ZJAOO">Rhine not renamed and missing the blue color</a></p>
<p>I just started using OSM, so my knowledge is limied. How does this happen and what would be the correct way to make this work? The log then "sometimes" spout out errors:</p>
<pre><code>Mapnik LOG&gt; 2024-01-19 21:55:02: SVG PARSING ERROR:&quot;SVG support error: &lt;enable-background&gt; attribute is not supported&quot;
Mapnik LOG&gt; 2024-01-19 21:55:04: SVG PARSING ERROR:&quot;SVG support error: &lt;enable-background&gt; attribute is not supported&quot;
Mapnik LOG&gt; 2024-01-19 21:55:04: SVG PARSING ERROR:&quot;SVG support error: &lt;overflow&gt; attribute is not supported&quot;
Mapnik LOG&gt; 2024-01-19 21:55:04: SVG PARSING ERROR:&quot;SVG support error: &lt;enable-background&gt; attribute is not supported&quot;
Mapnik LOG&gt; 2024-01-19 21:55:04: SVG PARSING ERROR:&quot;SVG support error: &lt;enable-background&gt; attribute is not supported&quot;
Mapnik LOG&gt; 2024-01-19 21:55:04: SVG PARSING ERROR:&quot;SVG support error: &lt;enable-background&gt; attribute is not supported&quot;
Mapnik LOG&gt; 2024-01-19 21:55:04: SVG PARSING ERROR:&quot;SVG support error: &lt;enable-background&gt; attribute is not supported&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-transformation" rel="tag" title="see questions tagged &#39;transformation&#39;">transformation</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '24, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ea22c4c883c5cf3c0f4b703818b87102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gor1lla&#39;s gravatar image" />
<p><span>Gor1lla</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gor1lla has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '24, 12:51</strong> </span></p>
</div>
</div>
<div id="comments-container-88180" class="comments-container">
<span id="88181"></span>
<div id="comment-88181" class="comment">
<div id="post-88181-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect the $64,000 question will be "what's actually in the database"?</p>
<p>Just to check, everything works (and you don't get the "Mapnik log errors" when you are not using osmosis?</p>
</div>
<div id="comment-88181-info" class="comment-info">
<span class="comment-age">(20 Jan '24, 14:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="88182"></span>
<div id="comment-88182" class="comment">
<div id="post-88182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info, in case it helps, some <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L386">working transformations</a> (using osmium and osm-tag-transform, but perhaps adaptable to your use).</p>
</div>
<div id="comment-88182-info" class="comment-info">
<span class="comment-age">(20 Jan '24, 14:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="88184"></span>
<div id="comment-88184" class="comment">
<div id="post-88184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@SomeonElse It works as expected if I don't change anything or just the waterways. I used the Baden-Wuerttemberg map from here <a href="https://download.geofabrik.de/europe/germany.html">https://download.geofabrik.de/europe/germany.html</a></p>
</div>
<div id="comment-88184-info" class="comment-info">
<span class="comment-age">(20 Jan '24, 22:38)</span> <span class="comment-user userinfo">Gor1lla</span>
</div>
</div>
</div>
<div id="comment-tools-88180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88180-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

