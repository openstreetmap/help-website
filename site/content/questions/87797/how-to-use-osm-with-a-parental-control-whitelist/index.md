+++
type = "question"
title = "How to use OSM with a parental control whitelist?"
description = '''Hi, I use CTparental with Linux Mint on my computer to limit access of young people to the Web with a whitelist. I think that it is important that they use OSM and also that they learn the OMS&#x27; philosophy. Unfortunately with these two items in my whitelist  openstreetmap.org  openstreetmap.org/asset...'''
date = "2023-09-04T15:17:00Z"
lastmod = "2023-09-08T15:47:00Z"
weight = 87797
keywords = [ "layers", "whitelist", "itinerary" ]
aliases = [ "/questions/87797" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to use OSM with a parental control whitelist?](/questions/87797/how-to-use-osm-with-a-parental-control-whitelist)

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
<span id="post-87797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87797-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I use CTparental with Linux Mint on my computer to limit access of young people to the Web with a whitelist. I think that it is important that they use OSM and also that they learn the OMS' philosophy. Unfortunately with these two items in my whitelist</p>
<p>openstreetmap.org</p>
<p>openstreetmap.org/assets</p>
<p>only the standard layer can be used, and it is not possible to obtain a trip itinerary. Does-it exist a complete list of all the URL for completely whitelisting OSM? Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-whitelist" rel="tag" title="see questions tagged &#39;whitelist&#39;">whitelist</span> <span class="post-tag tag-link-itinerary" rel="tag" title="see questions tagged &#39;itinerary&#39;">itinerary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '23, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d2680ec0a31ee02ee1dd43542eb4367a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Superdocious&#39;s gravatar image" />
<p><span>Superdocious</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Superdocious has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87797" class="comments-container">
&#10;</div>
<div id="comment-tools-87797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87797-form-container" class="comment-form-container">
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

<span id="87798"></span>

<div id="answer-container-87798" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87798-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-87798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would need to add:</p>
<ul>
<li><p>nominatim.openstreetmap.org (geo search)</p></li>
<li><p>routing.openstreetmap.de (OSRM<br />
routing car/bike/foot) and</p></li>
<li><p>valhalla1.openstreetmap.de (Valhalla routing car/bike/foot)</p></li>
</ul>
<p>If you need other maps than the standard map (e.g. CycleOSM etc), use your browers dev tools to see the requests and whitelist them as well (e.g. openstreetmap.fr, thunderforest.com etc)</p>
<p>More Domains to whitelist (Edit):</p>
<p>For those other map layers you would need:</p>
<ul>
<li><p>tileserver.memomaps.de</p></li>
<li><p>a.tile.thunderforest.com</p></li>
<li><p>b.tile.thunderforest.com</p></li>
<li><p>c.tile.thunderforest.com</p></li>
<li><p>a.tile-cyclosm.openstreetmap.fr</p></li>
<li><p>b.tile-cyclosm.openstreetmap.fr</p></li>
<li><p>c.tile-cyclosm.openstreetmap.fr</p></li>
<li><p>tile-a.openstreetmap.fr</p></li>
<li><p>tile-b.openstreetmap.fr</p></li>
<li><p>tile-c.openstreetmap.fr</p></li>
</ul>
<p>For Valhalla Routing you would need:</p>
<ul>
<li>valhalla1.openstreetmap.de</li>
</ul>
<p>(valhalla<strong>1</strong> &lt;- this one got edited above as well)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '23, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '23, 19:29</strong> </span></p>
</div>
</div>
<div id="comments-container-87798" class="comments-container">
<span id="87799"></span>
<div id="comment-87799" class="comment">
<div id="post-87799-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, graphhopper.com is necessary for calculating itineraries using GraphHopper.</p>
</div>
<div id="comment-87799-info" class="comment-info">
<span class="comment-age">(05 Sep '23, 11:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="87820"></span>
<div id="comment-87820" class="comment">
<div id="post-87820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for these responses With your items in my whitelist I have the itineraries calculated by OSMR and by GraphHopper. However I have not the itineraries using Vahalla, and moreover in the right hand menu I can use only the standard map and not the 5 other ones (CyclOSM, Carte cyclable, Carte de transport, ÖPNVKarte). I have not find any request for these maps in the source code given by Firefox, so I am looking for more info</p>
<p><img src="/upfiles/OSM_maps_with_whitelist.png" alt="Maps list screenshot" /></p>
</div>
<div id="comment-87820-info" class="comment-info">
<span class="comment-age">(07 Sep '23, 18:43)</span> <span class="comment-user userinfo">Superdocious</span>
</div>
</div>
<span id="87822"></span>
<div id="comment-87822" class="comment">
<div id="post-87822-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've edited the answer to include more domains/subdomains for those other map layers as well as corrected the valhalla domain.</p>
</div>
<div id="comment-87822-info" class="comment-info">
<span class="comment-age">(07 Sep '23, 19:25)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-87798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87798-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87825"></span>

<div id="answer-container-87825" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you so much for your help, it's a pleasure to see the kids using OSM safely. To recap, here are the 16 items of the whitelist</p>
<ul>
<li>openstreetmap.org</li>
<li>openstreetmap.org/assets</li>
<li>nominatim.openstreetmap.org</li>
<li>routing.openstreetmap.de</li>
<li>graphhopper.com</li>
<li>valhalla1.openstreetmap.de</li>
<li>tileserver.memomaps.de</li>
<li>a.tile.thunderforest.com</li>
<li>b.tile.thunderforest.com</li>
<li>c.tile.thunderforest.com</li>
<li>a.tile-cyclosm.openstreetmap.fr</li>
<li>b.tile-cyclosm.openstreetmap.fr</li>
<li>c.tile-cyclosm.openstreetmap.fr</li>
<li>tile-a.openstreetmap.fr</li>
<li>tile-b.openstreetmap.fr</li>
<li>tile-c.openstreetmap.fr</li>
</ul>
<p>Plus, with Linux, one can use the URL to create a "web application", which opens OSM directly without going through the browser's home page. So there's no temptation to waste time on the web!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '23, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d2680ec0a31ee02ee1dd43542eb4367a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Superdocious&#39;s gravatar image" />
<p><span>Superdocious</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Superdocious has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-87825" class="comments-container">
&#10;</div>
<div id="comment-tools-87825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87825-form-container" class="comment-form-container">
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

