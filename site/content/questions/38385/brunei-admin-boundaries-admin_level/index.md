+++
type = "question"
title = "Brunei admin boundaries admin_level"
description = '''At the moment, Brunei has only 2 (or 3 if you include my small admin_level=10 boundary additions) admin boundary levels mapped: 1.&quot;Country boundary&quot; (admin_level=2) for the country, 2.&quot;State boundary&quot; (admin_level=4) for the districts. The capital city (the one and only city) has no boundary and is ...'''
date = "2014-11-09T06:34:00Z"
lastmod = "2014-11-14T09:26:00Z"
weight = 38385
keywords = [ "admin_level", "boundary" ]
aliases = [ "/questions/38385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Brunei admin boundaries admin_level](/questions/38385/brunei-admin-boundaries-admin_level)

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
<span id="post-38385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38385-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>At the moment, Brunei has only 2 (or 3 if you include my small admin_level=10 boundary additions) admin boundary levels mapped: 1."Country boundary" (admin_level=2) for the country, 2."State boundary" (admin_level=4) for the districts. The capital city (the one and only city) has no boundary and is tagged admin_level=2.</p>
<p>The OSMwiki table at <a href="http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">Tag:boundary=administrative page</a> doesn't have Brunei. Looking at closest neighbour Malaysia especially, but also all other countries generally, admin_level=4 for Brunei's districts are wrong. So if I add Brunei to the table, it should probably be something like:</p>
<ul>
<li>admin_level=2 for National Borders</li>
<li>admin_level=6 for Districts (Daerahs)</li>
<li>admin_level=8 for Subdistricts (Mukims)</li>
<li>admin_level=10 for Villages/Towns (Kampongs/Pekans)</li>
</ul>
<p>And for the one and only City Border, which contains most of the Mukims in Brunei-Muara District (according to Wikipedia), maybe admin_level=7.</p>
<p>Also, some little tips on mapping all these boundaries, which are often not really defined, would be nice. Is it okay if I just estimate/guess based on the positions of rivers/roads/woods between the villages/towns? And then, is it better to place the boundary in the centre of these rivers/roads so 2 neighbouring villages can easily share a single way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '14, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/edf8bc160bbf7f47d6cbc6979120b2c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raito&#39;s gravatar image" />
<p><span>raito</span><br />
<span class="score" title="302 reputation points">302</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raito has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-38385" class="comments-container">
<span id="38394"></span>
<div id="comment-38394" class="comment">
<div id="post-38394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are talking about <a href="https://en.wikipedia.org/wiki/Brunei">brunei darussalam</a> right?</p>
</div>
<div id="comment-38394-info" class="comment-info">
<span class="comment-age">(09 Nov '14, 10:45)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="38403"></span>
<div id="comment-38403" class="comment">
<div id="post-38403-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes. Is there another Brunei somewhere else?</p>
</div>
<div id="comment-38403-info" class="comment-info">
<span class="comment-age">(09 Nov '14, 14:01)</span> <span class="comment-user userinfo">raito</span>
</div>
</div>
<span id="38423"></span>
<div id="comment-38423" class="comment">
<div id="post-38423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>boundaries of 2 neighbouring villages always have to share the same way.</p>
</div>
<div id="comment-38423-info" class="comment-info">
<span class="comment-age">(10 Nov '14, 06:12)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="38441"></span>
<div id="comment-38441" class="comment">
<div id="post-38441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">"Because ways have a maximum number of nodes, you are not required to loop around a whole administration with a single way to form a closed area (although this is a good idea for very small administrative areas)"</a></p>
<p>And villages are the smallest admistrative areas, at least in Brunei.</p>
</div>
<div id="comment-38441-info" class="comment-info">
<span class="comment-age">(11 Nov '14, 06:47)</span> <span class="comment-user userinfo">raito</span>
</div>
</div>
<span id="38442"></span>
<div id="comment-38442" class="comment">
<div id="post-38442-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A boundary is typically a relation. This relation exists of multiple (small) ways (aka lines). Each such way will belong to the boundaries of the villages that it is separating. There are never 2 parallel ways. Look e.g. at <a href="http://www.openstreetmap.org/relation/1323975">http://www.openstreetmap.org/relation/1323975</a> any of it's ways will also be part of the boundary of it's neighbours. The will also be reused in case there are subarea or larger areas with the same boundary Please don't use "subarea" as in the provided example</p>
</div>
<div id="comment-38442-info" class="comment-info">
<span class="comment-age">(11 Nov '14, 07:17)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-38385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38385-form-container" class="comment-form-container">
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

<span id="38536"></span>

<div id="answer-container-38536" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>have a look at the web service from user wambacher about displaying all boundary relations on the planet in hierarchical order:</p>
<p><a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a></p>
<p>There you can investigate how boundary lines and relations are mapped and tagged for other countries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '14, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '17, 08:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-38536" class="comments-container">
<span id="38551"></span>
<div id="comment-38551" class="comment">
<div id="post-38551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a nice link, thanks.</p>
<p>I guess I should first focus more on other things than boundaries. Neighbour Malaysia doesn't even have well developed state boundaries.</p>
</div>
<div id="comment-38551-info" class="comment-info">
<span class="comment-age">(14 Nov '14, 09:26)</span> <span class="comment-user userinfo">raito</span>
</div>
</div>
</div>
<div id="comment-tools-38536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38536-form-container" class="comment-form-container">
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

