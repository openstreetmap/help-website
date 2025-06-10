+++
type = "question"
title = "How to fix incorrect import or incorrect reading in Nominatim?"
description = '''I compiled from git my own nominatim server, and imported the latest osm data for the country Malta. The address search index is inaccurate however, and is not the same as what is provided by the nominatim api. Example: http://nominatim.openstreetmap.org/details.php?place_id=60073339 Selects the tow...'''
date = "2015-05-26T13:09:00Z"
lastmod = "2015-05-26T13:09:00Z"
weight = 43220
keywords = [ "planet.osm", "nominatim", "osm" ]
aliases = [ "/questions/43220" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to fix incorrect import or incorrect reading in Nominatim?](/questions/43220/how-to-fix-incorrect-import-or-incorrect-reading-in-nominatim)

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
<span id="post-43220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43220-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I compiled from git my own nominatim server, and imported the latest osm data for the country Malta.</p>
<p>The address search index is inaccurate however, and is not the same as what is provided by the nominatim api.</p>
<p>Example: <a href="http://nominatim.openstreetmap.org/details.php?place_id=60073339">http://nominatim.openstreetmap.org/details.php?place_id=60073339</a> Selects the town to be Senglea</p>
<p><a href="http://robin.dazzlepanel.com/Nom/details.php?place_id=109025">http://robin.dazzlepanel.com/Nom/details.php?place_id=109025</a> Selects the town to be the city Valletta</p>
<p>Looking into the postgres osm/nominatim database, the table place_addressline has a column isaddress, which is a boolean. In the example above, the place_id for "Senglea" under "triq ir-Rizq", is marked as false. If this is marked as true, it works correctly. So how do I fix this issue when the nodes are being generated and indexed while installing and setting up Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet.osm" rel="tag" title="see questions tagged &#39;planet.osm&#39;">planet.osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '15, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/7674255f67227e173400c635f053e027?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChristopherBartolo&#39;s gravatar image" />
<p><span>ChristopherB...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChristopherBartolo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43220" class="comments-container">
&#10;</div>
<div id="comment-tools-43220" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43220-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

