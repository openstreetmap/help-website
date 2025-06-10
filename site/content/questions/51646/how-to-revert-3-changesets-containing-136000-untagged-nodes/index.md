+++
type = "question"
title = "How to revert 3 changesets containing 136000 untagged nodes?"
description = '''Today I added the county boundaries for Iran but unfortunately the upload wasn&#x27;t successful and around 136000 untagged nodes has been added to map. I tried to revert the changsets by JOSM revert plugin but it keeps displaying the &quot;IO exception error: failed to upload data to or download data from OS...'''
date = "2016-08-22T17:03:00Z"
lastmod = "2016-08-22T19:07:00Z"
weight = 51646
keywords = [ "changeset", "revert", "untagged" ]
aliases = [ "/questions/51646" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to revert 3 changesets containing 136000 untagged nodes?](/questions/51646/how-to-revert-3-changesets-containing-136000-untagged-nodes)

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
<span id="post-51646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51646-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Today I added the county boundaries for Iran but unfortunately the upload wasn't successful and around 136000 untagged nodes has been added to map. I tried to revert the changsets by JOSM revert plugin but it keeps displaying the "IO exception error: failed to upload data to or download data from OSM due to a problem with transferring data. Read timed out"</p>
<p>What should I do? The changesets are as follows: 41606250 41606532 41606969</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-untagged" rel="tag" title="see questions tagged &#39;untagged&#39;">untagged</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '16, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f7da215f2999ecac8d169e32e2c3502e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adib%20Yz&#39;s gravatar image" />
<p><span>Adib Yz</span><br />
<span class="score" title="291 reputation points">291</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adib Yz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51646" class="comments-container">
&#10;</div>
<div id="comment-tools-51646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51646-form-container" class="comment-form-container">
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

<span id="51648"></span>

<div id="answer-container-51648" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51648-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adib Yz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First things first - thanks for letting us know!</p>
<p>What I'd suggest now is to let the DWG have a bit of a head-scratch and we'll try and figure out the best way to revert this data. There are a couple of possible ways forward, some of which will require reconstructing the changeset .osc by other means.</p>
<p>There's already a <a href="https://github.com/openstreetmap/openstreetmap-website/pull/1259">pull request</a> to try and prevent this being an issue in the future. It's something that seems to have happened more often in recent months (I can think of four examples I've had to do; other DWG members will have done others of course).</p>
<p>For completeness, there's also a <a href="http://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">wiki page</a> that explains what you're supposed to do before an import. One thing that I do note about that is that it's not translated to many languages, so one way that you can absolutely help while we're figuring out how to revert is to translate a copy of that into Persian (if you're unsure how translations are done, ask on <a href="http://wiki.openstreetmap.org/wiki/IRC">IRC</a> in #osm on OFTC and someone will help).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-51648" class="comments-container">
<span id="51649"></span>
<div id="comment-51649" class="comment">
<div id="post-51649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info. Before doing this import I discussed my plan with our comunnity members but since it hasn't been done before by anyone in Iran, I had no choice other than try it myself. I also sent a message to imports mailingg list but it been 3 days that it waits for moderation. I would also appreciate it if you or anyone else with experience in doing such activities can give me a step by step guide on how to upload my OSM file. I almost worked for 3 weeks on this file before trying to upload it.</p>
</div>
<div id="comment-51649-info" class="comment-info">
<span class="comment-age">(22 Aug '16, 18:21)</span> <span class="comment-user userinfo">Adib Yz</span>
</div>
</div>
<span id="51650"></span>
<div id="comment-51650" class="comment">
<div id="post-51650-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>As was pointed out to you in <a href="https://help.openstreetmap.org/questions/51466/how-to-update-all-the-administrative-boundaries-for-a-country">https://help.openstreetmap.org/questions/51466/how-to-update-all-the-administrative-boundaries-for-a-country</a> you did not follow the import guidelines. They are there for a reason (a decade of bad imports) and you could have avoided the work other people have to do to clean up the mess if you had taken them seriously.</p>
</div>
<div id="comment-51650-info" class="comment-info">
<span class="comment-age">(22 Aug '16, 18:25)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="51652"></span>
<div id="comment-51652" class="comment">
<div id="post-51652-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>You are right. I didn't take the guide seriously and I'm sorry for the mess. I hope some day I can do the kind of work that DWG members do.</p>
</div>
<div id="comment-51652-info" class="comment-info">
<span class="comment-age">(22 Aug '16, 19:07)</span> <span class="comment-user userinfo">Adib Yz</span>
</div>
</div>
</div>
<div id="comment-tools-51648" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51648-form-container" class="comment-form-container">
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

