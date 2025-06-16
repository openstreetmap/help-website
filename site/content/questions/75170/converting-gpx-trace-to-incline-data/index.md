+++
type = "question"
title = "Converting .gpx trace to incline data"
description = '''When hiking, I record my track, with the altitude, and I&#x27;d like to extract the incline data to fill the incline tag in OSM. Is there a way to extract this information and fill the tag automatically ? Or do I need to manually compute the altitude difference in all segments an manually modify the incl...'''
date = "2020-06-06T18:02:00Z"
lastmod = "2020-06-08T12:20:00Z"
weight = 75170
keywords = [ "extract", "gpx", "incline" ]
aliases = [ "/questions/75170" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting .gpx trace to incline data](/questions/75170/converting-gpx-trace-to-incline-data)

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
<span id="post-75170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75170-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When hiking, I record my track, with the altitude, and I'd like to extract the incline data to fill the <a href="https://wiki.openstreetmap.org/wiki/Key:incline">incline tag</a> in OSM. Is there a way to extract this information and fill the tag automatically ? Or do I need to manually compute the altitude difference in all segments an manually modify the incline tag ?</p>
<p>I saw a <a href="/questions/36155/extract-inclines-from-gpx-file">related question</a>, but it is 6 years old, and post necromancy is kind of bad practice...</p>
<p>I found nothing like that in JOSM or in plugins.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-incline" rel="tag" title="see questions tagged &#39;incline&#39;">incline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '20, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/138c7fe091b8bb5bc01ba1e60f3f5607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pantoophle&#39;s gravatar image" />
<p><span>Pantoophle</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pantoophle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75170" class="comments-container">
<span id="75174"></span>
<div id="comment-75174" class="comment">
<div id="post-75174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you use to record elevation? While HDOP isn't great for GPS I was under the impression that VDOP was horrendous.</p>
</div>
<div id="comment-75174-info" class="comment-info">
<span class="comment-age">(06 Jun '20, 23:15)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75175"></span>
<div id="comment-75175" class="comment">
<div id="post-75175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use the default <a href="https://osmand.net/">OsmAnd~</a> pluggin to record a track. So it is basic GPS precision. And when plotting the altitude curve of the trace, the precision looks not too bad. Some points are wrong, but most of them look fine and coherent.</p>
</div>
<div id="comment-75175-info" class="comment-info">
<span class="comment-age">(07 Jun '20, 01:32)</span> <span class="comment-user userinfo">Pantoophle</span>
</div>
</div>
<span id="75177"></span>
<div id="comment-75177" class="comment">
<div id="post-75177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> Absolute precision of vertical position is usually unusable, I'm often under the sea for example. But relative precision is not so bad, I mean the error looks consistent for each session.</p>
<p><a href="https://help.openstreetmap.org/users/18500/pantoophle">@Pantoophle</a> I'm afraid I never seen something like that. I guess the best would be to write a JOSM plugin. But there are quite a few challenges. You'll have to make a statistical analysis a the altitude curve, remove outliers, decide where to split the ways, etc.</p>
</div>
<div id="comment-75177-info" class="comment-info">
<span class="comment-age">(07 Jun '20, 12:35)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="75197"></span>
<div id="comment-75197" class="comment">
<div id="post-75197-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not sure how useful it is to add the incline tag to OSM ways. Elevation aware routers can use SRTM and similar data sources. This is already done by various popular routers.</p>
</div>
<div id="comment-75197-info" class="comment-info">
<span class="comment-age">(08 Jun '20, 10:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="75199"></span>
<div id="comment-75199" class="comment">
<div id="post-75199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I'm using <a href="https://osmand.net/">OsmAnd~</a> to plan a hike, it displays the inclination of each segment of the circuit. But on many segments, it just displays "No Data". So I thought that I could fill this missing data.</p>
</div>
<div id="comment-75199-info" class="comment-info">
<span class="comment-age">(08 Jun '20, 12:08)</span> <span class="comment-user userinfo">Pantoophle</span>
</div>
</div>
<span id="75200"></span>
<div id="comment-75200" class="comment not_top_scorer">
<div id="post-75200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OsmAnd has a <a href="https://osmand.net/features/contour-lines-plugin">contour lines plugin</a> and hill shade maps to visualize terrain information. It also uses this information to influence bicycle and foot routing. This works without any incline tags.</p>
</div>
<div id="comment-75200-info" class="comment-info">
<span class="comment-age">(08 Jun '20, 12:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75170" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-75170-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

