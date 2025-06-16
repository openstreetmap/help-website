+++
type = "question"
title = "Extracting navigable rivers"
description = '''Hi, I would like to extract all navigable rivers from the OSM data.  http://en.wikipedia.org/wiki/Navigability I know the tools and processes, but I cannot figure out the combination of tags I should use to filter the data. If I take all ways with tags river,riberbank,canal, then I get huge amounts ...'''
date = "2011-11-18T14:08:00Z"
lastmod = "2011-11-18T14:57:00Z"
weight = 9111
keywords = [ "navigable", "river" ]
aliases = [ "/questions/9111" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting navigable rivers](/questions/9111/extracting-navigable-rivers)

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
<span id="post-9111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9111-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to extract all navigable rivers from the OSM data. <a href="http://en.wikipedia.org/wiki/Navigability">http://en.wikipedia.org/wiki/Navigability</a></p>
<p>I know the tools and processes, but I cannot figure out the combination of tags I should use to filter the data. If I take all ways with tags river,riberbank,canal, then I get huge amounts of data and most of the rivers are small/narrow and not navigable.</p>
<p>Could anyone suggest additional tags to filter the rivers by?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-navigable" rel="tag" title="see questions tagged &#39;navigable&#39;">navigable</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '11, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/8e6d66cfd97b0b1d61b2833aa82d45fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dennisk&#39;s gravatar image" />
<p><span>dennisk</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dennisk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9111" class="comments-container">
&#10;</div>
<div id="comment-tools-9111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9111-form-container" class="comment-form-container">
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

<span id="9115"></span>

<div id="answer-container-9115" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9115-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dennisk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like you're going to have to make some assumptions about what kind of waterway is navigable and what isn't. Only a few waterways have been tagged as <code>navigable=*</code>, possibly because it's hard to ensure the <a href="https://wiki.openstreetmap.org/wiki/Verifiability">verifiability</a> of such a tag.</p>
<p>Many waterways have been tagged with legal permissions using the <code>boat=*</code> tag, but obviously this says nothing about the suitability of such waterways for navigation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '11, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-9115" class="comments-container">
&#10;</div>
<div id="comment-tools-9115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9115-form-container" class="comment-form-container">
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

