+++
type = "question"
title = "Getting addresses of residential buildings with information about the locality type"
description = '''Hi! I&#x27;m new to OSM.  I need to get a list of addresses of residential buildings with information about the locality type (village or city).  When I receive a list of nodes and select residential buildings, I do not receive information about the type of locality. As I understand it, this information ...'''
date = "2023-10-19T16:29:00Z"
lastmod = "2023-10-19T16:29:00Z"
weight = 87924
keywords = [ "map", "export", "data", "parsing" ]
aliases = [ "/questions/87924" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting addresses of residential buildings with information about the locality type](/questions/87924/getting-addresses-of-residential-buildings-with-information-about-the-locality-type)

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
<span id="post-87924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87924-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I'm new to OSM.</p>
<p>I need to get a list of addresses of residential buildings with information about the locality type (village or city).</p>
<p>When I receive a list of nodes and select residential buildings, I do not receive information about the type of locality. As I understand it, this information is contained in the relation or related objects. How i can add this information to target nodes?</p>
<p>I'm doing it:</p>
<pre><code>osmconvert.exe target-area.osm.pbf --all-to-nodes --max-objects=1000000000 -o=target-nodes.xml
osmfilter.exe target-nodes.xml --keep-nodes=&quot;building=residential or building=village or ... &quot; -o=buildings.xml</code></pre>
<p>... and then get the addresses from the received nodes.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '23, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/3e985249dd71bc5e82e4358b8bf53e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evsar&#39;s gravatar image" />
<p><span>evsar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evsar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87924" class="comments-container">
&#10;</div>
<div id="comment-tools-87924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87924-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

