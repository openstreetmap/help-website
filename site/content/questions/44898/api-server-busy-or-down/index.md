+++
type = "question"
title = "API Server busy or down?"
description = '''Hi, I&#x27;ve been trying to Export OSM data for while but get an error message that the request has timed out. This operation is something I often do as I develop custom Garmin maps. I have seen the message before but usually re-submitting the request a few minutes later works. But not this time. I trie...'''
date = "2015-08-25T01:07:00Z"
lastmod = "2015-08-25T14:20:00Z"
weight = 44898
keywords = [ "status", "osm", "server" ]
aliases = [ "/questions/44898" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [API Server busy or down?](/questions/44898/api-server-busy-or-down)

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
<span id="post-44898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44898-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've been trying to Export OSM data for while but get an error message that the request has timed out. This operation is something I often do as I develop custom Garmin maps. I have seen the message before but usually re-submitting the request a few minutes later works. But not this time. I tried last night and now this morning and the same message appears each time no matter how big or little I make the bounding box:</p>
<p>Error: runtime error: open64: 0 Success /osm3s_v0.7.51_osm_base Dispatcher_Client::request_read_and_idx::timeout. Probably the server is overcrowded.</p>
<p>The same thing happens if I try to download an area in JOSM using any of the File&gt;&gt;Download from.... options</p>
<p>Communication with the OSM server 'https://api.openstreetmap.org/api/0.6/' timed out. Please retry later</p>
<p>What's going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-status" rel="tag" title="see questions tagged &#39;status&#39;">status</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '15, 01:07</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44898" class="comments-container">
&#10;</div>
<div id="comment-tools-44898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44898-form-container" class="comment-form-container">
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

<span id="44901"></span>

<div id="answer-container-44901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44901-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>For questions regarding potential server problems (i.e. questions that are likely irrelevant as soon as the problem is fixed), it is better to use <a href="http://wiki.openstreetmap.org/wiki/IRC">IRC</a>. See the "What kinds of questions should be avoided?" section in the FAQ (link in upper right corner of this page).</li>
<li>If you frequently require exports, maybe the web page isn't the right tool to begin with; download an extract that covers the area you're interested in (e.g. from <a href="http://download.geofabrik.de">download.geofabrik.de</a> or <a href="https://mapzen.com/metro-extracts/">https://mapzen.com/metro-extracts/</a>) and then use Osmosis or osmconvert to cut out your area of interest. Or use extract.bbbike.org for a custom area selection.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '15, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '15, 10:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-44901" class="comments-container">
<span id="44903"></span>
<div id="comment-44903" class="comment">
<div id="post-44903-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Frederick, Your answer is not particularly helpful. I have never used the IRC channel, and this behavior is so bizarre that I felt a need to ask the question here. I've been unable to export even a few hundred MB of data since yesterday. The problem continues 18 hours after I first observed it. You could have simply responded with information, if you have it, about whether the server is experiencing difficulty or not.</p>
<p>But seeing as you talk about an IRC channel, what channel might that be? Alternatively, is there some sort of status page for OSM servers?</p>
<p>I add data to OSM almost every day because I want to include my edits and additions in a current GPS image so I don't map the same areas and POIs twice. Consequently I need frequent downloads of up-to-the-minute data. Waiting a week or even a day for new data to appear on one of those servers, or downloading huge parts of the dataset when what I want is usually a few hundred megabytes is wasteful and does not give me what I want.</p>
</div>
<div id="comment-44903-info" class="comment-info">
<span class="comment-age">(25 Aug '15, 09:52)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="44904"></span>
<div id="comment-44904" class="comment">
<div id="post-44904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5016/alaskadave">@alaskadave</a> I've updated the IRC link.</p>
</div>
<div id="comment-44904-info" class="comment-info">
<span class="comment-age">(25 Aug '15, 10:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44901-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44906"></span>

<div id="answer-container-44906" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44906-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Export function is finally working again. I tried the #OSM channel but abandoned that approach pretty quickly.</p>
<p>I reckon the server issue that was affecting my work will have to remain a mystery to me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '15, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44906" class="comments-container">
&#10;</div>
<div id="comment-tools-44906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44906-form-container" class="comment-form-container">
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

