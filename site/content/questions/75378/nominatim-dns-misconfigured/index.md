+++
type = "question"
title = "Nominatim DNS misconfigured?"
description = '''I&#x27;m having trouble resolving nominatim.openstreetmap.org on one of my servers. &amp;gt; nslookup nominatim.openstreetmap.org Server: 127.0.0.53 Address: 127.0.0.53#53  ** server can&#x27;t find nominatim.openstreetmap.org: SERVFAIL  Resolving with another DNS server works: &amp;gt; nslookup nominatim.openstreetm...'''
date = "2020-06-19T09:48:00Z"
lastmod = "2020-06-19T14:36:00Z"
weight = 75378
keywords = [ "nominatim", "dns" ]
aliases = [ "/questions/75378" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim DNS misconfigured?](/questions/75378/nominatim-dns-misconfigured)

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
<span id="post-75378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75378-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having trouble resolving nominatim.openstreetmap.org on one of my servers.</p>
<pre><code>&gt; nslookup nominatim.openstreetmap.org
Server:         127.0.0.53
Address:        127.0.0.53#53
&#10;** server can&#39;t find nominatim.openstreetmap.org: SERVFAIL</code></pre>
<p>Resolving with another DNS server works:</p>
<pre><code>&gt; nslookup nominatim.openstreetmap.org 1.1.1.1
Server:         1.1.1.1
Address:        1.1.1.1#53
&#10;Non-authoritative answer:
nominatim.openstreetmap.org     canonical name = nominatim.geo.openstreetmap.org.
nominatim.geo.openstreetmap.org canonical name = amsterdam.nominatim.openstreetmap.org.
Name:   amsterdam.nominatim.openstreetmap.org
Address: 130.117.76.9</code></pre>
<p>I already contacted support of the DNS server that my server uses by default and they replied, saying the following:</p>
<p>Our investigation shows that it may depend how their domain is being queried: if geo.openstreetmap.org is resolved first the misconfigured records [1] are being cached and will make any other related queries to fail.</p>
<p>It works if nominatim.geo.openstreetmap.org is resolved first and the (almost) correct records being cached for further queries. [2]</p>
<p>[1] <a href="https://mxtoolbox.com/SuperTool.aspx?action=dns%3ageo.openstreetmap.org&amp;run=toolpage">https://mxtoolbox.com/SuperTool.aspx?action=dns%3ageo.openstreetmap.org&amp;run=toolpage</a><br />
[2] <a href="https://mxtoolbox.com/SuperTool.aspx?action=dns%3anominatim.geo.openstreetmap.org&amp;run=toolpage">https://mxtoolbox.com/SuperTool.aspx?action=dns%3anominatim.geo.openstreetmap.org&amp;run=toolpage</a></p>
<hr />
<p>As one can see on the mxtoolbox site, it reports quite a few warnings for the DNS config of these domains and especially one error for geo.openstreetmap.org.</p>
<p>I'm not sure if I should have rather created an issue on GitHub or if this is the place to report potential bugs...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '20, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/e5bfea5d905ae887eaf0fb0f58599fb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toebu&#39;s gravatar image" />
<p><span>toebu</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toebu has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '20, 09:49</strong> </span></p>
</div>
</div>
<div id="comments-container-75378" class="comments-container">
&#10;</div>
<div id="comment-tools-75378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75378-form-container" class="comment-form-container">
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

<span id="75379"></span>

<div id="answer-container-75379" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75379-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="toebu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If nobody answers here, try the <a href="https://operations.osmfoundation.org/">https://operations.osmfoundation.org/</a> group directly at <a href="https://github.com/openstreetmap/operations/issues">https://github.com/openstreetmap/operations/issues</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '20, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-75379" class="comments-container">
&#10;</div>
<div id="comment-tools-75379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75379-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

