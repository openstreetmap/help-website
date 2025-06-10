+++
type = "question"
title = "Cannot load OSM tiles. Possible IP block?"
description = '''I don&#x27;t know if this is the right place to ask for this issue.  Clients in the LAN can access https://www.openstreetmap.org however all map background is greyed out; meaning that OSM tiles are not loading. Also this happens when using OSM within Leaflet API. Clients can load and view the map with OS...'''
date = "2019-01-16T12:38:00Z"
lastmod = "2019-01-16T13:13:00Z"
weight = 67605
keywords = [ "tiles" ]
aliases = [ "/questions/67605" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot load OSM tiles. Possible IP block?](/questions/67605/cannot-load-osm-tiles-possible-ip-block)

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
<span id="post-67605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67605-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't know if this is the right place to ask for this issue.</p>
<p>Clients in the LAN can access <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> however all map background is greyed out; meaning that OSM tiles are not loading.</p>
<p>Also this happens when using OSM within Leaflet API. Clients can load and view the map with OSM tiles when accessing the site from another IP but they cannot load the tiles when browsing inside office (with the IP 212.174.24.2)</p>
<p>Is it possible that OSM servers blocked/black listed our IP 212.174.24.2 ? If so, whom to contact for this issue?</p>
<p>Thanks..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '19, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/5c85abeeab75be45e9df35719f9e953b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cempro&#39;s gravatar image" />
<p><span>cempro</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cempro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '19, 12:39</strong> </span></p>
</div>
</div>
<div id="comments-container-67605" class="comments-container">
<span id="67606"></span>
<div id="comment-67606" class="comment">
<div id="post-67606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If they try and fetch and individual tile, what http error code (if any) do they see?</p>
</div>
<div id="comment-67606-info" class="comment-info">
<span class="comment-age">(16 Jan '19, 12:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67607"></span>
<div id="comment-67607" class="comment">
<div id="post-67607-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>E.g. <a href="https://a.tile.openstreetmap.org/2/2/2.png">https://a.tile.openstreetmap.org/2/2/2.png</a></p>
<p>returns nothing inside office (212.174.24.2 ), but when accessed outside from a different IP it loads the png</p>
<p>Office IT declares that they did not block anything and advised me to check whether our IP is blocked or not by the OSM.</p>
</div>
<div id="comment-67607-info" class="comment-info">
<span class="comment-age">(16 Jan '19, 13:05)</span> <span class="comment-user userinfo">cempro</span>
</div>
</div>
<span id="67608"></span>
<div id="comment-67608" class="comment">
<div id="post-67608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "returns nothing" mean? What actual error do you see?</p>
</div>
<div id="comment-67608-info" class="comment-info">
<span class="comment-age">(16 Jan '19, 13:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67609"></span>
<div id="comment-67609" class="comment">
<div id="post-67609-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"ERR_CONNECTION_TIMED_OUT" There seems two possible causes, a) our IP may be black listed b) our office proxy causing issues (although the IT dept. completely denies it) :)</p>
</div>
<div id="comment-67609-info" class="comment-info">
<span class="comment-age">(16 Jan '19, 13:13)</span> <span class="comment-user userinfo">cempro</span>
</div>
</div>
</div>
<div id="comment-tools-67605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67605-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

