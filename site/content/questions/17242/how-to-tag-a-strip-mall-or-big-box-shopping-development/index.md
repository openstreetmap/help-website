+++
type = "question"
title = "How to tag a strip mall or big-box shopping development?"
description = '''There are a number of places (in the US at least) where there is a named development that includes a mix of large standalone stores (&quot;big box&quot; stores), rows of storefronts, and standalone smaller stores or restaurants (&quot;outlot&quot; buildings), typically with a large sea of asphalt parking lot connecting...'''
date = "2012-10-28T22:53:00Z"
lastmod = "2012-10-29T22:10:00Z"
weight = 17242
keywords = [ "mall", "retail", "area" ]
aliases = [ "/questions/17242" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a strip mall or big-box shopping development?](/questions/17242/how-to-tag-a-strip-mall-or-big-box-shopping-development)

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
<span id="post-17242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17242-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are a number of places (in the US at least) where there is a named development that includes a mix of large standalone stores ("big box" stores), rows of storefronts, and standalone smaller stores or restaurants ("outlot" buildings), typically with a large sea of asphalt parking lot connecting them all. Smaller versions of this could be called a "strip mall".</p>
<p>It's no problem mapping and tagging the buildings and parking lots, but how should I tag the overall development? landuse=retail would seem to be more about zoning or a general area of a town, either unnamed or with a general name like "Downtown Farmville". But if I choose the tag marked "Shopping centre" in Potlatch2, it gets tagged shop=mall, which seems to be a different sort of thing (often indoors, or if outdoors, with inward-facing shops and pedestrian streets connecting them). More importantly, if it were tagging an actual (indoor) mall, I'd expect the tag to be on the building and exclude the parking lots, but the tag I'm seeking would be for the entire area of the development, including the parking.</p>
<p>So neither seems a perfect fit. Which is correct?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mall" rel="tag" title="see questions tagged &#39;mall&#39;">mall</span> <span class="post-tag tag-link-retail" rel="tag" title="see questions tagged &#39;retail&#39;">retail</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '12, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-17242" class="comments-container">
&#10;</div>
<div id="comment-tools-17242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17242-form-container" class="comment-form-container">
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

<span id="17281"></span>

<div id="answer-container-17281" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17281-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="blahedo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think an area tagged as <code>landuse=retail</code> is the best way of mapping this sort of thing. This tag can be used for any area that is mostly shops (along with associated car parking etc).</p>
<p>So it may be a general area of the town centre, containing a number of individual shops or shopping malls. Or it may be a distinct shopping development, with its own name and its own car park etc. Or it may even be a single out-of-town supermarket.</p>
<p>If the retail area has its own name, then tag that with <code>name=*</code></p>
<p>And of course you can map the individual shops within the shopping development. ie use the appropriate <code>shop=*</code> tag. Plus you can map building outlines, and any car parks or service roads etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '12, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17281" class="comments-container">
&#10;</div>
<div id="comment-tools-17281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17281-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17279"></span>

<div id="answer-container-17279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17279-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-17279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Blahedo, This question looks more or less at the earlier one, accidently ? But try to tag the area as follows landuse - commercial, thast should solve your problem. And please use multipolygones inner and outer just to make room for the shops or buildings. Happy cartering and ad all the different shops and developments later just as parking spaces. Hendrik</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '12, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-17279" class="comments-container">
&#10;</div>
<div id="comment-tools-17279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17279-form-container" class="comment-form-container">
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

