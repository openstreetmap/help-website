+++
type = "question"
title = "How to add part of a way to a relation"
description = '''I am currently trying to document a local cycle and hiking path that is being built. Much of it is over existing paths, tracks and streets so I am using a relation with type=route. I have gathered several ways into a relation (type=route) and it is working well. I now need to add part of a way to th...'''
date = "2013-08-09T13:32:00Z"
lastmod = "2013-08-11T13:26:00Z"
weight = 25122
keywords = [ "route", "relation", "split", "way" ]
aliases = [ "/questions/25122" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to add part of a way to a relation](/questions/25122/how-to-add-part-of-a-way-to-a-relation)

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
<span id="post-25122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25122-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently trying to document a local cycle and hiking path that is being built. Much of it is over existing paths, tracks and streets so I am using a relation with type=route.</p>
<p>I have gathered several ways into a relation (type=route) and it is working well. I now need to add part of a way to the relation. In reality the cycle and hiking path travels down part of a road then leaves it. The road is currently a single way which is useful for tagging it so I didnt want to split the way.</p>
<p>Any suggestions on the best way to do this?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '13, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/b98fdc9e74e64247497c6f8e41b90614?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LongSkinneyLine&#39;s gravatar image" />
<p><span>LongSkinneyLine</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LongSkinneyLine has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25122" class="comments-container">
&#10;</div>
<div id="comment-tools-25122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25122-form-container" class="comment-form-container">
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

<span id="25123"></span>

<div id="answer-container-25123" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25123-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-25123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Split the way.</p>
<p>Splitting a road into multiple ways is absolutely fine and is necessary to map e.g. bridges, one-way sections, etc.</p>
<p>For example, the <a href="http://www.openstreetmap.org/browse/way/24299099">southern part</a> of Heathfield Road is part of the <a href="http://www.openstreetmap.org/browse/relation/10952">Capital Ring</a> walking route, while the <a href="http://www.openstreetmap.org/browse/way/19785408">northern part</a> is not.</p>
<p>If you want to be thorough, you can create a relation for the road itself (relation:route=road, for example <a href="http://www.openstreetmap.org/browse/relation/2303009">Trinity Road</a>), however most software will automatically consider adjoining road ways with the same name to be the same road anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '13, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/b55da07dea89fa675c7e2894c77f8024?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecatmur&#39;s gravatar image" />
<p><span>ecatmur</span><br />
<span class="score" title="151 reputation points">151</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecatmur has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '13, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-25123" class="comments-container">
<span id="25199"></span>
<div id="comment-25199" class="comment">
<div id="post-25199-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. Now I know that I am not breaking heaps of ways.</p>
</div>
<div id="comment-25199-info" class="comment-info">
<span class="comment-age">(11 Aug '13, 13:26)</span> <span class="comment-user userinfo">LongSkinneyLine</span>
</div>
</div>
</div>
<div id="comment-tools-25123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25123-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25124"></span>

<div id="answer-container-25124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25124-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding only parts of a way to a relation is currently not supported, the way has to be split as explained by ecatmur. However there is a proposal for the next API version to implement <a href="https://wiki.openstreetmap.org/wiki/API_v0.7#Segments_.28instead_of_fragmented_ways.29_-_Yes.2C_a_new_primitive.21">way segments</a>. With this feature way splitting could become obsolete.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '13, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25124" class="comments-container">
<span id="25145"></span>
<div id="comment-25145" class="comment">
<div id="post-25145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nice, is there a way to show support for a proposal?</p>
</div>
<div id="comment-25145-info" class="comment-info">
<span class="comment-age">(10 Aug '13, 05:23)</span> <span class="comment-user userinfo">he_the_great</span>
</div>
</div>
</div>
<div id="comment-tools-25124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25124-form-container" class="comment-form-container">
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

