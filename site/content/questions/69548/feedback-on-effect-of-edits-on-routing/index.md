+++
type = "question"
title = "Feedback on effect of edits on routing"
description = '''I have just started using OSM for hiking tracks. The Directions panel is great for fast planning of tracks, but three times out of eight I have found the route is diverted around what looks like incomplete map data, like connections or permissions. I have edited the data, and would like to check if ...'''
date = "2019-06-10T11:09:00Z"
lastmod = "2019-06-10T20:30:00Z"
weight = 69548
keywords = [ "directions", "editing", "routing" ]
aliases = [ "/questions/69548" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Feedback on effect of edits on routing](/questions/69548/feedback-on-effect-of-edits-on-routing)

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
<span id="post-69548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69548-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have just started using OSM for hiking tracks. The Directions panel is great for fast planning of tracks, but three times out of eight I have found the route is diverted around what looks like incomplete map data, like connections or permissions. I have edited the data, and would like to check if that fixes the problem, but the effects don't seem to be shown on the directions. I guess this is because OSRM has to wait for a graph update. Could there be a way of checking quicker? Like being able to see the local route graph for a class of transport? Or running the router on what is on screen?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '19, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/01375adce3c1a6838725d5f088310e4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arbuthnot&#39;s gravatar image" />
<p><span>arbuthnot</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arbuthnot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69548" class="comments-container">
&#10;</div>
<div id="comment-tools-69548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69548-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="69550"></span>

<div id="answer-container-69550" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69550-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is: no.</p>
<p>The long version: all routing engines have to update the data and the routing graph in some fashion and currently none of the server side engines does this incrementally (for technical reasons). So typically you will need to wait a day or so to see you changes there.</p>
<p>JOSM used to have a plugin that did this on freshly edited data, but no idea how well this worked/works. Outside of that you best bet is OSMand with a "live" subscription that will typically update in 1-2 hours.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '19, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69550" class="comments-container">
&#10;</div>
<div id="comment-tools-69550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69550-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69552"></span>

<div id="answer-container-69552" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69552-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simon mentioned the JOSM plugins, so I don't understand his categorical "no". I would rather say "yes, but". :-)</p>
<p>Instead of iD you can use the <a href="https://wiki.openstreetmap.org/wiki/JOSM">OSM Editor JOSM</a>. For this editor there are two plugins available: <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/GraphView">GraphView</a> and <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Routing">Routing</a>. Both work with the OSM data currently loaded in the editor including all your changes you have made but not uploaded yet. The former plugin provides an overlay for a routing graph. It's a bit difficult to spot gaps with this tool, though. The latter plugin offers rudimentary routing and enables you to test your edits. It does not take into account access restrictions ("no bicycles here"), though. So it works to test if all roads are there and connected but not to test for the right permissions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '19, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69552" class="comments-container">
<span id="69556"></span>
<div id="comment-69556" class="comment">
<div id="post-69556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Following up on your advice, I have installed JOSM, found the remote control option, and enabled it. I get Failed to initialize communication with the OSM server <a href="http://api.openstreetmap.org/api.">http://api.openstreetmap.org/api.</a> Check the server URL in your preferences and your internet connection.</p>
<p>I have also tried downloading a map into JOSM, and get the same message. I have searched for advice on this, followed recommendations about connection and proxy settings , and still get the same. Sorry for all the beginner problems.</p>
</div>
<div id="comment-69556-info" class="comment-info">
<span class="comment-age">(10 Jun '19, 16:38)</span> <span class="comment-user userinfo">arbuthnot</span>
</div>
</div>
<span id="69562"></span>
<div id="comment-69562" class="comment">
<div id="post-69562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a>: as said that was the short version.</p>
</div>
<div id="comment-69562-info" class="comment-info">
<span class="comment-age">(10 Jun '19, 17:53)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="69569"></span>
<div id="comment-69569" class="comment">
<div id="post-69569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16772/arbuthnot">@arbuthnot</a>: Better start a new question for this issue.</p>
</div>
<div id="comment-69569-info" class="comment-info">
<span class="comment-age">(10 Jun '19, 20:30)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-69552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69552-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69565"></span>

<div id="answer-container-69565" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69565-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to test routing for small areas you can use <a href="https://wiki.openstreetmap.org/wiki/OsmAndMapCreator">OSMAndMapCreator</a> to generate OsmAnd file that can either be sideloaded onto a phone for testing or tested directly in the map creator software.</p>
<p>The MapCreator software is rather rough, so YMMV on testing without transferring to a mobile device.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '19, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-69565" class="comments-container">
<span id="69567"></span>
<div id="comment-69567" class="comment">
<div id="post-69567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've just checked and the router will route along un-uploaded ways in a JOSM file, so it may be possible to test reasonably complex edits before making them 'live'.</p>
</div>
<div id="comment-69567-info" class="comment-info">
<span class="comment-age">(10 Jun '19, 20:18)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-69565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69565-form-container" class="comment-form-container">
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

