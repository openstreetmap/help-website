+++
type = "question"
title = "How to display street names on a map ?"
description = '''Hello, I&#x27;m looking to make a map of the city of Bergerac in France. The problem is that when I select the area I want to download and I click on the download. On the pdf file, the names of the streets do not appear. How to do ? Have a good day'''
date = "2017-06-26T15:23:00Z"
lastmod = "2017-06-26T22:42:00Z"
weight = 56758
keywords = [ "street" ]
aliases = [ "/questions/56758" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to display street names on a map ?](/questions/56758/how-to-display-street-names-on-a-map)

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
<span id="post-56758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm looking to make a map of the city of Bergerac in France.</p>
<p>The problem is that when I select the area I want to download and I click on the download. On the pdf file, the names of the streets do not appear.</p>
<p>How to do ?</p>
<p>Have a good day</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '17, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/1a1fb1eac0985a6fc93efd521b41388e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DordognesudTeam&#39;s gravatar image" />
<p><span>DordognesudTeam</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DordognesudTeam has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56758" class="comments-container">
<span id="56765"></span>
<div id="comment-56765" class="comment">
<div id="post-56765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where are you downloading the file from?</p>
</div>
<div id="comment-56765-info" class="comment-info">
<span class="comment-age">(26 Jun '17, 22:01)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-56758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56758-form-container" class="comment-form-container">
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

<span id="56767"></span>

<div id="answer-container-56767" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56767-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you click the "share" icon to export a PDF of an area, the level of detail selected by default is that which you currently see on screen.</p>
<p>If you zoom out far enough to see all of Bergerac, you don't see street names on the screen, so the suggested output scale will not show street names either. You can try to set a lower output scale but you'd need to get as low as about 10,000 to see street names, and if the area is too large the system won't let you.</p>
<p>There used to be a good web service that created large maps, called MapOSMatic, but that is currently not running. It is, however, available in a "vagrant" package here <a href="https://github.com/hholzgra/maposmatic-vagrant">https://github.com/hholzgra/maposmatic-vagrant</a> and you could install and run that with relative ease, using the data from <a href="http://download.geofabrik.de/europe/france/aquitaine-latest.osm.pbf.">http://download.geofabrik.de/europe/france/aquitaine-latest.osm.pbf.</a></p>
<p>Another alternative to MapOSMatic for high-resolution outputs is <a href="http://printmaps-osm.de:8080/">http://printmaps-osm.de:8080/</a> which requires that you install a command line client to talk to the server (but you don't have to install a database or load data on your own machine). It covers France but the instructions are in German only.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '17, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56767" class="comments-container">
&#10;</div>
<div id="comment-tools-56767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56767-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56763"></span>

<div id="answer-container-56763" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56763-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, have a look here <a href="https://wiki.openstreetmap.org/wiki/Rendering">https://wiki.openstreetmap.org/wiki/Rendering</a> but remember OSM is just a datafile. The renderer, you for instance, could build a map out of it. The advantage is that you can maintain the file and add special items yourself as well. Or you could use one of the numerous services build on the OSM datafiles, <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services.">https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '17, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-56763" class="comments-container">
&#10;</div>
<div id="comment-tools-56763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56763-form-container" class="comment-form-container">
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

