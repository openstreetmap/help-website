+++
type = "question"
title = "Overpass Turbo: extract all ways of a set"
description = '''A short question: I would like to extract all ways that are included in a set consisting of both ways and relations. How can I do that?  Assume the set is called &quot;x&quot;, then, I tried:  way(w.x); way(.x);  all without success because recurse is not defined for way-way and a bit overkill. Feels like the...'''
date = "2021-09-09T11:32:00Z"
lastmod = "2021-09-30T13:20:00Z"
weight = 81702
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/81702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo: extract all ways of a set](/questions/81702/overpass-turbo-extract-all-ways-of-a-set)

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
<span id="post-81702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81702-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A short question: I would like to <strong>extract all ways</strong> that are included in a <strong>set consisting of</strong> both <strong>ways and relations</strong>. How can I do that?</p>
<p>Assume the set is called "x", then, I tried:</p>
<ul>
<li>way(w.x);</li>
<li>way(.x);</li>
</ul>
<p>all without success because recurse is not defined for <em>way-way</em> and a bit overkill. Feels like there must be a simple solution, I just cannot see it ;)</p>
<p><strong>Thanks</strong> for a hint!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '21, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-81702" class="comments-container">
&#10;</div>
<div id="comment-tools-81702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81702-form-container" class="comment-form-container">
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

<span id="81703"></span>

<div id="answer-container-81703" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81703-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, it is explained in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Sets">wiki</a>:</p>
<p>"To read elements from a set, append . and the set name to the command.</p>
<pre><code> node.a[amenity=foo];</code></pre>
<p>will return all nodes in the named set a that have the key amenity with the value foo."</p>
<p>So, in my case, it boild down to: <strong>node.x;</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '21, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '21, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-81703" class="comments-container">
<span id="82006"></span>
<div id="comment-82006" class="comment">
<div id="post-82006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This answer describes what solved my problem. Unfortunately, I cannot mark it as "accepted answer"; could one of the admins please do so, thanks! I hope that marking this question as "answered" can help others that have the same problem and spare those that want to help solving a problem to have to look at this one. Thanks!</p>
</div>
<div id="comment-82006-info" class="comment-info">
<span class="comment-age">(30 Sep '21, 12:39)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="82008"></span>
<div id="comment-82008" class="comment">
<div id="post-82008-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have marked it as accepted.</p>
</div>
<div id="comment-82008-info" class="comment-info">
<span class="comment-age">(30 Sep '21, 13:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81703-form-container" class="comment-form-container">
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

