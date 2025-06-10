+++
type = "question"
title = "addr:place for cases where building name replaces street name?"
description = '''I am attempting to map a commercial building with multiple addresses where the building&#x27;s name is used in place of any street names. Is addr:place=[building name] (on each of the entrance nodes and also on the building way) the proper way to achieve this? Here is the building I am trying to map: Cad...'''
date = "2018-03-15T05:43:00Z"
lastmod = "2018-03-16T05:11:00Z"
weight = 62684
keywords = [ "building", "addr_street", "nominatim", "addr_place" ]
aliases = [ "/questions/62684" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [addr:place for cases where building name replaces street name?](/questions/62684/addrplace-for-cases-where-building-name-replaces-street-name)

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
<span id="post-62684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am attempting to map a commercial building with multiple addresses where the building's name is used in place of any street names. Is addr:place=[building name] (on each of the entrance nodes and also on the building way) the proper way to achieve this?</p>
<p>Here is the building I am trying to map:</p>
<p><a href="https://www.openstreetmap.org/#map=19/42.43034/-83.48291">CadyCentre</a></p>
<p>The addresses are, for example, 125 CadyCentre, Northville, MI.</p>
<p>My understanding is that this can't be mapped with addr:street as there is no corresponding street. It does bother me that Nominatim is unable to find these addresses, though, and instead links them to the nearest street, but if that's simply an issue with Nominatim and the tagging is correct, then I'll settle for that.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-addr_street" rel="tag" title="see questions tagged &#39;addr_street&#39;">addr_street</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-addr_place" rel="tag" title="see questions tagged &#39;addr_place&#39;">addr_place</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '18, 05:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9dc03a035e635f97b5b33df262290ddb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flatmatt&#39;s gravatar image" />
<p><span>flatmatt</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flatmatt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62684" class="comments-container">
&#10;</div>
<div id="comment-tools-62684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62684-form-container" class="comment-form-container">
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

<span id="62685"></span>

<div id="answer-container-62685" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62685-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-62685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flatmatt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim will be able to recognise the address correctly if you do the following: use nodes for the house numbers with <code>addr:place=CadyCentre</code> (as you have already done) and then add a <code>landuse=commercial,name=CadyCentre</code> around the building.</p>
<p>The other possibility would be to tag your address nodes as follows: <code>addr:housename=CadyCentre,addr:housenumber=125,addr:place=Northville</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '18, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-62685" class="comments-container">
<span id="62697"></span>
<div id="comment-62697" class="comment">
<div id="post-62697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks; this is the element I was missing from the puzzle!</p>
</div>
<div id="comment-62697-info" class="comment-info">
<span class="comment-age">(16 Mar '18, 05:11)</span> <span class="comment-user userinfo">flatmatt</span>
</div>
</div>
</div>
<div id="comment-tools-62685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62685-form-container" class="comment-form-container">
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

