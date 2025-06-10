+++
type = "question"
title = "Populating database for Overpass application"
description = '''Hello. Yesterday I&#x27;ve started installation of Overpass API on my dedicated server, following steps described here. Since yesterday I am waiting for database populating step to be finished. I&#x27;ve executed following actions:  Instaled Overpass app via tarball Downloaded Europe data europe-latest.osm.bz...'''
date = "2019-10-24T08:56:00Z"
lastmod = "2019-10-24T09:50:00Z"
weight = 71301
keywords = [ "overpass", "database" ]
aliases = [ "/questions/71301" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Populating database for Overpass application](/questions/71301/populating-database-for-overpass-application)

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
<span id="post-71301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71301-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>Yesterday I've started installation of Overpass API on my dedicated server, following steps described <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">here</a>. Since yesterday I am waiting for database populating step to be finished. I've executed following actions:</p>
<ol>
<li>Instaled Overpass app via tarball</li>
<li>Downloaded Europe data <code>europe-latest.osm.bz2</code> from <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">Geofabrik</a></li>
<li>Executed following command:</li>
</ol>
<p><code>nohup init_osm3s.sh planet-latest.osm.bz2 $DB_DIR $EXEC_DIR &amp;</code></p>
<p>I have encountered memory problems during this step and OOM killer interrupted population process. After investigation I've realized that my VPS had memory swaping disabled, so I've enabled memory swapping and set swapfile to 8GB.</p>
<p>After that I repeated step 3. once more, this time no problems showed up. But I am wondering if everything is ok, because it is now ~20 hours since population started, and logs in <code>nohup.out</code> are indicating only 9 nodes flushed into database:</p>
<pre><code>Reading XML file ... elapsed node 130099515. Flushing to database ...... done.
Reading XML file ... elapsed node 270284771. Flushing to database ...... done.
Reading XML file ... elapsed node 299988093. Flushing to database ...... done.
Reading XML file ... elapsed node 337586538. Flushing to database ...... done.
Reading XML file ... elapsed node 366679358. Flushing to database ...... done.
Reading XML file ... elapsed node 421120908. Flushing to database ...... done.
Reading XML file ... elapsed node 472304225. Flushing to database ...... done.
Reading XML file ... elapsed node 523068300. Flushing to database ...... done.
Reading XML file ... elapsed node 580189749. Flushing to database ...... done.</code></pre>
<p>My questions are: <strong>is the speed normal?</strong> I can imagine that europe has millions of nodes so if every node has to be flushed that way, it will take almost forever to complete. <strong>How can I speed-up that process?</strong></p>
<p>My VM:</p>
<ol>
<li>60 GB SSD</li>
<li>4GB of RAM, 8GB SSD swap space</li>
<li>1 vCore</li>
<li>Ubuntu 18 LTS</li>
</ol>
<p>Currently all RAM memory is used and 4GB of swap space is utilized (actually no big changes in memory usage from yesterday).</p>
<p>If a larger machine is required then it is no problem, I can add more resources any time (Google compute engine here...). But I've tought i've met the requirements listed in wiki.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '19, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/757c88a5475d3bfd30aa213b3662f6a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="igoras1993&#39;s gravatar image" />
<p><span>igoras1993</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="igoras1993 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71301" class="comments-container">
&#10;</div>
<div id="comment-tools-71301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71301-form-container" class="comment-form-container">
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

<span id="71303"></span>

<div id="answer-container-71303" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71303-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="igoras1993 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It doesn't list all the nodes, just gives you a node ID every now and then. You seem to have processed about 10% of data in 20 hours so the whole import would take a bit over a week. I think your RAM is probably the reason why it's going slow. If you can allocate resources dynamically, give it 32 GB for the import and you can go down to 8 GB again after that has finished.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '19, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71303" class="comments-container">
<span id="71307"></span>
<div id="comment-71307" class="comment">
<div id="post-71307-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great! I will do that, thank You :) One more question: 60GB of disk space is enough? It seams like 80% is consumed just now. Should I upgrade disk space also (only europe needed)?</p>
</div>
<div id="comment-71307-info" class="comment-info">
<span class="comment-age">(24 Oct '19, 09:28)</span> <span class="comment-user userinfo">igoras1993</span>
</div>
</div>
<span id="71309"></span>
<div id="comment-71309" class="comment">
<div id="post-71309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a machine with an europe-wide Overpass database and it uses ~ 120 GB.</p>
</div>
<div id="comment-71309-info" class="comment-info">
<span class="comment-age">(24 Oct '19, 09:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="71310"></span>
<div id="comment-71310" class="comment">
<div id="post-71310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank You very much!</p>
</div>
<div id="comment-71310-info" class="comment-info">
<span class="comment-age">(24 Oct '19, 09:50)</span> <span class="comment-user userinfo">igoras1993</span>
</div>
</div>
</div>
<div id="comment-tools-71303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71303-form-container" class="comment-form-container">
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

