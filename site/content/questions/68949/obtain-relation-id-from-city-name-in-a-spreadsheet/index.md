+++
type = "question"
title = "Obtain relation ID from city name in a spreadsheet"
description = '''Hi,  I have a spreadsheet where in column A are listed some italian cities, is there a formula that can retrieve the relation ID of that city automatically? To do it I&#x27;m actually going to nominatin, searching the city, select first result and copy the relation ID. Is there a way to automate this wor...'''
date = "2019-04-25T16:32:00Z"
lastmod = "2019-04-25T20:15:00Z"
weight = 68949
keywords = [ "nominatim", "spreadsheet", "relations", "id" ]
aliases = [ "/questions/68949" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Obtain relation ID from city name in a spreadsheet](/questions/68949/obtain-relation-id-from-city-name-in-a-spreadsheet)

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
<span id="post-68949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68949-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a spreadsheet where in column A are listed some italian cities, is there a formula that can retrieve the relation ID of that city automatically? To do it I'm actually going to nominatin, searching the city, select first result and copy the relation ID. Is there a way to automate this work?</p>
<p>example:</p>
<p>COLUMN A COLUMN B</p>
<p>Milano 44915</p>
<p>L'Aquila 41842</p>
<p>Nissoria 39323</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-spreadsheet" rel="tag" title="see questions tagged &#39;spreadsheet&#39;">spreadsheet</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '19, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd10e3924e41387d5ccd750c71b2eef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="volo86&#39;s gravatar image" />
<p><span>volo86</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="volo86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68949" class="comments-container">
&#10;</div>
<div id="comment-tools-68949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68949-form-container" class="comment-form-container">
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

<span id="68954"></span>

<div id="answer-container-68954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68954-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This could, on the Unix command line, be achieved by a combination of using <code>curl</code> to send a request to Nominatim followed by processing the JSON result with the <code>jq</code> utility, for example:</p>
<pre><code>curl -s &quot;https://nominatim.openstreetmap.org/search?q=Milano&amp;format=json&quot; | 
  jq &#39;.[] | select(.class==&quot;place&quot;) | select(.type==&quot;city&quot;) | 
    select(.osm_type==&quot;relation&quot;).osm_id&#39;</code></pre>
<p>You might have to toy with the <code>jq</code> expression a bit to achive the best result. Of course, you can do the same in a programming language of your choice - "request this URL", "decode JSON", "find objects that are cities", "extract their osm_id" - this should be possible with most common scripting languages.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '19, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68954" class="comments-container">
&#10;</div>
<div id="comment-tools-68954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68954-form-container" class="comment-form-container">
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

