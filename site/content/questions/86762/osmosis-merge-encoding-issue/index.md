+++
type = "question"
title = "Osmosis merge encoding issue"
description = '''Hi, I am trying to merge together two .osm XML files using Osmosis from CLI. In the XML files there is some public transport data (like bus stops) and some of them have an apostrophe (&#x27;) in their name (as in Italy is often considered as an accent). When I try to merge the two files, I get a single X...'''
date = "2023-02-21T10:45:00Z"
lastmod = "2023-02-22T13:23:00Z"
weight = 86762
keywords = [ "xml", "merge", "java", "osmosis", "encoding" ]
aliases = [ "/questions/86762" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis merge encoding issue](/questions/86762/osmosis-merge-encoding-issue)

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
<span id="post-86762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to merge together two .osm XML files using Osmosis from CLI. In the XML files there is some public transport data (like bus stops) and some of them have an apostrophe (') in their name (as in Italy is often considered as an accent). When I try to merge the two files, I get a single XML file but with the apostrophes being replaced with the " <code>&amp;apos;</code> " string.</p>
<p>How can I preserve the apostrophes after the merge?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '23, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/12fe52dcbc1bb579e965583344eb4c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabenarni&#39;s gravatar image" />
<p><span>gabenarni</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabenarni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '23, 10:47</strong> </span></p>
</div>
</div>
<div id="comments-container-86762" class="comments-container">
&#10;</div>
<div id="comment-tools-86762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86762-form-container" class="comment-form-container">
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

<span id="86772"></span>

<div id="answer-container-86772" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86772-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gabenarni has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is nothing wrong with that. It is just how XML encodes apostrophes. Any program reading XML files should read those correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '23, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-86772" class="comments-container">
<span id="86776"></span>
<div id="comment-86776" class="comment">
<div id="post-86776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, I understand. It was mostly in case I needed to check manually the files so I could understand immediately what the special character was. Thanks!</p>
</div>
<div id="comment-86776-info" class="comment-info">
<span class="comment-age">(22 Feb '23, 13:23)</span> <span class="comment-user userinfo">gabenarni</span>
</div>
</div>
</div>
<div id="comment-tools-86772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86772-form-container" class="comment-form-container">
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

