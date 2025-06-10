+++
type = "question"
title = "Loading a larger KML file"
description = '''Hi, I have created a KML file with a separate color for each state in US using the Quantum GIS(QGIS) tool.and the file size is around 2 MB. I want to load the Map with this KML file layer overlayed on the Map.Its loading fine without any issues,However its showing a Popup dialog to the user,that thi...'''
date = "2012-07-16T10:33:00Z"
lastmod = "2013-04-04T17:02:00Z"
weight = 14288
keywords = [ "map", "kml", "osm" ]
aliases = [ "/questions/14288" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Loading a larger KML file](/questions/14288/loading-a-larger-kml-file)

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
<span id="post-14288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14288-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have created a KML file with a separate color for each state in US using the Quantum GIS(QGIS) tool.and the file size is around 2 MB.</p>
<p>I want to load the Map with this KML file layer overlayed on the Map.Its loading fine without any issues,However its showing a Popup dialog to the user,that this script is executing a longer time ,so Internet Explorer is displaying the message as "Stop running this script? A script on this page is causing Internet Explorer to run slowly. If it continues to run your computer become unresponsive." to select Yes/No.if we select No script will run and it loads the colors correctly.To avoid this warning message</p>
<p>So i tried setting the timeout in the javascript which did not make any difference</p>
<p>seems like the below code is causing the issue. new OpenLayers.Protocol.HTTP({ url: "http://servername/kml/US.kml", format: new OpenLayers.Format.KML({ extractStyles: true, extractAttributes: true })</p>
<p>Is there any way we can fix this? Please post your suggestions how to load it if the kml file is larger.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '12, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c330e0454ebc0cf055159a5962e4f6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VenuGopal&#39;s gravatar image" />
<p><span>VenuGopal</span><br />
<span class="score" title="16 reputation points">16</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VenuGopal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14288" class="comments-container">
&#10;</div>
<div id="comment-tools-14288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14288-form-container" class="comment-form-container">
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

<span id="14289"></span>

<div id="answer-container-14289" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14289-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use smaller KML file, e.g. this (500K): <a href="http://geocommons.com/maps/new?overlay_id=21424">http://geocommons.com/maps/new?overlay_id=21424</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '12, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14289" class="comments-container">
<span id="14290"></span>
<div id="comment-14290" class="comment">
<div id="post-14290-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,Thanks for your reply,How would I get the lesser size KML File?</p>
</div>
<div id="comment-14290-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 11:28)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
</div>
<div id="comment-tools-14289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14289-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21205"></span>

<div id="answer-container-21205" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21205-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The two most common practices to overcome the problem of slow large KML files and OpenLayers are:</p>
<ol>
<li>Convert the KML to images and serve them using a WMS.</li>
<li>Store the KML In a WFS server and query the server using the BBOX strategy.</li>
</ol>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '13, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/3a1a933ac656c11e34a8b9fc3240130e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lambertus&#39;s gravatar image" />
<p><span>Lambertus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lambertus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '13, 17:04</strong> </span></p>
</div>
</div>
<div id="comments-container-21205" class="comments-container">
&#10;</div>
<div id="comment-tools-21205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21205-form-container" class="comment-form-container">
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

