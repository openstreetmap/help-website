+++
type = "question"
title = "Highway=raceway=escape"
description = '''A raceway has on certain corners escapes (areas) made out of gravel. Highway=escape is a specific part of a road or way and I don’t want to use highway=escape solely. What’s the right tagging scheme ? Has someone somewhere tagged something like it ?  Or could highway=raceway, raceway=escape do the t...'''
date = "2015-07-07T23:17:00Z"
lastmod = "2015-09-06T19:43:00Z"
weight = 44029
keywords = [ "areas", "raceway", "escape" ]
aliases = [ "/questions/44029" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Highway=raceway=escape](/questions/44029/highwayracewayescape)

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
<span id="post-44029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A raceway has on certain corners escapes (areas) made out of gravel. Highway=escape is a specific part of a road or way and I don’t want to use highway=escape solely. What’s the right tagging scheme ? Has someone somewhere tagged something like it ? Or could highway=raceway, raceway=escape do the trick for the gravel areas ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span> <span class="post-tag tag-link-raceway" rel="tag" title="see questions tagged &#39;raceway&#39;">raceway</span> <span class="post-tag tag-link-escape" rel="tag" title="see questions tagged &#39;escape&#39;">escape</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '15, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-44029" class="comments-container">
&#10;</div>
<div id="comment-tools-44029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44029-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="44053"></span>

<div id="answer-container-44053" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44053-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem with "highway=escape" is that gravel traps tend not really to be like "highways" - they're normally a patch of gravel (or these days sometimes tarmac) separated from the circuit by grass (like this one that you mapped at Assen <a href="https://www.openstreetmap.org/way/359189162">here</a>). A "highway=escape" running down a hill is a continuation of the highway and is a linear feature - a gravel trap isn't really either of those.</p>
<p>It looks like almost no-one maps these, so essentially you can do what you like as long as you don't misuse a tag for another feature - I'd actually be tempted to stick with the "raceway=escape; surface=gravel; area=yes" that you've already used.</p>
<p>A quick look at <a href="https://www.openstreetmap.org/#map=15/52.3903/4.5399">Zandvoort</a>, <a href="https://www.openstreetmap.org/#map=15/52.0732/-1.0189">Silverstone</a>, <a href="https://www.openstreetmap.org/#map=15/52.5163/-0.6567">Rockingham</a>, <a href="https://www.openstreetmap.org/#map=16/53.1732/-2.6148">Oulton</a>, <a href="https://www.openstreetmap.org/#map=15/53.3088/-0.0661">Cadwell</a> and <a href="https://www.openstreetmap.org/#map=16/52.8304/-1.3767">Donington</a> doesn't reveal any other mapped gravel traps. At <a href="https://www.openstreetmap.org/query?lat=36.58455&amp;lon=-121.74914#map=19/36.58458/-121.74883">Laguna Seca</a> someone's mapped the ones around the Corkscrew as "natural=beach", which surely isn't correct!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '15, 01:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44053" class="comments-container">
&#10;</div>
<div id="comment-tools-44053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44053-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44034"></span>

<div id="answer-container-44034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44034-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:highway=escape">Highway=escape</a> is <a href="http://taginfo.openstreetmap.org/tags/highway=escape">fairly well established</a>, so I'd keep usig that. And to make it clear what type of road it belongs to, I suggest using escape=(highway type being escaped from). It hasn't been used for that yet, but it seems logical to me. See also <a href="http://taginfo.openstreetmap.org/keys/escape%3Atype#values">escape:type</a> to specify the method (gravel, etc).</p>
<p>Why not the other way around as you suggest ? Thinks of consumers that haven't done the extra work to interpret escape values. All they'd see is highway=raceway (or highway=motorway) and they'd make a bad decision (such as rendering that way as a normal part of the racetrack). Think in terms of gracefull degradation for consumers that don't have a complete knowledge of the tag schema.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '15, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-44034" class="comments-container">
&#10;</div>
<div id="comment-tools-44034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44034-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44048"></span>

<div id="answer-container-44048" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44048-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A highway = escape connected to a highway = raceway let little room for interpretation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '15, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-44048" class="comments-container">
&#10;</div>
<div id="comment-tools-44048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44048-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45086"></span>

<div id="answer-container-45086" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is called run-off area</p>
<p><a href="https://en.wikipedia.org/wiki/Run-off_area">wiki run-off</a></p>
<p>there are: gravel trap astro turf tarmac concrete</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '15, 19:43</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-45086" class="comments-container">
&#10;</div>
<div id="comment-tools-45086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45086-form-container" class="comment-form-container">
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

