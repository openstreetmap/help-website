+++
type = "question"
title = "[closed] Osmosis unit tests fail (latest git version, Feb. 9, 2012)"
description = '''I cloned todays current git repository, but the build stops somewhere because of a failed unit test. The build results in a jar file in the dist/ directory, but that doesn&#x27;t run either. Here is the last bit of output from running &quot;ant all&quot;: checkstyle: [cs:checkstyle] Running Checkstyle 5.4 on 75 fi...'''
date = "2012-02-09T11:01:00Z"
lastmod = "2012-02-09T11:44:00Z"
weight = 10508
keywords = [ "building", "bug", "osmosis" ]
aliases = [ "/questions/10508" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Osmosis unit tests fail (latest git version, Feb. 9, 2012)](/questions/10508/osmosis-unit-tests-fail-latest-git-version-feb-9-2012)

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
<span id="post-10508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10508-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I cloned todays current git repository, but the build stops somewhere because of a failed unit test. The build results in a jar file in the dist/ directory, but that doesn't run either.</p>
<p>Here is the last bit of output from running "ant all":</p>
<pre><code>checkstyle: [cs:checkstyle] Running Checkstyle 5.4 on 75 files
&#10;build_test:
&#10;test:
    [junit] Running org.openstreetmap.osmosis.apidb.v0_6.ApiDbTest
    [junit] Tests run: 5, Failures: 0, Errors: 5, Time elapsed: 0.765 sec
    [junit] Test org.openstreetmap.osmosis.apidb.v0_6.ApiDbTest FAILED
    [junit] Running org.openstreetmap.osmosis.apidb.v0_6.ApidbFileReplicatorTest
    [junit] Tests run: 1, Failures: 0, Errors: 1, Time elapsed: 0.054 sec
    [junit] Test org.openstreetmap.osmosis.apidb.v0_6.ApidbFileReplicatorTest FAILED
    [junit] Running org.openstreetmap.osmosis.apidb.v0_6.impl.ChangesetManagerTest
    [junit] Tests run: 1, Failures: 0, Errors: 1, Time elapsed: 0.075 sec
    [junit] Test org.openstreetmap.osmosis.apidb.v0_6.impl.ChangesetManagerTest FAILED
    [junit] Running org.openstreetmap.osmosis.apidb.v0_6.impl.ReplicationSequenceFormatterTest
    [junit] Tests run: 4, Failures: 0, Errors: 0, Time elapsed: 0.028 sec
    [junit] Running org.openstreetmap.osmosis.apidb.v0_6.impl.ReplicatorTest
    [junit] Tests run: 5, Failures: 0, Errors: 0, Time elapsed: 0.068 sec
    [junit] Running org.openstreetmap.osmosis.apidb.v0_6.impl.TransactionSnapshotTest
    [junit] Tests run: 1, Failures: 0, Errors: 0, Time elapsed: 0.003 sec
&#10;BUILD FAILED /home/mok/osm/sources/osmosis/build.xml:30: The following error occurred while executing this line: /home/mok/osm/sources/osmosis/build-support/script/build-java.xml:128: O
ne or more junit tests failed.</code></pre>
<p>Here is the output when I try to run the osomosis application:</p>
<pre><code>$ osmosis -h
Exception in thread &quot;main&quot; java.lang.NoClassDefFoundError: org/codehaus/classworlds/Launcher
Caused by: java.lang.ClassNotFoundException: org.codehaus.classworlds.Launcher
        at java.net.URLClassLoader$1.run(URLClassLoader.java:217)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(URLClassLoader.java:205)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:321)
        at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:294)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:266)
Could not find the main class: org.codehaus.classworlds.Launcher. Program will exit.</code></pre>
<p>I guess the question is: what's wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '12, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/2a833321a7baa594456b3a269dee33da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mok0&#39;s gravatar image" />
<p><span>mok0</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mok0 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>09 Feb '12, 11:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-10508" class="comments-container">
&#10;</div>
<div id="comment-tools-10508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10508-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Unsuitable question for help forum." by Frederik Ramm 09 Feb '12, 11:45

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10509"></span>

<div id="answer-container-10509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10509-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This help forum is a place where we try to find answers of a general relevance, i.e. ideally answers that will be useful to other people than just you, and that will be valid over a longer period of time.</p>
<p>On the <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis page in our Wiki</a>, under "getting help and reporting bugs", it says:</p>
<pre><code>The best place to get answers to questions on osmosis usage is the osmosis dev mailing list.
&#10;http://lists.openstreetmap.org/listinfo/osmosis-dev
&#10;Please discuss potential bugs on the dev mailing list before creating new tickets. If you&#39;re confident you have discovered a bug, it can be logged in the OSM trac system against the &quot;osmosis&quot; component:
&#10;http://trac.openstreetmap.org/query?component=osmosis</code></pre>
<p>Please follow that advice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '12, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10509" class="comments-container">
&#10;</div>
<div id="comment-tools-10509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10509-form-container" class="comment-form-container">
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

