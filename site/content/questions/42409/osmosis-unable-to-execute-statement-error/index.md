+++
type = "question"
title = "osmosis &#x27;unable to execute statement&#x27; error"
description = '''hello,  I&#x27;m trying to use osmosis to import data to PostgreSQL, got an error:    I don&#x27;t know what caused, what do you think? '''
date = "2015-04-17T13:12:00Z"
lastmod = "2015-04-19T15:15:00Z"
weight = 42409
keywords = [ "import", "data", "osmosis" ]
aliases = [ "/questions/42409" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmosis 'unable to execute statement' error](/questions/42409/osmosis-unable-to-execute-statement-error)

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
<span id="post-42409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello, I'm trying to use osmosis to import data to PostgreSQL, got an error: <img src="http://help.openstreetmap.org/upfiles/11.PNG" alt="alt text" /></p>
<pre><code> I don&#39;t know what caused, what do you think?</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '15, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/bf26170f5ff262ce8d8d7ceac68a373b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikenZ&#39;s gravatar image" />
<p><span>ikenZ</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikenZ has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>19 Apr '15, 08:00</strong> </span></p>
</div>
</div>
<div id="comments-container-42409" class="comments-container">
<span id="42410"></span>
<div id="comment-42410" class="comment">
<div id="post-42410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>and, I executed the following command successfully: <img src="http://help.openstreetmap.org/upfiles/10_Je6opAP.PNG" alt="alt text" /></p>
<p>thanks for any help!</p>
</div>
<div id="comment-42410-info" class="comment-info">
<span class="comment-age">(17 Apr '15, 13:15)</span> <span class="comment-user userinfo">ikenZ</span>
</div>
</div>
<span id="42411"></span>
<div id="comment-42411" class="comment">
<div id="post-42411-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The sensible test is to use a --wn (write null) to ensure that the xml file is properly readable. Given that part of the error message is from a pgsql component I'd tentatively suggest the problem lies not with --rx, but with the --write-pgsimp stage. Try writing to the DB with an empty OSM file.</p>
</div>
<div id="comment-42411-info" class="comment-info">
<span class="comment-age">(17 Apr '15, 16:06)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="42422"></span>
<div id="comment-42422" class="comment">
<div id="post-42422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I really appreciate your help very much！ and, I did two tests you suggested: 1,osmosis --read-xml beijing_china.osm --wn 2,osmosis --read-xml null.osm -write-pgsimp ... (null.osm is an empty osm file)</p>
</div>
<div id="comment-42422-info" class="comment-info">
<span class="comment-age">(18 Apr '15, 01:34)</span> <span class="comment-user userinfo">ikenZ</span>
</div>
</div>
<span id="42423"></span>
<div id="comment-42423" class="comment not_top_scorer">
<div id="post-42423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the first ran successfully, but the second also failed with error infomation 'unable to execute statement'. and, the environment: PostgreSQL9.3 + Postgis2.1 + the latest vesion of osmosis. my os is win8.1 I setup the environment on another machine, failed with the same error,too.</p>
</div>
<div id="comment-42423-info" class="comment-info">
<span class="comment-age">(18 Apr '15, 01:40)</span> <span class="comment-user userinfo">ikenZ</span>
</div>
</div>
<span id="42429"></span>
<div id="comment-42429" class="comment">
<div id="post-42429-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So it really appears to be your PostgreSQL environment. I suspect it is something as simple as the password or read/write permissions somewhere.</p>
</div>
<div id="comment-42429-info" class="comment-info">
<span class="comment-age">(18 Apr '15, 11:20)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="42439"></span>
<div id="comment-42439" class="comment">
<div id="post-42439-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I made it! And I particularly appreciate your suggestions. The reason of the error is the way of extension of postgis. I used the command 'psql -d osmdb -f D:\PostgreSQL9.3\share\contrib\postgis-2.1' to extend, then import data failed. when I replaced it with the command 'CREATE EXTENSION postgis;', the import ran successfully.</p>
</div>
<div id="comment-42439-info" class="comment-info">
<span class="comment-age">(19 Apr '15, 07:59)</span> <span class="comment-user userinfo">ikenZ</span>
</div>
</div>
<span id="42446"></span>
<div id="comment-42446" class="comment not_top_scorer">
<div id="post-42446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not what I expected! Well done. I'm grabbing bits &amp; pieces of this conversation to convert into an answer.</p>
</div>
<div id="comment-42446-info" class="comment-info">
<span class="comment-age">(19 Apr '15, 15:14)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42409" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-42409-form-container" class="comment-form-container">
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

<span id="42447"></span>

<div id="answer-container-42447" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42447-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ikenZ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When running into errors with Osmosis it is often difficult to disentangle where the error is occurring. The sensible test is to use a --wn (write null) to ensure that the xml file is properly readable. The obverse test is to start with an empty OSM file to check the latter part of the pipeline.</p>
<p>Given that part of the error message is from a pgsql component I'd tentatively suggest the problem lies not with --rx, but with the --write-pgsimp stage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '15, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-42447" class="comments-container">
&#10;</div>
<div id="comment-tools-42447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42447-form-container" class="comment-form-container">
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

