+++
type = "question"
title = "Mapping a non-public gas station"
description = '''How would I map a gas station that is part of a commercial-fueling network such as CFN? These are not gas stations open to the general public; rather, they&#x27;re for truck drivers, heavy-equipment operators, and others who drive as part of their job. I don&#x27;t want to map it in a way that would cause it ...'''
date = "2016-10-14T06:53:00Z"
lastmod = "2016-10-14T07:52:00Z"
weight = 52545
keywords = [ "fuel", "non-public", "safety", "tagging" ]
aliases = [ "/questions/52545" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping a non-public gas station](/questions/52545/mapping-a-non-public-gas-station)

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
<span id="post-52545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52545-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would I map a gas station that is part of a commercial-fueling network such as <a href="https://www.cfnnet.com/">CFN</a>? These are not gas stations open to the general public; rather, they're for truck drivers, heavy-equipment operators, and others who drive as part of their job.</p>
<p>I don't want to map it in a way that would cause it to show up in a general search for gas stations. There's a safety aspect here: these stations tend to show up in the same parts of the country as "Next gas: 75 miles" signs, and someone could easily wind up stranded after planning to fuel up at one of these.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fuel" rel="tag" title="see questions tagged &#39;fuel&#39;">fuel</span> <span class="post-tag tag-link-non-public" rel="tag" title="see questions tagged &#39;non-public&#39;">non-public</span> <span class="post-tag tag-link-safety" rel="tag" title="see questions tagged &#39;safety&#39;">safety</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '16, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '16, 12:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52545" class="comments-container">
&#10;</div>
<div id="comment-tools-52545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52545-form-container" class="comment-form-container">
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

<span id="52546"></span>

<div id="answer-container-52546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52546-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-52546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a tricky issue. You can tag it as amenity=fuel and add an access=private tag to that but it will probably still show up as a normal fuel stop in many renderings and map applications.</p>
<p>We have a related problem here in Thailand where there are many tiny shops selling fuel by the bottle or pumped from a 55-gal drum. The only available tag is amenity=fuel which is used used for full-service fuel stations. I've come up with some extra tags and a special icon that cause those shops to display differently on my own custom maps but they still appear as normal fuel stations on many other maps (maps.me and OSMand). At least if you arrive at one of these shops you can still purchase enough fuel to get to the next "real" fuel stop.</p>
<p>I suppose you could add something in the name tag to distinguish those stations but that sort of thing is, rightfully I believe, frowned upon by the OSM community.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '16, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52546" class="comments-container">
&#10;</div>
<div id="comment-tools-52546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52546-form-container" class="comment-form-container">
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

