+++
type = "question"
title = "Rendering of layer color oversight"
description = '''I think there is a oversight when rendering tunnels in OSM. Tunnels should have color of top layer, so it should look as we could just see trough eg. forest, and not like now when it seems like tunnel is cutting over some layer. To see what I mean look at this rendering of tunnel where it laps over ...'''
date = "2012-11-13T19:41:00Z"
lastmod = "2012-11-14T06:20:00Z"
weight = 17696
keywords = [ "tunnel", "rendering", "layer", "overlap" ]
aliases = [ "/questions/17696" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering of layer color oversight](/questions/17696/rendering-of-layer-color-oversight)

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
<span id="post-17696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17696-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I think there is a oversight when rendering tunnels in OSM. Tunnels should have color of top layer, so it should look as we could just see trough eg. forest, and not like now when it seems like tunnel is cutting over some layer. To see what I mean look at this rendering of tunnel where it laps over this historical layer and cuts one peas. If it would have same pink color, it would be much better.</p>
<p><a href="http://www.openstreetmap.org/index.html?mlat=43.852&amp;mlon=19.829&amp;zoom=18&amp;layers=B000FTF">http://www.openstreetmap.org/index.html?mlat=43.852&amp;mlon=19.829&amp;zoom=18&amp;layers=B000FTF</a></p>
<p>My question is, how to report/propose this, and who is in charge for layers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '12, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/1bbd575e2ed28bfaae0bbfcaf06e4b08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miller&#39;s gravatar image" />
<p><span>miller</span><br />
<span class="score" title="115 reputation points">115</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miller has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '12, 19:43</strong> </span></p>
</div>
</div>
<div id="comments-container-17696" class="comments-container">
&#10;</div>
<div id="comment-tools-17696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17696-form-container" class="comment-form-container">
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

<span id="17703"></span>

<div id="answer-container-17703" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17703-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="miller has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can report problems and suggestions <a href="https://trac.openstreetmap.org/">here</a>. Just log in with your regular OSM account, create a <a href="https://trac.openstreetmap.org/newticket">new ticket</a> and select <a href="http://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a> as <em>component</em>. Then explain your problem the same way you have don here.</p>
<p>When reporting problems or suggestions you can speed up the process by also providing a solution - in your specific case for example a patch to the renderer <a href="http://wiki.openstreetmap.org/wiki/Mapnik#Stylesheet">stylesheet</a> (the one used for the main page can be found <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/osm.xml">here</a>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '12, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17703" class="comments-container">
&#10;</div>
<div id="comment-tools-17703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17703-form-container" class="comment-form-container">
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

