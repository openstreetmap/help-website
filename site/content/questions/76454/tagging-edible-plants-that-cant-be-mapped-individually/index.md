+++
type = "question"
title = "Tagging edible plants that can&#x27;t be mapped individually"
description = '''I&#x27;d like to start mapping trees and bushes that grow edible fruit. It&#x27;s clear to me how to do this when I have a single tree that I want to tag. But what do I do when the shrubbery along a path contains a large amount of blackberry bushes, that I don&#x27;t feel I can map individually? Can natural=scrub ...'''
date = "2020-09-05T09:55:00Z"
lastmod = "2020-09-05T16:08:00Z"
weight = 76454
keywords = [ "plant", "scrub", "tagging", "vegetation", "species" ]
aliases = [ "/questions/76454" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging edible plants that can't be mapped individually](/questions/76454/tagging-edible-plants-that-cant-be-mapped-individually)

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
<span id="post-76454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76454-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to start mapping trees and bushes that grow edible fruit. It's clear to me how to do this when I have a single tree that I want to tag.</p>
<p>But what do I do when the shrubbery along a path contains a large amount of blackberry bushes, that I don't feel I can map individually?</p>
<p>Can <code>natural=scrub</code> be combined with <code>species=</code>? It doesn't seem like a good idea to me, because there is probably more than one species in this area, maybe even more than one that I want to tag explicitly (say, raspberry bushes mixed in as well).</p>
<p>On the other hand, for an area overgrown with mainly blackberries, it might be fine. Additional noteworthy plants could be added as individual points.</p>
<p>Are there established ways to do this? Otherwise, what are your thoughts?</p>
<p>Furthermore, although this is beyond what I want to do right now, how about a meadow where some specific edible plants grow, among many other things? Is this something that can be part of OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-plant" rel="tag" title="see questions tagged &#39;plant&#39;">plant</span> <span class="post-tag tag-link-scrub" rel="tag" title="see questions tagged &#39;scrub&#39;">scrub</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-vegetation" rel="tag" title="see questions tagged &#39;vegetation&#39;">vegetation</span> <span class="post-tag tag-link-species" rel="tag" title="see questions tagged &#39;species&#39;">species</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '20, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e7687474f445a58615ccf4e3c4dc7265?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zoosh&#39;s gravatar image" />
<p><span>zoosh</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zoosh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76454" class="comments-container">
&#10;</div>
<div id="comment-tools-76454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76454-form-container" class="comment-form-container">
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

<span id="76458"></span>

<div id="answer-container-76458" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76458-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zoosh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tags that come to mind are <code>produce=*</code> and <code>crop=*</code>. Since the wiki says that <code>crop=*</code> is specifically for "cultivated land" then I guess I'd go with <code>produce=*</code>.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Key:produce">the <code>produce=*</code> wiki page</a> for some examples. It looks like the typical method would be eg <code>produce=berries</code> + <code>berries=blackberry</code>, which you could add to whatever feature tag -- <code>natrual=scrub</code>, <code>landuse=meadow</code>, etc.</p>
<p>And if more than one thing is growing you could double up the tags with semicoloned values: <code>produce=berries;herbs</code> + <code>berries=blackberry;raspberry</code> + <code>herbs=mint;thyme</code>.</p>
<p>I'd avoid tagging species unless the feature you're tagging is entirely that species... plus it's difficult to get right; there are hundreds of species of blackberries alone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76458" class="comments-container">
<span id="76459"></span>
<div id="comment-76459" class="comment">
<div id="post-76459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you! it feels like "produce" was the one tag I didn't click on, and it's totally what I was looking for. Good point about <code>species=*</code>, too.</p>
</div>
<div id="comment-76459-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 15:14)</span> <span class="comment-user userinfo">zoosh</span>
</div>
</div>
<span id="76460"></span>
<div id="comment-76460" class="comment">
<div id="post-76460-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd be very surprised if anyone wanted to map individual blackberry microspecies, the standard aggregate name Rubus fruticosus used with species or taxon is fine. You can also use dominant_taxon (e.g., dominant_taxon=Rubus fruticosus, or dominant_taxon=Prunus spinosa) which provides more biologically relevant information about the area of shrubs. This is approprite when the area might be described as a bramble patch or blackthorn thicket.</p>
</div>
<div id="comment-76460-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 16:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76458-form-container" class="comment-form-container">
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

