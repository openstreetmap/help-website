+++
type = "question"
title = "Errors installing Osmosis on Window 10 64-bit"
description = '''Hi OpenStreetmap experts, I am having problems trying to installing Osmosis in my Windows 10 64-bits. I downloaded the lastest Java SE 32-bit &amp;amp; 64-bit as well as the latest osmosis version from http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip.  I tried to followed the install...'''
date = "2019-03-19T08:46:00Z"
lastmod = "2020-05-14T17:59:00Z"
weight = 68416
keywords = [ "windows", "osmosis" ]
aliases = [ "/questions/68416" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Errors installing Osmosis on Window 10 64-bit](/questions/68416/errors-installing-osmosis-on-window-10-64-bit)

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
<span id="post-68416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OpenStreetmap experts,</p>
<p>I am having problems trying to installing Osmosis in my Windows 10 64-bits. I downloaded the lastest Java SE 32-bit &amp; 64-bit as well as the latest osmosis version from <a href="http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip.">http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip.</a></p>
<p>I tried to followed the installation guide from <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)">https://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_(Windows)</a> and <a href="http://learnosm.org/en/osm-data/osmosis/#install-osmosis,">http://learnosm.org/en/osm-data/osmosis/#install-osmosis,</a> and thoroughly tried all the questions related to the trouble shooting on this forum and still don't get it to work.</p>
<p>In summary I have tried to</p>
<p>1) Edit the system environment variables and added the directory where osmosis.bat is located to the System variable (I tried both locations C:\Program Files (x86)\osmosis\bin\ and C:\osmosis\bin\ amongst my various attempts to get it to work).</p>
<p>2) Edit C:\Program Files (x86)\osmosis\bin\osmosis.bat and tried to point the Java application to both 32-bit and 64-bit versions in various attempts</p>
<pre><code>IF &quot;%JAVACMD%&quot;==&quot;&quot; set JAVACMD=&quot;C:\Program Files\Java\jre1.8.0_201\&quot;</code></pre>
<p>and</p>
<pre><code>IF &quot;%JAVACMD%&quot;==&quot;&quot; set JAVACMD=&quot;C:\Program Files (x86)\Java\jre1.8.0_201\bin\&quot;</code></pre>
<p>3) Tried to edit the OSMOSIS FILE (NOTE: not osmosis.bat) pointing to both the 32-bit and 64-bit Java SE application (I copied the 32-bits here but also tried the 64-bit as well)</p>
<pre><code>if [ -z &quot;$JAVACMD&quot; ] ; then
  # No JAVACMD provided in osmosis config files, therefore default to java
  JAVACMD=&quot;C:\Program Files (x86)\Java\jre1.8.0_201\bin\&quot;
fi</code></pre>
<p>and</p>
<pre><code>if [ -z &quot;$JAVACMD&quot; ] ; then
  # No JAVACMD provided in osmosis config files, therefore default to java
  JAVACMD=C:\Program Files (x86)\Java\jre1.8.0_201\bin\
