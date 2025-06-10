+++
type = "question"
title = "Custom map solution using opensteetmap"
description = '''Hi, I want to work in real estate portal and i need to filter the result and list the properties in map view using opensteetmap(Client requirement). They gave this reference site . I started on yesterday only but the documentation and all i am not able to understood(as a beginner).  Can we implement...'''
date = "2012-06-21T05:33:00Z"
lastmod = "2012-06-21T08:20:00Z"
weight = 13673
keywords = [ "openstreetmap", "map", "tutorial", "customization" ]
aliases = [ "/questions/13673" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Custom map solution using opensteetmap](/questions/13673/custom-map-solution-using-opensteetmap)

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
<span id="post-13673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13673-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-13673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to work in real estate portal and i need to filter the result and list the properties in map view using opensteetmap(Client requirement). They gave <a href="http://www.trulia.com/for_sale/New_York,NY/1500000-1000000000_price/x_map">this reference site</a> . I started on yesterday only but the documentation and all i am not able to understood(as a beginner).</p>
<p>Can we implement <a href="http://www.trulia.com/for_sale/New_York,NY/1500000-1000000000_price/x_map">like</a> this using opensteetmap?</p>
<p>Where should i start at first?</p>
<p>Also i have seen some of the users recommended openlayers,leaflet,mapquest in help answers.Which one is best for my requirement openstreetmap or thirdparty api? Please guide me to complete this task. I dont know where i am and where i have to start? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-tutorial" rel="tag" title="see questions tagged &#39;tutorial&#39;">tutorial</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '12, 05:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8c7a1d478e4d31179cdf2838e3926e54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ilayaraja&#39;s gravatar image" />
<p><span>Ilayaraja</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ilayaraja has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13673" class="comments-container">
&#10;</div>
<div id="comment-tools-13673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13673-form-container" class="comment-form-container">
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

<span id="13674"></span>

<div id="answer-container-13674" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13674-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ilayaraja has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're not very clear with what your problems really are. But of course it is possible to use the OpenStreetMap data for creating a background layer for your real estate site. Since you're using the data for commercial purposes I'd recommend to setup your own rendering chain to lighten the openstreetmap.org server load or use a commercial data provider like geofrabrik or cloudmade. And concerning your client interface, well its totally up to your requirements. Either client is suited to create popups on hover and display auxiliary data.</p>
<p>It appears to me that you're missing some (crucial) background knowledge to complete this task. Your best bet would be to look how other sites including openstreetmap.org are build and understand how things fit together, e.g. Javascript client, Tileserver for background maps and other mapdata servers for your real estate data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13674" class="comments-container">
&#10;</div>
<div id="comment-tools-13674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13674-form-container" class="comment-form-container">
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

