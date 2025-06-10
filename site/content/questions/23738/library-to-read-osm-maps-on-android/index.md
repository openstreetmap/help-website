+++
type = "question"
title = "Library to read OSM maps on Android"
description = '''I&#x27;m adding an offline routing functionality to an Android app, and wondering if there are any standalone libraries I can use to convert OSM map files into some topological object graph. I know there are bunch of open source apps that do this, but wondering if there&#x27;s any packaged library that does t...'''
date = "2013-06-27T01:23:00Z"
lastmod = "2014-10-07T12:04:00Z"
weight = 23738
keywords = [ "android", "osm", "offline", "library" ]
aliases = [ "/questions/23738" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Library to read OSM maps on Android](/questions/23738/library-to-read-osm-maps-on-android)

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
<span id="post-23738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23738-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm adding an offline routing functionality to an Android app, and wondering if there are any standalone libraries I can use to convert OSM map files into some topological object graph. I know there are bunch of open source apps that do this, but wondering if there's any packaged library that does that.</p>
<p>The routing is very app-dependent, so I'm not looking for a routing library, but just rather a simpler way to read in OSM data than having to parse it from XML by myself.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '13, 01:23</strong></p>
<img src="https://secure.gravatar.com/avatar/5cd68b48dba9a92ff163b85b77f6a761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="k0zyr&#39;s gravatar image" />
<p><span>k0zyr</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="k0zyr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '13, 01:51</strong> </span></p>
</div>
</div>
<div id="comments-container-23738" class="comments-container">
&#10;</div>
<div id="comment-tools-23738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23738-form-container" class="comment-form-container">
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

<span id="23752"></span>

<div id="answer-container-23752" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23752-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is something called <a href="http://wiki.openstreetmap.org/wiki/Libosmscout">Libosmscout</a> but I am not sure whether it is usable on android devices.</p>
<p>All known solutions should be collected at <a href="http://wiki.openstreetmap.org/wiki/Frameworks">Frameworks</a>, <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a> and <a href="http://wiki.openstreetmap.org/wiki/Android">Android</a></p>
<p>Maybe you should have a closer look at <a href="http://wiki.openstreetmap.org/wiki/GraphHopper">Graphhopper</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '13, 17:21</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-23752" class="comments-container">
<span id="23755"></span>
<div id="comment-23755" class="comment">
<div id="post-23755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This android app may be of use <a href="http://wiki.openstreetmap.org/wiki/AFTrack_GPS-Tracking">http://wiki.openstreetmap.org/wiki/AFTrack_GPS-Tracking</a></p>
</div>
<div id="comment-23755-info" class="comment-info">
<span class="comment-age">(27 Jun '13, 19:54)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="37382"></span>
<div id="comment-37382" class="comment">
<div id="post-37382-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>libosmscout has support for android but you will need to use the NDK. You can find good tutorials on the net for this. But i would still suggest using Graphhopper.</p>
</div>
<div id="comment-37382-info" class="comment-info">
<span class="comment-age">(07 Oct '14, 12:04)</span> <span class="comment-user userinfo">Nirab Pudasaini</span>
</div>
</div>
</div>
<div id="comment-tools-23752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23752-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25537"></span>

<div id="answer-container-25537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25537-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think <a href="http://graphhopper.com/">Graphhopper</a> is the library you are looking for. This <a href="https://github.com/graphhopper/graphhopper/wiki/Android">wiki</a> will help you get started. Also you can <a href="http://lists.openstreetmap.org/listinfo/graphhopper">subscribe</a> to the mailing list.</p>
<p>With graphhopper you can use a command line tool to convert the OSM files into graph files. You can load these graph files to your android device and then use the graphhopper library to get routes. This Project has matured a lot and is gaining lot of features day by day.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '13, 06:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a812981e0d01bb368aeb92536183d9e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nirab%20Pudasaini&#39;s gravatar image" />
<p><span>Nirab Pudasaini</span><br />
<span class="score" title="556 reputation points">556</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nirab Pudasaini has 2 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '14, 12:09</strong> </span></p>
</div>
</div>
<div id="comments-container-25537" class="comments-container">
&#10;</div>
<div id="comment-tools-25537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25537-form-container" class="comment-form-container">
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

