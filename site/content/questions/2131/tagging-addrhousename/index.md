+++
type = "question"
title = "Tagging addr:housename"
description = '''I live in a village (UK) where virtually every property has a house name rather than a number. Drivers frequently stop in the layby near my place and ask &#x27;where is ??? cottage please&#x27;? I would like to flourish a print of the area with the housenames on and so direct them on their way. I have had one...'''
date = "2011-01-09T16:19:00Z"
lastmod = "2011-04-20T22:13:00Z"
weight = 2131
keywords = [ "house", "name", "address" ]
aliases = [ "/questions/2131" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging addr:housename](/questions/2131/tagging-addrhousename)

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
<span id="post-2131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2131-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in a village (UK) where virtually every property has a house name rather than a number. Drivers frequently stop in the layby near my place and ask 'where is ??? cottage please'? I would like to flourish a print of the area with the housenames on and so direct them on their way. I have had one go of editing a name but nothing has been rendered. I see where names are visible that they have been entered as names in the addr:housenumber tag field. What is the correct way to edit housenames so they are rendered please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '11, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/27ff85291b9bc05aabe35725f69d682b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Molescott&#39;s gravatar image" />
<p><span>Molescott</span><br />
<span class="score" title="265 reputation points">265</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Molescott has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2131" class="comments-container">
&#10;</div>
<div id="comment-tools-2131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2131-form-container" class="comment-form-container">
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

<span id="2132"></span>

<div id="answer-container-2132" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2132-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a <a href="http://wiki.openstreetmap.org/wiki/Key:addr:housename">addr:housename</a> tag which you could use to enter house names. The <a href="http://wiki.openstreetmap.org/wiki/Name">name</a> tag could also be used, but I guess it is more appropriate to use it on POIs.</p>
<p>Rendering is another issue. <a href="http://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a>, OSM's main renderer, only renders house numbers / names if they roughly fit inside the rendered house outline (and don't conflict with surrounding captions). If the name is too long, it won't show up on a map rendered by mapnik. <a href="http://wiki.openstreetmap.org/wiki/Osmarender">Osmarender</a> instead is a bit more tolerant. You can activate it by selecting the corresponding layer via the blue <em>+</em> in the top right map corner or by adding <em>&amp;layers=O</em> to the URL. Maybe the name of your buildings will show up there. Besides, both mapnik and osmarender will need some time to render your updated map, especially at the weekend.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '11, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '11, 16:50</strong> </span></p>
</div>
</div>
<div id="comments-container-2132" class="comments-container">
<span id="2138"></span>
<div id="comment-2138" class="comment">
<div id="post-2138-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The 'name' tag would be appropriate if it can indeed be considered the name of the building, and thus equivalent to housename. If a building contains more than one housename, that won't work.</p>
</div>
<div id="comment-2138-info" class="comment-info">
<span class="comment-age">(10 Jan '11, 03:13)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-2132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2132-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4678"></span>

<div id="answer-container-4678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4678-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapnik isn't currently rendering addr:housename, but should be able to in the near future. We've planned for its addition and are now waiting for other processes to finish before we can incorporate it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/90263d23dc3f15a98d14d91e889b9d25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lennard&#39;s gravatar image" />
<p><span>Lennard</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lennard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4678" class="comments-container">
&#10;</div>
<div id="comment-tools-4678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2158"></span>

<div id="answer-container-2158" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2158-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>scai...... Thank you for your reply. I was aware of the housename tag but was trying to see if I could use it without drawing a building - as a node.</p>
<p>Mike N..... I agree with your comment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '11, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/27ff85291b9bc05aabe35725f69d682b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Molescott&#39;s gravatar image" />
<p><span>Molescott</span><br />
<span class="score" title="265 reputation points">265</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Molescott has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2158" class="comments-container">
<span id="2161"></span>
<div id="comment-2161" class="comment">
<div id="post-2161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes you can use the addr:housename tag on a node (possibly along with building=yes)</p>
</div>
<div id="comment-2161-info" class="comment-info">
<span class="comment-age">(12 Jan '11, 21:13)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="2165"></span>
<div id="comment-2165" class="comment">
<div id="post-2165-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just a note: Please post replies to answers as comments, not as new answers. Otherwise things get confused quickly...</p>
</div>
<div id="comment-2165-info" class="comment-info">
<span class="comment-age">(13 Jan '11, 10:44)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-2158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2158-form-container" class="comment-form-container">
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

