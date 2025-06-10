+++
type = "question"
title = "How the get distance by using adress and postal code on a website"
description = '''Hi! Our customers can use a configurator to plan their individual furniture. Part of this configurator should also be an estimated price with included delivery costs. Therefore the customer should only enter his adress and postal code in a website-form. With the distance from this adress and our loc...'''
date = "2020-11-10T15:11:00Z"
lastmod = "2020-11-10T19:47:00Z"
weight = 77493
keywords = [ "website", "distance", "javascript", "adress" ]
aliases = [ "/questions/77493" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How the get distance by using adress and postal code on a website](/questions/77493/how-the-get-distance-by-using-adress-and-postal-code-on-a-website)

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
<span id="post-77493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77493-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! Our customers can use a configurator to plan their individual furniture. Part of this configurator should also be an estimated price with included delivery costs. Therefore the customer should only enter his adress and postal code in a website-form. With the distance from this adress and our location (kilometer) we could calculate these delivery costs on the website (using java-script).</p>
<p>How do I get this distance by using adress and postal code? How can I realize this calculation with openstreepmap using a html-Website and java-script? Is there a script I can use?</p>
<p>I hope, you can help me, Thomas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-adress" rel="tag" title="see questions tagged &#39;adress&#39;">adress</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '20, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/9f581c3e71d60dd3fad2bd2e35812a55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThomasSo13&#39;s gravatar image" />
<p><span>ThomasSo13</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThomasSo13 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '20, 15:11</strong> </span></p>
</div>
</div>
<div id="comments-container-77493" class="comments-container">
&#10;</div>
<div id="comment-tools-77493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77493-form-container" class="comment-form-container">
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

<span id="77496"></span>

<div id="answer-container-77496" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77496-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As I assume you are looking for a turn-by-turn distance to calculate freight costs, you should go for a routing API based on OSM data. Examples for your use case are OSRM, Graphhopper or Valhalla.</p>
<p>Easiest way would be to use one of the hosted APIs, e.g. by Graphhopper, that offer API documentation or example integrations as well (see e.g. <a href="https://docs.graphhopper.com/#tag/Routing-API">https://docs.graphhopper.com/#tag/Routing-API</a> ). If you rather want to try out OSRM, there is a hosted version by several providers, e.g. Geofabrik or <a href="https://routing.openstreetmap.de/about.html">https://routing.openstreetmap.de/about.html</a> (provided by FOSSGIS e.V. - only for light use). Valhalla is offered as a hosted API by Geoapify, as far as I know.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '20, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-77496" class="comments-container">
&#10;</div>
<div id="comment-tools-77496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77496-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77495"></span>

<div id="answer-container-77495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77495-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="https://help.openstreetmap.org/upfiles/route_arrow.JPG" alt="alt text" /></p>
<p>Click on the route arrow and put in start and end points. A route will be calculated ( also for walking and cycling options for other uses). You may find it is not quick or easy enough for your use. You may find it simpler to build a quick look up table with a few limited areas of delivery prices. You may find postcodes are not complete enough either, although there are some busy postcode mappers working hard on post code coverage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '20, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '20, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-77495" class="comments-container">
&#10;</div>
<div id="comment-tools-77495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77495-form-container" class="comment-form-container">
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

