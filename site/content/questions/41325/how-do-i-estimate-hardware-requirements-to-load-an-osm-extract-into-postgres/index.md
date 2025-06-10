+++
type = "question"
title = "How do I estimate hardware requirements to load an OSM extract into Postgres?"
description = '''Yesterday I asked this question due to a problem I&#x27;m encountering when importing an OSM extract into a Postgres database. It appears my hard drive has only a few hundred MBs free.  At the moment, I&#x27;m using a VM on my own machine but I may move the processing to a VM in the cloud or build another VM ...'''
date = "2015-02-24T20:50:00Z"
lastmod = "2015-02-25T22:08:00Z"
weight = 41325
keywords = [ "space", "hardwarerequirements", "osm2pgsql", "ubuntu" ]
aliases = [ "/questions/41325" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I estimate hardware requirements to load an OSM extract into Postgres?](/questions/41325/how-do-i-estimate-hardware-requirements-to-load-an-osm-extract-into-postgres)

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
<span id="post-41325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41325-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Yesterday I asked <a href="/questions/41306/how-do-i-troubleshoot-pgsql_nodes_set-bad-result-during-copy">this</a> question due to a problem I'm encountering when importing an OSM extract into a Postgres database. It appears my hard drive has only a few hundred MBs free.</p>
<p>At the moment, I'm using a VM on my own machine but I may move the processing to a VM in the cloud or build another VM on my own hardware. Either way, I'll likely be building a new VM to handle this.</p>
<p>Question: How do I estimate the hardware requirements necessary to process an OSM extract?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-space" rel="tag" title="see questions tagged &#39;space&#39;">space</span> <span class="post-tag tag-link-hardwarerequirements" rel="tag" title="see questions tagged &#39;hardwarerequirements&#39;">hardwarerequirements</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '15, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/8cbac9d1845bd4993a49777ccda515b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="squatchy&#39;s gravatar image" />
<p><span>squatchy</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="squatchy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '15, 21:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41325" class="comments-container">
<span id="41367"></span>
<div id="comment-41367" class="comment">
<div id="post-41367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you accept the answer to your original question, with a comment that you indeed did not have enough disk space and add a link to this question.</p>
</div>
<div id="comment-41367-info" class="comment-info">
<span class="comment-age">(25 Feb '15, 22:08)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41325-form-container" class="comment-form-container">
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

<span id="41342"></span>

<div id="answer-container-41342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41342-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can visit our <a href="http://wiki.openstreetmap.org">wiki</a> and do a search for "benchmarks" there.</p>
<p>In the result list you will get some hints about duration of processing different amounts of raw OSm data with different tools on different machines.</p>
<p>Maybe this can help you a little bit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '15, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-41342" class="comments-container">
<span id="41348"></span>
<div id="comment-41348" class="comment">
<div id="post-41348-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that there are various tools to load OSM data in a db, depending on your usecase.</p>
</div>
<div id="comment-41348-info" class="comment-info">
<span class="comment-age">(25 Feb '15, 11:12)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="41352"></span>
<div id="comment-41352" class="comment">
<div id="post-41352-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to add one more data point, your us-midwest-latest.osm.pbf extract is around 1Gb. I find that the 330Mb extract from the UK that I use fits "nicely" onto a server with 30Gb of disk, provided that I trim the updates down before importing them. This is with a stylesheet based on an old OSM-carto one (same style file) - the actually storage requirements will of course be different if you store different data.</p>
</div>
<div id="comment-41352-info" class="comment-info">
<span class="comment-age">(25 Feb '15, 12:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41342-form-container" class="comment-form-container">
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

