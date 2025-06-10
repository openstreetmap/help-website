+++
type = "question"
title = "How do make nodes appear in `network_type=drive`?"
description = '''Hello,  I created a lot of nodes, e.g. 9955159975. However they are not in the graph resulted by calling: ox.graph_from_bbox(-23.46, -23.75, -46.5, -46.77, network_type=&#x27;drive&#x27;, simplify=False). I noticed that when changed to the network type all they are appearing. How can I change the nodes to sho...'''
date = "2022-08-16T14:54:00Z"
lastmod = "2022-08-17T09:49:00Z"
weight = 85355
keywords = [ "osmnx", "nodes", "osm", "drive" ]
aliases = [ "/questions/85355" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do make nodes appear in \`network_type=drive\`?](/questions/85355/how-do-make-nodes-appear-in-network_typedrive)

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
<span id="post-85355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85355-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I created a lot of nodes, e.g. 9955159975. However they are not in the graph resulted by calling: <code>ox.graph_from_bbox(-23.46, -23.75, -46.5, -46.77, network_type='drive', simplify=False)</code>.</p>
<p>I noticed that when changed to the network type <code>all</code> they are appearing. How can I change the nodes to show in the <code>drive</code> result?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmnx" rel="tag" title="see questions tagged &#39;osmnx&#39;">osmnx</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-drive" rel="tag" title="see questions tagged &#39;drive&#39;">drive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '22, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/9a0e02695d667bd051c8b34ed0d76892?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vwraposo&#39;s gravatar image" />
<p><span>vwraposo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vwraposo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '22, 09:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-85355" class="comments-container">
<span id="85356"></span>
<div id="comment-85356" class="comment">
<div id="post-85356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain in a bit more detail what your goal is here?</p>
</div>
<div id="comment-85356-info" class="comment-info">
<span class="comment-age">(16 Aug '22, 15:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85358"></span>
<div id="comment-85358" class="comment">
<div id="post-85358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We were adding points for restricted zones for trucks. And we want to take them into account when computing paths. It seems that now the API returned the correct points, there must be a long time for it to return or a long cache somewhere</p>
</div>
<div id="comment-85358-info" class="comment-info">
<span class="comment-age">(16 Aug '22, 16:05)</span> <span class="comment-user userinfo">vwraposo</span>
</div>
</div>
<span id="85359"></span>
<div id="comment-85359" class="comment">
<div id="post-85359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah - so you're using some other piece of software (which you haven't told us about) which gets information from OSM and determines whether a particular route is suitable for a particular type of vehicle.</p>
<p>Because they have to create their own routing graph, routers tend to update slower than some other OSM consumers.</p>
</div>
<div id="comment-85359-info" class="comment-info">
<span class="comment-age">(16 Aug '22, 16:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85365"></span>
<div id="comment-85365" class="comment">
<div id="post-85365-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This question seems to be about OSMnx. I've added the corresponding tag.</p>
</div>
<div id="comment-85365-info" class="comment-info">
<span class="comment-age">(17 Aug '22, 09:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85355-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

