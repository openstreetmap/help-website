+++
type = "question"
title = "Tools to search for profane language and unexpected characters in a tag value"
description = '''I am looking for a tool(s) that can be used to find profane language in a tag value within a specific country or region. I&#x27;d also like to find cases where a unicode character has been included in a tag value that is not expected in that particular part of the world. Does such a tool exist?'''
date = "2021-11-03T22:11:00Z"
lastmod = "2021-11-04T13:35:00Z"
weight = 82468
keywords = [ "profane", "uk" ]
aliases = [ "/questions/82468" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tools to search for profane language and unexpected characters in a tag value](/questions/82468/tools-to-search-for-profane-language-and-unexpected-characters-in-a-tag-value)

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
<span id="post-82468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a tool(s) that can be used to find profane language in a tag value within a specific country or region. I'd also like to find cases where a unicode character has been included in a tag value that is not expected in that particular part of the world. Does such a tool exist?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-profane" rel="tag" title="see questions tagged &#39;profane&#39;">profane</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '21, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/132b767a2673eaf42f00ceaa141a619c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobJN&#39;s gravatar image" />
<p><span>RobJN</span><br />
<span class="score" title="160 reputation points">160</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobJN has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82468" class="comments-container">
<span id="82471"></span>
<div id="comment-82471" class="comment">
<div id="post-82471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please refrain from fixing your findings in OSM via automated edits (<a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct).">https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct).</a></p>
</div>
<div id="comment-82471-info" class="comment-info">
<span class="comment-age">(04 Nov '21, 12:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="82472"></span>
<div id="comment-82472" class="comment">
<div id="post-82472-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks but I have no intention to make edits. I just want to understand what is in, and going in to, OSM.</p>
</div>
<div id="comment-82472-info" class="comment-info">
<span class="comment-age">(04 Nov '21, 13:35)</span> <span class="comment-user userinfo">RobJN</span>
</div>
</div>
</div>
<div id="comment-tools-82468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82468-form-container" class="comment-form-container">
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

<span id="82470"></span>

<div id="answer-container-82470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82470-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure that it is altogether wise to try and solve the <a href="https://en.wikipedia.org/wiki/Scunthorpe_problem">Scunthorpe problem</a>. The context of OSM is likely to produce a very high false-positive rate.</p>
<p>However an obvious approach would be a tool chain using <a href="https://osmcode.org/osmium-tool/">osmium-tool</a> =&gt; <a href="https://osmcode.org/file-formats-manual/#opl-object-per-line-format">OPL format</a> =&gt; standard UNIX pattern matching tools (<code>grep</code>, <code>sed</code> etc.). Osmium can provide bbox filtering and transformation. One-per-line format allows just tag &amp; key values to be examined (e.g., by pulling out that field with <code>awk</code> or <code>perl</code>). The UNIX tools provide a wide range of means of matching regular expressions (for instance, <code>tr</code> could be used to identify specific unicode characters if that was a particular issue.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '21, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-82470" class="comments-container">
&#10;</div>
<div id="comment-tools-82470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82470-form-container" class="comment-form-container">
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

