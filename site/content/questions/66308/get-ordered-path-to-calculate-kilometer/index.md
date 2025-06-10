+++
type = "question"
title = "Get ordered path to calculate kilometer"
description = '''Hi there, i have got a list of incident in Italian motorway and the kilometer where they happened. I should find lat and long of the event.  I extracted all nodes from the motorway using this script: [out:json][timeout:25]; //fetch area “Italy” to search in {{geocodeArea:Italy}}-&amp;gt;.searchArea; //g...'''
date = "2018-10-12T09:00:00Z"
lastmod = "2018-10-12T09:00:00Z"
weight = 66308
keywords = [ "ways", "path", "nodes", "overpass-turbo", "motorway" ]
aliases = [ "/questions/66308" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get ordered path to calculate kilometer](/questions/66308/get-ordered-path-to-calculate-kilometer)

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
<span id="post-66308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66308-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, i have got a list of incident in Italian motorway and the kilometer where they happened. I should find lat and long of the event. I extracted all nodes from the motorway using this script:</p>
<pre><code>[out:json][timeout:25];
//fetch area “Italy” to search in
{{geocodeArea:Italy}}-&gt;.searchArea;
//gather results
(
// query part for: “highway=motorway and ref=A14”
node[&quot;highway&quot;=&quot;motorway&quot;][&quot;ref&quot;=&quot;A14&quot;](area.searchArea);
way[&quot;highway&quot;=&quot;motorway&quot;][&quot;ref&quot;=&quot;A14&quot;](area.searchArea);
relation[&quot;highway&quot;=&quot;motorway&quot;][&quot;ref&quot;=&quot;A14&quot;](area.searchArea);
out body;
&gt;;
out skel qt;</code></pre>
<p>The problem is that while nodes are ordered (so i can calculate relative distance in km of a way), ways aren't. This means i can't create a path of way from the start of the street till the end.</p>
<p>Is there any way to order ways and calculate absolute distance in km?</p>
<p>Thanks for help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '18, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f11158996efb57d79291f693378bdac1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramingo92&#39;s gravatar image" />
<p><span>Ramingo92</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramingo92 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66308" class="comments-container">
&#10;</div>
<div id="comment-tools-66308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66308-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

