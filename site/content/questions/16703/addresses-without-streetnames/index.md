+++
type = "question"
title = "Addresses without streetnames"
description = '''How should addresses be tagged, when a village does not use streetnames? Here, addresses only consist of the village, optionally the hamlet and the housenumber? Should the hamlet name be used for addr:street? Or should another key like addr:place or addr:hamlet be used? But in that case: How can I i...'''
date = "2012-10-06T14:43:00Z"
lastmod = "2015-07-14T11:20:00Z"
weight = 16703
keywords = [ "hamlet", "streetnames", "address" ]
aliases = [ "/questions/16703" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Addresses without streetnames](/questions/16703/addresses-without-streetnames)

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
<span id="post-16703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16703-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should addresses be tagged, when a village does not use streetnames? Here, addresses only consist of the village, optionally the hamlet and the housenumber? Should the hamlet name be used for addr:street? Or should another key like addr:place or addr:hamlet be used? But in that case: How can I indicate that (searching/indexing) software should not try to (desperately) search for streetnames like Nominatim does if no addr:street is given?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hamlet" rel="tag" title="see questions tagged &#39;hamlet&#39;">hamlet</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '12, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-16703" class="comments-container">
&#10;</div>
<div id="comment-tools-16703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16703-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="16724"></span>

<div id="answer-container-16724" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16724-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tyr_asd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>in the wiki, the tag addr:place is shown for this purpose <a href="http://wiki.openstreetmap.org/wiki/Key:addr:place">http://wiki.openstreetmap.org/wiki/Key:addr:place</a></p>
<p>e.g. addr:place=Somevillage, addr:housenumber=123a</p>
<p>I used this on some addresses in Rustavi, where houses are numbered by microraions instead of streets, seems to be the most apropriate way of tagging so far... <a href="http://www.openstreetmap.org/?lat=41.57088&amp;lon=44.96872&amp;zoom=17&amp;layers=M">http://www.openstreetmap.org/?lat=41.57088&amp;lon=44.96872&amp;zoom=17&amp;layers=M</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '12, 05:59</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-16724" class="comments-container">
&#10;</div>
<div id="comment-tools-16724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16724-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16717"></span>

<div id="answer-container-16717" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16717-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd say tag it with the smallest feature that it is part of (town, village, street, whatever) using addr:*. It would be useful to have examples to improve nominatim, if you can tag something, document it in the wiki and create an example here (<a href="http://wiki.openstreetmap.org/wiki/Nominatim/TestCases)">http://wiki.openstreetmap.org/wiki/Nominatim/TestCases)</a> it should hopefully get resolved as a developer finds time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '12, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-16717" class="comments-container">
&#10;</div>
<div id="comment-tools-16717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16717-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44177"></span>

<div id="answer-container-44177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44177-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Should the hamlet name be used for addr:street?</p>
</blockquote>
<p>No. Don't try to "force" real data to meet an arbitrary addressing scheme. If there are no street names, then there should be no <code>addr:street</code> tags. OSM should reflect what's on the ground.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '15, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-44177" class="comments-container">
&#10;</div>
<div id="comment-tools-44177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44177-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16708"></span>

<div id="answer-container-16708" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16708-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-16708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In theory addr:suburb was suggested for this. Practically I use it, but I don't think all apps that would want to use it (search for it) could cope with it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '12, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-16708" class="comments-container">
<span id="16710"></span>
<div id="comment-16710" class="comment">
<div id="post-16710-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why would you use something that means "part of a bigger place" (suburb) when you are tagging a little mountain village?</p>
</div>
<div id="comment-16710-info" class="comment-info">
<span class="comment-age">(06 Oct '12, 22:09)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="16714"></span>
<div id="comment-16714" class="comment">
<div id="post-16714-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, your answer doesn't help at all. :( addr:suburb is clearly the wrong choice, when a village gives housenumbers by hamlet (one could use addr:hamlet already).</p>
<p>The main problem is, that geocoders (like nominatim) desperately try to find a streetname for a given housenumber, if none is supplied. I'm looking for a method to indicate that there is actually <em>no</em> streetname for a certain address (a missing addr:street does not mean that!).</p>
</div>
<div id="comment-16714-info" class="comment-info">
<span class="comment-age">(07 Oct '12, 11:30)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
</div>
<div id="comment-tools-16708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16708-form-container" class="comment-form-container">
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

