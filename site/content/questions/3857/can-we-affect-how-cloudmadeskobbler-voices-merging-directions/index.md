+++
type = "question"
title = "[closed] Can we affect how CloudMade/skobbler voices merging directions?"
description = '''This is a fairly specific skobbler situation, but there might be an underlying issue. I don&#x27;t have a direct contact with skobbler developers. They have a forum and a company representative answers almost all specific questions with a &quot;I will pass this info on to the developers&quot;. Why the devs can&#x27;t r...'''
date = "2011-03-16T18:58:00Z"
lastmod = "2011-03-17T06:34:00Z"
weight = 3857
keywords = [ "voice_command", "skobbler", "routing", "cloudmade" ]
aliases = [ "/questions/3857" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Can we affect how CloudMade/skobbler voices merging directions?](/questions/3857/can-we-affect-how-cloudmadeskobbler-voices-merging-directions)

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
<span id="post-3857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3857-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-3857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a fairly specific skobbler situation, but there might be an underlying issue. I don't have a direct contact with skobbler developers. They have a forum and a company representative answers almost all specific questions with a "I will pass this info on to the developers". Why the devs can't read their own forum is beyond me. I can't imagine it's the language thing. Anyway, I have asked the following question there and the answer (from the apparently non-technical company rep) was: "We get routes from CloudMade, it could be their bug". I have even less contact with CloudMade or an idea how it works, so this is the best place I could think of bringing my question.</p>
<p>If you check <a href="http://www.mapdust.com/detail/161593">this</a> skobbler bug I created, the route takes me on Glenwood Drive north and on to the CA-73 via the on-ramp. For some reason, the voice direction comes through as "Now take the exit right". It should be "Take the entrance on the right" or "Merge right" or something like that. "Exit" is quite the opposite of what the maneuver is. I know skobbler is not made by native English speakers, but CloudMade is. And I don't think it's the language thing because I don't get the same strange voice command when I enter other freeways. So i have to believe it's the configuration and tagging of the interchange that's causing it.</p>
<p>I guess my question is: can someone with deeper knowledge of skobbler and/or CloudMade explain what causes them to give such a strange command, and is there anything I can change in OSM tagging of the node or the motorway_link to change this behavior?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-voice_command" rel="tag" title="see questions tagged &#39;voice_command&#39;">voice_command</span> <span class="post-tag tag-link-skobbler" rel="tag" title="see questions tagged &#39;skobbler&#39;">skobbler</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-cloudmade" rel="tag" title="see questions tagged &#39;cloudmade&#39;">cloudmade</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '11, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>16 Mar '11, 23:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-3857" class="comments-container">
<span id="3865"></span>
<div id="comment-3865" class="comment">
<div id="post-3865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a native English speaker, I'd say that Skobbler's directions were correct here - it's asking you to take an exit from Glenwood Drive onto another road.</p>
<p>One more thing, when logging bugs in Mapdust it would help to be a little more descriptive - type="Other" / description="Exit" doesn't really help the OSM editor who spots the mapdust entry on the map and wants to fix it.<br />
</p>
<p>Ideally Skobbler ought to have a "not a problem with the map but with our routing" category which could be sent to Skobbler/Cloudmade devs rather than OSM editors, but in the absence of that more description would help.</p>
</div>
<div id="comment-3865-info" class="comment-info">
<span class="comment-age">(16 Mar '11, 23:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="3869"></span>
<div id="comment-3869" class="comment">
<div id="post-3869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let's just say that "Exit" was a note to self, since I _am_ the OSM editor for the area, or at least the MapDust watcher - as far as I know. There is an older bug dropped several feet away with a more detailed comment. I dropped another to remind myself that the issue has not been resolved.</p>
<p>I am still of the opinion that the wording is poor. One "exits" a freeway to a surface road. One does not "exit" a surface road to go on a higher rank motorway. Usually skobbler gives correct prompt in this situation. I forgot what the wording is, but will be happy to report after I test it tomorrow.</p>
</div>
<div id="comment-3869-info" class="comment-info">
<span class="comment-age">(17 Mar '11, 06:34)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3857-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by TomH 16 Mar '11, 23:34

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3861"></span>

<div id="answer-container-3861" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3861-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>I'm from CloudMade, will check this issue tomorrow and post an update here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '11, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2d402deb79e84abe84945a4ba0d49bdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pavelss&#39;s gravatar image" />
<p><span>Pavelss</span><br />
<span class="score" title="20 reputation points">20</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pavelss has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-3861" class="comments-container">
<span id="3862"></span>
<div id="comment-3862" class="comment">
<div id="post-3862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Excellent!</p>
</div>
<div id="comment-3862-info" class="comment-info">
<span class="comment-age">(16 Mar '11, 22:10)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3861-form-container" class="comment-form-container">
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