fi</code></pre>
<p>4) The %JAVACMD% in the SET statement of the osmosis.bat file already have double quotes so I leave this alone</p>
<pre><code>SET EXEC=&quot;%JAVACMD%&quot; %JAVACMD_OPTIONS% -cp &quot;%PLEXUS_CP%&quot; -Dapp.home=&quot;%MYAPP_HOME%&quot; -Dclassworlds.conf=&quot;%MYAPP_HOME%\config\plexus.conf&quot; %MAINCLASS%  %OSMOSIS_OPTIONS% %*</code></pre>
<p>5) I also commented out</p>
<pre><code>REM # IF EXIST &quot;%USERPROFILE%\osmosis.bat&quot; CALL &quot;%USERPROFILE%\osmosis.bat&quot;</code></pre>
<p>in the osmosis.bat file because I repeatedly run into BATCH RECURSION exceed stacks limit error</p>
<p>and left</p>
<pre><code>IF EXIST &quot;%ALLUSERSPROFILE%\osmosis.bat&quot; CALL &quot;%ALLUSERSPROFILE%\osmosis.bat&quot;</code></pre>
<p>unchanged. (also commented this out but it didn't do anything)</p>
<p>The errors I encountered are</p>
<pre><code>C:\Users\PAUL&gt;&quot;C:\osmosis\bin\osmosis&quot;
**** BATCH RECURSION exceed stacks limit ******
Recursion counts=317 Stack Usage=90 percent
****** BATCH PROCESSING IS ABORTED ******</code></pre>
<p>or</p>
<pre><code>C:\Users\PAUL&gt;&quot;C:\osmosis\bin\osmosis.bat&quot;
**** BATCH RECURSION exceed stacks limit ******
Recursion counts=317 Stack Usage=90 percent
****** BATCH PROCESSING IS ABORTED ******</code></pre>
<p>6) I typed in JAVA at the command prompt screen and it worked fine</p>
<p>7) Created another .bat file in C:\Users\PAUL\osmosis.bat which contain the line "C:\osmosis\bin\osmosis.bat" I also tried without the .bat extension as well i.e. "C:\osmosis\bin\osmosis"</p>
<p>8) However when I typed in osmosis at the command prompt it giving me this error</p>
<pre><code>C:\Users\PAUL&gt;&quot;C:\osmosis\bin\osmosis&quot;
Files was unexpected at this time</code></pre>
<p>or</p>
<pre><code>C:\Users\PAUL&gt;&quot;C:\osmosis\bin\osmosis.bat&quot;
Files was unexpected at this time</code></pre>
<p>I tried really hard to get osmosis to work but all attempts proved futile, so I really appreciate if any experts can show me the steps to get this working on Win 10 64-bit.</p>
<p>Best,</p>
<p>Paul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '19, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/5e0c868e7cd94af93129304d00693230?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Pi&#39;s gravatar image" />
<p><span>Paul Pi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Pi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '19, 09:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68416" class="comments-container">
<span id="68417"></span>
<div id="comment-68417" class="comment">
<div id="post-68417-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm not really experienced with Windows and .bat files but as far as I remember you should not use the same name for the binary and the .bat file. Otherwise when trying to call the binary (i.e. <code>osmosis</code>) Windows executes the .bat file instead (i.e. <code>osmosis.bat</code>), leading to a recursion and/or weird errors. Try renaming your <code>osmosis.bat</code>.</p>
</div>
<div id="comment-68417-info" class="comment-info">
<span class="comment-age">(19 Mar '19, 09:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68418"></span>
<div id="comment-68418" class="comment">
<div id="post-68418-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd suggest in the first instance adding ECHO statements for JAVACMD, MYAPP_HOME &amp; a copy of the final EXEC statement. Osmosis in my experience has always been fiddly to get working in Windows and mostly because of these environment variables.</p>
</div>
<div id="comment-68418-info" class="comment-info">
<span class="comment-age">(19 Mar '19, 10:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68416-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="68446"></span>

<div id="answer-container-68446" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68446-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at my osmosis.bat, JAVACMD should point to your java executable. If you have Java set up in your "Path" environment variable, then JAVACMD=java is all you need. Otherwise, JAVACMD should point to wherever the Java executable resides.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '19, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-68446" class="comments-container">
<span id="68451"></span>
<div id="comment-68451" class="comment">
<div id="post-68451-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just checked, and my .bat file is exactly the same as the one available when you download the program (ie. I haven't modified mine at all).</p>
<p>As for my variables, I don't have a JAVA_HOME one. My PATH system variable contains the following for Java (I have JRE installed with default settings): C:\Program Files (x86)\Common Files\Oracle\Java\javapath</p>
</div>
<div id="comment-68451-info" class="comment-info">
<span class="comment-age">(20 Mar '19, 23:33)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="68452"></span>
<div id="comment-68452" class="comment">
<div id="post-68452-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Tried to modified my earlier comments to reflect the latest update, yes I finally got this to work with the JAVA_HOME environment variable set-up shown above, finger cross no more issues comes up when I have more interaction with osmosis, but thank you <a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> for enlightened me that this was the issue.</p>
<p>I also just tried the latest version and it worked too, so happy days!</p>
<p>Best regards,</p>
<p>p</p>
</div>
<div id="comment-68452-info" class="comment-info">
<span class="comment-age">(20 Mar '19, 23:39)</span> <span class="comment-user userinfo">Paul Pi</span>
</div>
</div>
</div>
<div id="comment-tools-68446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68446-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68431"></span>

<div id="answer-container-68431" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68431-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@scai</a></a> &amp; <a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a></a>,</p>
<p>Thank you for your kind responses, I have renamed the osmosis.bat files in C:\Users\PAUL and leave the "real" osmosis.bat filename in C:\osmosis\bin\ unchanged. However it now giving me a new error message relates to Java</p>
<p>Files\Java\jre1.8.0_201\""=="" was unexpected at this time.</p>
<p>I checked both the osmosis and osmosis.bat files in C:\osmosis\bin\</p>
<p>and it is pointing to the right Java directory</p>
<p>IF "%JAVACMD%"=="" set JAVACMD="C:\Program Files (x86)\Java\jre1.8.0_201\bin"</p>
<p>I even tried the 64-bit version as well to no avail.</p>
<p>Update 1: I also attempted to modify the system environmental variables and path to reflect the new JRE installation location (from C:\Program Files\Java to C:\Java) because of the space in between "Program Files" plus modify the osmosis.bat file to point to the new Java location</p>
<p>IF "%JAVACMD%"=="" set JAVACMD=C:\Java\bin</p>
<p>again it didn't worked as hoped. The error encountered was</p>
<p>'"C:\Java\bin"' is not recognized as an internal or external command operable program or batch file</p>
<p>Update 2: Downloaded the previous version of osmosis and tried all the above, still doesn't work, is there anyone who have a fix for Windows? I don't believe I'm the only Window user who have this problem.</p>
<p>Best,</p>
<p>p</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '19, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/5e0c868e7cd94af93129304d00693230?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Pi&#39;s gravatar image" />
<p><span>Paul Pi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Pi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Mar '19, 22:32</strong> </span></p>
</div>
</div>
<div id="comments-container-68431" class="comments-container">
<span id="68450"></span>
<div id="comment-68450" class="comment">
<div id="post-68450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/8189/alester"></a><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a>, after more fiddling with the environment variables I got it to work for osmosis older version 0.46, haven't tried the latest version yet.</p>
<p>For the benefits of anyone else who have the same problem like me the last 3 days this is how I configure my Java environment.</p>
<p>Variable Name : JAVA_HOME Variable Value : C:\Program Files\Java\jdk-11.0.2</p>
<p>Variable Name : PATH Variable Value : %JAVA_HOME%\bin</p>
</div>
<div id="comment-68450-info" class="comment-info">
<span class="comment-age">(20 Mar '19, 22:31)</span> <span class="comment-user userinfo">Paul Pi</span>
</div>
</div>
</div>
<div id="comment-tools-68431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68431-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74811"></span>

<div id="answer-container-74811" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74811-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I also had problems. After I removed "" from JAVACMD="C:\Program Files (x86)\Java\jre1.8.0_201\bin" it worked. Maybe it is some region/language specific problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/9569fc92806792fed76b1fe7db3687b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trnovstyle&#39;s gravatar image" />
<p><span>trnovstyle</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trnovstyle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74811" class="comments-container">
&#10;</div>
<div id="comment-tools-74811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74811-form-container" class="comment-form-container">
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

