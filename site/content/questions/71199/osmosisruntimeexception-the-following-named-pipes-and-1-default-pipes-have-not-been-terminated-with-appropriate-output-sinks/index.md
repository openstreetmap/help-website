+++
type = "question"
title = "OsmosisRuntimeException: The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks."
description = '''Hi guys, I just started using osmosis and I used following instructions: But I immediatly get following error message when running the command (even with different pbf files). Can anyone help? C:&#92;Users&#92;mt5285&#92;Downloads&#92;Sample&amp;gt;osmosis --read-pbf file=&quot;sample_osmosis.osm.pbf&quot; Okt 16, 2019 1:33:44 P...'''
date = "2019-10-16T12:47:00Z"
lastmod = "2019-10-16T14:53:00Z"
weight = 71199
keywords = [ "osmosis", "error" ]
aliases = [ "/questions/71199" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OsmosisRuntimeException: The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks.](/questions/71199/osmosisruntimeexception-the-following-named-pipes-and-1-default-pipes-have-not-been-terminated-with-appropriate-output-sinks)

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
<span id="post-71199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71199-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I just started using osmosis and I used following instructions:</p>
<p>But I immediatly get following error message when running the command (even with different pbf files).</p>
<p>Can anyone help?</p>
<pre><code>C:\Users\mt5285\Downloads\Sample&gt;osmosis --read-pbf file=&quot;sample_osmosis.osm.pbf&quot;
Okt 16, 2019 1:33:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Osmosis Version 0.47
Okt 16, 2019 1:33:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Preparing pipeline.
Okt 16, 2019 1:33:44 PM org.openstreetmap.osmosis.core.Osmosis main
SCHWERWIEGEND: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.connectTasks(Pipeline.java:96)
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipeline.java:116)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '19, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1972db18ec903b5b890efb3c90c1be2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ulicious&#39;s gravatar image" />
<p><span>ulicious</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ulicious has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71199" class="comments-container">
&#10;</div>
<div id="comment-tools-71199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71199-form-container" class="comment-form-container">
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

<span id="71200"></span>

<div id="answer-container-71200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71200-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Link to instructions missing in your question.</p>
<p>The error message means that you have an input file but you haven't specified what to do with the data once it has been read.</p>
<p>Adding <code>--write-null</code> to the end of the command line would make it valid (it just throws away the data) but this is likely not what you want, so you'll have to tell osmosis what it is supposed to do with the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '19, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71200" class="comments-container">
&#10;</div>
<div id="comment-tools-71200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71200-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71201"></span>

<div id="answer-container-71201" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71201-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Frederik,</p>
<p>sorry for the missing link: <a href="https://learnosm.org/en/osm-data/osmosis/">https://learnosm.org/en/osm-data/osmosis/</a></p>
<p>The full command is following ( \ is used to change the line). I still get an error message but this time from line 7: completeRelations (saying its written incorrectly or can't be found)</p>
<p><img src="/upfiles/Unbenannt.PNG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '19, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/1972db18ec903b5b890efb3c90c1be2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ulicious&#39;s gravatar image" />
<p><span>ulicious</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ulicious has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71201" class="comments-container">
<span id="71202"></span>
<div id="comment-71202" class="comment">
<div id="post-71202-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Strange. Can you post the exact error message? Generally speaking, if you are only interested in Germany, why not use a Germany file to start with (<a href="http://download.geofabrik.de/europe/germany-150101.osm.pbf">http://download.geofabrik.de/europe/germany-150101.osm.pbf</a> if you're desperate for an antique one) that will be much faster. Also, unless you really need power lines that lead out of the country, you can just drop the "completeRelations=yes" and it should still work.</p>
</div>
<div id="comment-71202-info" class="comment-info">
<span class="comment-age">(16 Oct '19, 13:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="71204"></span>
<div id="comment-71204" class="comment">
<div id="post-71204-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Frederik, it's now finally running. It seems it was more my inexperience in cmd/osmosis than a problem with the code. Thanks for the support.</p>
<p>Yeah, you're right that this approach is not yet the best. But first I want to get things running and than it's about improving. I am also using the current planet data, but the documentation is from 2015 though</p>
</div>
<div id="comment-71204-info" class="comment-info">
<span class="comment-age">(16 Oct '19, 14:53)</span> <span class="comment-user userinfo">ulicious</span>
</div>
</div>
</div>
<div id="comment-tools-71201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71201-form-container" class="comment-form-container">
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

