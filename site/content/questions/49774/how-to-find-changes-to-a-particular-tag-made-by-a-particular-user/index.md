+++
type = "question"
title = "How to find changes to a particular tag, made by a particular user?"
description = '''I often come across an incorrect &quot;highway=track&quot; tag for existing ways. When looking at their history (using JOSM) I find that at some point the &quot;highway&quot; tag was changed from &quot;path&quot; to &quot;track&quot; by a particular user, whom I&#x27;ll call &quot;xyz&quot; here. So I got this idea: let&#x27;s look at all changes of the type...'''
date = "2016-05-21T10:12:00Z"
lastmod = "2016-05-21T14:19:00Z"
weight = 49774
keywords = [ "query", "correction", "changesets", "retagging", "database" ]
aliases = [ "/questions/49774" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find changes to a particular tag, made by a particular user?](/questions/49774/how-to-find-changes-to-a-particular-tag-made-by-a-particular-user)

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
<span id="post-49774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49774-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I often come across an incorrect "highway=track" tag for existing ways. When looking at their history (using JOSM) I find that at some point the "highway" tag was changed from "path" to "track" by a particular user, whom I'll call "xyz" here.</p>
<p>So I got this idea: let's look at all changes of the type "highway tag changed from path to track", made by xyz. We might decide to revert them all at once, or do a survey on them one by one, or send them to xyz so he looks at them and reverts the incorrect ones himself (he has admitted on a forum that some of these changes were by mistake). Please note: I am not asking about how to correct these changes; we'll decide on it later. My question is technical: how to make such a list?</p>
<p>The problem is, xyz is a very active member, who has done thousands of edits, with many fixes in each edit. Reviewing them one by one would be counter-productive.</p>
<p>So, is there any way (a database query?) to find all changes of this type?</p>
<ul>
<li>In a particular area</li>
<li>By a particular user</li>
<li>Changing a particular tag</li>
<li>From a specific value to another specific value</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-correction" rel="tag" title="see questions tagged &#39;correction&#39;">correction</span> <span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-retagging" rel="tag" title="see questions tagged &#39;retagging&#39;">retagging</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '16, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/83450238b4ee0eddbf54d7ce5a3a64e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anatolyg&#39;s gravatar image" />
<p><span>anatolyg</span><br />
<span class="score" title="201 reputation points">201</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anatolyg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '16, 10:38</strong> </span></p>
</div>
</div>
<div id="comments-container-49774" class="comments-container">
&#10;</div>
<div id="comment-tools-49774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49774-form-container" class="comment-form-container">
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

<span id="49777"></span>

<div id="answer-container-49777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49777-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get part of the way to what you want using Overpass API, which has support for restricting queries by user. <a href="http://overpass-turbo.eu/s/gmy">Here's an example.</a> So that at least gets you to tracks in your area of interest that were last touched by the user in question. I guess you could then retrieve the previous version of each way from the main api and examine it together with the current version to check for the questionable edits.</p>
<p>There is also some support in Overpass for examining changes, but <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Delta_between_two_dates_.28.22diff.22.29">it is based on dates</a> not users or versions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '16, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-49777" class="comments-container">
&#10;</div>
<div id="comment-tools-49777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49777-form-container" class="comment-form-container">
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

