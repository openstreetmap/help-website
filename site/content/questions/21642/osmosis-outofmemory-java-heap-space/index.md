+++
type = "question"
title = "osmosis OutOfMemory: Java heap space"
description = '''Hi,  I am trying to import a large area from europe.osm. To do that I executed the following command:  &quot;C:&#92;Program Files (x86)&#92;osmosis&#92;bin&#92;osmosis.bat&quot; --read-xml file=&quot;G:&#92;Restricted&#92;Radu&#92;Facultate&#92;2012-2013&#92;Licenta&#92;europe.osm&quot; --bounding-box left=12.04 top=55.44 right=30.19 bottom=43.51 --write-pgs...'''
date = "2013-04-18T10:33:00Z"
lastmod = "2016-06-06T20:47:00Z"
weight = 21642
keywords = [ "space", "osmosis", "heap", "memory" ]
aliases = [ "/questions/21642" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis OutOfMemory: Java heap space](/questions/21642/osmosis-outofmemory-java-heap-space)

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
<span id="post-21642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,<br />
</p>
<p>I am trying to import a large area from europe.osm. To do that I executed the following command:<br />
</p>
<p><em>"C:\Program Files (x86)\osmosis\bin\osmosis.bat" --read-xml file="G:\Restricted\Radu\Facultate\2012-2013\Licenta\europe.osm" --bounding-box left=12.04 top=55.44 right=30.19 bottom=43.51 --write-pgsql host="localhost" database="eastern_europe" user="postgres" password="parola"</em></p>
<p>After almost a day of executing the following error dropped:<br />
<em>OutOfMemmory: Java heap space</em></p>
<p>From what I've seen on <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Tuning">http://wiki.openstreetmap.org/wiki/Osmosis/Tuning</a> a quick fix for this error is to set JAVACMD_OPTIONS to change the amount of memmory allocated (JAVACMD_OPTIONS=-Xmx2G will allocate 2 GB).<br />
</p>
<p>First of all I would like to know where do I have to set JAVACMD_OPTIONS. I am a Windows user. Do I have to edit osmosis.bat in bin directory?<br />
</p>
<p>Also setting JAVACMD_OPTIONS to 2GB will be enough for osmosis to not crush again or do I have to set other variables? I want to be sure before executing the process again because I have to wait almost a day to see any results and I will loose a lot of time if it crashes again.<br />
</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-space" rel="tag" title="see questions tagged &#39;space&#39;">space</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-heap" rel="tag" title="see questions tagged &#39;heap&#39;">heap</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '13, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '13, 08:38</strong> </span></p>
</div>
</div>
<div id="comments-container-21642" class="comments-container">
<span id="21643"></span>
<div id="comment-21643" class="comment">
<div id="post-21643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you running a 32-bit or 64-bit version of Java? You're running a 64-bit version of Windows (you're running osmosis.bat out of "Program Files (x86)") but we don't know which Java you're running.</p>
</div>
<div id="comment-21643-info" class="comment-info">
<span class="comment-age">(18 Apr '13, 10:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="21644"></span>
<div id="comment-21644" class="comment">
<div id="post-21644-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It seems I am running a 32-bit JVM. The command: "java -d64 -version" returned: "This instance does not support a 64-bit JVM".</p>
</div>
<div id="comment-21644-info" class="comment-info">
<span class="comment-age">(18 Apr '13, 10:40)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
<span id="21652"></span>
<div id="comment-21652" class="comment">
<div id="post-21652-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do I have to install the 64-bit version?</p>
</div>
<div id="comment-21652-info" class="comment-info">
<span class="comment-age">(18 Apr '13, 22:24)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
</div>
<div id="comment-tools-21642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21642-form-container" class="comment-form-container">
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

<span id="43007"></span>

<div id="answer-container-43007" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43007-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try typing at the command line that you're going to run osmosis, "set JAVACMD_OPTIONS=-server -Xmx2G"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '15, 00:42</strong></p>
<img src="https://secure.gravatar.com/avatar/59e1b9cb8f35621687c5dd58ec93ceb9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heshy&#39;s gravatar image" />
<p><span>Heshy</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heshy has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '15, 00:51</strong> </span></p>
</div>
</div>
<div id="comments-container-43007" class="comments-container">
&#10;</div>
<div id="comment-tools-43007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43007-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50047"></span>

<div id="answer-container-50047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50047-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SET EXEC="%JAVACMD%" %JAVACMD_OPTIONS% -cp "%PLEXUS_CP%" -Dapp.home="%MYAPP_HOME%" -Dclassworlds.conf="%MYAPP_HOME%\config\plexus.conf" %MAINCLASS% %OSMOSIS_OPTIONS% %*</p>
<p>As per osmosis.bat file , set java options in the bat file like any other parameter with set xxxx=value</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '16, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d750190498694bc0867cb9e15dda14f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajashekar&#39;s gravatar image" />
<p><span>rajashekar</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajashekar has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-50047" class="comments-container">
&#10;</div>
<div id="comment-tools-50047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50047-form-container" class="comment-form-container">
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

