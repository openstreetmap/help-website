+++
type = "question"
title = "Can anyone explain the Amenity = Cafe Name Display sorcery to me?"
description = '''I&#x27;m looking at a couple of cafes in Bolton:- https://www.openstreetmap.org/node/4971453023 and https://www.openstreetmap.org/node/4971453026 Both are on the same building block and both are tagged exactly the same way, i.e.amenity = cafe and name = whatever. However one cafe title renders at zoom le...'''
date = "2018-12-13T10:20:00Z"
lastmod = "2018-12-14T19:23:00Z"
weight = 67155
keywords = [ "openstreetmap", "rendering", "amenity", "name" ]
aliases = [ "/questions/67155" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can anyone explain the Amenity = Cafe Name Display sorcery to me?](/questions/67155/can-anyone-explain-the-amenity-cafe-name-display-sorcery-to-me)

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
<span id="post-67155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67155-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking at a couple of cafes in Bolton:-</p>
<p><a href="https://www.openstreetmap.org/node/4971453023">https://www.openstreetmap.org/node/4971453023</a><br />
and<br />
<a href="https://www.openstreetmap.org/node/4971453026">https://www.openstreetmap.org/node/4971453026</a></p>
<p>Both are on the same building block and both are tagged exactly the same way, i.e.amenity = cafe and name = whatever.</p>
<p>However one cafe title renders at zoom level 18 (The Kitchen) and disappears at level 19, with other (The Bolton Town Coffee) only appearing at level 19!</p>
<p>Can anyone explain how this is happens?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '18, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ef56fd1ca827cd2c9068dbe283682611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mr%20Davros&#39;s gravatar image" />
<p><span>Mr Davros</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mr Davros has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67155" class="comments-container">
<span id="67203"></span>
<div id="comment-67203" class="comment">
<div id="post-67203-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"sorcery" is an appropriate term. Nobody knows which label Mapnik will choose, and nobody can control it!</p>
</div>
<div id="comment-67203-info" class="comment-info">
<span class="comment-age">(14 Dec '18, 19:23)</span> <span class="comment-user userinfo">LivingWithDr...</span>
</div>
</div>
</div>
<div id="comment-tools-67155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67155-form-container" class="comment-form-container">
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

<span id="67157"></span>

<div id="answer-container-67157" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67157-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-67157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mr Davros has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's the Mapnik label collision algorithm. A web search for this term produces a reasonable number of hits, such as this <a href="https://mapnik.org/news/gsoc2012-status8">one</a>.</p>
<p>When more than one label exists in the same space it will choose one of them to render. As the algorithm works independently for each individual tile there is no reason why one POI will always be guaranteed to appear. This is particularly true when additional labels may be present at one zoom level and therefore the label clashes will themselves be different. Another factor is differences in font size between layers</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '18, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-67157" class="comments-container">
<span id="67158"></span>
<div id="comment-67158" class="comment">
<div id="post-67158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's worth mentioning that I've noticed (in a different map style) far more problems with names disappearing in recent Mapnik versions than previous ones. Not all seem to be related to label collisions (though it looks to me like yours is) - the issue seems to be with label placement relative to the icon and no amount of text-dy tweaking to move it away seems to resolve the issue.</p>
<p>Incidentally you appear to have one of the cafes twice - see <a href="https://map.atownsend.org.uk/maps/map/map.html#zoom=21&amp;lat=53.576628&amp;lon=-2.4279712">here</a>.</p>
</div>
<div id="comment-67158-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 10:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67165"></span>
<div id="comment-67165" class="comment">
<div id="post-67165-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. That's a good, understandable explanation re what happens at level 18. However, why would "The Kitchen" appear at 18 yet disappear at 19? There isn't any other labels being rendered around it, so it's surprising to see that label disappear.</p>
<p>(I also saw that duplication of one of the cafes, thanks)</p>
</div>
<div id="comment-67165-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 13:10)</span> <span class="comment-user userinfo">Mr Davros</span>
</div>
</div>
<span id="67166"></span>
<div id="comment-67166" class="comment">
<div id="post-67166-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess the label "The Kitchen" collides with the icon of <a href="https://www.openstreetmap.org/node/4971453025">this shop</a>.</p>
</div>
<div id="comment-67166-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 13:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67167"></span>
<div id="comment-67167" class="comment">
<div id="post-67167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, ok got you - so even though that shop has no name (and therefore no title), Mapnik is doing some process whereby it works out a reserved width for the shop label and considers it would clash with the cafe.</p>
<p>I guess there should be an additional rule to check if that shop was actually named before calling out a clash or maybe it's just the shop "The Money Shop" on the other side causing the clash.</p>
<p>Either way that all makes sense to me now. Thanks everyone for all the help!</p>
</div>
<div id="comment-67167-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 13:51)</span> <span class="comment-user userinfo">Mr Davros</span>
</div>
</div>
<span id="67168"></span>
<div id="comment-67168" class="comment">
<div id="post-67168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think it is a "reserved width" but really the shop icon, i.e. the pink dot.</p>
</div>
<div id="comment-67168-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 13:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67157-form-container" class="comment-form-container">
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

