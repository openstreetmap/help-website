+++
type = "question"
title = "How should I tag craft breweries with tasting rooms?"
description = '''I have reviewed all of the brewery-related wiki pages and have found that craft breweries with tasting rooms are tagged very inconsistently around Vancouver and British Columbia. These establishments are full-on breweries (i.e. industrial sites) but have a built-in tasting room where customers can c...'''
date = "2018-05-31T01:39:00Z"
lastmod = "2018-06-03T19:40:00Z"
weight = 63899
keywords = [ "breweries", "tagging" ]
aliases = [ "/questions/63899" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How should I tag craft breweries with tasting rooms?](/questions/63899/how-should-i-tag-craft-breweries-with-tasting-rooms)

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
<span id="post-63899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63899-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have reviewed all of the <a href="https://wiki.openstreetmap.org/wiki/Brewery">brewery-related wiki pages</a> and have found that craft breweries with tasting rooms are <a href="https://wiki.openstreetmap.org/wiki/BC_Craft_Breweries#Currently_in_OSM">tagged very inconsistently around Vancouver and British Columbia</a>.</p>
<p>These establishments are full-on breweries (i.e. industrial sites) but have a built-in tasting room where customers can come sample their beers and buy some to take home with them.</p>
<p>I would like to switch to more consistent tagging, but I'm not sure exactly what the best tags are:</p>
<ul>
<li><p>How should I tag a brewery with a tasting room but only token food options like chips and pretzels? <code>amenity=bar</code>, <code>microbrewery=yes</code> and <code>craft=brewery</code>?</p></li>
<li><p>How should I tag a brewery with a tasting room and significant food options? <code>amenity=pub</code>, <code>microbrewery=yes</code> and <code>craft=brewery</code>?</p></li>
<li><p>Should I also add <code>shop=alcohol</code> to all of them since they offer they sell their own beers (either in bottles/cans or reuseable containers)?</p></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-breweries" rel="tag" title="see questions tagged &#39;breweries&#39;">breweries</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '18, 01:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0110e86fdb31486c22dd381326d99de9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fmarier&#39;s gravatar image" />
<p><span>fmarier</span><br />
<span class="score" title="211 reputation points">211</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fmarier has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-63899" class="comments-container">
&#10;</div>
<div id="comment-tools-63899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63899-form-container" class="comment-form-container">
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

<span id="63944"></span>

<div id="answer-container-63944" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63944-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fmarier has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the whole building belongs to the brewery, I'd tag the building with <code>craft=brewery</code> (or <code>industrial=brewery</code> for large scale operations) and put a node inside for the tasting room, <code>amenity=bar/pub/restaurant</code> etc, depending on the feel of the place. For a smaller brewing outfit I'd probably just add <code>craft=brewery</code> to the amenity.</p>
<p>Indicate food options with <code>cuisine=snack/pub/burger</code> etc.</p>
<p>I don't see any problem with adding <code>shop=alcohol</code> directly to the amenity node, but there might be reasons to make it its own node: If it's physically separated, has different hours, name, selection (ie you can buy liquor at the pub but only beer to go), payment options, etc.</p>
<p>As I understand it, <code>microbrewery=yes</code> is for establishments that are primarily amenities but include a small brewing operation onsite, while <code>craft=brewery</code> is for businesses that are primarily breweries, though they often include tasting rooms. Sometimes it's a blurry distinction.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '18, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-63944" class="comments-container">
&#10;</div>
<div id="comment-tools-63944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63944-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63906"></span>

<div id="answer-container-63906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63906-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd suggest as separate features for the brewery and bar. See <a href="https://map.atownsend.org.uk/maps/map/map.html#zoom=18&amp;lat=53.27676&amp;lon=-0.793414">here</a> for an example (which is <a href="https://www.openstreetmap.org/way/359616375">here</a> in OSM). I wouldn't worry about what does or does not get rendered in OSM's "Standard" map - that lags behind in a number of areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '18, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63906" class="comments-container">
<span id="63933"></span>
<div id="comment-63933" class="comment">
<div id="post-63933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The example you gave looks a lot like Red Truck: a brewery and an adjoining pub in two separate buildings (or sets of buildings). Unfortunately, that's the exception in Vancouver. Most craft breweries here have their tasting room and beer store in the same building as the brew tanks. In fact, in the case of Storm, you even have to walk on spilled beer in between fermenters in order to get to the counter where you can get your container filled (i.e. the beer store). Is there any downside to tagging a single way / node with three different things (<code>craft=brewery</code>, <code>amenity=bar</code> and <code>shop=alcohol</code>)? Will renderers be smart enough to have one of these take precendence? Does one of these uses need to be flagged as "primary" somehow?</p>
</div>
<div id="comment-63933-info" class="comment-info">
<span class="comment-age">(01 Jun '18, 05:01)</span> <span class="comment-user userinfo">fmarier</span>
</div>
</div>
<span id="63935"></span>
<div id="comment-63935" class="comment">
<div id="post-63935-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See <a href="https://www.openstreetmap.org/way/221456768">this example</a> for a large "craft=brewery" building with a pub node inside it, maybe that is more what you're looking for?</p>
<p>That approach has been used for ages with post offices inside shops and should work here too. A pedant might complain that actually the brewery only takes up the left-hand side of the building (there are railings that separate the "bar" part from the "brewery" part so that you don't get run over by a fork-lift). About the only one I can think of without that separation is <a href="https://www.openstreetmap.org/node/3676981225">here</a>.</p>
</div>
<div id="comment-63935-info" class="comment-info">
<span class="comment-age">(01 Jun '18, 09:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63986"></span>
<div id="comment-63986" class="comment">
<div id="post-63986-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, the post-office-within-a-shop comparison is very useful. I'll try to do that for the breweries I have surveyed.</p>
</div>
<div id="comment-63986-info" class="comment-info">
<span class="comment-age">(03 Jun '18, 19:40)</span> <span class="comment-user userinfo">fmarier</span>
</div>
</div>
</div>
<div id="comment-tools-63906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63906-form-container" class="comment-form-container">
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

