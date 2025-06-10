+++
type = "question"
title = "OSM TileServer broken?"
description = '''Hi, Seems that the OSM tileservers are broken for me. Can&#x27;t see anything untoward here: http://wiki.openstreetmap.org/wiki/Servers but am not sure which server(s) are relevant. Several of my pages, and others, using OSM tiles are not displaying anything but were OK yesterday. e.g. http://tinyurl.com...'''
date = "2013-09-18T18:42:00Z"
lastmod = "2013-09-19T08:29:00Z"
weight = 26471
keywords = [ "tileserver" ]
aliases = [ "/questions/26471" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM TileServer broken?](/questions/26471/osm-tileserver-broken)

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
<span id="post-26471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Seems that the OSM tileservers are broken for me. Can't see anything untoward here:<br />
<a href="http://wiki.openstreetmap.org/wiki/Servers">http://wiki.openstreetmap.org/wiki/Servers</a> but am not sure which server(s) are relevant.</p>
<p>Several of my pages, and others, using OSM tiles are not displaying anything but were OK yesterday. e.g.<br />
<a href="http://tinyurl.com/oj5d3rt">http://tinyurl.com/oj5d3rt</a><br />
<a href="http://openlayers.org/dev/examples/osm.html">http://openlayers.org/dev/examples/osm.html</a><br />
<a href="http://pgg123.co.uk/openlayers_simplest_example.html">http://pgg123.co.uk/openlayers_simplest_example.html</a></p>
<p>Anybody any ideas why I'm not seeing any OSM tiles?</p>
<p>Cheers, Peter</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '13, 18:42</strong></p>
<img src="https://secure.gravatar.com/avatar/0115f8b2c7aa0ca63cf903349fc830e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geep999&#39;s gravatar image" />
<p><span>geep999</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geep999 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-26471" class="comments-container">
<span id="26475"></span>
<div id="comment-26475" class="comment">
<div id="post-26475-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Seems to be a problem with <a href="http://openlayers.org/">OpenLayers</a> and not with the OSM tiles. But I can't tell you what's wrong though.</p>
</div>
<div id="comment-26475-info" class="comment-info">
<span class="comment-age">(18 Sep '13, 20:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="26485"></span>
<div id="comment-26485" class="comment">
<div id="post-26485-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, OpenLayers is reporting JavaScript errors on those pages:</p>
<p><code>Uncaught TypeError: Cannot read property 'prototype' of undefined - OpenLayers.js:1169 Uncaught TypeError: undefined is not a function - openlayers_simplest_example.html:7</code></p>
</div>
<div id="comment-26485-info" class="comment-info">
<span class="comment-age">(19 Sep '13, 00:26)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="26489"></span>
<div id="comment-26489" class="comment">
<div id="post-26489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answers - but Hmm.<br />
It's still not working for me.<br />
As some of my pages haven't changed since I know they were working I guess that openlayers must have been changed and broken, as I do point to <a href="http://www.openlayers.org/dev/OpenLayers.js">http://www.openlayers.org/dev/OpenLayers.js</a><br />
Seems that I need to install a working copy of openlayers locally.<br />
Cheers,<br />
Peter<br />
</p>
</div>
<div id="comment-26489-info" class="comment-info">
<span class="comment-age">(19 Sep '13, 08:00)</span> <span class="comment-user userinfo">geep999</span>
</div>
</div>
<span id="26490"></span>
<div id="comment-26490" class="comment">
<div id="post-26490-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Installing a local copy is always recommended. Otherwise your website will fail if the OpenLayers website is down or if there is a major version upgrade / API change.</p>
</div>
<div id="comment-26490-info" class="comment-info">
<span class="comment-age">(19 Sep '13, 08:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26471-form-container" class="comment-form-container">
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

<span id="26476"></span>

<div id="answer-container-26476" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26476-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You want to look <a href="http://wiki.openstreetmap.org/wiki/Status">here</a> where it sais everything is OK.<br />
Since osm.org (and some other maps based on the OSM tiles I checked) seems fine for the most people the problem is probably at your end?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '13, 20:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-26476" class="comments-container">
&#10;</div>
<div id="comment-tools-26476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26476-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26491"></span>

<div id="answer-container-26491" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26491-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that indeed openlayers dev is broken.<br />
Now I found their demo using openlayers 2.13.1 and it's fine - so I'll go off and install 2.13.1 on my server. <a href="http://dev.openlayers.org/releases/OpenLayers-2.13.1/examples/osm.html">http://dev.openlayers.org/releases/OpenLayers-2.13.1/examples/osm.html</a><br />
Cheers,<br />
Peter</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '13, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0115f8b2c7aa0ca63cf903349fc830e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geep999&#39;s gravatar image" />
<p><span>geep999</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geep999 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '13, 08:31</strong> </span></p>
</div>
</div>
<div id="comments-container-26491" class="comments-container">
&#10;</div>
<div id="comment-tools-26491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26491-form-container" class="comment-form-container">
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

