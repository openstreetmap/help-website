+++
type = "question"
title = "closed changeset constantly reappearing as if it was still opened"
description = '''Since some days, everytime I want to submit a new changeset using JOSM, it fails at first try (JOSM sas that the changeset is closed, thning that there&#x27;s already one open). I need to repeat the operation a second time and the submission succeeds. But then JOSM reports an error when I try to close it...'''
date = "2013-06-09T21:00:00Z"
lastmod = "2013-08-05T07:14:00Z"
weight = 23162
keywords = [ "changesets" ]
aliases = [ "/questions/23162" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [closed changeset constantly reappearing as if it was still opened](/questions/23162/closed-changeset-constantly-reappearing-as-if-it-was-still-opened)

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
<span id="post-23162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23162-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-23162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since some days, everytime I want to submit a new changeset using JOSM, it fails at first try (JOSM sas that the changeset is closed, thning that there's already one open). I need to repeat the operation a second time and the submission succeeds.</p>
<p>But then JOSM reports an error when I try to close it, because JOSM sees another completely unrelated old changeset (which is closed since long). It seems that the server has not registered the correct number of changesets submitted by me in my user account, and then it reports detects another changeset randomly from my own list of changesets, for now it is this one: 16393274</p>
<p>There's nothing wrong with it, it was properly sent and closed. It seems that the problem is that my account is not counting correctly my submitted changesets (so sometimes I have submitted and closed a changeset successfully, but the server forgot to increment my account in the same transaction).</p>
<p>This is very irritating, because I now have to close all changesets explicitly, by selecting them in the CTRL+ALT+Q dialog in JOSM, to select the correct one (the only one which is currently active), and ignore the old one that is still appearing first in the list.</p>
<p>I tried to investigate this is JOSM, including reinstalling it, purging caches and preferences. This affects ALL changesets that I try to create now, whatever their number. Potlatch does not seem to be irritated by this. It seems that this bug has been caused since the time I've tried the current beta of the iD editor (just once).</p>
<p>How can I purge this closed changeset from my history so that it does not block further data submissions ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '13, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '13, 21:00</strong> </span></p>
</div>
</div>
<div id="comments-container-23162" class="comments-container">
<span id="23163"></span>
<div id="comment-23163" class="comment">
<div id="post-23163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that the reappearing changeset sometimes changes, this is not always the same one, but it is always an old one already closed days before.</p>
</div>
<div id="comment-23163-info" class="comment-info">
<span class="comment-age">(09 Jun '13, 21:02)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="24896"></span>
<div id="comment-24896" class="comment">
<div id="post-24896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem persists. Reinstalling JOSM after clearing all its caches does not solve the problem. And now it becomes even worse: when I submit a changeset, the new changeset very frequently inexpectely inherits the comment from an older changeset and ignore my new comment.</p>
<p>The issue is visible if I use the option "leave the changeset open", but now it also affects the changesets that are closed automatically after submission (so I cannot submit another edit to force again the incorrect comment that is being recorded).</p>
<p>Apparently this is caused by the server (more precisely, apparently in the link from the frontend proxy of the API used by JOSM and the server, which apparently has an issue when reading my user profile stored in the database, which is constantly out of sync by 1 changeset, with an additional closed changeset overriding data from the new changeset).</p>
<p>I can no longer track my edits and differentiate them, all too many of my changeset comments are mixed. The ONLY way to avoid it for now is to close JOSM and restart it to force it to load my user status, otherwise the frontend proxy will report the wrong "last open changeset" and will sort the open changeset incorrectly. May be there's a changeset with an unknown status (not the standard value for a closed changeset, sometimes it is handled as if it was open, sometimes it will be treated as closed, and this seems to perturbate also some SQL queries, such as SQL aggregates like "HAVING changeset.date = MAX(changeset.date)" or similar).</p>
<p>It seems that the "last open changeset" is present in the proxy with an incorrect date (offsetted apparently by about 2 or 3 weeks, according to the random changeset that is being used to override what I am submitting).</p>
<p>Note that this does not affect the stored edits themselves which are correctly recorded and correctly associated to the newly create changesets.</p>
<p>Frequently when I send the 1st edit in a new JOSM run it will be sent correctly and closed correctly, but then when I send a newer changeset, it will fail immediately (a new changset is created but the server does not return its ID, but the ID of an older changeset, and the first edited data will be rejected, the submission fails. I need to send it again (changing nothing, my new edit comment is still kept in the submission form, but it will NOT be used on the server, a new changeset will be created, and its ID correctly reported, but with now the comment immediately replaced by the comment of my previous successfully closed changeset, if this was the 1st of my JOSM session, otherwise the comment used in a changeset closed 2-3 weeks ago).</p>
<p>This is very irritating. Each time now I need to close JOSM completely (saving my edits locally, without sending), and then restart it to avoid the error (submissions sent to the old closed changeset) when I will create the new changeset.</p>
<p>Sometimes when I leave the changeset open, and look at my history only, all is OK. Then I use CTRL+ALT+Q to close this changeset with no other data to send, but the dialog displays that there's TWO changesets (the new one still open and the old one already closed) both displayed with the same comment (the comment from the older changeset). I need to select the correct one (I click on the one with the highest ID, the dialog does not permit me to input and correct the comment, and finally the closed changeset will have its comment changed in the database to use the older comment.</p>
<p>I have tried on another PC the same issue appears. I am definitely not convinced that this is an issue of JOSM. In my opinion it is a bug the of the API server, in one of its internal caches for its own internal SQL queries, or a bug in the SQL server.</p>
</div>
<div id="comment-24896-info" class="comment-info">
<span class="comment-age">(04 Aug '13, 19:44)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
</div>
<div id="comment-tools-23162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23162-form-container" class="comment-form-container">
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

<span id="23183"></span>

<div id="answer-container-23183" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23183-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I beleive this should be filed as a JOSM error report on <a href="http://josm.openstreetmap.de/">http://josm.openstreetmap.de/</a> or an as an API issue here: <a href="https://trac.openstreetmap.org/">https://trac.openstreetmap.org/</a> ,if it isn't an operator error.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '13, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '13, 11:50</strong> </span></p>
</div>
</div>
<div id="comments-container-23183" class="comments-container">
<span id="23186"></span>
<div id="comment-23186" class="comment">
<div id="post-23186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't detect anything wrong with the API (when I perform manual requests using GET requests in my web browser. I absolutely don't know where this old changeset is coming from, I cannot find any local occurence of its ID anywhere on my data or in the JOSM caches (that I have deleted completely before retrying with a reinstallation). The extra changeset is not even related to what I want to upload, nothing in common with any object, except that it is part of my old changesets.</p>
<p>But I know that JOSM is performing some additional API requests and I don't see the full HTTP request, just one URL and not the metadata and details of responses. I've tried to use a local proxy to trace these requests, nothing seems wrong. This is a complete mystery (and it just affects JOSM, not other online editors like Potlatch 1/2, iD, or Osmose's rawedit). The extra changeset that appears, and changes sometimes, may be one created under rawedit and not within JOSM. It is unpredictable. May be it's a bug in JOSM that uses some strange cache for changesets.</p>
<p>Or it's something caused by my local antivirus inspecting the HTTP sessions in order to filter some potentially harmful data (I use AVG Antivirus). I've tried disabling it (the normal way) but this does not change things. I also checked if I had some rootkit using other security tools, but nothing found, my system is clean (I've never been infected by any threat on my PCs since many years).</p>
<p>I suspect that the problem is not on my PC but in a remote proxy (on the server side) that hides some data and returns inconsistant data about my account (but I don't know which kind of API may be incorrectly cached by such remote proxy that I absolutely o not control).</p>
<p>I've also tried to use an alternate API server in JOSM config: <a href="http://api.openstreetmap.fr/api">http://api.openstreetmap.fr/api</a> This does not change the problem (no difference compared to the default API server).</p>
</div>
<div id="comment-23186-info" class="comment-info">
<span class="comment-age">(10 Jun '13, 13:56)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="23436"></span>
<div id="comment-23436" class="comment">
<div id="post-23436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Problem still not solved. Using a proxy to trace requests does not reveal any problem in them. Visibl this is an issue in JOSM, that I cannot understand at all. I don't know from where this spurious closed changeset comes into the list of open changeset and find absolutely nothing in my own local caches explaining this irritating presence...</p>
</div>
<div id="comment-23436-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 08:20)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="23437"></span>
<div id="comment-23437" class="comment">
<div id="post-23437-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Have you opened an issue with the JOSM developers?</p>
</div>
<div id="comment-23437-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 08:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="24903"></span>
<div id="comment-24903" class="comment">
<div id="post-24903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can"t even post anything there, I have an account there, but the connection fails always when I logon (needed to post), even when I try to renew the password. It seems that my account on OSM is in fact corrupted.</p>
</div>
<div id="comment-24903-info" class="comment-info">
<span class="comment-age">(05 Aug '13, 07:14)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
</div>
<div id="comment-tools-23183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23183-form-container" class="comment-form-container">
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

