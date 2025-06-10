+++
type = "question"
title = "What type of wood should I use, and why doesn&#x27;t a forest show up in mapnik"
description = '''In http://www.openstreetmap.org/?lat=46.81373&amp;amp;lon=11.75608&amp;amp;zoom=16&amp;amp;layers=M, what is north should be covered in wood (same as what is in the south, the only thing i changed was adding some nodes on the contour to match it better with the current situation (previously, it was very crude)....'''
date = "2010-10-11T08:40:00Z"
lastmod = "2010-10-11T11:31:00Z"
weight = 1116
keywords = [ "wood", "renderer", "tagging" ]
aliases = [ "/questions/1116" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What type of wood should I use, and why doesn't a forest show up in mapnik](/questions/1116/what-type-of-wood-should-i-use-and-why-doesnt-a-forest-show-up-in-mapnik)

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
<span id="post-1116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In <a href="http://www.openstreetmap.org/?lat=46.81373&amp;lon=11.75608&amp;zoom=16&amp;layers=M">http://www.openstreetmap.org/?lat=46.81373&amp;lon=11.75608&amp;zoom=16&amp;layers=M</a>, what is north should be covered in wood (same as what is in the south, the only thing i changed was adding some nodes on the contour to match it better with the current situation (previously, it was very crude). Now it doesn't show up at all in mapnik, but in osmarenderer it does.</p>
<p>Then there is another thing with wood besides the river, which is <code>wood=mixed</code>, but is it also to be tagged <code>landuse=forest</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wood" rel="tag" title="see questions tagged &#39;wood&#39;">wood</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '10, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/720ecc66aa0d49f61a12c4d9e526e66f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Roalter&#39;s gravatar image" />
<p><span>Alexander Ro...</span><br />
<span class="score" title="276 reputation points">276</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Roalter has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '10, 17:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-1116" class="comments-container">
&#10;</div>
<div id="comment-tools-1116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1116-form-container" class="comment-form-container">
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

<span id="1122"></span>

<div id="answer-container-1122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1122-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That forest area was in two parts(small section near Lienerweg was apart from main part). Fixed it.</p>
<p>Forest areas should be tagged as <code>landuse=forest</code> (if forest is being maintained) or <code>natural=wood</code> (when it is not maintained). On both cases use <code>wood=*</code> to indicate what type of trees grow in that forest.</p>
<p>Another strange (and wrong) thing in that area is usage of <code>layer=*</code> tag. It should not be used on areas like landuse and natural. Take a look at: <a href="http://wiki.openstreetmap.org/wiki/Key:layer">http://wiki.openstreetmap.org/wiki/Key:layer</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '10, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '10, 17:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-1122" class="comments-container">
<span id="1123"></span>
<div id="comment-1123" class="comment">
<div id="post-1123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for fixing it (I cannot do it from my current computer).</p>
<p>Regarding the layer thing: The entire landuse=farmland/forest seem to be imported by someone from some official datasets, and they are consistently tagged as layer=-2 (which apparently is used for doing some 'layering' as you would do in a vector drawing application. I started drawing things with no overlap, but with common borders, as I reckon this is the correct way to do it.</p>
</div>
<div id="comment-1123-info" class="comment-info">
<span class="comment-age">(11 Oct '10, 11:31)</span> <span class="comment-user userinfo">Alexander Ro...</span>
</div>
</div>
</div>
<div id="comment-tools-1122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1122-form-container" class="comment-form-container">
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

