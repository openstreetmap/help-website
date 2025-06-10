+++
type = "question"
title = "Abandoned buildings don&#x27;t render when using the prefix."
description = '''In a place I know, there is an abandoned factory. iD tags the site as man_made=works. Inside the site there are 2 buildings, which are tagged as building=industrial. Since the place is abandoned, I followed the guidelines in the wiki article and added the prefix abandoned: to the buildings. However,...'''
date = "2019-03-27T09:01:00Z"
lastmod = "2019-03-27T14:07:00Z"
weight = 68507
keywords = [ "abandoned", "factory" ]
aliases = [ "/questions/68507" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Abandoned buildings don't render when using the prefix.](/questions/68507/abandoned-buildings-dont-render-when-using-the-prefix)

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
<span id="post-68507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68507-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a place I know, there is an abandoned factory. iD tags the site as man_made=works. Inside the site there are 2 buildings, which are tagged as building=industrial. Since the place is abandoned, I followed the guidelines in the wiki <a href="https://wiki.openstreetmap.org/wiki/Key:abandoned:">article</a> and added the prefix abandoned: to the buildings. However, they don't render on the map. Since the buildings are there, how can I make them render but still use the prefix correctly? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-abandoned" rel="tag" title="see questions tagged &#39;abandoned&#39;">abandoned</span> <span class="post-tag tag-link-factory" rel="tag" title="see questions tagged &#39;factory&#39;">factory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '19, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/78214cb50496534a77097dcca62350e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimcoun&#39;s gravatar image" />
<p><span>jimcoun</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimcoun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68507" class="comments-container">
&#10;</div>
<div id="comment-tools-68507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68507-form-container" class="comment-form-container">
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

<span id="68511"></span>

<div id="answer-container-68511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68511-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>abandoned:</code> prefix only works for features that don't exist in their original state. Since the building still exists you should tag it as <code>building=industrial</code>. Instead, replace the <code>man_made=works</code> with <code>abandoned:man_made=works</code> on the landuse way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '19, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68511" class="comments-container">
<span id="68512"></span>
<div id="comment-68512" class="comment">
<div id="post-68512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried to do this, but the area is not highlighted when the maps are rendered. One combination that works is man_made=works, abandoned:industrial=factory. Is this correct tagging?</p>
</div>
<div id="comment-68512-info" class="comment-info">
<span class="comment-age">(27 Mar '19, 13:13)</span> <span class="comment-user userinfo">jimcoun</span>
</div>
</div>
<span id="68513"></span>
<div id="comment-68513" class="comment">
<div id="post-68513-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Because typical renderers (or rather typical rendering stylesheets) don't support lifecycle prefixes, with few exceptions. However we are not <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>. So make sure your tagging is correct and don't get distracted by a missing rendering. <code>man_made=works</code> is only correct if this production plant / factory is still in use.</p>
</div>
<div id="comment-68513-info" class="comment-info">
<span class="comment-age">(27 Mar '19, 13:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68514"></span>
<div id="comment-68514" class="comment">
<div id="post-68514-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand, however in this page <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dworks,">https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dworks,</a> it doesn't mention that the factory must be operating. I feel that landuse=industrial, abandoned:industrial=factory, abandoned:man_made=works is correct. Sorry for possible mistakes, I am a very new user and I want to understand tagging correctly.</p>
</div>
<div id="comment-68514-info" class="comment-info">
<span class="comment-age">(27 Mar '19, 13:34)</span> <span class="comment-user userinfo">jimcoun</span>
</div>
</div>
<span id="68516"></span>
<div id="comment-68516" class="comment">
<div id="post-68516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In my opinion, using <code>man_made=works</code> only in case of a factory being still in use is a somewhat implicit assumption, also originating from the lifecycle prefix tags. A closed shop also won't get tagged as <code>shop=*</code> but as <code>disused:shop=*</code> instead. I guess <code>landuse=industrial</code>, <code>abandoned:industrial=factory</code>, <code>abandoned:man_made=works</code> is a valid approach.</p>
</div>
<div id="comment-68516-info" class="comment-info">
<span class="comment-age">(27 Mar '19, 13:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68517"></span>
<div id="comment-68517" class="comment">
<div id="post-68517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for the answers and explanations!</p>
</div>
<div id="comment-68517-info" class="comment-info">
<span class="comment-age">(27 Mar '19, 14:07)</span> <span class="comment-user userinfo">jimcoun</span>
</div>
</div>
</div>
<div id="comment-tools-68511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68511-form-container" class="comment-form-container">
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

