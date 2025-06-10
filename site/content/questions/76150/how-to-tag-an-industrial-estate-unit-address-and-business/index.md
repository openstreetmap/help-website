+++
type = "question"
title = "How to tag an industrial estate unit address and business"
description = '''Given an address like: Boulder Hut Unit 1, Olympic Park Poole Hall Road Ellesmere Port CH66 1ST I can add: addr:street=Poole Hall Road addr:city=Ellesmere Port addr:postcode=CH66 1ST  but what to do about the Unit number (it&#x27;s one big warehouse so addr:unit doesn&#x27;t seem to fit) or industrial estate ...'''
date = "2020-08-16T22:53:00Z"
lastmod = "2020-08-17T15:02:00Z"
weight = 76150
keywords = [ "operator", "brand", "industrial", "estate", "address" ]
aliases = [ "/questions/76150" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag an industrial estate unit address and business](/questions/76150/how-to-tag-an-industrial-estate-unit-address-and-business)

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
<span id="post-76150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76150-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given an address like: Boulder Hut Unit 1, Olympic Park Poole Hall Road Ellesmere Port CH66 1ST</p>
<p>I can add:</p>
<pre><code>addr:street=Poole Hall Road
addr:city=Ellesmere Port
addr:postcode=CH66 1ST</code></pre>
<p>but what to do about the Unit number (it's one big warehouse so addr:unit doesn't seem to fit) or industrial estate (if I don't want to/can't map the area of the estate). Also, since I was planning to tag the building with the amenity info, presumably name should not be boulder hut since that isn't the name of the building itself. I could put brand, and there is a company name that I could add to operator. Is this a good way to do it (or other tags)? Or should I create a separate amenity node/area? In which case should the address go there?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-operator" rel="tag" title="see questions tagged &#39;operator&#39;">operator</span> <span class="post-tag tag-link-brand" rel="tag" title="see questions tagged &#39;brand&#39;">brand</span> <span class="post-tag tag-link-industrial" rel="tag" title="see questions tagged &#39;industrial&#39;">industrial</span> <span class="post-tag tag-link-estate" rel="tag" title="see questions tagged &#39;estate&#39;">estate</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '20, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/09dd5995d85d7b0636ebd94e1f49c463?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrekClimbing&#39;s gravatar image" />
<p><span>TrekClimbing</span><br />
<span class="score" title="161 reputation points">161</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrekClimbing has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '20, 22:54</strong> </span></p>
</div>
</div>
<div id="comments-container-76150" class="comments-container">
&#10;</div>
<div id="comment-tools-76150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76150-form-container" class="comment-form-container">
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

<span id="76161"></span>

<div id="answer-container-76161" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76161-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TrekClimbing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the building is only used to house a business then the <code>name=</code> tag can be used for the name of the business, <code>addr:housename</code> can also be used to record the building name if it is different.</p>
<p>It's a bit of a stretch, but you could potentially use <code>addr:suburb</code> for the industrial estate.</p>
<p>I wouldn't rule out <code>addr:unit</code> if some of the other warehouses are split up within the same numbering scheme, but if you really think it's inappropriate you could use <code>addr:housenumber</code>.</p>
<p>With addresses that are quite difficult to fit within existing schemes it may also be advisable to include <a href="https://wiki.openstreetmap.org/wiki/Key:addr#Commonly_used_subkeys"><code>addr:full</code></a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '20, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76161" class="comments-container">
&#10;</div>
<div id="comment-tools-76161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76161-form-container" class="comment-form-container">
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

