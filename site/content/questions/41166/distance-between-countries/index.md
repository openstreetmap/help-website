+++
type = "question"
title = "Distance between countries"
description = '''Hi, I&#x27;m a newbie and feel a little foolish to ask this question. I have learned that you can get the routing distance between two points like Paris and Berlin.  Is it possible to ask for the distance between two points separated by countries, like driving from Paris to Berlin means x km in France an...'''
date = "2015-02-20T11:26:00Z"
lastmod = "2015-02-26T10:21:00Z"
weight = 41166
keywords = [ "distance", "borders", "countries" ]
aliases = [ "/questions/41166" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Distance between countries](/questions/41166/distance-between-countries)

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
<span id="post-41166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41166-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm a newbie and feel a little foolish to ask this question. I have learned that you can get the routing distance between two points like Paris and Berlin. Is it possible to ask for the distance between two points separated by countries, like driving from Paris to Berlin means x km in France and y km in Germany?</p>
<p>How could you do that?</p>
<p>Thank you very much for your advice</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-countries" rel="tag" title="see questions tagged &#39;countries&#39;">countries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '15, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/2e4706b690bf4e8533fca09391851d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karten-Newbie&#39;s gravatar image" />
<p><span>Karten-Newbie</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karten-Newbie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41166" class="comments-container">
<span id="41387"></span>
<div id="comment-41387" class="comment">
<div id="post-41387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>thank you for your advice. What I have learned so far is that I can get the routing information from (<a href="http://map.project-osrm.org/)">http://map.project-osrm.org/)</a> and with that information I can get the country information from Nominatin.</p>
<p>What I'm still missing - is there any trick how I could get the information if one of the routing distances is a highway, and/or whether I do have to pay toll. What I'm asking is: Is there anything like Nominatin with additional fields (highway, toll road)?</p>
<p>Thanks again for your help.</p>
</div>
<div id="comment-41387-info" class="comment-info">
<span class="comment-age">(26 Feb '15, 10:21)</span> <span class="comment-user userinfo">Karten-Newbie</span>
</div>
</div>
</div>
<div id="comment-tools-41166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41166-form-container" class="comment-form-container">
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

<span id="41185"></span>

<div id="answer-container-41185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41185-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most routing engines provide you with instructions which often contain markers where you cross the border. You may use these points to calculate the distance within a given country (like MapQuest Open). Often even if it's missing (osrm, openrouteservice, YOURS, graphhopper) there is an indicator of border crossing like roads changing their names, which could help you. (There's a few link on my <a href="http://wiki.openstreetmap.org/wiki/User:Grin/bookmarks#routing">bookmark page</a>.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '15, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/543f907c30de5772ec0625b82264c188?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grin&#39;s gravatar image" />
<p><span>grin</span><br />
<span class="score" title="158 reputation points">158</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41185" class="comments-container">
&#10;</div>
<div id="comment-tools-41185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41185-form-container" class="comment-form-container">
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

