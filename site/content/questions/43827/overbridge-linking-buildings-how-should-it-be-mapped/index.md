+++
type = "question"
title = "Overbridge linking buildings - how should it be mapped?"
description = '''This is a totally enclosed overbridge linking 2 buildings on the Waikato Hospital Campus. It crosses over, but does not connect with, Pembroke Street below. https://www.openstreetmap.org/way/354971865 At present it is tagged &#x27;highway=pedestrian&#x27; and &#x27;bridge=yes&#x27; based on its appearance on Bing imager...'''
date = "2015-06-28T04:51:00Z"
lastmod = "2015-06-30T17:40:00Z"
weight = 43827
keywords = [ "building", "overbridge", "tagging" ]
aliases = [ "/questions/43827" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overbridge linking buildings - how should it be mapped?](/questions/43827/overbridge-linking-buildings-how-should-it-be-mapped)

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
<span id="post-43827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a totally enclosed overbridge linking 2 buildings on the Waikato Hospital Campus. It crosses over, but does not connect with, Pembroke Street below. <a href="https://www.openstreetmap.org/way/354971865">https://www.openstreetmap.org/way/354971865</a></p>
<p>At present it is tagged 'highway=pedestrian' and 'bridge=yes' based on its appearance on Bing imagery and has given rise to this KeepRight alert <a href="http://keepright.ipax.at/report_map.php?schema=50&amp;error=78138632">http://keepright.ipax.at/report_map.php?schema=50&amp;error=78138632</a> - "way not connected with the rest of the map"</p>
<p>In my opinion the tag 'highway' isn't the most appropriate and I wonder if the feature would be better drawn as an area (linked to the buildings on either side) and tagged 'building=bridge' and 'layer=1' https://wiki.openstreetmap.org/wiki/Tag:building%3Dbridge</p>
<p>Advice appreciated please.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-overbridge" rel="tag" title="see questions tagged &#39;overbridge&#39;">overbridge</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '15, 04:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0b78593a39b9f71b9697697876327c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NZGraham&#39;s gravatar image" />
<p><span>NZGraham</span><br />
<span class="score" title="1814 reputation points"><span>1.8k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="49 badges"><span class="bronze">●</span><span class="badgecount">49</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NZGraham has 7 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-43827" class="comments-container">
&#10;</div>
<div id="comment-tools-43827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43827-form-container" class="comment-form-container">
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

<span id="43828"></span>

<div id="answer-container-43828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43828-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As usual you have always different (detailed) approaches on tagging in OSM. So for your quesion it's IMHO</p>
<ol>
<li>single way (highway=footway, bridge=yes, level=x, layer=x, covered=yes, ...)</li>
<li>closed way (building:part=yes, ...)</li>
</ol>
<p>The first one is easier and maybe more useful for indoor routing, while the second one is more likely for 3D rendering. For example I took the last one <a href="https://www.openstreetmap.org/way/243021976">here in Rostock</a> or <a href="https://www.openstreetmap.org/way/219515347">here in Schwerin</a> for a similar solid bridge/tunnel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '15, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-43828" class="comments-container">
<span id="43869"></span>
<div id="comment-43869" class="comment">
<div id="post-43869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even with indoor rendering, you want to have a building or building part around the indoor elements, so #2 is clearly the best option.</p>
</div>
<div id="comment-43869-info" class="comment-info">
<span class="comment-age">(30 Jun '15, 17:40)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-43828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43828-form-container" class="comment-form-container">
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

