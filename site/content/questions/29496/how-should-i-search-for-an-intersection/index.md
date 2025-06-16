+++
type = "question"
title = "How should I search for an intersection?"
description = '''What&#x27;s the best way to search for/geocode the intersection of two roads? EDIT: I am asking for a user-facing tool, like MapQuest Open or Nominatim.'''
date = "2014-01-01T06:25:00Z"
lastmod = "2014-01-01T22:07:00Z"
weight = 29496
keywords = [ "search", "intersection", "geocoding" ]
aliases = [ "/questions/29496" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How should I search for an intersection?](/questions/29496/how-should-i-search-for-an-intersection)

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
<span id="post-29496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29496-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What's the best way to search for/geocode the intersection of two roads?</p>
<p>EDIT: I am asking for a user-facing tool, like MapQuest Open or Nominatim.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jan '14, 06:25</strong></p>
<img src="https://secure.gravatar.com/avatar/e72946d7c81ee170b322f6e6abae3442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattflaschen&#39;s gravatar image" />
<p><span>mattflaschen</span><br />
<span class="score" title="226 reputation points">226</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattflaschen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jan '14, 22:02</strong> </span></p>
</div>
</div>
<div id="comments-container-29496" class="comments-container">
<span id="29518"></span>
<div id="comment-29518" class="comment">
<div id="post-29518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This should be possible using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> and the <em>around</em> keyword with a radius of 0. However I'm not skilled enough with the Overpass API to show you an example query. The <a href="https://wiki.openstreetmap.org/wiki/Maxheight_Map">maxheight map</a> uses a similar mechanism and especially detects roads crossing each other without sharing nodes.</p>
</div>
<div id="comment-29518-info" class="comment-info">
<span class="comment-age">(01 Jan '14, 22:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29496-form-container" class="comment-form-container">
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

<span id="29497"></span>

<div id="answer-container-29497" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29497-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mattflaschen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure if it's the best way, but AFAIK a common solution is:</p>
<ul>
<li>grab all way segments for road name A</li>
<li>grab all way segments for road named B</li>
<li>compare both list of nodes</li>
<li>return equal nodes</li>
</ul>
<p>Please keep in mind, that this <strong>isn't robust</strong> against 'dirty' OSM tagging. Here roads can be splitted in very creative ways, intersections don't have to contain traffic lights (at the expected positions), ... In the end a appropriate solution depends on the requirements of your usecase.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '14, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-29497" class="comments-container">
<span id="29501"></span>
<div id="comment-29501" class="comment">
<div id="post-29501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Er, would you care to elaborate about how to "compare both lists of nodes and return equal nodes"?</p>
</div>
<div id="comment-29501-info" class="comment-info">
<span class="comment-age">(01 Jan '14, 12:51)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="29503"></span>
<div id="comment-29503" class="comment">
<div id="post-29503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You generate a <a href="https://wiki.openstreetmap.org/wiki/Way#Street_as_a_vector">list of node IDs</a> per way segment and add them to a collection per Road. After that you compare the ID collections and select that nodes that are in both road collections.</p>
</div>
<div id="comment-29503-info" class="comment-info">
<span class="comment-age">(01 Jan '14, 13:01)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29505"></span>
<div id="comment-29505" class="comment">
<div id="post-29505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@iii</span>, thanks for your rapid reply, but I'm still in the dark. I'm not trying to be difficult but <em>how</em> do you generate those lists of node ids?</p>
<p>And for the comparison, do you simply eyeball the two lists or is there a way to do it computationally, e.g., put the lists into a spreadsheet, or whatever?</p>
<p>Can you try to be very specific?</p>
</div>
<div id="comment-29505-info" class="comment-info">
<span class="comment-age">(01 Jan '14, 13:09)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="29511"></span>
<div id="comment-29511" class="comment">
<div id="post-29511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>iii is talking about a mechanical mechanism, i.e. a script or program. Of course you can do this all manually but it will take some time and is prone to errors.</p>
</div>
<div id="comment-29511-info" class="comment-info">
<span class="comment-age">(01 Jan '14, 15:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="29517"></span>
<div id="comment-29517" class="comment">
<div id="post-29517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The algorithm seems generally good (of course, elaborations and refinements would probably be helpful). However, I was asking from and end-user perspective. In other words, are there are any tools like MapQuest Open or Nominatim (the web interface) that do this?</p>
</div>
<div id="comment-29517-info" class="comment-info">
<span class="comment-age">(01 Jan '14, 22:02)</span> <span class="comment-user userinfo">mattflaschen</span>
</div>
</div>
</div>
<div id="comment-tools-29497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29497-form-container" class="comment-form-container">
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

