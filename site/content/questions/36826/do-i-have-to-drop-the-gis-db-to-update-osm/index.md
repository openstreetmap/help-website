+++
type = "question"
title = "Do I have to drop the gis DB to update OSM?"
description = '''I previously had downloaded a metro extract from the OSM metro extracts page, and now found a site that offers individual state extract PBFs. I followed the instructions at http://switch2osm.org/loading-osm-data/ and for some reason the new data I imported, while it did not error out or anything and...'''
date = "2014-09-15T00:49:00Z"
lastmod = "2014-09-15T00:49:00Z"
weight = 36826
keywords = [ "update", "postgis", "tileserver" ]
aliases = [ "/questions/36826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Do I have to drop the gis DB to update OSM?](/questions/36826/do-i-have-to-drop-the-gis-db-to-update-osm)

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
<span id="post-36826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36826-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I previously had downloaded a metro extract from the OSM metro extracts page, and now found a site that offers individual state extract PBFs. I followed the instructions at <a href="http://switch2osm.org/loading-osm-data/">http://switch2osm.org/loading-osm-data/</a> and for some reason the new data I imported, while it did not error out or anything and is taking up the additional space - is not displaying when I view my tile server.</p>
<p>I did a <code>rm -fr /var/lib/tile</code> as well as service restarts on apache2 &amp; renderd, and after that didn't work even fully rebooted the machine. It's still stuck looking like it's "cached" the old tiles and isn't displaying the new "larger area" of data.</p>
<p>In psql, I did a \dt and it shows the same # of tables and table names. The size of the database, again, has increased - was ~270 MBs and is now ~862 MBs - so the data IS in there, just not displaying.</p>
<p>Do I have to drop the gis database and re-create it from the templates? Or is there an easier way to update this data?</p>
<p>Ubuntu 14.04 64-bit</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '14, 00:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '15, 20:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36826" class="comments-container">
&#10;</div>
<div id="comment-tools-36826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36826-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

