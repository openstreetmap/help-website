+++
type = "question"
title = "Data error when extract region from planet file"
description = '''I use osmium tool to extract smaller regions from the latest planet file: mirror: https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-220620.osm.pbf md5sum: https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-220620.osm.pbf.md5 The osmium extra...'''
date = "2022-06-28T10:44:00Z"
lastmod = "2022-06-28T10:44:00Z"
weight = 84906
keywords = [ "osmium", "extract", "planet_osm" ]
aliases = [ "/questions/84906" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Data error when extract region from planet file](/questions/84906/data-error-when-extract-region-from-planet-file)

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
<span id="post-84906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84906-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use osmium tool to extract smaller regions from the latest planet file:</p>
<p>mirror: <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-220620.osm.pbf">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-220620.osm.pbf</a> md5sum: <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-220620.osm.pbf.md5">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-220620.osm.pbf.md5</a></p>
<p>The osmium extract command ends with:</p>
<pre><code>failed to uncompress data: data error</code></pre>
<p>I checked the md5sum of downloaded planet file and seems to be correct:</p>
<pre><code>$md5sum planet-latest.osm.pbf
9cad5ab2818bb5abe08695974965407e  planet-latest.osm.pbf</code></pre>
<p>When osmium fileinfo -e</p>
<pre><code>osmium fileinfo planet-latest.osm.pbf
File:
  Name: planet-latest.osm.pbf
  Format: PBF
  Compression: none
  Size: 68838422488
Header:
  Bounding boxes:
    (-180,-90,180,90)
  With history: no
  Options:
    generator=planet-dump-ng 1.2.3
    osmosis_replication_timestamp=2022-06-19T23:59:47Z
    pbf_dense_nodes=true
    pbf_optional_feature_0=Has_Metadata
    pbf_optional_feature_1=Sort.Type_then_ID
    sorting=Type_then_ID
    timestamp=2022-06-19T23:59:47Z
[======================================================================] 100%
failed to uncompress data: data error</code></pre>
<p>I don't expect there to be any problem with the planet file or osmium-tool. However, could I ask you for advice on how to solve this problem?</p>
<p>Thanks, Petr</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '22, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/de468b49f909fd6238f169c4c8a225d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VOLDY&#39;s gravatar image" />
<p><span>VOLDY</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VOLDY has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84906" class="comments-container">
&#10;</div>
<div id="comment-tools-84906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

