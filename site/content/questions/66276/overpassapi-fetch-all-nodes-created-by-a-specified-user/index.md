+++
type = "question"
title = "[closed] OverpassAPI: fetch all nodes created by a specified user"
description = '''I&#x27;d like to list the nodes that were created by a specified user with the Overpass API. After stumbling on this wiki section I was able to fetch all nodes &quot;touched&quot; by a user. I tested my own username, and as expected it returns all the nodes I&#x27;ve created and edited. https://www.overpass-api.de/api/...'''
date = "2018-10-11T03:36:00Z"
lastmod = "2018-10-12T08:15:00Z"
weight = 66276
keywords = [ "overpass", "version", "user", "query" ]
aliases = [ "/questions/66276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] OverpassAPI: fetch all nodes created by a specified user](/questions/66276/overpassapi-fetch-all-nodes-created-by-a-specified-user)

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
<span id="post-66276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66276-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to list the nodes that were created by a specified user with the Overpass API.</p>
<p>After stumbling on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_user_.28user.2C_uid.29">this wiki section</a> I was able to fetch all nodes "touched" by a user.</p>
<p>I tested my own username, and as expected it returns all the nodes I've <strong>created and edited</strong>. <a href="https://www.overpass-api.de/api/interpreter?data=%5Bout:json%5D;node(user:%22robinmetral%22);out;">https://www.overpass-api.de/api/interpreter?data=[out:json];node(user:"robinmetral");out;</a></p>
<p>However I'm looking for a way to fetch only the nodes that a specified user has <strong>created</strong>, i.e. added to OSM for the first time (version 1).</p>
<p>Is there a way to do this? By looking at if the user has created the node's version 1 perhaps? Any inputs are welcome :)</p>
<p>Thanks for your help!</p>
<p>Side question: the wiki says that "<em>the user filter selects all <strong>elements that have been last touched</strong> by the specified user</em>". Why "last"? Does it select a limited number of elements?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '18, 03:36</strong></p>
<img src="https://secure.gravatar.com/avatar/f9fe45b76971785fd9287f048e9d3ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robinmetral&#39;s gravatar image" />
<p><span>robinmetral</span><br />
<span class="score" title="186 reputation points">186</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robinmetral has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>20 Oct '18, 12:43</strong> </span></p>
</div>
</div>
<div id="comments-container-66276" class="comments-container">
<span id="66277"></span>
<div id="comment-66277" class="comment">
<div id="post-66277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AFAIK, it is not possible to retrieve only revision 1 nodes via Overpass API.</p>
</div>
<div id="comment-66277-info" class="comment-info">
<span class="comment-age">(11 Oct '18, 04:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="66280"></span>
<div id="comment-66280" class="comment">
<div id="post-66280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm. Do you know of other possible solutions? Or would this be the only way?</p>
</div>
<div id="comment-66280-info" class="comment-info">
<span class="comment-age">(11 Oct '18, 04:45)</span> <span class="comment-user userinfo">robinmetral</span>
</div>
</div>
<span id="66287"></span>
<div id="comment-66287" class="comment">
<div id="post-66287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oooh I think I might have found a way using the OSM API instead of Overpass.</p>
<p>Looking at the history of a node with several versions (<a href="https://www.openstreetmap.org/api/0.6/node/3395080851/history">example in XML</a>) I might be able to extract the user of version 1!</p>
<p>I'll look into it, but feel free to give me a hand if you know how to convert this XML to JSON and fetch it! :)</p>
</div>
<div id="comment-66287-info" class="comment-info">
<span class="comment-age">(11 Oct '18, 10:07)</span> <span class="comment-user userinfo">robinmetral</span>
</div>
</div>
</div>
<div id="comment-tools-66276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66276-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, but I can not accept my own answer" by robinmetral 20 Oct '18, 12:43

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="66307"></span>

<div id="answer-container-66307" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So after some research, I solved my own question! I thought I'd post it on here in case someone else is looking for a similar solution.</p>
<p><strong>Clarification</strong>: though I first asked how to list all nodes created by a specific user (because I thought it would be more straightforward), in my case what I really wanted was to <strong>check whether a list of nodes were created by a specified user</strong>.</p>
<p>I was able to do this through the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">OpenStreetMap API</a> (not the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>).</p>
<p>Basically, I use the following request syntax in a JavaScript <code>XMLHttpRequest</code>:</p>
<pre><code>https://api.openstreetmap.org/api/0.6/nodes?nodes=100v1,101v1,102v1,103v1 // etc.</code></pre>
<p>Then I parse the XML response to get the value of the <code>user=""</code> class in each node.</p>
<p>Here are the relevant docs sections about <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Version:_GET_.2Fapi.2F0.6.2F.5Bnode.7Cway.7Crelation.5D.2F.23id.2F.23version">retrieving an element's specific version</a> and about <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:_GET_.2Fapi.2F0.6.2F.5Bnodes.7Cways.7Crelations.5D.3F.23parameters">fetching multiple elements at once</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '18, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f9fe45b76971785fd9287f048e9d3ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robinmetral&#39;s gravatar image" />
<p><span>robinmetral</span><br />
<span class="score" title="186 reputation points">186</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robinmetral has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66307" class="comments-container">
&#10;</div>
<div id="comment-tools-66307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66307-form-container" class="comment-form-container">
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

