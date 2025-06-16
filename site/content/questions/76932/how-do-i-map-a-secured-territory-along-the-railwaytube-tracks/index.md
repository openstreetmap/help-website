+++
type = "question"
title = "How do I map a secured territory along the railway/tube tracks?"
description = '''Example area: London, Stretch of a Northern tube line between Edgware and Colindale (https://www.openstreetmap.org/#map=16/51.6014/-0.2575)  There are tracks and a fenced area with trees/bushes on both sides. As I understand that&#x27;s a buffer zone which is maintained (or at least owned) by Tube/Rail c...'''
date = "2020-10-03T19:16:00Z"
lastmod = "2020-10-04T20:14:00Z"
weight = 76932
keywords = [ "railway", "landuse", "forest", "uk", "tube" ]
aliases = [ "/questions/76932" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I map a secured territory along the railway/tube tracks?](/questions/76932/how-do-i-map-a-secured-territory-along-the-railwaytube-tracks)

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
<span id="post-76932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Example area: London, Stretch of a Northern tube line between Edgware and Colindale (<a href="https://www.openstreetmap.org/#map=16/51.6014/-0.2575)">https://www.openstreetmap.org/#map=16/51.6014/-0.2575)</a> <img src="/upfiles/Screenshot_2020-10-03_at_19.10.22.png" alt="See screenshot" /></p>
<p>There are tracks and a fenced area with trees/bushes on both sides. As I understand that's a buffer zone which is maintained (or at least owned) by Tube/Rail company. I see it's mapped as <code>landuse=forest</code>, but from what I've learnt it's not the right usage of this tag. primarily, because nothing is harvested from this 'forest' and it's not really a forest.</p>
<p>So what would you suggest as a better option?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span> <span class="post-tag tag-link-tube" rel="tag" title="see questions tagged &#39;tube&#39;">tube</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '20, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/be20d26db9045491e65f24686822e4e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laechoppe&#39;s gravatar image" />
<p><span>laechoppe</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laechoppe has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-76932" class="comments-container">
&#10;</div>
<div id="comment-tools-76932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76932-form-container" class="comment-form-container">
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

<span id="76937"></span>

<div id="answer-container-76937" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76937-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="laechoppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most people would tag it as <code>natural=wood</code> as an alternative to <code>landuse=forest</code>. Another lesser used tagging would be <code>landcover=trees</code> but I don’t think many data consumers (i.e. map rendering sites) will render the landcover tag.</p>
<p>Rather than remove the landuse tag, you might want to change its value: <code>landuse=railway</code>. It doesn’t quite fit with the description on the wiki page but if it is owned and maintained by a rail company as part of their infrastructure it seems like that would be okay.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '20, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-76937" class="comments-container">
<span id="76938"></span>
<div id="comment-76938" class="comment">
<div id="post-76938-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Exactly what can be inferred from "landuse=forest" and "natural=wood" has been debated for some time - see <a href="https://wiki.openstreetmap.org/wiki/Forest">https://wiki.openstreetmap.org/wiki/Forest</a> for a discussion of that.</p>
<p>"landuse=railway" (in addition to something that says "there are trees here") sounds good for what you are describing though.</p>
</div>
<div id="comment-76938-info" class="comment-info">
<span class="comment-age">(03 Oct '20, 22:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="76939"></span>
<div id="comment-76939" class="comment">
<div id="post-76939-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could add an explicit <code>managed=yes</code> if one knows the <code>natural=wood</code> is actively maintained. Sometimes there are vegetation growing mindlessly on managed lands.</p>
</div>
<div id="comment-76939-info" class="comment-info">
<span class="comment-age">(04 Oct '20, 09:33)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-76937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76937-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76948"></span>

<div id="answer-container-76948" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding to the answer above, according to <a href="https://wiki.openstreetmap.org/wiki/RU:%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F/%D0%93%D0%BE%D0%BB%D0%BE%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F/%D0%9B%D0%B5%D1%81%D0%BD%D0%B0%D1%8F_%D1%80%D0%B0%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C">this page</a> in Russia they voted for the same approach (use of <code>natural=wood</code>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '20, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/be20d26db9045491e65f24686822e4e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laechoppe&#39;s gravatar image" />
<p><span>laechoppe</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laechoppe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76948" class="comments-container">
&#10;</div>
<div id="comment-tools-76948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76948-form-container" class="comment-form-container">
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

