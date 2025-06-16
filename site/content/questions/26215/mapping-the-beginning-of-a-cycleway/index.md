+++
type = "question"
title = "Mapping the beginning of a cycleway"
description = '''I am trying to find the best way to tag the following situation:  It is a bike path that starts near the intersection of two streets. It is necessary to somehow indicate that the path communicates with the roads. One way to do it of course is by adding the red line shown in the picture, and tagging ...'''
date = "2013-09-09T03:01:00Z"
lastmod = "2013-09-10T18:35:00Z"
weight = 26215
keywords = [ "bicycle" ]
aliases = [ "/questions/26215" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping the beginning of a cycleway](/questions/26215/mapping-the-beginning-of-a-cycleway)

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
<span id="post-26215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26215-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to find the best way to tag the following situation:</p>
<p><img src="/upfiles/crossing2.png" alt="alt text" /></p>
<p>It is a bike path that starts near the intersection of two streets. It is necessary to somehow indicate that the path communicates with the roads. One way to do it of course is by adding the red line shown in the picture, and tagging it as highway=cycleway.</p>
<p>Is there a more accurate way to tag this, that will still work well with routing? How about tagging the red segment as cycleway=crossing (without any other tags)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '13, 03:01</strong></p>
<img src="https://secure.gravatar.com/avatar/245cb5e781c1e0ce4e41027252ef9377?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Augusto%20S&#39;s gravatar image" />
<p><span>Augusto S</span><br />
<span class="score" title="111 reputation points">111</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Augusto S has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '13, 03:01</strong> </span></p>
</div>
</div>
<div id="comments-container-26215" class="comments-container">
<span id="26225"></span>
<div id="comment-26225" class="comment">
<div id="post-26225-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I regularly face this kind of conundrum for pedestrians as well. Most annoying is when I need to show that an area is connected (for routing but not geometrically) to a way. I haven't found a satisfying solution yet.</p>
</div>
<div id="comment-26225-info" class="comment-info">
<span class="comment-age">(09 Sep '13, 10:58)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26215-form-container" class="comment-form-container">
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

<span id="26217"></span>

<div id="answer-container-26217" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26217-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-26217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Augusto S has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your solution is fine and the red line is definitely required for a correct routing. Although there is a <a href="https://wiki.openstreetmap.org/wiki/Key:crossing">crossing</a> tag it is only used to describe points where one can cross the road from one side to the other.</p>
<p>Your proposed <em>cycleway=crossing</em> without any other tags wouldn't get recognized by any router because it is not an established tag. And it misses the highway key which is usually crucial for vehicle and pedestrian routing. Furthermore this is not a real crossing but more a link. So one could theoretically use both <em>highway=cycleway</em> and <em><a href="http://taginfo.openstreetmap.org/tags/cycleway=link">cycleway=link</a></em>.</p>
<p>Another solution would be to add <em><a href="https://wiki.openstreetmap.org/wiki/Key:cycleway">cycleway</a>=track</em> to the <em>existing</em> highway and remove the separate cycleway. See the <a href="https://wiki.openstreetmap.org/wiki/Bicycle">bicycle page on the wiki</a> for an overview with examples on the different cycleway values.</p>
<p>And don't forget to check the access restrictions. If you use <em>highway=cycleway</em> then you also need to add <em>foot=yes</em> to the way if pedestrians are allowed to walk there, too. Because according to the <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">default access restrictions</a> pedestrians are not allowed on cycleways. Forgetting to add this tag is a common error.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '13, 07:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '13, 07:43</strong> </span></p>
</div>
</div>
<div id="comments-container-26217" class="comments-container">
<span id="26238"></span>
<div id="comment-26238" class="comment">
<div id="post-26238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The only thing against tagging the red segment as highway=cycleway is that it is going to rendered in the map, and will look ugly. That's why I was looking for something that allows the router to determine the ways are connected, but is typically not rendered. But if there's not such a thing, it will stick to that solution.</p>
<p>[This cycleway soon diverges from the road, that's why I am not using cycleway=track.]</p>
</div>
<div id="comment-26238-info" class="comment-info">
<span class="comment-age">(09 Sep '13, 19:49)</span> <span class="comment-user userinfo">Augusto S</span>
</div>
</div>
<span id="26241"></span>
<div id="comment-26241" class="comment">
<div id="post-26241-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Don't give too much importance of rendering aspects. OSM is in anyway just a simplified view of the real world. The roads are not a simple thin line. A line is not an area and we have to accept some simplification, especially around the junctions.</p>
</div>
<div id="comment-26241-info" class="comment-info">
<span class="comment-age">(10 Sep '13, 09:25)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="26245"></span>
<div id="comment-26245" class="comment">
<div id="post-26245-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sometimes, I add short "artificial" ways like the one shown above to aid pedestrian routing around some pedestrian-only bridges (they would be unconnected to anything if they did not exist, and no routing would take place through them) and large bus stations (no other way to reach the bus stops without them). If they do not exist physically, I tag them with a note saying "Artificial for routing purposes".</p>
</div>
<div id="comment-26245-info" class="comment-info">
<span class="comment-age">(10 Sep '13, 11:09)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="26258"></span>
<div id="comment-26258" class="comment">
<div id="post-26258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am getting convinced that a special tag for "non-physical", router-aiding highways should be created to handle these situations.</p>
</div>
<div id="comment-26258-info" class="comment-info">
<span class="comment-age">(10 Sep '13, 18:35)</span> <span class="comment-user userinfo">Augusto S</span>
</div>
</div>
</div>
<div id="comment-tools-26217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26217-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26216"></span>

<div id="answer-container-26216" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26216-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-26216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Augusto, If I were mapping this I'd start the cycleway from the road running vertically - shift click to add new node then shift click on the node to start cycleway running off to the left. The road running left to right is already connected to the road running vertically (if I have interpreted your screen print correctly) so routing would be able to follow from that connection to the new connection you made when you drew the cycleway. I don't think your 'red line' linking all three elements (2 roads &amp; 1 cycleway) is needed. Ask me more if I haven't explained clearly enough! Graham</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '13, 06:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0b78593a39b9f71b9697697876327c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NZGraham&#39;s gravatar image" />
<p><span>NZGraham</span><br />
<span class="score" title="1814 reputation points"><span>1.8k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="49 badges"><span class="bronze">●</span><span class="badgecount">49</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NZGraham has 7 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-26216" class="comments-container">
&#10;</div>
<div id="comment-tools-26216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26216-form-container" class="comment-form-container">
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

