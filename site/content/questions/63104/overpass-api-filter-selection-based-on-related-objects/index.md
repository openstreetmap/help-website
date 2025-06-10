+++
type = "question"
title = "Overpass API: Filter selection based on related objects"
description = '''Hi everyone I&#x27;m trying to get all nodes with tag &quot;entrance&quot;=&quot;main&quot; which are part of a relation with ways that have the tag &quot;building&quot;=&quot;train_station&quot; through the Overpass Turbo API. I searched https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL for it but couldn&#x27;t find a matching example. ...'''
date = "2018-04-24T15:28:00Z"
lastmod = "2018-04-26T08:22:00Z"
weight = 63104
keywords = [ "overpass", "overpass-turbo", "relations" ]
aliases = [ "/questions/63104" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: Filter selection based on related objects](/questions/63104/overpass-api-filter-selection-based-on-related-objects)

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
<span id="post-63104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone I'm trying to get all nodes with tag "entrance"="main" which are part of a relation with ways that have the tag "building"="train_station" through the Overpass Turbo API. I searched <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a> for it but couldn't find a matching example.</p>
<p>Any help with this issue would be appreciated a lot :-)</p>
<p>Greetings, Egaru</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '18, 15:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e4a051b3f251672ff56bf53262a34976?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Egaru&#39;s gravatar image" />
<p><span>Egaru</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Egaru has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63104" class="comments-container">
<span id="63107"></span>
<div id="comment-63107" class="comment">
<div id="post-63107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There wouldn't typically be a reason for there to be a relation like you describe, so even if you could create the right query, it probably wouldn't find any results.</p>
</div>
<div id="comment-63107-info" class="comment-info">
<span class="comment-age">(24 Apr '18, 17:31)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-63104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63104-form-container" class="comment-form-container">
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

<span id="63111"></span>

<div id="answer-container-63111" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63111-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Egaru has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">filters to directly make the steps that you specify</a>;</p>
<p><a href="http://overpass-turbo.eu/s/ycW">Here's a working script</a> (I've used entrance instead of entrance=main to make it quicker to test):</p>
<pre><code>[bbox:{{bbox}}];
way[building=train_station];
rel(bw);
node(r)[entrance];
out;</code></pre>
<p>I guess without a bounding box it will be slow or timeout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '18, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63111" class="comments-container">
<span id="63119"></span>
<div id="comment-63119" class="comment">
<div id="post-63119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your responses! Perhaps my question was a bit vaguely phrased so I try again :-)</p>
<p>With the query <em>node<a href="%7B%7Bbbox%7D%7D">"entrance"=main</a>;</em> I get main entrances as nodes. However, it could be the entrance of a library, railway station, town hall or anything else. To reduce the nodes to such belonging to railway stations, I need to filter them. When I select the node on the map and click on the node ID, I see in the "Part of" section, that it belongs to a way having the tag building=station. Thus I think these objects are related and thus can be used in a query.</p>
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>: Unfortunately this query doesn't return any objects. Is it intended to work in the way I tried to explain above?</p>
</div>
<div id="comment-63119-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 07:25)</span> <span class="comment-user userinfo">Egaru</span>
</div>
</div>
<span id="63133"></span>
<div id="comment-63133" class="comment">
<div id="post-63133-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There might not be any matching data.</p>
<p>This query just looks for entrance nodes that are part of building=train_station ways: <a href="http://overpass-turbo.eu/s/yfy">http://overpass-turbo.eu/s/yfy</a></p>
</div>
<div id="comment-63133-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 12:25)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="63153"></span>
<div id="comment-63153" class="comment">
<div id="post-63153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've found the problem: The region I chose for testing had the tag building=station instead of building=train_station. Taking the union of both tags yielded the desired result:</p>
<p>[bbox:45.10378,5.53772,47.54818,9.49703]; (way[building=station]; way[building=train_station];); node(w)[entrance]; out;</p>
<p>Thanks a lot for your help!</p>
</div>
<div id="comment-63153-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 08:22)</span> <span class="comment-user userinfo">Egaru</span>
</div>
</div>
</div>
<div id="comment-tools-63111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63111-form-container" class="comment-form-container">
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

