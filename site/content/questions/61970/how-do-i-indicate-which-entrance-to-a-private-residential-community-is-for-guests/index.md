+++
type = "question"
title = "How do I indicate which entrance to a private residential community is for guests?"
description = '''I am aware of a number of nearby private residential communities with several entrances. The main entrance is for residents and guests to enter, the latter checking in at the guard booth. Other entrance gates don&#x27;t have a guard booth, and may be locked for maintenance access only, or may be open to ...'''
date = "2018-02-05T21:00:00Z"
lastmod = "2018-02-07T08:31:00Z"
weight = 61970
keywords = [ "access", "gate", "routing", "private" ]
aliases = [ "/questions/61970" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I indicate which entrance to a private residential community is for guests?](/questions/61970/how-do-i-indicate-which-entrance-to-a-private-residential-community-is-for-guests)

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
<span id="post-61970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61970-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am aware of a number of nearby private residential communities with several entrances. The main entrance is for residents and guests to enter, the latter checking in at the guard booth. Other entrance gates don't have a guard booth, and may be locked for maintenance access only, or may be open to residents with a passcode.</p>
<p>Streets beyond the guard booth are tagged highway=residential access=private. The entrance node is barrier=gate or barrier=lift_gate (should this also be access=private or is that unnecessary due to that tag being on the streets?). But what should I do with the back gate? How do I tell people reading the map and routing software to use the main gate?</p>
<p>Here is an example of a back gate (this one for maintenance only) and how it causes problems with routing (the correct route is to go all the way north to Oren Brown Road and in the main entrance): <a href="https://www.openstreetmap.org/node/5316953413">https://www.openstreetmap.org/node/5316953413</a> <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=28.2882%2C-81.4639%3B28.2962%2C-81.4632#map=16/28.2922/-81.4624">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=28.2882%2C-81.4639%3B28.2962%2C-81.4632#map=16/28.2922/-81.4624</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '18, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/564d262d61cd4fb6c46ccaf9385bc367?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mongo%20Poker&#39;s gravatar image" />
<p><span>Mongo Poker</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mongo Poker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61970" class="comments-container">
&#10;</div>
<div id="comment-tools-61970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61970-form-container" class="comment-form-container">
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

<span id="61981"></span>

<div id="answer-container-61981" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61981-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the barrier is mapped correctly. When I tested it with graphhopper routing didn't go via that gate (using either foot or car). I think the problem may be with OSRM, it is not as good as it used to be. Routers don't use new data for a number of days in my experience. The private tag seems to block all routing, which is correct. If you route to somewhere inside the private area the router will take you as close as possible via public roads or paths which isn't that useful. I doubt that any routers use guest tags for the guest entrance, but that is where visitors need to be routed to. In answer "how do i indicate.. " You could call it " Main Gate or Guest Entrance" and routing should go to that IF INCLUDED in the address of your end point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '18, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '18, 08:36</strong> </span></p>
</div>
</div>
<div id="comments-container-61981" class="comments-container">
<span id="61989"></span>
<div id="comment-61989" class="comment">
<div id="post-61989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm pretty sure Ballo didn't connect to Yowell before I joined them and added the gate. Anyway, routing certainly should take you into a private community if that's your destination. Maybe access=destination is better for these communities?</p>
</div>
<div id="comment-61989-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 15:55)</span> <span class="comment-user userinfo">Mongo Poker</span>
</div>
</div>
<span id="61993"></span>
<div id="comment-61993" class="comment">
<div id="post-61993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is the point of private then? This is graphhoppers route <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=28.2930%2C-81.4625%3B28.3028%2C-81.4649#map=15/28.2985/-81.4609">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=28.2930%2C-81.4625%3B28.3028%2C-81.4649#map=15/28.2985/-81.4609</a></p>
</div>
<div id="comment-61993-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 16:28)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="61996"></span>
<div id="comment-61996" class="comment">
<div id="post-61996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The point of access=private is to tell you that access is private. You can only enter if you have legitimate business there, such as living there or visiting a friend.</p>
<p>Graphhopper gives a worse result than going in the wrong gate: <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=28.2882%2C-81.4639%3B28.2962%2C-81.4632#map=16/28.2929/-81.4606">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=28.2882%2C-81.4639%3B28.2962%2C-81.4632#map=16/28.2929/-81.4606</a> It tells you to go into a different neighborhood and park at the end of the culdesac, then hop the fence into the neighborhood you want.</p>
</div>
<div id="comment-61996-info" class="comment-info">
<span class="comment-age">(07 Feb '18, 03:08)</span> <span class="comment-user userinfo">Mongo Poker</span>
</div>
</div>
<span id="61998"></span>
<div id="comment-61998" class="comment">
<div id="post-61998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do visitors have to stop and show a pass, or ring through what is the entrance procedure? You could also try asking Graphhopper or OSRM how their algorithms are set up and work in those situations.</p>
</div>
<div id="comment-61998-info" class="comment-info">
<span class="comment-age">(07 Feb '18, 08:31)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-61981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61981-form-container" class="comment-form-container">
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

