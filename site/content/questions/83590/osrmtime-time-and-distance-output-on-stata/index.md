+++
type = "question"
title = "OSRMtime time and distance output on Stata"
description = '''Hi! I&#x27;m trying to use the osrmtime command in Stata environment in order to calculate percurrence time/distance in an automaded way. At the moment the command works but the output not. After a general run I get the following results:  list Origine Destinazione distance duration jumpdist1 jumpdist2 r...'''
date = "2022-02-27T09:58:00Z"
lastmod = "2022-02-27T09:58:00Z"
weight = 83590
keywords = [ "duration", "osrm", "osrmtime", "stata", "distance" ]
aliases = [ "/questions/83590" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSRMtime time and distance output on Stata](/questions/83590/osrmtime-time-and-distance-output-on-stata)

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
<span id="post-83590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83590-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm trying to use the osrmtime command in Stata environment in order to calculate percurrence time/distance in an automaded way. At the moment the command works but the output not. After a general run I get the following results:</p>
<blockquote>
<p>list Origine Destinazione distance duration jumpdist1 jumpdist2 return_code in 1/4</p>
</blockquote>
<pre><code> +------------------------------------------------------------------------------+
 | Origine   Destinazi~e   distance   duration   jumpdi~1   jumpdi~2   return~e |
 |------------------------------------------------------------------------------|
 | ALGHERO       ALGHERO          0          0    4064617    4064617         OK |
 | ALGHERO     BENETUTTI          0          0    4064617    3980292         OK |
 | ALGHERO          BONO          0          0    4064617    3990541         OK |
 | ALGHERO   CASTELSARDO          0          0    4064617    4051115         OK |
 +------------------------------------------------------------------------------+</code></pre>
<p>There are several problems in this output.</p>
<ol>
<li>Using the Italy latest map it seems it does not cover Sardinia area, it is possible?</li>
<li>duration and distance are set to 0 of every pair of itineraries;</li>
<li>jumpdist1 and jumpdist2 are in order 4000km as if I was using a map from, maybe, middle east.</li>
<li>return~e give code ok, that is not normally planned to be in the Stata journal article.</li>
</ol>
<p>Someone could give me some advice on it? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-osrmtime" rel="tag" title="see questions tagged &#39;osrmtime&#39;">osrmtime</span> <span class="post-tag tag-link-stata" rel="tag" title="see questions tagged &#39;stata&#39;">stata</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '22, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/344bdbdcd1a959d1bb0ac9f8b58828a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shardana&#39;s gravatar image" />
<p><span>Shardana</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shardana has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '22, 09:59</strong> </span></p>
</div>
</div>
<div id="comments-container-83590" class="comments-container">
&#10;</div>
<div id="comment-tools-83590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83590-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

