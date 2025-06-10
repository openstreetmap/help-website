+++
type = "question"
title = "JOSM: cannot download map data"
description = '''I just installed JOSM 8677 on Ubuntu 14.04 LTS. When I try to download OSM data to start editing, I get an error message: Failed to open a connection to the remote server &#x27;https://api.openstreetmap.org/api/0.6/map?bbox=136.3265991,44.8617095,136.8676758,45.2304149&#x27;. Please check your internet connec...'''
date = "2015-08-31T14:59:00Z"
lastmod = "2015-08-31T17:04:00Z"
weight = 44990
keywords = [ "josm" ]
aliases = [ "/questions/44990" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM: cannot download map data](/questions/44990/josm-cannot-download-map-data)

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
<span id="post-44990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just installed JOSM 8677 on Ubuntu 14.04 LTS. When I try to download OSM data to start editing, I get an error message:</p>
<pre><code>Failed to open a connection to the remote server &#39;https://api.openstreetmap.org/api/0.6/map?bbox=136.3265991,44.8617095,136.8676758,45.2304149&#39;. Please check your internet connection.</code></pre>
<p>I can make the same API request and download the data through a browser. Clicking help results in a further network error:</p>
<pre><code>org.openstreetmap.josm.gui.help.HelpContentReaderException: java.net.SocketException: Network is unreachable</code></pre>
<p>I am not behind a proxy. I have an excellent internet connection. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '15, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/56dc4e87d18a1e2068e712e1272a1d10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexandervlpl&#39;s gravatar image" />
<p><span>alexandervlpl</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexandervlpl has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '15, 15:00</strong> </span></p>
</div>
</div>
<div id="comments-container-44990" class="comments-container">
<span id="44994"></span>
<div id="comment-44994" class="comment">
<div id="post-44994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your URL is working for me. Can you open it in a browser?</p>
</div>
<div id="comment-44994-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 15:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44995"></span>
<div id="comment-44995" class="comment">
<div id="post-44995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As mentioned in the question, I can open this URL (and download the osm file) in a browser.</p>
</div>
<div id="comment-44995-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 15:30)</span> <span class="comment-user userinfo">alexandervlpl</span>
</div>
</div>
<span id="44996"></span>
<div id="comment-44996" class="comment">
<div id="post-44996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, I missed this part of your question. Maybe it helps to gather some more information. Can you try running JOSM via terminal ("java -jar /path/to/josm.jar") and show us the full output?</p>
</div>
<div id="comment-44996-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 15:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44998"></span>
<div id="comment-44998" class="comment">
<div id="post-44998-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5390/escada"></a><a href="http://help.openstreetmap.org/users/5390/escada">@escada</a>: thanks, this was the problem! Got JOSM to connect to the outside world now. Care to make that an answer, so I can accept it? Also: should this issue be reported/documented somewhere?</p>
</div>
<div id="comment-44998-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 17:04)</span> <span class="comment-user userinfo">alexandervlpl</span>
</div>
</div>
</div>
<div id="comment-tools-44990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44990-form-container" class="comment-form-container">
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

<span id="44997"></span>

<div id="answer-container-44997" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44997-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexandervlpl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>is this an upgrade from an earlier version ? Perhaps it is a similar problem, as described in the <a href="http://forum.openstreetmap.org/viewtopic.php?id=32106">forum</a>, an ip6 problem. If so turn of both ip6 settings in the advanced preferences.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '15, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-44997" class="comments-container">
&#10;</div>
<div id="comment-tools-44997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44997-form-container" class="comment-form-container">
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

