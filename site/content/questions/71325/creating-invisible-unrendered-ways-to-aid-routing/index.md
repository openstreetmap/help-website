+++
type = "question"
title = "Creating &quot;invisible&quot; (unrendered) ways to aid routing"
description = '''I have been maintaining maps for a region with a shopping centre with multiple levels - and not only that, also roads and a subway terminal directly under it. I run into problems regarding pedestrian routing (of course, there are different routing engines, but still) to hundred shops in this complex...'''
date = "2019-10-25T06:48:00Z"
lastmod = "2019-10-25T20:12:00Z"
weight = 71325
keywords = [ "rendering", "routing", "footpath" ]
aliases = [ "/questions/71325" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Creating "invisible" (unrendered) ways to aid routing](/questions/71325/creating-invisible-unrendered-ways-to-aid-routing)

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
<span id="post-71325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71325-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been maintaining maps for a region with a shopping centre with multiple levels - and not only that, also roads and a subway terminal directly under it. I run into problems regarding pedestrian routing (of course, there are different routing engines, but still) to hundred shops in this complex. Routing engines often "snap" shops to an entirely wrong path: for instance, shops in floor 3 might get a suggestion to enter directly through subway station 50 m below it, which is of course physically impossible and completely useless for the end user. Even worse, they might get associated with a road which would put route anywhere at length of several kilometres, even inside the shopping centre.</p>
<p>I'm curious of solving this problem. One candidate that comes to my mind would be explicit footpaths to shops which would be forced not to render by default. I could of course create explicit paths for every shop, but that would make normal maps completely unreadable. So, is there a way to advise map viewers (but not editors) not to render a specific footpath? I'm naively speculating that this could help my case.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '19, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9104ef5e4f029338cf8df36de3ad23d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kirma&#39;s gravatar image" />
<p><span>kirma</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kirma has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '19, 07:19</strong> </span></p>
</div>
</div>
<div id="comments-container-71325" class="comments-container">
&#10;</div>
<div id="comment-tools-71325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71325-form-container" class="comment-form-container">
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

<span id="71326"></span>

<div id="answer-container-71326" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71326-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you seen the <a href="https://wiki.openstreetmap.org/wiki/Indoor_Mapping">"Indoor Mapping"</a> page on the wiki? I would suggest using the guidance there and hope that the routing engines are aware of the scheme (I was previously unaware of highway=corridor and have mapped some parts of a shopping centre in the past which should perhaps be retagged).</p>
<p>Edit: I've had a look at <a href="https://www.openstreetmap.org/#map=19/60.17524/24.80408">this area</a> and as you have level tags on the shops and the footways I suspect the issue is with the routing engine(s) rather than your mapping. Having footways/corridors connected to the nodes <em>might</em> help, but I can see why you wouldn't want them to render.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '19, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '19, 09:02</strong> </span></p>
</div>
</div>
<div id="comments-container-71326" class="comments-container">
<span id="71329"></span>
<div id="comment-71329" class="comment">
<div id="post-71329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm curious about indoor mapping but I fear the major users of mapping data on the region might not be ready to take advantage of it. It sounds like a good idea on the long term, but I would hope to find a less disruptive way of improving routing if possible.</p>
</div>
<div id="comment-71329-info" class="comment-info">
<span class="comment-age">(25 Oct '19, 11:59)</span> <span class="comment-user userinfo">kirma</span>
</div>
</div>
</div>
<div id="comment-tools-71326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71326-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71331"></span>

<div id="answer-container-71331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71331-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One thing you can try is make sure your shops are tagged with <code>addr:street</code> that matches exactly to a nearby street name (<em>If</em> in fact it's true -- don't fake it!) Routing engines will tend to try to approach the shop via that street. But having additional footways that are closer than the street, even underground in the subway station, may prevent this from working. Making sure all footways are tagged with level may help, may not. It's a limitation of the current routing engines.</p>
<p>Regarding "invisible" ways to route from entrance to POI, I asked about something similar last year in this question: <a href="/questions/65222/mapping-poi-nodes-with-multiple-entrances">https://help.openstreetmap.org/questions/65222/mapping-poi-nodes-with-multiple-entrances</a> The answering user brought up the proposed <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Associated_Entrance">associated_entrance</a> relation, to associate POIs with entrances so a routing engine could know where to aim when navigating from outside to a POI within a complex structure. But it's a very uncommon technique and unlikely to get routing support anytime soon.</p>
<p>It probably won't fix the short-term routing problem, but I think your best bet is using indoor mapping as mentioned by EdLoach. It's a popular technique so the software support for mapping, viewing, and routing will probably improve over time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '19, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71331" class="comments-container">
<span id="71332"></span>
<div id="comment-71332" class="comment">
<div id="post-71332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Although it would be questionable in nature, sometimes I'd wish there would be something like rendered=no, simply to indicate that a feature exists only for machine-derived results (routing, geocoding) and editing, not for general viewing...</p>
</div>
<div id="comment-71332-info" class="comment-info">
<span class="comment-age">(25 Oct '19, 20:12)</span> <span class="comment-user userinfo">kirma</span>
</div>
</div>
</div>
<div id="comment-tools-71331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71331-form-container" class="comment-form-container">
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

