+++
type = "question"
title = "How to put street name in a particular position"
description = '''For the map of the city of Havana, particularly in the Vedado neighborhood, I want to put the street names in a particular position. They should all be lined up... The neighborhood city plan is such that all the streets are organized in an alpha numeric grid. Currently, on the OSM the names are just...'''
date = "2014-03-19T15:15:00Z"
lastmod = "2014-03-20T08:38:00Z"
weight = 31692
keywords = [ "street", "streetnames" ]
aliases = [ "/questions/31692" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to put street name in a particular position](/questions/31692/how-to-put-street-name-in-a-particular-position)

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
<span id="post-31692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31692-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For the map of the city of Havana, particularly in the Vedado neighborhood, I want to put the street names in a particular position. They should all be lined up... The neighborhood city plan is such that all the streets are organized in an alpha numeric grid. Currently, on the OSM the names are just scattered. This makes it impossible to understand the grid. I want to line up the names so that the map looks more like this (<a href="http://2.bp.blogspot.com/-r2XUDMm5wjQ/UEiEc_h8kGI/AAAAAAAAic8/PiLNAwe6WUg/s1600/mapa-havana-cuba.JPG).">http://2.bp.blogspot.com/-r2XUDMm5wjQ/UEiEc_h8kGI/AAAAAAAAic8/PiLNAwe6WUg/s1600/mapa-havana-cuba.JPG).</a> Here you can easily see the organization. If somebody tells me how to do this, I will take care of the re positioning.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '14, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/25beddcf8ca60dbef8a269f7152e8b73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moe_greene&#39;s gravatar image" />
<p><span>moe_greene</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moe_greene has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31692" class="comments-container">
<span id="31694"></span>
<div id="comment-31694" class="comment">
<div id="post-31694-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which map rendering toolkit do you use? Where is your "the map"? Or do you want to add a hint for renderers in the data?</p>
</div>
<div id="comment-31694-info" class="comment-info">
<span class="comment-age">(19 Mar '14, 15:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31692-form-container" class="comment-form-container">
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

<span id="31713"></span>

<div id="answer-container-31713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31713-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't, and shouldn't, do this.</p>
<p>OpenStreetMap is a massive database of facts - where the world's roads and paths go, and what they're called. Our challenge is to record those facts, and nothing else.</p>
<p>Lots of different software then takes this database and does things with it. The "renderer" that you see on the front page of openstreetmap.org is one (a renderer takes the database and draws a map out of it). There are other renderers - you can click on the little three-layer icon on the front page for a few, but hundreds more exist. There are also "routers", which give driving directions from this database; and many other tools.</p>
<p>If you try to tweak the data such that it looks "right" on one renderer, you are potentially messing it up for another renderer. (For example, if you split the roads into segments to adjust the name positioning on the OSM front-page renderer, you might cause those names to disappear entirely on a renderer which uses a different or bigger font.)</p>
<p>So - please don't.</p>
<p>Instead, if you think the "rules" which the renderer uses to place labels could be improved, then you can make a suggestion to the volunteers who run that renderer. For the standard front-page style, the suggestions list is at <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a>, under "Issues" (you'll need a github.com account to post). Please be polite and humble when submitting issues!</p>
<p><em>(Unfortunately, for what it's worth, I suspect the particular challenges of this location are unusual and it would be difficult, perhaps impossible, for the renderer rules to be changed to get the result you desire. But I may be wrong and there's no harm in asking.)</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '14, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Mar '14, 08:40</strong> </span></p>
</div>
</div>
<div id="comments-container-31713" class="comments-container">
&#10;</div>
<div id="comment-tools-31713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31713-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31711"></span>

<div id="answer-container-31711" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31711-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-31711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, try to unite or combine the streets or ways with the same name, but only if Calle1 is the same as 1 ? Please contact the local community to make sure they want the same as you ! The old method to make a map readable is to minimize the visible elements but if all the Streets have one name tag, the tags should end up just below each other.</p>
<p>There has been a discussion about a look-a-like situation. Please read these questions and answers, as well:</p>
<ul>
<li><a href="/questions/20187/">more-road-names</a></li>
<li><a href="/questions/8023/">how-do-i-move-a-placename-label</a>. - The most voted answer in the last line is: don't do anything, leave it to the renderer !!</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '14, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '14, 22:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31711" class="comments-container">
&#10;</div>
<div id="comment-tools-31711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31711-form-container" class="comment-form-container">
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

