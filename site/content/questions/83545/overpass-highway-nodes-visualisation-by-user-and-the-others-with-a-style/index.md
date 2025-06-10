+++
type = "question"
title = "Overpass, highway nodes visualisation by user and the others with a style."
description = '''Roads, highway=*, only visualise the nodes, sorted by a user &quot;x&quot; and the others. How to visualise the nodes &quot;user=x&quot; nodes (red) and &quot;the rest&quot; (blue) in overpass. [bbox:{{bbox}}]; way[highway]-&amp;gt;.hw;  node (user:&quot;x&quot;)(w.hw); out;   {{style:  node {  color:red;  fill-color:red;  symbol-size:3;  }  ...'''
date = "2022-02-21T14:21:00Z"
lastmod = "2022-02-22T07:42:00Z"
weight = 83545
keywords = [ "overpass" ]
aliases = [ "/questions/83545" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass, highway nodes visualisation by user and the others with a style.](/questions/83545/overpass-highway-nodes-visualisation-by-user-and-the-others-with-a-style)

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
<span id="post-83545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83545-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Roads, highway=*, only visualise the nodes, sorted by a user "x" and the others. How to visualise the nodes "user=x" nodes (red) and "the rest" (blue) in overpass.</p>
<pre><code>[bbox:{{bbox}}];
way[highway]-&gt;.hw;
&#10;node (user:&quot;x&quot;)(w.hw);
out;
&#10;
{{style:
  node {
  color:red;
  fill-color:red;
  symbol-size:3;
  }
&#10;
}}</code></pre>
<p>Can you help with a good query code and styling code?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '22, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-83545" class="comments-container">
&#10;</div>
<div id="comment-tools-83545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83545-form-container" class="comment-form-container">
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

<span id="83546"></span>

<div id="answer-container-83546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83546-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're filtering out "the rest" by restricting the returned data with (user:"x")</p>
<p>You need to out the meta data.</p>
<pre><code>[bbox:{{bbox}}];
way[highway];
node(w);
out meta;
&#10;{{style:
node{color:blue;fill-color:blue;symbol-size:3;}
node[@user=X] {color:red;fill-color:red;symbol-size:5;}
}}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '22, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83546" class="comments-container">
<span id="83549"></span>
<div id="comment-83549" class="comment">
<div id="post-83549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this is working fine. I was thinking too difficult with the query.</p>
</div>
<div id="comment-83549-info" class="comment-info">
<span class="comment-age">(22 Feb '22, 07:42)</span> <span class="comment-user userinfo">Allroads</span>
</div>
</div>
</div>
<div id="comment-tools-83546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83546-form-container" class="comment-form-container">
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

