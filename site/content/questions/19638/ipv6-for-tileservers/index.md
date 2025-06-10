+++
type = "question"
title = "IPv6 for Tileservers"
description = '''Hello! I have seen that openstreetmap.org is reachable over IPv6. But the tileservers are not. Is this for a special reason? *.tile.openstreetmap.org Regards DonatelloXX'''
date = "2013-02-06T20:56:00Z"
lastmod = "2017-01-17T12:10:00Z"
weight = 19638
keywords = [ "tileserver", "ipv6" ]
aliases = [ "/questions/19638" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IPv6 for Tileservers](/questions/19638/ipv6-for-tileservers)

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
<span id="post-19638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19638-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I have seen that openstreetmap.org is reachable over IPv6. But the tileservers are not. Is this for a special reason?</p>
<p>*.tile.openstreetmap.org</p>
<p>Regards</p>
<p>DonatelloXX</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '13, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f15c2c019035eb3d529ec6659be174da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DonatelloXX&#39;s gravatar image" />
<p><span>DonatelloXX</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DonatelloXX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19638" class="comments-container">
&#10;</div>
<div id="comment-tools-19638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19638-form-container" class="comment-form-container">
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

<span id="19651"></span>

<div id="answer-container-19651" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19651-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-19651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DonatelloXX has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately there is.</p>
<p>OpenStreetMap servers are hosted predominantly in two locations: At University College London and at Imperial College. While IC has IPv6 connectivity, UCL does not offer it currently. The main tileserver is hosted at UCL and thus can't server tiles via IPv6 directly.</p>
<p>However, in the current setup the tiles aren't served directly from the tileserver anyway, but fronted by a set of squid proxy servers at a variety of distributed locations to act as a CDN. Although as far as I am aware some of those locations do have IPv6 connectivity it is still not possible to enable IPv6. The proxy servers use squid 2.x and squid doesn't support IPv6 until version 3.1. Unfortunately it currently isn't possible to update to a newer version of squid, as some of the features needed (e.g. tile throttling) do not work with squid 3.x.</p>
<p>I am sure the admins will otherwise enable IPv6 on the tile server as well as soon as the technical problems are worked out.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-19651" class="comments-container">
<span id="19771"></span>
<div id="comment-19771" class="comment">
<div id="post-19771-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>BTW: Do you know how much Bandwidth is needed for the Tileservers? We have a 10MBit Fiber-Connection here in Austria. If the Admins are interested in i could setup an IPv6 Reverse-Proxy to the Tileservers (Or two in different Locations). But this would only make Sense if the Bandwidth isn't to low for IPv6 Traffic.</p>
<p>EDIT: Google says that 1% of of the Overall Internet-Traffic is IPv6 Traffic. How much IPv4-Bandwith is used by the Tileservers?</p>
</div>
<div id="comment-19771-info" class="comment-info">
<span class="comment-age">(08 Feb '13, 22:57)</span> <span class="comment-user userinfo">DonatelloXX</span>
</div>
</div>
<span id="19887"></span>
<div id="comment-19887" class="comment">
<div id="post-19887-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>On the osm webservers that are IPv6 enabled, the percentage of IPv6 was recently about 0.3%. The total of tile server traffic can be seen at <a href="http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/index.html">http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/index.html</a> and can reach about 250 - 300 Mbit/s This traffic is currently served by 5 different reverse proxies, whos location you can see at <a href="http://dns.openstreetmap.org/tile.openstreetmap.org.html">http://dns.openstreetmap.org/tile.openstreetmap.org.html</a></p>
</div>
<div id="comment-19887-info" class="comment-info">
<span class="comment-age">(12 Feb '13, 21:16)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="19888"></span>
<div id="comment-19888" class="comment">
<div id="post-19888-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Currently 3 of the 5 reverse tile proxies do have IPv6 connectivity (The London, Brisbane and Sjöbo proxies). So once the software issue of upgrading to an IPv6 capable squid is solved (or using a different IPv6 capable reverse proxy software), comprehensive IPv6 connectivity should be no problem anymore.</p>
</div>
<div id="comment-19888-info" class="comment-info">
<span class="comment-age">(12 Feb '13, 21:22)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="54096"></span>
<div id="comment-54096" class="comment">
<div id="post-54096-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>Please enable support Ipv6, otherwise competitors tiles (Google, Yandex) are available, but favorite OpenstreetMap - no.</p>
<p>Also need statistics and monitored separately via IPv4 and via IPv6, because they are two different Internet.</p>
</div>
<div id="comment-54096-info" class="comment-info">
<span class="comment-age">(17 Jan '17, 10:43)</span> <span class="comment-user userinfo">bekreyev</span>
</div>
</div>
<span id="54099"></span>
<div id="comment-54099" class="comment">
<div id="post-54099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That isn't a question or an answer.</p>
</div>
<div id="comment-54099-info" class="comment-info">
<span class="comment-age">(17 Jan '17, 12:10)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19651-form-container" class="comment-form-container">
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

