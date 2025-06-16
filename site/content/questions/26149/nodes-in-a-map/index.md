+++
type = "question"
title = "nodes in a map"
description = '''how many nodes you can upload in a map each time and how? one node I can upload by an url but for example 1000 nodes? tks a lot braulio'''
date = "2013-09-05T18:58:00Z"
lastmod = "2013-09-17T23:28:00Z"
weight = 26149
keywords = [ "maps", "nodes" ]
aliases = [ "/questions/26149" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nodes in a map](/questions/26149/nodes-in-a-map)

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
<span id="post-26149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26149-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how many nodes you can upload in a map each time and how?</p>
<p>one node I can upload by an url but for example 1000 nodes?</p>
<p>tks a lot</p>
<p>braulio</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '13, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/300e7bf9adffb75b9e753ca65679d93f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brau1308&#39;s gravatar image" />
<p><span>brau1308</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brau1308 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26149" class="comments-container">
<span id="26150"></span>
<div id="comment-26150" class="comment">
<div id="post-26150-score" class="comment-score">
7
</div>
<div class="comment-text">
<p>Can you rephrase your question to explain what you want to do? While there is a correct technical answer to the question you've asked, it suggess that you're trying to do something more complex, like import a set of data in bulk, which is a different matter.</p>
</div>
<div id="comment-26150-info" class="comment-info">
<span class="comment-age">(05 Sep '13, 19:21)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-26149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26149-form-container" class="comment-form-container">
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

<span id="26457"></span>

<div id="answer-container-26457" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26457-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API v0.6 is currently places limits (defined by the server configuration) for the total number of elements allowed in a changeset, and the maximum number of nodes that a single way may contain. As of now, these limits are:</p>
<ul>
<li>Maximum of 50k elements (nodes + ways + relations) per changeset;</li>
<li>Maximum of 2k nodes per way.</li>
</ul>
<p>You can get the current values requesting the current API capabilities, using the functionality built-in, as described in the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Capabilities:_GET_.2Fapi.2Fcapabilities">API v0.6</a> documentation. For the public API server, see its <a href="https://www.openstreetmap.org/api/capabilities">Current Capabilities</a>.</p>
<p>It is very uncommon to reach those limits in common, urban editing, but quite possible when editing large bodies of water. I would recommend that when a way is close to half the maximum number of nodes (in this case, 1k nodes), it should be broken in two parts, one with 1k nodes and the other with the remainder of the nodes, and creating (or updating) the relevant relation. This way, it is possible to edit the element with very low risk of it reaching the limit again.</p>
<p>I never reached the maximum number of elements in a changeset, but created more than one with somewhat more than 20k elements - without any problem when uploading.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '13, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-26457" class="comments-container">
&#10;</div>
<div id="comment-tools-26457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26457-form-container" class="comment-form-container">
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

