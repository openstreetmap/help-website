+++
type = "question"
title = "Highway sections disappear when zoomed out. Rendering issue?"
description = '''Hi all, I&#x27;ve noticed that sections of Diagonal road (https://www.openstreetmap.org/edit#map=14/-35.0036/138.5411) are not highlighted in bold when zoomed out, but remain when zoomed back in. I only notice this in the editor, which wouldn&#x27;t be a problem, but Mapbox has a similar rendering issue which...'''
date = "2020-09-21T01:32:00Z"
lastmod = "2020-09-21T08:24:00Z"
weight = 76737
keywords = [ "rendering", "australia", "secondary" ]
aliases = [ "/questions/76737" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Highway sections disappear when zoomed out. Rendering issue?](/questions/76737/highway-sections-disappear-when-zoomed-out-rendering-issue)

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
<span id="post-76737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76737-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I've noticed that sections of Diagonal road (<a href="https://www.openstreetmap.org/edit#map=14/-35.0036/138.5411)">https://www.openstreetmap.org/edit#map=14/-35.0036/138.5411)</a> are not highlighted in bold when zoomed out, but remain when zoomed back in. I only notice this in the editor, which wouldn't be a problem, but Mapbox has a similar rendering issue which appears to break the roads, even when zoomed in (<a href="https://api.mapbox.com/styles/v1/mapbox/streets-v11.html?title=true&amp;access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#16.6/-35.002632/138.534638).">https://api.mapbox.com/styles/v1/mapbox/streets-v11.html?title=true&amp;access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#16.6/-35.002632/138.534638).</a> I don't think this is a caching/update time issue.</p>
<p>I'm assuming there's some property somewhere which is causing this inconsistency, but all the road segments look the same. I have found a few other instances of this in my local area, and I was wondering if someone could give me some pointers on how to begin fixing it. I've done some Googling around the problem, but found little information. I'm sure this is a simple fix, but maybe my keywords were not quite right.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-australia" rel="tag" title="see questions tagged &#39;australia&#39;">australia</span> <span class="post-tag tag-link-secondary" rel="tag" title="see questions tagged &#39;secondary&#39;">secondary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '20, 01:32</strong></p>
<img src="https://secure.gravatar.com/avatar/20e6e991604773d17b9f915ebdf83bf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dlbs&#39;s gravatar image" />
<p><span>dlbs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dlbs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76737" class="comments-container">
&#10;</div>
<div id="comment-tools-76737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76737-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="76738"></span>

<div id="answer-container-76738" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76738-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wouldn't expect an area that big to load in an in-browser editor at zoom level 14 without some data going missing. The data is in OSM - see <a href="https://www.openstreetmap.org/#map=18/-35.00377/138.53482&amp;layers=D">https://www.openstreetmap.org/#map=18/-35.00377/138.53482&amp;layers=D</a> .</p>
<p>The error that you can see at <a href="https://api.mapbox.com/styles/v1/mapbox/streets-v11.html?title=true&amp;access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#18.29/-35.003592/138.535455">https://api.mapbox.com/styles/v1/mapbox/streets-v11.html?title=true&amp;access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#18.29/-35.003592/138.535455</a> (and I can see too) is something that you'll need to talk to Mapbox about. The other layers that I see at osm.org don't show the error.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '20, 02:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76738" class="comments-container">
<span id="76741"></span>
<div id="comment-76741" class="comment">
<div id="post-76741-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I remember correctly the black road network shown when you zoom out in iD is provided by Mapbox. So it is only natural we see the same piece of road gone missing.</p>
</div>
<div id="comment-76741-info" class="comment-info">
<span class="comment-age">(21 Sep '20, 08:24)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76738-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

