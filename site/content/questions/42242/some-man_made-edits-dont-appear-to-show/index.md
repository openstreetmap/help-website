+++
type = "question"
title = "Some man_made edits don&#x27;t appear to show"
description = '''Some of the Land Use items I have added to OSM using don&#x27;t appear to be showing on the map several days later - example here https://www.openstreetmap.org/#map=18/51.47411/-2.81320 where the man_made storage tanks are not showing. What am I not doing please? Robin'''
date = "2015-04-10T10:39:00Z"
lastmod = "2015-04-12T12:34:00Z"
weight = 42242
keywords = [ "not_shown", "tank", "storage" ]
aliases = [ "/questions/42242" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Some man_made edits don't appear to show](/questions/42242/some-man_made-edits-dont-appear-to-show)

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
<span id="post-42242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some of the Land Use items I have added to OSM using don't appear to be showing on the map several days later - example here <a href="https://www.openstreetmap.org/#map=18/51.47411/-2.81320">https://www.openstreetmap.org/#map=18/51.47411/-2.81320</a> where the man_made storage tanks are not showing.</p>
<p>What am I not doing please? Robin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-tank" rel="tag" title="see questions tagged &#39;tank&#39;">tank</span> <span class="post-tag tag-link-storage" rel="tag" title="see questions tagged &#39;storage&#39;">storage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '15, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/45d62517b772d1ae37975c05be147cf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FollowMeChaps&#39;s gravatar image" />
<p><span>FollowMeChaps</span><br />
<span class="score" title="325 reputation points">325</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FollowMeChaps has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '15, 13:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42242" class="comments-container">
&#10;</div>
<div id="comment-tools-42242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42242-form-container" class="comment-form-container">
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

<span id="42245"></span>

<div id="answer-container-42245" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42245-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-42245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://github.com/gravitystorm/openstreetmap-carto">OpenStreetMap style</a> is hosted on GitHub, you can see exactly what is, and <em>isn't</em>, displayed there. It looks like <code>man_made=storage_tank</code> isn't rendered by that style, and hence it's not coming up.</p>
<p>You're lucky though, <code>man_made</code> as a key <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/2e22d987018e145fc5179e5034ab991998969be9/openstreetmap-carto.style#L41">is imported into the database</a>. You could try <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/2e22d987018e145fc5179e5034ab991998969be9/CONTRIBUTING.md">contributing to the OSM carto style</a> to get it to come up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-42245" class="comments-container">
<span id="42291"></span>
<div id="comment-42291" class="comment">
<div id="post-42291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks for the quick responses. Explains why I can't see them though I don't understand the logic and the GitHub and carto style is all gobbledygook to me - may as well be written in another language! Robin</p>
</div>
<div id="comment-42291-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 12:34)</span> <span class="comment-user userinfo">FollowMeChaps</span>
</div>
</div>
</div>
<div id="comment-tools-42245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42245-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42243"></span>

<div id="answer-container-42243" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42243-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm sure the man_made=storage_tank tag was being displayed on the standard map until recently. All my tanks have disappeared too. Probably just the whim of one of the devs I suppose.<br />
Edit: OK, I must admit that I have spent too much time admiring my tanks in Josm.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '15, 14:01</strong> </span></p>
</div>
</div>
<div id="comments-container-42243" class="comments-container">
<span id="42244"></span>
<div id="comment-42244" class="comment">
<div id="post-42244-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Computer says <a href="http://stefanosabatini.eu/doesitrender/#man_made=storage_tank">no</a>. I couldn't find a commit removing <em>man_made=storage_tank</em> either. Are you sure they have been rendered in the past? Maybe due to an additional tag (I'm not suggesting to add one :))?</p>
</div>
<div id="comment-42244-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 13:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42246"></span>
<div id="comment-42246" class="comment">
<div id="post-42246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use an old variant of openstreetmap-carto (from mid last year) and it doesn't render them either, so if there was a change that caused these not to show, if was before then.</p>
<p>Maybe some other storage tanks on the map had a building tag on them?</p>
</div>
<div id="comment-42246-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 14:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="42248"></span>
<div id="comment-42248" class="comment">
<div id="post-42248-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems very common to add the building tag to storage tanks, though I would have thought that man_made=storage_tank should be sufficient.<br />
<a href="https://taginfo.openstreetmap.org/tags/man_made=storage_tank#combinations">https://taginfo.openstreetmap.org/tags/man_made=storage_tank#combinations</a></p>
</div>
<div id="comment-42248-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 14:26)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-42243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42243-form-container" class="comment-form-container">
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

