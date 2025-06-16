+++
type = "question"
title = "Broken multipolygons?"
description = '''What is the story with the following multipolygons?  New Jersey, USA: 235961, 276888 Georgia, USA: 143646, 143639, 143464  JOSM and Mapnik seem to say they are legal, complete loops. However OSM Inspector says they are unclosed rings. What&#x27;s actually going on?'''
date = "2014-01-19T07:15:00Z"
lastmod = "2014-01-23T20:31:00Z"
weight = 29963
keywords = [ "multipolygon" ]
aliases = [ "/questions/29963" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Broken multipolygons?](/questions/29963/broken-multipolygons)

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
<span id="post-29963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29963-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the story with the following multipolygons?</p>
<ul>
<li>New Jersey, USA: <a href="https://www.openstreetmap.org/relation/235961">235961</a>, <a href="https://www.openstreetmap.org/relation/276888">276888</a></li>
<li>Georgia, USA: <a href="https://www.openstreetmap.org/relation/143646">143646</a>, <a href="https://www.openstreetmap.org/relation/143639">143639</a>, <a href="https://www.openstreetmap.org/relation/143464">143464</a></li>
</ul>
<p>JOSM and Mapnik seem to say they are legal, complete loops.<br />
However OSM Inspector says they are unclosed rings.</p>
<p>What's actually going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '14, 07:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ed0b2a6757c7515c4f9c529b2eb08ae3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eric22&#39;s gravatar image" />
<p><span>eric22</span><br />
<span class="score" title="401 reputation points">401</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eric22 has 2 accepted answers">50%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '14, 09:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-29963" class="comments-container">
&#10;</div>
<div id="comment-tools-29963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29963-form-container" class="comment-form-container">
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

<span id="29979"></span>

<div id="answer-container-29979" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29979-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eric22 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSM Inspector sometimes claims that a ring is not closed when instead the polygon has an inner ring touching an outer ring. This may occasionally confuse the ring building logic in OSMI, leading to the "ring not closed" complaint instead of correctly saying "inner touches outer".</p>
<p>I checked one of your examples and found exactly that: <a href="https://www.openstreetmap.org/relation/143464#map=16/33.2530/-84.5717">https://www.openstreetmap.org/relation/143464#map=16/33.2530/-84.5717</a> (right edge of the "hole" in the forest).</p>
<p>The data also contains a ton of useless tags that should never have been imported in the first place.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '14, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29979" class="comments-container">
<span id="30163"></span>
<div id="comment-30163" class="comment">
<div id="post-30163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That solves the problem for the Georgia multipolygons. But I can't find a similar problem with the New Jersey multipolygons. The most I can find is an inner ring touching another inner ring. Do you have any other ideas?</p>
</div>
<div id="comment-30163-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 20:31)</span> <span class="comment-user userinfo">eric22</span>
</div>
</div>
</div>
<div id="comment-tools-29979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29979-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29965"></span>

<div id="answer-container-29965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29965-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What is going one is that these (imported) multipolygons are bigger than you (or anyone else) can manage easily. You should split these at bigger roads (forest does not grow on highways) and deal with much smaller relations.</p>
<p>Otherwise you will waste some hours to find the mistake. Some seconds to fix it. And in a month or two you can do it again. In the meantime only few advanced contributors have the courage to modify such big relations. Meaning this place will evolve much slower than it could.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '14, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '14, 10:27</strong> </span></p>
</div>
</div>
<div id="comments-container-29965" class="comments-container">
<span id="29980"></span>
<div id="comment-29980" class="comment">
<div id="post-29980-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure I agree. If you open JOSM and choose "Download object" and the multipolygon number, you can work on a multipolygon easily without being confused by other objects. (You just have to be aware that your changes might affect other objects, and download those as necessary before editing, to avoid conflicts.)</p>
<p>I think Frederik is right that the problem is inner ways touching outer ways. The issue is some kind of multipolygon complexity, not the absolute number/length of ways...</p>
</div>
<div id="comment-29980-info" class="comment-info">
<span class="comment-age">(19 Jan '14, 20:15)</span> <span class="comment-user userinfo">eric22</span>
</div>
</div>
</div>
<div id="comment-tools-29965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29965-form-container" class="comment-form-container">
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

