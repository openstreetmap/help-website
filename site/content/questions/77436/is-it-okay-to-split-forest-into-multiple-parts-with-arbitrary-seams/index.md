+++
type = "question"
title = "Is it okay to split forest into multiple parts with arbitrary seams?"
description = '''I map in areas where there are very large forest covers. To make the mapping a bit more manageable I split the forest into several multipolygons which share borders, and my intention is that those seams should be invisible. I put the seams in arbitrary places, just focusing on making the least mess,...'''
date = "2020-11-07T21:17:00Z"
lastmod = "2020-11-09T09:18:00Z"
weight = 77436
keywords = [ "seams", "forest", "polygon" ]
aliases = [ "/questions/77436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it okay to split forest into multiple parts with arbitrary seams?](/questions/77436/is-it-okay-to-split-forest-into-multiple-parts-with-arbitrary-seams)

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
<span id="post-77436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77436-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I map in areas where there are very large forest covers. To make the mapping a bit more manageable I split the forest into several multipolygons which share borders, and my intention is that those seams should be invisible. I put the seams in arbitrary places, just focusing on making the least mess, meaning that I go around wetlands etc so I don't get the seam running through some other features.</p>
<p>This means that these forest polygon borders has no representation to anything in the real landscape, it's just a drawing technique. With the default OSM-Carto render this looks fine, as borders between forest polygons are invisible and it looks like a seamless forest just like I intend. However in some other renders, like here <a href="https://www.opentopomap.org/">https://www.opentopomap.org/</a> the borders are drawn as faint outlines, which make my polygon seams show up - not good!</p>
<p>So the question is, who's doing it wrong? Should I make sure that I have a single huge polygon for the forest (or hide the seams by putting them along roads etc), or is renders like opentopomap.org doing it wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-seams" rel="tag" title="see questions tagged &#39;seams&#39;">seams</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '20, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d04f4c51fab1e216224e5a7ae978b311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="torger&#39;s gravatar image" />
<p><span>torger</span><br />
<span class="score" title="220 reputation points">220</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="torger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77436" class="comments-container">
<span id="77446"></span>
<div id="comment-77446" class="comment">
<div id="post-77446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As an aside to this question, I quite often find myself splitting larger woodland areas because I've got notes that say "this bit is broadleaved trees and that bit needleleaved" or "this bit large conifers and that bit small ones".</p>
</div>
<div id="comment-77446-info" class="comment-info">
<span class="comment-age">(08 Nov '20, 17:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77448"></span>
<div id="comment-77448" class="comment">
<div id="post-77448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, if I would map very detailed depending on exactly the woodland type there would be more natural split points, however for the vast forest landscape I'm covering I don't really have that data at this point so I keep it simple and only differ between landuse=forest and natural=wood.</p>
<p>The forest here (taiga belt) is also quite uniform for large areas, so even with more detailed mapping there would be huge polygons with lots of inner members (mostly wetlands and screes) at times.</p>
</div>
<div id="comment-77448-info" class="comment-info">
<span class="comment-age">(08 Nov '20, 17:48)</span> <span class="comment-user userinfo">torger</span>
</div>
</div>
</div>
<div id="comment-tools-77436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77436-form-container" class="comment-form-container">
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

<span id="77438"></span>

<div id="answer-container-77438" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77438-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-77438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many mappers do the same thing you do for simplicity although it is not entirely correct; we try to map "one feature" as one OSM object, and if it is a very large forest then if you really want to do it "right" you would have to use one very large multipolygon for that.</p>
<p>You cannot make the assumption that renderers will use a specific rendering style, and drawing areas with an outline is not uncommon in cartography. A map style that chooses to draw outlines is certainly not "wrong". But on the other hand, renderers <em>could</em> also detect neighbouring polygons of the same kind and avoid drawing the outline there.</p>
<p>I'd try not to think of right and wrong in this situation. Map things in a way that works well for you, and we'll see where we go with that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '20, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77438" class="comments-container">
<span id="77445"></span>
<div id="comment-77445" class="comment">
<div id="post-77445-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Are there any technical disadvantages to having multipolygons with a large number of members? Once drawn I can quite easily merge them, but in the end I would probably end up with one forest polygon containing say 10,000 inner members (wetlands, screes etc, large natural area). So far I've tried to keep it say max 500 per polygon.</p>
</div>
<div id="comment-77445-info" class="comment-info">
<span class="comment-age">(08 Nov '20, 16:51)</span> <span class="comment-user userinfo">torger</span>
</div>
</div>
<span id="77463"></span>
<div id="comment-77463" class="comment">
<div id="post-77463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/19215/torger">@torger</a> Are they named or somewhat related? I would have hoped rivers, cliffs, and other barriers are plentiful enough to logically break them up.</p>
</div>
<div id="comment-77463-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 09:04)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="77464"></span>
<div id="comment-77464" class="comment">
<div id="post-77464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We have a lot of names in the landscape, but for smaller things, hills etc, large forest covers are generally nameless. It is indeed rather easy to find barriers in the form of roads, rivers are rather widely spaced so sometimes they will work, sometimes the polygon will be huge nevertheless. I could try and see though.</p>
<p>I have got the recommendation to not put seams on roads though as that is considered to make the map harder to maintain. So the strategy I've had so far is to make as low complexity (as few nodes as possible) on the seams, so rounding wetlands and curly rivers etc and make straight seams.</p>
</div>
<div id="comment-77464-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 09:18)</span> <span class="comment-user userinfo">torger</span>
</div>
</div>
</div>
<div id="comment-tools-77438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77438-form-container" class="comment-form-container">
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

