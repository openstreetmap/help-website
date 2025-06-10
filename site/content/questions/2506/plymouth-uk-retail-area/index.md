+++
type = "question"
title = "Plymouth UK retail area"
description = '''What is the best way to edit the plymouth retail area. The red area around plymouth town centre is very inaccurate and covers areas that are not even retail districts. Is it best to delete the current area and then redraw the corrects areas?'''
date = "2011-01-28T10:19:00Z"
lastmod = "2011-04-21T10:30:00Z"
weight = 2506
keywords = [ "retail", "delete" ]
aliases = [ "/questions/2506" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Plymouth UK retail area](/questions/2506/plymouth-uk-retail-area)

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
<span id="post-2506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2506-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to edit the plymouth retail area. The red area around plymouth town centre is very inaccurate and covers areas that are not even retail districts. Is it best to delete the current area and then redraw the corrects areas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-retail" rel="tag" title="see questions tagged &#39;retail&#39;">retail</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '11, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/210c7f9b4b735c6f837df397cde66b35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mark29&#39;s gravatar image" />
<p><span>mark29</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mark29 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2506" class="comments-container">
&#10;</div>
<div id="comment-tools-2506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2506-form-container" class="comment-form-container">
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

<span id="2509"></span>

<div id="answer-container-2509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2509-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://www.openstreetmap.org/?lat=50.36973&amp;lon=-4.14497&amp;zoom=16&amp;layers=M">Here you mean?</a></p>
<p>In general I would say, if you see something that's wrong, feel free to dive in and fix it. You've seen the area and you know the area, so go for it.</p>
<p>What's actually happened here is that TimSC has slapped in the <code>landuse=retail</code> area quickly and crudely. It says <code>source=landsat</code>, though how he can tell that an area is retail from fuzzy landsat imagery is beyond me, and the area has Yahoo coverage, so why use landsat? So yes... <a href="http://www.openstreetmap.org/browse/way/40862740">way:40862740</a>. Just delete it.</p>
<p>Different people have adopted different approaches to mapping landuse within cities (<a href="http://wiki.openstreetmap.org/wiki/Land_use_and_areas_of_natural_land#Open_questions">Open questions</a>) I tend to think of landuse as a fairly broad brush-stroke designation of types of areas, while <code>building=yes</code> and shop type tags can be used for the fine grained detail. So I'd say <a href="http://www.openstreetmap.org/?lat=50.371922&amp;lon=-4.143373&amp;zoom=18&amp;layers=M">this bit of landuse around Armada way</a> is probably a bit finicky and detailed for landuse area, and should swapped to <code>building=yes</code>, with a single wider encompassing <code>landuse=retail</code> area.</p>
<p>But yes the big messy area to the south is at the other extreme, and should just be deleted to make way for more careful landuse mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '11, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '11, 11:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-2509" class="comments-container">
<span id="2511"></span>
<div id="comment-2511" class="comment">
<div id="post-2511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the advice Harry. I think i will go ahead and dive right in and fix the issues and make the area generally tidier and accurate to give a better impression of what actually exists. Hopefully it make the area easier to use. Its a real shame that it has been placed crudely as it just makes the area look messy and unrealistic</p>
<p>Thanks again for the advice</p>
</div>
<div id="comment-2511-info" class="comment-info">
<span class="comment-age">(28 Jan '11, 11:33)</span> <span class="comment-user userinfo">mark29</span>
</div>
</div>
<span id="4700"></span>
<div id="comment-4700" class="comment">
<div id="post-4700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking a lot better now I see. Nicely done!</p>
</div>
<div id="comment-4700-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 10:30)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-2509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2509-form-container" class="comment-form-container">
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

