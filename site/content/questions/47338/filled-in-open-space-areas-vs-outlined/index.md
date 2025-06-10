+++
type = "question"
title = "Filled in open space areas vs. outlined"
description = '''Hi, As a result of some recent change to the standard map rendering, some of our open space areas are no longer filled in. They just have a green outline. Others are still filled. See this area for example: http://www.openstreetmap.org/#map=15/42.7137/-71.0938 Any ideas about what&#x27;s wrong with the t...'''
date = "2015-12-30T22:30:00Z"
lastmod = "2015-12-30T23:28:00Z"
weight = 47338
keywords = [ "rendering", "landuse", "openspace", "tagging" ]
aliases = [ "/questions/47338" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filled in open space areas vs. outlined](/questions/47338/filled-in-open-space-areas-vs-outlined)

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
<span id="post-47338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47338-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>As a result of some recent change to the standard map rendering, some of our open space areas are no longer filled in. They just have a green outline. Others are still filled. See this area for example:</p>
<p><a href="http://www.openstreetmap.org/#map=15/42.7137/-71.0938">http://www.openstreetmap.org/#map=15/42.7137/-71.0938</a></p>
<p>Any ideas about what's wrong with the tagging? We'd like everything to show as filled green.</p>
<p>Thanks! Glen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-openspace" rel="tag" title="see questions tagged &#39;openspace&#39;">openspace</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '15, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/6e2504984eea82e66eb8e3d304430595?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GlenAsp&#39;s gravatar image" />
<p><span>GlenAsp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GlenAsp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '15, 00:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47338" class="comments-container">
&#10;</div>
<div id="comment-tools-47338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47338-form-container" class="comment-form-container">
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

<span id="47339"></span>

<div id="answer-container-47339" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47339-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I looked at the tagging and (apart from the unnecessary area=yes) the landuse=conservation tag was one I didn't recognise, and I tracked down <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/1826">this discussion</a> which resulted in it no longer being rendered. I suspect you can find a more specific choice for each of the areas either linked from the <a href="http://wiki.openstreetmap.org/wiki/Landcover">landcover</a> or <a href="http://wiki.openstreetmap.org/wiki/Landuse">landuse</a> wiki pages.</p>
<p>Apart from that, if you are happy that the tagging is correct don't worry too much about how it is rendered in one particular rendering of the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '15, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-47339" class="comments-container">
&#10;</div>
<div id="comment-tools-47339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47339-form-container" class="comment-form-container">
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

