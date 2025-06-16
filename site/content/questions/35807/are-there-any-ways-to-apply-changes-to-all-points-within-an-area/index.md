+++
type = "question"
title = "Are there any ways to apply changes to all points within an area?"
description = '''In the United States, we have ZIP codes which are large regions that have five digit numbers assigned to them for ease of sorting mail. I would like to be able to draw an area that is a ZIP code and then just apply it to every point made within that area (unless a user explicitly changed it, maybe)....'''
date = "2014-08-14T07:14:00Z"
lastmod = "2014-08-14T17:56:00Z"
weight = 35807
keywords = [ "points", "feature-request", "areas" ]
aliases = [ "/questions/35807" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are there any ways to apply changes to all points within an area?](/questions/35807/are-there-any-ways-to-apply-changes-to-all-points-within-an-area)

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
<span id="post-35807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the United States, we have <abbr title="Zoning Improvement Plan">ZIP</abbr> codes which are large regions that have five digit numbers assigned to them for ease of sorting mail. I would like to be able to draw an area that is a ZIP code and then just apply it to every point made within that area (unless a user explicitly changed it, maybe). Is there a way to do this? If not, is there some bug/feature request process for it? This feature would make my editing much faster when adding addresses.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-feature-request" rel="tag" title="see questions tagged &#39;feature-request&#39;">feature-request</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '14, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/f936a6af8335f7f14b9ea53ff536b921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin_-koavf-&#39;s gravatar image" />
<p><span>Justin_-koavf-</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin_-koavf- has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35807" class="comments-container">
&#10;</div>
<div id="comment-tools-35807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35807-form-container" class="comment-form-container">
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

<span id="35812"></span>

<div id="answer-container-35812" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35812-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, do not do this. While technically possible with the JOSM editor, it is just too easy to introduce mistakes.</p>
<p>It is sufficient to add the polygon to OpenStreetMap and tag it <code>boundary=postal_code</code> (and then <code>postal_code=xxxxx</code>).</p>
<p>While you may use the <code>addr:postcode</code> tag to specify the post code for a single address, if your true source data is just a polygon (and you assume that every address inside that polygon will have a certain post code), then map that polygon. Adding <code>addr:postcode</code> to all addresses inside the polygon would just be fake accuracy - you don't really <em>know</em> that all these addresses have that post code, you just assume it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '14, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-35812" class="comments-container">
<span id="35838"></span>
<div id="comment-35838" class="comment">
<div id="post-35838-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But I could do the same for something like <code>city</code> which is <em>definitely</em> Indianapolis. Alternately, the interface could be tweaked so that such-and-such ZIP code is the default but it can still be modified by users. (That's more of a feature request, though.)</p>
</div>
<div id="comment-35838-info" class="comment-info">
<span class="comment-age">(14 Aug '14, 17:45)</span> <span class="comment-user userinfo">Justin_-koavf-</span>
</div>
</div>
<span id="35839"></span>
<div id="comment-35839" class="comment">
<div id="post-35839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For cities, the usual thing is to bound then with an area or a relation containing ways that form an area.</p>
<p>Generally the geocoding tools that us OSM data are smart enough to know that everything in that area is part of the city. Interestingly, I don't see that boundary around Indianapolis. I hope that it is just because I am not searching properly. I see that you edited the node for the city 7 days ago.</p>
</div>
<div id="comment-35839-info" class="comment-info">
<span class="comment-age">(14 Aug '14, 17:54)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="35840"></span>
<div id="comment-35840" class="comment">
<div id="post-35840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See: <a href="/questions/35806/how-do-i-make-boundaries-for-a-city-with-enclaves-inside-of-it">https://help.openstreetmap.org/questions/35806/how-do-i-make-boundaries-for-a-city-with-enclaves-inside-of-it</a></p>
</div>
<div id="comment-35840-info" class="comment-info">
<span class="comment-age">(14 Aug '14, 17:56)</span> <span class="comment-user userinfo">Justin_-koavf-</span>
</div>
</div>
</div>
<div id="comment-tools-35812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35812-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35837"></span>

<div id="answer-container-35837" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35837-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the US ZIP codes are not actually areas, they are linear lists of addresses maintained by the post office for delivery purposes (I believe they are based on the actual mail delivery routes). The census people create pseudo areas for their purposes but because ZIP codes are not really areas there are places where the census assumed ZIP code areas are wrong.</p>
<p>So in addition to Frederik Ramm's comment that you could do the edit in JOSM but it would be error prone, I'd like to add that it could be error prone because you would be assuming an area for data which is not area based.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '14, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-35837" class="comments-container">
&#10;</div>
<div id="comment-tools-35837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35837-form-container" class="comment-form-container">
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

