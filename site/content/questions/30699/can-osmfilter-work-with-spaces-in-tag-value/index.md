+++
type = "question"
title = "Can osmfilter work with spaces in tag value?"
description = '''Hello! I want to filter some administrative boundaries out. It works fine when city/village name consist of one word. But if there is a whitespace in the name it goes like this: $ ./osmfilter -v --keep=&#x27;name=&quot;Новые Ляды&quot;&#x27; perm.osm osmfilter Parameter: --keep=name=&quot;Новые Ляды&quot; osmfilter: Filter: keep...'''
date = "2014-02-13T07:07:00Z"
lastmod = "2014-02-18T06:28:00Z"
weight = 30699
keywords = [ "osmfilter", "tags" ]
aliases = [ "/questions/30699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can osmfilter work with spaces in tag value?](/questions/30699/can-osmfilter-work-with-spaces-in-tag-value)

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
<span id="post-30699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30699-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I want to filter some administrative boundaries out. It works fine when city/village name consist of one word. But if there is a whitespace in the name it goes like this:</p>
<pre><code>$ ./osmfilter -v --keep=&#39;name=&quot;Новые Ляды&quot;&#39; perm.osm
osmfilter Parameter: --keep=name=&quot;Новые Ляды&quot;
osmfilter: Filter: keep nodes:
osmfilter: Filter:     &quot;name&quot; = &quot;&quot;Новые&quot;
osmfilter: Filter:     &quot;Ляды&quot;&quot; = &quot;(anything)&quot;
osmfilter: Filter: keep ways:
osmfilter: Filter:     &quot;name&quot; = &quot;&quot;Новые&quot;
osmfilter: Filter:     &quot;Ляды&quot;&quot; = &quot;(anything)&quot;
osmfilter: Filter: keep relations:
osmfilter: Filter:     &quot;name&quot; = &quot;&quot;Новые&quot;
osmfilter: Filter:     &quot;Ляды&quot;&quot; = &quot;(anything)&quot;
osmfilter Parameter: perm.osm
Interrelational hierarchy 1: 0 dependencies.
osmfilter: Relation hierarchies: 0 of maximal 12.
osmfilter: Number of bytes read: 56401798
(3 lines of OSM XML)
osmfilter: Last processed: relation 3496144</code></pre>
<p>It fails to filter tag values with whitespaces. So the question is — is it a feature, a bug or there is a way to insert whitespace in query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '14, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0f096245c021136324dbde4eb91b2ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alsv&#39;s gravatar image" />
<p><span>alsv</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alsv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30699" class="comments-container">
&#10;</div>
<div id="comment-tools-30699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30699-form-container" class="comment-form-container">
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

<span id="30816"></span>

<div id="answer-container-30816" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30816-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've Read The F-ing Source and found an answer:</p>
<p>The space should be escaped with backslash!</p>
<pre><code>$ ./osmfilter -v --keep=&quot;name=Новые\ Ляды or place_name=Новые\ Ляды&quot; perm.osm 
osmfilter Parameter: --keep=name=Новые\ Ляды or place_name=Новые\ Ляды
osmfilter: Filter: keep nodes:
osmfilter: Filter:     &quot;name&quot; = &quot;Новые Ляды&quot;
osmfilter: Filter:   OR
osmfilter: Filter:     &quot;place_name&quot; = &quot;Новые Ляды&quot;
osmfilter: Filter: keep ways:
osmfilter: Filter:     &quot;name&quot; = &quot;Новые Ляды&quot;
osmfilter: Filter:   OR
osmfilter: Filter:     &quot;place_name&quot; = &quot;Новые Ляды&quot;
osmfilter: Filter: keep relations:
osmfilter: Filter:     &quot;name&quot; = &quot;Новые Ляды&quot;
osmfilter: Filter:   OR
osmfilter: Filter:     &quot;place_name&quot; = &quot;Новые Ляды&quot;
osmfilter Parameter: perm.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '14, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0f096245c021136324dbde4eb91b2ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alsv&#39;s gravatar image" />
<p><span>alsv</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alsv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30816" class="comments-container">
&#10;</div>
<div id="comment-tools-30816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30816-form-container" class="comment-form-container">
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

