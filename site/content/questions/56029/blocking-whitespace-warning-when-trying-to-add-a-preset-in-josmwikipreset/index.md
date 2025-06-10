+++
type = "question"
title = "Blocking whitespace warning when trying to add a preset in JOSM/wiki/preset"
description = '''I created a preset that works fine in JOSM (added from a local location) but I have this warnning message when I try to create a new preset in the JOSM wiki: Warning: Invalid Wiki page: XML validation for preset failed: Element &#x27;{http://josm.openstreetmap.de/tagging-preset-1.0}item&#x27;: Character conte...'''
date = "2017-05-04T13:35:00Z"
lastmod = "2017-05-04T14:07:00Z"
weight = 56029
keywords = [ "josm", "preset", "warning", "whitespace" ]
aliases = [ "/questions/56029" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Blocking whitespace warning when trying to add a preset in JOSM/wiki/preset](/questions/56029/blocking-whitespace-warning-when-trying-to-add-a-preset-in-josmwikipreset)

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
<span id="post-56029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created a preset that works fine in JOSM (added from a local location) but I have this warnning message when I try to create a new preset in the JOSM wiki:</p>
<p>Warning: Invalid Wiki page: XML validation for preset failed: Element '{<a href="http://josm.openstreetmap.de/tagging-preset-1.0%7Ditem&#39;:">http://josm.openstreetmap.de/tagging-preset-1.0}item':</a> Character content other than whitespace is not allowed because the content type is 'element-only'.</p>
<p>Though it looks fine otherwise on the preview. I understand there must be a non whitespace character between the tags, but as the warning does not provide any location or indication, I cannot find the problem.</p>
<p>If needed, the full text (header for the JOSM wiki + preset) can be seen here: <a href="https://gist.github.com/severinmenard/35059be8a308b85e73ce934f437557f8">link text</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-preset" rel="tag" title="see questions tagged &#39;preset&#39;">preset</span> <span class="post-tag tag-link-warning" rel="tag" title="see questions tagged &#39;warning&#39;">warning</span> <span class="post-tag tag-link-whitespace" rel="tag" title="see questions tagged &#39;whitespace&#39;">whitespace</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '17, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/35a2e88e2106806c0ba99b9b5e6ef093?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeverinGeo&#39;s gravatar image" />
<p><span>SeverinGeo</span><br />
<span class="score" title="81 reputation points">81</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeverinGeo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56029" class="comments-container">
&#10;</div>
<div id="comment-tools-56029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56029-form-container" class="comment-form-container">
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

<span id="56031"></span>

<div id="answer-container-56031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you should remove all text outside the presets-tag, so also the xml tag should be removed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '17, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-56031" class="comments-container">
&#10;</div>
<div id="comment-tools-56031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56031-form-container" class="comment-form-container">
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

