+++
type = "question"
title = "Basic questions about Nominatim on own server"
description = '''Hi everyone! I found information that it&#x27;s possible to download Nominatim and install it on the own server. But I couldn&#x27;t find answers to all my doubts.  Is the Nominatim independent? After installation on my own server, is there any need to cooperate with some external resources like openstreetmap...'''
date = "2014-11-23T18:44:00Z"
lastmod = "2014-11-24T18:24:00Z"
weight = 38732
keywords = [ "basics", "server", "nominatim" ]
aliases = [ "/questions/38732" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Basic questions about Nominatim on own server](/questions/38732/basic-questions-about-nominatim-on-own-server)

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
<span id="post-38732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38732-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone! I found information that it's possible to download Nominatim and install it on the own server. But I couldn't find answers to all my doubts.</p>
<ol>
<li>Is the Nominatim independent? After installation on my own server, is there any need to cooperate with some external resources like openstreetmap service? Or Nominatim works alone, without any interactions with external services?</li>
<li>Pricing? If I have nominatim installed on my own server, i have to pay anything? (as I know it would be free, am I right?)</li>
<li>Is it easy to get maps from nominatim and use them in mobile application?</li>
</ol>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-basics" rel="tag" title="see questions tagged &#39;basics&#39;">basics</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '14, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3e92742c5de09e167a1799d63636162c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicq&#39;s gravatar image" />
<p><span>nicq</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicq has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38732" class="comments-container">
&#10;</div>
<div id="comment-tools-38732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38732-form-container" class="comment-form-container">
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

<span id="38735"></span>

<div id="answer-container-38735" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38735-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>You can install Nominatim once and if you don't want to keep it in sync with the current OSM data, import once and thats it. But I don't believe you actually understand what Nominatim does, see 3).</li>
<li>Nominatim is free and open software and OSM data can be downloaded on similar <span>terms</span>. Naturally nobody is going to pay your servers etc. for you.</li>
<li><span>Nominatim</span> is the search engine behind the search on openstreetmap.org, it does not provide a "map service". What you need to provide maps is a "tile server" 1) and 2) would apply the same, however we are talking about very different software.</li>
</ol>
<p>See <a href="http://switch2osm.org/">switch2osm.org</a> for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '14, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '14, 18:26</strong> </span></p>
</div>
</div>
<div id="comments-container-38735" class="comments-container">
<span id="38752"></span>
<div id="comment-38752" class="comment">
<div id="post-38752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for a help! One more thing to be sure: Nominatim installed on server contains a some package of maps? I want to install Nominatim on server and then get some maps from my server to display them in another application. Is it possible?</p>
</div>
<div id="comment-38752-info" class="comment-info">
<span class="comment-age">(24 Nov '14, 17:21)</span> <span class="comment-user userinfo">nicq</span>
</div>
</div>
<span id="38756"></span>
<div id="comment-38756" class="comment">
<div id="post-38756-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've slightly extended my answer.</p>
</div>
<div id="comment-38756-info" class="comment-info">
<span class="comment-age">(24 Nov '14, 18:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38735-form-container" class="comment-form-container">
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

