+++
type = "question"
title = "Get GPX file of a trajectory from openstreetmap programmatically"
description = '''I want to ask if I can get the gpx file of a trajectory from openstreetmap using and an api that run under Android platform. I have the source and the destination, so to plot the shortest path between these two points I need the gpx file of this trajectory. Thank you :)'''
date = "2013-02-11T09:44:00Z"
lastmod = "2013-02-13T15:37:00Z"
weight = 19812
keywords = [ "gpx" ]
aliases = [ "/questions/19812" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get GPX file of a trajectory from openstreetmap programmatically](/questions/19812/get-gpx-file-of-a-trajectory-from-openstreetmap-programmatically)

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
<span id="post-19812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19812-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-19812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to ask if I can get the gpx file of a trajectory from openstreetmap using and an api that run under Android platform. I have the source and the destination, so to plot the shortest path between these two points I need the gpx file of this trajectory. Thank you :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '13, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/67d0bc74b15335eb039e36c3c58b9d55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yahya_Romdhane&#39;s gravatar image" />
<p><span>Yahya_Romdhane</span><br />
<span class="score" title="25 reputation points">25</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yahya_Romdhane has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '13, 09:58</strong> </span></p>
</div>
</div>
<div id="comments-container-19812" class="comments-container">
<span id="19836"></span>
<div id="comment-19836" class="comment">
<div id="post-19836-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>So basically you want a GPX file with 2 nodes: source and destination. Well...I don't see the problem.</p>
<p>Just look at the spec at <a href="http://www.topografix.com/GPX/1/1/">http://www.topografix.com/GPX/1/1/</a> and write the file yourself.</p>
</div>
<div id="comment-19836-info" class="comment-info">
<span class="comment-age">(11 Feb '13, 15:29)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="19838"></span>
<div id="comment-19838" class="comment">
<div id="post-19838-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is not the problem, I'm searching if a routing engine can gives me the calculated way between 2 geopoints in a GPX file. After surfing in the internet, I found that MapQuest and Cloudmade have both webservice api that allows developer to get such informations programmatically. For OSRM it's provides restful webservices but it doesn't return the gpx file of the calculated shortest path.</p>
</div>
<div id="comment-19838-info" class="comment-info">
<span class="comment-age">(11 Feb '13, 16:12)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
<span id="19841"></span>
<div id="comment-19841" class="comment">
<div id="post-19841-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You already asked lots of rather similar questions. Please start using the <a href="https://wiki.openstreetmap.org/w/index.php?search">wiki search function</a>. There is a <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">list of online routers</a> with a <em>GPX export</em> row.</p>
</div>
<div id="comment-19841-info" class="comment-info">
<span class="comment-age">(11 Feb '13, 18:50)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19868"></span>
<div id="comment-19868" class="comment not_top_scorer">
<div id="post-19868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I visited already this. Thanks anyway</p>
</div>
<div id="comment-19868-info" class="comment-info">
<span class="comment-age">(12 Feb '13, 13:44)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
<span id="19877"></span>
<div id="comment-19877" class="comment">
<div id="post-19877-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And why does none of those services featuring GPX export work for you?</p>
</div>
<div id="comment-19877-info" class="comment-info">
<span class="comment-age">(12 Feb '13, 17:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19901"></span>
<div id="comment-19901" class="comment not_top_scorer">
<div id="post-19901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For MapQuest and Cloudmade they limit access because the have business editions</p>
</div>
<div id="comment-19901-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 09:20)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
<span id="19916"></span>
<div id="comment-19916" class="comment">
<div id="post-19916-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And the others mentioned on the wiki; or how about bying the business access if you want to build a commercial application?</p>
</div>
<div id="comment-19916-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 15:37)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-19812" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-19812-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

