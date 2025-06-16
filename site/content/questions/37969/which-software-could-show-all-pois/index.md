+++
type = "question"
title = "Which software could show all POIs"
description = '''I found that JOSM is able to edit/show POIs like mountain ridge and pass, but they are not showed on OSM site. Which viewer is able to show such points on map? '''
date = "2014-10-26T16:17:00Z"
lastmod = "2014-10-26T23:20:00Z"
weight = 37969
keywords = [ "mapviewer", "poi" ]
aliases = [ "/questions/37969" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which software could show all POIs](/questions/37969/which-software-could-show-all-pois)

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
<span id="post-37969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37969-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found that JOSM is able to edit/show POIs like mountain ridge and pass, but they are not showed on OSM site. Which viewer is able to show such points on map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapviewer" rel="tag" title="see questions tagged &#39;mapviewer&#39;">mapviewer</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '14, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/84484a62a74894d7f4efe0aa0d30458c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Misher&#39;s gravatar image" />
<p><span>Misher</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Misher has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37969" class="comments-container">
<span id="37978"></span>
<div id="comment-37978" class="comment">
<div id="post-37978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This previous question re mountain pass may help.<br />
<a href="/questions/27370/mountain-pass-not-showing-on-map.">https://help.openstreetmap.org/questions/27370/mountain-pass-not-showing-on-map.</a><br />
I know of no map version that renders all data, though a map that renders everything in more data sparse areas would be useful.</p>
</div>
<div id="comment-37978-info" class="comment-info">
<span class="comment-age">(26 Oct '14, 22:11)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-37969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37969-form-container" class="comment-form-container">
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

<span id="37980"></span>

<div id="answer-container-37980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37980-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tend to use the combination of taginfo and overpass to show where arbitary things are on the map.</p>
<p>First, I'd look for where the thing that I'm looking for occurs as a value. In this case:</p>
<p><a href="http://taginfo.openstreetmap.org.uk/search?q=ridge#values">http://taginfo.openstreetmap.org.uk/search?q=ridge#values</a></p>
<p>(I'm using taginfo.org.uk because I want to see examples in the UK; if I wanted to search internationally I'd use taginfo.org).</p>
<p>Then click on "value" which takes us to:</p>
<p><a href="http://taginfo.openstreetmap.org.uk/tags/natural=ridge">http://taginfo.openstreetmap.org.uk/tags/natural=ridge</a></p>
<p>and then click on "Overpass turbo", move to an area I'm interested in and run the query, which takes us to:</p>
<p><a href="http://overpass-turbo.eu/?key=natural&amp;value=ridge&amp;template=key-value">http://overpass-turbo.eu/?key=natural&amp;value=ridge&amp;template=key-value</a></p>
<p>In this case there's probably some "mountaineer" rendering on an external map somewhere that shows this info on tiles, but this is a general solution for <a href="http://overpass-turbo.eu/?w=%22panda%22%3D*+global&amp;R">things that are unlikely to be rendered anywhere</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '14, 23:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-37980" class="comments-container">
&#10;</div>
<div id="comment-tools-37980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37980-form-container" class="comment-form-container">
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

