+++
type = "question"
title = "Building tiles server - part 2"
description = '''Hi everyone, sice a while i&#x27;ve been working on my own osm tiles server. I&#x27;ve made a huge progress since this -&amp;gt; https://help.openstreetmap.org/questions/58781/building-tiles-server Here are some pics showing the progress :)  Currenty i&#x27;m faceing another problem, this time with rendering multipoly...'''
date = "2017-11-09T19:20:00Z"
lastmod = "2017-11-13T13:54:00Z"
weight = 60525
keywords = [ "riverbank", "tileserver" ]
aliases = [ "/questions/60525" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Building tiles server - part 2](/questions/60525/building-tiles-server-part-2)

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
<span id="post-60525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60525-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>sice a while i've been working on my own osm tiles server. I've made a huge progress since this -&gt; <a href="/questions/58781/building-tiles-server">https://help.openstreetmap.org/questions/58781/building-tiles-server</a> Here are some pics showing the progress :) <img src="/upfiles/gw_map2.JPG" alt="alt text" /><img src="/upfiles/plock_map.JPG" alt="alt text" /></p>
<p>Currenty i'm faceing another problem, this time with rendering multipolygons, to be more precise I have a problem with getting nodes (points cordinates to be connected on the drawing) in the right order. Here is the pic showing the problem: <img src="/upfiles/riverbank_error.png" alt="alt text" /></p>
<p>Thats the riverbank build of ways. It seems i have all the nodes needed but they are (propobly) in the wrong order. Currently i'm grouping all the nodes by they orderId in the "way tag" and after that by the relationId of the "relation" so at the end I'm getting a list off all nodes in the relation (multipolygon) with x,y coordinates that are going to be connected on the drawing.</p>
<p>Aslo, I've noteced that if I draw each riverbanks way separatly the riverbanks shape looks correct, but it's not a polygon (programicaly), just a bunch of a separated lines, so I can't fill it with a color.</p>
<p>What am I missing? Already spend 4 days trying to figure it out, thank you for any comments :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '17, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/7ead15b2da5578cbe4ba69e985684623?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michal_poz&#39;s gravatar image" />
<p><span>michal_poz</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michal_poz has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '17, 19:30</strong> </span></p>
</div>
</div>
<div id="comments-container-60525" class="comments-container">
&#10;</div>
<div id="comment-tools-60525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60525-form-container" class="comment-form-container">
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

<span id="60526"></span>

<div id="answer-container-60526" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60526-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="michal_poz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Multipolygon relations are not guaranteed to be ordered. You have to write an algorithm that figures out which parts need to be connected in which sequence (and which are outer or inner rings). Writing such an algorithm is hard. There is <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon/Algorithm">a general description on the Wiki</a> and <a href="https://github.com/osmcode/libosmium/tree/4a49a23cab9c56a720cc5133b096863e3d4d6135/include/osmium/area">a good implementation in C++ in the Osmium library</a>. Another approach is the "Polygonizer" class in the C/C++ library GEOS (bindings exist for many languages), which takes a bunch of lines and constructs a proper polygon from them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '17, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-60526" class="comments-container">
<span id="60597"></span>
<div id="comment-60597" class="comment">
<div id="post-60597-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The above answer is correct, relation ways were not sorted in the right order. After implementing <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon/Algorithm">this algorithm</a> and some custom changes, everything seems to work correctly. Thank you for your help. And that is the current result<img src="/upfiles/riverbank.JPG" alt="alt text" /></p>
</div>
<div id="comment-60597-info" class="comment-info">
<span class="comment-age">(13 Nov '17, 13:54)</span> <span class="comment-user userinfo">michal_poz</span>
</div>
</div>
</div>
<div id="comment-tools-60526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60526-form-container" class="comment-form-container">
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

