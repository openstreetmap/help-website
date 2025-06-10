+++
type = "question"
title = "How to map complicated intersection so cyclists can cross it"
description = '''I recently stumbled upon a situation where I&#x27;m a bit unsure how to properly represent it in OSM. It&#x27;s about this intersection: https://www.openstreetmap.org/#map=19/54.86651/11.11583 I noticed using osmand that it would not route me across that intersection from south to north. It&#x27;s not an osmand is...'''
date = "2021-08-27T09:44:00Z"
lastmod = "2021-08-27T13:38:00Z"
weight = 81517
keywords = [ "intersection", "mapping", "cycle" ]
aliases = [ "/questions/81517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to map complicated intersection so cyclists can cross it](/questions/81517/how-to-map-complicated-intersection-so-cyclists-can-cross-it)

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
<span id="post-81517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently stumbled upon a situation where I'm a bit unsure how to properly represent it in OSM.</p>
<p>It's about this intersection: <a href="https://www.openstreetmap.org/#map=19/54.86651/11.11583">https://www.openstreetmap.org/#map=19/54.86651/11.11583</a></p>
<p>I noticed using osmand that it would not route me across that intersection from south to north. It's not an osmand issue, but an issue with the data.</p>
<p>The streets from north and south (Tårs Landvej) split up into 1-directional streets before the intersection and end in the west-east street (Spodsbjergvej) at slightly different locations. This is in line with the situation on the ground.</p>
<p>The problem now is this: On the west-east street (Spodsbjergvej) cycling is forbidden (and dangerous), so it's correctly tagged with "bicycle:no". However it is absolutely possible to cross this intersection in north/south direction, that is even part of some local cycling routes. But for the routing this means you have to cross a few meters on the larger road with "bicycle:no", so a routing software will not route bicycles through this.</p>
<p>I'm wondering how to best adress this. One option would be splitting the west-east roat (Spodsbjergvej) both at the left and right entrypoints of Tårs Landvej and changing the piece between to "bicycle:yes". Would that be a good way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-cycle" rel="tag" title="see questions tagged &#39;cycle&#39;">cycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '21, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/b56f02655a9de3d7197ee0518f76f814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hanno&#39;s gravatar image" />
<p><span>hanno</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hanno has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81517" class="comments-container">
&#10;</div>
<div id="comment-tools-81517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81517-form-container" class="comment-form-container">
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

<span id="81518"></span>

<div id="answer-container-81518" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81518-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is ultimately a false precision issue that tends to afflict junction mappers - London, for example, is full of cases like this.</p>
<p>There is no need to map the "wiggle" between the north and south streets. It is a straight-across turn; anyone driving or cycling across this turn would continue straight on without having to make a left-then-right manoeuvre. The entrances/exits are expressly flared to permit this to happen.</p>
<p>A better way of mapping this would be to map the topology (i.e. the highway ways) with a straight-across intersection, and then to use <a href="https://wiki.openstreetmap.org/wiki/Key:area:highway">area:highway</a> to record the exact geometry of the junction. That conveys all the information without suggesting misleading manoeuvres to drivers or cyclists.</p>
<p>(The wiggle is a form of traffic calming, to slow drivers on the approach to the junction and prevent them going straight across without stopping. I could see some logic in having a dedicated <code>traffic_calming</code> tag for this but I don't believe one's ever been proposed.)</p>
<p>Martin Lucas-Smith from CycleStreets touched on some related issues in a talk at SOTM 2019 in <a href="https://www.youtube.com/watch?v=pMCnEFzjPD8">https://www.youtube.com/watch?v=pMCnEFzjPD8</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '21, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '21, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-81518" class="comments-container">
<span id="81519"></span>
<div id="comment-81519" class="comment">
<div id="post-81519-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The east west highway here might be divided long enough to justify separately mapped carriageways? In which case there would be enough wiggle room to include the chicane and have the north-south roads continue through.</p>
</div>
<div id="comment-81519-info" class="comment-info">
<span class="comment-age">(27 Aug '21, 13:38)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-81518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81518-form-container" class="comment-form-container">
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

