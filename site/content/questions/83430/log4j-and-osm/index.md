+++
type = "question"
title = "Log4j and OSM"
description = '''Just wondering if there were any known log4j vulnerabilities if folks are using the OSM Overpass API? Haven&#x27;t seen any official statements put out by OSM like for other organizations. Admittedly I can&#x27;t see how there would be issues, but since it&#x27;s not super clear from the Wiki (to a novice like mys...'''
date = "2022-02-09T18:01:00Z"
lastmod = "2022-02-09T18:48:00Z"
weight = 83430
keywords = [ "overpass", "security", "api" ]
aliases = [ "/questions/83430" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Log4j and OSM](/questions/83430/log4j-and-osm)

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
<span id="post-83430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83430-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Just wondering if there were any known <code>log4j</code> <a href="https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance">vulnerabilities</a> if folks are using the OSM Overpass API? Haven't seen any official statements put out by OSM like for other organizations. Admittedly I can't see how there would be issues, but since it's not super clear from the Wiki (to a novice like myself) how the API is structured I figured I'd ask.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '22, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/621fb68d5f19a8fa1a36926bffddd05d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sillywizard&#39;s gravatar image" />
<p><span>sillywizard</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sillywizard has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '22, 18:23</strong> </span></p>
</div>
</div>
<div id="comments-container-83430" class="comments-container">
&#10;</div>
<div id="comment-tools-83430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83430-form-container" class="comment-form-container">
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

<span id="83434"></span>

<div id="answer-container-83434" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83434-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sillywizard has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://blog.osmfoundation.org/about/">OSMF</a> only manage the "core" openstreetmap.org servers, which run mostly on Ruby on Rails, with some C optimizations, so I don't think they will issue any statement regarding Log4j.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services">OSM ecosystem</a> is quite diverse and not centrally managed, so you'll need to check every software you use.</p>
<p>The <a href="https://github.com/drolbr/Overpass-API">Overpass API</a> you mention looks to be mostly coded in C++, so I don't think there would any trouble there.</p>
<p>Anyway, if I understand correctly the Log4Shell exploit, the trouble would be for server's administrators, not users.</p>
<p>Disclaimer : I'm neither security nor Java expert.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '22, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83434" class="comments-container">
&#10;</div>
<div id="comment-tools-83434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83434-form-container" class="comment-form-container">
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

