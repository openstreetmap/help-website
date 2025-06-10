+++
type = "question"
title = "SQL query for house numbers"
description = '''Hi, I&#x27;ve imported the tiger database and i now have house numbers in nominatim. I am trying to get a list of all house numbers on a street. Currently I am iterating through numbers using the local nominatim API to get the highest number but that is very inefficient. How would I get a list of house n...'''
date = "2014-06-21T13:36:00Z"
lastmod = "2014-06-22T13:18:00Z"
weight = 34222
keywords = [ "house", "query", "numbers", "sql" ]
aliases = [ "/questions/34222" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SQL query for house numbers](/questions/34222/sql-query-for-house-numbers)

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
<span id="post-34222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34222-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've imported the tiger database and i now have house numbers in nominatim. I am trying to get a list of all house numbers on a street. Currently I am iterating through numbers using the local nominatim API to get the highest number but that is very inefficient.</p>
<p>How would I get a list of house numbers using SQL? I am thinking it would be something like:</p>
<p>SELECT house_number, latitude, longitude FROM table WHERE street = "10th street NW, Washington";</p>
<p>Regards, Bob</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-numbers" rel="tag" title="see questions tagged &#39;numbers&#39;">numbers</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '14, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1ad59e184d56a0efd199b3b120c59bc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bob12&#39;s gravatar image" />
<p><span>bob12</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bob12 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34222" class="comments-container">
&#10;</div>
<div id="comment-tools-34222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34222-form-container" class="comment-form-container">
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

<span id="34245"></span>

<div id="answer-container-34245" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34245-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is currently no documentation available (at least not on the OSM wiki) describing the database schema nominatim uses. To get around this you either need to have a look at the scripts that create the database or alternatively use psql and the \d command to get a list of tables and then \d <em>tablename</em> to get the columns. If you do that, it would be a good idea to put the results of your research on the wiki :-).<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '14, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
</div>
<div id="comments-container-34245" class="comments-container">
<span id="34246"></span>
<div id="comment-34246" class="comment">
<div id="post-34246-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK this looks to be getting me on the right path: $pgsql nominatim $pgsql&gt; SELECT * FROM points WHERE street = 'xyz street';</p>
<p>Will return all house numbers and coordinates I'll Write up a better query and add it to the wiki if it works out well</p>
</div>
<div id="comment-34246-info" class="comment-info">
<span class="comment-age">(22 Jun '14, 13:18)</span> <span class="comment-user userinfo">bob12</span>
</div>
</div>
</div>
<div id="comment-tools-34245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34245-form-container" class="comment-form-container">
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

