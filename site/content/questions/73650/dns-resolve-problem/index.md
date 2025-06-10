+++
type = "question"
title = "DNS resolve problem"
description = '''Today i couldn&#x27;t get access to map. I made some digging and found i have problems with resolving tile.openstreetmap.org.  In browser i get error &quot;DNS_PROBE_FINISHED_NXDOMAIN&quot;. Here is &quot;nslookup&quot; for render.openstreetmap.org (he works ok) and a.tile.openstreetmap.org.  (sorry for russian text, it say...'''
date = "2020-03-20T17:16:00Z"
lastmod = "2020-03-21T15:22:00Z"
weight = 73650
keywords = [ "dns" ]
aliases = [ "/questions/73650" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DNS resolve problem](/questions/73650/dns-resolve-problem)

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
<span id="post-73650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Today i couldn't get access to map. I made some digging and found i have problems with resolving tile.openstreetmap.org. In browser i get error "DNS_PROBE_FINISHED_NXDOMAIN". Here is "nslookup" for render.openstreetmap.org (he works ok) and a.tile.openstreetmap.org.</p>
<p><img src="https://i.imgur.com/2xm5zlE.png" alt="alt text" /></p>
<p>(sorry for russian text, it says "Non-authoritative answer")</p>
<p>=============================</p>
<p>Online nslookup (Russia) <a href="https://2whois.ru/?t=nslookup&amp;data=a.tile.openstreetmap.org&amp;dns_type=a">https://2whois.ru/?t=nslookup&amp;data=a.tile.openstreetmap.org&amp;dns_type=a</a></p>
<p>Root DNS server answer:</p>
<pre><code>Server:     b2.org.afilias-nst.org
Address:    2001:500:48::1#53
&#10;Non-authoritative answer:
*** Can&#39;t find openstreetmap.org.: No answer
&#10;Authoritative answers can be found from:
openstreetmap.org   nameserver = daisy.ns.cloudflare.com.
openstreetmap.org   nameserver = rajeev.ns.cloudflare.com.</code></pre>
<p>DNS server answer:</p>
<pre><code>Server:     daisy.ns.cloudflare.com
Address:    2606:4700:50::adf5:3a5a#53
&#10;a.tile.openstreetmap.org    canonical name = tile.geo.openstreetmap.org.</code></pre>
<p>So there is no record type A in DNS server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '20, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/c852c792c308dd99e45b4cb792bc182f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Legista&#39;s gravatar image" />
<p><span>Legista</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Legista has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '20, 06:39</strong> </span></p>
</div>
</div>
<div id="comments-container-73650" class="comments-container">
<span id="73662"></span>
<div id="comment-73662" class="comment">
<div id="post-73662-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See issue (should be fixed?): <a href="https://github.com/openstreetmap/operations/issues/378">https://github.com/openstreetmap/operations/issues/378</a></p>
</div>
<div id="comment-73662-info" class="comment-info">
<span class="comment-age">(21 Mar '20, 10:51)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
<span id="73672"></span>
<div id="comment-73672" class="comment">
<div id="post-73672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh thanks!</p>
</div>
<div id="comment-73672-info" class="comment-info">
<span class="comment-age">(21 Mar '20, 15:22)</span> <span class="comment-user userinfo">Legista</span>
</div>
</div>
</div>
<div id="comment-tools-73650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73650-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="73654"></span>

<div id="answer-container-73654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73654-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tile are served by cache servers, chosen through GeoDNS. The same request from France :</p>
<pre><code>nslookup a.tile.openstreetmap.org 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8#53
&#10;Non-authoritative answer:
a.tile.openstreetmap.org        canonical name = tile.geo.openstreetmap.org.
tile.geo.openstreetmap.org      canonical name = france-02.tile.openstreetmap.org.
Name:   france-02.tile.openstreetmap.org
Address: 91.224.148.166</code></pre>
<p>So regarding your last remark, it's normal, you have to recurse on the canonical name.</p>
<p>Some information about the CDN setup is on the <a href="https://wiki.openstreetmap.org/wiki/Servers/Tile_CDN">wiki</a>. But I can't find much details about the DNS servers involved.</p>
<p>If the issue persist, you might want to reach <a href="https://github.com/openstreetmap/operations/issues">OWG</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '20, 22:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73654" class="comments-container">
&#10;</div>
<div id="comment-tools-73654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73659"></span>

<div id="answer-container-73659" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73659-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've changed DNS server to 1.1.1.1 (didn't knew about it before) and voilà:</p>
<p><img src="https://i.imgur.com/0jGX2mU.png" alt="alt text" /></p>
<p>And map works well and fast. So there is definitely problem with default google DNS server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '20, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c852c792c308dd99e45b4cb792bc182f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Legista&#39;s gravatar image" />
<p><span>Legista</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Legista has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73659" class="comments-container">
&#10;</div>
<div id="comment-tools-73659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73659-form-container" class="comment-form-container">
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

