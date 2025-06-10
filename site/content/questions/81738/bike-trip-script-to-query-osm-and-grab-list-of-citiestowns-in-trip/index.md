+++
type = "question"
title = "[Bike trip] Script to query OSM and grab list of cities/towns in trip?"
description = '''Hello, As a low-fi backup for my smarphone that I use as GPS during bike trips, I&#x27;m thinking of printing it on a single page to have a rough idea where I should head using a compass, and run a script that will 1) take the (simplfied down to 500 points) trip as input, 2) query OSM for all the towns a...'''
date = "2021-09-14T15:49:00Z"
lastmod = "2021-09-14T15:49:00Z"
weight = 81738
keywords = [ "overpass" ]
aliases = [ "/questions/81738" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Bike trip\] Script to query OSM and grab list of cities/towns in trip?](/questions/81738/bike-trip-script-to-query-osm-and-grab-list-of-citiestowns-in-trip)

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
<span id="post-81738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81738-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>As a low-fi backup for my smarphone that I use as GPS during bike trips, I'm thinking of printing it on a single page to have a rough idea where I should head using a compass, and run a script that will 1) take the (simplfied down to 500 points) trip as input, 2) query OSM for all the towns and cities along the way, and 3) output the list that I'll then use as a road book.</p>
<p>Provided Overpass won't complain with too many queries, would someone have some code to share (ideally Python)?</p>
<p>Thank you.</p>
<hr />
<p>Edit: The following query looks close to what I need. Is it the right way to find the city/town a point lives in?</p>
<pre><code>//How to also search for _nodes_ in just one query?
&#10;way[&quot;place&quot;~&quot;(city|town)&quot;](around:500,50.540853270068986,8.048780365649707,50.53106288705902,8.030823236553783);
&#10;(._;&gt;;);
&#10;out meta;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '21, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/222fc1ad4f1993620a21cb57fa816f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shohreh&#39;s gravatar image" />
<p><span>Shohreh</span><br />
<span class="score" title="85 reputation points">85</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shohreh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '21, 11:32</strong> </span></p>
</div>
</div>
<div id="comments-container-81738" class="comments-container">
&#10;</div>
<div id="comment-tools-81738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81738-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

