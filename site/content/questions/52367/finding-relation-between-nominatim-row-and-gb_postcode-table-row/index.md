+++
type = "question"
title = "Finding relation between Nominatim row and gb_postcode table row?"
description = '''Currently I have PgAdmin 3 open with a copy of the Nominatim DB I processed on a Linux virtual machine. I imported the gb_postcode.sql database successfully from the Nominatim documentation but I&#x27;m struggling to find a way to match a row in my main placex table in Nominatim to my gb_postcode table t...'''
date = "2016-10-04T14:29:00Z"
lastmod = "2016-10-04T14:40:00Z"
weight = 52367
keywords = [ "nominatim", "osm" ]
aliases = [ "/questions/52367" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Finding relation between Nominatim row and gb_postcode table row?](/questions/52367/finding-relation-between-nominatim-row-and-gb_postcode-table-row)

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
<span id="post-52367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52367-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Currently I have PgAdmin 3 open with a copy of the Nominatim DB I processed on a Linux virtual machine. I imported the gb_postcode.sql database successfully from the Nominatim documentation but I'm struggling to find a way to match a row in my main <code>placex</code> table in Nominatim to my <code>gb_postcode</code> table that's been imported.</p>
<p>Both tables provide a <code>Geometry</code> row, of which I tried using <code>ST_Intersection</code> on but the result was beyond inaccurate (returned 1.6m records rather than a single one, or a small subset of data).</p>
<p>Is there any way currently that will allow me to find a relationship between a <code>Geometry</code> object in a Nominatim record (such as <code>0102000020E61000000500000014A5CEED6F5A01C07D6F78E68A1A4A4091E398767B5A01C08A517C21891A4A404221020EA15A01C02E05FFB6821A4A405698631E9E5A01C0CBC1C7BB7E1A4A40A53D14BB6C5A01C026A36F777B1A4A40</code>) and the <code>Geometry</code> object in the <code>gb_postcode</code> table (such as <code>0101000020E61000005D96EA24715B01C0A76FB0828F1A4A40</code>)?</p>
<p>For examples sake, these two Geometry values are matching for the same street in the UK, but I'm struggling to relate them programmatically.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '16, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-52367" class="comments-container">
<span id="52368"></span>
<div id="comment-52368" class="comment">
<div id="post-52368-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Crossposted: <a href="http://gis.stackexchange.com/questions/212981/finding-relation-between-nominatim-row-and-gb-postcode-table-row">http://gis.stackexchange.com/questions/212981/finding-relation-between-nominatim-row-and-gb-postcode-table-row</a></p>
</div>
<div id="comment-52368-info" class="comment-info">
<span class="comment-age">(04 Oct '16, 14:40)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
</div>
<div id="comment-tools-52367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52367-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

