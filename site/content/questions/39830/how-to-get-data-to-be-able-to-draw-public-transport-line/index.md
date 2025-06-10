+++
type = "question"
title = "how to get data to be able to draw public transport line"
description = '''I need to extract information (latitude / longitude) from all public transport (bus stop and way) from a region. I want to draw public transport line like this :http://xn--pnvkarte-m4a.de/?zoom=14&amp;amp;lat=46.51856&amp;amp;lon=6.62505&amp;amp;layers=TBTTT I try with http://www.openstreetmap.org/export#map=18...'''
date = "2014-12-25T20:56:00Z"
lastmod = "2014-12-26T09:27:00Z"
weight = 39830
keywords = [ "development" ]
aliases = [ "/questions/39830" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get data to be able to draw public transport line](/questions/39830/how-to-get-data-to-be-able-to-draw-public-transport-line)

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
<span id="post-39830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to extract information (latitude / longitude) from all public transport (bus stop and way) from a region. I want to draw public transport line like this :<a href="http://xn--pnvkarte-m4a.de/?zoom=14&amp;lat=46.51856&amp;lon=6.62505&amp;layers=TBTTT">http://xn--pnvkarte-m4a.de/?zoom=14&amp;lat=46.51856&amp;lon=6.62505&amp;layers=TBTTT</a></p>
<p>I try with <a href="http://www.openstreetmap.org/export#map=18/46.52906/6.59971&amp;layers=T">http://www.openstreetmap.org/export#map=18/46.52906/6.59971&amp;layers=T</a> but didn't have all the relation (way), neither with <a href="http://overpass-turbo.eu/s/6Fp">http://overpass-turbo.eu/s/6Fp</a> What is the best practice to do that ?</p>
<p>I just need to have stop node and way with coordonate of the point and the name of the bus/tram/train line</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Dec '14, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/dc4a868d06aef17ec554147cc7f91509?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f3t&#39;s gravatar image" />
<p><span>f3t</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f3t has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Dec '14, 20:57</strong> </span></p>
</div>
</div>
<div id="comments-container-39830" class="comments-container">
<span id="39832"></span>
<div id="comment-39832" class="comment">
<div id="post-39832-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>do you know : <a href="http://overpass-api.de/public_transport.html">http://overpass-api.de/public_transport.html</a> ? Unfortunately it does not mention the queries it executes.</p>
</div>
<div id="comment-39832-info" class="comment-info">
<span class="comment-age">(25 Dec '14, 21:36)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="39833"></span>
<div id="comment-39833" class="comment">
<div id="post-39833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes but with this query <a href="http://overpass-api.de/api/sketch-line?network=TL&amp;ref=17&amp;operator=">http://overpass-api.de/api/sketch-line?network=TL&amp;ref=17&amp;operator=</a> I have only the Public Transport Line Diagram when I try Public Transport Line Map, i have nothing <a href="http://78.46.81.38/api/draw-line?network=network&amp;ref=ref">http://78.46.81.38/api/draw-line?network=network&amp;ref=ref</a> I dont need time juste geolocation :)</p>
</div>
<div id="comment-39833-info" class="comment-info">
<span class="comment-age">(25 Dec '14, 22:34)</span> <span class="comment-user userinfo">f3t</span>
</div>
</div>
</div>
<div id="comment-tools-39830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39830-form-container" class="comment-form-container">
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

<span id="39836"></span>

<div id="answer-container-39836" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39836-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are looking for is more along the lines of <a href="http://overpass-turbo.eu/s/6Gd">http://overpass-turbo.eu/s/6Gd</a> Which simply fetches all elements of any trolleybus route relation. You will need to request the result to be in a format that you can easily process further and potentially request more information (name etc) in the query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '14, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '14, 09:27</strong> </span></p>
</div>
</div>
<div id="comments-container-39836" class="comments-container">
&#10;</div>
<div id="comment-tools-39836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39836-form-container" class="comment-form-container">
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

