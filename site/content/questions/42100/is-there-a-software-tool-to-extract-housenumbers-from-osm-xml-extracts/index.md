+++
type = "question"
title = "Is there a software tool to extract housenumbers from OSM XML extracts?"
description = '''Hey, I was wondering if there is a tool to extract housenumbers from a OSM XML or pbf extract. I know this is a difficult task, but maybe someone already wrote a tool. Probably it would need Overpass API to get the surroundings borders that might not be included in the extract. Thanks in advance!'''
date = "2015-04-01T19:46:00Z"
lastmod = "2015-04-02T18:44:00Z"
weight = 42100
keywords = [ "housenumbers" ]
aliases = [ "/questions/42100" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a software tool to extract housenumbers from OSM XML extracts?](/questions/42100/is-there-a-software-tool-to-extract-housenumbers-from-osm-xml-extracts)

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
<span id="post-42100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42100-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I was wondering if there is a tool to extract housenumbers from a OSM XML or pbf extract. I know this is a difficult task, but maybe someone already wrote a tool. Probably it would need Overpass API to get the surroundings borders that might not be included in the extract.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '15, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7ec5c174de466f97a699757f71dc398b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerosin&#39;s gravatar image" />
<p><span>kerosin</span><br />
<span class="score" title="411 reputation points">411</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerosin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42100" class="comments-container">
&#10;</div>
<div id="comment-tools-42100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42100-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="42101"></span>

<div id="answer-container-42101" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42101-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Depends on what you want <em>with</em> your house numbers! Nominatim has an export facility which might be useful. I hear that people are also using <a href="https://github.com/ltog/osmi-addresses">https://github.com/ltog/osmi-addresses</a> to extract house numbers, even if that was originally made as a quality control tool.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '15, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42101" class="comments-container">
<span id="42102"></span>
<div id="comment-42102" class="comment">
<div id="post-42102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I want to store them in a separate database - just for testing purposes. SpatiaLite (SQLite) like in OSMI would be fine. So ./extract.osm.pbf output.sqlite would do the job?</p>
</div>
<div id="comment-42102-info" class="comment-info">
<span class="comment-age">(01 Apr '15, 20:01)</span> <span class="comment-user userinfo">kerosin</span>
</div>
</div>
</div>
<div id="comment-tools-42101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42101-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42112"></span>

<div id="answer-container-42112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42112-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note that addresses are basically stored in three ways: as part of polygons (closed ways, multipolygons), lines (non-closed ways) and points (nodes). Unless you extract all these geometry types, you may not get a full picture of addressing in different regions. E.g. for line features, address interpolation values can be stored ("from" - "to" values). Since, as with the line features, different addressing systems are in use, you will generally need to extract a different set of keys with each geometry type, and also consider / extract multiple addressing keys, as each country / region may make a different use of the available keys.</p>
<p>Even with all relevant keys extracted, making sense and technically using complete address information, will be hard across different regions. Of course, displaying just housenumbers (<strong>addr:housenumber=x</strong>), is less difficult and can be done relatively easy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '15, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-42112" class="comments-container">
&#10;</div>
<div id="comment-tools-42112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42112-form-container" class="comment-form-container">
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

