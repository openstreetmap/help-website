+++
type = "question"
title = "How should the turn restrictions be added to this junction?"
description = '''How should the the turn restrictions for this junction be represented in the OSM data?  Also, some follow up questions:  In iD I can only figure out how to add simple turn restrictions - from way, via node, to way - not the more complicated turn restrictions with ways as via elements. Is this expect...'''
date = "2015-08-15T21:50:00Z"
lastmod = "2015-08-20T08:26:00Z"
weight = 44778
keywords = [ "turn_restrictions" ]
aliases = [ "/questions/44778" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How should the turn restrictions be added to this junction?](/questions/44778/how-should-the-turn-restrictions-be-added-to-this-junction)

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
<span id="post-44778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44778-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should the the turn restrictions for <a href="https://www.openstreetmap.org/node/1675447389">this junction</a> be represented in the OSM data?</p>
<p><img src="/upfiles/osm-complex-junction-crescent-salford-flat.png" alt="Complex junction in Salford" /></p>
<p>Also, some follow up questions:</p>
<ul>
<li>In iD I can only figure out how to add simple turn restrictions - from way, via node, to way - not the more complicated turn restrictions with ways as via elements. Is this expected?</li>
<li>I think I could represent the turn restrictions using such simple turn restrictions, if I added a diagonal way from B to D. But that would mean duplicating roads for routing purposes. Would this be frowned upon? What about splitting a way into two ways for the same purposes?</li>
<li>If turn restrictions via ways are needed, are there any routing engines that support such restrictions so I can check my edits behave as I expect, to check my work for errors? I understand <a href="https://github.com/Project-OSRM/osrm-backend/issues/483">OSRM doesn't</a> ?</li>
</ul>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '15, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/7167d2302007163407c44fdbb67e7358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michaelt&#39;s gravatar image" />
<p><span>michaelt</span><br />
<span class="score" title="111 reputation points">111</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michaelt has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-44778" class="comments-container">
&#10;</div>
<div id="comment-tools-44778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44778-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="44782"></span>

<div id="answer-container-44782" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44782-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/edisonbell_turn_restiction.JPG" alt="alt text" />The tagging of the routing through any junction requires that " one ways" and junction "nodes" each have the correct restrictions. Once you have done all of them you will have to wait for the routing engines to use that data. This is my question when i struggled with a pair of simpler junctions <a href="/questions/32420/turn-restrictions-and-routing-engines">https://help.openstreetmap.org/questions/32420/turn-restrictions-and-routing-engines</a> you could also use an editor to inspect similar junctions, to learn by example. We now have some excellent routers accessible from the map page that can now be used to check routing .. but you may have to wait for recent edits to be used by the routing engines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '15, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '15, 06:53</strong> </span></p>
</div>
</div>
<div id="comments-container-44782" class="comments-container">
&#10;</div>
<div id="comment-tools-44782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44782-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44809"></span>

<div id="answer-container-44809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44809-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at the present tagging of your junction it may not need any additional turn restrictions as the one ways seem to do the job. The jpeg shows the results that one router gives. Does this agree with the road signs?<img src="/upfiles/a_route_through_the_junction.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '15, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-44809" class="comments-container">
<span id="44811"></span>
<div id="comment-44811" class="comment">
<div id="post-44811-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Both OSRM and MapQuest allow traffic from A to D, from C to B, and U-turns from A to A and C to C. None of these are allowed according to the road signs..</p>
</div>
<div id="comment-44811-info" class="comment-info">
<span class="comment-age">(18 Aug '15, 23:08)</span> <span class="comment-user userinfo">michaelt</span>
</div>
</div>
<span id="44814"></span>
<div id="comment-44814" class="comment">
<div id="post-44814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think i understand now. I'll see if i can get to grips with iD's functions</p>
</div>
<div id="comment-44814-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 06:23)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="44815"></span>
<div id="comment-44815" class="comment">
<div id="post-44815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Initial tries suggest some new turn lanes may be needed, and turn restrictions at each individual node where necessary.</p>
</div>
<div id="comment-44815-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 06:27)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="44816"></span>
<div id="comment-44816" class="comment">
<div id="post-44816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did not add any turn lanes. I found that iD as very good turn restriction editing facilities. I have mapped some or all of them, You can inspect or change them of course. We can now wait and see if they work correctly when the routers get to use the updated info.</p>
</div>
<div id="comment-44816-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 06:50)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="44817"></span>
<div id="comment-44817" class="comment">
<div id="post-44817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have added some turn restrictions to your junction with iD. The tool to do this is neatly implemented in the iD editor. We will have to wait and see if they work, but I suspect that you are correct in your question that some restrictions might not be easy to map.</p>
</div>
<div id="comment-44817-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 07:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-44809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44839"></span>

<div id="answer-container-44839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44839-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was so impressed with iD's turn restriction implementation that I thought i would share them. It works like this. Start iD. Click on the junction node, click on the "in Way" and then "out ways" show red or green indicator, to change a red or a green one just click on it to toggle or swap over, Excellent. well done iD Guys.<img src="/upfiles/An_illustration_of_turn_restrictions_in_iD.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '15, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-44839" class="comments-container">
&#10;</div>
<div id="comment-tools-44839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44839-form-container" class="comment-form-container">
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

