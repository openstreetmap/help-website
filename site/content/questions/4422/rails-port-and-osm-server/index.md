+++
type = "question"
title = "Rails Port and OSM Server"
description = '''Hi, Could someone explain me differences between OSM Rails Port [1] and building it&#x27;s own OSM Server [2]? I would like to develop an Indoor/Outdoor navigating system based on OSM. So I need to add OSM buildings descriptions to the database in order to insure indoor/outdoor routing continuity.  What ...'''
date = "2011-04-12T14:40:00Z"
lastmod = "2019-07-09T19:06:00Z"
weight = 4422
keywords = [ "outdoor", "indoor", "osm", "rails", "server" ]
aliases = [ "/questions/4422" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rails Port and OSM Server](/questions/4422/rails-port-and-osm-server)

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
<span id="post-4422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4422-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Could someone explain me differences between OSM Rails Port [1] and building it's own OSM Server [2]?</p>
<p>I would like to develop an Indoor/Outdoor navigating system based on OSM. So I need to add OSM buildings descriptions to the database in order to insure indoor/outdoor routing continuity.</p>
<p>What do you think about extending OSM to indoor mapping?</p>
<p>Thanks,<br />
Audrey</p>
<p>[1] <a href="https://wiki.openstreetmap.org/wiki/The_Rails_Port">Rails Port</a><br />
[2] <a href="http://weait.com/content/build-your-own-openstreetmap-server">Own OSM Server</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-outdoor" rel="tag" title="see questions tagged &#39;outdoor&#39;">outdoor</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '11, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/8c2f8361c0168ac69ac20b52b2977246?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AudreyC&#39;s gravatar image" />
<p><span>AudreyC</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AudreyC has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-4422" class="comments-container">
&#10;</div>
<div id="comment-tools-4422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4422-form-container" class="comment-form-container">
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

<span id="4423"></span>

<div id="answer-container-4423" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4423-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Rails Port is the currently used implemenation of the API. Editors talk to it using a REST-like protocoll with a XML description of the raw map data.</p>
<p>The blog post on "building your own OSM Server", cover the creation of a server that renders and servers PNGs files created from the raw map data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '11, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4423" class="comments-container">
<span id="4428"></span>
<div id="comment-4428" class="comment">
<div id="post-4428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer!</p>
<p>I have installed the Rails Port and populated the DB thanks to osmosis. I am not sure to understand why, if I edit the map on my server, I don't see <a href="http://img858.imageshack.us/i/screenshot20110412at173.png/">ways and nodes</a> as when I edit the <a href="http://img19.imageshack.us/i/screenshot20110412at173.png/">map on</a> <a href="http://openstreetmap.org"></a><a href="http://openstreetmap.org">openstreetmap.org</a>?</p>
</div>
<div id="comment-4428-info" class="comment-info">
<span class="comment-age">(12 Apr '11, 16:41)</span> <span class="comment-user userinfo">AudreyC</span>
</div>
</div>
<span id="44742"></span>
<div id="comment-44742" class="comment">
<div id="post-44742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the answer <a href="/questions/17450/point-rails-port-to-different-tile-server">here</a> help? I'm guessing a bit here, obviously.</p>
</div>
<div id="comment-44742-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 16:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69950"></span>
<div id="comment-69950" class="comment">
<div id="post-69950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, that topic remains unanswered, do you know how to address this issue?</p>
</div>
<div id="comment-69950-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 18:35)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="69952"></span>
<div id="comment-69952" class="comment">
<div id="post-69952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alas no...</p>
</div>
<div id="comment-69952-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 19:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4423-form-container" class="comment-form-container">
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

