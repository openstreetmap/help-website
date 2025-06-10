+++
type = "question"
title = "download map with tracks in C++"
description = '''Hello, i trying to write some application in C++. at this time I can handle download a map with correct center coordinate, using a url requests.  QString path = &quot;http://tile.openstreetmap.org/%1/%2/%3.png&quot;;  m_url = QUrl(path.arg(zoom).arg(grab.x()).arg(grab.y()));  QNetworkRequest request;  request...'''
date = "2012-10-30T16:53:00Z"
lastmod = "2012-10-30T16:53:00Z"
weight = 17306
keywords = [ "download", "map", "tracks", "c++", "gps" ]
aliases = [ "/questions/17306" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [download map with tracks in C++](/questions/17306/download-map-with-tracks-in-c)

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
<span id="post-17306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i trying to write some application in C++.</p>
<p>at this time I can handle download a map with correct center coordinate, using a url requests.</p>
<pre><code> QString path = &quot;http://tile.openstreetmap.org/%1/%2/%3.png&quot;;
 m_url = QUrl(path.arg(zoom).arg(grab.x()).arg(grab.y()));
 QNetworkRequest request;
 request.setUrl(m_url);
 ...</code></pre>
<p>I need: a) Download a clear map and be able to paint to it in right scale. (in this situation i have download a picture - i know a center coordinate, but draw some tracks in pixels of picture is bad solution with horrible accuracy)</p>
<p>b) Download a map with drawed gps tracks, which i send.</p>
<p>please can someone push me to the right direction? Thanks much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-tracks" rel="tag" title="see questions tagged &#39;tracks&#39;">tracks</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '12, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/cc5890303f4daf7fb242dd41774ba76a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20M&#39;s gravatar image" />
<p><span>Adam M</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam M has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17306" class="comments-container">
&#10;</div>
<div id="comment-tools-17306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17306-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

