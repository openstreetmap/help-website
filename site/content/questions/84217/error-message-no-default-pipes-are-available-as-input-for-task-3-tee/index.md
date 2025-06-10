+++
type = "question"
title = "Error message : &quot;No default pipes are available as input for task 3-tee&quot;"
description = '''Hello, all, Extracting data from the latest europe geofabrik pbf is a lengthy process. I want to extract 2 kinds of data, i.e. speed camera&#x27;s and some brand&#x27;s fuel stations. So to avoid spending too much time in the process, I am looking for the correct way to do so using osmosis. Could someone help...'''
date = "2022-04-19T15:29:00Z"
lastmod = "2022-04-19T17:51:00Z"
weight = 84217
keywords = [ "pipes", "tee" ]
aliases = [ "/questions/84217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error message : "No default pipes are available as input for task 3-tee"](/questions/84217/error-message-no-default-pipes-are-available-as-input-for-task-3-tee)

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
<span id="post-84217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84217-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, all,</p>
<p>Extracting data from the latest europe geofabrik pbf is a lengthy process. I want to extract 2 kinds of data, i.e. speed camera's and some brand's fuel stations. So to avoid spending too much time in the process, I am looking for the correct way to do so using osmosis. Could someone help me out on this ? I would think my command line should look something like</p>
<pre><code>&quot;$OSMOSIS&quot; --read-pbf $DATAIDIR/europe-latest.osm.pbf --write-xml outPipe.1=&quot;allxml&quot; --tee 3 --read-xml inPipe.1=&quot;allxml&quot; --node-key-value keyValueList=&quot;highway.speed_camera&quot; --write-xml $DATAODIR/radars.osm --read-xml inPipe.2=&quot;allxml&quot; --node-key-value keyValueList=&quot;amenity.fuel&quot; --write-xml outPipe.2=&quot;nafte&quot; --read-xml inPipe.2=&quot;nafte&quot; --tf accept-nodes brand=DATS%s24 --write-xml $DATAODIR/DATS24.osm</code></pre>
<p>but I get an error "org.openstreetmap.osmosis.core.OsmosisRuntimeException: No default pipes are available as input for task 3-tee."</p>
<p>In short, I don't arrive at the point of understanding the correct usage of the pipes and of the --tee argument.</p>
<p>Could someone please explain, because despite the detailed osmosis 0.47 usage manual, I don't get at any better result than the one above. Thanks a lot in advance !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pipes" rel="tag" title="see questions tagged &#39;pipes&#39;">pipes</span> <span class="post-tag tag-link-tee" rel="tag" title="see questions tagged &#39;tee&#39;">tee</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '22, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/bff07f8a6b3cbf4c2bfff3330a775bc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudolea&#39;s gravatar image" />
<p><span>sudolea</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudolea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84217" class="comments-container">
&#10;</div>
<div id="comment-tools-84217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84217-form-container" class="comment-form-container">
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

<span id="84218"></span>

<div id="answer-container-84218" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84218-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, if you can use <code>osmium</code> instead of <code>osmosis</code>, things will work faster. Your command line does not work because your first <code>--write-xml</code> already consumes the data stream created by <code>--read-pbf</code> and hence no data stream remains to feed into the <code>--tee</code>. I think if you drop the first <code>--write-xml</code> and <em>all</em> <code>--read-xml</code>s things might work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '22, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84218" class="comments-container">
<span id="84221"></span>
<div id="comment-84221" class="comment">
<div id="post-84221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes ! This works indeed. Thank you so much ! So my final command line reads :</p>
<p><code>"$OSMOSIS" --read-pbf $DATAIDIR/europe-latest.osm.pbf --tee 2 --node-key-value keyValueList="highway.speed_camera" --write-xml $DATAODIR/radars.osm --node-key-value keyValueList="amenity.fuel" --tf accept-nodes brand=DATS%s24 --write-xml $DATAODIR/DATS24.osm</code></p>
<p>Being unfamiliar with the osmium utility you suggest, and not immediately seeing the parallel osmium command I'd need to compare speeds, could I ask you how my osmosis command would (more or less) read in osmium ?</p>
<p>In the meantime, my "mental picture", with regard to osmosis' tee argument, is : <strong>whenever there is <em>any</em> write option, the <em>next</em> argument is the start of tee's next pipe</strong> I don't think I'm far off, am I ?</p>
</div>
<div id="comment-84221-info" class="comment-info">
<span class="comment-age">(19 Apr '22, 16:52)</span> <span class="comment-user userinfo">sudolea</span>
</div>
</div>
<span id="84222"></span>
<div id="comment-84222" class="comment">
<div id="post-84222-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your logic regarding osmosis is almost correct, replace "any write option" with "any option that consumes a stream and doesn't output one again". With osmium, you would probably require several runs since you cannot AND-combine expressions, but since only the first run would consume the large Europe file and every subsequent run would only work on a small intermediate file, that should still go quite fast. See <a href="https://docs.osmcode.org/osmium/latest/osmium-tags-filter.html">https://docs.osmcode.org/osmium/latest/osmium-tags-filter.html</a></p>
</div>
<div id="comment-84222-info" class="comment-info">
<span class="comment-age">(19 Apr '22, 17:51)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84218-form-container" class="comment-form-container">
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

