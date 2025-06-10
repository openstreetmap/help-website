+++
type = "question"
title = "[closed] Adding Custom tags to geocode in Nominatim"
description = '''Has anyone ever tried/accomplished adding custom tags into nominatim to geocode against? Basically what I would like to accomplish is to be able to geocode store id #s with nominatim, for instance, retail stores have unique identifying numbers for their particular store.  I would like to be able to,...'''
date = "2014-09-04T13:46:00Z"
lastmod = "2014-10-07T15:15:00Z"
weight = 36592
keywords = [ "custom", "all", "nominatim", "geocoding", "tags" ]
aliases = [ "/questions/36592" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Adding Custom tags to geocode in Nominatim](/questions/36592/adding-custom-tags-to-geocode-in-nominatim)

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
<span id="post-36592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36592-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Has anyone ever tried/accomplished adding custom tags into nominatim to geocode against?</p>
<p>Basically what I would like to accomplish is to be able to geocode store id #s with nominatim, for instance, retail stores have unique identifying numbers for their particular store.</p>
<p>I would like to be able to, for example, be able to add these tags under a custom tag store_id:123456 with something like the iD environment and then ingest that data into Nominatim to geocode against those custom store_id values.</p>
<p>Any suggestions? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-all" rel="tag" title="see questions tagged &#39;all&#39;">all</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '14, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b0cbb590dcfa387d76ad86beef6b49ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="olearytd12&#39;s gravatar image" />
<p><span>olearytd12</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="olearytd12 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>21 Oct '14, 19:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36592" class="comments-container">
&#10;</div>
<div id="comment-tools-36592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36592-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is self-answered (accepting own answers would not work here on this site) → closed" by aseerel4c26 21 Oct '14, 19:47

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37387"></span>

<div id="answer-container-37387" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37387-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up figuring this out myself, if anyone else is interested.</p>
<p>You can accomplish this by editing the output-gazetteer.c file in the osm2pgsql/ directory at the root of Nominatim. Add the custom "key" tag with the other name tags that are imported to the Nominatim database during ingest and you will have to rebuild Nominatim to pick up your changes to the gazetteer file.</p>
<p>Ingest your data that holds your custom key:value and you should be able to geocode that feature now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '14, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/b0cbb590dcfa387d76ad86beef6b49ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="olearytd12&#39;s gravatar image" />
<p><span>olearytd12</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="olearytd12 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37387" class="comments-container">
&#10;</div>
<div id="comment-tools-37387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37387-form-container" class="comment-form-container">
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

