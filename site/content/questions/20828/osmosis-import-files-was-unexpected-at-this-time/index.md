+++
type = "question"
title = "[closed] Osmosis import - Files was unexpected at this time"
description = '''Hi, I am trying to import an .osm file to my postgres database but I keep getting the following error: Files was unexpected at this time. Command I used to import the file: osmosis --read-xml file=&quot;D:&#92;Licenta&#92;Romania OSM&#92;romania.osm&quot; --write-apidb host=&quot;localhost:5432&quot; database=&quot;romania&quot; user=&quot;postg...'''
date = "2013-03-20T12:53:00Z"
lastmod = "2013-03-25T14:29:00Z"
weight = 20828
keywords = [ "import", "error" ]
aliases = [ "/questions/20828" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Osmosis import - Files was unexpected at this time](/questions/20828/osmosis-import-files-was-unexpected-at-this-time)

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
<span id="post-20828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to import an .osm file to my postgres database but I keep getting the following error: <em>Files was unexpected at this time</em>.</p>
<p>Command I used to import the file: <em>osmosis --read-xml file="D:\Licenta\Romania OSM\romania.osm" --write-apidb host="localhost:5432" database="romania" user="postgres" password="mypostgrespassword"</em></p>
<p>Any idea why I am getting this error?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '13, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Mar '13, 14:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-20828" class="comments-container">
&#10;</div>
<div id="comment-tools-20828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20828-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The questioner has answered their own question and provided the resolution for the benefit of others." by SomeoneElse 25 Mar '13, 14:41

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20966"></span>

<div id="answer-container-20966" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20966-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved this problem by setting the correct path to java.exe. You can do this by editing osmosis.bat in bin directory and setting JAVACMD to the correct path. This worked for me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '13, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20966" class="comments-container">
&#10;</div>
<div id="comment-tools-20966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20966-form-container" class="comment-form-container">
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

