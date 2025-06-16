+++
type = "question"
title = "Is it okay if a way turns at an intersection?"
description = '''I&#x27;ve come across a few single ways which someone would have to make a turn to follow. Examples (images linked to the locations):  I would have used two ways that meet where the roadways join for this single way.  I would have had one way going straight through the T-junction and another way ending a...'''
date = "2015-04-29T23:23:00Z"
lastmod = "2015-04-30T21:31:00Z"
weight = 42713
keywords = [ "geometry", "intersection", "editing", "routing", "road" ]
aliases = [ "/questions/42713" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is it okay if a way turns at an intersection?](/questions/42713/is-it-okay-if-a-way-turns-at-an-intersection)

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
<span id="post-42713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42713-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-42713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've come across a few single ways which someone would have to make a turn to follow.</p>
<p>Examples (images linked to the locations):</p>
<p><a href="https://www.openstreetmap.org/way/108893824#map=18/39.86001/-76.72910"><img src="/upfiles/fairway-court-u-turn.png" alt="Fairway Court is a residential highway. It begins at Reynolds Mill Road as a divided highway. It becomes an undivided highway just 60m in. One of the ways for Fairway Court starts at Reynolds Mill Road, makes a U-turn where the roadways join, and follows opposite roadway back." /></a></p>
<p>I would have used two ways that meet where the roadways join for this single way.</p>
<p><a href="https://www.openstreetmap.org/way/233534656#map=17/39.93420/-76.69238"><img src="/upfiles/service-road-right-turn.png" alt="A highway=service way near a strip mall turns right at a T-junction." /></a></p>
<p>I would have had one way going straight through the T-junction and another way ending at it, or, if I wanted to tag the two parts of the road that goes straight differently, I would use three ways for the two nodes, all meeting at the intersection.</p>
<p>These seem wrong to me. I'm worried that navigation systems will see these ways and think that a route that turns goes straight or vice versa. Are my fears unfounded? Should I change these to how I would have mapped them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '15, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/4b73c7299eaf4a72dea941d6a9770706?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beep21&#39;s gravatar image" />
<p><span>Beep21</span><br />
<span class="score" title="76 reputation points">76</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beep21 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '15, 00:46</strong> </span></p>
</div>
</div>
<div id="comments-container-42713" class="comments-container">
&#10;</div>
<div id="comment-tools-42713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42713-form-container" class="comment-form-container">
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

<span id="42714"></span>

<div id="answer-container-42714" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42714-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-42714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Beep21 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would say your fears are unfounded. Routing algorithms can leave a way at any intersection (shared node with other ways). And I guess that following an osm way at such an intersection is usually not cheaper/faster than doing not. Routers create their own graph of distances between locations.</p>
<p>Just try it: <span>routing with several routing engines on the osm.org homepage at the first image's location</span></p>
<p>So, you do not need to <em>change</em> this mapping. Yes, I personally, avoid to <em>create</em> such combined ways too, just because it feels strange in mind and maybe in a later detail level/mapping stage e.g. <span>turn restrictions</span> would need separate ways anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '15, 00:02</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '15, 00:05</strong> </span></p>
</div>
</div>
<div id="comments-container-42714" class="comments-container">
<span id="42722"></span>
<div id="comment-42722" class="comment">
<div id="post-42722-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This might be an extreme example, but I'd normally split the first example so if your route happened to take you along the whole of the one way section, such as <a href="http://osrm.at/c4t">http://osrm.at/c4t</a> then you would get more meaningful instructions where you need to u-turn/take a sharp left, rather than the router treating the road as one you can drive straight along.</p>
</div>
<div id="comment-42722-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 09:05)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="42724"></span>
<div id="comment-42724" class="comment">
<div id="post-42724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you sure that OSRM will give different instructions if the road is split at the u-turn? I can't believe that.</p>
</div>
<div id="comment-42724-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 09:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42760"></span>
<div id="comment-42760" class="comment">
<div id="post-42760-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See for example <a href="http://osrm.at/c55">http://osrm.at/c55</a> which are <a href="https://www.openstreetmap.org/way/200810428">separate</a> <a href="https://www.openstreetmap.org/way/200810427">roads</a>, yet OSRM doesn't tell you to perform a sharp turn. In contrast, see <a href="http://osrm.at/c57">http://osrm.at/c57</a> where the routing instructions contain a sharp turn, probably because the street <em>names</em> differ. The same applies for GraphHopper: <a href="https://graphhopper.com/maps/?point=51.03232%2C13.823006&amp;point=51.03234%2C13.822925">one</a> <a href="https://graphhopper.com/maps/?point=51.050793%2C13.776185&amp;point=51.050611%2C13.776072">two</a>.</p>
</div>
<div id="comment-42760-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 18:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42764"></span>
<div id="comment-42764" class="comment">
<div id="post-42764-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> This is on the todo list and will be improved. In general I recommend to avoid mapping for the router :)</p>
</div>
<div id="comment-42764-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 21:31)</span> <span class="comment-user userinfo">peatar</span>
</div>
</div>
</div>
<div id="comment-tools-42714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42714-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42725"></span>

