+++
type = "question"
title = "Need help understanding what&#x27;s happening with a specific junction (I-66 westbound at Dulles toll road split)"
description = '''Hello editors, I&#x27;m a NOOB here but quite familiar with wiki editing. I&#x27;ve recently come to learn that it appears Tesla uses OSM for routing. I thought I would look up road junction on my test route where my Tesla couldn&#x27;t make the maneuver happen correctly and, sure enough, the split marker is place...'''
date = "2019-11-09T04:50:00Z"
lastmod = "2019-11-09T17:52:00Z"
weight = 71551
keywords = [ "splitting", "split" ]
aliases = [ "/questions/71551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help understanding what's happening with a specific junction (I-66 westbound at Dulles toll road split)](/questions/71551/need-help-understanding-whats-happening-with-a-specific-junction-i-66-westbound-at-dulles-toll-road-split)

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
<span id="post-71551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71551-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello editors,</p>
<p>I'm a NOOB here but quite familiar with wiki editing. I've recently come to learn that it appears Tesla uses OSM for routing. I thought I would look up road junction on my test route where my Tesla couldn't make the maneuver happen correctly and, sure enough, the split marker is placed way, way, way too late. It needs to be many hundreds of yards further east where the white line starts. I thought this would be simple enough to edit but when I drag the motorway junction marker, there is another line feature that gets dragged along with it. I suspect this line feature is mistakenly connected to the split. The line appears to be a boundary marker but even that doesn't quite make sense.</p>
<p>My questions are:</p>
<p>1) Should I just move the split and let this line get dragged with the split to the new location? 2) Is there a proper place to discuss such moves if I'm not certain of what to do? 3) Could someone take a look at the I-66 westbound direction at the split where Dulles tollway splits off and see if you agree with me that this ancillary line is mistakenly connected to the split? 4) How would I break the connection to the split if we do deem it to be erroneous?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '19, 04:50</strong></p>
<img src="https://secure.gravatar.com/avatar/6bf1e9226bd603a0363a05165e0e27e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doyendon&#39;s gravatar image" />
<p><span>doyendon</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doyendon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71551" class="comments-container">
&#10;</div>
<div id="comment-tools-71551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71551-form-container" class="comment-form-container">
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

<span id="71557"></span>

<div id="answer-container-71557" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71557-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><p>No. You should disconnect them. Same with you, I believe it is erroneously connected , since it looks like it is supposed to follow the Haycock Road overpass.</p></li>
<li><p>help.openstreetmap.org is more for straightforward or topical questions. OSM Forum, Reddit, Discord, or whatever your local community , if you need to have detailed/exploratory discussion.</p></li>
<li><p>First of all, you should note that some imagery is outdated. I suppose this section has been recently widened and reconfigured? Now on your question, there's the matter of OSM history, and backward compatibility. What are you are seeing now and thinking about doing yourself is the "old" way. Lane-based features are newer, and you need to know if Tesla or the source they are using actually support such navigation mechanism to have any effect. Since there's no physical separation between the white solid line delineated lanes, the "old way" is ideally incorrect. There should simply be <code>turn:lanes=through|through|slight_right|slight_right</code> + <code>destination:lanes=none|none|Dulles Airport;Baltimore|Dulles Airport;Baltimore</code> + <code>destination:ref=none|none|VA 267|VA267</code> + <code>destination:to:ref=none|none|I 495|I 495</code> on the approach to guide drivers, plus <code>change:lanes=yes|not_left|not_right|yes</code> in addition on the white solid line marked section. Pushing the node back may be functional in driving, but does not reflect reality on the roadway. You should consult with other editors in this area on this issue.</p></li>
<li><p>Unfortunately the iD editor has implemented very stringent editing rules, because the node here connects ways in relations. It can only be disconnected in JOSM. You can ask someone in the area to review and help you.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '19, 06:00</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '19, 06:11</strong> </span></p>
</div>
</div>
<div id="comments-container-71557" class="comments-container">
<span id="71570"></span>
<div id="comment-71570" class="comment">
<div id="post-71570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a>, thanks for the helpful response. Some of it is still greek to me. There is little known about what Tesla is or isn't using exactly. All I know is when I drive this route on Navigate on Autopilot, the car makes no effort to get to the right lanes and takes no action to follow the split onto Dulles Toll Road until roads start to physically split, which just so happens to coincide with the location of the motorway junction object in OSM as it exists today.</p>
<p>For your "ideal" way, would those stipulations be assigned to the road segment where the white lane exists?</p>
<p>I'll try to connect into the Reddit community.</p>
</div>
<div id="comment-71570-info" class="comment-info">
<span class="comment-age">(09 Nov '19, 17:52)</span> <span class="comment-user userinfo">doyendon</span>
</div>
</div>
</div>
<div id="comment-tools-71557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71557-form-container" class="comment-form-container">
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

