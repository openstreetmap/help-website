+++
type = "question"
title = "Can&#x27;t get osmosis to read a pbf"
description = '''I try to read a recent planet and / or osmborder extract via Osmosis. The prebuild package, the ubuntu package as well as a self-compiled package all crash:  $ osmosis --read-pbf /media/self/planet-170130.osm.pbf  Feb 06, 2017 9:19:41 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Versi...'''
date = "2017-02-06T20:24:00Z"
lastmod = "2017-02-06T20:32:00Z"
weight = 54521
keywords = [ "debugging", "osmosis" ]
aliases = [ "/questions/54521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get osmosis to read a pbf](/questions/54521/cant-get-osmosis-to-read-a-pbf)

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
<span id="post-54521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to read a recent planet and / or osmborder extract via Osmosis. The prebuild package, the ubuntu package as well as a self-compiled package all crash:</p>
<pre><code>    $ osmosis --read-pbf /media/self/planet-170130.osm.pbf 
Feb 06, 2017 9:19:41 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.44.1
Feb 06, 2017 9:19:42 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load plugin class (uk.co.randomjunk.osmosis.transform.TransformPlugin).
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadPluginClass(TaskRegistrar.java:334)
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadPlugin(TaskRegistrar.java:313)
    at org.openstreetmap.osmosis.core.TaskRegistrar.initialize(TaskRegistrar.java:84)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:81)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:498)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:328)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:408)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:351)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:31)
Caused by: java.lang.ClassNotFoundException: uk.co.randomjunk.osmosis.transform.TransformPlugin
    at org.codehaus.plexus.classworlds.strategy.SelfFirstStrategy.loadClass(SelfFirstStrategy.java:53)
    at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClass(ClassRealm.java:208)
    at org.codehaus.plexus.classworlds.realm.ClassRealm.loadClass(ClassRealm.java:202)
    at org.openstreetmap.osmosis.core.TaskRegistrar.loadPluginClass(TaskRegistrar.java:332)
    ... 13 more</code></pre>
<p>It is also not working with the version here:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/DE:Osmosis#Verwenden_von_.pbf_Dateien">http://wiki.openstreetmap.org/wiki/DE:Osmosis#Verwenden_von_.pbf_Dateien</a></p>
<p>Is it just broken or am I doing something wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-debugging" rel="tag" title="see questions tagged &#39;debugging&#39;">debugging</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '17, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54521" class="comments-container">
&#10;</div>
<div id="comment-tools-54521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54521-form-container" class="comment-form-container">
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

<span id="54523"></span>

<div id="answer-container-54523" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was having a</p>
<pre><code>OSMOSIS_OPTIONS=&quot;-p uk.co.randomjunk.osmosis.transform.TransformPlugin&quot;</code></pre>
<p>in <code>~/.osmosis</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '17, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54523" class="comments-container">
&#10;</div>
<div id="comment-tools-54523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54523-form-container" class="comment-form-container">
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

