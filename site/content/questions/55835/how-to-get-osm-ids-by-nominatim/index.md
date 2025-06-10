+++
type = "question"
title = "How to get OSM IDs by Nominatim?"
description = '''For a local installation of the OSM and Nominatim databases, is there a way to get the OSM IDs of the individual address fields returned by a Nominatim query? For example, when two queries return the same city name, is there a way to determine whether or not this is in fact the same city, rather tha...'''
date = "2017-04-24T20:41:00Z"
lastmod = "2017-04-24T21:26:00Z"
weight = 55835
keywords = [ "nominatim", "id", "sql" ]
aliases = [ "/questions/55835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get OSM IDs by Nominatim?](/questions/55835/how-to-get-osm-ids-by-nominatim)

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
<span id="post-55835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55835-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For a local installation of the OSM and Nominatim databases, is there a way to get the OSM IDs of the individual address fields returned by a Nominatim query?</p>
<p>For example, when two queries return the same city name, is there a way to determine whether or not this is in fact the same city, rather than two cities with the same name?</p>
<p>An SQL select statement or a short "how to do this in SQL" would be very much appreciated. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '17, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/cf64e6fd5b4e577f7915f054fa1eb5e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxmeier12&#39;s gravatar image" />
<p><span>maxmeier12</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxmeier12 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '18, 19:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55835" class="comments-container">
<span id="55836"></span>
<div id="comment-55836" class="comment">
<div id="post-55836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>details.php from nominatim seems to have code doing this:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=158768940">http://nominatim.openstreetmap.org/details.php?place_id=158768940</a></p>
<p>(The "Address" section lists several Paris entries mapping to different OSM objects)</p>
</div>
<div id="comment-55836-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 21:26)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-55835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55835-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

