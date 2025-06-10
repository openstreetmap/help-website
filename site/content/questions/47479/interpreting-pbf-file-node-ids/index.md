+++
type = "question"
title = "Interpreting PBF file node ids"
description = '''Hi, I&#x27;m trying to parse PBF country file and I&#x27;m having trouble interpreting node ids. They should be &#x27;delta-encoded&#x27;, but for each DenseNodes group they go from 0 to 8000. Since there are many DenseNodes groups in the file, this results with many duplicate IDs. If I understood the PBF format descri...'''
date = "2016-01-12T13:52:00Z"
lastmod = "2016-01-12T14:15:00Z"
weight = 47479
keywords = [ "development", "nodes", "pbf", "id" ]
aliases = [ "/questions/47479" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Interpreting PBF file node ids](/questions/47479/interpreting-pbf-file-node-ids)

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
<span id="post-47479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47479-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to parse PBF country file and I'm having trouble interpreting node ids. They should be 'delta-encoded', but for each DenseNodes group they go from 0 to 8000. Since there are many DenseNodes groups in the file, this results with many duplicate IDs. If I understood the <span>PBF format description</span> correctly, where it says "x_1, x_2, x_3, I encode x_1, x_2-x_1, x_3-x_2, ...", the first node ID should be a 'real' node id, and the subsequent ones should be delta-encoded.</p>
<p>Can someone shed some light on this?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '16, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a97be53e49ffe4511d6493e940f5c8d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zepe&#39;s gravatar image" />
<p><span>zepe</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zepe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '16, 11:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47479" class="comments-container">
&#10;</div>
<div id="comment-tools-47479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47479-form-container" class="comment-form-container">
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

<span id="47482"></span>

<div id="answer-container-47482" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47482-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-47482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zepe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, you should probably not try to re-invent the wheel and use one of the existing libraries to read PBF files. Getting all the corner cases right isn't as easy as it looks. There are libraries for several languages available. (Shameless plug: if you use C++ I can recommend my <a href="http://osmcode.org/libosmium/">libosmium</a>.) If you still want to do your own you can still look at those implementations to help find your problem</p>
<p>Second: Your interpretation is right. I guess your code is doing something different than that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '16, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '16, 18:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-47482" class="comments-container">
&#10;</div>
<div id="comment-tools-47482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47482-form-container" class="comment-form-container">
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

