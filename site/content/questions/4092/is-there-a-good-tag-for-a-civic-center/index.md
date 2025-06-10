+++
type = "question"
title = "Is there a good tag for a civic center?"
description = '''There is a city block that&#x27;s known locally as the &quot;civic center&#x27;. It contains a city hall, sheriff&#x27;s station and miscellaneous government services. I want this civic center to stand out on the map. I did not find landuse=government and I am not sure if office=government is appropriate when tagging a...'''
date = "2011-03-25T19:01:00Z"
lastmod = "2011-04-06T05:03:00Z"
weight = 4092
keywords = [ "tagging", "government" ]
aliases = [ "/questions/4092" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a good tag for a civic center?](/questions/4092/is-there-a-good-tag-for-a-civic-center)

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
<span id="post-4092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4092-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a city block that's known locally as the "civic center'. It contains a city hall, sheriff's station and miscellaneous government services. I want this civic center to stand out on the map. I did not find landuse=government and I am not sure if office=government is appropriate when tagging a whole block. Is there an accepted solution?</p>
<p>There is an abandoned proposal for tagging civic centres/centers with amenity=local_government. But is it a good idea to adopt something that dies in the wiki?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-government" rel="tag" title="see questions tagged &#39;government&#39;">government</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '11, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4092" class="comments-container">
&#10;</div>
<div id="comment-tools-4092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4092-form-container" class="comment-form-container">
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

<span id="4094"></span>

<div id="answer-container-4094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4094-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My, fairly pragmatic, approach would be to use the following pretty widely used tags:</p>
<ul>
<li><a href="http://wiki.openstreetmap.org/wiki/Tag:landuse%3Dcommercial">landuse=commercial</a> for the area of the block, adding name=Civic Center.</li>
<li>map the building outlines building=yes or building=office (or indeed anything else which suits).</li>
<li>add nodes for the principal POIs such as <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtownhall">amenity=town_hall</a>. If these are in specific building they can be attached to the areas.</li>
<li>add appropriate operator=* tags.</li>
</ul>
<p>Combined together these different tags should be adequate both for plain rendered maps and apps which might want to consume the tags directly.</p>
<p>There are a small number of landuse=government tags (55 at the time of writing), but the range of activities of government bodies does not make this a very useful tag, whereas identifying the operator or owner of the land as such provides the same information without compromising more specific uses of the landuse tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '11, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4094" class="comments-container">
<span id="4111"></span>
<div id="comment-4111" class="comment">
<div id="post-4111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am intrigued. My first reaction was: "Commercial???" As I read on, it started making sense. I guess as long as visually it does not look like the shopping plaza next door, I am good with it. Testing to see what Mapnik will do with it.</p>
<p>Thanks!</p>
</div>
<div id="comment-4111-info" class="comment-info">
<span class="comment-age">(25 Mar '11, 21:30)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4112"></span>
<div id="comment-4112" class="comment">
<div id="post-4112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, my attitude is that these are basically offices &amp; I don't get too hung-up about whether they belong to for-profit, not-for-profit business, local govt, national govt. It's realistic as my local council has just taken over a building which used to a bank back-office.</p>
</div>
<div id="comment-4112-info" class="comment-info">
<span class="comment-age">(25 Mar '11, 21:50)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="4131"></span>
<div id="comment-4131" class="comment">
<div id="post-4131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While I agree that at the moment there is not yet a well established method to tag public administration and services in greater detail (there is amenity=public_building to mention), in the future this will most probably change. We should employ some time in finding a solution.</p>
</div>
<div id="comment-4131-info" class="comment-info">
<span class="comment-age">(26 Mar '11, 11:14)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="4289"></span>
<div id="comment-4289" class="comment">
<div id="post-4289-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In reviewing my city's zoning maps (official stuff), I realized that we left out a pretty basic land use type, namely landuse=institutional. It covers schools, government, etc. It would have been perfect for my civic center. I added a note to the landuse key discussion page on wiki, not sure what's next.</p>
</div>
<div id="comment-4289-info" class="comment-info">
<span class="comment-age">(06 Apr '11, 05:03)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4094-form-container" class="comment-form-container">
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

