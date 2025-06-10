+++
type = "question"
title = "How to detect place name (city/village etc) for a building (with street and building name) when name for area/boundary with admin_level = 8 is missing?"
description = '''I did a quick query on imported data (Europe) for administrative boundaries and I see all the admin boundaries up to level 7 have name tag provided for the area (with one exception only for relation 1727384, that has no such &quot;name&quot; tag).  The issue is with admin_level = 8 boundaries, because 1448 bo...'''
date = "2016-07-22T11:44:00Z"
lastmod = "2016-07-22T11:44:00Z"
weight = 51062
keywords = [ "admin_level", "boundary", "admin_boundary", "name" ]
aliases = [ "/questions/51062" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect place name (city/village etc) for a building (with street and building name) when name for area/boundary with admin_level = 8 is missing?](/questions/51062/how-to-detect-place-name-cityvillage-etc-for-a-building-with-street-and-building-name-when-name-for-areaboundary-with-admin_level-8-is-missing)

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
<span id="post-51062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51062-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did a quick query on imported data (Europe) for administrative boundaries and I see all the admin boundaries up to level 7 have name tag provided for the area (with one exception only for relation <a href="http://www.openstreetmap.org/relation/1727384" title="Missing &#39;name&#39; tag">1727384</a>, that has no such "name" tag).</p>
<p>The issue is with admin_level = 8 boundaries, because 1448 boundaries have no such name (but 105652 areas on level 8 has such name provided). Admin level 8 is a city or a village boundary for instance.</p>
<p>Sample: The relation with ID <a href="http://www.openstreetmap.org/relation/6071056">6071056</a> has no name, but has admin_centre node with name,<br />
relation <a href="http://www.openstreetmap.org/relation/5164506">5164506</a> has no name, but has some <a href="http://www.openstreetmap.org/node/337585514#map=15/48.7894/28.7913">node</a> inside this area with addr: and name tags.</p>
<p>In case of missing name tags for admin_level=8 areas should I look for any node inside such area with addr tags, or maybe there is some better idea to fix missing area names?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '16, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9d6cd718cdeb41535fa4aa16477eeeb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stalek&#39;s gravatar image" />
<p><span>stalek</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stalek has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '16, 11:59</strong> </span></p>
</div>
</div>
<div id="comments-container-51062" class="comments-container">
&#10;</div>
<div id="comment-tools-51062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51062-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

