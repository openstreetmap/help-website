+++
type = "question"
title = "How can I fix Osmosis stopping with &quot;Task type write-srtm doesn&#x27;t exist&quot;?"
description = '''Hi, I am using your osmosis-srtm-plugin for my project, but I have encounter some problem, I download the Osmosis from http://wiki.openstreetmap.org/wiki/Osmosis, and put osmosis-srtm-plugin in lib/default, and run the command  osmosis.bat --read-xml map.osm --write-srtm srvBase=http://dds.cr.usgs.g...'''
date = "2013-08-28T12:13:00Z"
lastmod = "2013-08-28T19:39:00Z"
weight = 25894
keywords = [ "development", "osmosis", "osmosis-srtm-plugin" ]
aliases = [ "/questions/25894" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I fix Osmosis stopping with "Task type write-srtm doesn't exist"?](/questions/25894/how-can-i-fix-osmosis-stopping-with-task-type-write-srtm-doesnt-exist)

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
<span id="post-25894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25894-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using your osmosis-srtm-plugin for my project, but I have encounter some problem, I download the Osmosis from <a href="http://wiki.openstreetmap.org/wiki/Osmosis,">http://wiki.openstreetmap.org/wiki/Osmosis,</a> and put osmosis-srtm-plugin in lib/default, and run the command osmosis.bat --read-xml map.osm --write-srtm srvBase=<a href="http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/">http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/</a> srvSubDirs=North_America;South_America --write-xml test.osm followed <a href="http://code.google.com/p/osmosis-srtm-plugin/wiki/Examples.">http://code.google.com/p/osmosis-srtm-plugin/wiki/Examples.</a></p>
<p>However, the result is: Aug 28, 2013 3:49:16 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.43.1 Aug 28, 2013 3:49:16 AM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Aug 28, 2013 3:49:16 AM org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: Task type write-srtm doesn't exist. at org.openstreetmap.osmosis.core.pipeline.common.TaskManagerFactoryRegister.getInstance(TaskManagerFactoryRegister.java:60) at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.buildTasks(Pipeline.java:50) at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipeline.java:112) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25) at java.lang.reflect.Method.invoke(Method.java:597) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352) at org.codehaus.classworlds.Launcher.main(Launcher.java:47) -bash: South_America: command not found</p>
<p>Could you please help me with that? Thank you very much.</p>
<p>Best</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-osmosis-srtm-plugin" rel="tag" title="see questions tagged &#39;osmosis-srtm-plugin&#39;">osmosis-srtm-plugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '13, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/2ef9d4ae850eea19bb3da21dd50a031a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="usunyu&#39;s gravatar image" />
<p><span>usunyu</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="usunyu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '13, 15:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-25894" class="comments-container">
<span id="25905"></span>
<div id="comment-25905" class="comment">
<div id="post-25905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want SRTM there are many easier ways to get it, and its best managed in a PostGIS db anyway. For instance, just load SRTM &amp; OSM nodes and then using PostGis queries to assign elevation data to your nodes.</p>
<p>I would not be surprised if this plugin is no longer compatible with Osmosis.</p>
</div>
<div id="comment-25905-info" class="comment-info">
<span class="comment-age">(28 Aug '13, 19:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25894-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

