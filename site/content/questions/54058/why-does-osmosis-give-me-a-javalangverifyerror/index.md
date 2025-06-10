+++
type = "question"
title = "Why does Osmosis give me a java.lang.VerifyError"
description = '''Running the most basic of Osmosis commands to extract data from a PBF file gives me a java.lang.VerifyError. Googling suggests this may be due to having the wrong libraries in the CLASSPATH. Where do I start to try abnd fix this? Stacktrace below: $ osmosis --read-pbf file=buckinghamshire-latest.osm...'''
date = "2017-01-15T17:12:00Z"
lastmod = "2017-01-15T23:28:00Z"
weight = 54058
keywords = [ "osmosis" ]
aliases = [ "/questions/54058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does Osmosis give me a java.lang.VerifyError](/questions/54058/why-does-osmosis-give-me-a-javalangverifyerror)

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
<span id="post-54058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54058-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Running the most basic of Osmosis commands to extract data from a PBF file gives me a java.lang.VerifyError. Googling suggests this may be due to having the wrong libraries in the CLASSPATH. Where do I start to try abnd fix this?</p>
<p>Stacktrace below:</p>
<pre><code>$ osmosis --read-pbf file=buckinghamshire-latest.osm.pbf --write-null
Jan 15, 2017 5:08:20 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.45
Jan 15, 2017 5:08:21 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jan 15, 2017 5:08:21 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jan 15, 2017 5:08:21 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Jan 15, 2017 5:08:21 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
java.lang.VerifyError: class org.openstreetmap.osmosis.osmbinary.Fileformat$BlobHeader overrides final method isInitialized.()Z
        at java.lang.ClassLoader.defineClass1(Native Method)
        at java.lang.ClassLoader.defineClass(ClassLoader.java:763)
        at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
        at java.net.URLClassLoader.defineClass(URLClassLoader.java:467)
        at java.net.URLClassLoader.access$100(URLClassLoader.java:73)
        at java.net.URLClassLoader$1.run(URLClassLoader.java:368)
        at java.net.URLClassLoader$1.run(URLClassLoader.java:362)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(URLClassLoader.java:361)
        at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClassFromSelf(ClassRealm.java:332)
        at org.codehaus.plexus.classworlds.strategy.SelfFirstStrategy.loadClass(SelfFirstStrategy.java:43)
        at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClass(ClassRealm.java:208)
        at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClass(ClassRealm.java:202)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockHead.readHead(FileBlockHead.java:57)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.java:130)
        at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
        at java.lang.Thread.run(Thread.java:745)
&#10;Jan 15, 2017 5:08:21 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:328)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:408)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:351)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:31)</code></pre>
<p>I'm using Java 1.8.0_111 on an <a href="http://www.osboxes.org/ubuntu-16-10-yakkety-yak-released-for-virtualbox-vmware/">OSBoxes Ubuntu 16.10 VM</a> and installed using <code>apt-get</code>.</p>
<pre><code>$ java -version
openjdk version &quot;1.8.0_111&quot;
OpenJDK Runtime Environment (build 1.8.0_111-8u111-b14-2ubuntu0.16.10.2-b14)
OpenJDK 64-Bit Server VM (build 25.111-b14, mixed mode)
&#10;$ uname -a
Linux osboxes 4.8.0-26-generic #28-Ubuntu SMP Tue Oct 18 14:39:52 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
&#10;$ dpkg -l osmosis
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name              Version       Architecture  Description
+++-=================-=============-=============-=======================================
ii  osmosis           0.45-2        all           Command line OpenStreetMap data process</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '17, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/9111c5a87d559757e4b10ea2a963e6a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mat_B&#39;s gravatar image" />
<p><span>Mat_B</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mat_B has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '17, 19:59</strong> </span></p>
</div>
</div>
<div id="comments-container-54058" class="comments-container">
<span id="54061"></span>
<div id="comment-54061" class="comment">
<div id="post-54061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you build from source and which JRE and version do you have installed?</p>
</div>
<div id="comment-54061-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 19:53)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="54062"></span>
<div id="comment-54062" class="comment">
<div id="post-54062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Details added above. Installed from package JRE 1.8</p>
</div>
<div id="comment-54062-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 19:59)</span> <span class="comment-user userinfo">Mat_B</span>
</div>
</div>
<span id="54065"></span>
<div id="comment-54065" class="comment">
<div id="post-54065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As just another data point, that version of Java works just find for me on 16.04 (locally installed off a server CD). Same JDK, older osmosis:</p>
<p>java -version</p>
<p>openjdk version "1.8.0_111" OpenJDK Runtime Environment (build 1.8.0_111-8u111-b14-2ubuntu0.16.04.2-b14) OpenJDK 64-Bit Server VM (build 25.111-b14, mixed mode)</p>
<p>osmosis --read-pbf file=derbyshire-latest.osm.pbf --write-null (snip - no errors) Jan 15, 2017 9:39:41 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Total execution time: 6654 milliseconds.</p>
<p>dpkg -l osmosis</p>
<p>Desired=Unknown/Install/Remove/Purge/Hold | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad) ||/ Name Version Architecture Description +++-==============-============-============-================================= ii osmosis 0.44.1-4 all Command line OpenStreetMap data p</p>
</div>
<div id="comment-54065-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 21:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54058-form-container" class="comment-form-container">
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

<span id="54066"></span>

<div id="answer-container-54066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note this is just me guessing. I don't believe that osmosis has a dependency outside of the standard Java classes so this might be a subtle incompatibility between oracles jdk and openjdk, I would suggest compiling from source.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '17, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54066" class="comments-container">
&#10;</div>
<div id="comment-tools-54066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54066-form-container" class="comment-form-container">
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

