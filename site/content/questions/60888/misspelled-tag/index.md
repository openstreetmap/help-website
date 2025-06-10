+++
type = "question"
title = "Misspelled tag"
description = '''Okay, I know the rules about mechanical edits and I&#x27;m prepared to simply let these tags stay the way they are but there are 304 instances of an obviously misspelled tag I would like to fix. I&#x27;m mapping some oil fields and checking out the various possibilities for tagging objects related to oil prod...'''
date = "2017-11-30T11:40:00Z"
lastmod = "2017-11-30T13:25:00Z"
weight = 60888
keywords = [ "misspelled_tag", "bulk_editing" ]
aliases = [ "/questions/60888" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Misspelled tag](/questions/60888/misspelled-tag)

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
<span id="post-60888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60888-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-60888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Okay, I know the rules about mechanical edits and I'm prepared to simply let these tags stay the way they are but there are 304 instances of an obviously misspelled tag I would like to fix. I'm mapping some oil fields and checking out the various possibilities for tagging objects related to oil production and came across this tag combination:</p>
<pre><code>industrisl=well_site</code></pre>
<p>I've contacted the mapper and he admits to the mistake — he wanted to use "industrial" instead of "industrisl" but a slip of the finger caused the error. He asked me to go ahead and fix them. I'm guessing he applied these tags by some sort of automatic process, otherwise I'm unable to explain the large number of mis-tagged objects.</p>
<p>I think perhaps he meant to use <code>industrial=well_site</code> but I didn't ask and that's another whole issue anyway.</p>
<p>So, leaving aside the question of whether <code>industrial=wellsite</code> is the best one for the job, what should be done? I'm not willing to edit each one of these individually so I'm looking for some sort of agreement that will allow me to correct them using JOSM or level0. I'm not going to write a proposal to justify this edit and if that's what's required to obtain a go ahead, I'll simply forget about it.</p>
<p>Thoughts, opinions?</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-misspelled_tag" rel="tag" title="see questions tagged &#39;misspelled_tag&#39;">misspelled_tag</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '17, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '17, 11:49</strong> </span></p>
</div>
</div>
<div id="comments-container-60888" class="comments-container">
&#10;</div>
<div id="comment-tools-60888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60888-form-container" class="comment-form-container">
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

<span id="60891"></span>

<div id="answer-container-60891" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60891-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If there's over 100 instances of an obviously misspelled tag it's often an indication of an undiscussd import (since the misspelling would have baan picked up had it been properly discussed!).</p>
<p>However in this case (see e.g. <a href="https://www.openstreetmap.org/#map=18/37.20239/-104.89915">here</a>) it's likely just a copy and paste faux pas that got a bit out of hand - the area is visible on imagery and there's also a "industrial=wellsite" tag as well.</p>
<p>Personally, I've used an example of changing "highway=pirmary" to "highway=primary" as something that doesn't need extensive discussion prior to change; here the fact that "industrisl" is wrong doesn't need discussion but "what to" perhaps does. <a href="https://taginfo.openstreetmap.org/keys/industrial#values">Taginfo</a> suggests both "oil" and "wellsite"; here it might need a bit of discussion about what these sites actually are and what part they play in the gas fracking / extraction process.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '17, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60891" class="comments-container">
<span id="60893"></span>
<div id="comment-60893" class="comment">
<div id="post-60893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Agreed, he was apparently trying to cover all the cases. The tagging for these features is a bit of a mess, which I'm guessing is why he tried to use both of these tags. Adding to the confusion, there is also a landuse=wellsite. At any rate, he wanted to use these tags:</p>
<p>industrial=wellsite and</p>
<p>industrial=well_site</p>
<p>Reiterating, I'm not asking about which of those is more proper because, as far as I'm concerned, they can both be used until one or the other becomes the accepted standard. My primary concern here is to fix the obvious misspellings, not to decide upon a more proper tag or tags.</p>
<p>Thanks for your interest,</p>
<p>Dave</p>
</div>
<div id="comment-60893-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 12:40)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="60894"></span>
<div id="comment-60894" class="comment">
<div id="post-60894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are no uses of industrial=well_site currently: <a href="https://taginfo.openstreetmap.org/search?q=industrial%3Dwell_site">https://taginfo.openstreetmap.org/search?q=industrial%3Dwell_site</a> .</p>
<p><a href="https://taginfo.openstreetmap.org/tags/man_made=petroleum_well">https://taginfo.openstreetmap.org/tags/man_made=petroleum_well</a> is actually far more used.</p>
</div>
<div id="comment-60894-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 12:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60895"></span>
<div id="comment-60895" class="comment">
<div id="post-60895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Most of the sites tagged are gas wells not petroleum wells. Perhaps the best approach is simply to remove the "industrisl" tag altogether.</p>
</div>
<div id="comment-60895-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 12:49)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="60896"></span>
<div id="comment-60896" class="comment">
<div id="post-60896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd definitely do that - you'd not be removing any information from OSM by doing so.</p>
</div>
<div id="comment-60896-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 13:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60897"></span>
<div id="comment-60897" class="comment">
<div id="post-60897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Appreciate the feedback.</p>
<p>Thanks.</p>
</div>
<div id="comment-60897-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 13:25)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-60891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60891-form-container" class="comment-form-container">
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

