+++
type = "question"
title = "when building tile server, can not download Shapefile"
description = '''Shapefile download # cd ~/src/openstreetmap-carto/ # scripts/get-external-data.py  INFO:root:Checking table water_polygons  why cannot download the shapefiel?'''
date = "2020-07-23T02:42:00Z"
lastmod = "2020-07-24T03:21:00Z"
weight = 75856
keywords = [ "building", "tile", "download", "shapefile", "server" ]
aliases = [ "/questions/75856" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [when building tile server, can not download Shapefile](/questions/75856/when-building-tile-server-can-not-download-shapefile)

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
<span id="post-75856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Shapefile download</p>
<pre><code># cd ~/src/openstreetmap-carto/
# scripts/get-external-data.py
&#10;INFO:root:Checking table water_polygons</code></pre>
<p>why cannot download the shapefiel?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '20, 02:42</strong></p>
<img src="https://secure.gravatar.com/avatar/4637c543421eb586aa1807010f43b39d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%E5%BC%A0%E6%B2%BB%E9%9F%B3&#39;s gravatar image" />
<p><span>张治音</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="张治音 has 2 accepted answers">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '20, 06:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-75856" class="comments-container">
&#10;</div>
<div id="comment-tools-75856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75856-form-container" class="comment-form-container">
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

<span id="75871"></span>

<div id="answer-container-75871" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75871-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have solved the problem that can not download the shapefile . As network is not good and the shapefile is too big, we can not download the shapefile zip . So we open the shell file 'openstreetmap-carto/external-data.yml', and get the info,as following,</p>
<pre><code>settings:
  temp_schema: loading
  schema: public
  data_dir: data
  database: gis
  metadata_table: external_data
sources:
  simplified_water_polygons:
    # The type of file this source is
    type: shp
    # Where to get it
    url: https://osmdata.openstreetmap.de/download/simplified-water-polygons-split-3857.zip
    # The location within the archive
    file: simplified-water-polygons-split-3857/simplified_water_polygons.shp
    archive:
      format: zip
      # Files to extract from the archive
      files:
&#10;  water_polygons:
    type: shp
    url: https://osmdata.openstreetmap.de/download/water-polygons-split-3857.zip
    file: water-polygons-split-3857/water_polygons.shp
    archive:
      format: zip
      files:
        icesheet_polygons:
    type: shp
    url: https://osmdata.openstreetmap.de/download/antarctica-icesheet-polygons-3857.zip
    file: antarctica-icesheet-polygons-3857/icesheet_polygons.shp
    archive:
      format: zip
      files:
        icesheet_outlines:
    type: shp
    url: https://osmdata.openstreetmap.de/download/antarctica-icesheet-outlines-3857.zip
    file: antarctica-icesheet-outlines-3857/icesheet_outlines.shp
    ogropts:
      - &quot;-explodecollections&quot;
    archive:
      format: zip
      files:
&#10;  ne_110m_admin_0_boundary_lines_land:
    type: shp
    url: http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_boundary_lines_land.zip
    file: ne_110m_admin_0_boundary_lines_land.shp
    ogropts: &amp;ne_opts
      - &quot;--config&quot;
      - &quot;SHAPE_ENCODING&quot;
      - &quot;WINDOWS-1252&quot;
      - &quot;-explodecollections&quot;
      # needs reprojecting
      - &#39;-t_srs&#39;
      - &#39;EPSG:3857&#39;
    archive:
      format: zip
      files:</code></pre>
<p>Then we download all the 5 *zip files manually , and put them to your web server, for me , The url is <a href="http://127.0.0.1/osm/">http://127.0.0.1/osm/</a></p>
<pre><code>  antarctica-icesheet-outlines-3857.zip 2020-07-24 09:37    51M  
  antarctica-icesheet-polygons-3857.zip 2020-07-24 09:37    51M  
  ne_110m_admin_0_boundary_lines_land.zip   2020-07-24 09:41    45K  
  simplified-water-polygons-split-3857.zip  2020-07-24 09:36    23M  
  water-polygons-split-3857.zip 2020-07-24 09:37    610M</code></pre>
<p>At last, we modify the shell file 'openstreetmap-carto/external-data.yml' ，instead of the url download to ours. As following,</p>
<pre><code>settings:
  temp_schema: loading
  schema: public
  data_dir: data
  database: gis
  metadata_table: external_data
sources:
  simplified_water_polygons:
    # The type of file this source is
    type: shp
    # Where to get it
    #url: https://osmdata.openstreetmap.de/download/simplified-water-polygons-split-3857.zip
    url: http://127.0.0.1/osm/simplified-water-polygons-split-3857.zip
    # The location within the archive
    file: simplified-water-polygons-split-3857/simplified_water_polygons.shp
    ...</code></pre>
<p>It's OK.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '20, 03:21</strong></p>
<img src="https://secure.gravatar.com/avatar/4637c543421eb586aa1807010f43b39d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%E5%BC%A0%E6%B2%BB%E9%9F%B3&#39;s gravatar image" />
<p><span>张治音</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="张治音 has 2 accepted answers">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '20, 06:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-75871" class="comments-container">
&#10;</div>
<div id="comment-tools-75871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75871-form-container" class="comment-form-container">
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

