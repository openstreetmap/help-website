+++
type = "question"
title = "Disused cable car is not rendered"
description = '''When prefixing aerialway=cable_car to disused:aerialway=cable_car it disappears from map rendering.  It is still present as a landmark, though, and should be rendered, in my opinion. Is this wrong tagging? Concerns Goldeck Pendelbahn, which stopped operating two years ago, but still exists.'''
date = "2020-09-21T16:17:00Z"
lastmod = "2020-09-23T14:31:00Z"
weight = 76745
keywords = [ "rendering", "disused" ]
aliases = [ "/questions/76745" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Disused cable car is not rendered](/questions/76745/disused-cable-car-is-not-rendered)

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
<span id="post-76745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76745-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When prefixing <code>aerialway=cable_car</code> to <code>disused:aerialway=cable_car</code> it disappears from map rendering.</p>
<p>It is still present as a landmark, though, and should be rendered, in my opinion. Is this wrong tagging?</p>
<p>Concerns <a href="https://www.openstreetmap.org/way/26422590">Goldeck Pendelbahn</a>, which stopped operating two years ago, but still exists.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-disused" rel="tag" title="see questions tagged &#39;disused&#39;">disused</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '20, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ff48105adb7b702391f6f562ae250d0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecuapac&#39;s gravatar image" />
<p><span>ecuapac</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecuapac has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76745" class="comments-container">
&#10;</div>
<div id="comment-tools-76745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76745-form-container" class="comment-form-container">
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

<span id="76786"></span>

<div id="answer-container-76786" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76786-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is probably a rare case where amenity=* + disused=yes is appropriate rather than then the use of a lifecycle prefix. To a certain extent it depends on what use-cases might be anticipated: is the presence of an aerial cableway important for routing, or is it a significant landmark? This is always an issue when a tag relates to two concepts: in this case a transport facility and a physical structure. Also would the casual passer-by be aware that it was disused. If the cable and cabins are still visible (depending on whether the cabins are detachable) then it is perfectly possible to not be aware that it is not in service.</p>
<p>Disused lifecycle tagging does cover a range of scenarios: for instance with cableway it might cover any of the following scenarios:</p>
<ul>
<li>The cableway has reached the end of its service life and is not being maintained prior to planned demolition.</li>
<li>The cableway is out-of-service because of financial problems with it's operator (this scenario affected me when I planned to use the Lungern-Turren-Bahn in 2001 : the operator has just gone bankrupt).</li>
<li>The cableway is out-of-service because it has failed safety tests, but it is anticipated that it will be restored. (Or, perhaps, as in a recent case at Squamish, the cableway was vandalised).</li>
<li>No traces of the cableway are obvious anymore (someone set the tag to disused:amenity, but it wasnt updated).</li>
</ul>
<p>Some infrastructure often exists long after a cableway has been demolished: for instance the top stations at Punta Indren (<a href="https://www.openstreetmap.org/way/149862631),">https://www.openstreetmap.org/way/149862631),</a> Furggen (<a href="https://www.openstreetmap.org/way/129217279),">https://www.openstreetmap.org/way/129217279),</a> and Fil de Cassons/Cassongrat (<a href="https://www.openstreetmap.org/way/232100249).">https://www.openstreetmap.org/way/232100249).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '20, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76786" class="comments-container">
&#10;</div>
<div id="comment-tools-76786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76786-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76753"></span>

<div id="answer-container-76753" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76753-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using the <code>disused:</code> prefix is the correct way of tagging. The problem here is that we do not differ between mapping the function and the physical infrastructure. For a closed supermarket you would still have a <code>building=yes</code> together with the <code>disused:shop=supermarket</code>.</p>
<p>Of the physical infrastructure you can map the pylons <a href="https://wiki.openstreetmap.org/wiki/Tag%3Aaerialway%3Dpylon"><code>aerialway=pylon</code></a> as has been done for this cable car. However on a quick search I couldn't find a map that displays them.</p>
<p>It should be up to the map renderers to consider placing a <code>disused:aerialway</code> on the map. <a href="https://openskimap.org/#13.19/46.7742/13.47399">Openskimap</a> is apparently doing so as a dotted line.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '20, 07:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76753" class="comments-container">
<span id="76754"></span>
<div id="comment-76754" class="comment">
<div id="post-76754-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a good question whether such a cableway pylon should still be <code>aerialway=pylon</code>. Changing to a non-purpose, structural <code>disused:aerialway=pylon</code> + <code>man_made=</code> <code>=tower</code>/<code>=mast</code> (a potential issue here is <code>aerialway=pylon</code> doesn't distinguish between structures as small as chairlifts to the biggest ones) may better reflect its status. Thinking about rendering can yet deepen the understanding on proper tagging.</p>
</div>
<div id="comment-76754-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 08:10)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-76753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76753-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76756"></span>

<div id="answer-container-76756" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76756-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option could be just adding disused=yes tag, which is also clear, but does not change rendering - see: <a href="https://wiki.openstreetmap.org/wiki/Key:disused">https://wiki.openstreetmap.org/wiki/Key:disused</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '20, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-76756" class="comments-container">
<span id="76757"></span>
<div id="comment-76757" class="comment">
<div id="post-76757-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>While adding "disused=yes" can be problematic (for example if an object had two main tags in OSM - which function is now disused?), in a case where something is "still obviously a thing" it might be appropriate - I believe I've used it on canals that are still full of water but no longer have traffic on them, for example.</p>
</div>
<div id="comment-76757-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 12:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="76772"></span>
<div id="comment-76772" class="comment">
<div id="post-76772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>access=no</code> would work in this case, too.</p>
</div>
<div id="comment-76772-info" class="comment-info">
<span class="comment-age">(22 Sep '20, 20:27)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="76779"></span>
<div id="comment-76779" class="comment">
<div id="post-76779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5/richard"></a><a href="https://help.openstreetmap.org/users/5/richard">@Richard</a> While correct on routing, I wonder if <code>access=no</code> + <code>disused=yes</code> would be confusing, as if the gondola vehicles themselves still remain there to be revived in the future. <code>abandoned=yes</code> may be clearer.</p>
</div>
<div id="comment-76779-info" class="comment-info">
<span class="comment-age">(23 Sep '20, 09:50)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-76756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76756-form-container" class="comment-form-container">
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

