+++
type = "question"
title = "How do I troubleshoot &quot;pgsql_nodes_set - bad result during COPY&quot; ?"
description = '''I&#x27;m trying to import the us-midwest-latest.osm.pbf extract from geofabrik into a Postgres database. I can import metro or even individual state extracts. I downloaded this regional extract from a few different days just to make sure I didn&#x27;t have a bad extract. I guess there is no guarantee the extr...'''
date = "2015-02-24T04:33:00Z"
lastmod = "2015-02-25T12:39:00Z"
weight = 41306
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/41306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I troubleshoot "pgsql_nodes_set - bad result during COPY" ?](/questions/41306/how-do-i-troubleshoot-pgsql_nodes_set-bad-result-during-copy)

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
<span id="post-41306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41306-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to import the us-midwest-latest.osm.pbf extract from geofabrik into a Postgres database. I can import metro or even individual state extracts. I downloaded this regional extract from a few different days just to make sure I didn't have a bad extract. I guess there is no guarantee the extract may not have problems.</p>
<p>I'm running Ubuntu 14.04 in a VirtualBox VM. The VM has been allocated 10GB of RAM and a 15GB disk. The extract is 950MB. The values following the word "data" in the error message have never been the same throughout the dozen or so times over the last few days that I tried importing this extract.</p>
<p>Here is the osm2pgsql command I used:</p>
<pre><code>osm2pgsql -H localhost --slim  --hstore-all -d midwest_from_osm -U postgres -W ~/Downloads/us-midwest-latest.osm.pbf</code></pre>
<p>I tried using <code>--slim</code> and <code>-C</code> with values from 1024 up to 4096.</p>
<p>Here are two screen captures from two attempts this evening. Any solutions or suggestions for how I can troubleshot this problem? Thanks!</p>
<p><img src="/upfiles/2015-02-23_21-12-06.png" alt="alt text" /></p>
<p><img src="/upfiles/2015-02-23_21-32-07.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '15, 04:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8cbac9d1845bd4993a49777ccda515b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="squatchy&#39;s gravatar image" />
<p><span>squatchy</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="squatchy has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '15, 04:34</strong> </span></p>
</div>
</div>
<div id="comments-container-41306" class="comments-container">
&#10;</div>
<div id="comment-tools-41306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41306-form-container" class="comment-form-container">
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

<span id="41308"></span>

<div id="answer-container-41308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41308-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error refers to the PostgreSQL "COPY" instruction see <a href="http://www.postgresql.org/docs/9.2/static/sql-copy.html">http://www.postgresql.org/docs/9.2/static/sql-copy.html</a> osm2pgsql uses this intensively to load data in to the database.</p>
<p>So likely this indicates issues with the PostgreSQL setup/or the maschine you are running it on, NOT with the input data. Next thing to do is to check your PostgreSQL logs for errors (informed guess: you are running out of disk).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '15, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '15, 20:35</strong> </span></p>
</div>
</div>
<div id="comments-container-41308" class="comments-container">
<span id="41351"></span>
<div id="comment-41351" class="comment">
<div id="post-41351-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to add to this - 15GB disk is <em>really</em> small. If you buy a phone, it'll probably have more storage than this.</p>
</div>
<div id="comment-41351-info" class="comment-info">
<span class="comment-age">(25 Feb '15, 12:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41308-form-container" class="comment-form-container">
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

