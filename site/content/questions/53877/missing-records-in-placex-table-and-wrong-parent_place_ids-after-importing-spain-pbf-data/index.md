+++
type = "question"
title = "Missing records in placex table and wrong parent_place_ids after importing Spain pbf data."
description = '''Hi: I have just installed nominatim (version 2.5.1) and imported the data for Spain from geofabrik in pbf format. Both the installation and the import processes finished without any problem.  After everything was imported, I compared the content of the details.php page for the &quot;Spain&quot; record for our...'''
date = "2017-01-05T17:34:00Z"
lastmod = "2017-01-05T17:34:00Z"
weight = 53877
keywords = [ "missing_records", "import", "nominatim", "inconsistency" ]
aliases = [ "/questions/53877" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing records in placex table and wrong parent_place_ids after importing Spain pbf data.](/questions/53877/missing-records-in-placex-table-and-wrong-parent_place_ids-after-importing-spain-pbf-data)

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
<span id="post-53877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53877-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi:</p>
<p>I have just installed nominatim (version 2.5.1) and imported the data for Spain from <a href="http://download.geofabrik.de/europe/spain.html">geofabrik</a> in pbf format. Both the installation and the import processes finished without any problem.</p>
<p>After everything was imported, I compared the content of the details.php page for the "Spain" record for our dataset with the one in nominatim.openstreetmap.com. And they are quite different:</p>
<p><a href="http://osm.tubaritu.com/details.php?place_id=3720192">Our installation</a> displays only 5 records in the section "Parent Of" while the <a href="https://nominatim.openstreetmap.org/details.php?place_id=159419888">nominatim site</a> displays all the administrative areas and other records. Any idea of why is this happening?</p>
<p>Other thing that we have observed is that there are some records which are missing in our system. For example, <a href="https://www.openstreetmap.org/relation/349050">the relation 349050</a> is missing. I run a sql query "SELECT * FROM placex where osm_id=349050" and the record is not there. It looks like the data is not complete or something went wrong during the import process. Any idea of where might the problem be? Anybody with the same problem?</p>
<p>Thanks.</p>
<p>UPDATE: after looking at the records in our placex table, I've noticed that there are only 5 records whose parent_place_id column is Spain. I've also checked that all the administrative areas that are shown in the <a href="https://nominatim.openstreetmap.org/details.php?place_id=159419888">Spain details.php of the nominatim site</a> have parent_place_id equals to zero. Still investigating the issue.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-missing_records" rel="tag" title="see questions tagged &#39;missing_records&#39;">missing_records</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-inconsistency" rel="tag" title="see questions tagged &#39;inconsistency&#39;">inconsistency</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '17, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/08757e88b3d4d98d7045b20f8339b794?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LuisLopez89&#39;s gravatar image" />
<p><span>LuisLopez89</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LuisLopez89 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '17, 07:09</strong> </span></p>
</div>
</div>
<div id="comments-container-53877" class="comments-container">
&#10;</div>
<div id="comment-tools-53877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53877-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

