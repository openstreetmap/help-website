+++
type = "question"
title = "Area not visible"
description = '''Hi, I mappeed this area: https://www.openstreetmap.org/way/292699788 But I can&#x27;t make it visible. What am I doing wrong? TIA Cheers, MarcoA'''
date = "2014-07-14T11:58:00Z"
lastmod = "2014-07-14T15:35:00Z"
weight = 34881
keywords = [ "mapnotvisible", "area" ]
aliases = [ "/questions/34881" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Area not visible](/questions/34881/area-not-visible)

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
<span id="post-34881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34881-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I mappeed this area: <a href="https://www.openstreetmap.org/way/292699788">https://www.openstreetmap.org/way/292699788</a> But I can't make it visible. What am I doing wrong?</p>
<p>TIA</p>
<p>Cheers, MarcoA</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnotvisible" rel="tag" title="see questions tagged &#39;mapnotvisible&#39;">mapnotvisible</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '14, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/457fe39db7132a8e147ce9fef4ac400b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marcoalici&#39;s gravatar image" />
<p><span>marcoalici</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marcoalici has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34881" class="comments-container">
&#10;</div>
<div id="comment-tools-34881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34881-form-container" class="comment-form-container">
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

<span id="34887"></span>

<div id="answer-container-34887" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34887-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-34887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your italian area is a closed way tagged with "area=yes" + "name=castello" which means "castle" in English. Based on Bing aerial imagery, your polygon seems to be the outer line of an historic castle. It this is the case, you just have to tag it with "<a href="http://wiki.openstreetmap.org/wiki/Buildings">building=yes</a>" (or building=castle) + "<a href="http://wiki.openstreetmap.org/wiki/Tag:historic%3Dcastle">historic=castle</a>" + "name=Castello".<br />
But if you do this, you will see a huge single block where in reality, there is a courtyard inside. To fix this, you will have to create a <a href="http://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon relation</a> with your "area" as outer ring and a new closed way representing the courtyard added in the relation with an "inner" role. Then, if you wish, you can move all tags from the outer ring (your current "area") to the multipolygon relation ("building" + "historic" + "name").</p>
<p>And with these tags, you don't need an "area=yes" tag because it is always the case for buildings. Basically, the tag "area=yes" is mainly used for "highway's" on closed ways only to determine if it's representing a loop (like a race track) or an uniform surface/area (area=yes).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '14, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jul '14, 13:28</strong> </span></p>
</div>
</div>
<div id="comments-container-34887" class="comments-container">
<span id="34890"></span>
<div id="comment-34890" class="comment">
<div id="post-34890-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>(in case it wasn't obvious) I'm guessing that the "area=yes" tag was added by the iD editor and not chosen by the mapper here.</p>
<p>But yes; as Pieren says you need to map things <em>as</em> something; just giving an unidentified feature a name doesn't work. Unfortunately this is something that the iD editor UI doesn't really make clear.</p>
</div>
<div id="comment-34890-info" class="comment-info">
<span class="comment-age">(14 Jul '14, 13:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34887-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34885"></span>

<div id="answer-container-34885" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34885-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The use of the area needs to be designated, you've just defined an area without defining it's purpose. Could it be landuse=residential? The area tag would then be redundant and should be removed. I think the name of the area ought to be capitalised as well. Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '14, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-34885" class="comments-container">
<span id="34895"></span>
<div id="comment-34895" class="comment">
<div id="post-34895-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>landuse=residential worked! Thank you!</p>
</div>
<div id="comment-34895-info" class="comment-info">
<span class="comment-age">(14 Jul '14, 14:31)</span> <span class="comment-user userinfo">marcoalici</span>
</div>
</div>
<span id="34899"></span>
<div id="comment-34899" class="comment">
<div id="post-34899-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Be careful : replacing "area=yes" by "landuse=residential" will fix your rendering issue. But is it semantically correct ? Is "Castello" the name of a residential area or the name of a building block being an historic castle ?</p>
</div>
<div id="comment-34899-info" class="comment-info">
<span class="comment-age">(14 Jul '14, 15:35)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-34885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34885-form-container" class="comment-form-container">
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

