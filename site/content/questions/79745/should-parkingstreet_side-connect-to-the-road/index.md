+++
type = "question"
title = "Should parking=street_side connect to the road?"
description = '''There are some street side parking spaces mapped by a particular user like this:  These small service roads don&#x27;t really exist, but are used to fill the gap between a road mapped as a way without an area and a street side parking space. How do I go about correcting this? I see following options:  pa...'''
date = "2021-04-19T18:41:00Z"
lastmod = "2022-01-21T12:18:00Z"
weight = 79745
keywords = [ "editing", "tagging", "road", "parking" ]
aliases = [ "/questions/79745" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Should parking=street_side connect to the road?](/questions/79745/should-parkingstreet_side-connect-to-the-road)

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
<span id="post-79745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79745-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are some street side parking spaces mapped by a particular user like this: <img src="https://help.openstreetmap.org/upfiles/original_O2vi3Fd.PNG" alt="alt text" /></p>
<p>These small service roads don't really exist, but are used to fill the gap between a road mapped as a way without an area and a street side parking space.</p>
<p>How do I go about correcting this? I see following options:</p>
<ol>
<li>parking:lane could be used, but I don't want to remove details added by other mapper.</li>
<li><p>Tag:parking=street_side wiki article has a picture where street side parking space is not connected to the road at all. But imagine two parallel roads with parking spaces in between. There is no way of knowing from which road they are accessible. And shouldn't we try to connect all infrastructure, which is actually connected? <img src="https://wiki.openstreetmap.org/w/images/0/06/Street_side_parking_carto_rendering.png" alt="alt text" /></p></li>
<li><p>I could connect street-side parking directly to the road, so that it would share one side with the road. But I don't actually know if this is acceptable. <img src="https://help.openstreetmap.org/upfiles/variant1_oGefjMw.png" alt="alt text" /></p></li>
<li>Maybe I'm wrong and the fake service ways are actually acceptable.</li>
</ol>
<p>Personally, I think that option 3 is better, but since option 2 is mentioned in wiki, is it the only acceptable option?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '21, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/b5b23f132c989f20ec4286a6aedc5d55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qqqqqqqqqqqqqqqqqqqq&#39;s gravatar image" />
<p><span>qqqqqqqqqqqq...</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qqqqqqqqqqqqqqqqqqqq has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '21, 20:51</strong> </span></p>
</div>
</div>
<div id="comments-container-79745" class="comments-container">
<span id="79747"></span>
<div id="comment-79747" class="comment">
<div id="post-79747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I only just learned about this tag today. I'm not really sure of the "right" way to represent the connectivity for these.</p>
<p>That being said, I would argue that option 3 is objectively "wrong". If the parking was connected to the highway way like in your example image, it would semantically be saying that the parking extends out to the centerline of the highway, which wouldn't reflect reality.</p>
</div>
<div id="comment-79747-info" class="comment-info">
<span class="comment-age">(19 Apr '21, 19:32)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="79751"></span>
<div id="comment-79751" class="comment">
<div id="post-79751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In reality roads aren't narrow lines either, but we accept them as a such simplified representation on maps. In my personal opinion, maps are always a simplified version of reality. For me, this would be mean that the parking spaces extend UNTIL the road, not it's CENTERLINE.</p>
<p>As another example, imagine a paved road to which connects a dirt road. The dirt road would connect as you say to centerline, but near the connection point in reality it would be a paved surface, which won't be represented on a map.</p>
<p>This is why I feel like the option 3 is better, but thank you for your opinion anyway, that's why I'm asking.</p>
</div>
<div id="comment-79751-info" class="comment-info">
<span class="comment-age">(19 Apr '21, 20:48)</span> <span class="comment-user userinfo">qqqqqqqqqqqq...</span>
</div>
</div>
</div>
<div id="comment-tools-79745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79745-form-container" class="comment-form-container">
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

<span id="79760"></span>

<div id="answer-container-79760" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79760-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-79760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would just leave them as standalone parking (option 2). Most routing software will span a gap of a few metres for routing purposes, all the other approaches involve mapping spurious things that aren't there: there are no service roads for access, the parking does not span to the road centre-line. Option 1 is often the best because it fits better with OSM's centre-line data model, but I agree with you about removing detail.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '21, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-79760" class="comments-container">
<span id="79770"></span>
<div id="comment-79770" class="comment">
<div id="post-79770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The small service roads feel definitely wrong. When you change them you could leave a comment in the change set that created those pointing to the wiki.</p>
</div>
<div id="comment-79770-info" class="comment-info">
<span class="comment-age">(20 Apr '21, 20:17)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="83141"></span>
<div id="comment-83141" class="comment">
<div id="post-83141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If this is indeed the "correct" answer, software like Vespucci (which internally uses Osmosis to find issues) needs to stop complaining about unconnected parking lots, because that's where people (including myself) get the idea to insert those fake service roads in the first place.</p>
</div>
<div id="comment-83141-info" class="comment-info">
<span class="comment-age">(21 Jan '22, 12:18)</span> <span class="comment-user userinfo">smheidrich</span>
</div>
</div>
</div>
<div id="comment-tools-79760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79760-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79773"></span>

<div id="answer-container-79773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79773-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-79773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Parking without roads connected to it either seems inaccessible or not completely mapped.For fine detail parking mapping, if imagery is good enough, I use gridify plugin to convert to individual parking spaces. I link them and the general area all into a relation. Either way, I extend the area to reach the road and not go beyond unless there is more parking on its other side. I connect it to the road when the road is an edge/point of the now defined area. For the first image, I'd drag those diagonal edges out toward the road at the same angle which results in being able to see the parking flow even without all parking spaces mapped nor does it require one-way to be mapped/correct to see through such omissions/errors. 'if' I separated the 5 from the main area, id still extend it to the road as I did with the little block just south of it.https://www.openstreetmap.org/#map=19/33.64299/-112.22476 shows one example of how that can turn out for how it works and how it gets awkward. I lose consistency just to the right of 'arrowhead towne center transit center' with the long extension to the 5 spots to its right and they reach beyond the road and back up to the above area where the majority of parking reaches down to it. I also chose to divide the larger area into two separate areas which gets into a micromapping thing and I do have them linked into the same relation. Not sure why the tile renders at best zoom with two 'p' symbols for the bigger left half. I could find other big/small examples if desired though I didn't know what the community even thinks of this work. The thought that the road/serviceway doesn't extend into the parking...does for most spots I have mapped; asphalt continued to flow from being a road to being a parking spot without any barrier. I guess if a dispute came up then you could start mapping each driveway into each spot. I guess we could also make the area connecting between be area=parking-way or some fun.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '21, 02:59</strong></p>
<img src="https://secure.gravatar.com/avatar/11863de191822fdbf4429e56a4323366?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mirror176&#39;s gravatar image" />
<p><span>mirror176</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mirror176 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79773" class="comments-container">
<span id="79789"></span>
<div id="comment-79789" class="comment">
<div id="post-79789-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What are suggesting in short is: make the parking connected to the road, but map parking spaces with amenity:parking_space, if I understood you correctly.</p>
<p>When the road isn't wide it may look good, but if the road has many lanes and the centerline if far from the road egde, then the parking will extend very far into the road. I feel like both option 2 and option 3 are not ideal now and have flaws.</p>
</div>
<div id="comment-79789-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 11:49)</span> <span class="comment-user userinfo">qqqqqqqqqqqq...</span>
</div>
</div>
<span id="79791"></span>
<div id="comment-79791" class="comment">
<div id="post-79791-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16568/mirror176">@mirror176</a>: this seems hugely complicated to say "here are 5 parking spaces at the side of the road". We should keep OSM simple enough that anyone can quickly add such information</p>
</div>
<div id="comment-79791-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 13:16)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79773-form-container" class="comment-form-container">
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

