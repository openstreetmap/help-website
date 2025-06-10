+++
type = "question"
title = "How to look for nodes that has been created using Maps.me in an area?"
description = '''Hi everyone, Since editing OSM via Maps.Me has been enabled for users, I have seen some people are adding their homes or other personal addresses using this feature. (probably by mistake, instead of adding places as their favorites) I&#x27;m trying to get a list of nodes that has been created by this app...'''
date = "2016-08-28T10:42:00Z"
lastmod = "2017-01-24T22:18:00Z"
weight = 51762
keywords = [ "maps.me", "query", "tagging", "created_by" ]
aliases = [ "/questions/51762" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to look for nodes that has been created using Maps.me in an area?](/questions/51762/how-to-look-for-nodes-that-has-been-created-using-mapsme-in-an-area)

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
<span id="post-51762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51762-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>Since editing OSM via Maps.Me has been enabled for users, I have seen some people are adding their homes or other personal addresses using this feature. (probably by mistake, instead of adding places as their favorites) I'm trying to get a list of nodes that has been created by this app in our country.</p>
<p>I know there is a created_by tag in changesets but I don't know to create a query that can fetch all the nodes that has been created by Maps.me in a area. Is it possible? if yes, what is the exact query?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps.me" rel="tag" title="see questions tagged &#39;maps.me&#39;">maps.me</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-created_by" rel="tag" title="see questions tagged &#39;created_by&#39;">created_by</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '16, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f7da215f2999ecac8d169e32e2c3502e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adib%20Yz&#39;s gravatar image" />
<p><span>Adib Yz</span><br />
<span class="score" title="291 reputation points">291</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adib Yz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51762" class="comments-container">
&#10;</div>
<div id="comment-tools-51762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51762-form-container" class="comment-form-container">
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

<span id="51764"></span>

<div id="answer-container-51764" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51764-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adib Yz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of the authors of MAPS.ME has created <a href="http://mmwatch.osmz.ru/">mmwatch</a>, which allows you to search for (and if necessary revert) MAPS.ME edits by country. <a href="http://mmwatch.osmz.ru/?country=Iran">Here</a>, for example is the list for Iran.</p>
<p>There certainly have been issues with people creating OSM POIs as MAPS.ME "favorites"; in some cases not understanding that they're actually updating a public map at all.</p>
<p>I'd always try and communicate with the users concerned via changeset discussion comments, though this won't always work because sometimes users use throwaway email accounts to sign up for online services. If there's a persistent problem of people not replying to comments you can let the Data Working Group know (by email to data@osmfoundation.org) - we can send them a message that they have to read before they can continue mapping.</p>
<p>I'd always try and make messages to new MAPS.ME users polite - often they don't know that they're adding to OpenStreetMap at all, and it's not their fault that the app that they're using hasn't communicated that to them effectively (there are a number of issues around that raised <a href="https://github.com/mapsme/omim/issues">here</a>). I'd always encourage them to carry on adding valuable data to OSM; just not the personal data that they probably didn't know they were adding in the first place :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '16, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-51764" class="comments-container">
<span id="54275"></span>
<div id="comment-54275" class="comment">
<div id="post-54275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a way to see what portion of total OSM edits is done via MAPS.ME (or other editors)? I just found this: <a href="http://wiki.openstreetmap.org/wiki/Editor_usage_stats">http://wiki.openstreetmap.org/wiki/Editor_usage_stats</a></p>
</div>
<div id="comment-54275-info" class="comment-info">
<span class="comment-age">(24 Jan '17, 22:18)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-51764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51764-form-container" class="comment-form-container">
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

