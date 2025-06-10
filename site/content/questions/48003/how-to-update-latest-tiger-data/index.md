+++
type = "question"
title = "how to update latest tiger data"
description = '''Hi, I setup nominatim with osm data &amp;amp; tiger data(2014). Also updated osm data frequently. How can I update latest tiger data(2015) in my DB. Thanks in advance for your help!'''
date = "2016-02-08T13:18:00Z"
lastmod = "2016-03-30T11:04:00Z"
weight = 48003
keywords = [ "tiger", "nominatim", "parser", "update" ]
aliases = [ "/questions/48003" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to update latest tiger data](/questions/48003/how-to-update-latest-tiger-data)

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
<span id="post-48003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48003-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I setup nominatim with osm data &amp; tiger data(2014). Also updated osm data frequently. How can I update latest tiger data(2015) in my DB.</p>
<p>Thanks in advance for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-parser" rel="tag" title="see questions tagged &#39;parser&#39;">parser</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '16, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '16, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-48003" class="comments-container">
<span id="48949"></span>
<div id="comment-48949" class="comment">
<div id="post-48949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried with single edge data &amp; got the following log:</p>
<p>Processing 72059...</p>
<p>DROP TABLE</p>
<p>CREATE TABLE</p>
<p>CREATE FUNCTION</p>
<p>Nominatim-2.3.1/data/tiger2011/72059.sql:</p>
<p>Creating indexes</p>
<p>CREATE INDEX</p>
<p>CREATE INDEX</p>
<p>DROP TABLE</p>
<p>ALTER TABLE</p>
<p>ALTER INDEX</p>
<p>ALTER INDEX</p>
<p>DROP FUNCTION</p>
<p>Setup finished.</p>
<p>From the above log, I think simply we can remove old sql data from data directory &amp; import new data. It will automatically drop old tiger data &amp; imports new data and created index. Am I correct ?</p>
</div>
<div id="comment-48949-info" class="comment-info">
<span class="comment-age">(30 Mar '16, 11:04)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-48003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48003-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

