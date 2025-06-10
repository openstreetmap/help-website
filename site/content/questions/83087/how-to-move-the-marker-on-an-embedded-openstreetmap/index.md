+++
type = "question"
title = "How to move the marker on an embedded OpenStreetMap"
description = '''Hello, I would like to use OSM as a location setter on my page. The user should be able to move the marker on the map and then save the location to the database and next time when he/she opens it, the marker should be on the new place. However the marker is not moveable if OSM is embedded. I found n...'''
date = "2022-01-16T15:25:00Z"
lastmod = "2022-01-17T13:28:00Z"
weight = 83087
keywords = [ "marker", "move", "embedded" ]
aliases = [ "/questions/83087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to move the marker on an embedded OpenStreetMap](/questions/83087/how-to-move-the-marker-on-an-embedded-openstreetmap)

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
<span id="post-83087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to use OSM as a location setter on my page. The user should be able to move the marker on the map and then save the location to the database and next time when he/she opens it, the marker should be on the new place. However the marker is not moveable if OSM is embedded. I found no information about how can i move the marker on an embedded OSM iframe. Any ideas on this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-move" rel="tag" title="see questions tagged &#39;move&#39;">move</span> <span class="post-tag tag-link-embedded" rel="tag" title="see questions tagged &#39;embedded&#39;">embedded</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '22, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/64dd4ea7b76fa3ddfa2f238184c7ca40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TCH68k&#39;s gravatar image" />
<p><span>TCH68k</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TCH68k has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83087" class="comments-container">
&#10;</div>
<div id="comment-tools-83087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83087-form-container" class="comment-form-container">
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

<span id="83095"></span>

<div id="answer-container-83095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83095-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You won't be able to achieve this if you are using the iframe embed option. Reason: all browsers have a cross origin security policy that does not allow your website to intercept any interactions a user would have with the map in the iframe.</p>
<p>You would rather have to include the map through a web library like Leaflet ( <a href="https://leaflet.org">https://leaflet.org</a> ) that would give you the chance to orchestrate the interaction with the map. Maybe a leaflet plugin like <a href="https://cliffcloud.github.io/Leaflet.LocationShare/">https://cliffcloud.github.io/Leaflet.LocationShare/</a> would be a start (but it does not save to a database but rather just uses an url to set the information).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '22, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83095" class="comments-container">
<span id="83097"></span>
<div id="comment-83097" class="comment">
<div id="post-83097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can read the iframe's src and see the changes from the URL, but that's not important. How can i move the marker if OSM is embedded? Even if i cannot detect the changes. How can i move the marker?</p>
</div>
<div id="comment-83097-info" class="comment-info">
<span class="comment-age">(17 Jan '22, 12:55)</span> <span class="comment-user userinfo">TCH68k</span>
</div>
</div>
<span id="83098"></span>
<div id="comment-83098" class="comment">
<div id="post-83098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you would go the embed way you would not only have to manipulate the marker lat/lon parameter but also calculate the surrounding bbox values to get the right iframe url for your users. So it is much easier to do this in using a library like Leaflet and start from there.</p>
</div>
<div id="comment-83098-info" class="comment-info">
<span class="comment-age">(17 Jan '22, 13:28)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-83095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83095-form-container" class="comment-form-container">
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

