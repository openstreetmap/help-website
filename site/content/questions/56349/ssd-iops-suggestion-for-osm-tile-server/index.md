+++
type = "question"
title = "SSD IOPS suggestion for OSM tile server"
description = '''I have provisioned an OSM tile server, but rendering is still a little slow (60Gb mem, 8 CPUs). The postgresql data is living on an AWS throughput-optimized HDD, but I am considering trying an AWS SSD with pre-provisioned IOPS to see if that improves rendering. Are there recommendations for IOPS pro...'''
date = "2017-05-29T05:39:00Z"
lastmod = "2017-05-29T05:39:00Z"
weight = 56349
keywords = [ "performance", "rendering", "postgresql", "postgis", "tileserver" ]
aliases = [ "/questions/56349" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSD IOPS suggestion for OSM tile server](/questions/56349/ssd-iops-suggestion-for-osm-tile-server)

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
<span id="post-56349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56349-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have provisioned an OSM tile server, but rendering is still a little slow (60Gb mem, 8 CPUs). The postgresql data is living on an <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">AWS throughput-optimized HDD</a>, but I am considering trying an AWS SSD with pre-provisioned IOPS to see if that improves rendering. Are there recommendations for IOPS provisioning for the rendering disk? AWS makes you pay for provisioned IOPS, as well as storage. I don't want to over do it, but also don't want a bottleneck.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '17, 05:39</strong></p>
<img src="https://secure.gravatar.com/avatar/88d088c7b8b53519aa8026bd00ce121c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgwozdz&#39;s gravatar image" />
<p><span>rgwozdz</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgwozdz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56349" class="comments-container">
&#10;</div>
<div id="comment-tools-56349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56349-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

