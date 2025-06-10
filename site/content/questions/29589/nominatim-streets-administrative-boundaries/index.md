+++
type = "question"
title = "Nominatim, streets &amp; administrative boundaries"
description = '''I thought this had come up before but couldn&#x27;t locate relevant past questions. Nominatim takes address info for POIs from their associated streets. This sometimes leads to incorrect results. I have two cases in mind:  Streets can and often run through administrative boundaries. It seems that these s...'''
date = "2014-01-05T00:48:00Z"
lastmod = "2014-01-06T12:21:00Z"
weight = 29589
keywords = [ "boundaries", "nominatim", "street", "address" ]
aliases = [ "/questions/29589" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim, streets & administrative boundaries](/questions/29589/nominatim-streets-administrative-boundaries)

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
<span id="post-29589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29589-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I thought this had come up before but couldn't locate relevant past questions. Nominatim takes address info for POIs from their associated streets. This sometimes leads to incorrect results. I have two cases in mind:</p>
<ol>
<li>Streets can and often run through administrative boundaries. It seems that these streets will have to be split, in order for Nominatim to show each segment with the correct place information. If done, should the boundary and the street share the node at the split? Would this be considered tagging for the geocoder?</li>
<li>How can we deal with cases where the (district) boundary follows the street? When this is the case, POIs on opposite sides would of course be in different districts, but since they are attached to the same street, it doesn't seem possible to get the system to work correctly here.</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '14, 00:48</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4de1232f3377cc783012d889d0375c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_012&#39;s gravatar image" />
<p><span>Paul_012</span><br />
<span class="score" title="686 reputation points">686</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_012 has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-29589" class="comments-container">
&#10;</div>
<div id="comment-tools-29589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29589-form-container" class="comment-form-container">
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

<span id="29612"></span>

<div id="answer-container-29612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29612-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Even if Nominatim or other services fail at assigning multiple addresses to objects crossing administrative boundaries you should <em>not</em> split them at these points. As you already mentioned this is tagging/mapping for a specific service and consequently should be avoided. The only valid solution is to improve these services and fix such problems on the data consumer side.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '14, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29612" class="comments-container">
&#10;</div>
<div id="comment-tools-29612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29593"></span>

<div id="answer-container-29593" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29593-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">this page right</a>, the indexing goes bottom-up. So i's invoked by the addresses itself and uses the tagged/closest road and the polygone/place radius area. So a road that crosses multiple boundaries can also be found in both cases and we don't need to split it.</p>
<p><em>(but please may nominatim experts call me wrong)</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '14, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-29593" class="comments-container">
<span id="29595"></span>
<div id="comment-29595" class="comment">
<div id="post-29595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Based on some observations searching at nominatim.openstreetmap.org, this doesn't appear to be the case.</p>
</div>
<div id="comment-29595-info" class="comment-info">
<span class="comment-age">(05 Jan '14, 12:04)</span> <span class="comment-user userinfo">Paul_012</span>
</div>
</div>
<span id="29596"></span>
<div id="comment-29596" class="comment">
<div id="post-29596-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe then a post (and updating the docs in the wiki) here might be a good choice: <a href="https://lists.openstreetmap.org/listinfo/geocoding">https://lists.openstreetmap.org/listinfo/geocoding</a></p>
</div>
<div id="comment-29596-info" class="comment-info">
<span class="comment-age">(05 Jan '14, 12:22)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29611"></span>
<div id="comment-29611" class="comment">
<div id="post-29611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>iii, the page you mention also states "During the indexing process an address is also calculated using the first feature found for each level. Where an is_in value is provided it is used to filter the address."</p>
<p>So, it's always located in "the first"</p>
</div>
<div id="comment-29611-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 12:01)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-29593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29593-form-container" class="comment-form-container">
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

