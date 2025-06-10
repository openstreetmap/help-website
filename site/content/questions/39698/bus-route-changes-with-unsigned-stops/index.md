+++
type = "question"
title = "Bus route changes with unsigned stops"
description = '''Recently a local bus route has changed (it now runs in the opposite direction from what it did formerly). However, there are no bus stop signs for the new stops, and the stops on the opposite side of the road are still signed. Obviously I can rework the route relation and remove the old stops from i...'''
date = "2014-12-18T17:41:00Z"
lastmod = "2014-12-19T22:56:00Z"
weight = 39698
keywords = [ "busstops", "busroutes" ]
aliases = [ "/questions/39698" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bus route changes with unsigned stops](/questions/39698/bus-route-changes-with-unsigned-stops)

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
<span id="post-39698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39698-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently a local bus route has changed (it now runs in the opposite direction from what it did formerly). However, there are no bus stop signs for the new stops, and the stops on the opposite side of the road are still signed.</p>
<p>Obviously I can rework the route relation and remove the old stops from it, but I'm not exactly sure about the best way to :</p>
<ol>
<li>Show the new stops</li>
<li>Mark the obviously signed stops as no longer in use</li>
</ol>
<p>I wonder if anyone has experienced a similar situation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-busroutes" rel="tag" title="see questions tagged &#39;busroutes&#39;">busroutes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '14, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-39698" class="comments-container">
&#10;</div>
<div id="comment-tools-39698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39698-form-container" class="comment-form-container">
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

<span id="39712"></span>

<div id="answer-container-39712" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39712-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I indicate which bus lines serve a stop with route_ref, so if route_ref is absent, the stop isn't served by any lines. The other indication is, of course, that the stops aren't members in any route relations. But in many cases the route relations could still be missing.</p>
<p>If I were you, I'd simply drag the stops to the other side of the street and reverse their order in the route relation. Maybe add a note on the route relation. At least for the stops which aren't served by other bus lines. For those, you can simply duplicate them with Ctrl-d.</p>
<p>Polyglot</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '14, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a7dfce5853b949d2c4d04076890b4899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Polyglot&#39;s gravatar image" />
<p><span>Polyglot</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Polyglot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39712" class="comments-container">
<span id="39726"></span>
<div id="comment-39726" class="comment">
<div id="post-39726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I prefer to do this with route relations, dragging the stops is not sensible. Firstly they have particular identifiers &amp; secondly the signage exists. It was only because I happened to pass when a bus came that I realised the route had changed. I could quite easily have waited at the signed stops (I'm sure others have).</p>
</div>
<div id="comment-39726-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 12:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="39727"></span>
<div id="comment-39727" class="comment">
<div id="post-39727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you send a link to the route relation in question? You can duplicate all the stops, then remove the identifiers from the copies and add the copies to your route relation. How to indicate that the stop poles which exist in the field are now defunct, I don't know. Here in Belgium I'd do that by clearing route_ref and possibly adding (afgeschaft) to the name.</p>
<p>I would expect that at some point in the future, they will 'replant' the poles on the other side of the street and I'd also expect them to keep the same identifiers, but it's impossible to know if they will, of course.</p>
<p>Jo</p>
</div>
<div id="comment-39727-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 14:16)</span> <span class="comment-user userinfo">Polyglot</span>
</div>
</div>
<span id="39729"></span>
<div id="comment-39729" class="comment">
<div id="post-39729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was pointed to a useful tag on IRC for bus stops: physically_present=yes/no. Thus I can add the ones as simple highway=bus_stop (either with same name as opposite or their names when they used to exist) with physically_present=no.</p>
</div>
<div id="comment-39729-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 21:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="39730"></span>
<div id="comment-39730" class="comment">
<div id="post-39730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/647/sk53">@SK53</a>: Great, I am going to map some of those in the Sahara: <code>amenity=drinking_water</code> <code>physically_present=no</code>. … oops, SCNR – those <a href="/questions/15069/is-it-normal-to-dream-of-osm-during-the-night">daydreams</a>…</p>
</div>
<div id="comment-39730-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 21:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39712-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39731"></span>

<div id="answer-container-39731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39731-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I went to Peru a few years ago, the combis were halting at fixed positions. Everybody knew that was were to go and wait for a combi. The drivers knew where to halt and the cobradores knew what stops to announce (names and all, regardless of which combi line you were on, the announced stop names were the same). Most of the time there was no physical pole present. I simply tagged them with highway=bus_stop. Today I'd add public_transport=platform/bus=yes to that and I might even add a node on the way with public_transport=stop_position/bus=yes.</p>
<p>A bus stop is where the bus stops to pick up passengers. Over here we're used to see a pole sticking out of the ground and benches and shelters and waste bins and platforms with tactile paving. In most of the rest of the world, all that is not necessary, but if a bus halts somewhere regularly to pick up passengers or let them off, it can safely be assumed to be a bus stop.</p>
<p>Now the defunct ones, that's another matter. A pole is sticking out of the ground, but no bus stops there anymore? Are they still really bus stops or simply places where flag poles happen to stick out of the ground? As far as I'm concerned, I'd leave them as long as the operator's pole is there. They might start using them once again later on. If it's only the shelter/paint on the asphalt, I'd (re)move them.</p>
<p>Cheers, Polyglot</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '14, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a7dfce5853b949d2c4d04076890b4899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Polyglot&#39;s gravatar image" />
<p><span>Polyglot</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Polyglot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39731" class="comments-container">
&#10;</div>
<div id="comment-tools-39731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39731-form-container" class="comment-form-container">
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

