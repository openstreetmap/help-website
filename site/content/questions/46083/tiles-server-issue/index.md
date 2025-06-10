+++
type = "question"
title = "tiles server issue"
description = '''i got some troubles with Configuring OSM Bright. it the switch2osm web site they said i need to use nano and &quot;Find the lines with URLs pointing to shapefiles (ending .zip) and replace each one with these appropriate pairs of lines&quot; what does it mean, how do i use the nano , and can i looking for sha...'''
date = "2015-10-23T20:39:00Z"
lastmod = "2015-10-23T20:39:00Z"
weight = 46083
keywords = [ "style", "switch2osm", "tileserver" ]
aliases = [ "/questions/46083" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tiles server issue](/questions/46083/tiles-server-issue)

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
<span id="post-46083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i got some troubles with Configuring OSM Bright. it the switch2osm web site they said i need to use nano and "Find the lines with URLs pointing to shapefiles (ending .zip) and replace each one with these appropriate pairs of lines"</p>
<p>what does it mean, how do i use the nano , and can i looking for shapefiles.. ? can someone explain me how i do this part .</p>
<pre><code>Configuring OSM Bright The OSM Bright stylesheet now needs to be adjusted to include the location of our data files. Edit the file osm-bright/osm-bright.osm2pgsql.mml in your favourite text editor, for example:
&#10;nano osm-bright/osm-bright.osm2pgsql.mml
&#10;Find the lines with URLs pointing to shapefiles (ending .zip) and replace each one with these appropriate  pairs of lines: &quot;file&quot;: &quot;/usr/local/share/maps/style/osm-bright-master/shp/land-polygons-split-3857/land_polygons.shp&quot;, &quot;type&quot;: &quot;shape&quot;
&#10;&quot;file&quot;: &quot;/usr/local/share/maps/style/osm-bright-master/shp/simplified-land-polygons-complete-3857/simplified_land_polygons.shp&quot;, &quot;type&quot;: &quot;shape&quot;,
&#10;&quot;file&quot;: &quot;/usr/local/share/maps/style/osm-bright-master/shp/ne_10m_populated_places_simple/ne_10m_populated_places_simple.shp&quot;, &quot;type&quot;: &quot;shape&quot;
&#10;Note that we are also adding “type”: “shape” to each one. (If you’re using nano, to save, now press ctrl-X and Y.) Finally, in the section dealing with “ne_places”, replace the “srs” and “srs-name” lines with this one line:
&#10;&quot;srs&quot;: &quot;+proj=longlat +ellps=WGS84
+datum=WGS84 +no_defs&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '15, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/6b66d6d6b94b411a9d897ff1887c43e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elad159&#39;s gravatar image" />
<p><span>elad159</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elad159 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '15, 23:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46083" class="comments-container">
&#10;</div>
<div id="comment-tools-46083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46083-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

