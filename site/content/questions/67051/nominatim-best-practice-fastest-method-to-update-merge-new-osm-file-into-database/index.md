+++
type = "question"
title = "Nominatim. Best Practice / Fastest Method to update / merge new osm file into database?"
description = '''Hi. I&#x27;d set up Nominatim for the Uk using http://download.geofabrik.de/europe/great-britain-latest.osm.pbf without any issues. However I then wished to update the database with an additional set of data (in this case: http://download.geofabrik.de/europe/ireland-and-northern-ireland-latest.osm.pbf). ...'''
date = "2018-12-03T12:29:00Z"
lastmod = "2018-12-03T12:29:00Z"
weight = 67051
keywords = [ "nominatim", "postgresql" ]
aliases = [ "/questions/67051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim. Best Practice / Fastest Method to update / merge new osm file into database?](/questions/67051/nominatim-best-practice-fastest-method-to-update-merge-new-osm-file-into-database)

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
<span id="post-67051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67051-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi.</p>
<p>I'd set up Nominatim for the Uk using <a href="http://download.geofabrik.de/europe/great-britain-latest.osm.pbf">http://download.geofabrik.de/europe/great-britain-latest.osm.pbf</a> without any issues. However I then wished to update the database with an additional set of data (in this case: <a href="http://download.geofabrik.de/europe/ireland-and-northern-ireland-latest.osm.pbf).">http://download.geofabrik.de/europe/ireland-and-northern-ireland-latest.osm.pbf).</a></p>
<p>My first effort was to use <strong>./utils/update.php --import-file</strong> using the Irish file. However this crashed my machine whilst attempting to reindex the updated tables - the machine ran out of disk space. Having read that there were some issues doing updates like this, I truncated the database tables and tried running the update.php script again having first merged the two osm files using osmosis.</p>
<p>This loaded the basic data in ok but unfortunately the php isn't expecting some of the support tables to be empty as I was left with the placex data missing certain key fields, e.g. postcodes, parent_place_ids, centroids.</p>
<p><strong>Is there any script I could have run before the osm import to ensure these fields would have been populated?</strong><br />
(from looking about the setup.php and update.php files, I found a script to populate location_postcodes, and then ran a cursory update on placex thinking the trigger plsql would update the fields but it didn't work)</p>
<p>As it stands I've just dropped the database entirely and am re-running the full setup <strong>--all</strong> procedure but don't think this can be the best means of doing this...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '18, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ef56fd1ca827cd2c9068dbe283682611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mr%20Davros&#39;s gravatar image" />
<p><span>Mr Davros</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mr Davros has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-67051" class="comments-container">
&#10;</div>
<div id="comment-tools-67051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67051-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

