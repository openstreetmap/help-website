+++
type = "question"
title = "Using API sometimes return CORS error"
description = '''Hi, we are using your API for searching polygon locations for our website. It was working everything how it was supposed to, but unfortunately recently often there is a problem. We are directly using your API https://nominatim.openstreetmap.org/search.php and sometimes we have Access-Control-Allow-O...'''
date = "2021-10-26T16:03:00Z"
lastmod = "2021-10-27T08:37:00Z"
weight = 82378
keywords = [ "cors" ]
aliases = [ "/questions/82378" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using API sometimes return CORS error](/questions/82378/using-api-sometimes-return-cors-error)

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
<span id="post-82378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82378-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, we are using your API for searching polygon locations for our website. It was working everything how it was supposed to, but unfortunately recently often there is a problem. We are directly using your API <a href="https://nominatim.openstreetmap.org/search.php">https://nominatim.openstreetmap.org/search.php</a> and sometimes we have Access-Control-Allow-Origin. This is an urgent matter for us so please, advise us on how to solve the issue or tell us why is happening? There is also a problem when we try to search on <a href="https://nominatim.openstreetmap.org/ui/search.html?q=New+York,">https://nominatim.openstreetmap.org/ui/search.html?q=New+York,</a> here screenshot <a href="https://prnt.sc/1xdxzc5.">https://prnt.sc/1xdxzc5.</a> Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cors" rel="tag" title="see questions tagged &#39;cors&#39;">cors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '21, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e6842dadad0b0c04fd80319fa915c5d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milica09&#39;s gravatar image" />
<p><span>milica09</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milica09 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82378" class="comments-container">
&#10;</div>
<div id="comment-tools-82378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82378-form-container" class="comment-form-container">
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

<span id="82379"></span>

<div id="answer-container-82379" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82379-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-82379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a known issue with OSM's Nominatim servers at the moment - see <a href="https://github.com/osm-search/Nominatim/issues/2485">https://github.com/osm-search/Nominatim/issues/2485</a> .</p>
<blockquote>
<p>This is an urgent matter for us</p>
</blockquote>
<p>If this is urgent for you, you shouldn't be using the volunteer-run OpenStreetMap servers. These are run on a best-effort basis with no uptime guarantees, and subject to a <a href="https://operations.osmfoundation.org/policies/nominatim/">usage policy</a> which can change without notice. If you need a service with reliable uptime, you should find a commercial provider running an instance of Nominatim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '21, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-82379" class="comments-container">
<span id="82384"></span>
<div id="comment-82384" class="comment">
<div id="post-82384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer, could you please recommend us commercial provider running an instance of Nominatim?</p>
</div>
<div id="comment-82384-info" class="comment-info">
<span class="comment-age">(27 Oct '21, 08:12)</span> <span class="comment-user userinfo">milica09</span>
</div>
</div>
<span id="82385"></span>
<div id="comment-82385" class="comment">
<div id="post-82385-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The Nominatim wiki page lists some <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives.2FThird-party_providers">third-party providers</a>.</p>
</div>
<div id="comment-82385-info" class="comment-info">
<span class="comment-age">(27 Oct '21, 08:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82379-form-container" class="comment-form-container">
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

