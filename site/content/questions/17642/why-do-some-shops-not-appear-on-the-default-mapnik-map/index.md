+++
type = "question"
title = "Why do some shops not appear on the default (mapnik?) map?"
description = '''I was looking for a state alcohol shop in Lund Sweden (https://www.openstreetmap.org/?lat=55.705917&amp;amp;lon=13.188067&amp;amp;zoom=18&amp;amp;layers=M)--my wife was sure that it was there but I didn&#x27;t see it on the default (mapnik?) map. I found it in person then went to add it to the map to find it was ther...'''
date = "2012-11-11T09:45:00Z"
lastmod = "2012-11-11T10:16:00Z"
weight = 17642
keywords = [ "shop", "alcohol" ]
aliases = [ "/questions/17642" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do some shops not appear on the default (mapnik?) map?](/questions/17642/why-do-some-shops-not-appear-on-the-default-mapnik-map)

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
<span id="post-17642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17642-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was looking for a state alcohol shop in Lund Sweden (<a href="https://www.openstreetmap.org/?lat=55.705917&amp;lon=13.188067&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=55.705917&amp;lon=13.188067&amp;zoom=18&amp;layers=M</a>)--my wife was sure that it was there but I didn't see it on the default (mapnik?) map. I found it in person then went to add it to the map to find it was there, with all details entered correctly (tag shop=alcohol). Why do some shops show up on the map and not others?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-alcohol" rel="tag" title="see questions tagged &#39;alcohol&#39;">alcohol</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '12, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/6255d93d0b676fd3314762bc97c0b751?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blaine&#39;s gravatar image" />
<p><span>Blaine</span><br />
<span class="score" title="45 reputation points">45</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blaine has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17642" class="comments-container">
&#10;</div>
<div id="comment-tools-17642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17642-form-container" class="comment-form-container">
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

<span id="17643"></span>

<div id="answer-container-17643" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17643-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-17643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an almost infinite number of potential "shop" values, but only the most common ones have icons in the Mapnik style. At the time of writing, these are</p>
<ul>
<li>bakery</li>
<li>bicycle</li>
<li>butcher</li>
<li>car</li>
<li>car_repair</li>
<li>clothes (and fashion)</li>
<li>convenience</li>
<li>department_store</li>
<li>doityourself</li>
<li>florist</li>
<li>hairdresser</li>
<li>supermarket</li>
</ul>
<p>There is no "generic" shop icon (that could be used for "some shop but none of the above").</p>
<p>The relevant code is in <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/inc/layer-amenity-points.xml.inc">http://svn.openstreetmap.org/applications/rendering/mapnik/inc/layer-amenity-points.xml.inc</a> - the usual way to suggest enhancements to the Mapnik style is opening a ticket on trac.openstreetmap.org, ideally with a patch and a suitable SVG icon attached.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17643" class="comments-container">
&#10;</div>
<div id="comment-tools-17643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17643-form-container" class="comment-form-container">
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

