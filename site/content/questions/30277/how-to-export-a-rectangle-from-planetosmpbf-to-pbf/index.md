+++
type = "question"
title = "How to export a rectangle from planet.osm.pbf to pbf"
description = '''Hi! I&#x27;m having a goal to be able to use osm data offline, if I travel somewhere - I just get a small rectangle part (a city - about 4 square degrees of latitude/longitude) from a big planet.osm.pbf and load it in some program (for now I came to Maperitive, but not sure if it would work). I wonder ho...'''
date = "2014-01-28T19:45:00Z"
lastmod = "2014-01-29T17:03:00Z"
weight = 30277
keywords = [ "export" ]
aliases = [ "/questions/30277" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to export a rectangle from planet.osm.pbf to pbf](/questions/30277/how-to-export-a-rectangle-from-planetosmpbf-to-pbf)

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
<span id="post-30277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30277-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm having a goal to be able to use osm data offline, if I travel somewhere - I just get a small rectangle part (a city - about 4 square degrees of latitude/longitude) from a big planet.osm.pbf and load it in some program (for now I came to Maperitive, but not sure if it would work). I wonder how fast such map would render on an average notebook, how long would it take to export a city from planet file, what should I write in osmosis console and if maybe there are better solutions.</p>
<p>I'm asking about exact code to write, because I've already tried<br />
bin\osmosis.bat --read-pbf file=planet-140122.osm.pbf enableDateParsing=no --log-progress interval=30 --bounding-box top=60.5700 left=29.1900 bottom 58.5700 right=31.1900 --write-pbf file=sanktpeterburg.osm.pbf</p>
<p>and got errors. Thanks for help in advance.</p>
<pre><code>F:\osmosis&gt;bin\osmosis.bat -v --read-pbf file=planet-140122.osm.pbf enableDatePa
rsing=no --buffer --log-progress interval=30 --bounding-box clipIncompleteEntiti
es=true top=60.5700 left=29.1900 bottom=58.5700 right=31.1900 --write-pbf file=s
anktpeterburg2.osm.pbf
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.43.1
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.TaskRegistrar loadJPFPlug
ins
FINE: Searching for JPF plugins.
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.TaskRegistrar loadJPFPlug
ins
FINE: Registering the core plugin.
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.TaskRegistrar loadJPFPlug
ins
FINE: Registering the extension plugins.
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.pipeline.common.Pipeline
prepare
FINE: Building tasks.
 эт 29, 2014 1:12:31 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Argument enableDateParsi
ng for task 1-read-pbf was not recognised.
        at org.openstreetmap.osmosis.core.pipeline.common.TaskManagerFactory.cre
ateTaskManager(TaskManagerFactory.java:64)
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.buildTasks(Pi
peline.java:50)
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipel
ine.java:112)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun
cher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav
a:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La
uncher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:
352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>Added:</p>
<pre><code>F:\osmosis&gt;bin\osmosis.bat --read-pbf file=planet-140122.osm.pbf --log-progress
interval=30 --bounding-box clipIncompleteEntities=true top=60.5700 left=29.1900
bottom=58.5700 right=31.1900 --write-pbf file=sanktpeterburg2.osm.pbf
 эт 29, 2014 1:06:08 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.43.1
 эт 29, 2014 1:06:09 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
 эт 29, 2014 1:06:09 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
 эт 29, 2014 1:06:09 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
