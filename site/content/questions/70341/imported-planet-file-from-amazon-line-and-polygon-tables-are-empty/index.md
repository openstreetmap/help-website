+++
type = "question"
title = "Imported planet file from Amazon, line and polygon tables are empty"
description = '''Hi, I imported the latest planet pbf file from AWS (s3://osm-pds) using osm2pgsql. It finished successfully, but the line and polygon tables are empty. I&#x27;m using a custom style and lua transform script, but I&#x27;ve done the same thing in the past and it&#x27;s worked fine. From what I&#x27;ve found it sounds lik...'''
date = "2019-08-07T23:52:00Z"
lastmod = "2019-08-20T20:00:00Z"
weight = 70341
keywords = [ "amazon", "pbf", "aws", "osm2pgsql" ]
aliases = [ "/questions/70341" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Imported planet file from Amazon, line and polygon tables are empty](/questions/70341/imported-planet-file-from-amazon-line-and-polygon-tables-are-empty)

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
<span id="post-70341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I imported the latest planet pbf file from AWS (s3://osm-pds) using osm2pgsql. It finished successfully, but the line and polygon tables are empty. I'm using a custom style and lua transform script, but I've done the same thing in the past and it's worked fine.</p>
<p>From what I've found it sounds like this can happen if the nodes/ways/rels aren't ordered correctly in the planet file. However I don't think Amazon is rearranging the data in their pbf...?</p>
<p>So two questions:</p>
<ol>
<li>What could've caused this?</li>
<li>Is there a way I can salvage the data I've imported without reimporting?</li>
</ol>
<p>Thanks,</p>
<p>Steve</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amazon" rel="tag" title="see questions tagged &#39;amazon&#39;">amazon</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '19, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/3d2f621468caf19f818a4efaf77c4a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skmoore&#39;s gravatar image" />
<p><span>skmoore</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skmoore has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70341" class="comments-container">
<span id="70343"></span>
<div id="comment-70343" class="comment">
<div id="post-70343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you share the last few lines of output when osm2pgsql ran? Are you sure it completed successfully?</p>
</div>
<div id="comment-70343-info" class="comment-info">
<span class="comment-age">(08 Aug '19, 09:05)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70347"></span>
<div id="comment-70347" class="comment">
<div id="post-70347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>NOTICE: Self-intersection at or near point -8947023.3594009988 2985562.7520912946 NOTICE: Self-intersection at or near point 7148486.4317922518 7047035.3777957428 Copying planet_osm_point to cluster by geometry finished Creating geometry index on planet_osm_point NOTICE: Self-intersection at or near point 14317693.027572632 8695223.7255895436 Copying planet_osm_roads to cluster by geometry finished Creating geometry index on planet_osm_roads NOTICE: Self-intersection at or near point 6506904.3278176021 5395859.9191456046 NOTICE: Self-intersection at or near point 4729261.1576032471 7937547.0538152577 Creating osm_id index on planet_osm_roads Creating osm_id index on planet_osm_point</p>
<p>Osm2pgsql took 472546s overall</p>
</div>
<div id="comment-70347-info" class="comment-info">
<span class="comment-age">(08 Aug '19, 17:15)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
<span id="70406"></span>
<div id="comment-70406" class="comment">
<div id="post-70406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I imported again using a planet file from planet.openstreetmap.org, having the same problem. I checked the osm2pgsql syntax I'm using and I don't see any issues. Any ideas...?</p>
</div>
<div id="comment-70406-info" class="comment-info">
<span class="comment-age">(17 Aug '19, 01:19)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
<span id="70443"></span>
<div id="comment-70443" class="comment">
<div id="post-70443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I ran a test importing a Central America pbf from Geofabrik, used the same style and transform and the same osm2pgsql syntax, this worked fine.</p>
<p>Has something changed with the planet files available at planet.openstreetmap.org?</p>
</div>
<div id="comment-70443-info" class="comment-info">
<span class="comment-age">(20 Aug '19, 20:00)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
</div>
<div id="comment-tools-70341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70341-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

