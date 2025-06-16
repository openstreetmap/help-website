+++
type = "question"
title = "How to tag a business with multiple buildings?"
description = '''In this case, I&#x27;m looking to tag a gas station that has a central building (a convenience store) and the separate covered area for gas pumps. Should I use a multipolygon relation? If so, what would the roles be if there is no &quot;inner&quot; and &quot;outer&quot; (as in the example of a building with a courtyard) but...'''
date = "2014-01-06T14:05:00Z"
lastmod = "2014-01-08T09:42:00Z"
weight = 29613
keywords = [ "building", "tagging", "multipolygon" ]
aliases = [ "/questions/29613" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a business with multiple buildings?](/questions/29613/how-to-tag-a-business-with-multiple-buildings)

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
<span id="post-29613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In this case, I'm looking to tag a gas station that has a central building (a convenience store) and the separate covered area for gas pumps. Should I use a multipolygon relation? If so, what would the roles be if there is no "inner" and "outer" (as in the example of a building with a courtyard) but rather just two separate buildings?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '14, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/58935a74b4c5d31a5cf13272e9b54257?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wdpk&#39;s gravatar image" />
<p><span>wdpk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wdpk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29613" class="comments-container">
&#10;</div>
<div id="comment-tools-29613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29613-form-container" class="comment-form-container">
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

<span id="29615"></span>

<div id="answer-container-29615" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29615-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In this example you could tag the whole area of the fuel station with <code>amenity=fuel</code> and tag the buildings as <code>building=yes/shop/whatever</code></p>
<p>A similar method works for <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">schools</a>.</p>
<p>In the more general case I have seen buildings tagged as <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Two_disjunct_outer_rings">multiple outers in a multipolygon relation</a> with no inners.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '14, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-29615" class="comments-container">
<span id="29659"></span>
<div id="comment-29659" class="comment">
<div id="post-29659-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You don't need 'multipolygon' relations. Either you can draw a single polygon (a closed way) and that's it. Or the business is spread in multiple locations and you have to use the relation 'site'</p>
</div>
<div id="comment-29659-info" class="comment-info">
<span class="comment-age">(08 Jan '14, 09:42)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-29615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29615-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29614"></span>

<div id="answer-container-29614" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29614-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi what about building=yes with tags for the available merchandise. The covered area for or with gas pumps is just that building=roof or covered=yes. And separatly tags not a polygone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '14, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-29614" class="comments-container">
<span id="29616"></span>
<div id="comment-29616" class="comment">
<div id="post-29616-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>ps read this as well <a href="/questions/22083/should-petrol-station-facilities-be-mapped-separately">https://help.openstreetmap.org/questions/22083/should-petrol-station-facilities-be-mapped-separately</a></p>
</div>
<div id="comment-29616-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 14:14)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-29614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29614-form-container" class="comment-form-container">
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

