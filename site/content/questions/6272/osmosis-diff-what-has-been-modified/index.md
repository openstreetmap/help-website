+++
type = "question"
title = "Osmosis diff: what has been modified"
description = '''Hi,  if I use Osmosis to create a Diff (--derive-change), there is only an information about the new state. Is there a way to get more informations about the old state? something like this: &amp;lt;modify&amp;gt;  &amp;lt;old&amp;gt;  &amp;lt;node id=&quot;52188999&quot; version=&quot;4&quot; uid=&quot;4902&quot; lat=&quot;53&quot; lon=&quot;9&quot;/&amp;gt;&amp;gt;  &amp;lt;/old...'''
date = "2011-07-11T11:04:00Z"
lastmod = "2011-07-12T11:27:00Z"
weight = 6272
keywords = [ "diff", "osmosis" ]
aliases = [ "/questions/6272" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis diff: what has been modified](/questions/6272/osmosis-diff-what-has-been-modified)

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
<span id="post-6272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6272-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, if I use Osmosis to create a Diff (--derive-change), there is only an information about the new state.</p>
<p>Is there a way to get more informations about the old state?</p>
<p>something like this:</p>
<pre><code>&lt;modify&gt;
    &lt;old&gt;
        &lt;node id=&quot;52188999&quot; version=&quot;4&quot; uid=&quot;4902&quot; lat=&quot;53&quot; lon=&quot;9&quot;/&gt;&gt;
    &lt;/old&gt;
    &lt;new&gt;
        &lt;node id=&quot;52188999&quot; version=&quot;6&quot; uid=&quot;63375&quot; lat=&quot;50&quot; lon=&quot;10&quot;/&gt;
    &lt;/new&gt;
&lt;/modify&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '11, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/db9d4c9ffd75f95f97122bbc97b90a64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josias&#39;s gravatar image" />
<p><span>josias</span><br />
<span class="score" title="598 reputation points">598</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josias has 3 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-6272" class="comments-container">
&#10;</div>
<div id="comment-tools-6272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6272-form-container" class="comment-form-container">
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

<span id="6280"></span>

<div id="answer-container-6280" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6280-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="josias has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no method within osmosis for doing that. It's expected that you want to use the diff updates in order to update another data source, and so it's expected that other data source (whether that's a planet file, or a database, or whatever) will have the original "old" state.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '11, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-6280" class="comments-container">
<span id="6285"></span>
<div id="comment-6285" class="comment">
<div id="post-6285-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>do you know some way to get informations about what has been changed?</p>
</div>
<div id="comment-6285-info" class="comment-info">
<span class="comment-age">(12 Jul '11, 11:27)</span> <span class="comment-user userinfo">josias</span>
</div>
</div>
</div>
<div id="comment-tools-6280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6280-form-container" class="comment-form-container">
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

