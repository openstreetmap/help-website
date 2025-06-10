+++
type = "question"
title = "highway=stop + stop=minor on intersection"
description = '''Hi helpers, I&#x27;ve recently become aware of the stop=minor tag modifier for highway=stop nodes. (Always something &quot;new&quot; to discover -- it&#x27;s been in the wiki since 2014 and has almost 25k uses, mostly in Europe and USA.) The only mention I could find in the current wiki is:  Tagging minor road stops: I...'''
date = "2019-07-28T17:40:00Z"
lastmod = "2019-08-01T07:20:00Z"
weight = 70227
keywords = [ "intersection", "stop", "highway", "minor" ]
aliases = [ "/questions/70227" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [highway=stop + stop=minor on intersection](/questions/70227/highwaystop-stopminor-on-intersection)

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
<span id="post-70227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70227-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi helpers, I've recently become aware of the <code>stop=minor</code> tag modifier for <code>highway=stop</code> nodes. (Always something "new" to discover -- it's been in the wiki since 2014 and has almost 25k uses, mostly in Europe and USA.)</p>
<p>The only mention I could find in the current wiki is:</p>
<ul>
<li><strong>Tagging minor road stops:</strong> Insert a node with tag <code>highway=stop</code> on the approach way(s) that must stop, at the stopping point. Drivers may be required to give way (yield) whether or not a physical sign is present; but if you also want to capture the signs, you can use a traffic_sign=* tag as well. In all-way stop countries you could also add <code>stop=minor</code> to distinguish 2-way from 4-way stop signs. (<a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dstop#Tagging_minor_road_stops">https://wiki.openstreetmap.org/wiki/Tag:highway:stop#Tagging minor road stops</a>)</li>
</ul>
<p>I find this text a little unclear... Regardless, the vast majority of these I've found do seem to correspond with the "you could also" suggestion: they're <code>highway=stop</code> nodes on a small road ("the approach way that must stop") near the intersection with a larger road, and so I guess the <code>stop=minor</code> tag gives a hint that perpendicular traffic on the bigger road will <em>not</em> be stopping, so cross with care.</p>
<p>But lately I've been seeing a few instances of <code>highway=stop</code> + <code>stop=minor</code> on the intersection node itself (eg <a href="https://www.openstreetmap.org/node/42468067">https://www.openstreetmap.org/node/42468067</a>). I think the intended meaning is that, because of the addition of the <code>stop=minor</code> tag, only the traffic on the smaller road should obey the <code>highway=stop</code> tag. (<a href="https://www.bing.com/maps?cp=40.580648~-73.966243&amp;dir=74&amp;style=x">Bing streetside</a> confirms no stop on the larger road.)</p>
<p>Offhand this seems like an error and I'm inclined to move these <code>highway=stop</code> tags off the intersections and onto nodes on the smaller roads. But is there something I'm not understanding here? (I've already attempted to communicate with the mapper without result.)</p>
<p>Thanks, J</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-minor" rel="tag" title="see questions tagged &#39;minor&#39;">minor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '19, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '19, 17:59</strong> </span></p>
</div>
</div>
<div id="comments-container-70227" class="comments-container">
&#10;</div>
<div id="comment-tools-70227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70227-form-container" class="comment-form-container">
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

<span id="70239"></span>

<div id="answer-container-70239" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70239-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jmapb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A <code>highway=stop</code> tag at the intersection node <em>always</em> means that his is a all-way stop. Combining <code>highway=stop</code> tag at the intersection node with <code>stop=minor</code> is clearly an error in my opinion.</p>
<p>Apart from that I'm unsure how useful the <code>stop=minor</code> tag is. When tagging a stop signs I always add a direction tag (<code>direction=forward</code> or <code>direction=backward</code>, depending on the direction of the way). This is similar to the <code>traffic_signals:direction</code> key for <code>highway=traffic_signals</code> tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '19, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70239" class="comments-container">
<span id="70255"></span>
<div id="comment-70255" class="comment">
<div id="post-70255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>IMO <code>highway=stop</code> on the intersection node should only be used for 1) all-way stops or 2) stops that can be properly described with a single <code>direction=forward/backward</code> tag. Anything more complicated than that needs to be tagged on the roads themselves, not on the intersection.</p>
<p>I agree that there's no obvious value to the <code>stop=minor</code> tag. It doesn't actually add any information and as we see it's potentially confusing. I'm guessing it must be part of a preset pulldown in one of the editors, because I can't understand why it would be so popular otherwise, especially without any clear documentation.</p>
<p>For now, I've fixed the "minor" problems that I've found... but I assume there are more I haven't found. If anyone has a handy overpass query for finding a specific tag on a road intersection, let me know! Otherwise I'll see what I can come up with.</p>
</div>
<div id="comment-70255-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 16:52)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-70239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70239-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70234"></span>

<div id="answer-container-70234" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70234-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<h1 id="background">Background</h1>
<p>It's a similar situation to traffic lights: Do we map the junction (node at intersection), or traffic control line (node on approach roadway).<br />
Problem of priority control (stop/yield) is that all-way stop/yield is not as guaranteed (traffic lights most often control all ways), and not as certain (what does a <code>highway=stop</code> without <code>stop=*</code> means? Even if it is on the intersection node, the practice of tagging all-way stops this way doesn't give much assurance)</p>
<h1 id="your-case">Your case</h1>
<blockquote>
<p>I'm inclined to move these highway=stop tags off the intersections and onto nodes on the smaller roads.</p>
</blockquote>
<p>Yes, I would do this.</p>
<blockquote>
<p>Offhand this seems like an error</p>
</blockquote>
<p>I would agree with this about the intended usage of <code>highway=stop</code>; but disagree on the paradigm of mapping stops in general, for the same reason as the current acceptance of various methods to map <code>highway=traffic_signals</code>. This should be acceptable, and further refined afterwards (that's what you are doing now).</p>
<p>There's also the no stop line exists argument for relations <a href="https://wiki.openstreetmap.org/wiki/Talk:Tag:highway%3Dstop#collection_of_notes">https://wiki.openstreetmap.org/wiki/Talk:Tag:highway%3Dstop#collection_of_notes</a> I read, that could possibility be applied to accepting the tagging scheme you found.</p>
<h1 id="personal-suggestion">Personal suggestion</h1>
<p>Mapping both the intersection, and control line (if available), is worthwhile. One shouldn't preclude the other, even in all-way stops and traffic signals. Using <code>highway=stop</code> on the intersection node for all-way stops is merely a convenience. Like <code>highway=traffic_signals</code>, if there are crosswalks or divided roadways , it could be more straightforward to map stop lines for all-way stops. Until the often brought up proposals for signal and priority control relations are confirmed, it would be the best to accept <code>stop=minor</code> on intersection nodes, but <code>highway=stop</code> in combination should be debated.</p>
<p>An idea of mine, as an example for full-fledged mapping on stop intersections marked stop lines.</p>
<p>Intersection node:</p>
<p><code>// `highway=stop` acceptable junction=* // `yes`, specifically `priority` (because priority intersections can often comprise both yield and stop control stop=* // `all`, `minor` // Add `give_way=*` if applicable (there exists all-way yields too)</code></p>
<p>Stop line node:</p>
<p><code>highway=stop stop=* // This tells users whether it is an all-way or minor road stop junction=no // inspired by `crossing=no` when handling `highway=traffic_signals`</code></p>
<p>For other cases, I haven't made up my mind for <code>priority_road</code> as I'm not familiar with it as it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '19, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '19, 22:13</strong> </span></p>
</div>
</div>
<div id="comments-container-70234" class="comments-container">
<span id="70254"></span>
<div id="comment-70254" class="comment">
<div id="post-70254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We already have the widely-supported <code>direction=*</code> tag for limiting the scope of highway=traffic_signals and highway=stop. The commonly used values of this tag certainly have their limitations (ie, there's no clear way, on an intersection, to indicate a "backward" direction for one road and a "forward" direction for another) but I don't think adding an additional <code>stop=*/traffic_signals=*</code> tag will make this situation any clearer.</p>
<p>For situations where traffic control at an intersection can't be properly described with <code>direction=*</code>, moving the stop (or signal) nodes to the approach ways is the only currently viable solution IMO. The way I see it, in fact, tagging the stop on the intersection itself is a "shortcut" that should only be used in unambiguous situations (either all-way stops or those that can be properly described with a single <code>direction=*</code> tag.)</p>
<p>I can see the appeal of relations, because they would allow the intersection to be described in great detail. But they're harder to tag and maintain and I don't think they're worth the complication.</p>
</div>
<div id="comment-70254-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 16:37)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="70256"></span>
<div id="comment-70256" class="comment">
<div id="post-70256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Personally I would also put <code>highway=stop</code> node where a stop line should exist (relations aren't something I would fancy here). What I'm suggesting is to show whether the stop is all-way or minor road only to users. Tagging it explicitly by <code>stop=*</code> would save some trouble and provide more information easily.</p>
<p>The <code>junction=*</code> part is primary grounded in signalized junctions (evaluating number of traffic lights, identifying controlled points to replace <code>highway=traffic_signals</code> at intersection nodes, etc). Either way concerning the former, priority junctions deserves to be tagged even more to caution the uninterrupted major road of priority on mergings (as opposed to zipper merge, or lane adds that needs more detailed/micro <code>lanes</code> tagging).</p>
</div>
<div id="comment-70256-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 17:04)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="70258"></span>
<div id="comment-70258" class="comment">
<div id="post-70258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Truth is I can't quite see the need for the junction tag and exactly how it would function, and these comment boxes, with their limited functionality, probably aren't the best place to clarify it. Using the wiki talk page is also a little awkward. Maybe try discussing on the tagging mailing list and/or writing up a diary entry on osm.org with example pictures for the various situations you're trying to cover.</p>
</div>
<div id="comment-70258-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 18:23)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="70260"></span>
<div id="comment-70260" class="comment">
<div id="post-70260-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>One thing I believe strongly, though, is that there shouldn't be a highway=stop node on an intersection if not all roads passing through that intersection have to stop there. I consider this "troll tagging", ie, what the main tag gives the subtag stop=minor takes away, which is a problem for any data consumers that aren't specifically looking for that tag. In a sense we already have troll tagging on highway=stop nodes via the direction=* tag, but that's in common use and people know to look for it. Attempting to use an additional troll tag with possibly contradictory information will be problematic.</p>
<p>If this scenario ("this road doesn't have to stop at this intersection but the other road does") is important enough that it needs to be explicitly tagged on the intersection itself (rather than be deduced from the tagging on the other road -- a data consumer can always follow the highway graph and find all this information from the connections if the stop node is there on the minor road) then a different tag would be needed. You might want to propose something like highway=minor_stop that will not interfere with existing software designed around the existing tagging scheme.</p>
</div>
<div id="comment-70260-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 18:29)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="70273"></span>
<div id="comment-70273" class="comment">
<div id="post-70273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm still new to OSM so I don't think it's best to be too formal and certain about my opinion yet. I saw <code>stop=*</code> being documented on wiki. I agree with <code>highway=stop</code> at minor stop intersection being essentially wrong, that's why I thought about <code>junction=*</code> as a better option for initial work and other cases. That being said, such incorrect tagging still needs to be detected and fixed.</p>
<p>I forgot to mention one reason is I encountered some priority junction having lane-based restriction on merging, prompting me to look at something that needs to support more complicated schemes like <code>stop:lanes=no|all</code>. Another potential use (I still need to look at international examples) is on roundabouts without physically segregated slip lanes (eg <code>give_way:lanes=no|minor|minor</code>).</p>
<p>I'm trying to see if there's a way to make use of existing tags the most (with backward comparability of course) as I don't want to propose new keys and values like <code>highway=minor_stop</code> unnecessarily.</p>
</div>
<div id="comment-70273-info" class="comment-info">
<span class="comment-age">(01 Aug '19, 07:20)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-70234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70234-form-container" class="comment-form-container">
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

