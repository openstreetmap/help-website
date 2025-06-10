+++
type = "question"
title = "Select only closed ways in Overpass turbo wizard"
description = '''In Overpass wizard one can say: type:node|way|relation What about type &quot;closed-way&quot;? What&#x27;s the syntax? Thank you, RB'''
date = "2017-10-22T09:42:00Z"
lastmod = "2019-08-24T08:52:00Z"
weight = 60208
keywords = [ "overpass", "wizard", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/60208" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Select only closed ways in Overpass turbo wizard](/questions/60208/select-only-closed-ways-in-overpass-turbo-wizard)

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
<span id="post-60208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60208-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Overpass wizard one can say: type:node|way|relation What about type "closed-way"? What's the syntax? Thank you, RB</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-wizard" rel="tag" title="see questions tagged &#39;wizard&#39;">wizard</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '17, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/85ba90f707d94f60b067fba8a35db716?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bapman&#39;s gravatar image" />
<p><span>bapman</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bapman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '17, 16:34</strong> </span></p>
</div>
</div>
<div id="comments-container-60208" class="comments-container">
&#10;</div>
<div id="comment-tools-60208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60208-form-container" class="comment-form-container">
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

<span id="70504"></span>

<div id="answer-container-70504" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70504-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Closedness">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Closedness</a> - use the operator <code>is_closed()</code></p>
<p>For example, this finds all closed ways with leisure=fitness_station</p>
<p><code> [out:csv(::count)][timeout:60]; ( way ["leisure"="fitness_station"] (if:is_closed()) ; ); out count;</code></p>
<p>See <a href="https://overpass-turbo.eu/s/LMB">https://overpass-turbo.eu/s/LMB</a></p>
<p>For unclosed ways, add ! before is_closed, eg:</p>
<p><code> [bbox:{{bbox}}] ; way["area"="yes"](if:!is_closed()); out geom; </code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '19, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/984eadc21cb77cb316db4ff21c94b869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20E&#39;s gravatar image" />
<p><span>Joseph E</span><br />
<span class="score" title="390 reputation points">390</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph E has 2 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '19, 09:00</strong> </span></p>
</div>
</div>
<div id="comments-container-70504" class="comments-container">
&#10;</div>
<div id="comment-tools-70504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70504-form-container" class="comment-form-container">
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

