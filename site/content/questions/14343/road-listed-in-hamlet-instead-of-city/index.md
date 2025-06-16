+++
type = "question"
title = "Road listed in Hamlet instead of City"
description = '''My parents live on Milton Road in Charlotte NC. When searching for their address I couldn&#x27;t originally find it. The reason is that it is listed in the Hamlet of Hope Park. This is incorrect, Hope Park would be considered a neighborhood at best. I noticed that a lot of the surrounding neighborhoods a...'''
date = "2012-07-17T18:46:00Z"
lastmod = "2012-07-18T11:57:00Z"
weight = 14343
keywords = [ "city", "wrong", "fix", "hamlet" ]
aliases = [ "/questions/14343" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Road listed in Hamlet instead of City](/questions/14343/road-listed-in-hamlet-instead-of-city)

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
<span id="post-14343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14343-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My parents live on Milton Road in Charlotte NC. When searching for their address I couldn't originally find it. The reason is that it is listed in the Hamlet of Hope Park. This is incorrect, Hope Park would be considered a neighborhood at best. I noticed that a lot of the surrounding neighborhoods are listed the same way. When trying to edit I could not see a way to change it from that Hamlet to the City of Charlotte, is it possible to change and if so, how? I'd like to start making changes to all of the "Hamlets" around them.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span> <span class="post-tag tag-link-hamlet" rel="tag" title="see questions tagged &#39;hamlet&#39;">hamlet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '12, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1e5b87853339fcf4717a0bcfd0e4c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chadlnc&#39;s gravatar image" />
<p><span>chadlnc</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chadlnc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14343" class="comments-container">
&#10;</div>
<div id="comment-tools-14343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14343-form-container" class="comment-form-container">
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

<span id="14359"></span>

<div id="answer-container-14359" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14359-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few ways you can improve things:</p>
<ul>
<li>Make sure the right <a href="https://wiki.openstreetmap.org/wiki/Key:place">place=</a> tag is used on affected nodes/ways. Sometimes the definition varies a bit from country to country (for example the population threshold), so check your country's page for information too.</li>
<li>Turn the place nodes into place areas (closed ways, or relations). When only nodes are available, Nominatim must take a wild guess at where one place starts and the other finishes.</li>
<li>Tag the houses with <a href="https://wiki.openstreetmap.org/wiki/Key:addr">addr:*=</a> (see also <a href="https://wiki.openstreetmap.org/wiki/Addresses">Addresses</a> and <a href="https://wiki.openstreetmap.org/wiki/Karlsruhe_Schema">Karlsruhe</a>). It takes more time to create and maintain, but sometimes it is necessary (for example when the street or postcode isn't the expected value considering the location).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '12, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-14359" class="comments-container">
<span id="14363"></span>
<div id="comment-14363" class="comment">
<div id="post-14363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>see also <a href="/questions/5745/town-nodes-and-polygons-that-fail-to-confine-the-name-within-an-area">https://help.openstreetmap.org/questions/5745/town-nodes-and-polygons-that-fail-to-confine-the-name-within-an-area</a></p>
</div>
<div id="comment-14363-info" class="comment-info">
<span class="comment-age">(18 Jul '12, 11:57)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-14359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14359-form-container" class="comment-form-container">
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

