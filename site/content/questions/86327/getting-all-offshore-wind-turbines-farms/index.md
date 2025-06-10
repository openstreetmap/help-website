+++
type = "question"
title = "Getting all offshore wind-turbines farms"
description = '''Hello,  I would like to have all the turbines of all offshore wind-farms in the world, I have tried these but a lot are still missing: /* This query looks for nodes, ways and relations  with the given key/value combination. Choose your region and hit the Run button above! */ [out:json][timeout:25]; ...'''
date = "2022-12-09T14:40:00Z"
lastmod = "2022-12-09T14:40:00Z"
weight = 86327
keywords = [ "turbine", "offshore", "wind" ]
aliases = [ "/questions/86327" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting all offshore wind-turbines farms](/questions/86327/getting-all-offshore-wind-turbines-farms)

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
<span id="post-86327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86327-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to have all the turbines of all offshore wind-farms in the world,</p>
<p>I have tried these but a lot are still missing:</p>
<pre><code>/*
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
*/
[out:json][timeout:25];
// gather results
(
  // query part for: “&quot;generator:source&quot;=wind”
  node[&quot;generator:source&quot;=&quot;wind&quot;]({{bbox}});
  way[&quot;generator:source&quot;=&quot;wind&quot;]({{bbox}});
  relation[&quot;generator:source&quot;=&quot;wind&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>but a lot are still missing</p>
<p>Any help would be more than welcome</p>
<p>R</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turbine" rel="tag" title="see questions tagged &#39;turbine&#39;">turbine</span> <span class="post-tag tag-link-offshore" rel="tag" title="see questions tagged &#39;offshore&#39;">offshore</span> <span class="post-tag tag-link-wind" rel="tag" title="see questions tagged &#39;wind&#39;">wind</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Dec '22, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/48470db55dde75a97ea6de422c5a418c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lamri19&#39;s gravatar image" />
<p><span>Lamri19</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lamri19 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '22, 15:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-86327" class="comments-container">
&#10;</div>
<div id="comment-tools-86327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86327-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

