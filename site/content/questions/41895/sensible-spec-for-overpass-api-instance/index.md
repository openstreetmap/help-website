+++
type = "question"
title = "Sensible spec for Overpass APi instance"
description = '''Does anyone have an idea of a &#x27;sensible&#x27; spec for a global Overpass API instance? I am doing some research into Big Data techniques for OSM, and would like to use Overpass as a comparator system, but a lot of the installation details seem to be quite old, so I was wondering if anyone had done it rec...'''
date = "2015-03-24T23:48:00Z"
lastmod = "2015-03-29T13:42:00Z"
weight = 41895
keywords = [ "overpass", "scientific", "server" ]
aliases = [ "/questions/41895" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Sensible spec for Overpass APi instance](/questions/41895/sensible-spec-for-overpass-api-instance)

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
<span id="post-41895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41895-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone have an idea of a 'sensible' spec for a global Overpass API instance? I am <a href="https://lists.openstreetmap.org/pipermail/dev/2015-January/028227.html">doing some research</a> into Big Data techniques for OSM, and would like to use Overpass as a comparator system, but a lot of the installation details seem to be quite old, so I was wondering if anyone had done it recently and was able to give a reasonable spec and any idea of how long things might take.</p>
<p>Many thanks</p>
<p>Stephen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-scientific" rel="tag" title="see questions tagged &#39;scientific&#39;">scientific</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '15, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/201c52faa380da64ae76e493d12c0f1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stev&#39;s gravatar image" />
<p><span>stev</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stev has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '15, 06:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-41895" class="comments-container">
<span id="41898"></span>
<div id="comment-41898" class="comment">
<div id="post-41898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you are asking for a doc to clone your own instance?</p>
</div>
<div id="comment-41898-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 06:23)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="41901"></span>
<div id="comment-41901" class="comment">
<div id="post-41901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is for my own instance yes. Testing, not production. I don't need a doc as such, I just want to know what is a reasonable spec, because I'm going to have to rent the server myself, so I don't want to underspec it and not be able to import the planet, or overspec it and pay too much money. I was guessing about 2GB of RAM, and 200GB HDD space. The latter sounds like very little and may be way out of date based on what I've read..</p>
</div>
<div id="comment-41901-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 09:38)</span> <span class="comment-user userinfo">stev</span>
</div>
</div>
</div>
<div id="comment-tools-41895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41895-form-container" class="comment-form-container">
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

<span id="41914"></span>

<div id="answer-container-41914" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41914-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stev has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would recommend to ask this question on the dedicated developer list for Overpass API to get some expert-level feedback:</p>
<p><a href="http://listes.openstreetmap.fr/wws/info/overpass">http://listes.openstreetmap.fr/wws/info/overpass</a></p>
<p>When posting your question, could you please also include some pointers to the installation documentation you've tried out before. Also, please include further details like:</p>
<ul>
<li>do you need current data only or also attic data (=previous object versions).</li>
<li>How about meta data for objects, is this also required for your use case?</li>
<li>Do you need continuous updates or a one-time set up of the db only?</li>
<li>Do you want to import all objects or only certain types (e.g. only highway=*, etc.)</li>
</ul>
<p>Roland (developer of Overpass API) has recently started to integrate db compression features. However, this is not officially released yet. The Overpass API development list archive has very detailed steps on how to set this up. This might also help to save some disk space.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '15, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '15, 14:11</strong> </span></p>
</div>
</div>
<div id="comments-container-41914" class="comments-container">
<span id="41984"></span>
<div id="comment-41984" class="comment">
<div id="post-41984-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, I didn't realise there was a mailing list</p>
</div>
<div id="comment-41984-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 13:42)</span> <span class="comment-user userinfo">stev</span>
</div>
</div>
</div>
<div id="comment-tools-41914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41914-form-container" class="comment-form-container">
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

