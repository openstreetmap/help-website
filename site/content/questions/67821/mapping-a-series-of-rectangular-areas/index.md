+++
type = "question"
title = "mapping a series of rectangular areas"
description = '''I want to map sets of locations in rectangular areas. These will be Amateur Radio repeaters which, for reasons of security, I want to show as &#x27;Maidenhead locator&#x27; rectangles, defined areas in which the repeaters exist. This grid already exists as a layer (correct term?) in OpenTopoMap and routinely ...'''
date = "2019-01-31T11:51:00Z"
lastmod = "2019-01-31T14:24:00Z"
weight = 67821
keywords = [ "locator", "draw", "maidenhead", "grid", "rectangle" ]
aliases = [ "/questions/67821" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapping a series of rectangular areas](/questions/67821/mapping-a-series-of-rectangular-areas)

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
<span id="post-67821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67821-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to map sets of locations in rectangular areas. These will be Amateur Radio repeaters which, for reasons of security, I want to show as 'Maidenhead locator' rectangles, defined areas in which the repeaters exist. This grid already exists as a layer (correct term?) in OpenTopoMap and routinely used in Amateur Radio. There are a few dozens of sites in the UK, in each of several categories, which I would propose to map separately. Is there a way - a 'draw rectangle' instruction - to present locations as a set of highlighted/coloured, labelled rectangles in this scheme? If necessary, I guess I could calculate the corners in lat/long. The rectangles are 2.5' lat by 5' long. Thanks Jerry</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-locator" rel="tag" title="see questions tagged &#39;locator&#39;">locator</span> <span class="post-tag tag-link-draw" rel="tag" title="see questions tagged &#39;draw&#39;">draw</span> <span class="post-tag tag-link-maidenhead" rel="tag" title="see questions tagged &#39;maidenhead&#39;">maidenhead</span> <span class="post-tag tag-link-grid" rel="tag" title="see questions tagged &#39;grid&#39;">grid</span> <span class="post-tag tag-link-rectangle" rel="tag" title="see questions tagged &#39;rectangle&#39;">rectangle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '19, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e47612332c253e0ee5efb7585d8959d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IcomJerry&#39;s gravatar image" />
<p><span>IcomJerry</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IcomJerry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67821" class="comments-container">
&#10;</div>
<div id="comment-tools-67821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67821-form-container" class="comment-form-container">
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

<span id="67823"></span>

<div id="answer-container-67823" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67823-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-67823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure the amateur radio repeaters belong in OpenStreetMap, particularly not as Maidenhead Locator areas. If you have the data though you should be able to display it as an overlay, converting the actual location to a rectangle as you suggest (perhaps pre-converting them so you could just have the Maidenhead co-ordinates in your javacript as per <a href="https://leafletjs.com/reference-1.4.0.html#rectangle">https://leafletjs.com/reference-1.4.0.html#rectangle</a> maybe).</p>
<p>You could use this site to determine the square from the location</p>
<p><a href="https://www.karhukoti.com/maidenhead-grid-square-locator/">https://www.karhukoti.com/maidenhead-grid-square-locator/</a></p>
<p>and this site gives opposite corners of the rectangle from the locator</p>
<p><a href="https://www.qsl.net/k7jar/Links_files/latlon2grid_1.html">https://www.qsl.net/k7jar/Links_files/latlon2grid_1.html</a></p>
<p>(G4ZXS in JO01nt)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '19, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-67823" class="comments-container">
<span id="67825"></span>
<div id="comment-67825" class="comment">
<div id="post-67825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks EdLoach I was thinking more of OpenTopoMap but here seems to be the place to ask questions.</p>
<h1 id="gotsomereadingtodo">gotsomereadingtodo</h1>
<p>Locator squares seem to be the right size for fairly vague locations, so the criminal community don't have good targets. A number of repeater keepers are quite bothered about this. I'm currently publishing postcode areas for maps but I'm not entirely happy with it, and want to show all repeaters of one type on the same map. Google is discontinuing the method I used previously. (jerry in JO01NI)</p>
</div>
<div id="comment-67825-info" class="comment-info">
<span class="comment-age">(31 Jan '19, 14:24)</span> <span class="comment-user userinfo">IcomJerry</span>
</div>
</div>
</div>
<div id="comment-tools-67823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67823-form-container" class="comment-form-container">
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

