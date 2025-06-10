+++
type = "question"
title = "Export wind farm data"
description = '''Hey,  I am quite new to OSM, I just used QGis in the past. Now I want to get the data points of the wind farms in the north sea. How can I export that data to put the points in my own map in QGis? Thanks'''
date = "2020-02-04T09:00:00Z"
lastmod = "2020-02-06T15:51:00Z"
weight = 72844
keywords = [ "export", "power" ]
aliases = [ "/questions/72844" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export wind farm data](/questions/72844/export-wind-farm-data)

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
<span id="post-72844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I am quite new to OSM, I just used QGis in the past. Now I want to get the data points of the wind farms in the north sea. How can I export that data to put the points in my own map in QGis?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '20, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5608d6bdf89619c9af6d61c9cc8015fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daniel3110&#39;s gravatar image" />
<p><span>daniel3110</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daniel3110 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72844" class="comments-container">
&#10;</div>
<div id="comment-tools-72844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72844-form-container" class="comment-form-container">
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

<span id="72850"></span>

<div id="answer-container-72850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72850-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is a geo-database (that is a database of geo-information), QGis is a desktop GIS tool. With other words you are talking about two very very different things.</p>
<p>The likely most convenient way to extract relevant data from OSM (and to save it is a form QGis can use) is to use "overpass-turbo", see <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">https://wiki.openstreetmap.org/wiki/Overpass_turbo</a> and <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> for the most popular instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '20, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72850" class="comments-container">
<span id="72858"></span>
<div id="comment-72858" class="comment">
<div id="post-72858-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is an example Overpass Turbo query: <a href="https://overpass-turbo.eu/s/Qol">https://overpass-turbo.eu/s/Qol</a></p>
</div>
<div id="comment-72858-info" class="comment-info">
<span class="comment-age">(04 Feb '20, 20:18)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="72871"></span>
<div id="comment-72871" class="comment">
<div id="post-72871-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that helps a lot. I've already tried some querys and it works quite well.</p>
</div>
<div id="comment-72871-info" class="comment-info">
<span class="comment-age">(05 Feb '20, 14:55)</span> <span class="comment-user userinfo">daniel3110</span>
</div>
</div>
<span id="72897"></span>
<div id="comment-72897" class="comment">
<div id="post-72897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can see if the wind farms you want are well-defined as relations including individual wind turbines with <code>relation[type=site][power=plant]["plant:source"=wind]({{bbox}});</code>. The North Sea (<a href="https://www.openstreetmap.org/relation/9051063)">https://www.openstreetmap.org/relation/9051063)</a> would be specifically: <a href="https://overpass-turbo.eu/s/Qtx">https://overpass-turbo.eu/s/Qtx</a></p>
</div>
<div id="comment-72897-info" class="comment-info">
<span class="comment-age">(06 Feb '20, 15:51)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72850-form-container" class="comment-form-container">
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

