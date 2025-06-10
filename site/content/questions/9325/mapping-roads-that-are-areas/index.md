+++
type = "question"
title = "Mapping roads that are areas?"
description = '''I come across this a lot. Today for example, A large factory with a clearly defined building and car park. There are other areas, some quite large which are (presumably) used for vehicle access of some kind. They are really areas rather than roads. How should they be mapped? On a similar theme - the...'''
date = "2011-12-03T10:55:00Z"
lastmod = "2011-12-03T20:04:00Z"
weight = 9325
keywords = [ "highway", "area" ]
aliases = [ "/questions/9325" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping roads that are areas?](/questions/9325/mapping-roads-that-are-areas)

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
<span id="post-9325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9325-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I come across this a lot. Today for example, A large factory with a clearly defined building and car park. There are other areas, some quite large which are (presumably) used for vehicle access of some kind. They are really areas rather than roads. How should they be mapped? On a similar theme - the MCFC ground near here has large, wide walkways and associated walk 'areas'. How should they be mapped?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '11, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f975d12117093ce5b3b4748dc4927400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobChafer&#39;s gravatar image" />
<p><span>RobChafer</span><br />
<span class="score" title="220 reputation points">220</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobChafer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9325" class="comments-container">
&#10;</div>
<div id="comment-tools-9325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9325-form-container" class="comment-form-container">
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

<span id="9327"></span>

<div id="answer-container-9327" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9327-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RobChafer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually by drawing a closed way around these areas and adding <code>area=yes</code>. Do not forget to connect it to the rest of the road network.</p>
<p><strong>Edit:</strong> In case it was not clear, as pointed out in comments, <code>area=yes</code> is added to any tags, it does not replace any. In your case <code>highway=service service=driveway area=yes</code> for the factory and <code>highway=pedestrian/footway area=yes</code> for the walkways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '11, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '11, 20:58</strong> </span></p>
</div>
</div>
<div id="comments-container-9327" class="comments-container">
<span id="9329"></span>
<div id="comment-9329" class="comment">
<div id="post-9329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any other tags (other than area)?</p>
</div>
<div id="comment-9329-info" class="comment-info">
<span class="comment-age">(03 Dec '11, 13:20)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="9330"></span>
<div id="comment-9330" class="comment">
<div id="post-9330-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>None that I know of.</p>
</div>
<div id="comment-9330-info" class="comment-info">
<span class="comment-age">(03 Dec '11, 14:45)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="9331"></span>
<div id="comment-9331" class="comment">
<div id="post-9331-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just to be clear, add area=yes in addition to the tags that would you would normally use. For example: highway=pedestrian area=yes</p>
</div>
<div id="comment-9331-info" class="comment-info">
<span class="comment-age">(03 Dec '11, 20:04)</span> <span class="comment-user userinfo">DanHomerick</span>
</div>
</div>
</div>
<div id="comment-tools-9327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9327-form-container" class="comment-form-container">
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

