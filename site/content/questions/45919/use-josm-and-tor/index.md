+++
type = "question"
title = "Use JOSM and TOR"
description = '''Greetings! I am in Nation restriction internet. I wish to contribute use JOSM. Operating system TAILS. Is it possible? Humble thanks :-)'''
date = "2015-10-15T18:36:00Z"
lastmod = "2015-12-21T12:43:00Z"
weight = 45919
keywords = [ "firewall", "josm", "api", "tor" ]
aliases = [ "/questions/45919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use JOSM and TOR](/questions/45919/use-josm-and-tor)

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
<span id="post-45919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45919-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings! I am in Nation restriction internet. I wish to contribute use JOSM. Operating system <a href="https://en.wikipedia.org/wiki/The_Amnesic_Incognito_Live_System">TAILS</a>. Is it possible? Humble thanks :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-tor" rel="tag" title="see questions tagged &#39;tor&#39;">tor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '15, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e112c1f7adae7820e264d63b66bf0aa9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wawjie&#39;s gravatar image" />
<p><span>wawjie</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wawjie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '15, 09:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-45919" class="comments-container">
<span id="45929"></span>
<div id="comment-45929" class="comment">
<div id="post-45929-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I suppose you tried to edit OSM the normal way already, what error(s) did you encounter ?</p>
</div>
<div id="comment-45929-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 09:00)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45919-form-container" class="comment-form-container">
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

<span id="45931"></span>

<div id="answer-container-45931" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45931-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-45931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM (and iD) use standard HTTP requests to access the REST editing APIs, and the imagery. So if access to these is blocked, you should be able to use TOR to access them.</p>
<p>Check the TOR configuration to make sure that api.openstreetmap.org is routed via TOR. You can change the API url and proxy parameters in JOSM's preferences (second tab from the top).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '15, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-45931" class="comments-container">
<span id="47250"></span>
<div id="comment-47250" class="comment">
<div id="post-47250-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="http://ubuntuguide.org/wiki/Tor">Different sites</a> suggest to set the SOCKS proxy to <code>localhost</code> port <code>9050</code>. That seems to be working except for the DNS resolution, which is still local (-&gt; Tor DNS leak).</p>
<p>Firefox has a setting "Remote DNS" for this purpose. Unfortunately, that's not available in JOSM though. Maybe <a href="http://stackoverflow.com/questions/16268878/how-to-stop-java-from-preresolving-my-host-while-browsing-via-proxy-tor">this link</a> might be helpful to fix this in JOSM?</p>
</div>
<div id="comment-47250-info" class="comment-info">
<span class="comment-age">(21 Dec '15, 12:43)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-45931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45931-form-container" class="comment-form-container">
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