java.util.zip.DataFormatException: incorrect data check
        at java.util.zip.Inflater.inflateBytes(Native Method)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockPosition.parseData(
FileBlockPosition.java:57)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockHead.readContents(F
ileBlockHead.java:95)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.
java:135)
        at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(Blo
ckInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
        at java.lang.Thread.run(Unknown Source)
 эт 29, 2014 1:06:10 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTas
kManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
java.lang.Error: java.util.zip.DataFormatException: incorrect data check
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockPosition.parseData(
FileBlockPosition.java:60)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockHead.readContents(F
ileBlockHead.java:95)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.
java:135)
        at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(Blo
ckInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
        at java.lang.Thread.run(Unknown Source)
Caused by: java.util.zip.DataFormatException: incorrect data check
        at java.util.zip.Inflater.inflateBytes(Native Method)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockPosition.parseData(
FileBlockPosition.java:57)
        ... 5 more
&#10; эт 29, 2014 1:06:10 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed
.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple
tion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun
cher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav
a:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La
uncher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:
352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '14, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/5fc3bac4d90cde97ca55f8bcb5536bb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kuzma1&#39;s gravatar image" />
<p><span>kuzma1</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kuzma1 has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '14, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-30277" class="comments-container">
<span id="30278"></span>
<div id="comment-30278" class="comment">
<div id="post-30278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I might be tempted to start with an extract of <a href="http://download.geofabrik.de/europe/russia-european-part.html">the European part of Russia</a> rather than the whole planet.</p>
</div>
<div id="comment-30278-info" class="comment-info">
<span class="comment-age">(28 Jan '14, 20:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30279"></span>
<div id="comment-30279" class="comment">
<div id="post-30279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, what version of Osmosis are you running (i.e. how old is it) and what errors do you actually get?</p>
</div>
<div id="comment-30279-info" class="comment-info">
<span class="comment-age">(28 Jan '14, 20:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30280"></span>
<div id="comment-30280" class="comment">
<div id="post-30280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I make such exports myself from a planet.pbf? Can you just provide me with WORKING code? I'm using the latest versions of all programs.</p>
</div>
<div id="comment-30280-info" class="comment-info">
<span class="comment-age">(28 Jan '14, 20:23)</span> <span class="comment-user userinfo">kuzma1</span>
</div>
</div>
<span id="30281"></span>
<div id="comment-30281" class="comment">
<div id="post-30281-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The last time I ran osmosis I did:</p>
<pre><code>osmosis  --read-pbf great-britain-latest.osm.pbf  --bounding-box top=54.623 left=-4.807 bottom=51.737 right=0.906 --write-pbf cut.pbf</code></pre>
<p>and it produced just what I wanted. That was on Linux rather than Windows, but should be otherwise the same. I notice that your example has "bottom 58.5700" - did you really miss the "=" sign out?</p>
</div>
<div id="comment-30281-info" class="comment-info">
<span class="comment-age">(28 Jan '14, 20:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30277-form-container" class="comment-form-container">
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

<span id="30295"></span>

<div id="answer-container-30295" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30295-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kuzma1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error</p>
<pre><code>java.util.zip.DataFormatException: incorrect data check</code></pre>
<p>suggests that there's a problem with the pbf file that you're trying to read. If you run md5sum on it (you'll need to download a version of that for Windows) does it match the values in the .md5 file on <a href="http://planet.openstreetmap.org/pbf/">http://planet.openstreetmap.org/pbf/</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '14, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-30295" class="comments-container">
<span id="30298"></span>
<div id="comment-30298" class="comment">
<div id="post-30298-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah, that was a problem. Now it executes, quite slow (the file sanktpetersburg2.osm.pbf grows about 100kbytes in minute - in console it tells ~95000 objects per second). Is it normal for 4gb ram on ultrabook? I already changed xmx in java settings to three quarters of my ram.</p>
</div>
<div id="comment-30298-info" class="comment-info">
<span class="comment-age">(29 Jan '14, 13:26)</span> <span class="comment-user userinfo">kuzma1</span>
</div>
</div>
<span id="30301"></span>
<div id="comment-30301" class="comment">
<div id="post-30301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright, it's nice, it took a little more than an hour. Map renders quite slow, guess it would be better to use other map formats, but I guess my question resolved, how can I accept an answer?</p>
</div>
<div id="comment-30301-info" class="comment-info">
<span class="comment-age">(29 Jan '14, 15:56)</span> <span class="comment-user userinfo">kuzma1</span>
</div>
</div>
<span id="30302"></span>
<div id="comment-30302" class="comment">
<div id="post-30302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've changed the "comment" suggesting that there might be a problem with the data to an "answer" - you should be able to accept that now.</p>
</div>
<div id="comment-30302-info" class="comment-info">
<span class="comment-age">(29 Jan '14, 16:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30307"></span>
<div id="comment-30307" class="comment">
<div id="post-30307-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for help</p>
</div>
<div id="comment-30307-info" class="comment-info">
<span class="comment-age">(29 Jan '14, 17:03)</span> <span class="comment-user userinfo">kuzma1</span>
</div>
</div>
</div>
<div id="comment-tools-30295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30295-form-container" class="comment-form-container">
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

