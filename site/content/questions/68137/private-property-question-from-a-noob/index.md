+++
type = "question"
title = "Private Property - question from a Noob"
description = '''Hi all,  I&#x27;ve only just recently become a member of OpenStreetMaps, so I&#x27;m not sure how to mark a property as private. Background I use a site in the Netherlands that creates a walking route for me over the various public walking paths in the Netherlands. It uses OpenStreetMaps. One of the routes th...'''
date = "2019-02-25T12:39:00Z"
lastmod = "2019-02-25T14:59:00Z"
weight = 68137
keywords = [ "privateroad" ]
aliases = [ "/questions/68137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Private Property - question from a Noob](/questions/68137/private-property-question-from-a-noob)

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
<span id="post-68137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68137-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I've only just recently become a member of OpenStreetMaps, so I'm not sure how to mark a property as private.</p>
<p>Background I use a site in the Netherlands that creates a walking route for me over the various public walking paths in the Netherlands. It uses OpenStreetMaps. One of the routes that it created for me, takes me down what is a public road, which then briefly becomes someone's private property and then carries on being a public road. (I discovered this when the owner of the property got irate with me.)</p>
<p>The name of the street is Smalsteeg, Lunteren (in the Netherlands). (I have added a public note in OSM.</p>
<p>Question My question is - how can I get that change it so that it is clear that that particular part of the road is private property?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-privateroad" rel="tag" title="see questions tagged &#39;privateroad&#39;">privateroad</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '19, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/2bb4e10416b06f362021f0815c58eedb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markjowen&#39;s gravatar image" />
<p><span>markjowen</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markjowen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68137" class="comments-container">
&#10;</div>
<div id="comment-tools-68137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68137-form-container" class="comment-form-container">
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

<span id="68138"></span>

<div id="answer-container-68138" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68138-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am guessing the issue is with either <a href="https://www.openstreetmap.org/way/240879480">this way</a> or <a href="https://www.openstreetmap.org/way/240879485">this way</a> and <a href="https://www.openstreetmap.org/note/1692016">this is your note</a>, which would suggest the issue is with the first of the two parts of Smalsteeg. You'll need to sign up for an edit account, then the way with a private section will need splitting where it starts and stops being private (in the default editor, click the way you want to split, then double-click to add a node where you want to split it, then right-click the node and select the scissors to split the way). Once you've split the way on both sides of the private area, click the way that is private and scroll down to change Allowed Access from All=yes to All=private. Save your changes and at some point other websites will get the update.</p>
<p>I notice though that the way is mapped as part of <a href="http://www.openstreetmap.org/relation/3250561">a local walking route</a> which the <a href="https://klompenpaden.nl/klompenpad/turfvelderpad/">operator says is marked with red clogs</a>, so you might want to use "permissive" rather than "private", assuming the operator had suitable permissions to signpost the route.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '19, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-68138" class="comments-container">
<span id="68139"></span>
<div id="comment-68139" class="comment">
<div id="post-68139-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much!</p>
<p>With regards the "marked as part of a local walking route", yes, I saw that. And I think that that is why it got recommended to me as part of the walking route that I was following. However, the owner of the property in the middle of Smalsteeg was adamant that that was his property and not for public access. There is a public walking path that skirts around his property and comes back out onto the other side of Smalsteeg, but this is not shown on the map. (It was going to be my next question...)</p>
<p>Thanks again.</p>
</div>
<div id="comment-68139-info" class="comment-info">
<span class="comment-age">(25 Feb '19, 14:22)</span> <span class="comment-user userinfo">markjowen</span>
</div>
</div>
<span id="68142"></span>
<div id="comment-68142" class="comment">
<div id="post-68142-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>FYI, there is a Dutch forum where you can discuss things specific to the Netherlands: <a href="https://forum.openstreetmap.org/viewforum.php?id=12">https://forum.openstreetmap.org/viewforum.php?id=12</a></p>
</div>
<div id="comment-68142-info" class="comment-info">
<span class="comment-age">(25 Feb '19, 14:59)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-68138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68138-form-container" class="comment-form-container">
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

