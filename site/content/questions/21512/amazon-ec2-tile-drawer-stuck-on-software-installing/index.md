+++
type = "question"
title = "Amazon ec2 Tile Drawer: Stuck on Software Installing"
description = '''Hello, I have been trying to set up an OSM tile server using the instructions from the following website: http://tiledrawer.com/ I&#x27;ve followed them exactly, but after setting up and running my Amazon ec2 instances and visiting the appropriate address for the instance, all I get is the &quot;1. Installing...'''
date = "2013-04-13T23:32:00Z"
lastmod = "2013-04-15T02:30:00Z"
weight = 21512
keywords = [ "tiledrawer", "installation", "ec2", "tileserver" ]
aliases = [ "/questions/21512" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Amazon ec2 Tile Drawer: Stuck on Software Installing](/questions/21512/amazon-ec2-tile-drawer-stuck-on-software-installing)

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
<span id="post-21512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21512-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have been trying to set up an OSM tile server using the instructions from the following website: <a href="http://tiledrawer.com/">http://tiledrawer.com/</a></p>
<p>I've followed them exactly, but after setting up and running my Amazon ec2 instances and visiting the appropriate address for the instance, all I get is the "1. Installing Software (setup.sh)" screen. I've run this multiple times for hours, but it never downloads the software.</p>
<p>I am using the free t1.micro servers provided by Amazon. So far, I have used ami-6fa27506 and ami-d0f89fb9 images for the servers, to no avail. The map I am downloading is 11 MB of OSM data, according to the tile drawer website.</p>
<p>Here is the User Data TileDrawer has me input:</p>
<p>#!/bin/sh -ex</p>
<p># Download 11 MB of OSM data from 1 extract.</p>
<p>curl -s <a href="http://tiledrawer.com/scripts/script-128JZs.sh.txt">http://tiledrawer.com/scripts/script-128JZs.sh.txt</a> | /bin/sh -ex</p>
<p>I am quite the newb, and I simply do not know what I can do or what is causing the issue.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiledrawer" rel="tag" title="see questions tagged &#39;tiledrawer&#39;">tiledrawer</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-ec2" rel="tag" title="see questions tagged &#39;ec2&#39;">ec2</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '13, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/131a10817452bc8a8cb3175af7296255?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MatThePhat&#39;s gravatar image" />
<p><span>MatThePhat</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MatThePhat has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '13, 23:36</strong> </span></p>
</div>
</div>
<div id="comments-container-21512" class="comments-container">
&#10;</div>
<div id="comment-tools-21512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21512-form-container" class="comment-form-container">
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

<span id="21515"></span>

<div id="answer-container-21515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21515-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-21515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The script you are using is attempting to download using an old URL. When OSM switched to OdBL geofabrik (the extract provider you are using) re-organized their URLs. The current link for geofabrik's connecticut extract is <a href="http://download.geofabrik.de/north-america/us/connecticut-latest.osm.pbf">http://download.geofabrik.de/north-america/us/connecticut-latest.osm.pbf</a> and you are using <a href="http://download.geofabrik.de/osm/north-america/us/connecticut.osm.pbf">http://download.geofabrik.de/osm/north-america/us/connecticut.osm.pbf</a></p>
<p>You could modify the script to download from the new path, or ask Michal Migurski to update the URLs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '13, 04:54</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-21515" class="comments-container">
<span id="21532"></span>
<div id="comment-21532" class="comment">
<div id="post-21532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting. So I input the script directly into the "user data" section so it wasn't trying to access some text file (removing curl as well), only this time I changed the url to the provided one. Unfortunately, it still seems to have the same problem. same screen stuck on installing software.</p>
</div>
<div id="comment-21532-info" class="comment-info">
<span class="comment-age">(15 Apr '13, 01:46)</span> <span class="comment-user userinfo">MatThePhat</span>
</div>
</div>
</div>
<div id="comment-tools-21515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21515-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21514"></span>

<div id="answer-container-21514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that the problem is asking for 11 MB of OSM data in one hit will cause the server to reject the request as too large. You need to reduce the size of the area that you are requesting (i.e. the number of tiles). It looks like the script that you are using does not handle this refusal and just keeps retrying, which is why it sits there for hours.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '13, 23:56</strong></p>
<img src="https://secure.gravatar.com/avatar/4afbcc50f5d94cce5f85c1da49f3de6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Feilipu&#39;s gravatar image" />
<p><span>Feilipu</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Feilipu has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-21514" class="comments-container">
<span id="21533"></span>
<div id="comment-21533" class="comment">
<div id="post-21533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any nudges toward areas of the internet that would elaborate on where I could start or how I would go about doing that perchance?</p>
</div>
<div id="comment-21533-info" class="comment-info">
<span class="comment-age">(15 Apr '13, 01:46)</span> <span class="comment-user userinfo">MatThePhat</span>
</div>
</div>
<span id="21536"></span>
<div id="comment-21536" class="comment">
<div id="post-21536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In light of the first answer, I'm not sure if my idea is correct. Maybe somebody can confirm the max data size request that server will accept. Good luck!</p>
</div>
<div id="comment-21536-info" class="comment-info">
<span class="comment-age">(15 Apr '13, 02:30)</span> <span class="comment-user userinfo">Feilipu</span>
</div>
</div>
</div>
<div id="comment-tools-21514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21514-form-container" class="comment-form-container">
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

