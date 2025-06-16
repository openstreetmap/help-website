+++
type = "question"
title = "How to tag something that is a ski piste in winter and a hiking trail in summer?"
description = '''Hi, there&#x27;s a couple of paths around here that are hiking trails in summer and ski pistes in winter - so probably they should be tagged both route=ski and highway=footway. However, to make things even more complicated, in winter pedestrians aren&#x27;t allowed on the ski pistes, so in winter, highway=foo...'''
date = "2014-04-02T22:52:00Z"
lastmod = "2014-04-03T08:18:00Z"
weight = 32084
keywords = [ "ski", "footway", "tagging" ]
aliases = [ "/questions/32084" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag something that is a ski piste in winter and a hiking trail in summer?](/questions/32084/how-to-tag-something-that-is-a-ski-piste-in-winter-and-a-hiking-trail-in-summer)

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
<span id="post-32084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32084-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, there's a couple of paths around here that are hiking trails in summer and ski pistes in winter - so probably they should be tagged both route=ski and highway=footway.</p>
<p>However, to make things even more complicated, in winter pedestrians aren't allowed on the ski pistes, so in winter, highway=footway is wrong.</p>
<p>Is there any way to tag this properly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ski" rel="tag" title="see questions tagged &#39;ski&#39;">ski</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '14, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/40ecc595f717c15489cc8f613076e547?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berolinux&#39;s gravatar image" />
<p><span>berolinux</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berolinux has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32084" class="comments-container">
&#10;</div>
<div id="comment-tools-32084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32084-form-container" class="comment-form-container">
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

<span id="32085"></span>

<div id="answer-container-32085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32085-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming it is not in a urban/suburban area, I'd tag it as highway=path, piste:type=downhill/nordic/skitour (whichever type of skiing is appropriate) to cover the basics. For a more urban area I'd probably use highway=footway instead of path. For ski tagging see: <a href="https://wiki.openstreetmap.org/wiki/Piste_Maps">https://wiki.openstreetmap.org/wiki/Piste_Maps</a></p>
<p>If pedestrian access is prohibited in winter, then I'd look at the seasonal and conditional access tags. See <a href="https://wiki.openstreetmap.org/wiki/Key:seasonal">https://wiki.openstreetmap.org/wiki/Key:seasonal</a> and <a href="https://wiki.openstreetmap.org/wiki/Key:conditional">https://wiki.openstreetmap.org/wiki/Key:conditional</a> Maybe something like foot:conditional=no @ Nov-Apr.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '14, 01:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-32085" class="comments-container">
<span id="32088"></span>
<div id="comment-32088" class="comment">
<div id="post-32088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had this problem ages ago with a cross-country ski track which had hefty fines (IIRC 250 Euro) for walking on it in winter. The conditional access tags seem to be the way to go (off to finally map my use-case).</p>
</div>
<div id="comment-32088-info" class="comment-info">
<span class="comment-age">(03 Apr '14, 08:18)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32085-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32087"></span>

<div id="answer-container-32087" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Route=ski is more a tag dedicated to route relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '14, 05:50</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-32087" class="comments-container">
&#10;</div>
<div id="comment-tools-32087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32087-form-container" class="comment-form-container">
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

