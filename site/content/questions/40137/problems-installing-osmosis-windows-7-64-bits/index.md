+++
type = "question"
title = "Problems installing Osmosis Windows 7 64 bits"
description = '''Hi everybody, I am having some problems to install Osmosis in my Windows 7 64 bits. I downloaded the last versión available (0.47.1 in http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip). I followed the install guide (http://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Window...'''
date = "2015-01-08T11:54:00Z"
lastmod = "2015-03-25T14:36:00Z"
weight = 40137
keywords = [ "windows7", "osmosis", "install" ]
aliases = [ "/questions/40137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problems installing Osmosis Windows 7 64 bits](/questions/40137/problems-installing-osmosis-windows-7-64-bits)

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
<span id="post-40137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40137-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody,</p>
<p>I am having some problems to install Osmosis in my Windows 7 64 bits. I downloaded the last versión available (0.47.1 in <a href="http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip).">http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip).</a> I followed the install guide (<a href="http://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)">http://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)</a> and <a href="http://learnosm.org/en/osm-data/osmosis/#install-osmosis).">http://learnosm.org/en/osm-data/osmosis/#install-osmosis).</a></p>
<p>I also changed the java issues as It is recommended in the guide:</p>
<ul>
<li>Find the java application (exe file)</li>
<li>it's probably in C:\Program Files (x86)\Java\jre6\bin.</li>
<li>Edit C:\Program Files (x86)\osmosis\bin\osmosis.bat</li>
<li>Find the line about 3/4 of the way down that sets JAVACMD and change it to:</li>
<li>IF "%JAVACMD%"=="" set JAVACMD="C:\Program Files (x86)\Java\jre7\bin\java"</li>
<li>You may also have to change the line near the end that sets EXEC and put double quotes before and after %JAVACMD%*</li>
</ul>
<p>When I check if osmosis is working through executing it in cmd, it doesn´t work: c:\osmosis\bin\osmosis or directly from c:\ --&gt; "Java" is not recognize as internal or external command, programm or ...</p>
<p>The weird thing is that I also installed osmosis in a virtual machine with xp and there It does work. The problem is that It works really really slow.</p>
<p>Does anybody know how to fix this problem in Windows 7?</p>
<p>Thanks in advanced, Fermin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '15, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1e7958f3cade065202251c2a3cc8142b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frose&#39;s gravatar image" />
<p><span>frose</span><br />
<span class="score" title="100 reputation points">100</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frose has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '15, 11:55</strong> </span></p>
</div>
</div>
<div id="comments-container-40137" class="comments-container">
&#10;</div>
<div id="comment-tools-40137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40137-form-container" class="comment-form-container">
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

<span id="40139"></span>

<div id="answer-container-40139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40139-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm using Osmosis on Windows 8 64 bit, and am using</p>
<pre><code>IF &quot;%JAVACMD%&quot;==&quot;&quot; set JAVACMD=C:\Windows\SysWOW64\java</code></pre>
<p>I don't remember changing anything else (though admit I seem to be a couple of versions behind at the moment).</p>
<p>Edit: If you just type JAVA at the command prompt, does it run?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '15, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '15, 12:12</strong> </span></p>
</div>
</div>
<div id="comments-container-40139" class="comments-container">
<span id="40151"></span>
<div id="comment-40151" class="comment">
<div id="post-40151-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi Ed,</p>
<p>You were right. I don´t know why but my java worked for several programms but not at the command prompt. I´ve updated the java versión and now It works everywhere although I have to close-open the command prompt window after each command because it seems only to allow one command each time. I think I could overcome this little problem.</p>
<p>Thanks!!!</p>
</div>
<div id="comment-40151-info" class="comment-info">
<span class="comment-age">(08 Jan '15, 14:20)</span> <span class="comment-user userinfo">frose</span>
</div>
</div>
<span id="41917"></span>
<div id="comment-41917" class="comment">
<div id="post-41917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interestingly I've just seen (on 64-bit Windows 7) an Oracle Java update delete the "SysWOW64" 32-bit version, though what I presume is a 32-bit version remains in "C:\Program Files (x86)\Java\jre1.8.0_40\bin".</p>
<p>So if you absolutely need a 32-bit version, and the "SysWOW64" one is missing, you know where to look...</p>
</div>
<div id="comment-41917-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 14:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40139-form-container" class="comment-form-container">
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

