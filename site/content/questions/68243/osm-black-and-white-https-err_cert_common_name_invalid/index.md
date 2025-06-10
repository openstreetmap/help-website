+++
type = "question"
title = "OSM Black and White https - ERR_CERT_COMMON_NAME_INVALID"
description = '''I&#x27;m using the tileserver https://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png in leaflet for a project.  I&#x27;m getting the following error on some of the tiles: GET https://b.tiles.wmflabs.org/bw-mapnik/9/266/170.png net::ERR_CERT_COMMON_NAME_INVALID It appears that the error only occurs on tiles l...'''
date = "2019-03-04T10:03:00Z"
lastmod = "2019-03-19T14:49:00Z"
weight = 68243
keywords = [ "tiles", "tileserver" ]
aliases = [ "/questions/68243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Black and White https - ERR_CERT_COMMON_NAME_INVALID](/questions/68243/osm-black-and-white-https-err_cert_common_name_invalid)

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
<span id="post-68243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68243-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the tileserver <a href="https://%7Bs%7D.tiles.wmflabs.org/bw-mapnik/%7Bz%7D/%7Bx%7D/%7By%7D.png">https://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png</a> in leaflet for a project. I'm getting the following error on some of the tiles:</p>
<p><code>GET </code><a href="https://b.tiles.wmflabs.org/bw-mapnik/9/266/170.png"><code>https://b.tiles.wmflabs.org/bw-mapnik/9/266/170.png</code></a><code> net::ERR_CERT_COMMON_NAME_INVALID</code></p>
<p>It appears that the error only occurs on tiles loaded from the b subdomain.</p>
<p>The error can be reproduced by replacing {s} in the link above with a, b, c and open the urls in a browser. The b url will raise the error, and the a and c urls will not.</p>
<p>For now I bypassed the problem by using the url "https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png".</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/38990dfcb2b656db7063cc5bd6f0574e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvbaalen&#39;s gravatar image" />
<p><span>mvbaalen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvbaalen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68243" class="comments-container">
&#10;</div>
<div id="comment-tools-68243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68243-form-container" class="comment-form-container">
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

<span id="68251"></span>

<div id="answer-container-68251" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68251-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll need to talk to the people in charge of that server (Wikimedia, not OpenStreetMap). A relevant help article is <a href="https://stackoverflow.com/questions/2115611/wildcard-ssl-on-sub-subdomain">here</a>. Wikimedia have tried to use a wildcard certificate, but it's not working for sub-sub-domains.</p>
<p>OpenStreetMap does it correctly for local tiles - <a href="https://a.tile.openstreetmap.org/9/253/166.png">here's</a> an example (click on the "lock" icon to get to the certificate details). OSM is just using a regular certificate for "tile.openstreetmap.org", which works fine.</p>
<p>Other reasons why you might not want to use these tiles include that they are very old (from <a href="https://c.tiles.wmflabs.org/bw-mapnik/9/266/170.png/status">2015</a>).</p>
<p>Also note that all of "a", "b" and "c" have the same problems for me - I suspect that you've accepted an exception for 2 of them.</p>
<p>EDIT: Wikimedia have now removed these old tiles completely.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '19, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Mar '19, 18:48</strong> </span></p>
</div>
</div>
<div id="comments-container-68251" class="comments-container">
<span id="68359"></span>
<div id="comment-68359" class="comment">
<div id="post-68359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I think I switch back to the default osm tileserver and use css to make the tiles black and white.</p>
</div>
<div id="comment-68359-info" class="comment-info">
<span class="comment-age">(12 Mar '19, 07:55)</span> <span class="comment-user userinfo">mvbaalen</span>
</div>
</div>
<span id="68424"></span>
<div id="comment-68424" class="comment">
<div id="post-68424-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Looks like Wikimedia have readded those tiles. I saw they were gone for a while, but now they are back.</p>
</div>
<div id="comment-68424-info" class="comment-info">
<span class="comment-age">(19 Mar '19, 14:42)</span> <span class="comment-user userinfo">kwkelly</span>
</div>
</div>
<span id="68425"></span>
<div id="comment-68425" class="comment">
<div id="post-68425-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I still wouldn't use them. <a href="https://b.tiles.wmflabs.org/bw-mapnik/9/266/170.png/status">https://b.tiles.wmflabs.org/bw-mapnik/9/266/170.png/status</a> says "Tile is clean. Last rendered at Fri Apr 10 09:00:52 2015". Newer tiles sources are available.</p>
</div>
<div id="comment-68425-info" class="comment-info">
<span class="comment-age">(19 Mar '19, 14:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68251-form-container" class="comment-form-container">
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

