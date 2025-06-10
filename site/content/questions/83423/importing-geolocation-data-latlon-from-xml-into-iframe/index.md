+++
type = "question"
title = "Importing geolocation data (lat/lon) from XML into iframe"
description = '''Hi all, I&#x27;m very overwhelmed with information and am very confused with the process of displaying maps (the way I want) on my website. I understand that I can grab the iframe and paste it on my website, which is great. However, I am importing geolocation data from an XML file so I have lots of diffe...'''
date = "2022-02-09T12:51:00Z"
lastmod = "2022-02-09T18:34:00Z"
weight = 83423
keywords = [ "xml", "iframe" ]
aliases = [ "/questions/83423" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Importing geolocation data (lat/lon) from XML into iframe](/questions/83423/importing-geolocation-data-latlon-from-xml-into-iframe)

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
<span id="post-83423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83423-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm very overwhelmed with information and am very confused with the process of displaying maps (the way I want) on my website.</p>
<p>I understand that I can grab the iframe and paste it on my website, which is great. However, I am importing geolocation data from an XML file so I have lots of different locations. I tried editing the iframe with the lat/long information I have from the XML file but it breaks the map. I'm assuming the process is a little more advanced than I thought?</p>
<p>Is there an easy way for me to just add custom lat/long data?</p>
<p>I'm very sorry if I'm misunderstanding something here.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-iframe" rel="tag" title="see questions tagged &#39;iframe&#39;">iframe</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '22, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/972ffb37aef9c3f0002f7f465679020f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CRugman&#39;s gravatar image" />
<p><span>CRugman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CRugman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83423" class="comments-container">
&#10;</div>
<div id="comment-tools-83423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83423-form-container" class="comment-form-container">
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

<span id="83431"></span>

<div id="answer-container-83431" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83431-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>Unfortunately the iframe code from opentreetmap.org is only meant to display a simple map, optionally with a single marker.</p>
<p>You'll need to write your own code, using the <a href="https://leafletjs.com/">Leaflet</a> js framework for example.</p>
<p>Or you could import your data in <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a> (or other similar service), and display this map in an iframe.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '22, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83431" class="comments-container">
&#10;</div>
<div id="comment-tools-83431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83431-form-container" class="comment-form-container">
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

