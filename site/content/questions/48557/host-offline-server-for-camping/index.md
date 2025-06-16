+++
type = "question"
title = "Host Offline Server for Camping"
description = '''I&#x27;m working on a plan to create a &quot;campsite raspberry pi server&quot;. It has various features that I think would be useful to a group in the middle of nowhere.  This server will sit on a wifi network that isn&#x27;t connected to anything else. One thing that I would like to do is be able to have users on the...'''
date = "2016-03-08T04:43:00Z"
lastmod = "2016-03-14T20:18:00Z"
weight = 48557
keywords = [ "offline", "raspberry", "camping" ]
aliases = [ "/questions/48557" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Host Offline Server for Camping](/questions/48557/host-offline-server-for-camping)

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
<span id="post-48557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48557-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a plan to create a "campsite raspberry pi server". It has various features that I think would be useful to a group in the middle of nowhere.</p>
<p>This server will sit on a wifi network that isn't connected to anything else. One thing that I would like to do is be able to have users on the wifi pull down a map using an app or web interface.</p>
<p>I guess my question is multi parted: 1) can I install an OpenStreetMap server on a raspberry pi? 2) what would be the easiest way to get the maps to people who are only connected to this network? 3) can I select what is cached on the server? I would image the entire mapset is pretty large, so maybe only grabbing something smaller like the the local area would be better.</p>
<p>I'm thinking that having them go to something like maps.privatedomain.com in their browser would be easier than trying to force an app to connect to the local server?</p>
<p>I appreciate your input!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-raspberry" rel="tag" title="see questions tagged &#39;raspberry&#39;">raspberry</span> <span class="post-tag tag-link-camping" rel="tag" title="see questions tagged &#39;camping&#39;">camping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '16, 04:43</strong></p>
<img src="https://secure.gravatar.com/avatar/e6ecf6a0c3330b8d684325bf2e31e0a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TJZ&#39;s gravatar image" />
<p><span>TJZ</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TJZ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48557" class="comments-container">
&#10;</div>
<div id="comment-tools-48557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48557-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="48559"></span>

<div id="answer-container-48559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48559-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It really depends on</p>
<p>a) if you want to be able to update the data (that would make things complicated)</p>
<p>b) which services you actually want to provide</p>
<p>Lets assume the answer to a) is no.</p>
<p>If you assume that all connecting devices will be fast enough to do on device rendering, you could serve vector tiles from the device. You migh even be able to provide rough global coverage and detailed local tiles.</p>
<p>Search will be difficult, see <a href="https://www.openstreetmap.org/user/SimonPoole/diary/34857">https://www.openstreetmap.org/user/SimonPoole/diary/34857</a> for a potential solution (the XSCE site would be worth looking at in any case).</p>
<p>Routing you might want to have a look at <a href="https://graphhopper.com/">https://graphhopper.com/</a> or OSRM (OSRM woul require pre-processing on a larger machine).</p>
<p>Naturally if you want to make your life easier and are not doing it for the challenge of craming everything on to a RPi, repurposing an old laptop is likely to work a lot better.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-48559" class="comments-container">
<span id="48564"></span>
<div id="comment-48564" class="comment">
<div id="post-48564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response!</p>
<p>A) I would want to update the data maybe monthly? back when the pi was actually connected to the internet. would that be difficult? B) I think I need to learn a lot more about open street maps. I didn't realize how many components there were, instead was thinking I could just "cache" an area and serve it locally. Sounds like I need to do some research! C) I'm hoping the RPi3 is going to be powerful enough for my project, which involves more than just the OSM server. It's starting to look like I may be under-estimating my needs here.</p>
</div>
<div id="comment-48564-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 10:27)</span> <span class="comment-user userinfo">TJZ</span>
</div>
</div>
<span id="48566"></span>
<div id="comment-48566" class="comment">
<div id="post-48566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It really depends, there are a lot of options and in the end it really depends what your target audience has from a device pov.</p>
</div>
<div id="comment-48566-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 12:41)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48559-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48660"></span>

<div id="answer-container-48660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming that the people that you want to provide maps for will be away from the server for most of the time, maybe don't try and overthink it and just provide downloads of something like OsmAnd / Maps.me / other app of choice, plus data for the local area (in whatever format the app needs)?</p>
<p>That's assuming that people have got phones, that GPS works on them, and you've got a way of charging them all over the period that you're away.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '16, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48660" class="comments-container">
&#10;</div>
<div id="comment-tools-48660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48660-form-container" class="comment-form-container">
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

