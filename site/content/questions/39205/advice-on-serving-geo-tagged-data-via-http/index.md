+++
type = "question"
title = "Advice on serving geo tagged data via HTTP"
description = '''I have a database of basically x,y coordinates with meta data associated - geo tagged data. I want to serve that data via HTTP. I could just write up and document how to request data in various ways. But are there standard approaches to this problem? For example I was thinking about using a similar ...'''
date = "2014-12-11T07:11:00Z"
lastmod = "2014-12-13T10:43:00Z"
weight = 39205
keywords = [ "tagging", "server" ]
aliases = [ "/questions/39205" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Advice on serving geo tagged data via HTTP](/questions/39205/advice-on-serving-geo-tagged-data-via-http)

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
<span id="post-39205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39205-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a database of basically x,y coordinates with meta data associated - geo tagged data. I want to serve that data via HTTP. I could just write up and document how to request data in various ways. But are there standard approaches to this problem? For example I was thinking about using a similar URL scheme to OSM's tile map server to request blocks of data - <a href="http://foo.com/%7Bz%7D/%7Bx%7D/%7By%7D.">http://foo.com/{z}/{x}/{y}.</a> This would aid in caching. Although the semantics of requesting tiles and data are slightly different. Anyway I'm just after some pointers. I can't find any documentation or case studies addressing this, but obviously its been thought about before...</p>
<p>To make things more concrete; I have a (Mongo) database of weather stations scattered over a large geographic area. Each station has a location and a flat list of descriptive data associated with it. I want to provide a public HTTP API to that, similar to how openstreetmaps has a public tile map server. I envisage people will use Leaflet or similar to visualize this data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '14, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e1430f9a10b98409c90b5a0f78c15ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapgenius323&#39;s gravatar image" />
<p><span>mapgenius323</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapgenius323 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '14, 03:49</strong> </span></p>
</div>
</div>
<div id="comments-container-39205" class="comments-container">
<span id="39231"></span>
<div id="comment-39231" class="comment">
<div id="post-39231-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you give more information about your intentions? How will the results be used, and by whom? What format is the data in/will the result need to be in (OSM, SHP, GPX, KML, etc.)?</p>
</div>
<div id="comment-39231-info" class="comment-info">
<span class="comment-age">(11 Dec '14, 23:37)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="39234"></span>
<div id="comment-39234" class="comment">
<div id="post-39234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="http://help.openstreetmap.org/users/8189/alester">@alester</a>. I have updated the question. Thanks.</p>
</div>
<div id="comment-39234-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 01:47)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="39236"></span>
<div id="comment-39236" class="comment">
<div id="post-39236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, a sufficient answer for me might be how OSM (<a href="http://www.openstreetmap.org">http://www.openstreetmap.org</a>) serves "notes". That is pretty much want I want to do.</p>
</div>
<div id="comment-39236-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 07:29)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="39237"></span>
<div id="comment-39237" class="comment">
<div id="post-39237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another example is switch2osm's Leaflet example - <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">http://switch2osm.org/using-tiles/getting-started-with-leaflet/</a> . That has a section on "Showing markers as the user pans around the map".</p>
</div>
<div id="comment-39237-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 09:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="39251"></span>
<div id="comment-39251" class="comment not_top_scorer">
<div id="post-39251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: No thats not what I'm asking about.</p>
</div>
<div id="comment-39251-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 23:07)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="39252"></span>
<div id="comment-39252" class="comment">
<div id="post-39252-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I have problems to see anything OSM-specific here. I guess your question rather belongs to <a href="https://gis.stackexchange.com">https://gis.stackexchange.com</a> or similar sites. If you move, please mention the new link here!</p>
</div>
<div id="comment-39252-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 23:20)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39205" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-39205-form-container" class="comment-form-container">
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

<span id="39212"></span>

<div id="answer-container-39212" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39212-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://www.opengeospatial.org/">http://www.opengeospatial.org/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '14, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-39212" class="comments-container">
<span id="39229"></span>
<div id="comment-39229" class="comment">
<div id="post-39229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer but I'm not finding it that helpful. Kind of like asking a question about electronics and getting "http://ieee.org" as a response... But thanks anyway.</p>
</div>
<div id="comment-39229-info" class="comment-info">
<span class="comment-age">(11 Dec '14, 21:51)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="39256"></span>
<div id="comment-39256" class="comment">
<div id="post-39256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question was: "But are there standard approaches to this problem?"</p>
</div>
<div id="comment-39256-info" class="comment-info">
<span class="comment-age">(13 Dec '14, 10:43)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39212-form-container" class="comment-form-container">
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

