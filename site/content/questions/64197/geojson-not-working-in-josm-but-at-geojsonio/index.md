+++
type = "question"
title = "GeoJSON not working in JOSM, but at geojson.io"
description = '''Why does this GeoJSON work at geojson.io, but not in JOSM? The link leads to Pastebin. Probably the mistake is obvious, but I just can&#x27;t see it.'''
date = "2018-06-13T14:31:00Z"
lastmod = "2018-07-23T18:49:00Z"
weight = 64197
keywords = [ "josm", "geojson" ]
aliases = [ "/questions/64197" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GeoJSON not working in JOSM, but at geojson.io](/questions/64197/geojson-not-working-in-josm-but-at-geojsonio)

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
<span id="post-64197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why does <a href="https://pastebin.com/hWiWHb7c">this GeoJSON</a> work at <a href="http://geojson.io/">geojson.io</a>, but not in JOSM? The link leads to Pastebin.</p>
<p>Probably the mistake is obvious, but I just can't see it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '18, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/b081ac1f1126c32011d2c9cf57c2b430?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nehaj&#39;s gravatar image" />
<p><span>Nehaj</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nehaj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64197" class="comments-container">
<span id="64201"></span>
<div id="comment-64201" class="comment">
<div id="post-64201-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what is "not working"?</p>
</div>
<div id="comment-64201-info" class="comment-info">
<span class="comment-age">(13 Jun '18, 19:03)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="64206"></span>
<div id="comment-64206" class="comment">
<div id="post-64206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM changed a couple of things in their GeoJSON generation roughly two months back, and it could be that there are still issues with reading back the new output.</p>
</div>
<div id="comment-64206-info" class="comment-info">
<span class="comment-age">(13 Jun '18, 20:36)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="64208"></span>
<div id="comment-64208" class="comment">
<div id="post-64208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> Which revision is safe to use?</p>
</div>
<div id="comment-64208-info" class="comment-info">
<span class="comment-age">(13 Jun '18, 21:28)</span> <span class="comment-user userinfo">Nehaj</span>
</div>
</div>
</div>
<div id="comment-tools-64197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64197-form-container" class="comment-form-container">
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

<span id="64209"></span>

<div id="answer-container-64209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect no JOSM version will read the file currently.</p>
<p>You need to open an issue on the JOSM issue tracker (as it is an obvious bug that JOSM can't read files it created): <a href="http://josm.openstreetmap.de/">http://josm.openstreetmap.de/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '18, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '18, 21:38</strong> </span></p>
</div>
</div>
<div id="comments-container-64209" class="comments-container">
<span id="64835"></span>
<div id="comment-64835" class="comment">
<div id="post-64835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've had no time for this. But here is another user with this problem: <a href="https://github.com/JOSM/geojson/issues/14">https://github.com/JOSM/geojson/issues/14</a></p>
</div>
<div id="comment-64835-info" class="comment-info">
<span class="comment-age">(21 Jul '18, 13:27)</span> <span class="comment-user userinfo">Nehaj</span>
</div>
</div>
</div>
<div id="comment-tools-64209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64865"></span>

<div id="answer-container-64865" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64865-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why has nobody noticed, that the file breaks when "properties": null ??</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '18, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64865" class="comments-container">
<span id="64877"></span>
<div id="comment-64877" class="comment">
<div id="post-64877-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That was already pointed out in the linked JOSM GitHub issue.</p>
</div>
<div id="comment-64877-info" class="comment-info">
<span class="comment-age">(23 Jul '18, 18:49)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-64865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64865-form-container" class="comment-form-container">
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

