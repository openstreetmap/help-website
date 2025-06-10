+++
type = "question"
title = "Can a route relation be added with &quot;state=proposed&quot;, if informal groups propose the route, or does it need to be an official body?"
description = '''A new user has been adding a few new bicycle routes, that seem to have been developed informally on various online communities, like facebook, ridewithgps, and others. I am concerned that this editor may be misunderstanding the scope of OSM, and is using it as an central part in a decentralized rout...'''
date = "2020-08-07T20:06:00Z"
lastmod = "2020-08-17T13:14:00Z"
weight = 76051
keywords = [ "route", "bicycle", "proposed", "relations" ]
aliases = [ "/questions/76051" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Can a route relation be added with "state=proposed", if informal groups propose the route, or does it need to be an official body?](/questions/76051/can-a-route-relation-be-added-with-stateproposed-if-informal-groups-propose-the-route-or-does-it-need-to-be-an-official-body)

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
<span id="post-76051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A new user has been adding a few new bicycle routes, that seem to have been developed informally on various online communities, like facebook, ridewithgps, and others. I am concerned that this editor may be misunderstanding the scope of OSM, and is using it as an central part in a decentralized route sharing initiative. Or at least adding routes based on their own options, with no official backing.</p>
<p>Am I correct that route relations should only refer to officially designated routes, and proposed ones should only be officially proposed ones?</p>
<p><strong>edit:</strong> Here's a link to the changeset where the majority of the conversation has taken place, <a href="https://www.openstreetmap.org/changeset/88962380">https://www.openstreetmap.org/changeset/88962380</a>, with other topics are covered also</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-proposed" rel="tag" title="see questions tagged &#39;proposed&#39;">proposed</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '20, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '20, 07:37</strong> </span></p>
</div>
</div>
<div id="comments-container-76051" class="comments-container">
<span id="76056"></span>
<div id="comment-76056" class="comment">
<div id="post-76056-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"state=proposed" would be a poor way of indicating that a route is proposed. A tag like that puts the burden on the data consumer to consciously process such a tag and determine whether the route actually exists or not. If the data consumer doesn't consider the "state" tag, then the route would seem to be active. A better way would be to use a lifecycle prefix, so the route would be tagged "proposed:route=bicycle". That shifts the burden and makes the route inactive by default, so it isn't accidentally shown as being active. If a data consumer is interested in proposed routes, they can choose to include it if they wish.</p>
</div>
<div id="comment-76056-info" class="comment-info">
<span class="comment-age">(07 Aug '20, 22:10)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-76051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76051-form-container" class="comment-form-container">
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

<span id="76102"></span>

<div id="answer-container-76102" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76102-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="keithonearth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You mentioned in a comment the same test that I would use:</p>
<p>"It seems to me that the route should at least be proposed by an organization that has the capability to signpost the route."</p>
<p>Other than that, I would simply remove the "casually proposed" routes from OpenStreetMap completely.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '20, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-76102" class="comments-container">
&#10;</div>
<div id="comment-tools-76102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76053"></span>

<div id="answer-container-76053" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76053-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally speaking routes should be signposted or otherwise marked in real life to make them verifiable. Whether they are "official" or not is not particularly relevant to OSM. Personal favourite routes etc. generally shouldn't be added unless they are also marked.</p>
<p>There has been debate over the years to what extent unmarked routes that "everyone local knows about" should be included, but no clear consensus as far as I'm aware. There has been some mapping of proposed public roads, but this is not without controversy either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '20, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76053" class="comments-container">
<span id="76054"></span>
<div id="comment-76054" class="comment">
<div id="post-76054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To clarify, when I say "not particularly relevant" I mean to determine whether to include them, tags for network and or operator are or course welcome per <a href="https://wiki.openstreetmap.org/wiki/Cycle_routes">the wiki</a>.</p>
</div>
<div id="comment-76054-info" class="comment-info">
<span class="comment-age">(07 Aug '20, 21:03)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76061"></span>
<div id="comment-76061" class="comment">
<div id="post-76061-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm talking about proposed routes, so as such they wouldn't be signposted yet. There is no intention to signpost this route at any time, other than the hope that if he/she/they do a good enough job maybe one day they will approach municipalities, or the Canada Bikes Association, with the hopes of getting it approved, and then possibly signposted.</p>
<p>It seems to me that the route should at least be proposed by an organization that has the capability to signpost the route. A loose group of people talking on facebook, with the hope to get other groups to do the actual signposting seems insufficient to me.</p>
</div>
<div id="comment-76061-info" class="comment-info">
<span class="comment-age">(08 Aug '20, 01:40)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="76062"></span>
<div id="comment-76062" class="comment">
<div id="post-76062-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd suggest that there should be a pretty high bar for proposed routes of any sort to be in OSM - perhaps (a) it's actually got funding to be built, (b) there isn't significant opposition that might stop it being built and (c) it will actually be signed when it is built.</p>
<p>Without those caveats all sorts of "pet project" and "hobby horse" routes will end up in OSM and will just sit there, because in the real world they're never going to happen.</p>
</div>
<div id="comment-76062-info" class="comment-info">
<span class="comment-age">(08 Aug '20, 02:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76053-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76159"></span>

<div id="answer-container-76159" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76159-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Personally I don't bother with proposals, official or otherwise. They seem to so rarely come to fruition or end up being nothing like the original layout. Roads can take decades. Sustrans (cycling UK) has 'proposals' longer than your arm.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '20, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76159" class="comments-container">
&#10;</div>
<div id="comment-tools-76159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76159-form-container" class="comment-form-container">
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

