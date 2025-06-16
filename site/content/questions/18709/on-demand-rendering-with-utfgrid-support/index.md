+++
type = "question"
title = "On-demand rendering with UTFgrid support?"
description = '''What would it need to serve live rendered tiles (such as in mod_tile / Tirex) with UTFgrid .json files? mod_tile does not seem to support UTFgrid. Does Tirex?  TileStream only can serve pre-rendered MBtiles. Is there any working alternative?'''
date = "2012-12-26T12:57:00Z"
lastmod = "2012-12-27T10:16:00Z"
weight = 18709
keywords = [ "rendering", "utfgrid", "mapnik" ]
aliases = [ "/questions/18709" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [On-demand rendering with UTFgrid support?](/questions/18709/on-demand-rendering-with-utfgrid-support)

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
<span id="post-18709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18709-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What would it need to serve live rendered tiles (such as in mod_tile / Tirex) with UTFgrid .json files? <a href="/questions/17856/utfgrid-support-in-mod_tile">mod_tile does not seem to support UTFgrid</a>. Does Tirex?</p>
<p>TileStream only can serve pre-rendered MBtiles.</p>
<p>Is there any working alternative?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-utfgrid" rel="tag" title="see questions tagged &#39;utfgrid&#39;">utfgrid</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '12, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '12, 12:57</strong> </span></p>
</div>
</div>
<div id="comments-container-18709" class="comments-container">
&#10;</div>
<div id="comment-tools-18709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18709-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="18710"></span>

<div id="answer-container-18710" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18710-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>TileMill actually can be used as an tileserver.</p>
<p>Edit the config.json and add the following (as shown <a href="http://mapbox.com/tilemill/docs/guides/ubuntu-service/#configuring_to_listen_for_public_traffic">in the TileMill docs</a>)</p>
<pre><code>  &quot;listenHost&quot;: &quot;0.0.0.0&quot;,
  &quot;coreUrl&quot;: &quot;127.0.0.1:20009&quot;,
  &quot;tileUrl&quot;: &quot;0.0.0.0:20008&quot;,
  &quot;server&quot;: true</code></pre>
<p>Tiles then would be surfed under for example:</p>
<p><a href="http://0.0.0.0:20008/tile/ProjectName/z/x/y.png">http://0.0.0.0:20008/tile/ProjectName/z/x/y.png</a></p>
<p>and the UTFgrid info under</p>
<p><a href="http://0.0.0.0:20008/tile/ProjectName/z/x/y.grid.json">http://0.0.0.0:20008/tile/ProjectName/z/x/y.grid.json</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '12, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18710" class="comments-container">
&#10;</div>
<div id="comment-tools-18710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18710-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18713"></span>

<div id="answer-container-18713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest way to get the {tirex|renderd}/mod_tile toolchain to support per-tile metadata - UTFgrid, Metawriter, or others - would probably be to extend the meta tiles used by these systems, which currently contain the PNG data only, to also include the extra data.</p>
<p>Since these systems usually render a larger area - typically, 8x8 tiles - in one go for performance reasons, and cut up the resulting PNG into tiles afterwards, you'd have to make sure the metadata is treated similarly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18713" class="comments-container">
&#10;</div>
<div id="comment-tools-18713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18713-form-container" class="comment-form-container">
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

