+++
type = "question"
title = "is there an alternative to graphhopper for walking routes?"
description = '''Hi Guys, We&#x27;ve created a nice little wordpress plugin that allows us to create trails of religious spots across some fairly barren areas. The problem is that we have 9 trails and each trail has around 8 markers. The GraphHopper subscription we would need is 160 a month which is way to high for us, i...'''
date = "2021-04-20T19:31:00Z"
lastmod = "2021-04-21T18:41:00Z"
weight = 79768
keywords = [ "routes", "trails", "walking", "graphhopper" ]
aliases = [ "/questions/79768" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [is there an alternative to graphhopper for walking routes?](/questions/79768/is-there-an-alternative-to-graphhopper-for-walking-routes)

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
<span id="post-79768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79768-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>We've created a nice little wordpress plugin that allows us to create trails of religious spots across some fairly barren areas. The problem is that we have 9 trails and each trail has around 8 markers.</p>
<p>The GraphHopper subscription we would need is 160 a month which is way to high for us, it will not be a popular site, just a few pilgrims following a trail.</p>
<p>Is there an alternative method to create a walking trail with this amount of spots along the way?</p>
<p>David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span> <span class="post-tag tag-link-trails" rel="tag" title="see questions tagged &#39;trails&#39;">trails</span> <span class="post-tag tag-link-walking" rel="tag" title="see questions tagged &#39;walking&#39;">walking</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '21, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/e14c263b574077a1560a94637d73702c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidHenry&#39;s gravatar image" />
<p><span>DavidHenry</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidHenry has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-79768" class="comments-container">
<span id="79769"></span>
<div id="comment-79769" class="comment">
<div id="post-79769-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Can you explain more about the plugin. If you say that the trails are known and fixed, then what would you need a routing engine for? You could just save them to a file and display them? I am obviously missing some important detail.</p>
</div>
<div id="comment-79769-info" class="comment-info">
<span class="comment-age">(20 Apr '21, 19:45)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="79776"></span>
<div id="comment-79776" class="comment">
<div id="post-79776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, maybe my terminology is wrong, I'm new to OSM. The plugin uses the api to get the addresses, then records the coordinates.</p>
<p>The displayed map then shows the markers with a colour coded line connecting them in the correct order.</p>
<p>Are you saying that I don't need Graphhopper to do this?</p>
<p>David</p>
</div>
<div id="comment-79776-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 08:25)</span> <span class="comment-user userinfo">DavidHenry</span>
</div>
</div>
<span id="79777"></span>
<div id="comment-79777" class="comment">
<div id="post-79777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How often do you do that David? For me it sounds like a one time exercise for each of the nine trails (routes). Once you have recorded the coordinates they won't change. Thus no need for a subscription.</p>
<p>Maybe we take this from the other direction: Tell us what a user of your website (the few pilgrims you mentioned) are expecting to see and do. Are they just looking at a map (possibly to print out) or do they need a turn by turn navigation along the trail? Do they need driving directions to the start of the route? Will they change routes?</p>
</div>
<div id="comment-79777-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 08:49)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79784"></span>
<div id="comment-79784" class="comment">
<div id="post-79784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, your right, the maps have historical points, churches don't move about much so they are very unlikely to change. Once the marker is set it's permanent.</p>
<p>When the users visit the site, they click on a route/trail, they see the info and a map which has a start and finish, with markers along the way, the markers are connected by a trail. Something like this: <a href="https://prnt.sc/11snvcf">https://prnt.sc/11snvcf</a></p>
</div>
<div id="comment-79784-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 09:57)</span> <span class="comment-user userinfo">DavidHenry</span>
</div>
</div>
</div>
<div id="comment-tools-79768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79768-form-container" class="comment-form-container">
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

<span id="79798"></span>

<div id="answer-container-79798" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79798-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you want to do is create a GeoJSON file that contains the markers and/or route that you want to display, and then load that into your Leaflet or OpenLayers map. Since the route does, according to what you write above, not depend on any input from the user, there is absolutely no need why everyone looking at your map would need to have a route calculated by Graphhopper. Everyone can simply look at the route that you have created, and supplied in a GeoJSON file. This will require a little programming but, having created a WordPress plugin, you are no stranger to that.</p>
<p>(Note that even if you're not using the Graphhopper service, your plugin still depends on using a free map tile source, likely openstreetmap.org. While "just a few pilgrims following a trail" is unlikely to pose a problem, should your app become more popular you will want to study <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> to make sure you can continue to use this free resource.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '21, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79798" class="comments-container">
&#10;</div>
<div id="comment-tools-79798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79798-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79778"></span>

<div id="answer-container-79778" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79778-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you just want a static map with trails marked on it, would something like <a href="https://umap.openstreetmap.fr/en/">uMap</a> work?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '21, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-79778" class="comments-container">
<span id="79786"></span>
<div id="comment-79786" class="comment">
<div id="post-79786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, looking into this now.</p>
</div>
<div id="comment-79786-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 10:09)</span> <span class="comment-user userinfo">DavidHenry</span>
</div>
</div>
<span id="79797"></span>
<div id="comment-79797" class="comment">
<div id="post-79797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>unfortunately uMap didn't work for us.</p>
</div>
<div id="comment-79797-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 17:55)</span> <span class="comment-user userinfo">DavidHenry</span>
</div>
</div>
</div>
<div id="comment-tools-79778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79778-form-container" class="comment-form-container">
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

