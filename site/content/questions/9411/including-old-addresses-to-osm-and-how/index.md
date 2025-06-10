+++
type = "question"
title = "Including old addresses to OSM, and how?"
description = '''I have a question about old addresses of buildings and if / how to include them into OSM. I came across several buildings in my neighbourhood that have official address X-street 7 but still additionally signposted their old address Y-street 63a. So the service road accessing these buildings from Y-s...'''
date = "2011-12-10T06:29:00Z"
lastmod = "2015-11-11T08:12:00Z"
weight = 9411
keywords = [ "adddresses", "addressing", "old", "housenumbers", "address" ]
aliases = [ "/questions/9411" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Including old addresses to OSM, and how?](/questions/9411/including-old-addresses-to-osm-and-how)

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
<span id="post-9411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9411-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a question about old addresses of buildings and if / how to include them into OSM. I came across several buildings in my neighbourhood that have official address X-street 7 but still additionally signposted their old address Y-street 63a. So the service road accessing these buildings from Y-street recieved its own name some time in the past and also the accessed buildings were renumbered.</p>
<p>I think, it would still make sense to retain the old addresses, as in my city (Tbilisi, Georgia), many buildings were re-addressed in the past, and are still continually re-addressed. When going to one certain property, someone might use old or not updated guidebooks et al.</p>
<p>Anyway, the Wiki <a href="http://wiki.openstreetmap.org/wiki/Addr">http://wiki.openstreetmap.org/wiki/Addr</a> does not cover old addresses.</p>
<p>Can I include the info like this or in which way? addr:street = X-street addr:housenumber = 7 old_addr:street = Y-street old_addr:housenumber = 63a</p>
<p>Thanks for feedback and suggestions <em>thumbs up</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-adddresses" rel="tag" title="see questions tagged &#39;adddresses&#39;">adddresses</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '11, 06:29</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-9411" class="comments-container">
&#10;</div>
<div id="comment-tools-9411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9411-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="9415"></span>

<div id="answer-container-9415" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9415-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can include them this way, and is what I'd be tempted to do. Unfortunately unless the tags become widely used it is unlikely that searches for the old addresses will find them, unless you do something like create your own custom Nominatim search installation that does use them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '11, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9415" class="comments-container">
<span id="9421"></span>
<div id="comment-9421" class="comment">
<div id="post-9421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but is there a standard way yet? old_addr was just an invention for now, to illustrate my question.</p>
</div>
<div id="comment-9421-info" class="comment-info">
<span class="comment-age">(10 Dec '11, 14:22)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="9422"></span>
<div id="comment-9422" class="comment">
<div id="post-9422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>old_addr has been used a bit already - <a href="http://taginfo.openstreetmap.org/search?q=old_addr#keys">http://taginfo.openstreetmap.org/search?q=old_addr#keys</a></p>
</div>
<div id="comment-9422-info" class="comment-info">
<span class="comment-age">(10 Dec '11, 14:37)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="9433"></span>
<div id="comment-9433" class="comment">
<div id="post-9433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>good to know... by now, I added a new node with the old addresses, but with addr:*=, including a fixme tag to either delete them or include them into the building with an appropriate tag. Guess I will clean it myself.</p>
</div>
<div id="comment-9433-info" class="comment-info">
<span class="comment-age">(11 Dec '11, 09:39)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-9415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46523"></span>

<div id="answer-container-46523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46523-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would use addr:old: <em>Is also a bit more conmen. (<a href="http://taginfo.openstreetmap.org/search?q=addr:old#keys)">http://taginfo.openstreetmap.org/search?q=addr:old#keys)</a> Less used is old:addr:</em> (<a href="http://taginfo.openstreetmap.org/search?q=old:addr#keys)">http://taginfo.openstreetmap.org/search?q=old:addr#keys)</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '15, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ba45c429eada4d97e7ea03ae23cb4c9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mono11&#39;s gravatar image" />
<p><span>mono11</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mono11 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46523" class="comments-container">
&#10;</div>
<div id="comment-tools-46523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9434"></span>

<div id="answer-container-9434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9434-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-9434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Inventing a new tag by prefixing it with old_ does not seem a good solution to me. If it changes again you will need older_ or put multiple values in it...<br />
If the numbers were not reassigned, independent node with addr:* should be fine with some time information like <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/temporary">http://wiki.openstreetmap.org/wiki/Proposed_features/temporary</a><br />
If the numbers were used again it cannot be really used (there would be two places with the same address)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '11, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '11, 10:03</strong> </span></p>
</div>
</div>
<div id="comments-container-9434" class="comments-container">
&#10;</div>
<div id="comment-tools-9434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9434-form-container" class="comment-form-container">
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

