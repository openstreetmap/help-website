+++
type = "question"
title = "Get changed nodes and ways from area"
description = '''I want to get the diff of the area, but I&#x27;m only interested in the nodes and ways that changed. I don&#x27;t care about relations. I know I can do: [adiff:&quot;2016-03-01T15:00:00Z&quot;]; (  node(52.1,20.9,52.3,21.2);  &amp;lt;; ); out;  Which returns nodes, ways they&#x27;re on, relations they&#x27;re on (correct me if I und...'''
date = "2016-04-15T13:36:00Z"
lastmod = "2016-04-15T13:36:00Z"
weight = 49243
keywords = [ "overpass", "diff", "area" ]
aliases = [ "/questions/49243" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get changed nodes and ways from area](/questions/49243/get-changed-nodes-and-ways-from-area)

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
<span id="post-49243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49243-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get the diff of the area, but I'm only interested in the nodes and ways that changed. <strong>I don't care about relations</strong>. I know I can do:</p>
<pre><code>[adiff:&quot;2016-03-01T15:00:00Z&quot;];
(
  node(52.1,20.9,52.3,21.2);
  &lt;;
);
out;</code></pre>
<p>Which returns nodes, ways they're on, relations they're on (correct me if I understand something wrong).</p>
<p>So I've modified the query.:</p>
<pre><code>[adiff:&quot;2016-03-01T15:00:00Z&quot;];
(
  node(52.1,20.9,52.3,21.2);
  way(bn);
);
out;</code></pre>
<p>But then I thought, what if a way was changed, but not the node's on it (two ways merged, or a way split or something like that). Is that possible? Would the below query be my final form ?</p>
<pre><code>[adiff:&quot;2016-03-01T15:00:00Z&quot;];
(
  node(52.1,20.9,52.3,21.2);
  way(bn);
  way(52.1,20.9,52.3,21.2);
  node(w);
);
out;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '16, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/3e73428522352ea6f8b8488b21e8fc24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prajmus&#39;s gravatar image" />
<p><span>prajmus</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prajmus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49243" class="comments-container">
&#10;</div>
<div id="comment-tools-49243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49243-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

