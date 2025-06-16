+++
type = "question"
title = "How can I set up a street to be only accessible on week days?"
description = '''The Blankeneser Hauptstraße in Hamburg/Germany is only allowed to drive on weekdays but not allowed on weekends. How can I set it up?  On top of this it is only from beginning of Kahlkamp to end. '''
date = "2013-07-08T15:33:00Z"
lastmod = "2013-07-10T00:26:00Z"
weight = 24090
keywords = [ "week", "access", "prohibited", "days", "tagging" ]
aliases = [ "/questions/24090" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I set up a street to be only accessible on week days?](/questions/24090/how-can-i-set-up-a-street-to-be-only-accessible-on-week-days)

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
<span id="post-24090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24090-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Blankeneser Hauptstraße in Hamburg/Germany is only allowed to drive on weekdays but not allowed on weekends. How can I set it up? On top of this it is only from beginning of Kahlkamp to end.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-week" rel="tag" title="see questions tagged &#39;week&#39;">week</span> <span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-prohibited" rel="tag" title="see questions tagged &#39;prohibited&#39;">prohibited</span> <span class="post-tag tag-link-days" rel="tag" title="see questions tagged &#39;days&#39;">days</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '13, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/45444e439f494123318b6707ae274b7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivolino&#39;s gravatar image" />
<p><span>ivolino</span><br />
<span class="score" title="169 reputation points">169</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivolino has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '13, 03:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24090" class="comments-container">
&#10;</div>
<div id="comment-tools-24090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24090-form-container" class="comment-form-container">
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

<span id="24094"></span>

<div id="answer-container-24094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24094-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In order to apply a restriction only to part of a street, you have to split it into multiple sections (if it isn't already).</p>
<p>The time-dependent restriction itself can then be applied to the appropriate section(s) using <strong><a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">Conditional restrictions</a></strong>. In your example the correct tag would be <strong>vehicle:conditional = no @ (Sa,Su)</strong></p>
<p>Note that this assumes that all vehicles, including e.g. bicycles are banned, and that the day of the week - rather than whether it is a workday - is the relevant factor. Otherwise, the tag has to look somewhat different. Also note that, in order to be able to enter more complex tags such as these, you may have to tell your editor to show you "all tags" (iD) or switch to "advanced mode" (Potlatch 2).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '13, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '13, 00:23</strong> </span></p>
</div>
</div>
<div id="comments-container-24094" class="comments-container">
<span id="24145"></span>
<div id="comment-24145" class="comment">
<div id="post-24145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok this is too complicated for me. Maybe someone else can do it.</p>
</div>
<div id="comment-24145-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 22:04)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="24149"></span>
<div id="comment-24149" class="comment">
<div id="post-24149-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@aseerel4c26</span>: Thanks for pointing out the missing :conditional.</p>
</div>
<div id="comment-24149-info" class="comment-info">
<span class="comment-age">(10 Jul '13, 00:24)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="24151"></span>
<div id="comment-24151" class="comment">
<div id="post-24151-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(oops, sorry, I wrote all in German - too lazy to translate now)</p>
<p><span>@ivolino</span>: Wenn du zukünftig solche Fehler in unseren Daten feststellst, aber es vorerst nicht selbst beheben kannst (und nicht hier nachfragen willst, wie es geht), dann <span>melde den Fehler</span>. Ich habe es nun <a href="https://www.openstreetmap.org/browse/changeset/16893760">eingetragen</a> (dazu habe ich erstmal die Straße in zwei Teile getrennt, um sie getrennt voneinander taggen zu können), ich hoffe es ist so richtig und der richtige <a href="https://www.openstreetmap.org/browse/way/229353584">Straßenabschnitt</a>.</p>
<p><span>@Tordanik</span>: Laut der Wikiseite sollte <code>:conditional</code> an den key, hast du das absichtlich weggelassen? Ich habe nun <code>vehicle:conditional = no @ (Sa-Su)</code> verwendet.</p>
</div>
<div id="comment-24151-info" class="comment-info">
<span class="comment-age">(10 Jul '13, 00:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24094-form-container" class="comment-form-container">
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

