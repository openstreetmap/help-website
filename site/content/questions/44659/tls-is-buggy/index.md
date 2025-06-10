+++
type = "question"
title = "[closed] TLS is buggy"
description = '''Not a question, but a hint for people who may fix this. Feel free to move this comment to any other place, where you think it belongs. Loading https://osm.org brings some TLS related problems. First one: The certificate CN is wrong. This is annoying, but passable. Major one: Only the standard map an...'''
date = "2015-08-07T17:57:00Z"
lastmod = "2015-08-10T07:24:00Z"
weight = 44659
keywords = [ "tls", "osm.org", "https" ]
aliases = [ "/questions/44659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] TLS is buggy](/questions/44659/tls-is-buggy)

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
<span id="post-44659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44659-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Not a question, but a hint for people who may fix this. Feel free to move this comment to any other place, where you think it belongs.</p>
<p>Loading</p>
<pre><code>https://osm.org</code></pre>
brings some TLS related problems. First one: The certificate CN is wrong. This is annoying, but passable. Major one: Only the standard map and MapQuest Open work, when you forbid loading cleartext content on TLS websites – which is generally a good idea. For example the bicycle map is included via
<pre><code>http://a.tile.thunderforest.com/cycle/…,</code></pre>
although
<pre><code>https://a.tile.thunderforest.com/cycle/…</code></pre>
would work as well. Unnecessarily, to be able to use the bicycle map, I have to instruct my browser to transmit HTTP requests in an HTTPS context.
<p>Maybe you want to fix this, as it should be not such a big deal.<br />
Greets<br />
Torsten</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '15, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/17d7c4948584ec6a9b39e72dad1da85c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="6sH3Hpz2&#39;s gravatar image" />
<p><span>6sH3Hpz2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="6sH3Hpz2 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>07 Aug '15, 18:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-44659" class="comments-container">
<span id="44662"></span>
<div id="comment-44662" class="comment">
<div id="post-44662-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Regarding the first issue: <a href="https://osm.org">https://osm.org</a> is not an official OSM domain so there is nothing OSM can do about it. The second issue sounds like it can be fixed so try to report it at <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a></p>
</div>
<div id="comment-44662-info" class="comment-info">
<span class="comment-age">(08 Aug '15, 08:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44683"></span>
<div id="comment-44683" class="comment">
<div id="post-44683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>whois lists OSMF as the admin organization for osm.org it doesn't get much more official than that.</p>
</div>
<div id="comment-44683-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 01:08)</span> <span class="comment-user userinfo">mvexel</span>
</div>
</div>
<span id="44685"></span>
<div id="comment-44685" class="comment">
<div id="post-44685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting. It has been an unofficial domain in the past IIRC.</p>
</div>
<div id="comment-44685-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 07:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44659-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not a question" by SomeoneElse 07 Aug '15, 18:53

</div>

</div>

</div>

