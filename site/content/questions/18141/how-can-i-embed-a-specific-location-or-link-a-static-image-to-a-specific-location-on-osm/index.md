+++
type = "question"
title = "How can I embed a specific location OR link a static image to a specific location on OSM?"
description = '''I would like to place a map of a specific place (state park) on a web page about that park. Embedded map would be best; screenshot would suffice. When users click the map, I want them to go to that specific location on OSM. '''
date = "2012-12-01T22:46:00Z"
lastmod = "2012-12-03T16:58:00Z"
weight = 18141
keywords = [ "website" ]
aliases = [ "/questions/18141" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I embed a specific location OR link a static image to a specific location on OSM?](/questions/18141/how-can-i-embed-a-specific-location-or-link-a-static-image-to-a-specific-location-on-osm)

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
<span id="post-18141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18141-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to place a map of a specific place (state park) on a web page about that park. Embedded map would be best; screenshot would suffice. When users click the map, I want them to go to that specific location on OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '12, 22:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7dd0149399bad5e3a30a1532e7fa805d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hilltromper&#39;s gravatar image" />
<p><span>Hilltromper</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hilltromper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18141" class="comments-container">
&#10;</div>
<div id="comment-tools-18141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18141-form-container" class="comment-form-container">
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

<span id="18142"></span>

<div id="answer-container-18142" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18142-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Browse to the park on the openstreetmap website. Then click on the export tab at the top.</p>
<p>Select either "Embeddable HTML" for an embedded map or select "Map Image (shows standard layer)" for a static image.</p>
<p>You can make a static image clickable by putting code like the following in your webpage.</p>
<pre><code>&lt;a href=&quot;https://www.openstreetmap.org/?lat=52.08825&amp;lon=5.14009&amp;zoom=17&amp;layers=M&quot;&gt;
  &lt;img src=&quot;Wilhelminapark.png&quot; /&gt;
&lt;/a&gt;</code></pre>
<p>You can get the value for "href" by clicking on the "permalink" at the bottom right of the map when looking at the park on the openstreetmap website.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '12, 00:59</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-18142" class="comments-container">
&#10;</div>
<div id="comment-tools-18142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18142-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18171"></span>

<div id="answer-container-18171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18171-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Static_map_images">Static_map_images</a> to find some solutions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '12, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-18171" class="comments-container">
&#10;</div>
<div id="comment-tools-18171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18171-form-container" class="comment-form-container">
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

