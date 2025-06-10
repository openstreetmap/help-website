+++
type = "question"
title = "Problem running osmosis w/mapsforge on mac"
description = '''Hello, I&#x27;m trying to run osmosis(with mapsforge writer) on Yosemite, but I have encountered a problem. I followed the tutorials, but when I try to run the command I get this:  GRAVE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load plugin class ({&#92;rtf1&#92;ansi&#92;a...'''
date = "2015-08-18T15:09:00Z"
lastmod = "2015-08-21T07:40:00Z"
weight = 44805
keywords = [ "mac", "mapsforge", "classnotfound", "osmosis" ]
aliases = [ "/questions/44805" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem running osmosis w/mapsforge on mac](/questions/44805/problem-running-osmosis-wmapsforge-on-mac)

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
<span id="post-44805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44805-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm trying to run osmosis(with mapsforge writer) on Yosemite, but I have encountered a problem. I followed the tutorials, but when I try to run the command I get this:</p>
<pre><code>    GRAVE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load plugin class ({\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170).
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadPluginClass(TaskRegistrar.java:334)
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadPlugin(TaskRegistrar.java:313)
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadBuiltInPlugins(TaskRegistrar.java:123)
    at org.openstreetmap.osmosis.core.TaskRegistrar.initialize(TaskRegistrar.java:80)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:81)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:497)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:47)
Caused by: java.lang.ClassNotFoundException: {\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
    at org.codehaus.plexus.classworlds.strategy.SelfFirstStrategy.loadClass(SelfFirstStrategy.java:50)
    at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClass(ClassRealm.java:244)
    at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClass(ClassRealm.java:230)
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadPluginClass(TaskRegistrar.java:332)
    ... 14 more</code></pre>
<p>I have no clue what this cocoasubrtf class is, and I could not find any help by googling (quite extensively). Any Ideas?</p>
<p>UPDATE: I have tried running osmosis on Windows as well, and I get the exact same error.</p>
<p>UPDATE 2: I have been suggested to use osmosis 0.44 as a fresh install, and that somehow worked :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-mapsforge" rel="tag" title="see questions tagged &#39;mapsforge&#39;">mapsforge</span> <span class="post-tag tag-link-classnotfound" rel="tag" title="see questions tagged &#39;classnotfound&#39;">classnotfound</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '15, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/3d8c24fd0f8a993692b7bff7580c7e41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZappyKeyboard&#39;s gravatar image" />
<p><span>ZappyKeyboard</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZappyKeyboard has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '15, 19:45</strong> </span></p>
</div>
</div>
<div id="comments-container-44805" class="comments-container">
<span id="44821"></span>
<div id="comment-44821" class="comment">
<div id="post-44821-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Try asking at the osmosis-dev mailing list although it seems to be pretty low traffic.</p>
</div>
<div id="comment-44821-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 10:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44822"></span>
<div id="comment-44822" class="comment">
<div id="post-44822-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd also add details of what tutorials you followed and what the output of "java -version" from the command line is.</p>
</div>
<div id="comment-44822-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 11:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="44823"></span>
<div id="comment-44823" class="comment">
<div id="post-44823-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I followed the quick install guide on <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_%28Windows%29,">http://wiki.openstreetmap.org/wiki/Osmosis/Quick_Install_%28Windows%29,</a> but I should mention that I had to tinker a bit before making it work: at first it didnt see the jre path, then I had to modify the classworlds pointer in the osmosis file, because it was wrong. I have both java 8 and 7 on my Windows PC.</p>
<p>For mac, a first I downloaded the zipfile and tried running it from there (I used the guide on the wiki). Then I tried downloading osmosis with homebrew. On mac I only have java 8 (for work). Should I try to download java 7 and see if that works?</p>
<p>terminal output on mac: java version "1.8.0_45" Java(TM) SE Runtime Environment (build 1.8.0_45-b14) Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)</p>
<p>It's especially odd to me that I get the same error on both machines.</p>
</div>
<div id="comment-44823-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 11:37)</span> <span class="comment-user userinfo">ZappyKeyboard</span>
</div>
</div>
<span id="44828"></span>
<div id="comment-44828" class="comment">
<div id="post-44828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... maybe you can also ask (or do an intensive search for "osmosis" there before) on the mapsforge mailinglist,</p>
<p>see <a href="https://groups.google.com/forum/#!forum/mapsforge-dev">https://groups.google.com/forum/#!forum/mapsforge-dev</a></p>
</div>
<div id="comment-44828-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 16:41)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="44856"></span>
<div id="comment-44856" class="comment">
<div id="post-44856-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It looks like you somehow managed to get RTF encoded text into a context where plain text was expected (all that "{\rtf1\ansi..." stuff smells of RTF). Editing some source or config file with TextEdit.app and accidentally saving as RTF, perhaps?</p>
</div>
<div id="comment-44856-info" class="comment-info">
<span class="comment-age">(21 Aug '15, 07:40)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
</div>
<div id="comment-tools-44805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44805-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

