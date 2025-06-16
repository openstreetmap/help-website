+++
type = "question"
title = "Nominatim : Why would a node return no reverse information ?"
description = '''Using this query : http://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;osm_type=N&amp;amp;osm_id=1914299432&amp;amp;accept-language=fr  I retrieve no informations and I can&#x27;t understand why.  I looking for data for every station of this relation, only two return nothing : the one I gave above and the ...'''
date = "2014-06-11T18:53:00Z"
lastmod = "2014-06-12T18:58:00Z"
weight = 33882
keywords = [ "nominatim" ]
aliases = [ "/questions/33882" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim : Why would a node return no reverse information ?](/questions/33882/nominatim-why-would-a-node-return-no-reverse-information)

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
<span id="post-33882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33882-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using this query : <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_type=N&amp;osm_id=1914299432&amp;accept-language=fr">http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_type=N&amp;osm_id=1914299432&amp;accept-language=fr</a></p>
<p>I retrieve no informations and I can't understand why.</p>
<p>I looking for data for every station of <a href="http://openstreetmap.org/relation/3300434">this relation</a>, only two return nothing : the one I gave above and the same station in the opposite direction.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '14, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33882" class="comments-container">
&#10;</div>
<div id="comment-tools-33882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33882-form-container" class="comment-form-container">
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

<span id="33883"></span>

<div id="answer-container-33883" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33883-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kyro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I looked at the node above. Then at the first three nodes of <a href="https://www.openstreetmap.org/relation/2396015">Relation: A : Fontaine =&gt; Echirolles (2396015)</a>.</p>
<p>Those three all have the tag railway=tram_stop. For the node that doesn't give results this tag was removed. Can this be the cause?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '14, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-33883" class="comments-container">
<span id="33886"></span>
<div id="comment-33886" class="comment">
<div id="post-33886-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, that does it. Any idea why ?</p>
</div>
<div id="comment-33886-info" class="comment-info">
<span class="comment-age">(11 Jun '14, 19:21)</span> <span class="comment-user userinfo">Kyro</span>
</div>
</div>
<span id="33923"></span>
<div id="comment-33923" class="comment">
<div id="post-33923-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Once upon a time Openstreetmap contained a lot less data. People mapped a whole tram stop with a single node with the tag <code>railway=tram_stop</code>. The dual rail line would at that time probably be mapped with a single way. So a node with the tag <code>railway=tram_stop</code> was a point of interest (POI).</p>
<p>Over time we started mapping more and more detail. First the single way would become two ways, so there would also be two tram stops. Then we started adding the platforms. And lastly some people invented a relation to tie it all together.</p>
<p>Nominatim can't index all objects in the world, so only "interesting" objects are indexed. If you <a href="http://nominatim.openstreetmap.org/search.php?q=echirolles+gare&amp;viewbox=-103.36%2C61.65%2C103.36%2C-61.65">search for Echirolles Gare</a>, you'll see that the platforms are indexed (because that is where you actually go to wait for the tram) and the tram stop is indexed (because in the past that was the whole POI). The stop position of the tram is however not very interesting for a lot of people and applications. Besides it is always very near the platform.</p>
</div>
<div id="comment-33923-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 18:58)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33883-form-container" class="comment-form-container">
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

