+++
type = "question"
title = "ERROR: result COPY_END for planet_osm_point failed: ERROR:  invalid input syntax for integer: &quot;0,1&quot;"
description = '''Can anyone help I set up a tile server, and imported the british-isles-latest.osm.pbf 10th Aug 2019, then starting doing the hour updates. It was working fine until it got to the following update 3624820, and then gave the error below Any one help me. Allocating memory for dense node cache Allocatin...'''
date = "2019-08-20T15:05:00Z"
lastmod = "2019-08-27T09:11:00Z"
weight = 70439
keywords = [ "import", "copy_end", "error" ]
aliases = [ "/questions/70439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ERROR: result COPY_END for planet_osm_point failed: ERROR: invalid input syntax for integer: "0,1"](/questions/70439/error-result-copy_end-for-planet_osm_point-failed-error-invalid-input-syntax-for-integer-01)

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
<span id="post-70439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70439-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone help</p>
<p>I set up a tile server, and imported the british-isles-latest.osm.pbf 10th Aug 2019, then starting doing the hour updates.</p>
<p>It was working fine until it got to the following update 3624820, and then gave the error below</p>
<p>Any one help me.</p>
<p>Allocating memory for dense node cache Allocating dense node cache in one big chunk Allocating memory for sparse node cache Sharing dense sparse Node-cache: cache=800MB, maxblocks=12800*65536, allocation method=11 Mid: pgsql, cache=800 Using built-in tag processing pipeline Using projection SRS 3857 (Spherical Mercator) Setting up table: planet_osm_point Setting up table: planet_osm_line Setting up table: planet_osm_polygon Setting up table: planet_osm_roads</p>
<p>Reading in file: /var/lib/mod_tile/changes.osc.gz Using XML parser. Processing: Node(1k 0.7k/s) Way(2k 1.35k/s) Relation(10 10.00/s) parse time: 4s Node stats: total(1373), max(6705113729) in 2s Way stats: total(2701), max(713278169) in 2s Relation stats: total(139), max(9912327) in 0s <strong>DB writer thread failed due to ERROR: result COPY_END for planet_osm_point failed: ERROR: invalid input syntax for integer: "0,1" CONTEXT: COPY planet_osm_point, line 9, column layer: "0,1"</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-copy_end" rel="tag" title="see questions tagged &#39;copy_end&#39;">copy_end</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '19, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/38e6d558e7e337c63ce2551c30287e3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karl_G&#39;s gravatar image" />
<p><span>Karl_G</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karl_G has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70439" class="comments-container">
<span id="70531"></span>
<div id="comment-70531" class="comment">
<div id="post-70531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Further to this error, I have located the lines that result in the error.</p>
<p>Can anyone explain what might be wrong?</p>
<p>DEBUG Worker thred - COPY -COPY planet_osm_point(osm_id,"access","addr:housename","addr:housenumber","addr:interpolation","admin_level","aerialway","aeroway","amenity","area","barrier","bicycle","brand","bridge","boundary","building","capital","construction","covered","culvert","cutting","denomination","disused","ele","embankment","foot","generator:source","harbour","highway","historic","horse","intermittent","junction","landuse","layer","leisure","lock","man_made","military","motorcar","name","natural","office","oneway","operator","place","population","power","power_source","public_transport","railway","ref","religion","route","service","shop","sport","surface","toll","tourism","tower:type","tunnel","water","waterway","wetland","width","wood","z_order",way) FROM STDIN Write Complete</p>
<p>DEBUG Worker thred - SYNC - DEBUG db_copy_thread_t::db_copy_thread_t DB writer thread failed due to ERROR: result COPY_END for planet_osm_point failed: ERROR: invalid input syntax for integer: "0,1" CONTEXT: COPY planet_osm_point, line 9, column layer: "0,1"</p>
</div>
<div id="comment-70531-info" class="comment-info">
<span class="comment-age">(27 Aug '19, 09:11)</span> <span class="comment-user userinfo">Karl_G</span>
</div>
</div>
</div>
<div id="comment-tools-70439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70439-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

