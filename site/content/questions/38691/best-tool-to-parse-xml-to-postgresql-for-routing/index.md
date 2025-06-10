+++
type = "question"
title = "Best tool to parse XML to PostgreSQL for routing?"
description = '''I need to parse osm xml into PostgreSQL - there are a lot of tools to do that - I want to know which tool is best when I want to create a routing engine using the PostgreSQL database?  THANKS EDIT: Using Windows - also by best I mean something that&#x27;s relatively easy to use - I&#x27;m really new to this.'''
date = "2014-11-21T01:16:00Z"
lastmod = "2014-11-21T16:59:00Z"
weight = 38691
keywords = [ "xml", "postgresql", "parsing" ]
aliases = [ "/questions/38691" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best tool to parse XML to PostgreSQL for routing?](/questions/38691/best-tool-to-parse-xml-to-postgresql-for-routing)

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
<span id="post-38691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38691-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to parse osm xml into PostgreSQL - there are a lot of tools to do that - I want to know which tool is best when I want to create a routing engine using the PostgreSQL database?</p>
<p>THANKS</p>
<p>EDIT: Using Windows - also by best I mean something that's relatively easy to use - I'm really new to this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '14, 01:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a759928a25662633a5d3ba0288eb1561?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="echoalphapapa&#39;s gravatar image" />
<p><span>echoalphapapa</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="echoalphapapa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '14, 02:19</strong> </span></p>
</div>
</div>
<div id="comments-container-38691" class="comments-container">
&#10;</div>
<div id="comment-tools-38691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38691-form-container" class="comment-form-container">
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

<span id="38695"></span>

<div id="answer-container-38695" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38695-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That depends on what routing engine you're using, but assuming it's pgrouting, look at <a href="http://pgrouting.org/docs/tools/osm2pgrouting.html">osm2pgrouting</a> and <a href="http://osm2po.de/">osm2po</a>. osm2po is a Java application and much more likely to run satisfactorily on Windows, though it's closed source (if that's important to you).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '14, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-38695" class="comments-container">
<span id="38702"></span>
<div id="comment-38702" class="comment">
<div id="post-38702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9952/echoalphapapa">@echoalphapapa</a></p>
<p>if you want to try other opensource routing frameworks, type "routing" in the search box of this FAQ site.</p>
</div>
<div id="comment-38702-info" class="comment-info">
<span class="comment-age">(21 Nov '14, 15:45)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="38709"></span>
<div id="comment-38709" class="comment">
<div id="post-38709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5/richard">@Richard</a> actually the point of the project I'm working is to build my own routing engine. Right now I'm just look at ways to parse the data into a PostgreSQL database and then build my routing engine.</p>
</div>
<div id="comment-38709-info" class="comment-info">
<span class="comment-age">(21 Nov '14, 16:59)</span> <span class="comment-user userinfo">echoalphapapa</span>
</div>
</div>
</div>
<div id="comment-tools-38695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38695-form-container" class="comment-form-container">
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

