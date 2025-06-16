+++
type = "question"
title = "Given a polygon path, how do I find the number of tiles?"
description = '''Given a latitude and longitude, I can find the correct tile number. In Javascript like this function long2tile(lon,zoom) {  return (Math.floor((lon+180)/360*Math.pow(2,zoom))); } function lat2tile(lat,zoom) {  return (Math.floor((1-Math.log(Math.tan(lat*Math.PI/180) + 1/Math.cos(lat*Math.PI/180))/Ma...'''
date = "2015-02-03T13:21:00Z"
lastmod = "2015-02-07T01:33:00Z"
weight = 40761
keywords = [ "maptile", "javascript", "map" ]
aliases = [ "/questions/40761" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Given a polygon path, how do I find the number of tiles?](/questions/40761/given-a-polygon-path-how-do-i-find-the-number-of-tiles)

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
<span id="post-40761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40761-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given a latitude and longitude, I can find the correct tile number. In Javascript like <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#ECMAScript_.28JavaScript.2FActionScript.2C_etc..29">this</a></p>
<pre><code>function long2tile(lon,zoom)  {
    return (Math.floor((lon+180)/360*Math.pow(2,zoom)));
}
function lat2tile(lat,zoom)  {
    return (Math.floor((1-Math.log(Math.tan(lat*Math.PI/180) + 1/Math.cos(lat*Math.PI/180))/Math.PI)/2 *Math.pow(2,zoom))); 
}`</code></pre>
<p>But how can i find all tiles by given polygon?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maptile" rel="tag" title="see questions tagged &#39;maptile&#39;">maptile</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '15, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/fe1775d0c8e73239fe82ae8ad00e5a9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blu&#39;s gravatar image" />
<p><span>Blu</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '15, 05:44</strong> </span></p>
</div>
</div>
<div id="comments-container-40761" class="comments-container">
<span id="40783"></span>
<div id="comment-40783" class="comment">
<div id="post-40783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question is not quite clear, do you want to</p>
<ul>
<li><p>count how many tiles are needed to cover the polygon</p></li>
<li><p>get a list of the tile g the numbers covering the polygon</p></li>
<li><p>get, as a variant of the above, the tiles just for the polygon outline or do you need them for the area</p></li>
</ul>
</div>
<div id="comment-40783-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 21:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40761-form-container" class="comment-form-container">
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

<span id="40832"></span>

<div id="answer-container-40832" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40832-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question implicitly triggers another, even more important vector mapping related question, namely - is it necessary to pre-create the inner/trivial tiles of a polygon/area or those can be regenerated on the fly. I will try to answer both but on a generalized algorithmic level.<br />
I assume we have a common understanding of tiles, a tiled coordinate space, of tile referencing, when a point belongs to a tile (inside or on the left or top edge), a tile coverage ... and a like. Further, you have some basic and effective functions like: pointTOpolygon(...) that checks the relation of a given point to a given polygon (on, inside, outside); pointTOline(...) that checks the relation of a point to a (straight) line (on, one-side, other-side) ... and a like. So, the major algorithm steps are:<br />
1. Find the tile coverage/matrix of the polygon's bounding box (detect the tiles containing three corners of the box the rest of the coverage is then predefined). All the other tiles are of no interest further.<br />
2. For any edge-vectors of the polygon detect the tile candidates that might have common points with the edge. The candidates are quickly detectable (early filtering). They are never under, over, left or right to the vector.<br />
3. For any tile candidates check whether it has a common point with the edge-vector. If any two corner points are on the different sides of the line defined by the edge, or the edge is horizontal and has common points with the top tile-edge (excluding the top-right corner), or the polygon edge is vertical and has common points with the left tile edge (excluding the bottom-left corner) then mark the tile candidate as a member of the polygon tile coverage.<br />
Note that the tile coverage (the set of the marked tiles) is still organized in a row/column structure. In any of the tile rows the consecutive marked tiles are forming tile-runs. Any of the rows must have at least one run. If more runs exist they are separated by empty/unmarked tiles. Let us denote the runs R1, R2 ... Rn from the left to right in a tile row. Now, if you want the inner/trivial tiles (if any), the next procedure might be used to detect them:<br />
4. In any tile rows, where the number of runs is n&gt;1, start with the first pair of runs (Rf,Rs) from the left. Select a point P (example gratia, the central point) of the first empty/unmarked tile just to the right from Rf. If P is inside the polygon, then all the tiles between Rf and Rs are inner/trivial tiles (you may mark them). Reset n-=2 and if n&gt;1 take the pair to the right from Rs as (Rf,Rs). If P is not inside the polygon then all the tiles between Rf and Rs are outside the polygon and may be just ignored. In this case reset n-=1 and if n&gt;1 take the pair to the right of Rs as (Rf,Rs). Finally, if n&gt;1 just repeat the procedure from selecting the point P.<br />
Now, in this way you have all the none trivial tiles covering the polygon (area borders) and the trivial tiles that are inside the polygon (area).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '15, 01:33</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-40832" class="comments-container">
&#10;</div>
<div id="comment-tools-40832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40832-form-container" class="comment-form-container">
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

