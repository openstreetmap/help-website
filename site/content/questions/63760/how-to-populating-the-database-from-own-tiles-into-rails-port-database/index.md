+++
type = "question"
title = "how to Populating the database from own tiles into Rails Port  database"
description = '''Hello,  I have installed Rails Port in our local server and We have a seperate server for Tiles. Now I understand from thsi link https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md that, I will need run bellow to import geographical Data osmosis --read-pbf greater-london-...'''
date = "2018-05-27T14:29:00Z"
lastmod = "2018-05-27T16:32:00Z"
weight = 63760
keywords = [ "rails", "railsport" ]
aliases = [ "/questions/63760" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to Populating the database from own tiles into Rails Port database](/questions/63760/how-to-populating-the-database-from-own-tiles-into-rails-port-database)

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
<span id="post-63760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63760-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have installed Rails Port in our local server and We have a seperate server for Tiles.</p>
<p>Now I understand from thsi link <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md</a> that, I will need run bellow to import geographical Data</p>
<pre><code>osmosis --read-pbf greater-london-latest.osm.pbf \
  --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; \
  user=&quot;openstreetmap&quot; password=&quot;&quot; validateSchemaVersion=&quot;no&quot;</code></pre>
<p>But what I am asking is, How can I use my Own tiles which is in 192.168.1.32/Hot with this Ruby port ?</p>
<p>Please help me with this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '18, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-63760" class="comments-container">
&#10;</div>
<div id="comment-tools-63760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63760-form-container" class="comment-form-container">
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

<span id="63762"></span>

<div id="answer-container-63762" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since I cant Delete this question, So i am making it Answered, found the solution <a href="/questions/36946/set-railsport-and-josm-to-use-local-tile-server">https://help.openstreetmap.org/questions/36946/set-railsport-and-josm-to-use-local-tile-server</a></p>
<p>although, just had to edit all link in leaflet.osm.js</p>
<p>Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '18, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-63762" class="comments-container">
<span id="63763"></span>
<div id="comment-63763" class="comment">
<div id="post-63763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've marked it answered for you...</p>
</div>
<div id="comment-63763-info" class="comment-info">
<span class="comment-age">(27 May '18, 16:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63762-form-container" class="comment-form-container">
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

