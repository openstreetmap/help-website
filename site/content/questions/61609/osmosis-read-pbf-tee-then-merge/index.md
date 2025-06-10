+++
type = "question"
title = "Osmosis : --read-pbf, --tee then --merge"
description = '''Hello !  I want to read a big pbf file (europe.osm.pbf) only one time and filter tags twice on it, so i&#x27;m using --tee 2 time osmosis &#92;  --read-pbf europe.pbf &#92;  --log-progress &#92;  --tee 2 &#92;  &#92;  --tag-filter accept-relations route=bus &#92;  --used-way &#92;  --tf reject-relations &#92;  --used-node &#92;  --tag-filt...'''
date = "2018-01-12T21:42:00Z"
lastmod = "2018-01-13T09:58:00Z"
weight = 61609
keywords = [ "osmosis" ]
aliases = [ "/questions/61609" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis : --read-pbf, --tee then --merge](/questions/61609/osmosis-read-pbf-tee-then-merge)

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
<span id="post-61609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61609-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello ! I want to read a big <code>pbf</code> file (<code>europe.osm.pbf</code>) only one time and filter tags twice on it, so i'm using <code>--tee 2</code></p>
<pre><code>time osmosis \
    --read-pbf europe.pbf \
    --log-progress \
    --tee 2 \
    \
          --tag-filter accept-relations route=bus \
          --used-way \
          --tf reject-relations \
          --used-node \
          --tag-filter reject-ways building=yes \
                                   public_transport=platform \
                                   highway=construction \
    outPipe.0=&quot;bus_route&quot; \
    \
          --tag-filter reject-relations \
          --tag-filter accept-ways highway=motorway,motorway_link \
          --tag-filter reject-ways disused=yes \
                                   highway=construction \
          --used-node \
    outPipe.0=&quot;freeways&quot; \
  --merge inPipe.0=&quot;bus_route&quot; inPipe.1=&quot;freeways&quot;  --write-pbf bus_route_and_freeways.pbf</code></pre>
<p>but this does not work : no error, but osmosis is running forever.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '18, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/691585dd5690f8183d347d86ffc11b04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djakk&#39;s gravatar image" />
<p><span>djakk</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djakk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61609" class="comments-container">
&#10;</div>
<div id="comment-tools-61609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61609-form-container" class="comment-form-container">
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

<span id="61610"></span>

<div id="answer-container-61610" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61610-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="djakk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This problem is explained in <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.46:">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.46:</a> "If both inputs for the merge are coming from the same thread (e.g. using the tee task followed by the merge task), Osmosis will experience deadlock and the operation will never finish. One solution to this deadlock problem is to read the data in two separate tasks."</p>
<p>It might be easier to simply read the file twice. If you can use the osmium-tool command line program, that will be even quicker.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '18, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-61610" class="comments-container">
<span id="61612"></span>
<div id="comment-61612" class="comment">
<div id="post-61612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot Frederik ! I've just installed osmium this morning, it is very fast indeed :O</p>
</div>
<div id="comment-61612-info" class="comment-info">
<span class="comment-age">(13 Jan '18, 09:58)</span> <span class="comment-user userinfo">djakk</span>
</div>
</div>
</div>
<div id="comment-tools-61610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61610-form-container" class="comment-form-container">
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

