+++
type = "question"
title = "Why can&#x27;t I get routing service for new roads recently changed from Construction to Residential?"
description = '''I changed a few new roads from under construction to Residential but when I request routing service it returns &quot;error 4003: Routing Service failed with status 404 Not Found&quot; My question is, is there anything else required to do so that I may receive routes when I request route from GPS coordinate A ...'''
date = "2021-10-15T08:14:00Z"
lastmod = "2021-10-15T21:49:00Z"
weight = 82176
keywords = [ "gps" ]
aliases = [ "/questions/82176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I get routing service for new roads recently changed from Construction to Residential?](/questions/82176/why-cant-i-get-routing-service-for-new-roads-recently-changed-from-construction-to-residential)

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
<span id="post-82176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82176-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I changed a few new roads from under construction to Residential but when I request routing service it returns "<em>error 4003: Routing Service failed with status 404 Not Found</em>" My question is, is there anything else required to do so that I may receive routes when I request route from GPS coordinate A to coordinate B? Does the system generate gps data for these roads automatically or each road must be programmed manually?</p>
<p>I'm learning to improve my city. Forgive me if I broke a rule somewhere.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '21, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/92f4264b741f351d1723e283e88c1d57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TroneLegacy&#39;s gravatar image" />
<p><span>TroneLegacy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TroneLegacy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82176" class="comments-container">
<span id="82184"></span>
<div id="comment-82184" class="comment">
<div id="post-82184-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you get this message only when you try to route over the new roads? Or do you also get if you try somewhere completely different on the map?</p>
<p>Also, are you using the routing services on the openstreetmap.org home page, and if so are you using Graphhopper or OSRM?</p>
</div>
<div id="comment-82184-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 16:55)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="82191"></span>
<div id="comment-82191" class="comment">
<div id="post-82191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get this message only on zebra marked roads / under construction. One other thing I noticed is "these roads I have updated sort of change back to the old state in appearance (become zebra) when I zoom out. If I zoom back in they turn to white.</p>
<p>I'm requesting api data via MIT App inventor maps component, I believe Its OSRM in use.</p>
</div>
<div id="comment-82191-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 20:28)</span> <span class="comment-user userinfo">TroneLegacy</span>
</div>
</div>
</div>
<div id="comment-tools-82176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82176-form-container" class="comment-form-container">
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

<span id="82179"></span>

<div id="answer-container-82179" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82179-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-82179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure about the particular error messages you are getting, but...<br />
You are updating a database when editing the osm. The maps take time to be re-rendered and routing engines also need time update their routing. The standard, Cyclosm and Humanitarian map layers at www.openstreetmap.org update very soon, the others about a week later and the routing engines normally take quite a while to update too. So try the routing in a few days time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '21, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '21, 17:28</strong> </span></p>
</div>
</div>
<div id="comments-container-82179" class="comments-container">
<span id="82192"></span>
<div id="comment-82192" class="comment">
<div id="post-82192-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get the message only on the zebra marked roads (under construction). I noticed that "these roads I have updated sort of change back to the old state in appearance (become zebra) when I zoom out. If I zoom back in they turn to white."</p>
<p>I will give it a couple of days and then try again. Thank you for the heads up</p>
</div>
<div id="comment-82192-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 20:37)</span> <span class="comment-user userinfo">TroneLegacy</span>
</div>
</div>
<span id="82193"></span>
<div id="comment-82193" class="comment">
<div id="post-82193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On the standard layer at osm.org, I have found that map tiles for zoom levels 17 and 18 are usually the first to be updated and those further away have a slower update schedule and you see this difference when you zoom in and out.</p>
</div>
<div id="comment-82193-info" class="comment-info">
<span class="comment-age">(15 Oct '21, 21:49)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-82179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82179-form-container" class="comment-form-container">
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

