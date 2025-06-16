+++
type = "question"
title = "In JOSM how do I create a multipolygon with multiple adjacent &quot;inners&quot;"
description = '''I have the following 3 polygons: ABCD, DEFI, IFGH. These are arranged as shown here: A-------------B | | | D-----E | | | | | | I-----F | | | | | | H-----G | | | C-------------D  I want to create a multi polygon with ABCD as the outer and DEFGHI as the inner. If I select all three polygons and use th...'''
date = "2016-07-13T14:19:00Z"
lastmod = "2016-07-14T20:39:00Z"
weight = 50892
keywords = [ "josm", "intersection", "polygon", "multipolygon" ]
aliases = [ "/questions/50892" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [In JOSM how do I create a multipolygon with multiple adjacent "inners"](/questions/50892/in-josm-how-do-i-create-a-multipolygon-with-multiple-adjacent-inners)

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
<span id="post-50892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50892-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the following 3 polygons: ABCD, DEFI, IFGH. These are arranged as shown here:</p>
<pre><code>A-------------B
|             |
|   D-----E   |
|   |     |   |
|   I-----F   |
|   |     |   |
|   H-----G   |
|             |
C-------------D</code></pre>
<p>I want to create a multi polygon with ABCD as the outer and DEFGHI as the inner. If I select all three polygons and use the "Create Multipolygon" tool (Ctrl+B) I then get a validation warning saying "Intersection between multipolygon ways". I understand why this occurs, the two inner polygons share the edge FI.</p>
<p><strong>How do I correctly create the desire multipolygon?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '16, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/b372136094bdbf5901a66c8fe1b3a548?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BarnsleyOli&#39;s gravatar image" />
<p><span>BarnsleyOli</span><br />
<span class="score" title="91 reputation points">91</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BarnsleyOli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50892" class="comments-container">
&#10;</div>
<div id="comment-tools-50892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50892-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="50898"></span>

<div id="answer-container-50898" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50898-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It works perfectly in JOSM. Draw a polygon ABDCA tag it as natural=wood. Inside that polygon draw polygon DEFID tag it as natural=beach, also draw polygon IFGHI tag it as natural=water, water=lake. Select all three polygons click 'create multipolygon. Check the relation editor to make sure the inners and outer are correct (adjust if neccessary). Job done!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '16, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '16, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-50898" class="comments-container">
<span id="50904"></span>
<div id="comment-50904" class="comment">
<div id="post-50904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"adjust if neccessary, Job done!" is a nice solution for various kinds of problems ;)</p>
</div>
<div id="comment-50904-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 08:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50898-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50895"></span>

<div id="answer-container-50895" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50895-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an example of this in <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Relation:multipolygon</a> .<br />
See 'touching inner rings' and can be a valid osm polygon.<br />
I haven't mapped one yet, so unsure what problem needs to be overcome to be accepted by the validator. Possibly you need to complete each polygon by reusing the nodes on the shared boundary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '16, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '16, 15:02</strong> </span></p>
</div>
</div>
<div id="comments-container-50895" class="comments-container">
<span id="50897"></span>
<div id="comment-50897" class="comment">
<div id="post-50897-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a> Thanks, I had already read this and the talk page (which gives the example of a lake with a beach both inside a wood). However I couldn't find any advice on what to do where the phrase "The boundary between farmland and lake does not belong to the forest" applies.</p>
</div>
<div id="comment-50897-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 15:20)</span> <span class="comment-user userinfo">BarnsleyOli</span>
</div>
</div>
</div>
<div id="comment-tools-50895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50895-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50896"></span>

<div id="answer-container-50896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi BarnsleyOli, try to make 2 complete inners DEFI &amp; FGHI or try the trick and draw them at a large scale or zoom in and align FI and IF next to each other closely. I presume that you read the Multi pages instructions ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '16, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-50896" class="comments-container">
&#10;</div>
<div id="comment-tools-50896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50896-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50902"></span>

<div id="answer-container-50902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50902-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-50902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A possible solution to avoid touching inner ways is to split inner polygons into three segments, creating three multipolygons as follows:</p>
<p>1) ABCDA - outer IDEF - inner FGHI - inner</p>
<p>2) IDEF - outer FI - outer</p>
<p>3) FGHI - outer FI - outer</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '16, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/b75c397321b010a8a70f44ab78e7bb44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alecs01&#39;s gravatar image" />
<p><span>Alecs01</span><br />
<span class="score" title="1371 reputation points"><span>1.4k</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alecs01 has 6 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-50902" class="comments-container">
<span id="50907"></span>
<div id="comment-50907" class="comment">
<div id="post-50907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While this uses 3 relations, it would work fine, so I don't understand the down-vote.</p>
</div>
<div id="comment-50907-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 18:29)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="50908"></span>
<div id="comment-50908" class="comment">
<div id="post-50908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't vote it down, but I have found that relations mapped that way are pretty unmanageable.</p>
<p>The problem is the abstraction - "IDEF" and "IF" are just line segments, and don't actually match anything in the real world, whereas DEFID, FGHIF and even DEFGHID all do represent physical features.</p>
</div>
<div id="comment-50908-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 19:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50909"></span>
<div id="comment-50909" class="comment">
<div id="post-50909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> it adds complexity for sure, it's an edge case to me, slightly better than two touching inner rings. I wasn't aware before there was some discussion on the topic here, and not much consensus: <a href="https://wiki.openstreetmap.org/wiki/Talk:Relation:multipolygon#Touching_inner_rings">https://wiki.openstreetmap.org/wiki/Talk:Relation:multipolygon#Touching_inner_rings</a></p>
</div>
<div id="comment-50909-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 20:39)</span> <span class="comment-user userinfo">Alecs01</span>
</div>
</div>
</div>
<div id="comment-tools-50902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50902-form-container" class="comment-form-container">
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

