+++
type = "question"
title = "Filtering osc files and import to PostgreSQL"
description = '''I am trying to deal with some osc (osm change) files, and put them into PostgreSQL database with Osmosis, but it seems that, Osmosis won&#x27;t work with --read-xml-change and --tag-filter together. I have the following code: osmosis --read-xml-change file=source/file.osc outPipe.0=&quot;SOURCE&quot; &#92;  --tf accep...'''
date = "2017-09-11T14:48:00Z"
lastmod = "2017-09-11T15:40:00Z"
weight = 59542
keywords = [ "osm", ".osc", "postgresql", "postgis", "osmosis" ]
aliases = [ "/questions/59542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering osc files and import to PostgreSQL](/questions/59542/filtering-osc-files-and-import-to-postgresql)

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
<span id="post-59542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59542-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to deal with some osc (osm change) files, and put them into PostgreSQL database with Osmosis, but it seems that, Osmosis won't work with --read-xml-change and --tag-filter together. I have the following code:</p>
<pre><code>osmosis --read-xml-change file=source/file.osc outPipe.0=&quot;SOURCE&quot; \
        --tf accept-ways highway=motorway,primary inPipe.0=&quot;SOURCE&quot; outPipe.0=&quot;step1&quot; \
        --tag-filter reject-relations \ 
        --used-node inPipe.0=&quot;step1&quot; outPipe.0=&quot;step2&quot; \               
        --wpc database=mydb user=postgres inPipe.0=&quot;step2&quot;</code></pre>
<p>(formatted code in order to be readable)</p>
<p>Then the following error message comes:</p>
<pre><code>Task 2-tf does not support data provided by input pipe SOURCE.</code></pre>
<p>How can I provide a pipe to make it run without errors or how can I apply filters and insert change file into database?</p>
<p>without pipes and filters Osmosis were able to write osc files to the database</p>
<p>I tried only with just read change file and convert it to osm and it also fails with this message:</p>
<pre><code>Task 2-wx does not support data provided by default pipe stored at level 1 in the default pipe stack.</code></pre>
<p>Osmosis version is: 0.45-52-gd4e52fd-SNAPSHOT</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '17, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/bd59a1956b8ee779ec94d29e78596b72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="horvatha&#39;s gravatar image" />
<p><span>horvatha</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="horvatha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '17, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-59542" class="comments-container">
&#10;</div>
<div id="comment-tools-59542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59542-form-container" class="comment-form-container">
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

<span id="59545"></span>

<div id="answer-container-59545" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59545-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot do what you are planning to do because the osc file does not contain enough information. For example, consider a motorway with three nodes that exists in the OSM database. Now I move these nodes to another continent. The osc file will contain the information that the nodes have moved, but it will not contain anything about the way (which is, in OSM's data model, unchanged, consisting now as before of the same three nodes). Your filter query would then fail to detect that the three nodes are actually relevant for your motorway subset and drop them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '17, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-59545" class="comments-container">
&#10;</div>
<div id="comment-tools-59545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59545-form-container" class="comment-form-container">
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

