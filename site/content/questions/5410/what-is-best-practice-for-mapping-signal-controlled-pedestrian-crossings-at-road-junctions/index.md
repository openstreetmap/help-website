+++
type = "question"
title = "What is best practice for mapping signal controlled pedestrian crossings at road junctions"
description = '''I&#x27;ve never quite understood the way in which signal-controlled pedestrian crossings (in the UK pelicans, toucans etc.) are tagged. This is fine when I&#x27;m using JOSM as there are pre-sets, but when I&#x27;m using Potlatch I find the exact convention used in JOSM difficult to remember. So to start with I&#x27;m ...'''
date = "2011-05-27T10:52:00Z"
lastmod = "2011-11-04T12:36:00Z"
weight = 5410
keywords = [ "crossing", "pedestrian", "junction", "traffic_signals", "tagging" ]
aliases = [ "/questions/5410" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is best practice for mapping signal controlled pedestrian crossings at road junctions](/questions/5410/what-is-best-practice-for-mapping-signal-controlled-pedestrian-crossings-at-road-junctions)

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
<span id="post-5410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5410-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've never quite understood the way in which signal-controlled pedestrian crossings (in the UK pelicans, toucans etc.) are tagged. This is fine when I'm using JOSM as there are pre-sets, but when I'm using Potlatch I find the exact convention used in JOSM difficult to remember. So to start with I'm never sure whether to use <code>highway=traffic_signals</code> or <code>highway=crossing</code> together with <code>crossing=traffic_signals</code>.</p>
<p>At road junctions when the traffic signals control vehicular traffic as well as the pedestrian crossing I get more confused. For a simple junction (two streets crossing) I could leave a <code>highway=traffic_signals</code> on the junction node, and tag the pedestrian crossings as <code>highway=crossing</code>, or I can remove a single node for the traffic signals and rely on tagging each set of lights together with their pedestrian crossing attributes.</p>
<p>I would like:</p>
<ul>
<li><p>a description of the standard practice of tagging for signal-controlled crossings (if your answer is fully covered by existing responses to this question <a href="http://help.openstreetmap.org/questions/1489/how-to-tag-traffic-lights-on-pedestrian-crossing">how-to-tag-traffic-lights-on-pedestrian-crossing</a>, please avoid duplicating answers);</p></li>
<li><p>an explanation of why a particular combination of tags are used;</p></li>
<li><p>how this should be applied to junctions where the signals are controlling both vehicles and pedestrians;</p></li>
<li><p>and, lastly, advice on linking together traffic signals at junctions (e.g., with a relation). Please don't forget that most cases of junctions are more complex than just two streets crossing.</p></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '11, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5410" class="comments-container">
<span id="5429"></span>
<div id="comment-5429" class="comment">
<div id="post-5429-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've also found this a bit confusing, and would love for some more examples and clearer explanations to be added to the wiki, on how advanced pedestrian crossings should be tagged. So once you have received a good answer here, maybe relevant pages in the wiki could be updated based on it?</p>
</div>
<div id="comment-5429-info" class="comment-info">
<span class="comment-age">(29 May '11, 23:50)</span> <span class="comment-user userinfo">Martin Holmgren</span>
</div>
</div>
</div>
<div id="comment-tools-5410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5410-form-container" class="comment-form-container">
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

<span id="8812"></span>

<div id="answer-container-8812" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8812-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fairly easy. <em>highway=crossing</em> and <em>crossing=traffic_signals</em> is used for a traffic signal which could be replaced in function from a zebra.</p>
<p><em>highway=traffic_signals</em> and <em>crossing=traffic_signals</em> is used when its a normal junction Where a pedestrian traffic signals makes a crossing possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '11, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/35cb5954a17f0e0c0a819bcaad5ea424?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="B%C3%BCrste&#39;s gravatar image" />
<p><span>Bürste</span><br />
<span class="score" title="84 reputation points">84</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bürste has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8812" class="comments-container">
&#10;</div>
<div id="comment-tools-8812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8812-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5590"></span>

<div id="answer-container-5590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5590-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-5590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Key:crossing">http://wiki.openstreetmap.org/wiki/Key:crossing</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '11, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7a81832ca1b48080d1a57be29dff3a8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c2r&#39;s gravatar image" />
<p><span>c2r</span><br />
<span class="score" title="413 reputation points">413</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c2r has 2 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-5590" class="comments-container">
<span id="5594"></span>
<div id="comment-5594" class="comment">
<div id="post-5594-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>sorry SK53 if you don't like the page, but it seems to me to clearly state that it should be highway=crossing; crossing=traffic_signals; foot=yes for the case where there is a signal controlled junction with foot crossing facilities...</p>
<p>so I'm unsure what the issue is - perhaps you could clarify with a couple of clear examples?</p>
</div>
<div id="comment-5594-info" class="comment-info">
<span class="comment-age">(06 Jun '11, 20:49)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
<span id="5674"></span>
<div id="comment-5674" class="comment">
<div id="post-5674-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I down voted your answer because it did <em>NOT</em> answer the question.</p>
<p>The wiki page &amp; the answer I linked to are fine as far as they go. I would like a little more detail and some background. I'm sure that if I find it difficult to remember the tagging after a couple of years its probably not instinctive for others. I asked the question to encourage elaboration of what has already been said, in the hope that this would be useful to any contributor.</p>
</div>
<div id="comment-5674-info" class="comment-info">
<span class="comment-age">(10 Jun '11, 13:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5590-form-container" class="comment-form-container">
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

