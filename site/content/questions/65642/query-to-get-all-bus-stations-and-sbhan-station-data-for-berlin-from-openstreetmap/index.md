+++
type = "question"
title = "Query to get all bus stations and sBhan station data for Berlin from openstreetmap"
description = '''I am very new with openstreetmap and i am doing my university assignment. I am trying to get all bus station and sBhan data for Berlin in jsonform or any other useful form. I tried following but its not looks correct. overpass-turbo [out:json][timeout:25]; // gather results ( // query part for: “bar...'''
date = "2018-08-30T12:58:00Z"
lastmod = "2018-08-30T12:58:00Z"
weight = 65642
keywords = [ "openstreetmap" ]
aliases = [ "/questions/65642" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Query to get all bus stations and sBhan station data for Berlin from openstreetmap](/questions/65642/query-to-get-all-bus-stations-and-sbhan-station-data-for-berlin-from-openstreetmap)

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
<span id="post-65642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am very new with <a href="https://www.openstreetmap.org/#map=10/52.5072/13.4248">openstreetmap</a> and i am doing my university assignment. I am trying to get all bus station and sBhan data for Berlin in jsonform or any other useful form.</p>
<p>I tried following but its not looks correct. <a href="http://overpass-turbo.eu/s/Bv9">overpass-turbo</a></p>
<pre><code>[out:json][timeout:25];
// gather results
(
// query part for: “bar”
node[&quot;amenity&quot;=&quot;bus&quot;]({{bbox}});
way[&quot;amenity&quot;=&quot;bus&quot;]({{bbox}});
relation[&quot;amenity&quot;=&quot;bus&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>I would be great if some guide me how correctly i can access for bus and sBhan.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '18, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3cb42530f4db925a2e7b8fdba0c6124d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sajjadmurtaza&#39;s gravatar image" />
<p><span>sajjadmurtaza</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sajjadmurtaza has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '18, 13:15</strong> </span></p>
</div>
</div>
<div id="comments-container-65642" class="comments-container">
&#10;</div>
<div id="comment-tools-65642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65642-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

