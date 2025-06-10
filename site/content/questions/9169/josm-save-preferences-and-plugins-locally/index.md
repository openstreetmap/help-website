+++
type = "question"
title = "JOSM - save preferences and plugins locally"
description = '''I am starting JOSM using the following script:  rem Set up settings + plugin location set APPDATA=&#92;APPDATA echo %APPDATA%  rem Download latest version curl http://josm.openstreetmap.de/download/josm-tested.jar -o josm-tested.jar  rem Run  java.exe -Xmx1024M -jar josm-tested.jar  The update works, th...'''
date = "2011-11-21T23:37:00Z"
lastmod = "2011-11-22T12:46:00Z"
weight = 9169
keywords = [ "josm" ]
aliases = [ "/questions/9169" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM - save preferences and plugins locally](/questions/9169/josm-save-preferences-and-plugins-locally)

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
<span id="post-9169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9169-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am starting JOSM using the following script:</p>
<pre><code>rem Set up settings + plugin location
set APPDATA=\APPDATA
echo %APPDATA%
&#10;rem Download latest version
curl http://josm.openstreetmap.de/download/josm-tested.jar -o josm-tested.jar
&#10;rem Run 
java.exe -Xmx1024M -jar josm-tested.jar</code></pre>
<p>The update works, the running itself works, but all preferences are saved to C:UsersMyNameAppDataRoaming despite environment variable being set to APPDATA.</p>
<p>I looked into the source code of JOSM and on the first look it seems like asking for the correct environment variable. Why does it not work?</p>
<p>Background: I want to have JOSM in a folder together with everything, however I do not want to install java on a flash drive and run it from there ...</p>
<p><strong>Edit:</strong> If anyone is interested this is the result so far (updates josm only if needed, keeps all settings within own folder, starts josm and tracerserver (only relevant for the Czech Rep.)</p>
<pre><code>@echo off
&#10;echo:Setting up settings + plugin location
set APPDATA=appdata
echo:set to %APPDATA%
&#10;echo:Determining latest tested version
curl http://josm.openstreetmap.de/tested -verbose -o tested.txt
set /p testedVersion=&lt;tested.txt
&#10;echo:Determining current version
java.exe -Xmx1024M -jar josm-tested.jar -? | findstr /C:&quot;Revision&quot; &gt; current.txt
set /p temp=&lt;current.txt
set currentVersion=%temp:~10,4%
&#10;set /a diffVersion=testedVersion-currentVersion
echo %diffVersion%
&#10;if %diffVersion% gtr 0 (
    echo:Update needed
) else (
    echo:JOSM is up to date 
    goto runapps
)
&#10;echo:Downloading latest version
rem Download to temporary file, then copy and remove - to prevent file corruption when download fails
curl http://josm.openstreetmap.de/download/josm-tested.jar -o josm-tested-download.jar
move /Y josm-tested-download.jar josm-tested.jar
del josm-tested-download.jar
&#10;:runapps
echo Starting tracer server
start TracerServer\bin\Osm.Kn.Trace.Server.exe
&#10;echo Starting JOSM 
start java.exe -Xmx1024M -jar josm-tested.jar
&#10;:end</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '11, 23:37</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '11, 19:02</strong> </span></p>
</div>
</div>
<div id="comments-container-9169" class="comments-container">
&#10;</div>
<div id="comment-tools-9169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9169-form-container" class="comment-form-container">
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

<span id="9176"></span>

<div id="answer-container-9176" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9176-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also pass the preferences folder on the command line. Assuming a subfolder of "JosmTestedSettings" -</p>
<p>java.exe -Xmx1024M -jar josm-tested.jar -Djosm.home="./JosmTestedSettings"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '11, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-9176" class="comments-container">
&#10;</div>
<div id="comment-tools-9176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9176-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9170"></span>

<div id="answer-container-9170" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9170-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found the problem, it has to be set to <code>APPDATA</code>, not <code>\APPDATA</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '11, 00:12</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-9170" class="comments-container">
&#10;</div>
<div id="comment-tools-9170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9170-form-container" class="comment-form-container">
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

