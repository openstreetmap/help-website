+++
type = "question"
title = "Tagging a makeshift wooden crossing aid over a small stream?"
description = '''What should I use to tag a small makeshift wooden crossing aid (&quot;bridge&quot;) on a path that goes over a small stram? The &quot;bridge&quot; is really just a few wooden frames thrown into the stream to cross it without getting your feet wet. I&#x27;m hesitant to call it a &quot;bridge&quot;, something like a &quot;crossing&quot; might be...'''
date = "2012-05-30T19:29:00Z"
lastmod = "2012-06-06T10:48:00Z"
weight = 13132
keywords = [ "water", "bridge", "crossing", "stream" ]
aliases = [ "/questions/13132" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging a makeshift wooden crossing aid over a small stream?](/questions/13132/tagging-a-makeshift-wooden-crossing-aid-over-a-small-stream)

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
<span id="post-13132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13132-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What should I use to tag a small makeshift wooden crossing aid ("bridge") on a path that goes over a small stram?</p>
<p>The "bridge" is really just a few wooden frames thrown into the stream to cross it without getting your feet wet. I'm hesitant to call it a "bridge", something like a "crossing" might be more appropriate term. Using it is really more closely related to something like stepping stones (<code>highway=stepping_stones</code>) than a bridge, since you're almost at water level, and does have some gaps in the coverage where the water goes over it. Though I guess it might be technically still a bridge...</p>
<p>I'm very aware this isn't a very important detail to get correct, but still I'm curious as to what would be the best approach.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '12, 19:29</strong></p>
<img src="https://secure.gravatar.com/avatar/91158719fabe7385df1f177f1bd79b91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ilari&#39;s gravatar image" />
<p><span>Ilari</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ilari has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '12, 19:30</strong> </span></p>
</div>
</div>
<div id="comments-container-13132" class="comments-container">
&#10;</div>
<div id="comment-tools-13132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13132-form-container" class="comment-form-container">
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

<span id="13134"></span>

<div id="answer-container-13134" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13134-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ilari has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no "official" way of tagging this type of bridge.</p>
<p>The best option is probably to tag it as <code>bridge=plank</code> or <code>bridge=beam</code>, which are already in use according to <a href="http://taginfo.openstreetmap.org/keys/?key=bridge#values">taginfo</a>.</p>
<p>At any rate, if the path leading to the bridge is tagged appropriately, e.g. <code>highway=footway</code>, you could also just tag the bridge as <code>bridge=yes</code>. Any user and any decent mapping software will probably assume that it must be a very small bridge.</p>
<p>For completeness, tag the width with <code>width=0.8</code> or so (meters is implied). This will help routing software decide that it is unsuitable for most vehicles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '12, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-13134" class="comments-container">
<span id="13172"></span>
<div id="comment-13172" class="comment">
<div id="post-13172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Um, you do mean the <em>path</em> leading to the bridge should be tagged <code>highway=path</code> instead of footway, right? That's how it seems to be used here in finland, at least...</p>
</div>
<div id="comment-13172-info" class="comment-info">
<span class="comment-age">(31 May '12, 22:20)</span> <span class="comment-user userinfo">Ilari</span>
</div>
</div>
<span id="13267"></span>
<div id="comment-13267" class="comment">
<div id="post-13267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Ilari</span>: Well, that depends on the path. If it is mainly meant (or only allowed) for pedestrians, it's <code>footpath</code>. If it's a shared-use path that allows pedestrians and bicycles, it's <code>path</code>.</p>
</div>
<div id="comment-13267-info" class="comment-info">
<span class="comment-age">(05 Jun '12, 16:29)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="13275"></span>
<div id="comment-13275" class="comment">
<div id="post-13275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(not that it's likely to be relevant to this specific question, but) in most of the known world, pedestrians are allowed on cycle paths so (if the bridge concerned looks like mostly like a cycleway), "highway=cycleway" may be the more appropriate way to tag it. However, if your specific locality mostly tags mult-use paths as "highway=path", then I'd do that though.</p>
</div>
<div id="comment-13275-info" class="comment-info">
<span class="comment-age">(06 Jun '12, 10:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13134-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13143"></span>

<div id="answer-container-13143" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13143-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Often dirt footpaths only have a plank or sleeper bridge, it is all that is needed. If it works as a bridge it's a bridge. It should be tagged as a bridge so that when a path crosses a stream it is nice to know there is a bridge.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '12, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-13143" class="comments-container">
&#10;</div>
<div id="comment-tools-13143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13143-form-container" class="comment-form-container">
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

