+++
type = "question"
title = "Obtaining a list of items with &quot;tag x but not tag y&quot;"
description = '''I can obtain a list of items with a combination of two tags using the XAPI as follows: wget http://jxapi.openstreetmap.org/xapi/api/0.6/*[amenity=pub][source=*][bbox=-0.645,52.756,-0.595,52.856]  but is it possible to obtain a list of &quot;tag X but not tag Y&quot; (using either XAPI, or Overpass, or somethi...'''
date = "2011-10-09T13:20:00Z"
lastmod = "2011-10-09T18:01:00Z"
weight = 8373
keywords = [ "query", "xapi", "tags" ]
aliases = [ "/questions/8373" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Obtaining a list of items with "tag x but not tag y"](/questions/8373/obtaining-a-list-of-items-with-tag-x-but-not-tag-y)

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
<span id="post-8373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8373-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can obtain a list of items with a combination of two tags using the XAPI as follows:</p>
<pre><code>wget http://jxapi.openstreetmap.org/xapi/api/0.6/*[amenity=pub][source=*][bbox=-0.645,52.756,-0.595,52.856]</code></pre>
<p>but is it possible to obtain a list of "tag X but not tag Y" (using either XAPI, or Overpass, or something else)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '11, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8373" class="comments-container">
&#10;</div>
<div id="comment-tools-8373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8373-form-container" class="comment-form-container">
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

<span id="8374"></span>

<div id="answer-container-8374" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8374-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems like you could use <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a> after downloading a .osm file to <em>drop</em> elements with specific tags. I never used it though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '11, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8374" class="comments-container">
<span id="8376"></span>
<div id="comment-8376" class="comment">
<div id="post-8376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - that was exactly what I was looking for.</p>
</div>
<div id="comment-8376-info" class="comment-info">
<span class="comment-age">(09 Oct '11, 18:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8374-form-container" class="comment-form-container">
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

