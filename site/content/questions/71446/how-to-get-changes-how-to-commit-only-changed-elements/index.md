+++
type = "question"
title = "How to get changes / How to commit only changed elements?"
description = '''Hi, I&#x27;ve made a large .osc (osmChange XML) file, like I use to when I&#x27;m in the mood. I&#x27;ve sit on it for two months [waiting for feedback from the local community] so I wanted to update it, resolve conflicts, commit this state to Git, finally to upload it to OSM. However, JOSM doesn&#x27;t let me saving t...'''
date = "2019-11-04T14:06:00Z"
lastmod = "2019-11-05T11:22:00Z"
weight = 71446
keywords = [ "josm", "change", "diff" ]
aliases = [ "/questions/71446" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get changes / How to commit only changed elements?](/questions/71446/how-to-get-changes-how-to-commit-only-changed-elements)

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
<span id="post-71446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71446-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've made a large .osc (osmChange XML) file, like I use to when I'm in the mood. I've sit on it for two months [waiting for feedback from the local community] so I wanted to update it, resolve conflicts, commit this state to Git, finally to upload it to OSM.</p>
<p>However, JOSM doesn't let me saving to .osc, only to .osm (full OSM XML). Let it be a minor problem. Even though .osc has double quotes and the latter has apostrophes (not making file comparison easier), I can survive.</p>
<p>My main issue is that JOSM downloads all dependencies (nodes and ways) of the elements edited in it, resulting in an .osm file three times bigger - and makes file compare completely impossible. This still would not be a problem in itself. However, my previous experiences show that neither JOSM, nor OSM is clever enough to upload only the changed elements. It means that if I modify a character in the name of a relation, all included nodes and ways get a new version under my name - even though I haven't touched a line or vertex.</p>
<p>Is there a plugin, setting, or an external tool to handle this situation in a sane way, e.g., to get back the changed elements only, or to commit only the changed elements?</p>
<p>Greets, Akos</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '19, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e9e80e09b997cc5aee06feb512dae3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ITineris&#39;s gravatar image" />
<p><span>ITineris</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ITineris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71446" class="comments-container">
&#10;</div>
<div id="comment-tools-71446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71446-form-container" class="comment-form-container">
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

<span id="71464"></span>

<div id="answer-container-71464" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71464-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM keeps track of which exact elements have been changed. On upload it will ignore all objects you haven't touched. There might be exceptions, e.g. when adding a tag and removing it later again.</p>
<p>This information is also stored in the OSM XML file. Only elements with <code>action='modify'</code> and <code>action='delete'</code> get uploaded to the OSM database.</p>
<p>If you experienced otherwise please tell us the corresponding changeset.</p>
<p>JOSM also allows you to select all modified objects by using the search string "modified". Likewise, you can limit the upload to the current selection by using "File" -&gt; "Upload selection". As noted above this should not be necessary to achieve your goal since the upload is always restricted to modified objects only.</p>
<p>Also, reconsider your current work flow. A typically suggested work flow is to "upload early, upload often" to reduce the chance of conflicts. If you need to discuss changes with the community ideally discuss them <em>before</em> editing the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '19, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '19, 12:29</strong> </span></p>
</div>
</div>
<div id="comments-container-71464" class="comments-container">
&#10;</div>
<div id="comment-tools-71464" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71464-form-container" class="comment-form-container">
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

