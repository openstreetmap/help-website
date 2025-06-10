+++
type = "question"
title = "osmosis permanent breakdown: &quot;pipes have not been terminated with appropriate output sinks&quot;"
description = '''I terminated osmosis several times during the run by Ctrl+c, and now it cannot do enen simplest tasks, giving an error: &quot;The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks.&quot; $ osmosis --rx file=&quot;my.xml&quot; 14.05.2016 14:24:29 org.openstreetmap.osmosi...'''
date = "2016-05-14T12:29:00Z"
lastmod = "2016-05-18T10:08:00Z"
weight = 49691
keywords = [ "osmosis" ]
aliases = [ "/questions/49691" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmosis permanent breakdown: "pipes have not been terminated with appropriate output sinks"](/questions/49691/osmosis-permanent-breakdown-pipes-have-not-been-terminated-with-appropriate-output-sinks)

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
<span id="post-49691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49691-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I terminated <code>osmosis</code> several times during the run by <code>Ctrl+c</code>, and now it cannot do enen simplest tasks, giving an error: <strong>"The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks."</strong></p>
<pre><code>$ osmosis --rx file=&quot;my.xml&quot;
14.05.2016 14:24:29 org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.44.1
14.05.2016 14:24:29 org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
14.05.2016 14:24:29 org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks.
at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.connectTasks(Pipeline.java:94)
at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipeline.java:116)
at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86)
at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>I'm on OSX 10.8, rebooting or even</p>
<pre><code> brew uninstall osmosis
 brew install osmosis</code></pre>
<p>don't help. How can I fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '16, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6cf5f23ff9e96e3379c1b0b2634e99da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pantlmn&#39;s gravatar image" />
<p><span>Pantlmn</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pantlmn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49691" class="comments-container">
&#10;</div>
<div id="comment-tools-49691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49691-form-container" class="comment-form-container">
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

<span id="49692"></span>

<div id="answer-container-49692" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pantlmn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The command you are using will yield this error message on any system. The <code>--rx</code> opens a pipe and puts data in it. Osmosis expects you to specify where this data should go, but you don't. Add <code>--write-null</code> to your command line (which means "discard the data") and it will stop complaining. Of course, to make Osmosis do something useful, you'll have to specify something else than <code>--write-null</code>...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '16, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49692" class="comments-container">
<span id="49693"></span>
<div id="comment-49693" class="comment">
<div id="post-49693-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, that's my fault. <code>--wx file="NNN"</code> fixes that.</p>
</div>
<div id="comment-49693-info" class="comment-info">
<span class="comment-age">(14 May '16, 13:18)</span> <span class="comment-user userinfo">Pantlmn</span>
</div>
</div>
<span id="49726"></span>
<div id="comment-49726" class="comment">
<div id="post-49726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For further reference, see the documentation: <a href="http://wiki.openstreetmap.org/w/index.php?title=Osmosis/Detailed_Usage">http://wiki.openstreetmap.org/w/index.php?title=Osmosis/Detailed_Usage</a></p>
</div>
<div id="comment-49726-info" class="comment-info">
<span class="comment-age">(18 May '16, 10:08)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-49692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49692-form-container" class="comment-form-container">
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

