+++
type = "question"
title = "[Overpass-api] How to get all relations for a node/way?"
description = '''Speaking in Overpass QL I can select a node by its ID: node(3815147164);out; This however doesn&#x27;t provide any info about relations or ways this node is a part of. Going to OSM site: http://www.openstreetmap.org/node/3815147164 I can see at least which ways the node belongs to. And then to the way pa...'''
date = "2016-01-29T07:44:00Z"
lastmod = "2016-01-29T14:59:00Z"
weight = 47725
keywords = [ "overpass", "relations" ]
aliases = [ "/questions/47725" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [\[Overpass-api\] How to get all relations for a node/way?](/questions/47725/overpass-api-how-to-get-all-relations-for-a-nodeway)

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
<span id="post-47725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47725-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Speaking in Overpass QL I can select a node by its ID:</p>
<p><code>node(3815147164);out;</code></p>
<p>This however doesn't provide any info about relations or ways this node is a part of.</p>
<p>Going to OSM site: <a href="http://www.openstreetmap.org/node/3815147164">http://www.openstreetmap.org/node/3815147164</a> I can see at least which ways the node belongs to. And then to the way page: <a href="http://www.openstreetmap.org/way/136322077">http://www.openstreetmap.org/way/136322077</a> I see its relations.</p>
<p>In Overpass relations are not returned, even for the way query:</p>
<p><code>way(136322077);out;</code></p>
<p>Any ideas how to get relations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '16, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '16, 10:17</strong> </span></p>
</div>
</div>
<div id="comments-container-47725" class="comments-container">
&#10;</div>
<div id="comment-tools-47725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47725-form-container" class="comment-form-container">
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

<span id="47739"></span>

<div id="answer-container-47739" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47739-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API only returns objects that are explicitly included in the query. To fetch the parents of an input set, use <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_up_.28.3C.29">recurse up</a>:</p>
<pre><code>(node(3815147164);
&lt;;
);
out geom;</code></pre>
<p>Note that <code>&lt;</code> does not fetch the parents of relations, use <code>&lt;&lt;</code> for that.</p>
<p>There are also some more fine grained operators if you only want the parent ways of nodes or whatever:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '16, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-47739" class="comments-container">
&#10;</div>
<div id="comment-tools-47739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47739-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47727"></span>

<div id="answer-container-47727" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47727-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://www.openstreetmap.org/node/3815147164">Node 3815147164</a> is not part of any relation itself. It is part of <a href="http://www.openstreetmap.org/way/136322077">way 136322077</a> which in turn is part of a relation. You already seem to have figured this out by yourself but your question is still a little bit misleading.</p>
<p>You don't need Overpass API for returning the ways a node is part of, see <a href="http://www.openstreetmap.org/api/0.6/node/3815147164/ways">http://www.openstreetmap.org/api/0.6/node/3815147164/ways</a>. And you don't need Overpass API for returning the relation a node or way is part of, see <a href="http://www.openstreetmap.org/api/0.6/way/136322077/relations">http://www.openstreetmap.org/api/0.6/way/136322077/relations</a>.</p>
<p>If this doesn't really answer your question then maybe someone can come up with an Overpass API query for returning the relation(s) containing way(s) a node is part of.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '16, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '16, 09:23</strong> </span></p>
</div>
</div>
<div id="comments-container-47727" class="comments-container">
<span id="47729"></span>
<div id="comment-47729" class="comment">
<div id="post-47729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, you are right. I've changed the title a bit, to match my intention in a better way.</p>
<p>I'd like to have a pure Overpass solution and not having to mix different APIs in the same application.</p>
</div>
<div id="comment-47729-info" class="comment-info">
<span class="comment-age">(29 Jan '16, 10:19)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
</div>
<div id="comment-tools-47727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47727-form-container" class="comment-form-container">
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

