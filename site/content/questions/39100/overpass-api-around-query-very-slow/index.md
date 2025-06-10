+++
type = "question"
title = "Overpass API : around query very slow"
description = '''I want to find all the communes in a &quot;Département&quot; and around 10 kilometers of the limit of this département. rel[name=&quot;Ille-et-Vilaine&quot;][boundary=administrative];rel(around:10000)[&#x27;admin_level&#x27;=&#x27;8&#x27;];out meta; The request is very very slow'''
date = "2014-12-06T12:45:00Z"
lastmod = "2015-06-24T21:20:00Z"
weight = 39100
keywords = [ "overpass", "around" ]
aliases = [ "/questions/39100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API : around query very slow](/questions/39100/overpass-api-around-query-very-slow)

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
<span id="post-39100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39100-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to find all the communes in a "Département" and around 10 kilometers of the limit of this département. rel[name="Ille-et-Vilaine"][boundary=administrative];rel(around:10000)['admin_level'='8'];out meta;</p>
<p>The request is very very slow</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '14, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/79073eb17b9dccd64df88187d0d7561d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mga_geo&#39;s gravatar image" />
<p><span>mga_geo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mga_geo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39100" class="comments-container">
&#10;</div>
<div id="comment-tools-39100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39100-form-container" class="comment-form-container">
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

<span id="39101"></span>

<div id="answer-container-39101" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39101-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-39101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No surprise here. This kind of query is known to be slow. Moreover, the way you constructed the query would even return incorrect results, as you wouldn't get all communities in your department (only those up to 10km proximity to the border).</p>
<p><strong>Note: I had to remove most parts of my previous answer, as it didn't properly take the 10km distance into account. Sorry for that.</strong></p>
<p>I've submitted a <a href="https://github.com/drolbr/Overpass-API/pull/167">pull request</a> to improve the runtime of your query. Once that fix is in place, your query will run in about 2 minutes with the following result:</p>
<p><img src="http://help.openstreetmap.org/upfiles/role.png" alt="alt text" /></p>
<p>Link to previous (non-working) overpass turbo query: <a href="http://overpass-turbo.eu/s/6oX">http://overpass-turbo.eu/s/6oX</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '14, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Dec '14, 15:30</strong> </span></p>
</div>
</div>
<div id="comments-container-39101" class="comments-container">
<span id="43758"></span>
<div id="comment-43758" class="comment">
<div id="post-43758-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Pull request for faster <code>around</code> statement can now be tested on the dev instance: <a href="http://overpass-turbo.eu/s/a6n">http://overpass-turbo.eu/s/a6n</a></p>
<p>This query might take up to 2 minutes and returns about 30MB of data. Results should look pretty much like on the screenshot above.</p>
</div>
<div id="comment-43758-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 21:20)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39101-form-container" class="comment-form-container">
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

