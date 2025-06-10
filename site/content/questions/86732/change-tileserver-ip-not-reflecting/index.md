+++
type = "question"
title = "change tileserver ip not reflecting."
description = '''I&#x27;m trying a vpn setup over openstreetmap server that i setup following https://www.linuxbabe.com/linux-server/osm-openstreetmap-tile-server-ubuntu-22-04 My internal IP is 192.168.0.190, vpn ip is 10.8.0.6(VPN tunnel). During setup, I try to change the renderd and apache2 host from localhost to 10.8...'''
date = "2023-02-19T03:24:00Z"
lastmod = "2023-02-21T14:59:00Z"
weight = 86732
keywords = [ "rendering" ]
aliases = [ "/questions/86732" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [change tileserver ip not reflecting.](/questions/86732/change-tileserver-ip-not-reflecting)

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
<span id="post-86732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86732-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying a vpn setup over openstreetmap server that i setup following <a href="https://www.linuxbabe.com/linux-server/osm-openstreetmap-tile-server-ubuntu-22-04">https://www.linuxbabe.com/linux-server/osm-openstreetmap-tile-server-ubuntu-22-04</a></p>
<p>My internal IP is 192.168.0.190, vpn ip is 10.8.0.6(VPN tunnel). During setup, I try to change the renderd and apache2 host from localhost to 10.8.0.6, but it only render correctly when i use 192.168.0.190, confirmed with local leaflet(hosted on 190), which is using <a href="http://192.168.0.190/osm/%7Bz%7D/%7Bx%7D/%7By%7D.png,">http://192.168.0.190/osm/{z}/{x}/{y}.png,</a> but it doesnt work on <a href="http://10.8.0.6/osm/%7Bz%7D/%7Bx%7D/%7By%7D.png,">http://10.8.0.6/osm/{z}/{x}/{y}.png,</a> I've changed /etc/renderd.conf and /etc/apache2/sites-available/tileserver_site.conf's host to 10.8.0.6</p>
<p>Is there any place i missed, so renderd could serve from 10.8.0.6? (VPN tunnel).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '23, 03:24</strong></p>
<img src="https://secure.gravatar.com/avatar/edccc4f49f3835644f94f566c4bcd407?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skymyth&#39;s gravatar image" />
<p><span>skymyth</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skymyth has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86732" class="comments-container">
&#10;</div>
<div id="comment-tools-86732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86732-form-container" class="comment-form-container">
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

<span id="86767"></span>

<div id="answer-container-86767" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86767-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Is there any place i missed, so renderd could serve from 10.8.0.6?</p>
</blockquote>
<p>No. renderd just makes tiles available, and apache just allows people to access to access them by serving on whatever local IPs you choose to let it. Beyond that, whatever internet plumbing you have (in your case a VPN) allows traffic from (somewhere) access that (or not).</p>
<blockquote>
<p>During setup, I try to change the renderd and apache2 host from localhost to 10.8.0.6</p>
</blockquote>
<p>That was probably a mistake. Generally speaking, sets of instructions like <a href="https://www.linuxbabe.com/linux-server/osm-openstreetmap-tile-server-ubuntu-22-04">https://www.linuxbabe.com/linux-server/osm-openstreetmap-tile-server-ubuntu-22-04</a> and <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> will work if you follow them, and don't try a bit of "freestyle jazz" in the middle.</p>
<p>If you were following a recipe and baking a cake, and decided "but I really like sausages so let's add some of those", the result is unlikely to be what you intend.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '23, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86767" class="comments-container">
&#10;</div>
<div id="comment-tools-86767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86767-form-container" class="comment-form-container">
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

