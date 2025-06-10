+++
type = "question"
title = "Automating the tally of road lengths added - by username"
description = '''I&#x27;m trying to find a way where I can keep track (automated) of the length of roads I add in OSM over time. Is there a script/tool/api that I can use to automatically download the ways (version =1) that I&#x27;ve added into OSM?  I don&#x27;t want to download from geofabrik and process via osmosis each time, a...'''
date = "2018-10-09T00:19:00Z"
lastmod = "2018-10-10T12:56:00Z"
weight = 66232
keywords = [ "lengths", "achavi", "username", "api", "quantifying" ]
aliases = [ "/questions/66232" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Automating the tally of road lengths added - by username](/questions/66232/automating-the-tally-of-road-lengths-added-by-username)

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
<span id="post-66232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66232-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to find a way where I can keep track (automated) of the length of roads I add in OSM over time. Is there a script/tool/api that I can use to automatically download the ways (version =1) that I've added into OSM?</p>
<p>I don't want to download from geofabrik and process via osmosis each time, and overpass has a limit of 100 returns.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lengths" rel="tag" title="see questions tagged &#39;lengths&#39;">lengths</span> <span class="post-tag tag-link-achavi" rel="tag" title="see questions tagged &#39;achavi&#39;">achavi</span> <span class="post-tag tag-link-username" rel="tag" title="see questions tagged &#39;username&#39;">username</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-quantifying" rel="tag" title="see questions tagged &#39;quantifying&#39;">quantifying</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '18, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/146f9c2b954b5bbe3c30ae5f4be407e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markzawi&#39;s gravatar image" />
<p><span>markzawi</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markzawi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66232" class="comments-container">
&#10;</div>
<div id="comment-tools-66232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66232-form-container" class="comment-form-container">
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

<span id="66238"></span>

<div id="answer-container-66238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66238-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many different approaches you can take. I'd probably use <a href="https://osmcode.org/osmium-tool">osmium</a> to convert the downloaded data into <a href="https://osmcode.org/opl-file-format/">OPL</a> format (using <code>osmium cat</code>) in which I can simply filter out all ways edited by a specific user id (simple <code>grep ' u123 '</code>) on the OPL file, then <code>grep ' v1 '</code> to get the first version. All of this can be done in one command line. You then have to get the nodes for those ways you filtered out <code>osmium getid -r</code>. In the <code>libosmium</code> repository there is a tool call <a href="https://github.com/osmcode/libosmium/blob/master/examples/osmium_road_length.cpp">road_length</a> which can do the rest. And while this seems to be a bit complicated at first, after you have used those tools a few times, you will appreciate the enormous flexibility you get from having tools like this that can be put together in different ways to achieve complex ends.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '18, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-66238" class="comments-container">
<span id="66258"></span>
<div id="comment-66258" class="comment">
<div id="post-66258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Awesome, thank you Jochen! The road_length tool looks promising.</p>
</div>
<div id="comment-66258-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 19:06)</span> <span class="comment-user userinfo">markzawi</span>
</div>
</div>
<span id="66261"></span>
<div id="comment-66261" class="comment">
<div id="post-66261-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hmm, actually it is "slightly" more complicated than just getting v1 of the way, as "to do it properly"TM you should add extensions of existing ways added by the user in question and to be really nit-picky new ways created by splits shouldn't be counted :-).</p>
</div>
<div id="comment-66261-info" class="comment-info">
<span class="comment-age">(10 Oct '18, 11:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="66263"></span>
<div id="comment-66263" class="comment">
<div id="post-66263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is OSM, of course it is always more complicated. I am just providing an answer to the original question, not saying that the question is valid. :-)</p>
</div>
<div id="comment-66263-info" class="comment-info">
<span class="comment-age">(10 Oct '18, 12:56)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-66238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66238-form-container" class="comment-form-container">
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

