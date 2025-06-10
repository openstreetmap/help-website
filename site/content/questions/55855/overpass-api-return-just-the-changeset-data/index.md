+++
type = "question"
title = "Overpass-api: Return just the changeset data?"
description = '''Hi I&#x27;m using QL to try &amp;amp; return data of changesets created in the previous day. [out:xml][timeout:25]; (  (node(newer:&quot;{{date:1Day}}&quot;)({{bbox}});  way(newer:&quot;{{date:1Day}}&quot;)({{bbox}});  )  ); out meta;  This code returns the data I require (changeset &amp;amp; user) but does it for each entity found...'''
date = "2017-04-25T12:20:00Z"
lastmod = "2022-10-30T01:31:00Z"
weight = 55855
keywords = [ "overpass", "meta", "ql", "changeset" ]
aliases = [ "/questions/55855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass-api: Return just the changeset data?](/questions/55855/overpass-api-return-just-the-changeset-data)

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
<span id="post-55855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55855-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm using QL to try &amp; return data of changesets created in the previous day.</p>
<pre><code>[out:xml][timeout:25];
(
 (node(newer:&quot;{{date:1Day}}&quot;)({{bbox}});
   way(newer:&quot;{{date:1Day}}&quot;)({{bbox}});
 ) 
);
out meta;</code></pre>
<p>This code returns the data I require (changeset &amp; user) but does it for each entity found:</p>
<pre><code>  &quot;&lt;&quot;way id=&quot;197195793&quot; version=&quot;3&quot; timestamp=&quot;2017-04-24T16:41:29Z&quot; changeset=&quot;12345678&quot; uid=&quot;876432&quot; user=&quot;Joe Bloggs&quot;&gt;
    &quot;&lt;&quot;snip&gt;
  &quot;&lt;&quot;/way&gt;</code></pre>
<p>Is there a way to return purely a list of the changesets?</p>
<p>OT Website question: Why doesn't the Markdown 'code' button accept (auto translate) '&lt;' characters?!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-meta" rel="tag" title="see questions tagged &#39;meta&#39;">meta</span> <span class="post-tag tag-link-ql" rel="tag" title="see questions tagged &#39;ql&#39;">ql</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '17, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-55855" class="comments-container">
&#10;</div>
<div id="comment-tools-55855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55855-form-container" class="comment-form-container">
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

<span id="86021"></span>

<div id="answer-container-86021" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86021-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For everybody who get past this question, here's the answer:</p>
<p><code>node(if: changeset() == "CHANGESET_ID")({{bbox}});</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '22, 00:25</strong></p>
<img src="https://secure.gravatar.com/avatar/30f644b2f9a6ce5f3364a5bba71d839b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hanzceo&#39;s gravatar image" />
<p><span>hanzceo</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hanzceo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86021" class="comments-container">
<span id="86022"></span>
<div id="comment-86022" class="comment">
<div id="post-86022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That doesn't answer the question.</p>
</div>
<div id="comment-86022-info" class="comment-info">
<span class="comment-age">(30 Oct '22, 01:31)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-86021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86021-form-container" class="comment-form-container">
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

