+++
type = "question"
title = "can I get photos of places on the map using rest API"
description = '''can I download or get a link to photos of places (monuments, buildings, etc.) received by rest request having in my order go places'''
date = "2019-12-16T20:58:00Z"
lastmod = "2019-12-17T12:20:00Z"
weight = 72126
keywords = [ "photos", "rest" ]
aliases = [ "/questions/72126" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [can I get photos of places on the map using rest API](/questions/72126/can-i-get-photos-of-places-on-the-map-using-rest-api)

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
<span id="post-72126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72126-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>can I download or get a link to photos of places (monuments, buildings, etc.) received by rest request having in my order go places</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-photos" rel="tag" title="see questions tagged &#39;photos&#39;">photos</span> <span class="post-tag tag-link-rest" rel="tag" title="see questions tagged &#39;rest&#39;">rest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '19, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9052f33aa50d0009708c373fc6e1ad59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jailbot666&#39;s gravatar image" />
<p><span>jailbot666</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jailbot666 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72126" class="comments-container">
<span id="72128"></span>
<div id="comment-72128" class="comment">
<div id="post-72128-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>What service are you referring to? OpenStreetMap itself does not store any photos.</p>
</div>
<div id="comment-72128-info" class="comment-info">
<span class="comment-age">(16 Dec '19, 21:24)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72130"></span>
<div id="comment-72130" class="comment">
<div id="post-72130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but, some places on the map have image tags, with links, for example mappilary. I wanted to know if it is possible to pull these tags?</p>
</div>
<div id="comment-72130-info" class="comment-info">
<span class="comment-age">(17 Dec '19, 08:02)</span> <span class="comment-user userinfo">jailbot666</span>
</div>
</div>
</div>
<div id="comment-tools-72126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72126-form-container" class="comment-form-container">
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

<span id="72135"></span>

<div id="answer-container-72135" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72135-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jailbot666 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Example of a place with image tag <a href="https://www.openstreetmap.org/node/6286421825">https://www.openstreetmap.org/node/6286421825</a> Documentation of possible image tags <a href="https://wiki.openstreetmap.org/wiki/Key:image">https://wiki.openstreetmap.org/wiki/Key:image</a></p>
<p>There isn't a REST or other API for those. You'd have to build it yourself. Basically download a copy of the <a href="https://planet.openstreetmap.org/">https://planet.openstreetmap.org/</a> or regional extract (explained on the same page) and using tools like <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a> and some programming to extract the data you need.</p>
<p>Note mapillary has license terms. If you effectively build a mapillary image browser (and thus request images from their servers) you might have to pay. That's my reading of their terms, I'm not an expert and this is not legal advise.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '19, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72135" class="comments-container">
<span id="72136"></span>
<div id="comment-72136" class="comment">
<div id="post-72136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, thx. you help me</p>
</div>
<div id="comment-72136-info" class="comment-info">
<span class="comment-age">(17 Dec '19, 12:20)</span> <span class="comment-user userinfo">jailbot666</span>
</div>
</div>
</div>
<div id="comment-tools-72135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72135-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72127"></span>

<div id="answer-container-72127" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72127-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That doesn't sound like the sort of thing that OpenStreetMap itself does, although someone might have created a photo-sharng service that uses OSM data to either display a map background or translating locations (latitude and longitude) to the name of a nearby place.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '19, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72127" class="comments-container">
<span id="72132"></span>
<div id="comment-72132" class="comment">
<div id="post-72132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tags such as picture, mappilary are described on the wiki. but it’s not clear how to use it</p>
</div>
<div id="comment-72132-info" class="comment-info">
<span class="comment-age">(17 Dec '19, 08:40)</span> <span class="comment-user userinfo">jailbot666</span>
</div>
</div>
</div>
<div id="comment-tools-72127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72127-form-container" class="comment-form-container">
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

