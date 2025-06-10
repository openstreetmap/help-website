+++
type = "question"
title = "Is it mandatory to specify --style argument and --tag-transform-script in osm2pgsql query for importing .pbf file?"
description = '''I am trying to build a tile server that serves tiles of multiple styles(osm and osm-bright). I have followed this link for implementing this. But here I found that osm2pgsql query for importing .pdf file is specifing the --style argument and --tag-transform-script for importing data to postgres data...'''
date = "2018-07-11T17:15:00Z"
lastmod = "2018-07-11T17:15:00Z"
weight = 64659
keywords = [ "mapbox_osm-bright", "renderd", "openlayers", "osm2pgsql", "lua" ]
aliases = [ "/questions/64659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it mandatory to specify --style argument and --tag-transform-script in osm2pgsql query for importing .pbf file?](/questions/64659/is-it-mandatory-to-specify-style-argument-and-tag-transform-script-in-osm2pgsql-query-for-importing-pbf-file)

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
<span id="post-64659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64659-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to build a tile server that serves tiles of multiple styles(osm and osm-bright). I have followed this <a href="https://gis.stackexchange.com/questions/79077/serving-multiple-styles-from-tile-server">link</a> for implementing this. But <a href="https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/#load-data-to-postgis">here</a> I found that osm2pgsql query for importing .pdf file is specifing the --style argument and --tag-transform-script for importing data to postgres database.</p>
<pre><code>osm2pgsql -s -C 300 -c -G --hstore --style openstreetmap-carto.style --tag-transform-script openstreetmap-carto.lua -d gis -H $HOSTNAME -U postgres [.osm or .pbf file]</code></pre>
<p>So my question is that - Is it mandatory to use --style argument and --tag-transform-script osm2pgsql? If yes , what should be the alternate way for serving multiple styles?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapbox_osm-bright" rel="tag" title="see questions tagged &#39;mapbox_osm-bright&#39;">mapbox_osm-bright</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '18, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '18, 17:16</strong> </span></p>
</div>
</div>
<div id="comments-container-64659" class="comments-container">
&#10;</div>
<div id="comment-tools-64659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64659-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

