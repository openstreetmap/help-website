+++
type = "question"
title = "Power lines: minor_line threshold ?"
description = '''Hello, there. I have a question about mapping power lines: here, in France, electricity transport and distribution is mainly parted between RTE, for Réseau de Transport d&#x27;Électricité — Electricity transport network —, and ErDF, for Électricité réseau et Distribution de France — Electricity network a...'''
date = "2015-10-07T15:04:00Z"
lastmod = "2015-10-14T16:27:00Z"
weight = 45781
keywords = [ "line", "minor_line", "power", "france" ]
aliases = [ "/questions/45781" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Power lines: minor_line threshold ?](/questions/45781/power-lines-minor_line-threshold)

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
<span id="post-45781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45781-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I have a question about mapping power lines: here, in France, electricity transport and distribution is mainly parted between RTE, for <em>Réseau de Transport d'Électricité</em> — Electricity transport network —, and ErDF, for <em>Électricité réseau et Distribution de France</em> — Electricity network and distribution of France. The first manages of 63 kV and higher voltage lines, mainly on towers, while the second manages 20 kV and lower lines, mainly on poles — there is no standard voltage between 20 kV and 63 kV here — and, as their names say, the first is responsible of transport, while the other one is responsible of distribution.</p>
<p>Do I correctly interpret the wiki, when I assume this parting between line voltages and societies essentially reflects the parting between <code>power=line</code> and <code>power=minor_line</code>, and therefore that I should then map ErDF/20kV-and-lower-voltage lines as <code>minor_line</code>, and RTE/63kV-and-higher-voltage lines as <code>line</code>?</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-minor_line" rel="tag" title="see questions tagged &#39;minor_line&#39;">minor_line</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '15, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45781" class="comments-container">
&#10;</div>
<div id="comment-tools-45781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45781-form-container" class="comment-form-container">
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

<span id="45800"></span>

<div id="answer-container-45800" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45800-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-45800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general my view is that the choice of <code>minor_line</code> vs. <code>line</code> should not be directly termined by the voltage of the line. Instead the choice should be based on the general visibility of the line in the general landscape.</p>
<p>Lines supported on pylons or very tall towers will be visible over long distances and can be useful navigation markers. Lines supported on poles close to the ground are only useful for local orientation. In general this difference will follow voltage, but there are exceptions. For instance in Britain there are still a number of 33kV and 66kV lines supported on pylons which are considerably smaller than those of the main distribution network. Sometimes low voltage lines are placed on pylons to cross rivers and gorges.</p>
<p>The main issue is a practical one: what can a relatively naive mapper conveniently use as a tag. Discerning the voltage requires somewhat arcane knowledge, and this information is conveniently supported by its own tag. So for me the deciding factor is the overall visibility of the line in the landscape (say immediately obvious from over 200m away).</p>
<p>The absolutely clinching factor for me, was a mapping need which arose earlier this year after the Nepal earthquake. After a US helicopter crashed with the loss of several rescuers' lives, there was a <a href="https://lists.openstreetmap.org/pipermail/hot/2015-May/009128.html">fear that unmapped power lines</a> represented a significant danger to rescue workers. Helicopter pilots have no interest in the voltage of a power line: merely whether it is a significant aerial hazard, and that entirely depends on the height of the supports. Thus an entirely different use-case (hazard maps) would use similar criteria to my own (navigation in the landscape), which broadly corresponds to the height above ground of the highest wires on the power line, and nothing directly corresponding to voltage.</p>
<p>Lastly, in general it is not a good practice to use one tag as a proxy for another (see place &amp; population): it is effectively tagging the same thing twice.</p>
<p><strong>Summary</strong>: Use height of line off the ground to assign lines to <code>power=line</code> or <code>power=minor_line</code>. If possible add voltage and/or the tags which enable a 'power mapper' to assign voltage. This was we get both information relevant to the grid network <strong>and</strong> information relevant for other use cases.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '15, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-45800" class="comments-container">
<span id="45802"></span>
<div id="comment-45802" class="comment">
<div id="post-45802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I got your meaning, but what about when a minor line uses towers to cross valleys or long gaps? Should I tag it <code>power=line</code> only on this section?</p>
</div>
<div id="comment-45802-info" class="comment-info">
<span class="comment-age">(08 Oct '15, 12:45)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="45809"></span>
<div id="comment-45809" class="comment">
<div id="post-45809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, good question. I'm not really sure (and the one case I did it I think I left the line as minor line), but give the additional reasoning from the helicopter hazard case I think power=line is best. Possibly some additional tag indicating it's a valley/river/gorge crossing may help.</p>
</div>
<div id="comment-45809-info" class="comment-info">
<span class="comment-age">(08 Oct '15, 14:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="45814"></span>
<div id="comment-45814" class="comment">
<div id="post-45814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Or giving the height of the towers? This way, the power line modelling will remain whole and the aerial danger could still be noticed if seeked.</p>
</div>
<div id="comment-45814-info" class="comment-info">
<span class="comment-age">(09 Oct '15, 10:45)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="45875"></span>
<div id="comment-45875" class="comment">
<div id="post-45875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, as I saw different points of view, even between pages of the wiki, I raised the topic on the tagging ML, to see if I can get a consensus. I'm inclined to use the main type of support (poles/towers) of the line to know how to model it, but I'll first see if I can get a consensus and correct the wiki accordingly, if possible.</p>
</div>
<div id="comment-45875-info" class="comment-info">
<span class="comment-age">(14 Oct '15, 08:26)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="45876"></span>
<div id="comment-45876" class="comment">
<div id="post-45876-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11353/penegal">@Penegal</a>, perhaps more useful would be to look how lines were originally mapped <em>before</em> the current wiki description was written. I know I always find the way this area is rendered annoying <a href="https://www.openstreetmap.org/#map=15/52.9236/-0.9574">https://www.openstreetmap.org/#map=15/52.9236/-0.9574</a> (two parallel lines on pylons).</p>
</div>
<div id="comment-45876-info" class="comment-info">
<span class="comment-age">(14 Oct '15, 09:40)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="45881"></span>
<div id="comment-45881" class="comment not_top_scorer">
<div id="post-45881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> ♦ Wow, this is weird, indeed, having the towers rendered but not the line. I don't see what you're getting at speaking of <em>before the wiki desc</em>, but, IMHO, the two lines should be mapped as <code>power=line</code>, as they seem to be quite obvious, even for miles.</p>
</div>
<div id="comment-45881-info" class="comment-info">
<span class="comment-age">(14 Oct '15, 16:27)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
</div>
<div id="comment-tools-45800" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-45800-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45790"></span>

<div id="answer-container-45790" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From my point of view, 20 kV and below should be tagged power=minor_line.</p>
<p>These tag is very useful for the authors of map rendering stylesheets because they can easily differ between important (high voltage, high towers) and less important (lower towers/poles, lower voltage) power lines and render important power lines on lower zoom levels because these are good visible landmarks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '15, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-45790" class="comments-container">
&#10;</div>
<div id="comment-tools-45790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45790-form-container" class="comment-form-container">
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

