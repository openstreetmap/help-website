+++
type = "question"
title = "&quot;Authentication required&quot; error, losing lots of map edits"
description = '''Lately I have been receiving an &quot;authentication required&quot; message very frequently when trying to save edits to iD. I am asked to re-enter my username and password, told my password is incorrect (it&#x27;s not, I have entered it over a dozen times now), and am eventually forced to close the tab and lose m...'''
date = "2015-04-10T14:49:00Z"
lastmod = "2015-04-11T00:20:00Z"
weight = 42249
keywords = [ "ideditor", "authentication", "editing" ]
aliases = [ "/questions/42249" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["Authentication required" error, losing lots of map edits](/questions/42249/authentication-required-error-losing-lots-of-map-edits)

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
<span id="post-42249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42249-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Lately I have been receiving an "authentication required" message very frequently when trying to save edits to iD. I am asked to re-enter my username and password, told my password is incorrect (it's not, I have entered it over a dozen times now), and am eventually forced to close the tab and lose my changes. I have attached a screenshot of the error message. Some students I am working with are having the same issue. Thoughts? <img src="/upfiles/Authorization_Message_-PC_Mapping.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-authentication" rel="tag" title="see questions tagged &#39;authentication&#39;">authentication</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '15, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/dcd5fb9045b2a4cfa4cc5014da332de3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CourtneyMClark&#39;s gravatar image" />
<p><span>CourtneyMClark</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CourtneyMClark has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '15, 13:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42249" class="comments-container">
<span id="42260"></span>
<div id="comment-42260" class="comment">
<div id="post-42260-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>off topic: the displayed changeset comment/commit message "#peaceCorps" <span>should be improved</span> to make it more useful</p>
</div>
<div id="comment-42260-info" class="comment-info">
<span class="comment-age">(11 Apr '15, 00:20)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42249-form-container" class="comment-form-container">
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

<span id="42250"></span>

<div id="answer-container-42250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issues you are experiencing are likely due to <a href="https://github.com/phusion/passenger/issues/1472">https://github.com/phusion/passenger/issues/1472</a> an issue with Passenger 5. It is likely that the operations team with roll back to Passenger 4 until this is resolved.</p>
<p>The only other workaround right now is to use an offline editor, JOSM or vespucci that allows you to save your work locally.</p>
<p>Thanks to TomH for debugging and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '15, 15:43</strong> </span></p>
</div>
</div>
<div id="comments-container-42250" class="comments-container">
&#10;</div>
<div id="comment-tools-42250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42250-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42251"></span>

<div id="answer-container-42251" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42251-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><p>Are you accepting and retaining cookies?</p></li>
<li><p>Do you have the problem with both http and https, you mention students so it is possible the university is unpacking secure packages and repackaging them in a way that breaks the trust between your browser and OSM.</p></li>
<li><p>Do other site you login to have similar issues.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/eb2bf53c1e2a0b137c64d07a34ad5a29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trigpoint&#39;s gravatar image" />
<p><span>trigpoint</span><br />
<span class="score" title="759 reputation points">759</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trigpoint has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-42251" class="comments-container">
<span id="42252"></span>
<div id="comment-42252" class="comment">
<div id="post-42252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you all. I'll pass the message on to the students (they are 6th grade, actually). Yes, I'm accepting and retaining cookies, and no, I don't have similar login issues with other sites. I just tried both http and https and didn't have issues saving edits with either, but the issue was also off and on anyways, so it is hard to say. It doesn't always occur.</p>
</div>
<div id="comment-42252-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 16:43)</span> <span class="comment-user userinfo">CourtneyMClark</span>
</div>
</div>
</div>
<div id="comment-tools-42251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42251-form-container" class="comment-form-container">
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