<div id="answer-container-42725" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42725-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-42725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's nothing to worry about. I've occasionally mapped like in your second example. From a data aesthetics point of view, I'd shy away from the first example. But there is nothing <em>wrong</em> with this. Routers should be clever enough to know not to follow the OSM way to it's end. I'm pretty sure <em>all</em> routers convert OSM data into their own format and then route on that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '15, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-42725" class="comments-container">
<span id="42761"></span>
<div id="comment-42761" class="comment">
<div id="post-42761-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I'd shy away from mapping like in the first example not because it might confuse renderers or routers, but because it might confuse future mappers. It's quite likely that some future tags may apply to only one side of the flare (sidewalk=right, perhaps?) so joining both sections of flare seems "riskier" to me, since they aren't part of the same "long straight road".</p>
</div>
<div id="comment-42761-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 19:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="42762"></span>
<div id="comment-42762" class="comment">
<div id="post-42762-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: the same what I wrote in my "answer". Also directly mapping them separately means a more clear history later on (no split which creates one way with a new id).</p>
</div>
<div id="comment-42762-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 20:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42725-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42715"></span>

<div id="answer-container-42715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42715-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A router can decide to leave a way at any node connecting it with another way (barring restrictions preventing it like oneway, access, etc.); they don't have to travel all the way to the end nodes.</p>
<p>In your first example, the router could turn off of Reynolds Mill Road onto the southern piece of Fairway Court, then leave that way at the middle of the highlighted way to continue on the single way to the northeast. There's no need to break this way into two parts.</p>
<p>In your second example, the router could turn off of the highlighted way onto any of the parking aisles. There's no need to break this way into 18 parts.</p>
<p>Edit: Looks like aseerel4c26 beat me to saying pretty much the same thing :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '15, 00:15</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '15, 00:16</strong> </span></p>
</div>
</div>
<div id="comments-container-42715" class="comments-container">
<span id="42716"></span>
<div id="comment-42716" class="comment">
<div id="post-42716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>… indeed, get a faster keyboard! Jokes aside, you've nicely described a thought model of the router's single decisions (although this usually does not happen in really this way, if I understand usual routers correctly)!</p>
</div>
<div id="comment-42716-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 00:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42717"></span>
<div id="comment-42717" class="comment">
<div id="post-42717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was more worried about the directions missing a turn than a bad route being generated, but indeed, aseerel4c26's answer has everything I need to know, and you seeing nothing wrong with the examples either is a nice confirmation.</p>
<p>I understood that routes can leave a way at any node.—In my second example I was only concerned about the southernmost node, where the way turns right. I had no problem with all the intersections it goes straight through.</p>
</div>
<div id="comment-42717-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 00:44)</span> <span class="comment-user userinfo">Beep21</span>
</div>
</div>
<span id="42718"></span>
<div id="comment-42718" class="comment">
<div id="post-42718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10917/beep21">@Beep21</a>: as far as I know (I only remotely dived into routing software/algorithms) the OSM data is transformed into a routing graph possibly loosing all "ways". So at each intersection the turn advise has to be generated based on the angle of the connections between two nodes. Your southernmost node? Let's <span>turn "Sharp right"</span>. Did you fear that a router might say "go straight" / "follow the way"?</p>
</div>
<div id="comment-42718-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 00:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42719"></span>
<div id="comment-42719" class="comment">
<div id="post-42719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. Thanks.</p>
</div>
<div id="comment-42719-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 01:06)</span> <span class="comment-user userinfo">Beep21</span>
</div>
</div>
</div>
<div id="comment-tools-42715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42715-form-container" class="comment-form-container">
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

