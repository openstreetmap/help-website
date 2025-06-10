+++
type = "question"
title = "Overpass-api sends an error Index inconsistent."
description = '''my attempt to retrieve: http://overpass-api.de/api/map?bbox=19.3813,39.0555,21.5373,40.0718 provides the answer: &amp;lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&amp;gt; &amp;lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API&quot;&amp;gt; &amp;lt;note&amp;gt;The data included in this document is from www.openstreetmap.org. The data is m...'''
date = "2017-07-20T22:52:00Z"
lastmod = "2017-07-21T08:52:00Z"
weight = 57215
keywords = [ "overpassapi", "index", "error" ]
aliases = [ "/questions/57215" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass-api sends an error Index inconsistent.](/questions/57215/overpass-api-sends-an-error-index-inconsistent)

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
<span id="post-57215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57215-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>my attempt to retrieve: <a href="http://overpass-api.de/api/map?bbox=19.3813,39.0555,21.5373,40.0718">http://overpass-api.de/api/map?bbox=19.3813,39.0555,21.5373,40.0718</a></p>
<p>provides the answer: &lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;osm version="0.6" generator="Overpass API"&gt; &lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt; &lt;meta osm_base="2017-07-19T23:01:03Z"/&gt; &lt;bounds minlat="39.0917000" minlon="19.2783000" maxlat="39.9403000" maxlon="20.2959000"/&gt; &lt;remark&gt; <strong>runtime error: open64: 1500 Unknown error 1500 /opt/osm-3s/v0.7.54/db/relations.bin File_Blocks::read_block: Index inconsistent</strong> &lt;/remark&gt; &lt;/osm&gt;</p>
<p>is there something I should do locally to retrieve the dataset or is it a server error that should be corrected ? -&gt; I prefer using overpassapi but for the time being I can look at another source for this dataset (will try with geofabrik)... thx</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '17, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6b4cc43a00b92c715b072359d8597198?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jc67&#39;s gravatar image" />
<p><span>jc67</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jc67 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57215" class="comments-container">
&#10;</div>
<div id="comment-tools-57215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57215-form-container" class="comment-form-container">
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

<span id="57218"></span>

<div id="answer-container-57218" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57218-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This might be a result of the recent server issues, see <a href="https://lists.openstreetmap.org/pipermail/talk/2017-July/078321.html">https://lists.openstreetmap.org/pipermail/talk/2017-July/078321.html</a> and <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/status">http://wiki.openstreetmap.org/wiki/Overpass_API/status</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '17, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-57218" class="comments-container">
&#10;</div>
<div id="comment-tools-57218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57218-form-container" class="comment-form-container">
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

