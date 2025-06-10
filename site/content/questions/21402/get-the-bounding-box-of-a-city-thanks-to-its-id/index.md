+++
type = "question"
title = "Get the bounding box of a city thanks to its ID"
description = '''Hello, I&#x27;m using Overpass API and I&#x27;m looking for a way to get everything which is in a city determined by the ID of its node.  For instance, If we&#x27;re getting a closer look to London, it shows :   &amp;lt;node id=&quot;**107775**&quot; lat=&quot;51.5072759&quot; lon=&quot;-0.1276597&quot;&amp;gt;  &amp;lt;tag k=&quot;capital&quot; v=&quot;yes&quot;/&amp;gt;  &amp;lt;t...'''
date = "2013-04-11T12:20:00Z"
lastmod = "2013-04-15T17:10:00Z"
weight = 21402
keywords = [ "bounding", "box", "overpass", "id", "city" ]
aliases = [ "/questions/21402" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get the bounding box of a city thanks to its ID](/questions/21402/get-the-bounding-box-of-a-city-thanks-to-its-id)

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
<span id="post-21402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21402-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm using Overpass API and I'm looking for a way to get everything which is in a city determined by the ID of its node. For instance, If we're getting a closer look to London, it shows :</p>
<pre><code> &lt;node id=&quot;**107775**&quot; lat=&quot;51.5072759&quot; lon=&quot;-0.1276597&quot;&gt;
    &lt;tag k=&quot;capital&quot; v=&quot;yes&quot;/&gt;
    &lt;tag k=&quot;ele&quot; v=&quot;15&quot;/&gt;
    &lt;tag k=&quot;is_in&quot; v=&quot;England, United Kingdom, UK, Great Britain, Europe&quot;/&gt;
    &lt;tag k=&quot;is_in:continent&quot; v=&quot;Europe&quot;/&gt;
    &lt;tag k=&quot;is_in:country&quot; v=&quot;United Kingdom&quot;/&gt;
    &lt;tag k=&quot;media:commons&quot; v=&quot;https://commons.wikimedia.org/wiki/Category:London&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;London&quot;/&gt;
    [...]
    &lt;tag k=&quot;website&quot; v=&quot;http://www.london.gov.uk/&quot;/&gt;
    &lt;tag k=&quot;wikipedia&quot; v=&quot;en:London&quot;/&gt;
  &lt;/node&gt;</code></pre>
<p>I'd like to get the bounding box of this city thanks to its node ID (here : 107775). I managed to do this thanks to the name of the city by the request : (rel["name"='London'];&gt;;);out; But as you can see, in case of multiple places with the same name, you get multiple bounding box. That's the reason why I'd like to get this bounding box thanks to the ID of the node associated to the city.</p>
<p>So, to sum um, with this node : node(107775), is it possible to get the bounding box of the city ?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-box" rel="tag" title="see questions tagged &#39;box&#39;">box</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '13, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1e01b7993253cd6f5b2a7313012f493b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kobz&#39;s gravatar image" />
<p><span>Kobz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kobz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '13, 12:22</strong> </span></p>
</div>
</div>
<div id="comments-container-21402" class="comments-container">
<span id="21494"></span>
<div id="comment-21494" class="comment">
<div id="post-21494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not really sure that I understand your question (a bounding box based on a node?!?) - however, maybe it helps that many cities have their boundaries mapped like this: <a href="http://www.openstreetmap.org/browse/relation/62400">http://www.openstreetmap.org/browse/relation/62400</a> Note that this does not applies to every city (remarkably small ones) as OSM's data quality varies.</p>
</div>
<div id="comment-21494-info" class="comment-info">
<span class="comment-age">(13 Apr '13, 01:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21402-form-container" class="comment-form-container">
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

<span id="21551"></span>

<div id="answer-container-21551" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21551-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, it seems that you are not looking for exact bounding boxes of a certain city, but for its boundary relation.</p>
<p>Main problem: the binding from a node to its boundary relation is not completley mapped in the OSM data. There are some countries where you have boundary relations with one node as a member with the role admin_centre ... thus you ca find all place nodes that are member of a boundary relation.</p>
<p>But this binding is incomplete in the world, even in Germany this data model is not so widely spreaded.</p>
<p>see <a href="http://wiki.openstreetmap.org/wiki/Relation:boundary">Relation:boundary</a> in the OSM wiki.</p>
<p>Maybe also helpful: <a href="https://help.openstreetmap.org/questions/19925/overpass-get-relation-and-node-in-one-query-for-city">overpass-get-relation-and-node-in-one-query-for-city</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '13, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-21551" class="comments-container">
&#10;</div>
<div id="comment-tools-21551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21551-form-container" class="comment-form-container">
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

