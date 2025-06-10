+++
type = "question"
title = "Should indoor ways be created to connect a building&#x27;s entrance and exit?"
description = '''I was under the impression that a node tagged with amenity=parking_entrance would mark the end of the road as it met the building, at least in cases where indoor information isn&#x27;t available. However, I&#x27;ve seen a user create skeleton ways connecting these parking entrances, apparently as a fix/workar...'''
date = "2012-11-19T22:20:00Z"
lastmod = "2020-07-08T09:00:00Z"
weight = 17815
keywords = [ "parking_entrance", "indoor", "routing" ]
aliases = [ "/questions/17815" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should indoor ways be created to connect a building's entrance and exit?](/questions/17815/should-indoor-ways-be-created-to-connect-a-buildings-entrance-and-exit)

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
<span id="post-17815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17815-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was under the impression that a node tagged with amenity=parking_entrance would mark the end of the road as it met the building, at least in cases where indoor information isn't available. However, I've seen a user create skeleton ways connecting these parking entrances, apparently as a fix/workaround for routing issues detected by Project OSRM (e.g. <a href="http://www.openstreetmap.org/browse/way/188908352">http://www.openstreetmap.org/browse/way/188908352</a> ). Is this recommended?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-parking_entrance" rel="tag" title="see questions tagged &#39;parking_entrance&#39;">parking_entrance</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '12, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4de1232f3377cc783012d889d0375c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_012&#39;s gravatar image" />
<p><span>Paul_012</span><br />
<span class="score" title="686 reputation points">686</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_012 has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-17815" class="comments-container">
&#10;</div>
<div id="comment-tools-17815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17815-form-container" class="comment-form-container">
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

<span id="17861"></span>

<div id="answer-container-17861" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17861-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Paul_012 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's always difficult to say what is "recommended" or not in OSM. The problem with indoor mapping is the difficulty to verify the information. What is done in your example is not incorrect. The position of the parking aisle lane is probably a rough outline but it is better than nothing and accuracy can be improved in the future by the next contributors. BUT it might require an "access" tag if the parking access is restricted to some public (<a href="http://wiki.openstreetmap.org/wiki/Key:access">private</a>) or time (<a href="http://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a>) or requires some <a href="http://wiki.openstreetmap.org/wiki/Key:fee">fee</a>. An explicit tag like "access=yes" might clarify this point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17861" class="comments-container">
<span id="18267"></span>
<div id="comment-18267" class="comment">
<div id="post-18267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm concerned that while making such educated guesses may generally be useful, (the linked example is a pretty simple case of two exits at each end of a parking building,) there's the possibility that the result may turn out to be completely wrong, especially in more complex buildings with several entrances and exits. Is risking such incorrect information really better than having nothing at all, especially since satellite navigators aren't going to work indoors anyway?</p>
</div>
<div id="comment-18267-info" class="comment-info">
<span class="comment-age">(07 Dec '12, 08:01)</span> <span class="comment-user userinfo">Paul_012</span>
</div>
</div>
<span id="18269"></span>
<div id="comment-18269" class="comment">
<div id="post-18269-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I replied for your case: 1 entrance, 1 exit. In such easy case, it is of course not harmful to speculate on the parking service road. In more complexes cases, it is of course better to not introduce intentional mistakes or, at least, high speculations on the routing options inside the building. In such cse, it is better to do nothing. But more generally, for all contributors mapping remotely, you have to use your common sense when you add stuff in OSM. More importantly if you decide to add speculated information in OSM, add your sources or a 'note' tag explaining that you are not 100% sure.</p>
</div>
<div id="comment-18269-info" class="comment-info">
<span class="comment-age">(07 Dec '12, 09:13)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-17861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17861-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75594"></span>

<div id="answer-container-75594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75594-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-75594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At least 60% of public entrances must be accessible in new construction, in addition to entrances directly serving tenancies, parking facilities, pedestrian tunnels and elevated walkways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '20, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75594" class="comments-container">
&#10;</div>
<div id="comment-tools-75594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75594-form-container" class="comment-form-container">
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

