+++
type = "question"
title = "Sites and buildings with multiple entrances having different address info"
description = '''Please advise how to code sites and buildings (e.g. large industrial or commercial) with multiple entrances, each having different street addresses (at least house numbers):  (Q1) each entrance a node (building=entrance) + address information? However, this does not appear on the map :-( (Q2) should...'''
date = "2011-08-17T10:46:00Z"
lastmod = "2011-08-17T12:23:00Z"
weight = 7147
keywords = [ "address" ]
aliases = [ "/questions/7147" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Sites and buildings with multiple entrances having different address info](/questions/7147/sites-and-buildings-with-multiple-entrances-having-different-address-info)

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
<span id="post-7147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7147-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please advise how to code sites and buildings (e.g. large industrial or commercial) with multiple entrances, each having different street addresses (at least house numbers):<br />
(Q1) each entrance a node (building=entrance) + address information? However, this does not appear on the map :-(<br />
(Q2) should this node be part of the site's / building's border line, or a separate POI? I think, an entrance is part of the building and thus should be part of the site's / building's surrounding polygon.<br />
(Q3) Sometimes (e.g. large commercial areas) have entrances with a street address associated with that entrance. Would this still be a building=entrance type of node? Should this node be part of the polygon surrounding the site? Or an extra node?<br />
(Q4) Large appartment buildings may also have several entrances with separate house numbers. I do not want to add all house numbers to the building's address since the building is quite long and I think it is important to know which end has which address. Again I would like to know: One POI for each entrance (building=entrance)? Should this node be part of the building's polygon? Or separate? Or should I still split the building into seperate buildings, one for each address?<br />
(Q5) Not every building can be split into separate building polygons, one for each address: There are large business buildings with several entrances which cannot (artificially) be split into several buildings.<br />
Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '11, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7821aef37df982816c514f07a993af01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wribln&#39;s gravatar image" />
<p><span>wribln</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wribln has one accepted answer">100%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7147" class="comments-container">
&#10;</div>
<div id="comment-tools-7147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7147-form-container" class="comment-form-container">
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

<span id="7151"></span>

<div id="answer-container-7151" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7151-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wribln has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>The <em>addr:housenumber</em> tag appears on the map. But the important thing is that routers and search engines finds the address.</li>
<li>You should add the <em>building=entrance</em> node to the building because entrances are part of the building outline. If you do not have the building outline you do not have to do so.</li>
<li>If the node is not an entrance to a <strong>building</strong> then you do not tag it as <em>building=entrance</em>. You can still tag the address to a node and even tag it with <em>barrier=gate</em> if that is more appropriate.</li>
<li>For longer stretches of housenumbers you can add them to a way that you tag with <em><a href="http://wiki.openstreetmap.org/wiki/Key:addr:interpolation">addr:intrapolation</a></em>.</li>
<li>That is where you use <em>building=entrance</em> to add several entrances and addresses to the same building. There is no reason there should be only one <em>building=entrance</em> assosiated with a single building.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '11, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '11, 12:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></br></p>
</div>
</div>
<div id="comments-container-7151" class="comments-container">
<span id="7154"></span>
<div id="comment-7154" class="comment">
<div id="post-7154-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this helps. As for #4: I understood addr:interpolation is only for ways but I have a situation where several long appartment buildings are not along the road but at a right angle to the road, worse: the street has an even-odd numbering scheme such that one building has housenumbers 10 (next to the road) and 12 (a little away from the road). According to your answer to #2, I will now add the entrances with their respective house numbers and hope they will show up on the map. Thank you, again.</p>
</div>
<div id="comment-7154-info" class="comment-info">
<span class="comment-age">(17 Aug '11, 12:23)</span> <span class="comment-user userinfo">wribln</span>
</div>
</div>
</div>
<div id="comment-tools-7151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7151-form-container" class="comment-form-container">
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

