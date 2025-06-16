+++
type = "question"
title = "How to find out why relation does not render in Mapnik (error)?"
description = '''I have added some inner boundaries to a relation (forest) that somehow have broken it. The relation is: https://www.openstreetmap.org/browse/relation/1364273 Previously, the multipoligon was shown correctly in Mapnik as a forest, but not anymore. I have even removed the new inner boundaries from the ...'''
date = "2012-11-10T23:13:00Z"
lastmod = "2012-11-11T00:23:00Z"
weight = 17639
keywords = [ "rendering", "relation", "mapnik", "error" ]
aliases = [ "/questions/17639" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find out why relation does not render in Mapnik (error)?](/questions/17639/how-to-find-out-why-relation-does-not-render-in-mapnik-error)

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
<span id="post-17639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17639-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have added some inner boundaries to a relation (forest) that somehow have broken it.</p>
<p>The relation is: <a href="https://www.openstreetmap.org/browse/relation/1364273">https://www.openstreetmap.org/browse/relation/1364273</a></p>
<p>Previously, the multipoligon was shown correctly in Mapnik as a forest, but not anymore.</p>
<p>I have even removed the new inner boundaries from the relation to try to restore it and get it to render correclty in Mapnik, but this has not helped. I suppose some of my changes from 10.11.2012 have damaged the realtion, because up to today my changes to the ralation were shown correctly.</p>
<p>Is there a straightforwad way to find out where the problem might lie?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '12, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d1d8f3c14b702d19ff4fd74e3b0d26af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BollWeevil&#39;s gravatar image" />
<p><span>BollWeevil</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BollWeevil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17639" class="comments-container">
&#10;</div>
<div id="comment-tools-17639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17639-form-container" class="comment-form-container">
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

<span id="17640"></span>

<div id="answer-container-17640" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17640-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BollWeevil has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Having had a look at the data three things were more or less straightforward:</p>
<ul>
<li>a multipolygon relation should not tagged as type=broad_leaved but type=multipolygon</li>
<li>one inner way did intersect itself</li>
<li>an inner way outside of the outer way doesn't make renderers happy, even if it is inside of another outer way, too.</li>
</ul>
<p>I fixed the above mentioned issues.</p>
<p>Afaik the JOSM editor is a little more advanced compared to Potlatch when it comes to editing relations and checking for errors. Maybe you want to have a look at it. (e.g. JOSM didn't show the area of the wood getting rendered as wood as long as there was no type=multipolygon)</p>
<p>Best regards<br />
malenki</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '12, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></p>
</div>
</div>
<div id="comments-container-17640" class="comments-container">
&#10;</div>
<div id="comment-tools-17640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17640-form-container" class="comment-form-container">
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

