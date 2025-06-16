+++
type = "question"
title = "Installing Osmosis"
description = '''I&#x27;m trying to install Osmosis on Windows XP. I moved the osmosis-0.38 folder into my profile under documents and settings. Do I need to move the .bat and .jar files into the main directory out of the folder. When I try to run the script to merge two files, I get an error that says &quot;unable to access ...'''
date = "2011-01-01T22:46:00Z"
lastmod = "2011-06-08T09:54:00Z"
weight = 1980
keywords = [ "osmosis" ]
aliases = [ "/questions/1980" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Installing Osmosis](/questions/1980/installing-osmosis)

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
<span id="post-1980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1980-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to install Osmosis on Windows XP. I moved the osmosis-0.38 folder into my profile under documents and settings. Do I need to move the .bat and .jar files into the main directory out of the folder. When I try to run the script to merge two files, I get an error that says "unable to access jarfile osmosis.jar" Is there anything else I need to do to install it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jan '11, 22:46</strong></p>
<img src="https://secure.gravatar.com/avatar/5b617670d373ec7c3c87ad9c557327c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nmixter&#39;s gravatar image" />
<p><span>nmixter</span><br />
<span class="score" title="131 reputation points">131</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nmixter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1980" class="comments-container">
&#10;</div>
<div id="comment-tools-1980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1980-form-container" class="comment-form-container">
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

<span id="2012"></span>

<div id="answer-container-2012" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2012-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should <em>not</em> need to move the bat or jar files from their unzipped directory locations. You should be able to run osmosis.bat from the bin directory.</p>
<p>This old forum discussion gives some <a href="http://forum.openstreetmap.org/viewtopic.php?id=4039">messy solutions for getting osmosis classpaths to work</a> However things have moved on since then. I think osmosis launch scripts (<a href="http://svn.openstreetmap.org/applications/utils/osmosis/trunk/package/bin/osmosis.bat">osmosis.bat</a> for windows) have changed to use some <code>codehaus.classworlds.Launcher</code> mechanism, which is hopefully better. In general, you'll have an easier time if you can get it to work without rearranging anything. Keep things as they are when you unzip osmosis. There are some other notes for windows users on the <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis wiki page</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '11, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-2012" class="comments-container">
<span id="5633"></span>
<div id="comment-5633" class="comment">
<div id="post-5633-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Osmosis 0.38 works if the .bat file is called from its initial location (as Harry says this was not true for much older versions (0.29 &amp; 0.31). I usually run it from the osmosis directory and mostly I will write another batch file so that I dont forget how I've used the osmosis options. So binosmosis.bat --rx file=....</p>
</div>
<div id="comment-5633-info" class="comment-info">
<span class="comment-age">(08 Jun '11, 09:54)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-2012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2012-form-container" class="comment-form-container">
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

