+++
type = "question"
title = "Ubuntu: cant install latest JOSM file..."
description = '''Ive tried following the instructions given at: http://josm.openstreetmap.de/wiki/Download But when I get to the point where it instructs you to install the &quot;josm-latest&quot; file I get an error message returned as follows: (note it says I typed in josm-tested but i simply copied my last attempt. Ive dow...'''
date = "2012-08-13T04:17:00Z"
lastmod = "2012-08-13T20:44:00Z"
weight = 15000
keywords = [ "josm", "update", "ubuntu" ]
aliases = [ "/questions/15000" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ubuntu: cant install latest JOSM file...](/questions/15000/ubuntu-cant-install-latest-josm-file)

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
<span id="post-15000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15000-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ive tried following the instructions given at: <a href="http://josm.openstreetmap.de/wiki/Download">http://josm.openstreetmap.de/wiki/Download</a> But when I get to the point where it instructs you to install the "josm-latest" file I get an error message returned as follows: (note it says I typed in josm-tested but i simply copied my last attempt. Ive downloaded the .jar file with "josm tested" file)</p>
<pre><code>michael@michael-Satellite-L350D:~$ sudo apt-get install josm-latest                       Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package josm-latest</code></pre>
<p>Im not sure why its unable to locate the package... any help would be appreciated... Michael</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '12, 04:17</strong></p>
<img src="https://secure.gravatar.com/avatar/66001846f0632f073fa821d84341d7cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Azzitizz&#39;s gravatar image" />
<p><span>Azzitizz</span><br />
<span class="score" title="445 reputation points">445</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Azzitizz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15000" class="comments-container">
<span id="15001"></span>
<div id="comment-15001" class="comment">
<div id="post-15001-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Did you add the josm repository to your <em>sources.list</em> and run <em>apt-get update</em> afterwards?</p>
</div>
<div id="comment-15001-info" class="comment-info">
<span class="comment-age">(13 Aug '12, 05:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15000-form-container" class="comment-form-container">
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

<span id="15043"></span>

<div id="answer-container-15043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15043-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apt-get usually is the preferred method, but this is really simple if you can configure things for yourself. This is especially true because the distribution version of josm may well be out of date. Here is what I did --</p>
<p>1:download josm-tested.jar from the link on <a href="https://wiki.openstreetmap.org/wiki/JOSM">https://wiki.openstreetmap.org/wiki/JOSM</a><br />
2: make a directory called "lib" under your HOME directory, and put josm-tested.jar there<br />
3: find the "bin" directory under your HOME directory and create a script file josm.sh containing<br />
</p>
<p>#!/bin/bash<br />
java -jar ~/lib/josm-tested.jar</p>
<p>4: in the properties, set the toggle "Allow executing file as program"</p>
<p>Then typing josm.sh from a terminal window or double clicking on the josm.sh file icon will launch josm</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '12, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/31393c8dfc76d3e3c585227cfef175c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johntrudy&#39;s gravatar image" />
<p><span>johntrudy</span><br />
<span class="score" title="110 reputation points">110</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johntrudy has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-15043" class="comments-container">
&#10;</div>
<div id="comment-tools-15043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15043-form-container" class="comment-form-container">
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

