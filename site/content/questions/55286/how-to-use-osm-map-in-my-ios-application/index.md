+++
type = "question"
title = "How to use  osm map in my iOS Application"
description = '''Hi, I want to use OSM in my iOS application, and I found a solution that OSM is not providing any SDK to integrate for mobile APPS.Do I definitely need to go for 3rd party libraries to integrate open street Maps?.If Yes please suggest me some open source libraries to load kml files and GeoJSON files...'''
date = "2017-03-27T12:57:00Z"
lastmod = "2017-03-27T16:32:00Z"
weight = 55286
keywords = [ "objective", "c", "ios", "xcode" ]
aliases = [ "/questions/55286" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use osm map in my iOS Application](/questions/55286/how-to-use-osm-map-in-my-ios-application)

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
<span id="post-55286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55286-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to use OSM in my iOS application, and I found a solution that OSM is not providing any SDK to integrate for mobile APPS.Do I definitely need to go for 3rd party libraries to integrate open street Maps?.If Yes please suggest me some open source libraries to load kml files and GeoJSON files on to the map view.Please help me</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-objective" rel="tag" title="see questions tagged &#39;objective&#39;">objective</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-xcode" rel="tag" title="see questions tagged &#39;xcode&#39;">xcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '17, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/6e3717e12d81c5097d6b522d48268cb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dinesh%20kothuri&#39;s gravatar image" />
<p><span>dinesh kothuri</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dinesh kothuri has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>27 Mar '17, 12:59</strong> </span></p>
</div>
</div>
<div id="comments-container-55286" class="comments-container">
&#10;</div>
<div id="comment-tools-55286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55286-form-container" class="comment-form-container">
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

<span id="55291"></span>

<div id="answer-container-55291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55291-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes you definitely need to go for 3rd party libraries, however quite a few are Open Source. Depending on the technology you are using to develop your application, man different approaches exist - see <a href="http://wiki.openstreetmap.org/wiki/Apple_iOS#Libraries_for_developers">our iOS wiki page</a>. You will very likely also need to set up a server component that delivers OSM data or OSM-based services to the mobile device, again this depends on the technology and library chosen. While OpenStreetMap <em>data</em> is free, OpenStreetMap <em>server capacity</em> isn't (at least not at scale), hence the requirement to run your own server powering your app.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '17, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55291" class="comments-container">
&#10;</div>
<div id="comment-tools-55291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55291-form-container" class="comment-form-container">
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

