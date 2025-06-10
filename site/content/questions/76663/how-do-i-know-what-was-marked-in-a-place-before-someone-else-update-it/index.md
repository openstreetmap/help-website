+++
type = "question"
title = "How do I know what was marked in a place before someone else update it?"
description = '''I would like to evaluate the tag history for a location. An agricultural site, for example, I would like to know if what today is a soy plantation, was a corn plantation once. It is possible?'''
date = "2020-09-16T15:06:00Z"
lastmod = "2020-09-16T17:56:00Z"
weight = 76663
keywords = [ "plantation", "soil", "agriculture", "history" ]
aliases = [ "/questions/76663" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I know what was marked in a place before someone else update it?](/questions/76663/how-do-i-know-what-was-marked-in-a-place-before-someone-else-update-it)

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
<span id="post-76663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76663-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to evaluate the tag history for a location. An agricultural site, for example, I would like to know if what today is a soy plantation, was a corn plantation once. It is possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-plantation" rel="tag" title="see questions tagged &#39;plantation&#39;">plantation</span> <span class="post-tag tag-link-soil" rel="tag" title="see questions tagged &#39;soil&#39;">soil</span> <span class="post-tag tag-link-agriculture" rel="tag" title="see questions tagged &#39;agriculture&#39;">agriculture</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '20, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/bedfa3abac632da0b3f6ccebce894c9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nataliapedroso&#39;s gravatar image" />
<p><span>nataliapedroso</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nataliapedroso has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76663" class="comments-container">
&#10;</div>
<div id="comment-tools-76663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76663-form-container" class="comment-form-container">
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

<span id="76664"></span>

<div id="answer-container-76664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use Overpass-turbo to query an area at a date in the past. <a href="https://overpass-turbo.eu/s/Y4K">https://overpass-turbo.eu/s/Y4K</a> is an example of that. Zoom out, zoom in anywhere you are interested in, and click "run". You can then click on any of the things that are highlighted. That query is:</p>
<pre><code>[date:&quot;2018-09-04T00:00:00Z&quot;];
nwr({{bbox}});
out geom;</code></pre>
<p>but you can of course search for specific things, like with any other overpass query.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '20, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76664" class="comments-container">
&#10;</div>
<div id="comment-tools-76664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76666"></span>

<div id="answer-container-76666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76666-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://osmlab.github.io/osm-deep-history/">Deep History</a>, <a href="https://pewu.github.io/osm-history/#/">PeWu</a> or <a href="http://osm.mapki.com/history/">Deep Diff</a> to view the history of an object (node, way or relation)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '20, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '20, 17:59</strong> </span></p>
</div>
</div>
<div id="comments-container-76666" class="comments-container">
&#10;</div>
<div id="comment-tools-76666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76666-form-container" class="comment-form-container">
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

