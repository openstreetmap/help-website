+++
type = "question"
title = "One way &quot;pedestrian&quot; or &quot;pedestrians&quot;?"
description = '''There is a bicycle/pedestrian roundabout here: http://osm.org/go/0EumgXv94. It is mapped as highway:cycleway, and I&#x27;ve added foot:designated to it. It was correctly marked oneway:yes (for bicycles). I want to tag it as non-one way for pedestrians. What is the correct way to do it? Here — http://wiki...'''
date = "2014-08-28T21:23:00Z"
lastmod = "2014-08-29T23:56:00Z"
weight = 36346
keywords = [ "exceptions", "pedestrian", "tagging", "oneway" ]
aliases = [ "/questions/36346" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [One way "pedestrian" or "pedestrians"?](/questions/36346/one-way-pedestrian-or-pedestrians)

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
<span id="post-36346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36346-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a bicycle/pedestrian roundabout here: <a href="http://osm.org/go/0EumgXv94">http://osm.org/go/0EumgXv94</a>. It is mapped as <code>highway:cycleway</code>, and I've added <code>foot:designated</code> to it. It was correctly marked <code>oneway:yes</code> (for bicycles). I want to tag it as non-one way for pedestrians. What is the correct way to do it? Here — <a href="http://wiki.openstreetmap.org/wiki/Key:oneway">http://wiki.openstreetmap.org/wiki/Key:oneway</a> — I see that I can add exceptions. However I am stuck at the word choice: should it be <code>oneway:</code>pedestrian or pedestrians<code>=no</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-exceptions" rel="tag" title="see questions tagged &#39;exceptions&#39;">exceptions</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '14, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/7f75b476d4984deb5e4c83d276b9c22b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kotya&#39;s gravatar image" />
<p><span>Kotya</span><br />
<span class="score" title="631 reputation points">631</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kotya has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36346" class="comments-container">
&#10;</div>
<div id="comment-tools-36346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36346-form-container" class="comment-form-container">
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

<span id="36350"></span>

<div id="answer-container-36350" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36350-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kotya has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The correct tag to express that a oneway restriction does not affect pedestrians would be <code>oneway:foot=no</code> (the term for the type of transport is the same as the keys you use for yes/designated/... values).</p>
<p>However, oneway restrictions don't affect pedestrians by default anyway, so you don't need to do anything.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '14, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-36350" class="comments-container">
<span id="36357"></span>
<div id="comment-36357" class="comment">
<div id="post-36357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you add a prooflink for "don't affect pedestrians by default anyway" please? I am of course concerned about routing apps.</p>
</div>
<div id="comment-36357-info" class="comment-info">
<span class="comment-age">(29 Aug '14, 07:00)</span> <span class="comment-user userinfo">Kotya</span>
</div>
</div>
<span id="36376"></span>
<div id="comment-36376" class="comment">
<div id="post-36376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I accept <code>oneway:foot=no</code> as the answer, however please do provide a prooflink, so that I do not have to tag all other roundabouts in the area (lots of them). Thanks!</p>
</div>
<div id="comment-36376-info" class="comment-info">
<span class="comment-age">(29 Aug '14, 21:25)</span> <span class="comment-user userinfo">Kotya</span>
</div>
</div>
<span id="36387"></span>
<div id="comment-36387" class="comment">
<div id="post-36387-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is mentioned in the <a href="http://wiki.openstreetmap.org/wiki/Key:oneway#Translation_for_routing">section for data consumers</a> on the Key:access page, for example. There it effectively states that (except on paths that are exclusively for pedestrians) oneway restrictions only apply to vehicles.</p>
</div>
<div id="comment-36387-info" class="comment-info">
<span class="comment-age">(29 Aug '14, 23:56)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-36350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36350-form-container" class="comment-form-container">
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

