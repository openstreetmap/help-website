+++
type = "question"
title = "[closed] Parse Tiger Data Exception"
description = '''Hi to all, After nominatim-2.3.1 installed successfully, I want to import tiger data into nominatim database. Also installed gdal-python.  $gdalinfo --version  GDAL 1.11.2, released 2015/02/10  When I execute the cmd for parse tigerdata, I got the below Exception: ./Nominatim-2.3.1/utils/imports.php...'''
date = "2015-07-22T08:16:00Z"
lastmod = "2015-08-05T08:23:00Z"
weight = 44335
keywords = [ "tiger", "python", "nominatim", "parser", "ogr2osm" ]
aliases = [ "/questions/44335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Parse Tiger Data Exception](/questions/44335/parse-tiger-data-exception)

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
<span id="post-44335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44335-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>After nominatim-2.3.1 installed successfully, I want to import tiger data into nominatim database. Also installed gdal-python.</p>
<blockquote>
<p>$gdalinfo --version <strong>GDAL 1.11.2, released 2015/02/10</strong></p>
</blockquote>
<p>When I execute the cmd for parse tigerdata, I got the below Exception:</p>
<p><strong>./Nominatim-2.3.1/utils/imports.php --parse-tiger-2011 TIGERDATA/EDGES/</strong></p>
<blockquote>
<p><strong>Processing 15005... Traceback (most recent call last): File "Nominatim-2.3.1/utils/tigerAddressImport.py", line 50, in &lt;module&gt; import ogr ImportError:No module named ogr Failed parse (TIGERDATA/EDGES/tl_2013_15005_edges.zip)</strong></p>
</blockquote>
<p>Also I tried as ./Nominatim-2.3.1/utils/imports.php --parse-tiger TIGERDATA/EDGES/</p>
<p>But there is no logs(not processing my request)</p>
<p>Kindly help me for fix the above issue/Exception.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-parser" rel="tag" title="see questions tagged &#39;parser&#39;">parser</span> <span class="post-tag tag-link-ogr2osm" rel="tag" title="see questions tagged &#39;ogr2osm&#39;">ogr2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '15, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>26 Aug '15, 17:35</strong> </span></p>
</div>
</div>
<div id="comments-container-44335" class="comments-container">
&#10;</div>
<div id="comment-tools-44335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44335-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by Rajavelu_M 26 Aug '15, 17:35

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44618"></span>

<div id="answer-container-44618" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44618-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>ImportError:No module named ogr</p>
</blockquote>
<p>Yes. python library ogr not installed properly, So only I met that err, Now I fixed &amp; working fine.</p>
<p>But as per wiki,</p>
<p>Convert the data into SQL statements (stored in data/tiger2011):</p>
<p><strong>./utils/imports.php --parse-tiger-2011 tiger_edge_data_directory</strong></p>
<p>Attention:when using the latest development version, use <strong>--parse-tiger.</strong></p>
<p>But not working --parse-tiger in nominatim-2.3.1 , we need to execute as --parse-tiger-2011.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '15, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '15, 08:43</strong> </span></p>
</div>
</div>
<div id="comments-container-44618" class="comments-container">
&#10;</div>
<div id="comment-tools-44618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44618-form-container" class="comment-form-container">
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

