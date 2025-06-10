+++
type = "question"
title = "Relation type boundary or multipolygon"
description = '''hi  I wanted to edit a large sandy area divided into small areas, is it right that I:  - set Relation type as boundary instead of multipolygon for small and large areas  - put tag &quot;natural:sand&quot; for large area  - add small areas as members to large area and set it as &quot;subarea&quot;  is that right or i ca...'''
date = "2021-01-11T07:00:00Z"
lastmod = "2021-01-11T10:17:00Z"
weight = 78321
keywords = [ "relation", "boundary", "type", "subarea", "multipolygon" ]
aliases = [ "/questions/78321" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Relation type boundary or multipolygon](/questions/78321/relation-type-boundary-or-multipolygon)

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
<span id="post-78321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi I wanted to edit a large sandy area divided into small areas, is it right that I:<br />
- set Relation type as boundary instead of multipolygon for small and large areas<br />
- put tag "natural:sand" for large area<br />
- add small areas as members to large area and set it as "subarea"</p>
<p>is that right or i can not use boundary type for natural places, and is it right to use "subarea" as Role to members of multipolygon?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-subarea" rel="tag" title="see questions tagged &#39;subarea&#39;">subarea</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '21, 07:00</strong></p>
<img src="https://secure.gravatar.com/avatar/1bff5fc63d9919afbc3969b09d7b8d35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abdullah%20abdulrhman&#39;s gravatar image" />
<p><span>abdullah abd...</span><br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abdullah abdulrhman has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '21, 07:24</strong> </span></p>
</div>
</div>
<div id="comments-container-78321" class="comments-container">
&#10;</div>
<div id="comment-tools-78321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78321-form-container" class="comment-form-container">
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

<span id="78324"></span>

<div id="answer-container-78324" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78324-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="abdullah abdulrhman has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The multipolygon tagging does not allow for a hierarchy. If you have serveral patches of sand, I would not even use a multipolygon at all - just tag them as individual sand areas. If they all share a common characteristic - e.g. there are 20 patches of sand and together they are called the "Someplace Sands", then it makes sense to build a multipolygon relation with that name and make the individual bits a member. Do not use boundary tags for sand areas unless they are some form of protected area or a country-sized named feature.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '21, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-78324" class="comments-container">
<span id="78326"></span>
<div id="comment-78326" class="comment">
<div id="post-78326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you<br />
and i did used multipolygon because the area have inner and outer lines<br />
if you have some time lock at this:<br />
<a href="https://overpass-turbo.eu/s/12eT">https://overpass-turbo.eu/s/12eT</a></p>
</div>
<div id="comment-78326-info" class="comment-info">
<span class="comment-age">(11 Jan '21, 10:17)</span> <span class="comment-user userinfo">abdullah abd...</span>
</div>
</div>
</div>
<div id="comment-tools-78324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78324-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78322"></span>

<div id="answer-container-78322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78322-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The type=boundary is reserved for use to define official boundaries, for example, those of towns, states and other so-called administrative boundaries, national parks, wildlife refuges, etc.</p>
<p>Natural areas do not need a boundary tag at all. Members of multipolygons that define natural areas need use no role other than inner or outer as the case may be. For example, a typical small areas inside a larger multipolygon might be a wetland inside a wooded area. That will have role inner while the containing multipolygon would have role outer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '21, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '21, 08:50</strong> </span></p>
</div>
</div>
<div id="comments-container-78322" class="comments-container">
<span id="78323"></span>
<div id="comment-78323" class="comment">
<div id="post-78323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, but the problem we have in Saudi Arabia is that there are large sand areas, from which small areas follow that large area and they are all sand, how do I make a dependent multipolygon to the large multipolygon is it right to but multipolygon inside multipolygon with out link it with "subarea" role ?</p>
</div>
<div id="comment-78323-info" class="comment-info">
<span class="comment-age">(11 Jan '21, 09:13)</span> <span class="comment-user userinfo">abdullah abd...</span>
</div>
</div>
</div>
<div id="comment-tools-78322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78322-form-container" class="comment-form-container">
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

