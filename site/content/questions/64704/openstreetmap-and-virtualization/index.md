+++
type = "question"
title = "OpenStreetMap and Virtualization"
description = '''Can OpenStreetMap utilize the speed of SSD SAN Storage in a VMWare virtualization environment? Given that the ESXi host would be doing the ultimate write to the SAN, and hence is a potential bottleneck.'''
date = "2018-07-13T20:56:00Z"
lastmod = "2018-07-13T23:53:00Z"
weight = 64704
keywords = [ "storage", "san", "virtual" ]
aliases = [ "/questions/64704" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap and Virtualization](/questions/64704/openstreetmap-and-virtualization)

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
<span id="post-64704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can OpenStreetMap utilize the speed of SSD SAN Storage in a VMWare virtualization environment? Given that the ESXi host would be doing the ultimate write to the SAN, and hence is a potential bottleneck.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-storage" rel="tag" title="see questions tagged &#39;storage&#39;">storage</span> <span class="post-tag tag-link-san" rel="tag" title="see questions tagged &#39;san&#39;">san</span> <span class="post-tag tag-link-virtual" rel="tag" title="see questions tagged &#39;virtual&#39;">virtual</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '18, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/7ebd578646a31ef08d160d4b50b2ee3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rhelan&#39;s gravatar image" />
<p><span>Rhelan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rhelan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jul '18, 06:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span></p>
</div>
</div>
<div id="comments-container-64704" class="comments-container">
<span id="64709"></span>
<div id="comment-64709" class="comment">
<div id="post-64709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what do you mean by "OpenStreetMap"? Do you want to donate hardware? Do you want to run your own server (what should it serve?)?</p>
</div>
<div id="comment-64709-info" class="comment-info">
<span class="comment-age">(13 Jul '18, 21:20)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64704-form-container" class="comment-form-container">
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

<span id="64707"></span>

<div id="answer-container-64707" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64707-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer - yes.</p>
<p>Slightly longer answer - it'd depend on where the bottleneck is (what's limiting the speed of access to data on the SAN now?), but in all likelihood having the VM accessing faster disk will make a difference.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '18, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64707" class="comments-container">
<span id="64710"></span>
<div id="comment-64710" class="comment">
<div id="post-64710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SomeoneElse,</p>
<p>Thank you for the info.</p>
<p>For clarification, we would be hosting our own server and, before we converted part of our SAN into SSD storage, we wanted to be sure that this solution would be able to make full use of the increased write speed in a virtualized (VMWare) environment.</p>
</div>
<div id="comment-64710-info" class="comment-info">
<span class="comment-age">(13 Jul '18, 21:23)</span> <span class="comment-user userinfo">Rhelan</span>
</div>
</div>
<span id="64716"></span>
<div id="comment-64716" class="comment">
<div id="post-64716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You haven't said what kind of server you are hosting - I assume a tile server? There are many ways to shoot yourself in the foot by misconfiguring the virtual environment, or using a virtualisation software with badly written disk virtualisation drivers, but all else being equal, using SSD will make a difference. I notice you are talking about a SAN - this would commonly mean that the disks are not even built into the VM host, but somewhere else. This adds <em>another</em> layer of shoot-yourself-in-the-foot possiblities; database access on a tile server is very heavy on random I/O so it is the latency that counts. A SSD that is built into the VM host will <em>always</em> beat a SAN on performance.</p>
</div>
<div id="comment-64716-info" class="comment-info">
<span class="comment-age">(13 Jul '18, 23:53)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64707-form-container" class="comment-form-container">
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

