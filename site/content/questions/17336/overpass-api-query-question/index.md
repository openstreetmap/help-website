+++
type = "question"
title = "Overpass API query question"
description = '''I was looking at the overpass API wiki trying to figure out how it works. I cannot seem to get it all the way. I am close! How do I get all the bicycle routes in Germany downloaded in one file? I have downloaded the germany.osm file from geofabrik but it does not seem to have all the ways and nodes ...'''
date = "2012-10-31T19:51:00Z"
lastmod = "2012-11-02T15:22:00Z"
weight = 17336
keywords = [ "overpass", "relation" ]
aliases = [ "/questions/17336" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API query question](/questions/17336/overpass-api-query-question)

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
<span id="post-17336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17336-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was looking at the overpass API wiki trying to figure out how it works. I cannot seem to get it all the way. I am close! How do I get all the bicycle routes in Germany downloaded in one file? I have downloaded the germany.osm file from geofabrik but it does not seem to have all the ways and nodes that are referenced for a given relation that has the name/value pair of route/bicycle. So, I looked at overpass API to see if I can get all the bicycle routes including all their ways, nodes, and relations but cannot seem to be able to wrote that query successfully. Tried something like this but nothing is returned. Any suggestion would be greatly appreciated.</p>
<p>&lt;union&gt; &lt;query type="relation"&gt; &lt;has-kv k="route" v="bicycle"/&gt; &lt;/query&gt; &lt;recurse type="relation-node" into="nodes"/&gt; &lt;recurse type="relation-way"/&gt; &lt;recurse type="way-node"/&gt; &lt;/union&gt; &lt;print/&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '12, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17336" class="comments-container">
<span id="17362"></span>
<div id="comment-17362" class="comment">
<div id="post-17362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you define a target area that is limiting the output to a certain region?</p>
<p>Because I think without limiting you get data for the whole planet, or am I wrong?</p>
<p>You can define a boundingbox with free chosen values by you or add a boundary relation that is already in the OSM data as a kind of polygon.</p>
</div>
<div id="comment-17362-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 16:45)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="17376"></span>
<div id="comment-17376" class="comment">
<div id="post-17376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much!</p>
</div>
<div id="comment-17376-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 20:28)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-17336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17336-form-container" class="comment-form-container">
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

<span id="17372"></span>

<div id="answer-container-17372" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17372-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kcjailbirds has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, a bounding box is the right approach to limit the result to Germany. Please consider</p>
<p>&lt;union&gt; &lt;query type="relation"&gt; &lt;bbox-query s="47.5" n="55.0" w="6.0" e="15.0"/&gt; &lt;has-kv k="route" v="bicycle"/&gt; &lt;/query&gt; &lt;recurse type="relation-node" into="nodes"/&gt; &lt;recurse type="relation-way"/&gt; &lt;recurse type="way-node"/&gt; &lt;/union&gt; &lt;print/&gt;</p>
<p>However, this is still a really huge download; please expect more than 100 MB and up to an hour waiting time. To tell this the server you need to set a larger timeout:</p>
<p>&lt;osm-script timeout="3600"&gt; &lt;union&gt; &lt;query type="relation"&gt; &lt;bbox-query s="47.5" n="55.0" w="6.0" e="15.0"/&gt; &lt;has-kv k="route" v="bicycle"/&gt; &lt;/query&gt; &lt;recurse type="relation-node" into="nodes"/&gt; &lt;recurse type="relation-way"/&gt; &lt;recurse type="way-node"/&gt; &lt;/union&gt; &lt;print/&gt; &lt;osm-script&gt;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '12, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-17372" class="comments-container">
<span id="17375"></span>
<div id="comment-17375" class="comment">
<div id="post-17375-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much!</p>
</div>
<div id="comment-17375-info" class="comment-info">
<span class="comment-age">(01 Nov '12, 20:27)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17408"></span>
<div id="comment-17408" class="comment">
<div id="post-17408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The query worked as advertised! The query gave me all the nodes and ways that were referenced by a relation and all the nodes within the ways. How can I modify this query to also give me all the relations that are referenced within a relation and all the nodes, ways, and nodes within ways for that referenced relation in addition to what it gave me? Of course I can change the box to a smaller area at a time.</p>
</div>
<div id="comment-17408-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 12:56)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17411"></span>
<div id="comment-17411" class="comment">
<div id="post-17411-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, please use &lt;osm-script timeout="3600"&gt; &lt;union&gt; &lt;query type="relation"&gt; &lt;bbox-query s="47.5" n="55.0" w="6.0" e="15.0"/&gt; &lt;has-kv k="route" v="bicycle"/&gt; &lt;/query&gt; &lt;recurse type="down-rel"/&gt; &lt;/union&gt; &lt;print/&gt; &lt;osm-script&gt;</p>
<p>For the sake of completeness, the query that resolves olny ways and nodes can be abbreviated as &lt;osm-script timeout="3600"&gt; &lt;union&gt; &lt;query type="relation"&gt; &lt;bbox-query s="47.5" n="55.0" w="6.0" e="15.0"/&gt; &lt;has-kv k="route" v="bicycle"/&gt; &lt;/query&gt; &lt;recurse type="down"/&gt; &lt;/union&gt; &lt;print/&gt; &lt;osm-script&gt;</p>
</div>
<div id="comment-17411-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 13:52)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="17416"></span>
<div id="comment-17416" class="comment">
<div id="post-17416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much Roland! I am trying that now. Is there a way to instead of defining a box, define the actual boundaries around Germany? If so, How do I get the actual boundaries around germany? When I put a box around it, it pulls in relations that are actually outside Germany and in other countries like Czech Republic. I am trying to see if I can restrict it to Just Germany. Later on, I need to do it for each individual city in Germany. Thank you very much for all you help.</p>
</div>
<div id="comment-17416-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 15:22)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-17372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17372-form-container" class="comment-form-container">
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

